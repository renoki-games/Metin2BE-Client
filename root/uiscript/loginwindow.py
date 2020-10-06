import uiScriptLocale

LOCAL_PATH = uiScriptLocale.LOGIN_PATH
ETC_PATH = "d:/ymir work/ui/public/"
#LOCAL_PATH = "d:/de/ui/login/"

CH_START_X = 4
CH_STEP_X = 45

CH_TEXT_1_Y = 30
CH_TEXT_2_Y = 50

BUTTON_START_X = 20
BUTTON_START_Y = 208
BUTTON_STEP_X = 200
BUTTON_STEP_Y = 28

SAFE_INPUT_X = 225
SAFE_INPUT_START_Y = 40
SAFE_INPUT_STEP_Y = 30

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
				"x_scale" : float(SCREEN_WIDTH) / 1024.0,
				"y_scale" : float(SCREEN_HEIGHT) / 768.0,
				"image" : "locale/de/ui/login_bg.jpg",
				"children" : 
				(
					{
						"name" : "board_main",
						"type" : "window",
						"x" : 0, "y" : 40,
						"width" : 420, "height" : 270,
						"vertical_align" : "center",
						"horizontal_align" : "center",
						"children" :(
							{
								"name" : "board",
								"type" : "thinboard",
								"x" : 0, "y" : 0,
								"width" : 420, "height" : 270,
								"children" :(
									{
										"name" : "VerticalLine1",
										"type" : "line",

										"x" : 420/2,
										"y" : 10,
										"width" : 0,
										"height" : 180,
										"color" : 0xff777777,
									},
									{
										"name" : "HorizontalLine1",
										"type" : "line",

										"x" : 10,
										"y" : 200,
										"width" : 400,
										"height" : 0,
										"color" : 0xff777777,
									},
									{
										"name" : "exit_button",
										"type" : "button",
										"x" : 400, "y" : 5,
										"default_image" : ETC_PATH + "close_button_01.sub",
										"over_image" :  ETC_PATH + "close_button_02.sub",
										"down_image" : ETC_PATH + "close_button_03.sub",
									},
									## LOGIN
									{
										"name" : "ServerName",
										"type" : "text",

										"x" : 110, "y" : 8,
										
										"text_horizontal_align" : "center",
										"fontsize":"LARGE",
										"outline" : 1,
										"text" : "Account Management",
									},
									{
										"name" : "input_user",
										"type" : "image",
										"x" : 43, "y" : 28,
										"image" : ETC_PATH + "parameter_slot_05.sub",
										"children" : 
										(
											{
												"name" : "ID",
												"type" : "text",

												"x" : 3, "y" : 2,
												#"outline" : 1,
												"text" : "ID:",
											},
											{
												"name" : "id",
												"type" : "editline",
												"x" : 19, "y" : 2,
												"width" : 200, "height" : 16,
												"input_limit": 16,
											},
										),
									},
									{
										"name" : "input_password",
										"type" : "image",
										"x" : 43, "y" : 55,
										"image" : ETC_PATH + "parameter_slot_05.sub",
										"children" : 
										(
											{
												"name" : "Password",
												"type" : "text",

												"x" : 3, "y" : 2,
												#"outline" : 1,
												"text" : "PW:",
											},
											{
												"name" : "pwd",
												"type" : "editline",
												"x" : 24, "y" : 2,
												"width" : 200, "height" : 16,
												"input_limit": 16,
												"secret_flag": 1,
											},
										),
									},
									{
										"name" : "ch_board",
										"type" : "thinboard_circle",
										"x" : 13, "y" : 85,
										"width" : 187, "height" : 75,
										"children" :(
											{
												"name" : "ch1",
												"type" : "radio_button",
												"x" : CH_START_X + CH_STEP_X*0, "y" : 5,
												"default_image" : ETC_PATH + "small_button_01.sub",
												"over_image" : ETC_PATH + "small_button_02.sub",
												"down_image" : ETC_PATH + "small_button_03.sub",
												"text" : "CH1",
												"children" : 
												(
													{
														"name" : "player_ch1",
														"type" : "text",
														"color" : 0xff494949,
														"x" : 0, "y" : CH_TEXT_1_Y,
														"horizontal_align" : "center", "text_horizontal_align" : "center",

														"text" : "----",
													},
													{
														"name" : "state_ch1",
														"type" : "text",
														"color" : 0xff494949,
														"x" : 0, "y" : CH_TEXT_2_Y,
														"horizontal_align" : "center", "text_horizontal_align" : "center",

														"text" : "OFF",
													},
												),
											},
											{
												"name" : "ch2",
												"type" : "radio_button",
												"x" : CH_START_X + CH_STEP_X*1, "y" : 5,
												"default_image" : ETC_PATH + "small_button_01.sub",
												"over_image" : ETC_PATH + "small_button_02.sub",
												"down_image" : ETC_PATH + "small_button_03.sub",
												"text" : "CH2",
												"children" : 
												(
													{
														"name" : "player_ch2",
														"type" : "text",
														"color" : 0xff494949,
														"x" : 0, "y" : CH_TEXT_1_Y,
														"horizontal_align" : "center", "text_horizontal_align" : "center",

														"text" : "----",
													},
													{
														"name" : "state_ch2",
														"type" : "text",
														"color" : 0xff494949,
														"x" : 0, "y" : CH_TEXT_2_Y,
														"horizontal_align" : "center", "text_horizontal_align" : "center",

														"text" : "OFF",
													},
												),
											},
											{
												"name" : "ch3",
												"type" : "radio_button",
												"x" : CH_START_X + CH_STEP_X*2, "y" : 5,
												"default_image" : ETC_PATH + "small_button_01.sub",
												"over_image" : ETC_PATH + "small_button_02.sub",
												"down_image" : ETC_PATH + "small_button_03.sub",
												"text" : "CH3",
												"children" : 
												(
													{
														"name" : "player_ch3",
														"type" : "text",
														"color" : 0xff494949,
														"x" : 0, "y" : CH_TEXT_1_Y,
														"horizontal_align" : "center", "text_horizontal_align" : "center",

														"text" : "----",
													},
													{
														"name" : "state_ch3",
														"type" : "text",
														"color" : 0xff494949,
														"x" : 0, "y" : CH_TEXT_2_Y,
														"horizontal_align" : "center", "text_horizontal_align" : "center",

														"text" : "OFF",
													},
												),
											},
											{
												"name" : "ch4",
												"type" : "radio_button",
												"x" : CH_START_X + CH_STEP_X*3, "y" : 5,
												"default_image" : ETC_PATH + "small_button_01.sub",
												"over_image" : ETC_PATH + "small_button_02.sub",
												"down_image" : ETC_PATH + "small_button_03.sub",
												"text" : "CH4",
												"children" : 
												(
													{
														"name" : "player_ch4",
														"type" : "text",

														"x" : 0, "y" : CH_TEXT_1_Y,
														"horizontal_align" : "center", "text_horizontal_align" : "center",
														"color" : 0xff494949,
														"text" : "----",
													},
													{
														"name" : "state_ch4",
														"type" : "text",

														"x" : 0, "y" : CH_TEXT_2_Y,
														"horizontal_align" : "center", "text_horizontal_align" : "center",
														"color" : 0xff494949,
														"text" : "OFF",
													},
												),
											},
										),
									},
									
									{
										"name" : "login_button",
										"type" : "button",
										"x" : 62, "y" : 170,
										"default_image" : ETC_PATH + "large_button_01.sub",
										"over_image" : ETC_PATH + "large_button_02.sub",
										"down_image" : ETC_PATH + "large_button_03.sub",
										"text" : "Login",
									},
									
									## ACCOUNT-MANAGEMENT
									{
										"name" : "AccM",
										"type" : "text",

										"x" : SAFE_INPUT_X+30, "y" : 17,
										
										"fontsize":"LARGE",
										"outline" : 1,
										"text" : "Account Management",
									},
									{
										"name" : "f1_button",
										"type" : "button",
										"x" : SAFE_INPUT_X, "y" : SAFE_INPUT_START_Y+SAFE_INPUT_STEP_Y*0,
										"default_image" : ETC_PATH + "xsmall_button_01.sub",
										"over_image" : ETC_PATH + "xsmall_button_02.sub",
										"down_image" : ETC_PATH + "xsmall_button_03.sub",
										"text" : "F1",
										"children" : 
										(
											{
												"name" : "input_safe_f1",
												"type" : "image",
												"x" : 40, "y" : 0,
												"image" : ETC_PATH + "parameter_slot_05.sub",
												"children" : 
												(
													{
														"name" : "platzhalter_f1",
														"type" : "text",
														"color" : 0xff494949,
														"x" : 3, "y" : 2,
														"text" : "Leer",
													},
												),
											},
										),
									},
									{
										"name" : "f2_button",
										"type" : "button",
										"x" : SAFE_INPUT_X, "y" : SAFE_INPUT_START_Y+SAFE_INPUT_STEP_Y*1,
										"default_image" : ETC_PATH + "xsmall_button_01.sub",
										"over_image" : ETC_PATH + "xsmall_button_02.sub",
										"down_image" : ETC_PATH + "xsmall_button_03.sub",
										"text" : "F2",
										"children" : 
										(
											{
												"name" : "input_safe_f2",
												"type" : "image",
												"x" : 40, "y" : 0,
												"image" : ETC_PATH + "parameter_slot_05.sub",
												"children" : 
												(
													{
														"name" : "platzhalter_f2",
														"type" : "text",
														"color" : 0xff494949,
														"x" : 3, "y" : 2,
														"text" : "Leer",
													},
												),
											},
										),
									},
									{
										"name" : "f3_button",
										"type" : "button",
										"x" : SAFE_INPUT_X, "y" : SAFE_INPUT_START_Y+SAFE_INPUT_STEP_Y*2,
										"default_image" : ETC_PATH + "xsmall_button_01.sub",
										"over_image" : ETC_PATH + "xsmall_button_02.sub",
										"down_image" : ETC_PATH + "xsmall_button_03.sub",
										"text" : "F3",
										"children" : 
										(
											{
												"name" : "input_safe_f3",
												"type" : "image",
												"x" : 40, "y" : 0,
												"image" : ETC_PATH + "parameter_slot_05.sub",
												"children" : 
												(
													{
														"name" : "platzhalter_f3",
														"type" : "text",
														"color" : 0xff494949,
														"x" : 3, "y" : 2,
														"text" : "Leer",
													},
												),
											},
										),
									},
									{
										"name" : "f4_button",
										"type" : "button",
										"x" : SAFE_INPUT_X, "y" : SAFE_INPUT_START_Y+SAFE_INPUT_STEP_Y*3,
										"default_image" : ETC_PATH + "xsmall_button_01.sub",
										"over_image" : ETC_PATH + "xsmall_button_02.sub",
										"down_image" : ETC_PATH + "xsmall_button_03.sub",
										"text" : "F4",
										"children" : 
										(
											{
												"name" : "input_safe_f4",
												"type" : "image",
												"x" : 40, "y" : 0,
												"image" : ETC_PATH + "parameter_slot_05.sub",
												"children" : 
												(
													{
														"name" : "platzhalter_f4",
														"type" : "text",
														"color" : 0xff494949,
														"x" : 3, "y" : 2,
														"text" : "Leer",
													},
												),
											},
										),
									},
									{
										"name" : "save_button",
										"type" : "button",
										"x" : 220 , "y" : 167,
										"default_image" : ETC_PATH + "large_button_01.sub",
										"over_image" : ETC_PATH + "large_button_02.sub",
										"down_image" : ETC_PATH + "large_button_03.sub",
										"text" : "Speichern",
									},
									{
										"name" : "edit_button",
										"type" : "toggle_button",
										"x" : 220+90 , "y" : 167,
										"default_image" : ETC_PATH + "large_button_01.sub",
										"over_image" : ETC_PATH + "large_button_02.sub",
										"down_image" : ETC_PATH + "large_button_03.sub",
										"text" : "Bearbeiten",
									},
									## BUTTONS
									{
										"name" : "delete_button_acc1",
										"type" : "button",
										"x" : SAFE_INPUT_X + 153, "y" : SAFE_INPUT_START_Y+SAFE_INPUT_STEP_Y*0 + 2,
										"default_image" : ETC_PATH + "close_button_01.sub",
										"over_image" :  ETC_PATH + "close_button_02.sub",
										"down_image" : ETC_PATH + "close_button_03.sub",
									},
									{
										"name" : "delete_button_acc2",
										"type" : "button",
										"x" : SAFE_INPUT_X + 153, "y" : SAFE_INPUT_START_Y+SAFE_INPUT_STEP_Y*1 + 2,
										"default_image" : ETC_PATH + "close_button_01.sub",
										"over_image" :  ETC_PATH + "close_button_02.sub",
										"down_image" : ETC_PATH + "close_button_03.sub",
									},
									{
										"name" : "delete_button_acc3",
										"type" : "button",
										"x" : SAFE_INPUT_X + 153, "y" : SAFE_INPUT_START_Y+SAFE_INPUT_STEP_Y*2 + 2,
										"default_image" : ETC_PATH + "close_button_01.sub",
										"over_image" :  ETC_PATH + "close_button_02.sub",
										"down_image" : ETC_PATH + "close_button_03.sub",
									},
									{
										"name" : "delete_button_acc4",
										"type" : "button",
										"x" : SAFE_INPUT_X + 153, "y" : SAFE_INPUT_START_Y+SAFE_INPUT_STEP_Y*3 + 2,
										"default_image" : ETC_PATH + "close_button_01.sub",
										"over_image" :  ETC_PATH + "close_button_02.sub",
										"down_image" : ETC_PATH + "close_button_03.sub",
									},
									##########################################################################################
									
									## BUTTONS
									{
										"name" : "homepage_button",
										"type" : "button",
										"x" : BUTTON_START_X+BUTTON_STEP_X*0 , "y" : BUTTON_START_Y+BUTTON_STEP_Y*0,
										"default_image" : ETC_PATH + "xlarge_button_01.sub",
										"over_image" : ETC_PATH + "xlarge_button_02.sub",
										"down_image" : ETC_PATH + "xlarge_button_03.sub",
										"text" : "Homepage",
									},
									{
										"name" : "register_button",
										"type" : "button",
										"x" : BUTTON_START_X+BUTTON_STEP_X*0 , "y" : BUTTON_START_Y+BUTTON_STEP_Y*1,
										"default_image" : ETC_PATH + "xlarge_button_01.sub",
										"over_image" : ETC_PATH + "xlarge_button_02.sub",
										"down_image" : ETC_PATH + "xlarge_button_03.sub",
										"text" : "Registrieren",
									},
									{
										"name" : "forum_button",
										"type" : "button",
										"x" : BUTTON_START_X+BUTTON_STEP_X*1 , "y" : BUTTON_START_Y+BUTTON_STEP_Y*0,
										"default_image" : ETC_PATH + "xlarge_button_01.sub",
										"over_image" : ETC_PATH + "xlarge_button_02.sub",
										"down_image" : ETC_PATH + "xlarge_button_03.sub",
										"text" : "Forum",
									},
									{
										"name" : "changelog_button",
										"type" : "button",
										"x" : BUTTON_START_X+BUTTON_STEP_X*1 , "y" : BUTTON_START_Y+BUTTON_STEP_Y*1,
										"default_image" : ETC_PATH + "xlarge_button_01.sub",
										"over_image" : ETC_PATH + "xlarge_button_02.sub",
										"down_image" : ETC_PATH + "xlarge_button_03.sub",
										"text" : "Changelog",
									},
								),
							},
						),
					},
				),
			},
		),
	}