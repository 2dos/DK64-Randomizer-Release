typedef enum console {
    NONE,
    N64,
    WIIU,
    EMULATOR,
} console;

typedef enum data_indexes {
	TABLE_MUSIC_MIDI,
	TABLE_MAP_GEOMETRY,
	TABLE_MAP_WALLS,
	TABLE_MAP_FLOORS,
	TABLE_MODELTWO_GEOMETRY,
	TABLE_ACTOR_GEOMETRY,
	TABLE_UNK06,
	TABLE_TEXTURES_UNCOMPRESSED,
	TABLE_CUTSCENES,
	TABLE_MAP_SETUPS,
	TABLE_MAP_OBJECT_SCRIPTS,
	TABLE_ANIMATIONS,
	TABLE_TEXT,
	TABLE_UNK0D,
	TABLE_TEXTURES,
	TABLE_MAP_PATHS,
	TABLE_MAP_CHARACTER_SPAWNERS,
	TABLE_UNK11,
	TABLE_MAP_LOADING_ZONES,
	TABLE_UNK13,
	TABLE_UNK14,
	TABLE_MAP_AUTOWALKS,
	TABLE_UNK16,
	TABLE_MAP_EXITS,
	TABLE_MAP_RACE_CHECKPOINTS,
	TABLE_TEXTURES_2,
	TABLE_UNCOMPRESSED_FILE_SIZES,
	TABLE_UNK1B,
	TABLE_UNK1C,
	TABLE_UNK1D,
	TABLE_UNK1E,
	TABLE_UNK1F,
	TABLE_UNK20,
} data_indexes;

typedef enum load_modes {
	SAVESTATE,
	MAPWARP,
} load_modes;

typedef enum codecs {
    IA4,
    IA8,
    RGBA16,
    RGBA32,
} codecs;

typedef enum collision_types {
	/* 0x000 */ COLLISION_BBLAST,
	/* 0x001 */ COLLISION_UNKNOWN_1,
	/* 0x002 */ COLLISION_SIMIAN_SPRING,
	/* 0x003 */ COLLISION_MONKEYPORT_WARP,
	/* 0x004 */ COLLISION_GORILLA_GONE,
	/* 0x005 */ COLLISION_BANANAPORT,
	/* 0x006 */ COLLISION_BABOON_BALLOON,
	/* 0x007 */ COLLISION_BATTLE_CROWN,
	/* 0x008 */ COLLISION_UNKNOWN_8,
	/* 0x009 */ COLLISION_MULTI_BANANAPORT,
	/* 0x00A */ COLLISION_MAPWARP,
} collision_types;

typedef enum location_list {
	/* 0x000 */ LOCATION_DIVE,
	/* 0x001 */ LOCATION_ORANGE,
	/* 0x002 */ LOCATION_BARREL,
	/* 0x003 */ LOCATION_VINE,
	/* 0x004 */ LOCATION_BFI
} location_list;

typedef enum helm_hurry_items {
	/* 0x000 */ HHITEM_NOTHING,
	/* 0x001 */ HHITEM_GB,
	/* 0x002 */ HHITEM_BLUEPRINT,
	/* 0x003 */ HHITEM_COMPANYCOIN,
	/* 0x004 */ HHITEM_MOVE,
	/* 0x005 */ HHITEM_MEDAL,
	/* 0x006 */ HHITEM_RAINBOWCOIN,
	/* 0x007 */ HHITEM_KEY,
	/* 0x008 */ HHITEM_CROWN,
	/* 0x009 */ HHITEM_BEAN,
	/* 0x00A */ HHITEM_PEARL,
	/* 0x00B */ HHITEM_KONG,
	/* 0x00C */ HHITEM_FAIRY,
	/* 0x00D */ HHITEM_CB,
	/* 0x00E */ HHITEM_FAKEITEM,
} helm_hurry_items;

typedef enum purchase_classification {
	/* 0x000 */ PCLASS_NOTHING,
	/* 0x001 */ PCLASS_MOVE,
	/* 0x002 */ PCLASS_INSTRUMENT,
	/* 0x003 */ PCLASS_GUN,
	/* 0x004 */ PCLASS_CAMERA,
	/* 0x005 */ PCLASS_SHOCKWAVE,
	/* 0x006 */ PCLASS_CAMSHOCK,
	/* 0x007 */ PCLASS_GB,
	/* 0x008 */ PCLASS_BLUEPRINT,
	/* 0x009 */ PCLASS_COMPANYCOIN,
	/* 0x00A */ PCLASS_MEDAL,
	/* 0x00B */ PCLASS_RAINBOWCOIN,
	/* 0x00C */ PCLASS_KEY,
	/* 0x00D */ PCLASS_CROWN,
	/* 0x00E */ PCLASS_BEAN,
	/* 0x00F */ PCLASS_PEARL,
	/* 0x010 */ PCLASS_KONG,
	/* 0x011 */ PCLASS_FAIRY,
	/* 0x012 */ PCLASS_FAKEITEM,
} purchase_classification;

typedef enum pad_refresh_signals {
    /* 0x000 */ ITEMREFRESH_BLAST,
    /* 0x001 */ ITEMREFRESH_SPRING,
    /* 0x002 */ ITEMREFRESH_BALLOON,
    /* 0x003 */ ITEMREFRESH_MONKEYPORT,
    /* 0x004 */ ITEMREFRESH_GONE,
	/* 0x005 */ ITEMREFRESH_VINE,
} pad_refresh_signals;

typedef enum moverando_hinttext {
	/* 0x000 */ MRT_CANBUY_BBLAST,
	/* 0x001 */ MRT_CANBUY_SKONG,
	/* 0x002 */ MRT_CANBUY_GGRAB,
	/* 0x003 */ MRT_CANBUY_CCHARGE,
	/* 0x004 */ MRT_CANBUY_RBARREL,
	/* 0x005 */ MRT_CANBUY_SSPRING,
	/* 0x006 */ MRT_CANBUY_OSTAND,
	/* 0x007 */ MRT_CANBUY_BBALLOON,
	/* 0x008 */ MRT_CANBUY_OSPRINT,
	/* 0x009 */ MRT_CANBUY_MMONKEY,
	/* 0x00A */ MRT_CANBUY_PTT,
	/* 0x00B */ MRT_CANBUY_MPORT,
	/* 0x00C */ MRT_CANBUY_HCHUNKY,
	/* 0x00D */ MRT_CANBUY_PPUNCH,
	/* 0x00E */ MRT_CANBUY_GGONE,
	/* 0x00F */ MRT_CANBUY_SLAM,
	/* 0x010 */ MRT_CANBUY_COCONUT,
	/* 0x011 */ MRT_CANBUY_PEANUT,
	/* 0x012 */ MRT_CANBUY_GRAPE,
	/* 0x013 */ MRT_CANBUY_FEATHER,
	/* 0x014 */ MRT_CANBUY_PINEAPPLE,
	/* 0x015 */ MRT_CANBUY_HOMING,
	/* 0x016 */ MRT_CANBUY_SNIPER,
	/* 0x017 */ MRT_CANBUY_AMMOBELT,
	/* 0x018 */ MRT_CANBUY_BONGOS,
	/* 0x019 */ MRT_CANBUY_GUITAR,
	/* 0x01A */ MRT_CANBUY_TROMBONE,
	/* 0x01B */ MRT_CANBUY_SAX,
	/* 0x01C */ MRT_CANBUY_TRIANGLE,
	/* 0x01D */ MRT_CANBUY_INSTRUMENTUPGRADE,
	/* 0x01E */ MRT_CANBUY_DIVE,
	/* 0x01F */ MRT_CANBUY_ORANGE,
	/* 0x020 */ MRT_CANBUY_BARREL,
	/* 0x021 */ MRT_CANBUY_VINE,
	/* 0x022 */ MRT_CANBUY_CAMERA,
	/* 0x023 */ MRT_CANBUY_SHOCKWAVE,
	/* 0x024 */ MRT_CANBUY_CAMERACOMBO,
	/* 0x025 */ MRT_CANBUY_BANANA,
	/* 0x026 */ MRT_CANBUY_CROWN,
	/* 0x027 */ MRT_CANBUY_MEDAL,
	/* 0x028 */ MRT_CANBUY_KEY,
	/* 0x029 */ MRT_CANBUY_BLUEPRINT,
	/* 0x02A */ MRT_CANBUY_NINTENDO,
	/* 0x02B */ MRT_CANBUY_RAREWARE,
	/* 0x02C */ MRT_CANBUY_BEAN,
	/* 0x02D */ MRT_CANBUY_PEARL,
	/* 0x02E */ MRT_CANBUY_KONG,
	/* 0x02F */ MRT_CANBUY_FAIRY,
	/* 0x030 */ MRT_CANBUY_FAKEITEM,
	/* 0x031 */ MRT_NOBUY_SPECIALMOVE,
	/* 0x032 */ MRT_NOBUY_SLAM,
	/* 0x033 */ MRT_NOBUY_GUN,
	/* 0x034 */ MRT_NOBUY_GUNUPGRADE,
	/* 0x035 */ MRT_NOBUY_AMMOBELT,
	/* 0x036 */ MRT_NOBUY_INSTRUMENT,
	/* 0x037 */ MRT_NOBUY_TRAINING,
	/* 0x038 */ MRT_NOBUY_FAIRYMOVE,
	/* 0x039 */ MRT_NOBUY_ITEM,
	/* 0x03A */ MRT_NOBUY_BANANA,
	/* 0x03B */ MRT_NOBUY_BLUEPRINT,
	/* 0x03C */ MRT_NOBUY_MEDAL,
	/* 0x03D */ MRT_NOBUY_KONG,
} moverando_hinttext;

typedef enum item_purchase_text {
	/* 0x000 */ ITEMTEXT_SLAM1,
	/* 0x001 */ ITEMTEXT_SLAM1_LATIN,
	/* 0x002 */ ITEMTEXT_SLAM2,
	/* 0x003 */ ITEMTEXT_SLAM2_LATIN,
	/* 0x004 */ ITEMTEXT_SLAM3,
	/* 0x005 */ ITEMTEXT_SLAM3_LATIN,
	/* 0x006 */ ITEMTEXT_BBLAST,
	/* 0x007 */ ITEMTEXT_BBLAST_LATIN,
	/* 0x008 */ ITEMTEXT_SKONG,
	/* 0x009 */ ITEMTEXT_SKONG_LATIN,
	/* 0x00A */ ITEMTEXT_GGRAB,
	/* 0x00B */ ITEMTEXT_GGRAB_LATIN,
	/* 0x00C */ ITEMTEXT_CCHARGE,
	/* 0x00D */ ITEMTEXT_CCHARGE_LATIN,
	/* 0x00E */ ITEMTEXT_RBARREL,
	/* 0x00F */ ITEMTEXT_RBARREL_LATIN,
	/* 0x010 */ ITEMTEXT_SSPRING,
	/* 0x011 */ ITEMTEXT_SSPRING_LATIN,
	/* 0x012 */ ITEMTEXT_OSTAND,
	/* 0x013 */ ITEMTEXT_OSTAND_LATIN,
	/* 0x014 */ ITEMTEXT_BBALLOON,
	/* 0x015 */ ITEMTEXT_BBALLOON_LATIN,
	/* 0x016 */ ITEMTEXT_OSPRINT,
	/* 0x017 */ ITEMTEXT_OSPRINT_LATIN,
	/* 0x018 */ ITEMTEXT_MMONKEY,
	/* 0x019 */ ITEMTEXT_MMONKEY_LATIN,
	/* 0x01A */ ITEMTEXT_PTT,
	/* 0x01B */ ITEMTEXT_PTT_LATIN,
	/* 0x01C */ ITEMTEXT_MPORT,
	/* 0x01D */ ITEMTEXT_MPORT_LATIN,
	/* 0x01E */ ITEMTEXT_HCHUNKY,
	/* 0x01F */ ITEMTEXT_HCHUNKY_LATIN,
	/* 0x020 */ ITEMTEXT_PPUNCH,
	/* 0x021 */ ITEMTEXT_PPUNCH_LATIN,
	/* 0x022 */ ITEMTEXT_GGONE,
	/* 0x023 */ ITEMTEXT_GGONE_LATIN,
	/* 0x024 */ ITEMTEXT_COCONUT,
	/* 0x025 */ ITEMTEXT_PEANUT,
	/* 0x026 */ ITEMTEXT_GRAPE,
	/* 0x027 */ ITEMTEXT_FEATHER,
	/* 0x028 */ ITEMTEXT_PINEAPPLE,
	/* 0x029 */ ITEMTEXT_BONGOS,
	/* 0x02A */ ITEMTEXT_GUITAR,
	/* 0x02B */ ITEMTEXT_TROMBONE,
	/* 0x02C */ ITEMTEXT_SAX,
	/* 0x02D */ ITEMTEXT_TRIANGLE,
	/* 0x02E */ ITEMTEXT_HOMING,
	/* 0x02F */ ITEMTEXT_SNIPER,
	/* 0x030 */ ITEMTEXT_BELT1,
	/* 0x031 */ ITEMTEXT_BELT2,
	/* 0x032 */ ITEMTEXT_THIRDMELON,
	/* 0x033 */ ITEMTEXT_INSUPGRADE1,
	/* 0x034 */ ITEMTEXT_INSUPGRADE2,
	/* 0x035 */ ITEMTEXT_DIVE,
	/* 0x036 */ ITEMTEXT_ORANGE,
	/* 0x037 */ ITEMTEXT_BARREL,
	/* 0x038 */ ITEMTEXT_VINE,
	/* 0x039 */ ITEMTEXT_CAMERA,
	/* 0x03A */ ITEMTEXT_SHOCKWAVE,
	/* 0x03B */ ITEMTEXT_CAMERACOMBO,
	/* 0x03C */ ITEMTEXT_BANANA,
	/* 0x03D */ ITEMTEXT_MEDAL,
	/* 0x03E */ ITEMTEXT_BLUEPRINT_DK,
	/* 0x03F */ ITEMTEXT_BLUEPRINT_DIDDY,
	/* 0x040 */ ITEMTEXT_BLUEPRINT_LANKY,
	/* 0x041 */ ITEMTEXT_BLUEPRINT_TINY,
	/* 0x042 */ ITEMTEXT_BLUEPRINT_CHUNKY,
	/* 0x043 */ ITEMTEXT_NINTENDO,
	/* 0x044 */ ITEMTEXT_RAREWARE,
	/* 0x045 */ ITEMTEXT_KEYGENERIC,
	/* 0x046 */ ITEMTEXT_CROWN,
	/* 0x047 */ ITEMTEXT_BEAN,
	/* 0x048 */ ITEMTEXT_KEY1,
	/* 0x049 */ ITEMTEXT_KEY2,
	/* 0x04A */ ITEMTEXT_KEY3,
	/* 0x04B */ ITEMTEXT_KEY4,
	/* 0x04C */ ITEMTEXT_KEY5,
	/* 0x04D */ ITEMTEXT_KEY6,
	/* 0x04E */ ITEMTEXT_KEY7,
	/* 0x04F */ ITEMTEXT_KEY8,
	/* 0x050 */ ITEMTEXT_PEARL,
	/* 0x051 */ ITEMTEXT_KONG_DK,
	/* 0x052 */ ITEMTEXT_KONG_DIDDY,
	/* 0x053 */ ITEMTEXT_KONG_LANKY,
	/* 0x054 */ ITEMTEXT_KONG_TINY,
	/* 0x055 */ ITEMTEXT_KONG_CHUNKY,
	/* 0x056 */ ITEMTEXT_FAIRY,
	/* 0x057 */ ITEMTEXT_RAINBOWCOIN,
	/* 0x058 */ ITEMTEXT_FAKEITEM,
} item_purchase_text;

typedef enum pausescreenlist {
	/* 0x000 */ PAUSESCREEN_MAIN,
	/* 0x001 */ PAUSESCREEN_LEVEL_KONGS,
	/* 0x002 */ PAUSESCREEN_LEVEL_ALL,
	/* 0x003 */ PAUSESCREEN_TOTALS,
	/* 0x004 */ PAUSESCREEN_CHECKS,
	/* 0x005 */ PAUSESCREEN_HINTS,
	/* 0x006 */ PAUSESCREEN_MOVES,
	/* ----- */ PAUSESCREEN_TERMINATOR,
} pausescreenlist;

typedef enum colorblind_modes {
	/* 0x000 */ COLORBLIND_OFF,
	/* 0x001 */ COLORBLIND_PROT,
	/* 0x002 */ COLORBLIND_DEUT,
	/* 0x003 */ COLORBLIND_TRIT,
} colorblind_modes;

typedef enum seasons {
	/* 0x000 */ SEASON_NONE,
	/* 0x001 */ SEASON_HALLOWEEN,
	/* 0x002 */ SEASON_CHRISTMAS,
} seasons;

typedef enum kongs {
	/* 0x000 */ KONG_DK,
	/* 0x001 */ KONG_DIDDY,
	/* 0x002 */ KONG_LANKY,
	/* 0x003 */ KONG_TINY,
	/* 0x004 */ KONG_CHUNKY,
} kongs;

typedef enum win_conditions {
	/* 0x000 */ GOAL_KROOL,
	/* 0x001 */ GOAL_KEY8,
	/* 0x002 */ GOAL_ALLFAIRIES,
	/* 0x003 */ GOAL_ALLBLUEPRINTS,
	/* 0x004 */ GOAL_ALLMEDALS,
	/* 0x005 */ GOAL_POKESNAP,
	/* 0x006 */ GOAL_ALLKEYS,
} win_conditions;

typedef enum master_types_list {
	/* 0x000 */ ACTORMASTER_UNUSED,
	/* 0x001 */ ACTORMASTER_LOWLEVEL,
	/* 0x002 */ ACTORMASTER_3D,
	/* 0x003 */ ACTORMASTER_CONTROLLER,
	/* 0x004 */ ACTORMASTER_SPRITE,
} master_types_list;

typedef enum vendors {
	/* 0x000 */ SHOP_CRANKY,
	/* 0x001 */ SHOP_FUNKY,
	/* 0x002 */ SHOP_CANDY,
	/* 0x003 */ SHOP_SNIDE,
} vendors;

typedef enum flagtypes {
	/* 0x000 */ FLAGTYPE_PERMANENT,
	/* 0x001 */ FLAGTYPE_GLOBAL,
	/* 0x002 */ FLAGTYPE_TEMPORARY,
} flagtypes;

typedef enum maps {
	/* 0x000 */ MAP_TESTMAP,
    /* 0x001 */ MAP_FUNKY,
    /* 0x002 */ MAP_DKARCADE,
    /* 0x003 */ MAP_HELMBARREL_LANKYMAZE,
    /* 0x004 */ MAP_JAPESMOUNTAIN,
    /* 0x005 */ MAP_CRANKY,
    /* 0x006 */ MAP_JAPESMINECART,
    /* 0x007 */ MAP_JAPES,
    /* 0x008 */ MAP_JAPESDILLO,
    /* 0x009 */ MAP_JETPAC,
    /* 0x00A */ MAP_KOSH_VEASY,
    /* 0x00B */ MAP_SNOOP_NORMALNOLOGO,
    /* 0x00C */ MAP_JAPESSHELL,
    /* 0x00D */ MAP_JAPESPAINTING,
    /* 0x00E */ MAP_AZTECBEETLE,
    /* 0x00F */ MAP_SNIDE,
    /* 0x010 */ MAP_AZTECTINYTEMPLE,
    /* 0x011 */ MAP_HELM,
    /* 0x012 */ MAP_TURTLES_VEASY,
    /* 0x013 */ MAP_AZTEC5DTDK,
    /* 0x014 */ MAP_AZTECLLAMATEMPLE,
    /* 0x015 */ MAP_AZTEC5DTDIDDY,
    /* 0x016 */ MAP_AZTEC5DTTINY,
    /* 0x017 */ MAP_AZTEC5DTLANKY,
    /* 0x018 */ MAP_AZTEC5DTCHUNKY,
    /* 0x019 */ MAP_CANDY,
    /* 0x01A */ MAP_FACTORY,
    /* 0x01B */ MAP_FACTORYCARRACE,
    /* 0x01C */ MAP_HELM_INTROSGAMEOVER,
    /* 0x01D */ MAP_FACTORYPOWERSHED,
    /* 0x01E */ MAP_GALLEON,
    /* 0x01F */ MAP_GALLEONSEASICKSHIP,
    /* 0x020 */ MAP_BATTYBARREL_VEASY,
    /* 0x021 */ MAP_JAPESUNDERGROUND,
    /* 0x022 */ MAP_ISLES,
    /* 0x023 */ MAP_HELMBARREL_TARGET,
    /* 0x024 */ MAP_FACTORYCRUSHER,
    /* 0x025 */ MAP_JAPESBBLAST,
    /* 0x026 */ MAP_AZTEC,
    /* 0x027 */ MAP_GALLEONSEALRACE,
    /* 0x028 */ MAP_NINTENDOLOGO,
    /* 0x029 */ MAP_AZTECBBLAST,
    /* 0x02A */ MAP_TROFFNSCOFF,
    /* 0x02B */ MAP_GALLEON5DSDIDDYLANKYCHUNKY,
    /* 0x02C */ MAP_GALLEONTREASURECHEST,
    /* 0x02D */ MAP_GALLEONMERMAID,
    /* 0x02E */ MAP_GALLEON5DSDKTINY,
    /* 0x02F */ MAP_GALLEON2DS,
    /* 0x030 */ MAP_FUNGI,
    /* 0x031 */ MAP_GALLEONLIGHTHOUSE,
    /* 0x032 */ MAP_HELMBARREL_MUSHROOMBOUNCE,
    /* 0x033 */ MAP_GALLEONMECHFISH,
    /* 0x034 */ MAP_FUNGIANTHILL,
    /* 0x035 */ MAP_BATTLEARENA_BEAVERBRAWL,
    /* 0x036 */ MAP_GALLEONBBLAST,
    /* 0x037 */ MAP_FUNGIMINECART,
    /* 0x038 */ MAP_FUNGIDIDDYBARN,
    /* 0x039 */ MAP_FUNGIDIDDYATTIC,
    /* 0x03A */ MAP_FUNGILANKYATTIC,
    /* 0x03B */ MAP_FUNGIDKBARN,
    /* 0x03C */ MAP_FUNGISPIDER,
    /* 0x03D */ MAP_FUNGIMILLFRONT,
    /* 0x03E */ MAP_FUNGIMILLREAR,
    /* 0x03F */ MAP_FUNGIMUSHROOMSLAM,
    /* 0x040 */ MAP_FUNGIGIANTMUSHROOM,
    /* 0x041 */ MAP_SNOOP_NORMAL,
    /* 0x042 */ MAP_MAUL_HARD,
    /* 0x043 */ MAP_SNATCH_NORMAL,
    /* 0x044 */ MAP_MAUL_EASY,
    /* 0x045 */ MAP_MAUL_NORMAL,
    /* 0x046 */ MAP_FUNGIMUSHROOMLEAP,
    /* 0x047 */ MAP_FUNGISHOOTINGGAME,
    /* 0x048 */ MAP_CAVES,
    /* 0x049 */ MAP_BATTLEARENA_KRITTERKARNAGE,
    /* 0x04A */ MAP_SNATCH_EASY,
    /* 0x04B */ MAP_SNATCH_HARD,
    /* 0x04C */ MAP_DKRAP,
    /* 0x04D */ MAP_MMAYHEM_EASY,
    /* 0x04E */ MAP_BARRAGE_EASY,
    /* 0x04F */ MAP_BARRAGE_NORMAL,
    /* 0x050 */ MAP_MAINMENU,
    /* 0x051 */ MAP_NFRTITLESCREEN,
    /* 0x052 */ MAP_CAVESBEETLERACE,
    /* 0x053 */ MAP_FUNGIDOGADON,
    /* 0x054 */ MAP_CAVES5DITINY,
    /* 0x055 */ MAP_CAVES5DILANKY,
    /* 0x056 */ MAP_CAVES5DIDK,
    /* 0x057 */ MAP_CASTLE,
    /* 0x058 */ MAP_CASTLEBALLROOM,
    /* 0x059 */ MAP_CAVESROTATINGROOM,
    /* 0x05A */ MAP_CAVES5DCCHUNKY,
    /* 0x05B */ MAP_CAVES5DCDK,
    /* 0x05C */ MAP_CAVES5DCDIDDYLOW,
    /* 0x05D */ MAP_CAVES5DCTINY,
    /* 0x05E */ MAP_CAVES1DC,
    /* 0x05F */ MAP_CAVES5DICHUNKY,
    /* 0x060 */ MAP_SALVAGE_NORMAL,
    /* 0x061 */ MAP_KLUMSY,
    /* 0x062 */ MAP_CAVESTILEFLIP,
    /* 0x063 */ MAP_SORTIE_EASY,
    /* 0x064 */ MAP_CAVES5DIDIDDY,
    /* 0x065 */ MAP_KLAMOUR_EASY,
    /* 0x066 */ MAP_BASH_VEASY,
    /* 0x067 */ MAP_SEARCHLIGHT_VEASY,
    /* 0x068 */ MAP_BBOTHER_EASY,
    /* 0x069 */ MAP_CASTLETOWER,
    /* 0x06A */ MAP_CASTLEMINECART,
    /* 0x06B */ MAP_MULTIPLAYERBATTLEARENA,
    /* 0x06C */ MAP_CASTLECRYPTLANKYTINY,
    /* 0x06D */ MAP_MULTIPLAYERARENA1,
    /* 0x06E */ MAP_FACTORYBBLAST,
    /* 0x06F */ MAP_GALLEONPUFFTOSS,
    /* 0x070 */ MAP_CASTLECRYPTDKDIDDYCHUNKY,
    /* 0x071 */ MAP_CASTLEMUSEUM,
    /* 0x072 */ MAP_CASTLELIBRARY,
    /* 0x073 */ MAP_KOSH_EASY,
    /* 0x074 */ MAP_KOSH_NORMAL,
    /* 0x075 */ MAP_KOSH_HARD,
    /* 0x076 */ MAP_TURTLES_EASY,
    /* 0x077 */ MAP_TURTLES_NORMAL,
    /* 0x078 */ MAP_TURTLES_HARD,
    /* 0x079 */ MAP_BATTYBARREL_EASY,
    /* 0x07A */ MAP_BATTYBARREL_NORMAL,
    /* 0x07B */ MAP_BATTYBARREL_HARD,
    /* 0x07C */ MAP_MAUL_INSANE,
    /* 0x07D */ MAP_SNATCH_INSANE,
    /* 0x07E */ MAP_SNOOP_VEASY,
    /* 0x07F */ MAP_SNOOP_EASY,
    /* 0x080 */ MAP_SNOOP_HARD,
    /* 0x081 */ MAP_MMAYHEM_NORMAL,
    /* 0x082 */ MAP_MMAYHEM_HARD,
    /* 0x083 */ MAP_BARRAGE_HARD,
    /* 0x084 */ MAP_SALVAGE_HARD,
    /* 0x085 */ MAP_SALVAGE_EASY,
    /* 0x086 */ MAP_SORTIE_NORMAL,
    /* 0x087 */ MAP_SORTIE_HARD,
    /* 0x088 */ MAP_BBOTHER_NORMAL,
    /* 0x089 */ MAP_BBOTHER_HARD,
    /* 0x08A */ MAP_SEARCHLIGHT_EASY,
    /* 0x08B */ MAP_SEARCHLIGHT_NORMAL,
    /* 0x08C */ MAP_SEARCHLIGHT_HARD,
    /* 0x08D */ MAP_KLAMOUR_NORMAL,
    /* 0x08E */ MAP_KLAMOUR_HARD,
    /* 0x08F */ MAP_KLAMOUR_INSANE,
    /* 0x090 */ MAP_PPPANIC_VEASY,
    /* 0x091 */ MAP_PPPANIC_EASY,
    /* 0x092 */ MAP_PPPANIC_NORMAL,
    /* 0x093 */ MAP_PPPANIC_HARD,
    /* 0x094 */ MAP_BASH_EASY,
    /* 0x095 */ MAP_BASH_NORMAL,
    /* 0x096 */ MAP_BASH_HARD,
    /* 0x097 */ MAP_CASTLEDUNGEON,
    /* 0x098 */ MAP_HELM_INTROSTORY,
    /* 0x099 */ MAP_ISLES_DKTHEATRE,
    /* 0x09A */ MAP_FACTORYJACK,
    /* 0x09B */ MAP_BATTLEARENA_ARENAAMBUSH,
    /* 0x09C */ MAP_BATTLEARENA_MOREKRITTERKARNAGE,
    /* 0x09D */ MAP_BATTLEARENA_FORESTFRACAS,
    /* 0x09E */ MAP_BATTLEARENA_BISHBASHBRAWL,
    /* 0x09F */ MAP_BATTLEARENA_KAMIKAZEKREMLINGS,
    /* 0x0A0 */ MAP_BATTLEARENA_PLINTHPANIC,
    /* 0x0A1 */ MAP_BATTLEARENA_PINNACLEPALAVER,
    /* 0x0A2 */ MAP_BATTLEARENA_SHOCKWAVESHOWDOWN,
    /* 0x0A3 */ MAP_CASTLEBASEMENT,
    /* 0x0A4 */ MAP_CASTLETREE,
    /* 0x0A5 */ MAP_HELMBARREL_RANDOMKREMLING,
    /* 0x0A6 */ MAP_CASTLESHED,
    /* 0x0A7 */ MAP_CASTLETRASH,
    /* 0x0A8 */ MAP_CASTLEGREENHOUSE,
    /* 0x0A9 */ MAP_JAPESLOBBY,
    /* 0x0AA */ MAP_HELMLOBBY,
    /* 0x0AB */ MAP_TREEHOUSE,
    /* 0x0AC */ MAP_ISLES_INTROSTORYROCK,
    /* 0x0AD */ MAP_AZTECLOBBY,
    /* 0x0AE */ MAP_GALLEONLOBBY,
    /* 0x0AF */ MAP_FACTORYLOBBY,
    /* 0x0B0 */ MAP_TRAININGGROUNDS,
    /* 0x0B1 */ MAP_TBARREL_DIVE,
    /* 0x0B2 */ MAP_FUNGILOBBY,
    /* 0x0B3 */ MAP_GALLEONSUBMARINE,
    /* 0x0B4 */ MAP_TBARREL_ORANGE,
    /* 0x0B5 */ MAP_TBARREL_BARREL,
    /* 0x0B6 */ MAP_TBARREL_VINE,
    /* 0x0B7 */ MAP_CASTLECRYPT,
    /* 0x0B8 */ MAP_ENGUARDEARENA,
    /* 0x0B9 */ MAP_CASTLECARRACE,
    /* 0x0BA */ MAP_CAVESBBLAST,
    /* 0x0BB */ MAP_CASTLEBBLAST,
    /* 0x0BC */ MAP_FUNGIBBLAST,
    /* 0x0BD */ MAP_FAIRYISLAND,
    /* 0x0BE */ MAP_MULTIPLAYERARENA2,
    /* 0x0BF */ MAP_RAMBIARENA,
    /* 0x0C0 */ MAP_MULTIPLAYERARENA3,
    /* 0x0C1 */ MAP_CASTLELOBBY,
    /* 0x0C2 */ MAP_CAVESLOBBY,
    /* 0x0C3 */ MAP_ISLES_SNIDEROOM,
    /* 0x0C4 */ MAP_CAVESDILLO,
    /* 0x0C5 */ MAP_AZTECDOGADON,
    /* 0x0C6 */ MAP_TRAININGGROUNDS_ENDSEQUENCE,
    /* 0x0C7 */ MAP_CASTLEKUTOUT,
    /* 0x0C8 */ MAP_CAVESSHACKDIDDYHIGH,
    /* 0x0C9 */ MAP_HELMBARREL_ROCKETBARREL,
    /* 0x0CA */ MAP_HELMBARREL_LANKYSHOOTING,
    /* 0x0CB */ MAP_KROOLDK,
    /* 0x0CC */ MAP_KROOLDIDDY,
    /* 0x0CD */ MAP_KROOLLANKY,
    /* 0x0CE */ MAP_KROOLTINY,
    /* 0x0CF */ MAP_KROOLCHUNKY,
    /* 0x0D0 */ MAP_BLOOPERSENDING,
    /* 0x0D1 */ MAP_HELMBARREL_HIDDENKREMLING,
    /* 0x0D2 */ MAP_HELMBARREL_FLOORISLAVA,
    /* 0x0D3 */ MAP_HELMBARREL_CHUNKYSHOOTING,
    /* 0x0D4 */ MAP_HELMBARREL_RAMBI,
    /* 0x0D5 */ MAP_KLUMSYENDING,
    /* 0x0D6 */ MAP_KROOLSHOE,
    /* 0x0D7 */ MAP_KROOLARENA,
} maps;

typedef enum file_data_indexes {
    DATA_JETPACHISCORE = 0x11,
    DATA_ARCADEHISCORE_CHAR0 = 0x12,
    DATA_ARCADEHISCORE_CHAR1 = 0x13,
    DATA_ARCADEHISCORE_CHAR2 = 0x14,
    DATA_ARCADEHISCORE_NUM = 0x15,
    DATA_RAMBIHISCORE_CHAR0 = 0x16,
    DATA_RAMBIHISCORE_CHAR1 = 0x17,
    DATA_RAMBIHISCORE_CHAR2 = 0x18,
    DATA_RAMBIHISCORE_NUM = 0x19,
    DATA_ENGUARDEHISCORE_CHAR0 = 0x1A,
    DATA_ENGUARDEHISCORE_CHAR1 = 0x1B,
    DATA_ENGUARDEHISCORE_CHAR2 = 0x1C,
    DATA_ENGUARDEHISCORE_NUM = 0x1D,
    DATA_SOUNDTYPE = 0x1E,
    DATA_LANGUAGE = 0x1F,
    DATA_CAMERATYPE = 0x20,
    DATA_LEVELIGT = 0x21,
	DATA_HELMHURRYIGT = 0x22,
	DATA_HELMHURRYOFF = 0x23,
	DATA_BONUSSTAT = 0x24,
	DATA_KONGIGT = 0x25,
	DATA_FILENAME = 0x26,
} file_data_indexes;

typedef enum extra_global_data {
	EGD_LEVELIGT,
	EGD_HELMHURRYIGT,
	EGD_BONUSSTAT,
	EGD_KONGIGT,
	EGD_FILENAME,
	EGD_TERMINATOR,
} extra_global_data;

typedef enum bonus_stat {
    /* 0x000 */ STAT_TAGCOUNT,
    /* ----- */ STAT_TERMINATOR,
} bonus_stat;

typedef enum gamemodes {
	/* 0x000 */ GAMEMODE_NINTENDOLOGO,
	/* 0x001 */ GAMEMODE_OPENINGCUTSCENE,
	/* 0x002 */ GAMEMODE_RAP,
	/* 0x003 */ GAMEMODE_DKTV,
	/* 0x004 */ GAMEMODE_UNK4,
	/* 0x005 */ GAMEMODE_MAINMENU,
	/* 0x006 */ GAMEMODE_ADVENTURE,
	/* 0x007 */ GAMEMODE_LOADGAMEOVER,
	/* 0x008 */ GAMEMODE_UNK8,
	/* 0x009 */ GAMEMODE_GAMEOVER,
	/* 0x00A */ GAMEMODE_ENDSEQADV,
	/* 0x00B */ GAMEMODE_DKTHEATRE,
	/* 0x00C */ GAMEMODE_DKBONUS,
	/* 0x00D */ GAMEMODE_SNIDEGAMES,
	/* 0x00E */ GAMEMODE_ENDSEQTHEATRE,
} gamemodes;

typedef enum microhint_types {
	/* 0x000 */ MICROHINTS_NONE,
	/* 0x001 */ MICROHINTS_SOME,
	/* 0x002 */ MICROHINTS_ALL,
} microhint_types;

typedef enum tracker_types {
	/* 0 */ TRACKER_TYPE_COCONUT,
	/* 1 */ TRACKER_TYPE_BONGOS,
	/* 2 */ TRACKER_TYPE_GRAB,
	/* 3 */ TRACKER_TYPE_STRONG,
	/* 4 */ TRACKER_TYPE_BLAST,
	/* 5 */ TRACKER_TYPE_PEANUT,
	/* 6 */ TRACKER_TYPE_GUITAR,
	/* 7 */ TRACKER_TYPE_CHARGE,
	/* 8 */ TRACKER_TYPE_ROCKET,
	/* 9 */ TRACKER_TYPE_SPRING,
	/* 10 */ TRACKER_TYPE_GRAPE,
	/* 11 */ TRACKER_TYPE_TROMBONE,
	/* 12 */ TRACKER_TYPE_OSTAND,
	/* 13 */ TRACKER_TYPE_OSPRINT,
	/* 14 */ TRACKER_TYPE_BALLOON,
	/* 15 */ TRACKER_TYPE_FEATHER,
	/* 16 */ TRACKER_TYPE_SAX,
	/* 17 */ TRACKER_TYPE_PTT,
	/* 18 */ TRACKER_TYPE_MINI,
	/* 19 */ TRACKER_TYPE_MONKEYPORT,
	/* 20 */ TRACKER_TYPE_PINEAPPLE,
	/* 21 */ TRACKER_TYPE_TRIANGLE,
	/* 22 */ TRACKER_TYPE_PUNCH,
	/* 23 */ TRACKER_TYPE_HUNKY,
	/* 24 */ TRACKER_TYPE_GONE,
	/* 25 */ TRACKER_TYPE_SLAM,
	/* 26 */ TRACKER_TYPE_HOMING,
	/* 27 */ TRACKER_TYPE_SNIPER,
	/* 28 */ TRACKER_TYPE_AMMOBELT,
	/* 29 */ TRACKER_TYPE_INSTRUMENT_UPG,
	/* 30 */ TRACKER_TYPE_DIVE,
	/* 31 */ TRACKER_TYPE_ORANGE,
	/* 32 */ TRACKER_TYPE_BARREL,
	/* 33 */ TRACKER_TYPE_VINE,
	/* 34 */ TRACKER_TYPE_CAMERA,
	/* 35 */ TRACKER_TYPE_SHOCKWAVE,
	/* 36 */ TRACKER_TYPE_KEY1,
	/* 37 */ TRACKER_TYPE_KEY2,
	/* 38 */ TRACKER_TYPE_KEY3,
	/* 39 */ TRACKER_TYPE_KEY4,
	/* 40 */ TRACKER_TYPE_KEY5,
	/* 41 */ TRACKER_TYPE_KEY6,
	/* 42 */ TRACKER_TYPE_KEY7,
	/* 43 */ TRACKER_TYPE_KEY8,
	/* 44 */ TRACKER_TYPE_MELON_2,
	/* 45 */ TRACKER_TYPE_MELON_3,
	/* 46 */ TRACKER_TYPE_INSUPG_1,
	/* 47 */ TRACKER_TYPE_INSUPG_2,
	/* 48 */ TRACKER_TYPE_BELT_1,
	/* 49 */ TRACKER_TYPE_BELT_2,
} tracker_types;