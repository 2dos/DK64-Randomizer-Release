"""Stores the item class and a list of each item with its attributes."""

from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional, Union

from randomizer.Enums.Items import Items
from randomizer.Enums.Kongs import Kongs
from randomizer.Enums.Levels import Levels
from randomizer.Enums.MoveTypes import MoveTypes
from randomizer.Enums.Types import Types


class Item:
    """Stores information about an item."""

    def __init__(
        self,
        name: str,
        playthrough: bool,
        type: Types,
        kong: Kongs,
        data: Optional[Union[List[Union[MoveTypes, int]], List[Union[MoveTypes, str, int]], List[Levels], List[int]]] = None,
    ) -> None:
        """Initialize with given parameters."""
        if data is None:
            data = []
        self.name = name
        self.playthrough = playthrough
        self.type = type
        self.kong = kong
        self.movetype = None
        self.rando_flag = None  # The flag the ROM reads to know if you have this item - set to -1 for progressive moves as those are special
        if type == Types.Shop:
            self.movetype = data[0]
            self.index = data[1]
            self.rando_flag = data[2]
        if type in (Types.TrainingBarrel, Types.Shockwave, Types.Climbing):
            self.movetype = data[0]
            self.flag = data[1]
            self.rando_flag = data[2]
        if type == Types.Key:
            self.rando_flag = data[0]
            self.index = data[1]  # Key 1 = 1, Key 2 = 2, etc
        if type == Types.Kong:
            self.rando_flag = data[0]
        if type == Types.Hint:
            self.level = data[0]
            self.rando_flag = 0x384 + (self.level * 5) + self.kong
        if type in (Types.NintendoCoin, Types.RarewareCoin):
            self.flag = data[0]


def ItemFromKong(kong: Kongs) -> Items:
    """Get the item representation of a Kong enum."""
    if kong == Kongs.donkey:
        return Items.Donkey
    elif kong == Kongs.diddy:
        return Items.Diddy
    elif kong == Kongs.lanky:
        return Items.Lanky
    elif kong == Kongs.tiny:
        return Items.Tiny
    elif kong == Kongs.chunky:
        return Items.Chunky
    else:
        return Items.NoItem


def NameFromKong(kong: Kongs) -> str:
    """Get the name of a kong from its Kong enum value."""
    if kong == Kongs.donkey:
        return "Donkey"
    elif kong == Kongs.diddy:
        return "Diddy"
    elif kong == Kongs.lanky:
        return "Lanky"
    elif kong == Kongs.tiny:
        return "Tiny"
    elif kong == Kongs.chunky:
        return "Chunky"
    else:
        return "No Kong"


def KongFromItem(item: Items) -> Kongs:
    """Get the Kong enum representation of a kong item."""
    if item == Items.Donkey:
        return Kongs.donkey
    elif item == Items.Diddy:
        return Kongs.diddy
    elif item == Items.Lanky:
        return Kongs.lanky
    elif item == Items.Tiny:
        return Kongs.tiny
    elif item == Items.Chunky:
        return Kongs.chunky
    else:
        return Kongs.any


ItemList = {
    Items.NoItem: Item("No Item", False, Types.Constant, Kongs.any),
    Items.TestItem: Item("Fill Helper Item - SHOULD NOT BE PLACED", False, Types.Constant, Kongs.any),
    Items.Donkey: Item("Donkey", True, Types.Kong, Kongs.any, [385]),
    Items.Diddy: Item("Diddy", True, Types.Kong, Kongs.any, [6]),
    Items.Lanky: Item("Lanky", True, Types.Kong, Kongs.any, [70]),
    Items.Tiny: Item("Tiny", True, Types.Kong, Kongs.any, [66]),
    Items.Chunky: Item("Chunky", True, Types.Kong, Kongs.any, [117]),
    Items.Vines: Item("Vines", True, Types.TrainingBarrel, Kongs.any, [MoveTypes.Flag, "vine", 387]),
    Items.Swim: Item("Diving", True, Types.TrainingBarrel, Kongs.any, [MoveTypes.Flag, "dive", 386]),
    Items.Oranges: Item("Oranges", True, Types.TrainingBarrel, Kongs.any, [MoveTypes.Flag, "orange", 388]),
    Items.Barrels: Item("Barrels", True, Types.TrainingBarrel, Kongs.any, [MoveTypes.Flag, "barrel", 389]),
    Items.Climbing: Item("Climbing", True, Types.Climbing, Kongs.any, [MoveTypes.Flag, "climbing", 0x297]),
    Items.ProgressiveSlam: Item("Progressive Slam", True, Types.Shop, Kongs.any, [MoveTypes.Slam, 2, -1]),
    Items.ProgressiveSlam2: Item("Progressive Slam ", False, Types.Constant, Kongs.any),  # Only used for the starting move list selector modal
    Items.ProgressiveSlam3: Item("Progressive Slam  ", False, Types.Constant, Kongs.any),  # Only used for the starting move list selector modal
    Items.ProgressiveDonkeyPotion: Item("Progressive Donkey Potion", True, Types.Shop, Kongs.donkey, [MoveTypes.Moves, 1, -1]),
    Items.BaboonBlast: Item("Baboon Blast", True, Types.Shop, Kongs.donkey, [MoveTypes.Moves, 1, 0x8001]),
    Items.StrongKong: Item("Strong Kong", True, Types.Shop, Kongs.donkey, [MoveTypes.Moves, 2, 0x8002]),
    Items.GorillaGrab: Item("Gorilla Grab", True, Types.Shop, Kongs.donkey, [MoveTypes.Moves, 3, 0x8003]),
    Items.ProgressiveDiddyPotion: Item("Progressive Diddy Potion", True, Types.Shop, Kongs.diddy, [MoveTypes.Moves, 1, -1]),
    Items.ChimpyCharge: Item("Chimpy Charge", True, Types.Shop, Kongs.diddy, [MoveTypes.Moves, 1, 0x9001]),
    Items.RocketbarrelBoost: Item("Rocketbarrel Boost", True, Types.Shop, Kongs.diddy, [MoveTypes.Moves, 2, 0x9002]),
    Items.SimianSpring: Item("Simian Spring", True, Types.Shop, Kongs.diddy, [MoveTypes.Moves, 3, 0x9003]),
    Items.ProgressiveLankyPotion: Item("Progressive Lanky Potion", True, Types.Shop, Kongs.lanky, [MoveTypes.Moves, 1, -1]),
    Items.Orangstand: Item("Orangstand", True, Types.Shop, Kongs.lanky, [MoveTypes.Moves, 1, 0xA001]),
    Items.BaboonBalloon: Item("Baboon Balloon", True, Types.Shop, Kongs.lanky, [MoveTypes.Moves, 2, 0xA002]),
    Items.OrangstandSprint: Item("Orangstand Sprint", True, Types.Shop, Kongs.lanky, [MoveTypes.Moves, 3, 0xA003]),
    Items.ProgressiveTinyPotion: Item("Progressive Tiny Potion", True, Types.Shop, Kongs.tiny, [MoveTypes.Moves, 1, -1]),
    Items.MiniMonkey: Item("Mini Monkey", True, Types.Shop, Kongs.tiny, [MoveTypes.Moves, 1, 0xB001]),
    Items.PonyTailTwirl: Item("Pony Tail Twirl", True, Types.Shop, Kongs.tiny, [MoveTypes.Moves, 2, 0xB002]),
    Items.Monkeyport: Item("Monkeyport", True, Types.Shop, Kongs.tiny, [MoveTypes.Moves, 3, 0xB003]),
    Items.ProgressiveChunkyPotion: Item("Progressive Chunky Potion", True, Types.Shop, Kongs.chunky, [MoveTypes.Moves, 1, -1]),
    Items.HunkyChunky: Item("Hunky Chunky", True, Types.Shop, Kongs.chunky, [MoveTypes.Moves, 1, 0xC001]),
    Items.PrimatePunch: Item("Primate Punch", True, Types.Shop, Kongs.chunky, [MoveTypes.Moves, 2, 0xC002]),
    Items.GorillaGone: Item("Gorilla Gone", True, Types.Shop, Kongs.chunky, [MoveTypes.Moves, 3, 0xC003]),
    Items.Coconut: Item("Coconut", True, Types.Shop, Kongs.donkey, [MoveTypes.Guns, 1, 0x8201]),
    Items.Peanut: Item("Peanut", True, Types.Shop, Kongs.diddy, [MoveTypes.Guns, 1, 0x9201]),
    Items.Grape: Item("Grape", True, Types.Shop, Kongs.lanky, [MoveTypes.Guns, 1, 0xA201]),
    Items.Feather: Item("Feather", True, Types.Shop, Kongs.tiny, [MoveTypes.Guns, 1, 0xB201]),
    Items.Pineapple: Item("Pineapple", True, Types.Shop, Kongs.chunky, [MoveTypes.Guns, 1, 0xC201]),
    Items.HomingAmmo: Item("Homing Ammo", True, Types.Shop, Kongs.any, [MoveTypes.Guns, 2, 0xD202]),
    Items.SniperSight: Item("Sniper Sight", True, Types.Shop, Kongs.any, [MoveTypes.Guns, 3, 0xD203]),
    Items.ProgressiveAmmoBelt: Item("Progressive Ammo Belt", False, Types.Shop, Kongs.any, [MoveTypes.AmmoBelt, 1, -1]),
    Items.ProgressiveAmmoBelt2: Item("Progressive Ammo Belt ", False, Types.Constant, Kongs.any),  # Only used for the starting move list selector modal
    Items.Bongos: Item("Bongos", True, Types.Shop, Kongs.donkey, [MoveTypes.Instruments, 1, 0x8401]),
    Items.Guitar: Item("Guitar", True, Types.Shop, Kongs.diddy, [MoveTypes.Instruments, 1, 0x9401]),
    Items.Trombone: Item("Trombone", True, Types.Shop, Kongs.lanky, [MoveTypes.Instruments, 1, 0xA401]),
    Items.Saxophone: Item("Saxophone", True, Types.Shop, Kongs.tiny, [MoveTypes.Instruments, 1, 0xB401]),
    Items.Triangle: Item("Triangle", True, Types.Shop, Kongs.chunky, [MoveTypes.Instruments, 1, 0xC401]),
    Items.ProgressiveInstrumentUpgrade: Item("Progressive Instrument Upgrade", False, Types.Shop, Kongs.any, [MoveTypes.Instruments, 2, -1]),
    Items.ProgressiveInstrumentUpgrade2: Item("Progressive Instrument Upgrade ", False, Types.Constant, Kongs.any),  # Only used for the starting move list selector modal
    Items.ProgressiveInstrumentUpgrade3: Item("Progressive Instrument Upgrade  ", False, Types.Constant, Kongs.any),  # Only used for the starting move list selector modal
    Items.Camera: Item("Fairy Camera", True, Types.Shockwave, Kongs.any, [MoveTypes.Flag, "camera", 0x2FD]),
    Items.Shockwave: Item("Shockwave", True, Types.Shockwave, Kongs.any, [MoveTypes.Flag, "shockwave", 377]),
    Items.CameraAndShockwave: Item(
        "Camera and Shockwave", True, Types.Shockwave, Kongs.any, [MoveTypes.Flag, "camera_shockwave", -2]
    ),  # -2 means do not use this rando_flag outside of full item rando
    Items.NintendoCoin: Item("Nintendo Coin", True, Types.NintendoCoin, Kongs.any, [132]),
    Items.RarewareCoin: Item("Rareware Coin", True, Types.RarewareCoin, Kongs.any, [379]),
    Items.JungleJapesKey: Item("Key 1", True, Types.Key, Kongs.any, [26, 1]),
    Items.AngryAztecKey: Item("Key 2", True, Types.Key, Kongs.any, [74, 2]),
    Items.FranticFactoryKey: Item("Key 3", True, Types.Key, Kongs.any, [138, 3]),
    Items.GloomyGalleonKey: Item("Key 4", True, Types.Key, Kongs.any, [168, 4]),
    Items.FungiForestKey: Item("Key 5", True, Types.Key, Kongs.any, [236, 5]),
    Items.CrystalCavesKey: Item("Key 6", True, Types.Key, Kongs.any, [292, 6]),
    Items.CreepyCastleKey: Item("Key 7", True, Types.Key, Kongs.any, [317, 7]),
    Items.HideoutHelmKey: Item("Key 8", True, Types.Key, Kongs.any, [380, 8]),
    Items.HelmDonkey1: Item("Helm Donkey Barrel 1", False, Types.Constant, Kongs.donkey),
    Items.HelmDonkey2: Item("Helm Donkey Barrel 2", False, Types.Constant, Kongs.donkey),
    Items.HelmDiddy1: Item("Helm Diddy Barrel 1", False, Types.Constant, Kongs.diddy),
    Items.HelmDiddy2: Item("Helm Diddy Barrel 2", False, Types.Constant, Kongs.diddy),
    Items.HelmLanky1: Item("Helm Lanky Barrel 1", False, Types.Constant, Kongs.lanky),
    Items.HelmLanky2: Item("Helm Lanky Barrel 2", False, Types.Constant, Kongs.lanky),
    Items.HelmTiny1: Item("Helm Tiny Barrel 1", False, Types.Constant, Kongs.tiny),
    Items.HelmTiny2: Item("Helm Tiny Barrel 2", False, Types.Constant, Kongs.tiny),
    Items.HelmChunky1: Item("Helm Chunky Barrel 1", False, Types.Constant, Kongs.chunky),
    Items.HelmChunky2: Item("Helm Chunky Barrel 2", False, Types.Constant, Kongs.chunky),
    Items.GoldenBanana: Item("Golden Banana", True, Types.Banana, Kongs.any),
    Items.BananaFairy: Item("Banana Fairy", False, Types.Fairy, Kongs.any),
    Items.BananaMedal: Item("Banana Medal", False, Types.Medal, Kongs.any),
    Items.BattleCrown: Item("Battle Crown", False, Types.Crown, Kongs.any),
    Items.Bean: Item("The Bean", False, Types.Bean, Kongs.any),
    Items.Pearl: Item("Pearl", False, Types.Pearl, Kongs.any),
    Items.RainbowCoin: Item("Rainbow Coin", False, Types.RainbowCoin, Kongs.any),
    Items.IceTrapBubble: Item("Ice Trap (Bubble)", False, Types.FakeItem, Kongs.any),
    Items.IceTrapReverse: Item("Ice Trap (Reverse)", False, Types.FakeItem, Kongs.any),
    Items.IceTrapSlow: Item("Ice Trap (Slow)", False, Types.FakeItem, Kongs.any),
    Items.JunkCrystal: Item("Junk Item (Crystal)", False, Types.JunkItem, Kongs.any),
    Items.JunkMelon: Item("Junk Item (Melon Slice)", False, Types.JunkItem, Kongs.any),
    Items.JunkAmmo: Item("Junk Item (Ammo Crate)", False, Types.JunkItem, Kongs.any),
    Items.JunkFilm: Item("Junk Item (Film)", False, Types.JunkItem, Kongs.any),
    Items.JunkOrange: Item("Junk Item (Orange)", False, Types.JunkItem, Kongs.any),
    Items.CrateMelon: Item("Crate Melon", False, Types.CrateItem, Kongs.any),
    Items.EnemyItem: Item("Enemy Item", False, Types.Enemies, Kongs.any),
    Items.Cranky: Item("Cranky", True, Types.Cranky, Kongs.any),
    Items.Funky: Item("Funky", True, Types.Funky, Kongs.any),
    Items.Candy: Item("Candy", True, Types.Candy, Kongs.any),
    Items.Snide: Item("Snide", True, Types.Snide, Kongs.any),
    Items.DKIslesDonkeyBlueprint: Item("DK Isles Donkey Blueprint", False, Types.Blueprint, Kongs.donkey),
    Items.DKIslesDiddyBlueprint: Item("DK Isles Diddy Blueprint", False, Types.Blueprint, Kongs.diddy),
    Items.DKIslesLankyBlueprint: Item("DK Isles Lanky Blueprint", False, Types.Blueprint, Kongs.lanky),
    Items.DKIslesTinyBlueprint: Item("DK Isles Tiny Blueprint", False, Types.Blueprint, Kongs.tiny),
    Items.DKIslesChunkyBlueprint: Item("DK Isles Chunky Blueprint", False, Types.Blueprint, Kongs.chunky),
    Items.JungleJapesDonkeyBlueprint: Item("Jungle Japes Donkey Blueprint", False, Types.Blueprint, Kongs.donkey),
    Items.JungleJapesDiddyBlueprint: Item("Jungle Japes Diddy Blueprint", False, Types.Blueprint, Kongs.diddy),
    Items.JungleJapesLankyBlueprint: Item("Jungle Japes Lanky Blueprint", False, Types.Blueprint, Kongs.lanky),
    Items.JungleJapesTinyBlueprint: Item("Jungle Japes Tiny Blueprint", False, Types.Blueprint, Kongs.tiny),
    Items.JungleJapesChunkyBlueprint: Item("Jungle Japes Chunky Blueprint", False, Types.Blueprint, Kongs.chunky),
    Items.AngryAztecDonkeyBlueprint: Item("Angry Aztec Donkey Blueprint", False, Types.Blueprint, Kongs.donkey),
    Items.AngryAztecDiddyBlueprint: Item("Angry Aztec Diddy Blueprint", False, Types.Blueprint, Kongs.diddy),
    Items.AngryAztecLankyBlueprint: Item("Angry Aztec Lanky Blueprint", False, Types.Blueprint, Kongs.lanky),
    Items.AngryAztecTinyBlueprint: Item("Angry Aztec Tiny Blueprint", False, Types.Blueprint, Kongs.tiny),
    Items.AngryAztecChunkyBlueprint: Item("Angry Aztec Chunky Blueprint", False, Types.Blueprint, Kongs.chunky),
    Items.FranticFactoryDonkeyBlueprint: Item("Frantic Factory Donkey Blueprint", False, Types.Blueprint, Kongs.donkey),
    Items.FranticFactoryDiddyBlueprint: Item("Frantic Factory Diddy Blueprint", False, Types.Blueprint, Kongs.diddy),
    Items.FranticFactoryLankyBlueprint: Item("Frantic Factory Lanky Blueprint", False, Types.Blueprint, Kongs.lanky),
    Items.FranticFactoryTinyBlueprint: Item("Frantic Factory Tiny Blueprint", False, Types.Blueprint, Kongs.tiny),
    Items.FranticFactoryChunkyBlueprint: Item("Frantic Factory Chunky Blueprint", False, Types.Blueprint, Kongs.chunky),
    Items.GloomyGalleonDonkeyBlueprint: Item("Gloomy Galleon Donkey Blueprint", False, Types.Blueprint, Kongs.donkey),
    Items.GloomyGalleonDiddyBlueprint: Item("Gloomy Galleon Diddy Blueprint", False, Types.Blueprint, Kongs.diddy),
    Items.GloomyGalleonLankyBlueprint: Item("Gloomy Galleon Lanky Blueprint", False, Types.Blueprint, Kongs.lanky),
    Items.GloomyGalleonTinyBlueprint: Item("Gloomy Galleon Tiny Blueprint", False, Types.Blueprint, Kongs.tiny),
    Items.GloomyGalleonChunkyBlueprint: Item("Gloomy Galleon Chunky Blueprint", False, Types.Blueprint, Kongs.chunky),
    Items.FungiForestDonkeyBlueprint: Item("Fungi Forest Donkey Blueprint", False, Types.Blueprint, Kongs.donkey),
    Items.FungiForestDiddyBlueprint: Item("Fungi Forest Diddy Blueprint", False, Types.Blueprint, Kongs.diddy),
    Items.FungiForestLankyBlueprint: Item("Fungi Forest Lanky Blueprint", False, Types.Blueprint, Kongs.lanky),
    Items.FungiForestTinyBlueprint: Item("Fungi Forest Tiny Blueprint", False, Types.Blueprint, Kongs.tiny),
    Items.FungiForestChunkyBlueprint: Item("Fungi Forest Chunky Blueprint", False, Types.Blueprint, Kongs.chunky),
    Items.CrystalCavesDonkeyBlueprint: Item("Crystal Caves Donkey Blueprint", False, Types.Blueprint, Kongs.donkey),
    Items.CrystalCavesDiddyBlueprint: Item("Crystal Caves Diddy Blueprint", False, Types.Blueprint, Kongs.diddy),
    Items.CrystalCavesLankyBlueprint: Item("Crystal Caves Lanky Blueprint", False, Types.Blueprint, Kongs.lanky),
    Items.CrystalCavesTinyBlueprint: Item("Crystal Caves Tiny Blueprint", False, Types.Blueprint, Kongs.tiny),
    Items.CrystalCavesChunkyBlueprint: Item("Crystal Caves Chunky Blueprint", False, Types.Blueprint, Kongs.chunky),
    Items.CreepyCastleDonkeyBlueprint: Item("Creepy Castle Donkey Blueprint", False, Types.Blueprint, Kongs.donkey),
    Items.CreepyCastleDiddyBlueprint: Item("Creepy Castle Diddy Blueprint", False, Types.Blueprint, Kongs.diddy),
    Items.CreepyCastleLankyBlueprint: Item("Creepy Castle Lanky Blueprint", False, Types.Blueprint, Kongs.lanky),
    Items.CreepyCastleTinyBlueprint: Item("Creepy Castle Tiny Blueprint", False, Types.Blueprint, Kongs.tiny),
    Items.CreepyCastleChunkyBlueprint: Item("Creepy Castle Chunky Blueprint", False, Types.Blueprint, Kongs.chunky),
    Items.JapesDonkeyHint: Item("Japes Donkey Hint", False, Types.Hint, Kongs.donkey, [Levels.JungleJapes]),
    Items.JapesDiddyHint: Item("Japes Diddy Hint", False, Types.Hint, Kongs.diddy, [Levels.JungleJapes]),
    Items.JapesLankyHint: Item("Japes Lanky Hint", False, Types.Hint, Kongs.lanky, [Levels.JungleJapes]),
    Items.JapesTinyHint: Item("Japes Tiny Hint", False, Types.Hint, Kongs.tiny, [Levels.JungleJapes]),
    Items.JapesChunkyHint: Item("Japes Chunky Hint", False, Types.Hint, Kongs.chunky, [Levels.JungleJapes]),
    Items.AztecDonkeyHint: Item("Aztec Donkey Hint", False, Types.Hint, Kongs.donkey, [Levels.AngryAztec]),
    Items.AztecDiddyHint: Item("Aztec Diddy Hint", False, Types.Hint, Kongs.diddy, [Levels.AngryAztec]),
    Items.AztecLankyHint: Item("Aztec Lanky Hint", False, Types.Hint, Kongs.lanky, [Levels.AngryAztec]),
    Items.AztecTinyHint: Item("Aztec Tiny Hint", False, Types.Hint, Kongs.tiny, [Levels.AngryAztec]),
    Items.AztecChunkyHint: Item("Aztec Chunky Hint", False, Types.Hint, Kongs.chunky, [Levels.AngryAztec]),
    Items.FactoryDonkeyHint: Item("Factory Donkey Hint", False, Types.Hint, Kongs.donkey, [Levels.FranticFactory]),
    Items.FactoryDiddyHint: Item("Factory Diddy Hint", False, Types.Hint, Kongs.diddy, [Levels.FranticFactory]),
    Items.FactoryLankyHint: Item("Factory Lanky Hint", False, Types.Hint, Kongs.lanky, [Levels.FranticFactory]),
    Items.FactoryTinyHint: Item("Factory Tiny Hint", False, Types.Hint, Kongs.tiny, [Levels.FranticFactory]),
    Items.FactoryChunkyHint: Item("Factory Chunky Hint", False, Types.Hint, Kongs.chunky, [Levels.FranticFactory]),
    Items.GalleonDonkeyHint: Item("Galleon Donkey Hint", False, Types.Hint, Kongs.donkey, [Levels.GloomyGalleon]),
    Items.GalleonDiddyHint: Item("Galleon Diddy Hint", False, Types.Hint, Kongs.diddy, [Levels.GloomyGalleon]),
    Items.GalleonLankyHint: Item("Galleon Lanky Hint", False, Types.Hint, Kongs.lanky, [Levels.GloomyGalleon]),
    Items.GalleonTinyHint: Item("Galleon Tiny Hint", False, Types.Hint, Kongs.tiny, [Levels.GloomyGalleon]),
    Items.GalleonChunkyHint: Item("Galleon Chunky Hint", False, Types.Hint, Kongs.chunky, [Levels.GloomyGalleon]),
    Items.ForestDonkeyHint: Item("Forest Donkey Hint", False, Types.Hint, Kongs.donkey, [Levels.FungiForest]),
    Items.ForestDiddyHint: Item("Forest Diddy Hint", False, Types.Hint, Kongs.diddy, [Levels.FungiForest]),
    Items.ForestLankyHint: Item("Forest Lanky Hint", False, Types.Hint, Kongs.lanky, [Levels.FungiForest]),
    Items.ForestTinyHint: Item("Forest Tiny Hint", False, Types.Hint, Kongs.tiny, [Levels.FungiForest]),
    Items.ForestChunkyHint: Item("Forest Chunky Hint", False, Types.Hint, Kongs.chunky, [Levels.FungiForest]),
    Items.CavesDonkeyHint: Item("Caves Donkey Hint", False, Types.Hint, Kongs.donkey, [Levels.CrystalCaves]),
    Items.CavesDiddyHint: Item("Caves Diddy Hint", False, Types.Hint, Kongs.diddy, [Levels.CrystalCaves]),
    Items.CavesLankyHint: Item("Caves Lanky Hint", False, Types.Hint, Kongs.lanky, [Levels.CrystalCaves]),
    Items.CavesTinyHint: Item("Caves Tiny Hint", False, Types.Hint, Kongs.tiny, [Levels.CrystalCaves]),
    Items.CavesChunkyHint: Item("Caves Chunky Hint", False, Types.Hint, Kongs.chunky, [Levels.CrystalCaves]),
    Items.CastleDonkeyHint: Item("Castle Donkey Hint", False, Types.Hint, Kongs.donkey, [Levels.CreepyCastle]),
    Items.CastleDiddyHint: Item("Castle Diddy Hint", False, Types.Hint, Kongs.diddy, [Levels.CreepyCastle]),
    Items.CastleLankyHint: Item("Castle Lanky Hint", False, Types.Hint, Kongs.lanky, [Levels.CreepyCastle]),
    Items.CastleTinyHint: Item("Castle Tiny Hint", False, Types.Hint, Kongs.tiny, [Levels.CreepyCastle]),
    Items.CastleChunkyHint: Item("Castle Chunky Hint", False, Types.Hint, Kongs.chunky, [Levels.CreepyCastle]),
    Items.ArchipelagoItem: Item("Archipelago Item", False, Types.ArchipelagoItem, Kongs.any),
    Items.BananaHoard: Item("Banana Hoard", True, Types.Constant, Kongs.any),
}

HHItemSelector = []
HHItems = [
    ("Starting Time", 20 * 60),
    ("Golden Banana", 20),
    ("Blueprint", 45),
    ("Company Coins", 300),
    ("Move", 30),
    ("Banana Medal", 60),
    ("Rainbow Coin", 15),
    ("Boss Key", 150),
    ("Battle Crown", 90),
    ("Bean", 120),
    ("Pearl", 50),
    ("Kongs", 240),
    ("Fairies", 50),
    ("Colored Bananas", 3),
    ("Ice Traps", -40),
]
for item in HHItems:
    HHItemSelector.append({"name": item[0], "value": item[0].lower().replace(" ", "_"), "tooltip": "", "default": item[1]})

CustomStartingMoveSelector = []
StartingMoveOptions = [
    Items.Vines,
    Items.Swim,
    Items.Oranges,
    Items.Barrels,
    Items.Climbing,
    Items.ProgressiveSlam,
    Items.ProgressiveSlam2,
    Items.ProgressiveSlam3,
    Items.Coconut,
    Items.Bongos,
    Items.BaboonBlast,
    Items.StrongKong,
    Items.GorillaGrab,
    Items.Peanut,
    Items.Guitar,
    Items.ChimpyCharge,
    Items.RocketbarrelBoost,
    Items.SimianSpring,
    Items.Grape,
    Items.Trombone,
    Items.Orangstand,
    Items.BaboonBalloon,
    Items.OrangstandSprint,
    Items.Feather,
    Items.Saxophone,
    Items.MiniMonkey,
    Items.PonyTailTwirl,
    Items.Monkeyport,
    Items.Pineapple,
    Items.Triangle,
    Items.HunkyChunky,
    Items.PrimatePunch,
    Items.GorillaGone,
    Items.HomingAmmo,
    Items.SniperSight,
    Items.ProgressiveAmmoBelt,
    Items.ProgressiveAmmoBelt2,
    Items.ProgressiveInstrumentUpgrade,
    Items.ProgressiveInstrumentUpgrade2,
    Items.ProgressiveInstrumentUpgrade3,
    Items.Cranky,
    Items.Funky,
    Items.Candy,
    Items.Snide,
    Items.Camera,
    Items.Shockwave,
]

for item in StartingMoveOptions:
    CustomStartingMoveSelector.append({"name": ItemList[item].name, "value": item.value, "tooltip": "", "state": 0})
