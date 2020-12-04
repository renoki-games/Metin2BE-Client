######################################## AICI INCEPE TREABA ######################################## ORA: 21:36
import app, net, ui, snd, wndMgr, dbg, os
import musicInfo, systemSetting
import localeInfo as _localeInfo
localeInfo = _localeInfo.localeInfo()
import constInfo, localeInfo, uicommon
import ime
import serverInfo
import serverCommandParser
import time
import ServerStateChecker
import serverlogindata
import uiCommon

class LoginWindow(ui.ScriptWindow):
	languages = [ "de", "en", "tr" ]

	def __init__(self, stream):
		ui.ScriptWindow.__init__(self)
		
		net.SetPhaseWindow(net.PHASE_WINDOW_LOGIN, self)
		net.SetAccountConnectorHandler(self)

		self.AccountManager = [
									[None, None],
									[None, None],
									[None, None],
									[None, None],
								]
		self.AccountManagerData	= [
								["", ""],
								["", ""],
								["", ""],
								["", ""],
							  	]

		self.stateCH		= [None, None, None, None]
		self.channelCount	= [None, None, None, None]
		self.stream = stream
		self.isDown = False

		if hasattr(app, "ENABLE_LANG_SYSTEM"):
			self.language_buttons = {}
		
	def __del__(self):
		ui.ScriptWindow.__del__(self)
		
		net.ClearPhaseWindow(net.PHASE_WINDOW_LOGIN, self)
		net.SetAccountConnectorHandler(0)

	def LoadAccountData(self):
		with open('account.cfg', 'r+') as content_file:
			encContent = content_file.read()
			content = app.DecryptByHWID(encContent)
			
			if ';' in content:
				accounts = content.split(';')
				for idx, account in enumerate(accounts):
					if ':#:' in account:
						data = account.split(':#:')
						self.AccountManagerData[idx][0] = data[0]
						self.AccountManagerData[idx][1] = data[1]
		
		
		for idx, account in enumerate(self.AccountManagerData):
			if account[0] != "":
				self.AccountManager[idx][0].SetText(account[0])
				self.AccountManager[idx][0].SetFontColor(0.8549, 0.8549, 0.8549)

	def SaveAccountData(self):
		with open('account.cfg', 'w+') as content_file:
			data = self.AccountManagerData[0][0] + ':#:' + self.AccountManagerData[0][1] + ';'
			data += self.AccountManagerData[1][0] + ':#:' + self.AccountManagerData[1][1] + ';'
			data += self.AccountManagerData[2][0] + ':#:' + self.AccountManagerData[2][1] + ';'
			data += self.AccountManagerData[3][0] + ':#:' + self.AccountManagerData[3][1] + ';'
			
			encData = app.EncryptByHWID(data)
			content_file.write(encData)

	def Open(self):
		ServerStateChecker.Create(self)
		self.__RefreshServerStateList()
		ServerStateChecker.Request()

		self.loginFailureMsgDict={

			"ALREADY"	: localeInfo.LOGIN_FAILURE_ALREAY,
			"NOID"		: localeInfo.LOGIN_FAILURE_NOT_EXIST_ID,
			"WRONGPWD"	: localeInfo.LOGIN_FAILURE_WRONG_PASSWORD,
			"FULL"		: localeInfo.LOGIN_FAILURE_TOO_MANY_USER,
			"SHUTDOWN"	: localeInfo.LOGIN_FAILURE_SHUTDOWN,
			"REPAIR"	: localeInfo.LOGIN_FAILURE_REPAIR_ID,
			"BLOCK"		: localeInfo.LOGIN_FAILURE_BLOCK_ID,
			"WRONGMAT"	: localeInfo.LOGIN_FAILURE_WRONG_MATRIX_CARD_NUMBER,
			"QUIT"		: localeInfo.LOGIN_FAILURE_WRONG_MATRIX_CARD_NUMBER_TRIPLE,
			"BESAMEKEY"	: localeInfo.LOGIN_FAILURE_BE_SAME_KEY,
			"NOTAVAIL"	: localeInfo.LOGIN_FAILURE_NOT_AVAIL,
			"NOBILL"	: localeInfo.LOGIN_FAILURE_NOBILL,
			"BLKLOGIN"	: localeInfo.LOGIN_FAILURE_BLOCK_LOGIN,
			"WEBBLK"	: localeInfo.LOGIN_FAILURE_WEB_BLOCK,
		}

		self.loginFailureFuncDict = {
			"WRONGPWD"	: localeInfo.LOGIN_FAILURE_WRONG_PASSWORD,
			"WRONGMAT"	: localeInfo.LOGIN_FAILURE_WRONG_MATRIX_CARD_NUMBER,
			"QUIT"		: app.Exit,
		}

		self.SetSize(wndMgr.GetScreenWidth(), wndMgr.GetScreenHeight())
		self.SetWindowName("LoginWindow")
		self.__BuildKeyDict()

		self.__LoadScript("UIScript/loginwindow.py")
		# if not self.__LoadScript(localeInfo.LOCALE_UISCRIPT_PATH + "LoginWindow.py"):
			# dbg.TraceError("LoginWindow.Open - __LoadScript Error")
			# return
		
		if musicInfo.loginMusic != "":
			snd.SetMusicVolume(systemSetting.GetMusicVolume())
			snd.FadeInMusic("BGM/" + musicInfo.loginMusic)

		snd.SetSoundVolume(systemSetting.GetSoundVolume())

		ime.AddExceptKey(91)
		ime.AddExceptKey(93)
		self.SetChannel(0)

		if not os.path.exists('account.cfg'):
			self.SaveAccountData()
		
		self.LoadAccountData()
		
		self.Show()
		app.ShowCursor()	

	def Close(self):
		self.serverList					= None
		self.channelList				= None
		self.onPressKeyDict 			= None

		if hasattr(app, "ENABLE_LANG_SYSTEM"):
			self.language_buttons = {}

		self.AccountManager = [
									[None, None],
									[None, None],
									[None, None],
									[None, None],
								]
		self.AccountManagerData	= None

		self.stateCH = [None, None, None, None]
		self.channelCount	= [None, None, None, None]

		if musicInfo.loginMusic != "" and musicInfo.selectMusic != "":
			snd.FadeOutMusic("BGM/"+musicInfo.loginMusic)
	
		if self.stream.popupWindow:
			self.stream.popupWindow.Close()
	
		self.Hide()
		app.HideCursor()
		ime.ClearExceptKey()

	def __BuildKeyDict(self):
		onPressKeyDict = {}

		onPressKeyDict[app.DIK_F1]	= lambda : self.loginWithHotkey(1)
		onPressKeyDict[app.DIK_F2]	= lambda : self.loginWithHotkey(2)
		onPressKeyDict[app.DIK_F3]	= lambda : self.loginWithHotkey(3)
		onPressKeyDict[app.DIK_F4]	= lambda : self.loginWithHotkey(4)

		self.onPressKeyDict = onPressKeyDict

	def OnKeyDown(self, key):
		try:
			self.onPressKeyDict[key]()
		except KeyError:
			pass
		except:
			raise

		return TRUE

	def OnConnectFailure(self):
		snd.PlaySound("sound/ui/loginfail.wav")
		self.PopupNotifyMessage(localeInfo.LOGIN_CONNECT_FAILURE, self.EmptyFunc)

	def OnHandShake(self):
		snd.PlaySound("sound/ui/loginok.wav")
		self.PopupDisplayMessage(localeInfo.LOGIN_CONNECT_SUCCESS)

	def OnLoginStart(self):
		self.PopupDisplayMessage(localeInfo.LOGIN_PROCESSING)

	def OnLoginFailure(self, error):
		ServerStateChecker.Request()
		try:
			loginFailureMsg = self.loginFailureMsgDict[error]
		except KeyError:
		
			loginFailureMsg = localeInfo.LOGIN_FAILURE_UNKNOWN  + error

		loginFailureFunc = self.loginFailureFuncDict.get(error, self.EmptyFunc)

		self.PopupNotifyMessage(loginFailureMsg, loginFailureFunc)

		snd.PlaySound("sound/ui/loginfail.wav")

	def __LoadScript(self, fileName):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, fileName)
		except:
			import exception
			exception.Abort("LoginWindow.__LoadScript.LoadObject")

		try:
			self.serverName			= self.GetChild("ServerName")
			self.idEditLine			= self.GetChild("id")
			self.pwdEditLine		= self.GetChild("pwd")

			self.stateCH[0]			= self.GetChild("state_ch1")
			self.stateCH[1]			= self.GetChild("state_ch2")
			self.stateCH[2]			= self.GetChild("state_ch3")
			self.stateCH[3]			= self.GetChild("state_ch4")

			self.channelCount[0]	= self.GetChild("player_ch1")
			self.channelCount[1]	= self.GetChild("player_ch2")
			self.channelCount[2]	= self.GetChild("player_ch3")
			self.channelCount[3]	= self.GetChild("player_ch4")

			self.loginButton		= self.GetChild("login_button")
			self.exitButton			= self.GetChild("exit_button")

			self.homepageButton		= self.GetChild("homepage_button")
			self.registerButton		= self.GetChild("register_button")
			self.forumButton		= self.GetChild("forum_button")
			self.changelogButton	= self.GetChild("changelog_button")

			self.saveButton			= self.GetChild("save_button")
			self.editButton			= self.GetChild("edit_button")

			self.AccountManager[0][0]	= self.GetChild("platzhalter_f1")
			self.AccountManager[0][1]	= self.GetChild("delete_button_acc1")

			self.AccountManager[1][0]	= self.GetChild("platzhalter_f2")
			self.AccountManager[1][1]	= self.GetChild("delete_button_acc2")

			self.AccountManager[2][0]	= self.GetChild("platzhalter_f3")
			self.AccountManager[2][1]	= self.GetChild("delete_button_acc3")

			self.AccountManager[3][0]	= self.GetChild("platzhalter_f4")
			self.AccountManager[3][1]	= self.GetChild("delete_button_acc4")
			
			self.f1Button			= self.GetChild("f1_button")
			self.f2Button			= self.GetChild("f2_button")
			self.f3Button			= self.GetChild("f3_button")
			self.f4Button			= self.GetChild("f4_button")

			self.channelButton = {
				0 : self.GetChild("ch1"),
				1 :	self.GetChild("ch2"),
				2 : self.GetChild("ch3"),
				3 : self.GetChild("ch4")}

			if hasattr(app, "ENABLE_LANG_SYSTEM"):
				for	index, name in enumerate(self.languages):
					self.language_buttons[name] = self.GetChild("flag_{}".format(name))

		except:
			import exception
			exception.Abort("LoginWindow.__LoadScript.BindObject")
			
				
		for (channelID, channelButtons) in self.channelButton.items():
				channelButtons.SetEvent(ui.__mem_func__(self.SetChannel), channelID)
		
		self.serverName.SetText("%s" % (serverlogindata.SRV_LIST[0][0][0]))
		
		self.loginButton.SetEvent(ui.__mem_func__(self.__OnClickLoginButton))
		self.exitButton.SetEvent(ui.__mem_func__(self.OnPressExitKey))

		self.homepageButton.SetEvent(ui.__mem_func__(self.GoHomepage))
		self.registerButton.SetEvent(ui.__mem_func__(self.GoRegister))
		self.forumButton.SetEvent(ui.__mem_func__(self.GoForum))
		self.changelogButton.SetEvent(ui.__mem_func__(self.GoChangelog))

		self.idEditLine.SetReturnEvent(ui.__mem_func__(self.pwdEditLine.SetFocus))
		self.idEditLine.SetTabEvent(ui.__mem_func__(self.pwdEditLine.SetFocus))
		self.pwdEditLine.SetReturnEvent(ui.__mem_func__(self.__OnClickLoginButton))
		self.pwdEditLine.SetTabEvent(ui.__mem_func__(self.idEditLine.SetFocus))
		self.idEditLine.SetFocus()

		self.saveButton.SetEvent(ui.__mem_func__(self.__OnClickAccountSave))
		self.editButton.SetToggleDownEvent(lambda arg=0: self.__OnClickEditButton(arg))
		self.editButton.SetToggleUpEvent(lambda arg=1: self.__OnClickEditButton(arg))

		self.f1Button.SAFE_SetEvent(self.loginWithHotkey, 1)
		self.f2Button.SAFE_SetEvent(self.loginWithHotkey, 2)
		self.f3Button.SAFE_SetEvent(self.loginWithHotkey, 3)
		self.f4Button.SAFE_SetEvent(self.loginWithHotkey, 4)

		self.AccountManager[0][1].SAFE_SetEvent(self.__OnClickAccountErase, 0)
		self.AccountManager[1][1].SAFE_SetEvent(self.__OnClickAccountErase, 1)
		self.AccountManager[2][1].SAFE_SetEvent(self.__OnClickAccountErase, 2)
		self.AccountManager[3][1].SAFE_SetEvent(self.__OnClickAccountErase, 3)

		for i in range(len(self.AccountManager)):
			self.AccountManager[i][1].Hide()

		if hasattr(app, "ENABLE_LANG_SYSTEM"):
			for	index, name in enumerate(self.languages):
				self.language_buttons[name].SAFE_SetEvent(self.SetLanguage, index)

		self.RefreshLanguageButtons()

	if hasattr(app, "ENABLE_LANG_SYSTEM"):
		def RefreshLanguageButtons(self):
			for language_button_name, language_button in self.language_buttons.iteritems():
				language_name = systemSetting.GetLanguageShortString()

				if language_name == language_button_name:
					language_button.Down()
				else:
					language_button.SetUp()

		def SetLanguage(self, language_index):
			if systemSetting.GetLanguage() == language_index:
				return

			systemSetting.SetLanguage(language_index)

			localeInfo.CreateLocaleConfig(language_index)
			localeInfo.SetDefaultCodePage(language_index)

			self.RefreshLanguageButtons()
			self.RestartClient()

		def RestartClient(self):
			app.Exit()
			os.system('start Metin2-BlackEdition.exe')

	def OnUpdate(self):
		ServerStateChecker.Update()
		
	def SetChannel(self, ch):
		for key, button in self.channelButton.items():
			button.SetUp()

		serverIP = serverlogindata.MAIN_SERVER_IP
			
		self.channelButton[ch].Down()
		self.stream.SetConnectInfo(serverIP, self.ChannelPort(ch, 0), serverIP, self.ChannelPort("LOGIN"))

		net.SetMarkServer(serverIP, self.ChannelPort("LOGO"))
		app.SetGuildMarkPath("10.tga")
		app.SetGuildSymbolPath("10")
		net.SetServerInfo(self.ChannelPort(ch, 2))
		
	def ChannelPort(self, ch, value=0):
		channel = {
			0	:	serverlogindata.SRV_LIST[0][0][3][0][2],
			1	:	serverlogindata.SRV_LIST[0][0][3][1][2],
			2	:	serverlogindata.SRV_LIST[0][0][3][2][2],
			3	:	serverlogindata.SRV_LIST[0][0][3][3][2],
		}
		
		if ch == "LOGIN":
			return serverlogindata.SRV_LIST[0][0][1]
		elif ch == "LOGO":
			return channel[0]
		elif value == 2:
			return serverlogindata.SRV_LIST[0][0][0] + ", CH%s" % (ch+1)
		else:
			return channel[ch]

	def Connect(self, id, pwd):
		if constInfo.SEQUENCE_PACKET_ENABLE:
			net.SetPacketSequenceMode()
			
		constInfo.LastAccount = id.lower()

		self.stream.popupWindow.Close()
		self.stream.popupWindow.Open(localeInfo.LOGIN_CONNETING, self.EmptyFunc, localeInfo.UI_CANCEL)

		self.stream.SetLoginInfo(id, pwd)
		self.stream.Connect()
		
	def PopupDisplayMessage(self, msg):
		self.stream.popupWindow.Close()
		self.stream.popupWindow.Open(msg)

	def PopupNotifyMessage(self, msg, func=0):
		if not func:
			func = self.EmptyFunc

		self.stream.popupWindow.Close()
		self.stream.popupWindow.Open(msg, func, localeInfo.UI_OK)

	def OnPressExitKey(self):
		if self.stream.popupWindow:
			self.stream.popupWindow.Close()
		self.stream.SetPhaseWindow(0)
		return TRUE

	def __GetRegionID(self):
		return 0

	def __GetServerID(self):
		return 0

	def __GetChannelID(self):
		return self.channelList.GetSelectedItem()

## SERVER STATE CHECKER

	def NotifyChannelState(self, key, state, player_count):
		serverlogindata.SERVER_STATE_TABLE[key] = state
		
		serverIndex = self.__GetServerID()
		if (key / 10) == serverIndex:
			try:
				stateName = serverlogindata.STATE_DICT[state]
				stateNameText = serverlogindata.STATE_TEXT_DICT[state]
			except:
				stateName = serverlogindata.STATE_NONE
				stateNameText = serverlogindata.STATE_TEXT_NONE

			channelIndex = key % 10
			channelName = serverlogindata.SRV_LIST[0][serverIndex][3][channelIndex][0]

			self.stateCH[channelIndex].SetText(str(stateNameText))

			if state == 1:
				if player_count > 0:
					self.channelCount[channelIndex].SetText("%d Players" % player_count)
				else:
					self.channelCount[channelIndex].SetText("%d Players" % (serverlogindata.SRV_LIST[0][0][3][0][4]))

				self.stateCH[channelIndex].SetFontColor(128.0 / 255.0, 153.0 / 255.0, 204.0 / 255.0)
				self.channelCount[channelIndex].SetFontColor(128.0 / 255.0, 153.0 / 255.0, 204.0 / 255.0)
			else:
				self.stateCH[channelIndex].SetFontColor(101.0 / 255.0, 101.0 / 255.0, 101.0 / 255.0)
				self.channelCount[channelIndex].SetFontColor(101.0 / 255.0, 101.0 / 255.0, 101.0 / 255.0)
			
	def __RequestServerStateList(self):
		serverIndex = self.__GetServerID()
		channelData = None

		try:
			channelData = serverlogindata.SRV_LIST[0][serverIndex][3]
		except:
			print "LoginWindow::__RequestServerStateList"
			return

		ServerStateChecker.Request()

	def __RefreshServerStateList(self):
		serverIndex = self.__GetServerID()
		channelData = None

		try:
			channelData = serverlogindata.SRV_LIST[0][0][3]
		except:
			print "LoginWindow::__RefreshServerStateList"
			return
			
		for index, channel in enumerate(channelData):
			ServerStateChecker.AddChannel(index, channel[1], channel[2])
			stateName = serverlogindata.STATE_NONE

			print "LoginWindow::__RefreshServerStateList(): key %d, channelName %s, stateName %s" % (index + 1, channel[0], stateName)

## ACCSAVE System ##
	def __OnClickEditButton(self, arg):
		if arg == 0:
			for i in range(len(self.AccountManagerData)):
				if self.AccountManagerData[i][0] != "":
					self.AccountManager[i][1].Show()
		else:
			for i in range(len(self.AccountManager)):
				self.AccountManager[i][1].Hide()

	def __OnClickAccountSave(self):

		for i in range(len(self.AccountManagerData)):
			if self.AccountManagerData[i][0] == "":
				id = self.idEditLine.GetText()
				pwd = self.pwdEditLine.GetText()
				
				if id == "" or pwd == "":
					return

				self.AccountManagerData[i][0] = id
				self.AccountManagerData[i][1] = pwd
				self.SaveAccountData()
				self.AccountManager[i][0].SetText(id)
				self.AccountManager[i][0].SetFontColor(0.8549, 0.8549, 0.8549)
				break

	def __OnClickAccountErase(self, idx):
		self.questionDialog = uiCommon.QuestionDialog()
		self.questionDialog.SetText(localeInfo.REALLY_WANNA_DELETE_ACCOUNT_DATA) #translateme
		self.questionDialog.SetAcceptEvent(lambda arg=idx: self.OnDelAccAcceptEvent(arg))
		self.questionDialog.SetCancelEvent(ui.__mem_func__(self.OnDelAccQuestionCancel))
		self.questionDialog.Open()
		constInfo.SET_ITEM_QUESTION_DIALOG_STATUS(1)
		
	def OnDelAccAcceptEvent(self, idx):
		self.OnCloseQuestionDialog()
		self.AccountManagerData[idx][0] = ""
		self.AccountManagerData[idx][1] = ""
		
		self.AccountManager[idx][0].SetText("Leer")
		self.AccountManager[idx][0].SetFontColor(0.37, 0.37, 0.37)
		self.AccountManager[idx][1].Hide()
		self.SaveAccountData()
		
	def OnDelAccQuestionCancel(self):
		self.OnCloseQuestionDialog()
		
	def OnCloseQuestionDialog(self):
		if not self.questionDialog:
			return
		
		self.questionDialog.Close()
		self.questionDialog = None
		constInfo.SET_ITEM_QUESTION_DIALOG_STATUS(0)
#####################

## BUTTONS ##

	def GoHomepage(self):
		import os
		os.system('@echo off && explorer "http://yumano3.net/"')
		return TRUE

	def GoRegister(self):
		import os
		os.system('@echo off && explorer "http://yumano3.net/register"')
		return TRUE

	def GoForum(self):
		import os
		os.system('@echo off && explorer "http://board.yumano3.net/"')
		return TRUE

	def GoChangelog(self):
		import os
		os.system('@echo off && explorer "http://board.yumano3.net/forum/index.php?thread/4-patchnotes-yumano3/"')
		return TRUE

############################

	def EmptyFunc(self):
		pass

	def __OnClickLoginButton(self):
		id = self.idEditLine.GetText()
		pwd = self.pwdEditLine.GetText()

		if len(id)==0:
			self.PopupNotifyMessage(localeInfo.LOGIN_INPUT_ID, self.EmptyFunc)
			return

		if len(pwd)==0:
			self.PopupNotifyMessage(localeInfo.LOGIN_INPUT_PASSWORD, self.EmptyFunc)
			return

		self.Connect(id, pwd)

	def loginWithHotkey(self, arg):
		self.Connect(self.AccountManagerData[arg-1][0], self.AccountManagerData[arg-1][1])
