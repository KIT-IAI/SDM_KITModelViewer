import BuildingPropertiesDialog
import BuildingProperties
import ifcdb
import wx

class BuildingPropertiesDialogImpl(BuildingPropertiesDialog.BuildingPropertiesDialog):

    def __init__(self, parent):

        self.CurrentBuilding = None

        BuildingPropertiesDialog.BuildingPropertiesDialog.__init__(self, parent)

        self.properties = BuildingProperties.BuildingProperties(self)

    def __del__(self):
        pass

    def OnGmlIdChanged(self, event):
        self.properties.mark_changed("gml:id")
        self.m_buttonUpdateData.Enable(True)

    def OnFunctionChanged(self, event):
        self.properties.mark_changed("bldg:function")
        self.m_buttonUpdateData.Enable(True) 

    def OnYearOfConstructionChanged(self, event):
        self.properties.mark_changed("bldg:yearOfConstruction")
        self.m_buttonUpdateData.Enable(True)

    def OnRoofTypeChanged(self, event):
        self.properties.mark_changed("bldg:roofType")
        self.m_buttonUpdateData.Enable(True)

    def OnBuildingHeightChanged(self, event):
        self.properties.mark_changed("bldg:measuredHeight")
        self.m_buttonUpdateData.Enable(True)

    def OnStoreyAboveGroundChanged(self, event):
        self.properties.mark_changed("bldg:storeysAboveGround")
        self.m_buttonUpdateData.Enable(True)

    def OnStoreyHeightsAboveGroundChanged(self, event):
        self.properties.mark_changed("bldg:storeyHeightsAboveGround")
        self.m_buttonUpdateData.Enable(True)

    def OnStoreyBelowGroundChanged(self, event):
        self.properties.mark_changed("bldg:storeysBelowGround")
        self.m_buttonUpdateData.Enable(True)

    def OnStoreyHeightsBelowGroundChanged(self, event):
        self.properties.mark_changed("bldg:storeyHeightsBelowGround")
        self.m_buttonUpdateData.Enable(True)

    def OnButtonUpdateSelection(self, event):
        self.m_buttonUpdateData.Enable(False)
        self.fillData()

    def OnButtonUpdateData(self, event):
        self.storeData()

    def get_selected_building(self):
        document = ifcdb.get_document()
        selected_entities = document.get_selected_entities()

        if len(selected_entities) != 1:
            wx.MessageBox("Please select only one building!", "Warning", wx.OK | wx.ICON_EXCLAMATION)
            return None

        entity = selected_entities[0]

        if entity.type not in ["bldg:Building", "bldg:BuildingPart"]:
            wx.MessageBox("Selected entity is not a building or building part!", "Warning", wx.OK | wx.ICON_EXCLAMATION)
            return None

        return entity

    def fillData(self):
        
        building = self.get_selected_building()
        
        if building != None:

            self.CurrentBuilding = building
            self.properties.fill(building)
                        
    def storeData(self):

        if self.CurrentBuilding is None:

            wx.MessageBox("No building data available!", "Warning", wx.OK | wx.ICON_EXCLAMATION)
            return

        if not self.properties.store(self.CurrentBuilding):

            wx.MessageBox("Invalid property value!", "Input Error", wx.OK | wx.ICON_ERROR)

        self.m_buttonUpdateData.Enable(False)