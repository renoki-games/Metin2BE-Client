import uiScriptLocale
import app

ROOT = "d:/ymir work/ui/game/"

Y_ADD_POSITION = 0
window = {
	"name" : "ExpandTaskBar",

	"x" : SCREEN_WIDTH/2 - 5,
	"y" : SCREEN_HEIGHT - 74,

	"width" : 37,
	"height" : 37,

	"children" :
	[
		{
			"name" : "ExpanedTaskBar_Board",
			"type" : "window",

			"x" : 0,
			"y" : 0,

			"width" : 37,
			"height" : 37,

			"children" :
			[
				{
					"name" : "DragonSoulButton",
					"type" : "button",

					"x" : 0,
					"y" : 0,

					"width" : 37,
					"height" : 37,

					"tooltip_text" : uiScriptLocale.TASKBAR_DRAGON_SOUL,
							
					"default_image" : "d:/ymir work/ui/dragonsoul/DragonSoul_Button_01.tga",
					"over_image" : "d:/ymir work/ui/dragonsoul/DragonSoul_Button_02.tga",
					"down_image" : "d:/ymir work/ui/dragonsoul/DragonSoul_Button_03.tga",
				},
			],
		},		
	],
}
if app.ENABLE_AUTO_SYSTEM:
	window["width"] = 37*2
	window["children"][0]["width"] = window["children"][0]["width"] + 37
	window["children"][0]["children"] = window["children"][0]["children"] + [
					{
						"name" : "AutoButton",
						"type" : "button",

						"x" : 38,
						"y" : 0,

						"width" : 37,
						"height" : 37,

						"tooltip_text" : uiScriptLocale.KEYCHANGE_AUTO_WINDOW,
								
						"default_image" : "icon/item/TaskBar_Auto_Button_01.tga",
						"over_image" : "icon/item/TaskBar_Auto_Button_02.tga",
						"down_image" : "icon/item/TaskBar_Auto_Button_03.tga",
					},]

if app.ENABLE_GROWTH_PET_SYSTEM:
	window["width"] = 37*3
	window["children"][0]["width"] = window["children"][0]["width"] + 37
	window["children"][0]["children"] = window["children"][0]["children"] + [
					{
						"name" : "PetInfoButton",
						"type" : "button",

						"x" : 74,
						"y" : 0,

						"width" : 37,
						"height" : 37,

						"tooltip_text" : uiScriptLocale.TASKBAR_DISABLE,
								
						"default_image" : "d:/ymir work/ui/pet/TaskBar_Pet_Button_01.tga",
						"over_image" : "d:/ymir work/ui/pet/TaskBar_Pet_Button_02.tga",
						"down_image" : "d:/ymir work/ui/pet/TaskBar_Pet_Button_03.tga",
					},]
if app.ENABLE_MONSTER_CARD:
	window["width"] = 37*4
	window["children"][0]["width"] = window["children"][0]["width"] + 37
	window["children"][0]["children"] = window["children"][0]["children"] + [
					{
						"name" : "MonsterCardWindow",
						"type" : "button",

						"x" : 110,
						"y" : 0,

						"width" : 37,
						"height" : 37,

						"tooltip_text" : uiScriptLocale.KEYCHANGE_MONSTER_CARD_WINDOW,
								
						"default_image" : "icon/item/Mcard_Button_01.tga",
						"over_image" : "icon/item/Mcard_Button_02.tga",
						"down_image" : "icon/item/Mcard_Button_03.tga",
					},]
