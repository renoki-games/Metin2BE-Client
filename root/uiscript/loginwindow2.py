import uiScriptLocale

LOCAL_PATH = uiScriptLocale.LOGIN_PATH
ETC_PATH = "d:/ymir work/ui/public/"
#LOCAL_PATH = "d:/de/ui/login/"

CH_START_X = 4
CH_STEP_X = 80

CH_TEXT_1_Y = 30
CH_TEXT_2_Y = 50

BUTTON_START_X = 25
BUTTON_START_Y = 411
BUTTON_STEP_X = 385
BUTTON_STEP_Y = 46

SAFE_INPUT_X = 425
SAFE_INPUT_START_Y = 115
SAFE_INPUT_STEP_Y = 55

window = {
	"sytle" : ("movable",),
	"x" : 0, "y" : 0,
	"width" : SCREEN_WIDTH,
	"height" : SCREEN_HEIGHT,
	"children" : 
	(
		{
			"name" : "background", 
			"type" : "expanded_image",
			"x" : 0, "y" : 0,
			"x_scale" : float(SCREEN_WIDTH) / 1920.0,
			"y_scale" : float(SCREEN_HEIGHT) / 1080.0,
			"image" : LOCAL_PATH + "background.jpg",
			"children" : 
			(
				{
					"name" : "board_main",
					"type" : "thinboard",
					"x" : 0, "y" : 170,
					"width" : 520, "height" : 350,
					"vertical_align" : "center",
					"horizontal_align" : "center",
					"children" :
					(
						{
							"name" : "VerticalLine1",
							"type" : "line",

							"x" : 520/2,
							"y" : 5,
							"width" : 0,
							"height" : 275,
							"color" : 0xff777777,
						},
						{
							"name" : "HorizontalLine1",
							"type" : "line",

							"x" : 5,
							"y" : 280,
							"width" : 510,
							"height" : 0,
							"color" : 0xff777777,
						},
						{
							"name" : "board",
							"type" : "image",
							"x" : 0, "y" : 0,
							"width" : 208,
							"height" : 30,
							"children" :
							(
								{
									"name" : "exit_button",
									"type" : "button",
									"x" : 733, "y" : 15,
									"default_image" : ETC_PATH + "close_button_01.sub",
									"over_image" :  ETC_PATH + "close_button_02.sub",
									"down_image" : ETC_PATH + "close_button_03.sub",
								},
							)
						},
							
						## LOGIN
						{
							"name" : "input_user",
							"type" : "image",
							"x" : 40, "y" : 105,
							"image" : ETC_PATH + "parameter_slot_03.sub",
							"children" : (
								{
									"name" : "id",
									"type" : "editline",
									"x" : 50, "y" : 8,
									"width" : 200, "height" : 16,
									"color" : 0xffc96820,
									"fontsize":"XLARGE",
									"input_limit": 16,
								},
							),
						},
						{
							"name" : "input_password",
							"type" : "image",
							"x" : 40, "y" : 174,
							"image" : ETC_PATH + "parameter_slot_03.sub",
							"children" : 
							(
								{
									"name" : "pwd",
									"type" : "editline",
									"x" : 50, "y" : 8,
									"width" : 200, "height" : 16,
									"color" : 0xffc96820,
									"fontsize":"XLARGE",
									"input_limit": 16,
									"secret_flag": 1,
								},
							),
						},
						{
							"name" : "ch1",
							"type" : "radio_button",
							"x" : CH_START_X + CH_STEP_X*0, "y" : 5,
							"default_image" : ETC_PATH + "ch1_down.sub",
							"over_image" : ETC_PATH + "ch1_hover.sub",
							"down_image" : ETC_PATH + "ch1_active.sub",
							"children" : 
							(
								{
									"name" : "player_ch1",
									"type" : "text",

									"x" : 0, "y" : CH_TEXT_1_Y,
									"color" : 0xff656565,
									"fontsize":"LARGE",
									"horizontal_align" : "center", "text_horizontal_align" : "center",

									"text" : "-------",
								},
								{
									"name" : "state_ch1",
									"type" : "text",

									"x" : 0, "y" : CH_TEXT_2_Y,
									"color" : 0xff656565,
									"fontsize":"LARGE",
									"horizontal_align" : "center", "text_horizontal_align" : "center",

									"text" : "OFFLINE",
								},
							),
						},
						{
							"name" : "ch2",
							"type" : "radio_button",
							"x" : CH_START_X + CH_STEP_X*1, "y" : 5,
							"default_image" : LOCAL_PATH + "ch2_down.sub",
							"over_image" : LOCAL_PATH + "ch2_hover.sub",
							"down_image" : LOCAL_PATH + "ch2_active.sub",
							"children" : 
							(
								{
									"name" : "player_ch2",
									"type" : "text",

									"x" : 0, "y" : CH_TEXT_1_Y,
									"color" : 0xff656565,
									"fontsize":"LARGE",
									"horizontal_align" : "center", "text_horizontal_align" : "center",

									"text" : "-------",
								},
								{
									"name" : "state_ch2",
									"type" : "text",

									"x" : 0, "y" : CH_TEXT_2_Y,
									"color" : 0xff656565,
									"fontsize":"LARGE",
									"horizontal_align" : "center", "text_horizontal_align" : "center",

									"text" : "OFFLINE",
								},
							),
						},
						{
							"name" : "ch3",
							"type" : "radio_button",
							"x" : CH_START_X + CH_STEP_X*2, "y" : 5,
							"default_image" : LOCAL_PATH + "ch3_down.sub",
							"over_image" : LOCAL_PATH + "ch3_hover.sub",
							"down_image" : LOCAL_PATH + "ch3_active.sub",
							"children" : 
							(
								{
									"name" : "player_ch3",
									"type" : "text",

									"x" : 0, "y" : CH_TEXT_1_Y,
									"color" : 0xff656565,
									"fontsize":"LARGE",
									"horizontal_align" : "center", "text_horizontal_align" : "center",

									"text" : "-------",
								},
								{
									"name" : "state_ch3",
									"type" : "text",

									"x" : 0, "y" : CH_TEXT_2_Y,
									"color" : 0xff656565,
									"fontsize":"LARGE",
									"horizontal_align" : "center", "text_horizontal_align" : "center",

									"text" : "OFFLINE",
								},
							),
						},
						{
							"name" : "ch4",
							"type" : "radio_button",
							"x" : CH_START_X + CH_STEP_X*3, "y" : 5,
							"default_image" : LOCAL_PATH + "ch4_down.sub",
							"over_image" : LOCAL_PATH + "ch4_hover.sub",
							"down_image" : LOCAL_PATH + "ch4_active.sub",
							"children" : 
							(
								{
									"name" : "player_ch4",
									"type" : "text",

									"x" : 0, "y" : CH_TEXT_1_Y,
									"color" : 0xff656565,
									"fontsize":"LARGE",
									"horizontal_align" : "center", "text_horizontal_align" : "center",

									"text" : "-------",
								},
								{
									"name" : "state_ch4",
									"type" : "text",

									"x" : 0, "y" : CH_TEXT_2_Y,
									"color" : 0xff656565,
									"fontsize":"LARGE",
									"horizontal_align" : "center", "text_horizontal_align" : "center",

									"text" : "OFFLINE",
								},
							),
						},
						
						{
							"name" : "login_button",
							"type" : "button",
							"x" : 61, "y" : 333,
							"default_image" : ETC_PATH + "xlarge_button_01.sub",
							"over_image" : ETC_PATH + "xlarge_button_02.sub",
							"down_image" : ETC_PATH + "xlarge_button_03.sub",
						},
						
						## ACCOUNT-MANAGEMENT
						{
							"name" : "input_safe_f1",
							"type" : "image",
							"x" : SAFE_INPUT_X, "y" : SAFE_INPUT_START_Y+SAFE_INPUT_STEP_Y*0,
							"image" : LOCAL_PATH + "input_safe_f1.sub",
							"children" : 
							(
								{
									"name" : "platzhalter_f1",
									"type" : "text",

									"x" : 50, "y" : 8,
									"color" : 0xff790000,
									"fontsize": "XLARGE",

									"text" : "Leer",
								},
								# {
									# "name" : "id",
									# "type" : "editline",
									# "x" : 50, "y" : 8,
									# "width" : 200, "height" : 16,
									# "color" : 0xffc45a02,
									# "fontsize":"XLARGE",
									# "input_limit": 16,
								# },
							),
						},
						{
							"name" : "input_safe_f2",
							"type" : "image",
							"x" : SAFE_INPUT_X, "y" : SAFE_INPUT_START_Y+SAFE_INPUT_STEP_Y*1,
							"image" : LOCAL_PATH + "input_safe_f2.sub",
							"children" : 
							(
								{
									"name" : "platzhalter_f2",
									"type" : "text",

									"x" : 50, "y" : 8,
									"color" : 0xff790000,
									"fontsize": "XLARGE",

									"text" : "Leer",
								},
								# {
									# "name" : "id",
									# "type" : "editline",
									# "x" : 50, "y" : 8,
									# "width" : 200, "height" : 16,
									# "color" : 0xffc45a02,
									# "fontsize":"XLARGE",
									# "input_limit": 16,
								# },
							),
						},
						{
							"name" : "input_safe_f3",
							"type" : "image",
							"x" : SAFE_INPUT_X, "y" : SAFE_INPUT_START_Y+SAFE_INPUT_STEP_Y*2,
							"image" : LOCAL_PATH + "input_safe_f3.sub",
							"children" : 
							(
								{
									"name" : "platzhalter_f3",
									"type" : "text",

									"x" : 50, "y" : 8,
									"color" : 0xff790000,
									"fontsize": "XLARGE",

									"text" : "Leer",
								},
								# {
									# "name" : "id",
									# "type" : "editline",
									# "x" : 50, "y" : 8,
									# "width" : 200, "height" : 16,
									# "color" : 0xffc45a02,
									# "fontsize":"XLARGE",
									# "input_limit": 16,
								# },
							),
						},
						{
							"name" : "input_safe_f4",
							"type" : "image",
							"x" : SAFE_INPUT_X, "y" : SAFE_INPUT_START_Y+SAFE_INPUT_STEP_Y*3,
							"image" : LOCAL_PATH + "input_safe_f4.sub",
							"children" : 
							(
								{
									"name" : "platzhalter_f4",
									"type" : "text",

									"x" : 50, "y" : 8,
									"color" : 0xff790000,
									"fontsize": "XLARGE",

									"text" : "Leer",
								},
								# {
									# "name" : "id",
									# "type" : "editline",
									# "x" : 50, "y" : 8,
									# "width" : 200, "height" : 16,
									# "color" : 0xffc45a02,
									# "fontsize":"XLARGE",
									# "input_limit": 16,
								# },
							),
						},
						## BUTTONS
						{
							"name" : "save_button",
							"type" : "button",
							"x" : 460 , "y" : 350,
							"default_image" : LOCAL_PATH + "button_safe_normal.sub",
							"over_image" : LOCAL_PATH + "button_safe_hover.sub",
							"down_image" : LOCAL_PATH + "button_safe_click.sub",
						},
						{
							"name" : "edit_button",
							"type" : "toggle_button",
							"x" : 460 + 130 , "y" : 350,
							"default_image" : LOCAL_PATH + "button_edit_normal.sub",
							"over_image" : LOCAL_PATH + "button_edit_hover.sub",
							"down_image" : LOCAL_PATH + "button_edit_click.sub",
						},
						{
							"name" : "delete_button_acc1",
							"type" : "button",
							"x" : SAFE_INPUT_X + 280, "y" : SAFE_INPUT_START_Y+SAFE_INPUT_STEP_Y*0 + 4,
							"default_image" : LOCAL_PATH + "delete_normal.sub",
							"over_image" : LOCAL_PATH + "deleter_hover.sub",
							"down_image" : LOCAL_PATH + "delete_click.sub",
						},
						{
							"name" : "delete_button_acc2",
							"type" : "button",
							"x" : SAFE_INPUT_X + 280, "y" : SAFE_INPUT_START_Y+SAFE_INPUT_STEP_Y*1 + 4,
							"default_image" : LOCAL_PATH + "delete_normal.sub",
							"over_image" : LOCAL_PATH + "deleter_hover.sub",
							"down_image" : LOCAL_PATH + "delete_click.sub",
						},
						{
							"name" : "delete_button_acc3",
							"type" : "button",
							"x" : SAFE_INPUT_X + 280, "y" : SAFE_INPUT_START_Y+SAFE_INPUT_STEP_Y*2 + 4,
							"default_image" : LOCAL_PATH + "delete_normal.sub",
							"over_image" : LOCAL_PATH + "deleter_hover.sub",
							"down_image" : LOCAL_PATH + "delete_click.sub",
						},
						{
							"name" : "delete_button_acc4",
							"type" : "button",
							"x" : SAFE_INPUT_X + 280, "y" : SAFE_INPUT_START_Y+SAFE_INPUT_STEP_Y*3 + 4,
							"default_image" : LOCAL_PATH + "delete_normal.sub",
							"over_image" : LOCAL_PATH + "deleter_hover.sub",
							"down_image" : LOCAL_PATH + "delete_click.sub",
						},
						##########################################################################################
						
						## BUTTONS
						{
							"name" : "homepage_button",
							"type" : "button",
							"x" : BUTTON_START_X+BUTTON_STEP_X*0 , "y" : BUTTON_START_Y+BUTTON_STEP_Y*0,
							"default_image" : LOCAL_PATH + "button_homepage_normal.sub",
							"over_image" : LOCAL_PATH + "button_homepage_hover.sub",
							"down_image" : LOCAL_PATH + "button_homepage_click.sub",
						},
						{
							"name" : "register_button",
							"type" : "button",
							"x" : BUTTON_START_X+BUTTON_STEP_X*0 , "y" : BUTTON_START_Y+BUTTON_STEP_Y*1,
							"default_image" : LOCAL_PATH + "button_register_normal.sub",
							"over_image" : LOCAL_PATH + "button_register_hover.sub",
							"down_image" : LOCAL_PATH + "button_register_click.sub",
						},
						{
							"name" : "forum_button",
							"type" : "button",
							"x" : BUTTON_START_X+BUTTON_STEP_X*1 , "y" : BUTTON_START_Y+BUTTON_STEP_Y*0,
							"default_image" : LOCAL_PATH + "button_forum_normal.sub",
							"over_image" : LOCAL_PATH + "button_forum_hover.sub",
							"down_image" : LOCAL_PATH + "button_forum_click.sub",
						},
						{
							"name" : "changelog_button",
							"type" : "button",
							"x" : BUTTON_START_X+BUTTON_STEP_X*1 , "y" : BUTTON_START_Y+BUTTON_STEP_Y*1,
							"default_image" : LOCAL_PATH + "button_changelog_normal.sub",
							"over_image" : LOCAL_PATH + "button_changelog_hover.sub",
							"down_image" : LOCAL_PATH + "button_changelog_click.sub",
						},
					),
				},
			),
		},
	),
},