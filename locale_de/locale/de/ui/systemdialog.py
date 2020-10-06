import uiScriptLocale

ROOT = "d:/ymir work/ui/public/"

STEP_1 = 17
STEP_2 = 57
STEP_3 = 247
BUTTON_STEP_X = 30

window = {
	"name" : "SystemDialog",
	"style" : ("float",),

	"x" : (SCREEN_WIDTH  - 200) /2,
	"y" : (SCREEN_HEIGHT - 288) /2,

	"width" : 200,
	"height" : 288 + 30,

	"children" :
	(
		{
			"name" : "board",
			"type" : "thinboard",

			"x" : 0,
			"y" : 0,

			"width" : 200,
			"height" : 288 + 30,

			"children" :
			(
				{
					"name" : "help_button",
					"type" : "button",

					"x" : 10,
					"y" : STEP_1 + BUTTON_STEP_X*0,

					"text" : uiScriptLocale.SYSTEM_HELP,

					"default_image" : ROOT + "XLarge_Button_01.sub",
					"over_image" : ROOT + "XLarge_Button_02.sub",
					"down_image" : ROOT + "XLarge_Button_03.sub",
				},
				{
					"name" : "mall_button",
					"type" : "button",

					"x" : 10,
					"y" : STEP_2 + BUTTON_STEP_X*0,

					"text" : uiScriptLocale.SYSTEM_MALL,
					"text_color" : 0xffF8BF24,

					"default_image" : ROOT + "XLarge_Button_02.sub",
					"over_image" : ROOT + "XLarge_Button_02.sub",
					"down_image" : ROOT + "XLarge_Button_02.sub",
				},

				{
					"name" : "system_option_button",
					"type" : "button",

					"x" : 10,
					"y" : STEP_2 + BUTTON_STEP_X*1,

					"text" : uiScriptLocale.SYSTEMOPTION_TITLE,

					"default_image" : ROOT + "XLarge_Button_01.sub",
					"over_image" : ROOT + "XLarge_Button_02.sub",
					"down_image" : ROOT + "XLarge_Button_03.sub",
				},
				{
					"name" : "game_option_button",
					"type" : "button",

					"x" : 10,
					"y" : STEP_2 + BUTTON_STEP_X*2,

					"text" : uiScriptLocale.GAMEOPTION_TITLE,

					"default_image" : ROOT + "XLarge_Button_01.sub",
					"over_image" : ROOT + "XLarge_Button_02.sub",
					"down_image" : ROOT + "XLarge_Button_03.sub",
				},
				{
					"name" : "movechannel_button",
					"type" : "button",

					"x" : 10,
					"y" : STEP_2 + BUTTON_STEP_X*3,

					"text" : uiScriptLocale.SYSTEM_MOVE_CHANNEL,

					"default_image" : ROOT + "XLarge_Button_01.sub",
					"over_image" : ROOT + "XLarge_Button_02.sub",
					"down_image" : ROOT + "XLarge_Button_03.sub",
				},
				{
					"name" : "change_button",
					"type" : "button",

					"x" : 10,
					"y" : STEP_2 + BUTTON_STEP_X*4,

					"text" : uiScriptLocale.SYSTEM_CHANGE,

					"default_image" : ROOT + "XLarge_Button_01.sub",
					"over_image" : ROOT + "XLarge_Button_02.sub",
					"down_image" : ROOT + "XLarge_Button_03.sub",
				},
				{
					"name" : "logout_button",
					"type" : "button",

					"x" : 10,
					"y" : STEP_2 + BUTTON_STEP_X*5,

					"text" : uiScriptLocale.SYSTEM_LOGOUT,

					"default_image" : ROOT + "XLarge_Button_01.sub",
					"over_image" : ROOT + "XLarge_Button_02.sub",
					"down_image" : ROOT + "XLarge_Button_03.sub",
				},
				{
					"name" : "exit_button",
					"type" : "button",

					"x" : 10,
					"y" : STEP_3 + BUTTON_STEP_X*0,

					"text" : uiScriptLocale.SYSTEM_EXIT,

					"default_image" : ROOT + "XLarge_Button_01.sub",
					"over_image" : ROOT + "XLarge_Button_02.sub",
					"down_image" : ROOT + "XLarge_Button_03.sub",
				},
				{
					"name" : "cancel_button",
					"type" : "button",

					"x" : 10,
					"y" : STEP_3 + BUTTON_STEP_X*1,

					"text" : uiScriptLocale.CANCEL,

					"default_image" : ROOT + "XLarge_Button_01.sub",
					"over_image" : ROOT + "XLarge_Button_02.sub",
					"down_image" : ROOT + "XLarge_Button_03.sub",
				},
			),
		},
	),
}
