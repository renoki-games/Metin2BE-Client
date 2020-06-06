import localeInfo
import uiScriptLocale

ROOT = "d:/ymir work/ui/game/"

window = {
	"name" : "ExchangeDialog",

	"x" : 0,
	"y" : 0,

	"style" : ("movable", "float",),

	"width" : 430,
	"height" : 197,

	"children" :
	(
		{
			"name" : "board",
			"type" : "board",
			"style" : ("attach",),

			"x" : 0,
			"y" : 0,

			"width" : 430,
			"height" : 197,

			"children" :
			(
				## Title
				{
					"name" : "TitleBar",
					"type" : "titlebar",
					"style" : ("attach",),

					"x" : 3,
					"y" : 8,
 
					"width" : 421,
					"color" : "gray",

					"children" :
					(
						{ "name":"TitleName", "type":"text", "x":215, "y":3, "text":localeInfo.EXCHANGE_TITLE, "text_horizontal_align":"center" },
					),
				},

				## MiddleBar
				{
					"name" : "Middle_Bar",
					"type" : "image",

					"x" : 213,
					"y" : 46,

					"image" : ROOT + "windows/middlebar.sub",
				},

				## Owner
				{
					"name" : "Owner",
					"type" : "window",

					"x" : 228,
					"y" : 33,

					"width" : 194,
					"height" : 160,

					"children" :
					(
						{
							"name" : "Owner_Slot",
							"type" : "grid_table",

							"start_index" : 0,

							"x" : 0,
							"y" : 0,

							"x_count" : 6,
							"y_count" : 4,
							"x_step" : 32,
							"y_step" : 32,
							"x_blank" : 0,
							"y_blank" : 0,

							"image" : "d:/ymir work/ui/public/slot_base.sub",
						},
						{
							"name" : "Owner_Money",
							"type" : "button",

							"x" : 0,
							"y" : 135,

							"default_image" : "d:/ymir work/ui/public/parameter_slot_05.sub",
							"over_image" : "d:/ymir work/ui/public/parameter_slot_05.sub",
							"down_image" : "d:/ymir work/ui/public/parameter_slot_05.sub",

							"children" :
							(
								{
									"name" : "Owner_Money_Value",
									"type" : "text",

									"x" : 2,
									"y" : 2,

									"text" : "1234567",

									"horizontal_align" : "right",
									"text_horizontal_align" : "right",
								},
							),
						},
						{
							"name" : "Owner_Accept_Light",
							"type" : "button",

							"x" : 131,
							"y" : 134,

							"default_image" : "d:/ymir work/ui/game/windows/accept_button_off.sub",
							"over_image" : "d:/ymir work/ui/game/windows/accept_button_off.sub",
							"down_image" : "d:/ymir work/ui/game/windows/accept_button_on.sub",
						},
						{
							"name" : "Owner_Accept_Button",
							"type" : "toggle_button",

							"x" : 152,
							"y" : 134,

							"text" : uiScriptLocale.EXCHANGE_ACCEPT,

							"default_image" : "d:/ymir work/ui/public/small_button_01.sub",
							"over_image" : "d:/ymir work/ui/public/small_button_02.sub",
							"down_image" : "d:/ymir work/ui/public/small_button_03.sub",
						},
					),
				},

				## Target
				{
					"name" : "Target",
					"type" : "window",

					"x" : 10,
					"y" : 33,

					"width" : 194,
					"height" : 160,

					"children" :
					(
						{
							"name" : "Target_Slot",
							"type" : "grid_table",

							"start_index" : 0,

							"x" : 0,
							"y" : 0,

							"x_count" : 6,
							"y_count" : 4,
							"x_step" : 32,
							"y_step" : 32,
							"x_blank" : 0,
							"y_blank" : 0,

							"image" : "d:/ymir work/ui/public/slot_base.sub",
						},
						{
							"name" : "Target_Money",
							"type" : "image",

							"x" : 0,
							"y" : 134,

							"image" : "d:/ymir work/ui/public/parameter_slot_05.sub",

							"children" :
							(
								{
									"name" : "Target_Money_Value",
									"type" : "text",

									"x" : 2,
									"y" : 2,

									"text" : "1234567",

									"horizontal_align" : "right",
									"text_horizontal_align" : "right",
								},
							),
						},
						{
							"name" : "Target_Accept_Light",
							"type" : "button",

							"x" : 131,
							"y" : 134,

							"default_image" : "d:/ymir work/ui/game/windows/accept_button_off.sub",
							"over_image" : "d:/ymir work/ui/game/windows/accept_button_off.sub",
							"down_image" : "d:/ymir work/ui/game/windows/accept_button_on.sub",
						},
					),
				},
			),
		},
	),
}