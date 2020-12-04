import localeInfo as _localeInfo
localeInfo = _localeInfo.localeInfo()
import item
import app

import player
EQUIPMENT_START_INDEX = player.EQUIPMENT_SLOT_START

window = {
	"name" : "InventoryWindow",

	"x" : SCREEN_WIDTH - 176,
	"y" : SCREEN_HEIGHT - 37 - 585,

	"style" : ("movable", "float",),

	"width" : 176,
	"height" : 585,

	"children" :
	(
		## Inventory, Equipment Slots
		{
			"name" : "board",
			"type" : "board",
			"style" : ("attach",),

			"x" : 0,
			"y" : 0,

			"width" : 176,
			"height" : 585,

			"children" :
			(
				## Title
				{
					"name" : "TitleBar",
					"type" : "titlebar",
					"style" : ("attach",),

					"x" : 8,
					"y" : 7,

					"width" : 161,
					"color" : "yellow",

					"children" :
					(
						{ "name":"TitleName", "type":"text", "x":77, "y":3, "text":localeInfo.INVENTORY_TITLE, "text_horizontal_align":"center" },
					),
				},

				## Equipment Slot
				{
					"name" : "Equipment_Base",
					"type" : "image",

					"x" : 10,
					"y" : 33,

					"image" : "d:/ymir work/ui/equipment_bg_without_ring.tga",

					"children" :
					(

						{
							"name" : "EquipmentSlot",
							"type" : "slot",

							"x" : 0,
							"y" : 0,

							"width" : 155,
							"height" : 187,

							"slot" : (
										{"index":EQUIPMENT_START_INDEX+0, "x":41, "y":36, "width":32, "height":64},	#Rüstung
										{"index":EQUIPMENT_START_INDEX+1, "x":41, "y":4, "width":32, "height":32},	#Helm
										{"index":EQUIPMENT_START_INDEX+2, "x":41, "y":147, "width":32, "height":32},#Schuhe
										{"index":EQUIPMENT_START_INDEX+3, "x":77, "y":68, "width":32, "height":32},	#Armband
										{"index":EQUIPMENT_START_INDEX+4, "x":5, "y":4, "width":32, "height":96},	#Waffe
										{"index":EQUIPMENT_START_INDEX+5, "x":117, "y":68, "width":32, "height":32},#Halskette
										{"index":EQUIPMENT_START_INDEX+6, "x":117, "y":36, "width":32, "height":32},#Ohrringe
										{"index":EQUIPMENT_START_INDEX+7, "x":5, "y":147, "width":32, "height":32},	#IS-Slot1
										{"index":EQUIPMENT_START_INDEX+8, "x":77, "y":147, "width":32, "height":32},#IS-Slot2
										{"index":EQUIPMENT_START_INDEX+9, "x":117, "y":4, "width":32, "height":32},	#Pfeile
										{"index":EQUIPMENT_START_INDEX+10, "x":77, "y":36, "width":32, "height":32},#Schild
										{"index":item.EQUIPMENT_SPECIAL, "x":42, "y":106, "width":32, "height":32},#Spezialbücher
										
									),
						},
						## MallButton
						{
							"name" : "SafeboxButton",
							"type" : "button",

							"x" : 117,
							"y" : 108,

							"tooltip_text" : localeInfo.SAFEBOX_TITLE,

							"default_image" : "d:/ymir work/ui/safebox_normal.tga",
							"over_image" : "d:/ymir work/ui/safebox_hover.tga",
							"down_image" : "d:/ymir work/ui/safebox_down.tga",
						},
						## MallButton
						{
							"name" : "MallButton",
							"type" : "button",

							"x" : 117,
							"y" : 147,

							"tooltip_text" : localeInfo.MALL_TITLE,

							"default_image" : "d:/ymir work/ui/game/TaskBar/Mall_Button_01.tga",
							"over_image" : "d:/ymir work/ui/game/TaskBar/Mall_Button_02.tga",
							"down_image" : "d:/ymir work/ui/game/TaskBar/Mall_Button_03.tga",
						},
						## CostumeButton
						{
							"name" : "CostumeButton",
							"type" : "button",

							"x" : 77,
							"y" : 4,

							"tooltip_text" : localeInfo.COSTUME_TITLE,

							"default_image" : "d:/ymir work/ui/game/taskbar/costume_Button_01.tga",
							"over_image" : "d:/ymir work/ui/game/taskbar/costume_Button_02.tga",
							"down_image" : "d:/ymir work/ui/game/taskbar/costume_Button_03.tga",
						},						
						{
							"name" : "Equipment_Tab_01",
							"type" : "radio_button",

							"x" : 86,
							"y" : 161,

							"default_image" : "d:/ymir work/ui/game/windows/tab_button_small_01.sub",
							"over_image" : "d:/ymir work/ui/game/windows/tab_button_small_02.sub",
							"down_image" : "d:/ymir work/ui/game/windows/tab_button_small_03.sub",

							"children" :
							(
								{
									"name" : "Equipment_Tab_01_Print",
									"type" : "text",

									"x" : 0,
									"y" : 0,

									"all_align" : "center",

									"text" : "I",
								},
							),
						},
						{
							"name" : "Equipment_Tab_02",
							"type" : "radio_button",

							"x" : 86 + 32,
							"y" : 161,

							"default_image" : "d:/ymir work/ui/game/windows/tab_button_small_01.sub",
							"over_image" : "d:/ymir work/ui/game/windows/tab_button_small_02.sub",
							"down_image" : "d:/ymir work/ui/game/windows/tab_button_small_03.sub",

							"children" :
							(
								{
									"name" : "Equipment_Tab_02_Print",
									"type" : "text",

									"x" : 0,
									"y" : 0,

									"all_align" : "center",

									"text" : "II",
								},
							),
						},

					),
				},

				{
					"name" : "Inventory_Tab_01",
					"type" : "radio_button",

					"x" : 6 + 33*0,
					"y" : 33 + 191,

					"default_image" : "d:/ymir work/ui/game/windows/tab_button_small_01.sub",
					"over_image" : "d:/ymir work/ui/game/windows/tab_button_small_02.sub",
					"down_image" : "d:/ymir work/ui/game/windows/tab_button_small_03.sub",
					"tooltip_text" : localeInfo.INVENTORY_PAGE_BUTTON_TOOLTIP_1,

					"children" :
					(
						{
							"name" : "Inventory_Tab_01_Print",
							"type" : "text",

							"x" : 0,
							"y" : 0,

							"all_align" : "center",

							"text" : "I",
						},
					),
				},
				{
					"name" : "Inventory_Tab_02",
					"type" : "radio_button",

					"x" : 6 + 33*1,
					"y" : 33 + 191,

					"default_image" : "d:/ymir work/ui/game/windows/tab_button_small_01.sub",
					"over_image" : "d:/ymir work/ui/game/windows/tab_button_small_02.sub",
					"down_image" : "d:/ymir work/ui/game/windows/tab_button_small_03.sub",
					"tooltip_text" : localeInfo.INVENTORY_PAGE_BUTTON_TOOLTIP_2,

					"children" :
					(
						{
							"name" : "Inventory_Tab_02_Print",
							"type" : "text",

							"x" : 0,
							"y" : 0,

							"all_align" : "center",

							"text" : "II",
						},
					),
				},
				
				{
					"name" : "Inventory_Tab_03",
					"type" : "radio_button",

					"x" : 6 + 33*2,
					"y" : 33 + 191,

					"default_image" : "d:/ymir work/ui/game/windows/tab_button_small_01.sub",
					"over_image" : "d:/ymir work/ui/game/windows/tab_button_small_02.sub",
					"down_image" : "d:/ymir work/ui/game/windows/tab_button_small_03.sub",
					"tooltip_text" : localeInfo.INVENTORY_PAGE_BUTTON_TOOLTIP_3,

					"children" :
					(
						{
							"name" : "Inventory_Tab_03_Print",
							"type" : "text",

							"x" : 0,
							"y" : 0,

							"all_align" : "center",

							"text" : "III",
						},
					),
				},
				
				{
					"name" : "Inventory_Tab_04",
					"type" : "radio_button",

					"x" : 6 + 33*3,
					"y" : 33 + 191,

					"default_image" : "d:/ymir work/ui/game/windows/tab_button_small_01.sub",
					"over_image" : "d:/ymir work/ui/game/windows/tab_button_small_02.sub",
					"down_image" : "d:/ymir work/ui/game/windows/tab_button_small_03.sub",
					"tooltip_text" : localeInfo.INVENTORY_PAGE_BUTTON_TOOLTIP_4,

					"children" :
					(
						{
							"name" : "Inventory_Tab_04_Print",
							"type" : "text",

							"x" : 0,
							"y" : 0,

							"all_align" : "center",

							"text" : "IV",
						},
					),
				},
				
				{
					"name" : "Inventory_Tab_05",
					"type" : "radio_button",

					"x" : 6 + 33*4,
					"y" : 33 + 191,

					"default_image" : "d:/ymir work/ui/game/windows/tab_button_small_01.sub",
					"over_image" : "d:/ymir work/ui/game/windows/tab_button_small_02.sub",
					"down_image" : "d:/ymir work/ui/game/windows/tab_button_small_03.sub",
					"tooltip_text" : localeInfo.INVENTORY_PAGE_BUTTON_TOOLTIP_5,

					"children" :
					(
						{
							"name" : "Inventory_Tab_05_Print",
							"type" : "text",

							"x" : 0,
							"y" : 0,

							"all_align" : "center",

							"text" : "V",
						},
					),
				},

				## Item Slot
				{
					"name" : "ItemSlot",
					"type" : "grid_table",

					"x" : 8,
					"y" : 246,

					"start_index" : 0,
					"x_count" : 5,
					"y_count" : 9,
					"x_step" : 32,
					"y_step" : 32,

					"image" : "d:/ymir work/ui/public/Slot_Base.sub"
				},

				## Print DR
				{
					"name":"DR_Slot",
					"type":"image",

					"x":31,
					"y":48,

					"vertical_align":"bottom",

					"image" : "d:/ymir work/ui/public/parameter_slot_02.sub",

					"children" :
					(
						{
							"name":"DR_Icon",
							"type":"image",

							"x":-18,
							"y":2,

							"image":"d:/ymir work/ui/game/windows/money_icon.sub",
						},

						{
							"name" : "DR",
							"type" : "text",

							"x" : 3,
							"y" : 3,

							"horizontal_align" : "right",
							"text_horizontal_align" : "right",

							"text" : "123456789",
						},
					),
				},

				## Print DM
				{
					"name":"DM_Slot",
					"type":"image",

					"x":100,
					"y":48,

					"vertical_align":"bottom",
					"image" : "d:/ymir work/ui/public/parameter_slot_02.sub",

					"children" :
					(
						{
							"name" : "DM",
							"type" : "text",

							"x" : 3,
							"y" : 3,

							"horizontal_align" : "right",
							"text_horizontal_align" : "right",

							"text" : "123456789",
						},
					),
				},

				## Print Money
				{
					"name":"Money_Slot",
					"type":"button",

					"x":8,
					"y":28,

					"horizontal_align":"center",
					"vertical_align":"bottom",

					"default_image" : "d:/ymir work/ui/public/parameter_slot_05.sub",
					"over_image" : "d:/ymir work/ui/public/parameter_slot_05.sub",
					"down_image" : "d:/ymir work/ui/public/parameter_slot_05.sub",

					"children" :
					(
						{
							"name":"Money_Icon",
							"type":"image",

							"x":-18,
							"y":2,

							"image":"d:/ymir work/ui/game/windows/money_icon.sub",
						},

						{
							"name" : "Money",
							"type" : "text",

							"x" : 3,
							"y" : 3,

							"horizontal_align" : "right",
							"text_horizontal_align" : "right",

							"text" : "123456789",
						},
					),
				},

			),
		},
	),
}
