import wx
import wx.xrc

class ventanaCat(wx.Frame):
    def __init__(self, parent):

        self.mainFrame = parent

        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Agregar Gato", pos = wx.DefaultPosition, size = wx.Size( 720,480 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )

        bSizer1 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText7.Wrap( -1 )
        bSizer1.Add( self.m_staticText7, 0, wx.ALL, 5 )

        self.LabelName = wx.StaticText( self, wx.ID_ANY, u"Name:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.LabelName.Wrap( -1 )
        bSizer1.Add( self.LabelName, 0, wx.ALL, 5 )

        self.catName = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTRE )
        self.catName.SetMaxLength( 20 ) 
        bSizer1.Add( self.catName, 0, wx.ALL|wx.EXPAND, 5 )

        self.LabelColor = wx.StaticText( self, wx.ID_ANY, u"Color:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.LabelColor.Wrap( -1 )
        bSizer1.Add( self.LabelColor, 0, wx.ALL, 5 )
        
        self.catColor = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTRE )
        self.catColor.SetMaxLength( 20 ) 
        bSizer1.Add( self.catColor, 0, wx.ALL|wx.EXPAND, 5 )

        self.LabelAge = wx.StaticText( self, wx.ID_ANY, u"Age:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.LabelAge.Wrap( -1 )
        bSizer1.Add( self.LabelAge, 0, wx.ALL, 5 )

        self.catAge = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTRE )
        self.catAge.SetMaxLength( 2 ) 
        bSizer1.Add( self.catAge, 0, wx.ALL|wx.EXPAND, 5 )
        
        self.LabelNotes = wx.StaticText( self, wx.ID_ANY, u"Notes:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.LabelNotes.Wrap( -1 )
        bSizer1.Add( self.LabelNotes, 0, wx.ALL, 5 )
        
        self.catNotes = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
        self.catNotes.SetMaxLength( 99 ) 
        bSizer1.Add( self.catNotes, 0, wx.ALL|wx.EXPAND, 5 )

        self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText5.Wrap( -1 )
        bSizer1.Add( self.m_staticText5, 0, wx.ALL, 5 )
        
        self.Save = wx.Button( self, wx.ID_ANY, u"Registrar", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer1.Add( self.Save, 0, wx.ALL|wx.EXPAND, 5 )
        
        self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText6.Wrap( -1 )
        bSizer1.Add( self.m_staticText6, 0, wx.ALL, 5 )

        self.again = wx.Button( self, wx.ID_ANY, u"Nuevo", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer1.Add( self.again, 0, wx.ALIGN_CENTER, 5 )
        
        self.return_main = wx.Button( self, wx.ID_ANY, u"Continuar", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer1.Add( self.return_main, 0, wx.ALIGN_CENTER, 5 )
        
        
        self.SetSizer( bSizer1 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
		# Connect Events
        self.Save.Bind(wx.EVT_BUTTON, self.Saving)
        self.again.Bind( wx.EVT_BUTTON, self.ReFill)
        self.return_main.Bind( wx.EVT_BUTTON, self.Continue)

    def Continue(self, event):
        self.Close()

    def ReFill(self, event):
        self.catName.SetValue("")
        self.catAge.SetValue("")
        self.catColor.SetValue("")
        self.catNotes.SetValue("")
        pass

    def Saving(self, event):

        cName = self.catName.GetValue()
        cAge = self.catAge.GetValue()
        cColor = self.catColor.GetValue()
        cNotes = self.catNotes.GetValue()

        self.mainFrame.form_gatos(cName, cAge, cColor)

        wx.MessageBox(cName +' ha sido agregado', 'Gato Agregado', wx.OK | wx.ICON_INFORMATION)
