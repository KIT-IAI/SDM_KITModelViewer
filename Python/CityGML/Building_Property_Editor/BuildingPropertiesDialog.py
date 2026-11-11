# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 4.2.1-0-g80c4cb6)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

import gettext
_ = gettext.gettext

###########################################################################
## Class BuildingPropertiesDialog
###########################################################################

class BuildingPropertiesDialog ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"CityGML Building Properties Editor"), pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer1 = wx.BoxSizer( wx.VERTICAL )

        fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
        fgSizer1.AddGrowableCol( 1 )
        fgSizer1.SetFlexibleDirection( wx.VERTICAL )
        fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_gmlIdText = wx.StaticText( self, wx.ID_ANY, _(u"GML ID"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_gmlIdText.Wrap( -1 )

        fgSizer1.Add( self.m_gmlIdText, 0, wx.ALL, 5 )

        self.m_gmlId = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer1.Add( self.m_gmlId, 1, wx.ALL|wx.EXPAND, 5 )

        self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, _(u"Building Function"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText9.Wrap( -1 )

        fgSizer1.Add( self.m_staticText9, 0, wx.ALL, 5 )

        self.m_buildingFunction = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer1.Add( self.m_buildingFunction, 1, wx.ALL|wx.EXPAND, 5 )

        self.m_yearOfConstructionText = wx.StaticText( self, wx.ID_ANY, _(u"Year of Construction"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_yearOfConstructionText.Wrap( -1 )

        fgSizer1.Add( self.m_yearOfConstructionText, 0, wx.ALL, 5 )

        self.m_yearOfConstruction = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer1.Add( self.m_yearOfConstruction, 1, wx.ALL|wx.EXPAND, 5 )

        self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, _(u"Roof Type"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText4.Wrap( -1 )

        fgSizer1.Add( self.m_staticText4, 0, wx.ALL, 5 )

        self.m_roofType = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer1.Add( self.m_roofType, 1, wx.ALL|wx.EXPAND, 5 )

        self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, _(u"Building Height"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )

        fgSizer1.Add( self.m_staticText3, 0, wx.ALL, 5 )

        fgSizer3 = wx.FlexGridSizer( 0, 2, 0, 0 )
        fgSizer3.AddGrowableCol( 0 )
        fgSizer3.SetFlexibleDirection( wx.BOTH )
        fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_buildingHeight = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_RIGHT )
        fgSizer3.Add( self.m_buildingHeight, 1, wx.ALL|wx.EXPAND, 5 )

        self.m_buildingHeightUnit = wx.StaticText( self, wx.ID_ANY, _(u"---"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_buildingHeightUnit.Wrap( -1 )

        fgSizer3.Add( self.m_buildingHeightUnit, 0, wx.ALIGN_BOTTOM|wx.ALL, 5 )


        fgSizer1.Add( fgSizer3, 1, wx.EXPAND, 5 )

        self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, _(u"Storeys above Ground"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText5.Wrap( -1 )

        fgSizer1.Add( self.m_staticText5, 0, wx.ALL, 5 )

        self.m_storeysAboveGround = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer1.Add( self.m_storeysAboveGround, 1, wx.ALL|wx.EXPAND, 5 )

        self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, _(u"Storey Heights above Ground"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText6.Wrap( -1 )

        fgSizer1.Add( self.m_staticText6, 0, wx.ALL, 5 )

        self.m_storeyHeightsAboveGround = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer1.Add( self.m_storeyHeightsAboveGround, 1, wx.ALL|wx.EXPAND, 5 )

        self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, _(u"Storeys below Ground"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText7.Wrap( -1 )

        fgSizer1.Add( self.m_staticText7, 0, wx.ALL, 5 )

        self.m_storeysBelowGround = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer1.Add( self.m_storeysBelowGround, 1, wx.ALL|wx.EXPAND, 5 )

        self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, _(u"Storey Heights below Ground"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText8.Wrap( -1 )

        fgSizer1.Add( self.m_staticText8, 0, wx.ALL, 5 )

        self.m_storeyHeightsBelowGround = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer1.Add( self.m_storeyHeightsBelowGround, 1, wx.ALL|wx.EXPAND, 5 )


        bSizer1.Add( fgSizer1, 0, wx.EXPAND, 5 )

        fgSizer4 = wx.FlexGridSizer( 0, 3, 0, 0 )
        fgSizer4.AddGrowableCol( 1 )
        fgSizer4.SetFlexibleDirection( wx.BOTH )
        fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_buttonUpdateSelection = wx.Button( self, wx.ID_ANY, _(u"Update Selection"), wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer4.Add( self.m_buttonUpdateSelection, 0, wx.ALL, 5 )

        self.m_buttonUpdateData = wx.Button( self, wx.ID_ANY, _(u"Update Data"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_buttonUpdateData.Enable( False )

        fgSizer4.Add( self.m_buttonUpdateData, 0, wx.ALL, 5 )

        self.m_buttonClose = wx.Button( self, wx.ID_OK, _(u"Close"), wx.DefaultPosition, wx.DefaultSize, 0 )

        self.m_buttonClose.SetDefault()
        fgSizer4.Add( self.m_buttonClose, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


        bSizer1.Add( fgSizer4, 0, wx.EXPAND, 5 )


        self.SetSizer( bSizer1 )
        self.Layout()
        bSizer1.Fit( self )

        self.Centre( wx.BOTH )

        # Connect Events
        self.m_gmlId.Bind( wx.EVT_TEXT, self.OnGmlIdChanged )
        self.m_buildingFunction.Bind( wx.EVT_TEXT, self.OnFunctionChanged )
        self.m_yearOfConstruction.Bind( wx.EVT_TEXT, self.OnYearOfConstructionChanged )
        self.m_roofType.Bind( wx.EVT_TEXT, self.OnRoofTypeChanged )
        self.m_buildingHeight.Bind( wx.EVT_TEXT, self.OnBuildingHeightChanged )
        self.m_storeysAboveGround.Bind( wx.EVT_TEXT, self.OnStoreyAboveGroundChanged )
        self.m_storeyHeightsAboveGround.Bind( wx.EVT_TEXT, self.OnStoreyHeightsAboveGroundChanged )
        self.m_storeysBelowGround.Bind( wx.EVT_TEXT, self.OnStoreyBelowGroundChanged )
        self.m_storeyHeightsBelowGround.Bind( wx.EVT_TEXT, self.OnStoreyHeightsBelowGroundChanged )
        self.m_buttonUpdateSelection.Bind( wx.EVT_BUTTON, self.OnButtonUpdateSelection )
        self.m_buttonUpdateData.Bind( wx.EVT_BUTTON, self.OnButtonUpdateData )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def OnGmlIdChanged( self, event ):
        event.Skip()

    def OnFunctionChanged( self, event ):
        event.Skip()

    def OnYearOfConstructionChanged( self, event ):
        event.Skip()

    def OnRoofTypeChanged( self, event ):
        event.Skip()

    def OnBuildingHeightChanged( self, event ):
        event.Skip()

    def OnStoreyAboveGroundChanged( self, event ):
        event.Skip()

    def OnStoreyHeightsAboveGroundChanged( self, event ):
        event.Skip()

    def OnStoreyBelowGroundChanged( self, event ):
        event.Skip()

    def OnStoreyHeightsBelowGroundChanged( self, event ):
        event.Skip()

    def OnButtonUpdateSelection( self, event ):
        event.Skip()

    def OnButtonUpdateData( self, event ):
        event.Skip()


