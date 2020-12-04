import localeInfo as _localeInfo
localeInfo = _localeInfo.localeInfo()

ROOT = "d:/ymir work/ui/minimap/"

window = {
	"name" : "AtlasWindow",
	"style" : ("movable", "float",),

	"x" : SCREEN_WIDTH - 136 - 256 - 10,
	"y" : 0,

	"width" : 256 + 15,
	"height" : 256 + 38,

	"children" :
	(
		## BOARD
		{
			"name" : "board",
			"type" : "board_with_titlebar",

			"x" : 0,
			"y" : 0,

			"width" : 256 + 15,
			"height" : 256 + 38,

			"title" : localeInfo.ZONE_MAP,
		},
	),
}
