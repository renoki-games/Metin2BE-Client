import localeInfo as _localeInfo
localeInfo = _localeInfo.localeInfo()

import chr

BOARD_WIDTH = 215
BOARD_HEIGHT = 200

window = {
	"name" : "TransferSystemWindow",
	"style" : ("movable", "float",),

	"x" : (SCREEN_WIDTH / 2) - (BOARD_WIDTH / 2),
	"y" : (SCREEN_HEIGHT / 2) - (BOARD_HEIGHT / 2),

	"horizontal_align": "center",
	"vertical_align": "center",

	"width" : BOARD_WIDTH,
	"height" : BOARD_HEIGHT,

	"children" :
	(
		{
			"name" : "board",
			"type" : "board_with_titlebar",
			"style" : ("attach",),

			"x" : 0,
			"y" : 0,

			"width" : BOARD_WIDTH,
			"height" : BOARD_HEIGHT,

			"title": "Transfersystem",

			"children":
			(
				{
					"name" : "itemSlot_bg",
					"type" : "image",

					"x" : 20,
					"y" : 40,

					"image" : "d:/ymir work/ui/Slot_Base_x3.png",

					"children" :
					(
						{
							"name" : "itemSlot",
							"type" : "slot",

							"x": 0,
							"y": 0,

							"width": 32,
							"height": 96,

							"slot" : (
								{ "index": 0, "x": 0, "y": 0, "width": 32, "height": 96 },
							),
						},
					),
				},

				{
					"name": "acceptCheckbox",
					"type": "checkbox",

					"x": 125,
					"y": 42,

					"text": localeInfo.TRANSFERSYSTEM_CHECKBOX_LABEL,
					"check": True,
				},

				{
					"name": "characterNameLabel",
					"type": "text",

					"x": 60,
					"y": 40,

					"text": localeInfo.TRANSFERSYSTEM_NAME_LABEL,
				},

				{
					"name": "characterNameInput_bg",
					"type": "image",
					"style": ("not_pick", ),

					"x": 60,
					"y": 60,

					"image": "d:/ymir work/ui/public/parameter_slot_05.sub",

					"children":
					(
						{
							"name": "characterNameInput",
							"type": "editline",

							"width": 130,
							"height": 18,

							"x": 2,
							"y": 2,

							"input_limit": chr.CHARACTER_NAME_MAX_LEN,
							"text": "",
						},
					),
				},

				{
					"name": "goldInputLabel",
					"type": "text",

					"x": 60,
					"y": 90,

					"text": localeInfo.TRANSFERSYSTEM_GOLD_LABEL,
				},

				{
					"name": "goldInputButton",
					"type": "button",

					"x": 60,
					"y": 110,

					"default_image": "d:/ymir work/ui/public/parameter_slot_05.sub",
					"over_image": "d:/ymir work/ui/public/parameter_slot_05.sub",
					"down_image": "d:/ymir work/ui/public/parameter_slot_05.sub",

					"children":
					(
						{
							"name": "goldInput",
							"type": "text",

							"x": 2,
							"y": 2,

							"text" : localeInfo.NumberToMoneyString(0),
						},
					),
				},

				{
					"name": "acceptButton",
					"type": "button",

					"x": 0,
					"y": 155,

					"horizontal_align": "center",

					"text": localeInfo.TRANSFERSYSTEM_TRANSFER_BUTTON_TEXT,

					"default_image": "d:/ymir work/ui/game/myshop_deco/select_btn_01.sub",
					"over_image": "d:/ymir work/ui/game/myshop_deco/select_btn_02.sub",
					"down_image": "d:/ymir work/ui/game/myshop_deco/select_btn_03.sub",
				},
			),
		},
	),
}
