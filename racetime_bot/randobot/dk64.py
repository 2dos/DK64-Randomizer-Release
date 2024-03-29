"""Main web endpoint API calls for the bot."""

import json
import os
import requests
import time


class DK64:
    """Class for interacting with dk64randomizer.com to generate seeds and available presets."""

    hash_map = {
        0: {"Bongos": 908522167522709545},
        1: {"Crown": 1160363625723199600},
        2: {"RaceCoin": 1160363626645962872},
        3: {"Fairy": 1160363628369817682},
        4: {"Guitar": 908522167338139689},
        5: {"NintendoCoin": 1160363629422592111},
        6: {"Orange": 1160363630638936074},
        7: {"RainbowCoin": 1160363632337625098},
        8: {"RarewareCoin": 1160363633314893865},
        9: {"Saxophone": 908522167296208956},
    }

    def __init__(self):
        """Initialize the API class."""
        if os.environ.get("DEV_SERVER", False):
            self.seed_url = "https://dev.dk64randomizer.com/randomizer?seed_id=%s"
            self.seed_endpoint = "https://dev-generate.dk64rando.com/generate"
            self.json_converter = "https://dev-generate.dk64rando.com/convert_settings_string"
            self.preset_endpoint = "https://dev-generate.dk64rando.com/get_presets"
            self.data_endpoint = "https://dev-generate.dk64rando.com/get_seed_data"
            self.status_endpoint = "https://dev-generate.dk64rando.com/status"
        else:
            self.seed_url = "https://dk64randomizer.com/randomizer?seed_id=%s"
            self.seed_endpoint = "https://generate.dk64rando.com/generate"
            self.json_converter = "https://generate.dk64rando.com/convert_settings_string"
            self.preset_endpoint = "https://generate.dk64rando.com/get_presets"
            self.data_endpoint = "https://generate.dk64rando.com/get_seed_data"
            self.status_endpoint = "https://generate.dk64rando.com/status"
        self.discord_webhook = os.environ.get("DISCORD_WEBHOOK", None)
        self.presets = self.load_presets()

    def load_presets(self):
        """Load and return available seed presets."""
        presets = requests.get(self.preset_endpoint).json()
        # turn the presets into a dict of name being the key with the settings_string as the value
        presets_dict = {}
        for preset in presets:
            presets_dict[preset["name"].lower()] = preset
        return presets_dict

    def roll_seed(self, preset, race):
        """Generate a seed and return its public URL."""
        # Roll with provided preset for non-draft races.
        if preset is not None:
            converted_settings = requests.post(
                self.json_converter,
                json.dumps({"settings_string": self.presets[preset]["settings_string"]}),
                headers={"Content-Type": "application/json"},
            ).json()
            if race:
                converted_settings["generate_spoilerlog"] = False
            req_body = {"post_body": json.dumps(converted_settings)}
            data = requests.post(
                self.seed_endpoint,
                headers={"Content-Type": "application/json"},
                params={"gen_key": time.time()},
                json=req_body,
            ).json()
            data["id"] = data["start_time"]
            return data["start_time"]
        return None, None

    def get_status(self, seed_id):
        """Get the status of a seed."""
        data = requests.get(
            self.status_endpoint,
            params={
                "gen_key": seed_id,
            },
        )
        if data.status_code == 200 and data.json()["status"] in ["failure", "stopped", "error"]:
            return 2
        elif data.status_code == 200 and data.json()["status"] == "ready":
            return 1
        else:
            return 0

    def get_hash(self, seed_id):
        """Get the hash for a seed."""
        data = requests.get(
            self.data_endpoint,
            params={
                "gen_key": seed_id,
            },
        ).json()
        if data.get("status") == "complete":
            return (
                " ".join([next(iter(self.hash_map.get(index, {}).keys()), next(iter(self.hash_map.values()))) for index in data["hash"]]),
                data.get("seed_number"),
                self.seed_url,
            )
        return None, None, None
