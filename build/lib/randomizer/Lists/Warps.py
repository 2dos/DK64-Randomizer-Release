'Designates Bananaport properties.'
_A=True
from randomizer.Enums.Regions import Regions
from randomizer.Enums.Warps import Warps
from randomizer.Lists.MapsAndExits import Maps
class BananaportData:
	'Information about the bananaport.'
	def __init__(A,*,name='',map_id=0,region_id=0,obj_id_vanilla=0,locked=False,vanilla_warp=0):'Initialize with given parameters.';B=vanilla_warp;A.name=name;A.map_id=map_id;A.region_id=region_id;A.obj_id_vanilla=obj_id_vanilla;A.locked=locked;A.vanilla_warp=B;A.new_warp=B
	def setNewWarp(A,new_warp):'Set new warp type.';A.new_warp=new_warp
BananaportVanilla={Warps.JapesNearPortal:BananaportData(name='Jungle Japes: Near Portal',map_id=Maps.JungleJapes,region_id=Regions.JungleJapesMain,obj_id_vanilla=89,vanilla_warp=0),Warps.JapesEndOfTunnel:BananaportData(name='Jungle Japes: End of Tunnel',map_id=Maps.JungleJapes,region_id=Regions.JungleJapesMain,obj_id_vanilla=90,vanilla_warp=0),Warps.JapesNearMainTag:BananaportData(name='Jungle Japes: Near Main Tag',map_id=Maps.JungleJapes,region_id=Regions.JungleJapesMain,obj_id_vanilla=152,vanilla_warp=1),Warps.JapesNearMountain:BananaportData(name='Jungle Japes: Outside the Mountain',map_id=Maps.JungleJapes,region_id=Regions.JungleJapesMain,obj_id_vanilla=159,vanilla_warp=1),Warps.JapesFarRight:BananaportData(name='Jungle Japes: Near Painting Room',map_id=Maps.JungleJapes,region_id=Regions.JungleJapesMain,obj_id_vanilla=158,vanilla_warp=2),Warps.JapesFarLeft:BananaportData(name='Jungle Japes: Near Baboon Blast',map_id=Maps.JungleJapes,region_id=Regions.JungleJapesMain,obj_id_vanilla=151,vanilla_warp=2),Warps.JapesCrankyTunnelNear:BananaportData(name='Jungle Japes: Start of Cranky Tunnel',map_id=Maps.JungleJapes,region_id=Regions.JapesBeyondCoconutGate2,obj_id_vanilla=94,vanilla_warp=3),Warps.JapesCrankyTunnelFar:BananaportData(name='Jungle Japes: Near Cranky',map_id=Maps.JungleJapes,region_id=Regions.JapesBeyondCoconutGate2,obj_id_vanilla=111,vanilla_warp=3),Warps.JapesShellhive:BananaportData(name='Jungle Japes: Outside the Shellhive',map_id=Maps.JungleJapes,region_id=Regions.JapesBeyondFeatherGate,obj_id_vanilla=298,vanilla_warp=4),Warps.JapesOnMountain:BananaportData(name='Jungle Japes: On top of the Mountain',map_id=Maps.JungleJapes,region_id=Regions.JapesTopOfMountain,obj_id_vanilla=299,vanilla_warp=4),Warps.AztecNearPortal:BananaportData(name='Angry Aztec: Near Portal',map_id=Maps.AngryAztec,region_id=Regions.AngryAztecStart,obj_id_vanilla=6,vanilla_warp=0),Warps.AztecNearCandy:BananaportData(name='Angry Aztec: Near Candy',map_id=Maps.AngryAztec,region_id=Regions.AngryAztecStart,obj_id_vanilla=7,vanilla_warp=0),Warps.AztecNearTinyTemple:BananaportData(name='Angry Aztec: Outside Tiny Temple',map_id=Maps.AngryAztec,region_id=Regions.AngryAztecStart,obj_id_vanilla=128,vanilla_warp=1),Warps.AztecEndOfTunnel:BananaportData(name='Angry Aztec: End of the Tunnel',map_id=Maps.AngryAztec,region_id=Regions.AngryAztecMain,obj_id_vanilla=127,vanilla_warp=1),Warps.AztecTotemNearLeft:BananaportData(name='Angry Aztec: Near Totem Rocketbarrel',map_id=Maps.AngryAztec,region_id=Regions.AngryAztecMain,obj_id_vanilla=152,vanilla_warp=2),Warps.AztecCranky:BananaportData(name="Angry Aztec: Outside Cranky's",map_id=Maps.AngryAztec,region_id=Regions.AngryAztecMain,obj_id_vanilla=149,vanilla_warp=2),Warps.AztecTotemNearRight:BananaportData(name='Angry Aztec: Near Llama Temple',map_id=Maps.AngryAztec,region_id=Regions.AngryAztecMain,obj_id_vanilla=115,vanilla_warp=3),Warps.AztecFunky:BananaportData(name="Angry Aztec: Outside Funky's",map_id=Maps.AngryAztec,region_id=Regions.AngryAztecMain,obj_id_vanilla=177,vanilla_warp=3),Warps.AztecNearSnide:BananaportData(name="Angry Aztec: Near Snide's",map_id=Maps.AngryAztec,region_id=Regions.AngryAztecMain,obj_id_vanilla=130,vanilla_warp=4),Warps.AztecSnoopTunnel:BananaportData(name='Angry Aztec: Sandy Tunnel',map_id=Maps.AngryAztec,region_id=Regions.AztecDonkeyQuicksandCave,obj_id_vanilla=135,vanilla_warp=4),Warps.LlamaNearLeft:BananaportData(name='Llama Temple: Near the Bongo Pad',map_id=Maps.AztecLlamaTemple,region_id=Regions.LlamaTemple,obj_id_vanilla=88,vanilla_warp=0),Warps.LlamaMatchingGame:BananaportData(name='Llama Temple: Outside Matching Game',map_id=Maps.AztecLlamaTemple,region_id=Regions.LlamaTemple,obj_id_vanilla=78,vanilla_warp=0),Warps.LlamaNearRight:BananaportData(name='Llama Temple: Near the Trombone Pad',map_id=Maps.AztecLlamaTemple,region_id=Regions.LlamaTemple,obj_id_vanilla=154,vanilla_warp=1),Warps.LlamaLavaRoom:BananaportData(name='Llama Temple: In the Lava Room',map_id=Maps.AztecLlamaTemple,region_id=Regions.LlamaTempleBack,obj_id_vanilla=153,vanilla_warp=1),Warps.FactoryNearHatchTunnel:BananaportData(name='Frantic Factory: Near Hatch Tunnel',map_id=Maps.FranticFactory,region_id=Regions.FranticFactoryStart,obj_id_vanilla=125,vanilla_warp=0),Warps.FactoryStorageRoom:BananaportData(name='Frantic Factory: Storage Room',map_id=Maps.FranticFactory,region_id=Regions.BeyondHatch,obj_id_vanilla=322,vanilla_warp=0),Warps.FactoryNearBlockTunnel:BananaportData(name='Frantic Factory: Near Block Tower Tunnel',map_id=Maps.FranticFactory,region_id=Regions.FranticFactoryStart,obj_id_vanilla=321,vanilla_warp=1),Warps.FactoryRAndD:BananaportData(name='Frantic Factory: R&D',map_id=Maps.FranticFactory,region_id=Regions.RandD,obj_id_vanilla=324,vanilla_warp=1),Warps.FactoryLobbyFar:BananaportData(name='Frantic Factory: Lobby Far',map_id=Maps.FranticFactory,region_id=Regions.FranticFactoryStart,obj_id_vanilla=217,vanilla_warp=2),Warps.FactorySnides:BananaportData(name="Frantic Factory: Outside Snide's",map_id=Maps.FranticFactory,region_id=Regions.Testing,obj_id_vanilla=323,vanilla_warp=2),Warps.FactoryProdBottom:BananaportData(name='Frantic Factory: Production Room (Bottom)',map_id=Maps.FranticFactory,region_id=Regions.BeyondHatch,obj_id_vanilla=261,vanilla_warp=3),Warps.FactoryProdTop:BananaportData(name='Frantic Factory: Production Room (Top)',map_id=Maps.FranticFactory,region_id=Regions.MiddleCore,obj_id_vanilla=268,vanilla_warp=3),Warps.FactoryArcade:BananaportData(name='Frantic Factory: Arcade Room',map_id=Maps.FranticFactory,region_id=Regions.BeyondHatch,obj_id_vanilla=267,vanilla_warp=4),Warps.FactoryFunky:BananaportData(name="Frantic Factory: Outside Funky's",map_id=Maps.FranticFactory,region_id=Regions.Testing,obj_id_vanilla=238,vanilla_warp=4),Warps.GalleonNearTunnelIntersection:BananaportData(name='Gloomy Galleon: Near Tunnel Intersection',map_id=Maps.GloomyGalleon,region_id=Regions.GloomyGalleonStart,obj_id_vanilla=503,vanilla_warp=0),Warps.GalleonLighthouseRear:BananaportData(name='Gloomy Galleon: Lighthouse Rear',map_id=Maps.GloomyGalleon,region_id=Regions.LighthouseArea,obj_id_vanilla=502,vanilla_warp=0),Warps.GalleonNearChestGB:BananaportData(name='Gloomy Galleon: Near Chest Room',map_id=Maps.GloomyGalleon,region_id=Regions.GloomyGalleonStart,obj_id_vanilla=95,vanilla_warp=1),Warps.GalleonNear2DS:BananaportData(name='Gloomy Galleon: Near 2-Door Ship',map_id=Maps.GloomyGalleon,region_id=Regions.Shipyard,obj_id_vanilla=108,locked=_A,vanilla_warp=1),Warps.GalleonNearCranky:BananaportData(name="Gloomy Galleon: Near Cranky's",map_id=Maps.GloomyGalleon,region_id=Regions.GloomyGalleonStart,obj_id_vanilla=96,vanilla_warp=2),Warps.GalleonSnides:BananaportData(name="Gloomy Galleon: Outside Snide's",map_id=Maps.GloomyGalleon,region_id=Regions.LighthouseArea,obj_id_vanilla=102,vanilla_warp=2),Warps.GalleonGoldTower:BananaportData(name='Gloomy Galleon: On a Gold Tower',map_id=Maps.GloomyGalleon,region_id=Regions.TreasureRoomDiddyGoldTower,obj_id_vanilla=85,vanilla_warp=3),Warps.GalleonNearSeal:BananaportData(name='Gloomy Galleon: Near Seal Race',map_id=Maps.GloomyGalleon,region_id=Regions.Shipyard,obj_id_vanilla=86,locked=_A,vanilla_warp=3),Warps.GalleonNearRocketbarrel:BananaportData(name='Gloomy Galleon: Near Lighthouse Rocketbarrel',map_id=Maps.GloomyGalleon,region_id=Regions.LighthouseArea,obj_id_vanilla=22,vanilla_warp=4),Warps.GalleonNearFunky:BananaportData(name="Gloomy Galleon: Near Funky's",map_id=Maps.GloomyGalleon,region_id=Regions.Shipyard,obj_id_vanilla=21,locked=_A,vanilla_warp=4),Warps.FungiClock1:BananaportData(name='Fungi Forest: Clock (1)',map_id=Maps.FungiForest,region_id=Regions.FungiForestStart,obj_id_vanilla=54,vanilla_warp=0),Warps.FungiMill:BananaportData(name='Fungi Forest: Mill',map_id=Maps.FungiForest,region_id=Regions.MillArea,obj_id_vanilla=53,vanilla_warp=0),Warps.FungiClock2:BananaportData(name='Fungi Forest: Clock (2)',map_id=Maps.FungiForest,region_id=Regions.FungiForestStart,obj_id_vanilla=73,vanilla_warp=1),Warps.FungiFunky:BananaportData(name="Fungi Forest: Outside Funky's",map_id=Maps.FungiForest,region_id=Regions.WormArea,obj_id_vanilla=74,vanilla_warp=1),Warps.FungiClock3:BananaportData(name='Fungi Forest: Clock (3)',map_id=Maps.FungiForest,region_id=Regions.FungiForestStart,obj_id_vanilla=75,vanilla_warp=2),Warps.FungiMushEntrance:BananaportData(name='Fungi Forest: Giant Mushroom Lowest Entrance',map_id=Maps.FungiForest,region_id=Regions.GiantMushroomArea,obj_id_vanilla=78,vanilla_warp=2),Warps.FungiClock4:BananaportData(name='Fungi Forest: Clock (4)',map_id=Maps.FungiForest,region_id=Regions.FungiForestStart,obj_id_vanilla=79,vanilla_warp=3),Warps.FungiOwlTree:BananaportData(name='Fungi Forest: Owl Tree',map_id=Maps.FungiForest,region_id=Regions.HollowTreeArea,obj_id_vanilla=81,vanilla_warp=3),Warps.FungiTopMush:BananaportData(name='Fungi Forest: Giant Mushroom (Top)',map_id=Maps.FungiForest,region_id=Regions.MushroomUpperExterior,obj_id_vanilla=86,vanilla_warp=4),Warps.FungiLowMush:BananaportData(name='Fungi Forest: Giant Mushroom (Bottom)',map_id=Maps.FungiForest,region_id=Regions.GiantMushroomArea,obj_id_vanilla=85,vanilla_warp=4),Warps.CavesNearLeft:BananaportData(name='Crystal Caves: Near Left',map_id=Maps.CrystalCaves,region_id=Regions.CrystalCavesMain,obj_id_vanilla=34,vanilla_warp=0),Warps.CavesNearChunkyShield:BananaportData(name='Crystal Caves: Near Chunky Shield',map_id=Maps.CrystalCaves,region_id=Regions.IglooArea,obj_id_vanilla=33,vanilla_warp=0),Warps.CavesNearRight:BananaportData(name='Crystal Caves: Near Right',map_id=Maps.CrystalCaves,region_id=Regions.CrystalCavesMain,obj_id_vanilla=55,vanilla_warp=1),Warps.CavesWaterfall:BananaportData(name='Crystal Caves: Near Waterfall',map_id=Maps.CrystalCaves,region_id=Regions.CabinArea,obj_id_vanilla=54,vanilla_warp=1),Warps.CavesNearIglooTag:BananaportData(name='Crystal Caves: Near Igloo Tag',map_id=Maps.CrystalCaves,region_id=Regions.IglooArea,obj_id_vanilla=87,vanilla_warp=2),Warps.CavesBonusRoom:BananaportData(name='Crystal Caves: Inside Bonus Room',map_id=Maps.CrystalCaves,region_id=Regions.CavesBonusCave,obj_id_vanilla=86,locked=_A,vanilla_warp=2),Warps.CavesThinPillar:BananaportData(name='Crystal Caves: On the Thin Pillar',map_id=Maps.CrystalCaves,region_id=Regions.CavesBananaportSpire,obj_id_vanilla=107,vanilla_warp=3),Warps.CavesBlueprintRoom:BananaportData(name='Crystal Caves: Inside Blueprint Room',map_id=Maps.CrystalCaves,region_id=Regions.CavesBlueprintCave,obj_id_vanilla=106,locked=_A,vanilla_warp=3),Warps.CavesThickPillar:BananaportData(name='Crystal Caves: On the Thick Pillar',map_id=Maps.CrystalCaves,region_id=Regions.CavesBlueprintPillar,obj_id_vanilla=181,locked=_A,vanilla_warp=4),Warps.CavesCabins:BananaportData(name='Crystal Caves: On the 5-Door Cabin',map_id=Maps.CrystalCaves,region_id=Regions.CabinArea,obj_id_vanilla=96,vanilla_warp=4),Warps.CastleCenter1:BananaportData(name='Creepy Castle: Center (1)',map_id=Maps.CreepyCastle,region_id=Regions.CreepyCastleMain,obj_id_vanilla=36,vanilla_warp=0),Warps.CastleRear:BananaportData(name='Creepy Castle: Rear',map_id=Maps.CreepyCastle,region_id=Regions.CreepyCastleMain,obj_id_vanilla=34,vanilla_warp=0),Warps.CastleCenter2:BananaportData(name='Creepy Castle: Center (2)',map_id=Maps.CreepyCastle,region_id=Regions.CreepyCastleMain,obj_id_vanilla=43,vanilla_warp=1),Warps.CastleRocketbarrel:BananaportData(name='Creepy Castle: Rocketbarrel',map_id=Maps.CreepyCastle,region_id=Regions.CreepyCastleMain,obj_id_vanilla=40,vanilla_warp=1),Warps.CastleCenter3:BananaportData(name='Creepy Castle: Center (3)',map_id=Maps.CreepyCastle,region_id=Regions.CreepyCastleMain,obj_id_vanilla=44,vanilla_warp=2),Warps.CastleCranky:BananaportData(name="Creepy Castle: Outside Cranky's",map_id=Maps.CreepyCastle,region_id=Regions.CreepyCastleMain,obj_id_vanilla=35,vanilla_warp=2),Warps.CastleCenter4:BananaportData(name='Creepy Castle: Center (4)',map_id=Maps.CreepyCastle,region_id=Regions.CreepyCastleMain,obj_id_vanilla=33,vanilla_warp=3),Warps.CastleTrashCan:BananaportData(name='Creepy Castle: Outside Trash Can',map_id=Maps.CreepyCastle,region_id=Regions.CreepyCastleMain,obj_id_vanilla=41,vanilla_warp=3),Warps.CastleCenter5:BananaportData(name='Creepy Castle: Center (5)',map_id=Maps.CreepyCastle,region_id=Regions.CreepyCastleMain,obj_id_vanilla=45,vanilla_warp=4),Warps.CastleTop:BananaportData(name='Creepy Castle: Top',map_id=Maps.CreepyCastle,region_id=Regions.CreepyCastleMain,obj_id_vanilla=42,vanilla_warp=4),Warps.CryptNearLeft:BananaportData(name='Crypt: Near Left',map_id=Maps.CastleCrypt,region_id=Regions.Crypt,obj_id_vanilla=24,vanilla_warp=0),Warps.CryptFarLeft:BananaportData(name='Crypt: Far Left',map_id=Maps.CastleCrypt,region_id=Regions.Crypt,obj_id_vanilla=29,vanilla_warp=0),Warps.CryptNearCenter:BananaportData(name='Crypt: Near Center',map_id=Maps.CastleCrypt,region_id=Regions.Crypt,obj_id_vanilla=25,vanilla_warp=1),Warps.CryptFarCenter:BananaportData(name='Crypt: Outside Minecart',map_id=Maps.CastleCrypt,region_id=Regions.Crypt,obj_id_vanilla=28,vanilla_warp=1),Warps.CryptNearRight:BananaportData(name='Crypt: Near Right',map_id=Maps.CastleCrypt,region_id=Regions.Crypt,obj_id_vanilla=26,vanilla_warp=2),Warps.CryptFarRight:BananaportData(name='Crypt: Far Right',map_id=Maps.CastleCrypt,region_id=Regions.Crypt,obj_id_vanilla=27,vanilla_warp=2),Warps.IslesRing1:BananaportData(name='DK Isles: Ring (1)',map_id=Maps.Isles,region_id=Regions.IslesMain,obj_id_vanilla=16,vanilla_warp=0),Warps.IslesKLumsy:BananaportData(name="DK Isles: Outside K. Lumsy's Prison",map_id=Maps.Isles,region_id=Regions.IslesMain,obj_id_vanilla=17,vanilla_warp=0),Warps.IslesRing2:BananaportData(name='DK Isles: Ring (2)',map_id=Maps.Isles,region_id=Regions.IslesMain,obj_id_vanilla=18,vanilla_warp=1),Warps.IslesAztecLobby:BananaportData(name='DK Isles: Outside Aztec Lobby',map_id=Maps.Isles,region_id=Regions.IslesMain,obj_id_vanilla=19,vanilla_warp=1),Warps.IslesRing3:BananaportData(name='DK Isles: Ring (3)',map_id=Maps.Isles,region_id=Regions.IslesMain,obj_id_vanilla=22,vanilla_warp=2),Warps.IslesWaterfall:BananaportData(name='DK Isles: Waterfall',map_id=Maps.Isles,region_id=Regions.IslesMain,obj_id_vanilla=20,vanilla_warp=2),Warps.IslesRing4:BananaportData(name='DK Isles: Ring (4)',map_id=Maps.Isles,region_id=Regions.IslesMain,obj_id_vanilla=23,vanilla_warp=3),Warps.IslesFactoryLobby:BananaportData(name='DK Isles: Outside Factory Lobby',map_id=Maps.Isles,region_id=Regions.CrocodileIsleBeyondLift,obj_id_vanilla=24,vanilla_warp=3),Warps.IslesRing5:BananaportData(name='DK Isles: Ring (5)',map_id=Maps.Isles,region_id=Regions.IslesMain,obj_id_vanilla=21,vanilla_warp=4),Warps.IslesFairyIsland:BananaportData(name='DK Isles: Fairy Island',map_id=Maps.Isles,region_id=Regions.IslesMain,obj_id_vanilla=25,vanilla_warp=4)}