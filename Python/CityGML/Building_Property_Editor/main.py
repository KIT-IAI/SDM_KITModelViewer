import ifcdb
import wx
import BuildingPropertiesDialogImpl

def start_building_properties_dialog():

    app = wx.App(False)

    document = ifcdb.get_document()
    document.log_message("CityGML Building Properties Editor")

    dlg = BuildingPropertiesDialogImpl.BuildingPropertiesDialogImpl(None)
    dlg.fillData()
    dlg.ShowModal()
    dlg.Destroy()

start_building_properties_dialog()