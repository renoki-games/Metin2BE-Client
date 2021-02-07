import ui
import mouseModule

import uiPickMoney
import localeInfo

import chat
import player
import net

import dbg
import re

class TransferSystemWindow(ui.ScriptWindow):
	def __init__(self, layer = "UI"):
		ui.ScriptWindow.__init__(self, layer)

		net.SetTransferHandler(self)

		self.__Initialize()
		self.__LoadWindow()

	def __Initialize(self):
		self.acceptCheckbox = None
		self.itemSlot = None
		self.characterNameInput = None
		self.goldInputButton = None
		self.goldInput = None
		self.acceptButton = None

		self.tooltipItem = None
		self.itemPosition = -1
		self.offerDialog = None

	def Destroy(self):
		if self.offerDialog:
			self.offerDialog.Destroy()

		self.__Initialize()

	def __LoadWindow(self):
		self.__Load_LoadScript("uiscript/transfersystemwindow.py")
		self.__Load_BindObject()
		self.__Load_BindEvents()

		self.offerDialog = uiPickMoney.PickMoneyDialog()
		self.offerDialog.LoadDialog()
		self.offerDialog.SetMax(13)
		self.offerDialog.SetTitleName(localeInfo.TRANSFERSYSTEM_OFFERDIALOG_TITLE)
		self.offerDialog.SetAcceptEvent(ui.__mem_func__(self.OnOffer))

	def __Load_LoadScript(self, fileName):
		try:
			pyScriptLoader = ui.PythonScriptLoader()
			pyScriptLoader.LoadScriptFile(self, fileName)

		except Exception as e:
			dbg.TraceError("TransferSystemWindow.__Load_LoadScript")
			dbg.TraceError("Error: %s" % (e))

	def __Load_BindObject(self):
		try:
			self.GetChild("board").SetCloseEvent(ui.__mem_func__(self.Close))

			self.acceptCheckbox = self.GetChild("acceptCheckbox")
			self.itemSlot = self.GetChild("itemSlot")
			self.characterNameInput = self.GetChild("characterNameInput")

			self.goldInputButton = self.GetChild("goldInputButton")
			self.goldInput = self.GetChild("goldInput")
			self.acceptButton = self.GetChild("acceptButton")

		except Exception as e:
			dbg.TraceError("TransferSystemWindow.__Load_BindObject")
			dbg.TraceError("Error: %s" % (e))

	def __Load_BindEvents(self):
		try:
			self.acceptButton.SAFE_SetEvent(self.Accept)

			self.acceptCheckbox.SetEvent(ui.__mem_func__(self.ChangeTransferStatus), "ON_CHECK")
			self.acceptCheckbox.SetEvent(ui.__mem_func__(self.ChangeTransferStatus), "ON_UNCHECK")

			self.itemSlot.SetOverInItemEvent(ui.__mem_func__(self.OverInItem))
			self.itemSlot.SetOverOutItemEvent(ui.__mem_func__(self.OverOutItem))
			self.itemSlot.SetUnselectItemSlotEvent(ui.__mem_func__(self.ClearItem))
			self.itemSlot.SetUseSlotEvent(ui.__mem_func__(self.ClearItem))
			self.itemSlot.SetSelectEmptySlotEvent(ui.__mem_func__(self.SelectEmptySlot))

			self.characterNameInput.SetEscapeEvent(ui.__mem_func__(self.OnPressEscapeKey))
			self.goldInputButton.SAFE_SetEvent(self.OnOpenOfferDialog)

		except Exception as e:
			dbg.TraceError("TransferSystemWindow.__Load_BindEvents")
			dbg.TraceError("Error: %s" % (e))

	def OverInItem(self):
		if mouseModule.mouseController.isAttached():
			return

		self.tooltipItem.ClearToolTip()
		self.tooltipItem.SetInventoryItem(self.itemPosition)
		self.tooltipItem.ShowToolTip()

	def OverOutItem(self):
		self.tooltipItem.HideToolTip()

	def CanAddItem(self):
		attachedSlotType = mouseModule.mouseController.GetAttachedType()
		attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()

		if not mouseModule.mouseController.isAttached():
			return False

		if attachedSlotType not in [player.SLOT_TYPE_INVENTORY]:
			return False

		if player.IsEquipmentSlot(attachedSlotPos):
			return False

		if self.itemPosition > 0 or self.itemSlot.GetSlotVnum(0) > 0:
			return False

		return True

	def SelectEmptySlot(self):
		if not self.CanAddItem():
			return

		attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
		itemVnum = player.GetItemIndex(attachedSlotPos)

		if not itemVnum:
			return

		self.itemPosition = attachedSlotPos
		self.itemSlot.SetItemSlot(0, itemVnum)

		mouseModule.mouseController.DeattachObject()

	def SetToolTipItem(self, tooltipItem):
		self.tooltipItem = tooltipItem

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def Hide(self):
		ui.ScriptWindow.Hide(self)

	def Show(self):
		ui.ScriptWindow.Show(self)

	def Close(self):
		self.Hide()

	def Open(self):
		self.Show()

	def OnOpenOfferDialog(self):
		self.offerDialog.Open()

	def OnOffer(self, gold):
		self.goldInput.SetText(localeInfo.NumberToMoneyString(gold))

	def CanAccept(self):
		characterName = self.characterNameInput.GetText()

		if not characterName:
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.TRANSFERSYSTEM_PLEASE_REENTER_CHARACTERNAME)
			return False

		return True

	def ClearItem(self):
		self.itemSlot.ClearSlot(0)
		self.itemPosition = -1

	def ClearGoldInput(self):
		self.goldInput.SetText(localeInfo.NumberToMoneyString(0))

	def Clear(self):
		self.ClearItem()
		self.ClearGoldInput()

	def InputsAreFocussed(self):
		if self.characterNameInput.IsFocus():
			self.characterNameInput.KillFocus()
			return True

		if self.goldInput.IsFocus():
			self.goldInput.KillFocus()
			return True

		return False

	def GetGoldInputValue(self):
		if not self.goldInput.GetText() or self.goldInput.GetText() == localeInfo.NumberToMoneyString(0):
			return 0

		value = self.goldInput.GetText()
		value = re.sub('[^0-9]+', '', value)
		value = long(value)
		return value

	def Accept(self):
		if not self.CanAccept():
			return

		characterName = self.characterNameInput.GetText()
		gold = self.GetGoldInputValue()
		itemPosition = self.itemPosition

		net.SendTransferPacket(characterName, gold, itemPosition)
		self.Clear()

	def ChangeTransferStatus(self):
		configParam = "transfer_status"
		configValue = self.acceptCheckbox.GetCheckStatus()
		net.SendChatPacket("/config {} {}".format(configParam, configValue))

	def OnPressEscapeKey(self):
		if self.InputsAreFocussed():
			return False

		self.Close()
		return True

	def BINARY_SetTransferStatus(self, status):	
		self.acceptCheckbox.SetCheckStatus(status)
