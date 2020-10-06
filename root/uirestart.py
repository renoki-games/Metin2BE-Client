import dbg
import app
import net
if app.RENEWAL_DEAD_PACKET:
	import player
	import localeInfo

import ui

###################################################################################################
## Restart
class RestartDialog(ui.ScriptWindow):

	def __init__(self):
		ui.ScriptWindow.__init__(self)

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def LoadDialog(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "uiscript/restartdialog.py")
		except Exception, msg:
			import sys
			(type, msg, tb)=sys.exc_info()
			dbg.TraceError("RestartDialog.LoadDialog - %s:%s" % (type, msg))
			app.Abort()
			return 0

		try:
			self.restartHereButton=self.GetChild("restart_here_button")
			self.restartTownButton=self.GetChild("restart_town_button")
		except:
			import sys
			(type, msg, tb)=sys.exc_info()
			dbg.TraceError("RestartDialog.LoadDialog - %s:%s" % (type, msg))
			app.Abort()
			return 0

		self.restartHereButton.SetEvent(ui.__mem_func__(self.RestartHere))
		self.restartTownButton.SetEvent(ui.__mem_func__(self.RestartTown))
		if app.RENEWAL_DEAD_PACKET:
			self.reviveTimeStamp = [0 for i in xrange(player.REVIVE_TYPE_MAX)]
			self.reviveTimeTexts = map(lambda i:self.GetChild("T{:02d}".format(i)), xrange(player.REVIVE_TYPE_MAX))

		return 1

	def Destroy(self):
		self.restartHereButton=0
		self.restartTownButton=0
		if app.RENEWAL_DEAD_PACKET:
			del self.reviveTimeStamp[:]
			del self.reviveTimeTexts[:]
		self.ClearDictionary()

	if app.RENEWAL_DEAD_PACKET:
		def OpenDialog(self, times):
			for x in xrange(player.REVIVE_TYPE_MAX):
				self.reviveTimeStamp[x] = app.GetTime() + times[x]
				self.reviveTimeTexts[x].Show()
			self.restartHereButton.Disable()
			self.restartTownButton.Disable()
			self.Show()

		def OnUpdate(self):
			for x in xrange(player.REVIVE_TYPE_MAX): 
				endtime = self.reviveTimeStamp[x] - app.GetTime()
				if endtime <= .1:
					self.reviveTimeTexts[x].Hide()
					if x == player.REVIVE_TYPE_HERE:
						self.restartHereButton.Enable()
					if x == player.REVIVE_TYPE_TOWN:
						self.restartTownButton.Enable()

				if x == player.REVIVE_TYPE_AUTO_TOWN:
					self.reviveTimeTexts[x].SetText(localeInfo.REVIVE_AUTO_TOWN_MESSAGE.format(localeInfo.SecondToMS(endtime)))
				else:
					self.reviveTimeTexts[x].SetText("{0:.1f}".format(endtime))
	else:
		def OpenDialog(self):
			self.Show()

	def Close(self):
		self.Hide()
		return True

	def RestartHere(self):
		net.SendChatPacket("/restart_here")

	def RestartTown(self):
		net.SendChatPacket("/restart_town")

	def OnPressExitKey(self):
		return True

	def OnPressEscapeKey(self):
		return True
