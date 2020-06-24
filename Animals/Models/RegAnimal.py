import wx
import wx.xrc

class signupWindow(wx.Frame):
    def __init__(self, parent):

        """
        class signupWindow(wx.Frame):
            def __init__(self, parent):

                Creating the register frame, hat includes a form to add an animal instance
        """

        self.mainFrame = parent

        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Animal Register Form", pos = wx.DefaultPosition, size = wx.Size( 720,480 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )

        bSizer1 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText7.Wrap( -1 )
        bSizer1.Add( self.m_staticText7, 0, wx.ALL, 5 )

        self.LabelName = wx.StaticText( self, wx.ID_ANY, u"Name:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.LabelName.Wrap( -1 )
        bSizer1.Add( self.LabelName, 0, wx.ALL, 5 )

        self.animalName = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTRE )
        self.animalName.SetMaxLength( 20 ) 
        bSizer1.Add( self.animalName, 0, wx.ALL|wx.EXPAND, 5 )

        self.LabelColor = wx.StaticText( self, wx.ID_ANY, u"Color:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.LabelColor.Wrap( -1 )
        bSizer1.Add( self.LabelColor, 0, wx.ALL, 5 )
        
        self.animalColor = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTRE )
        self.animalColor.SetMaxLength( 20 ) 
        bSizer1.Add( self.animalColor, 0, wx.ALL|wx.EXPAND, 5 )

        self.LabelAge = wx.StaticText( self, wx.ID_ANY, u"Age:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.LabelAge.Wrap( -1 )
        bSizer1.Add( self.LabelAge, 0, wx.ALL, 5 )

        self.animalAge = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTRE )
        self.animalAge.SetMaxLength( 2 ) 
        bSizer1.Add( self.animalAge, 0, wx.ALL|wx.EXPAND, 5 )
        
        self.LabelFriendly = wx.StaticText( self, wx.ID_ANY, u"Animal:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.LabelFriendly.Wrap( -1 )
        bSizer1.Add( self.LabelFriendly, 0, wx.ALL, 5 )
           
        dogFriendChoices = [ u"Cat", u"Dog" ]
        self.animalType = wx.ComboBox( self, wx.ID_ANY, u"Select One...", wx.DefaultPosition, wx.DefaultSize, dogFriendChoices, 0 )
        bSizer1.Add( self.animalType, 0, wx.ALL|wx.EXPAND, 5 )

        self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText5.Wrap( -1 )
        bSizer1.Add( self.m_staticText5, 0, wx.ALL, 5 )

        #"""
        #Boton used to add a new animal instance
        #"""
        
        self.Save = wx.Button( self, wx.ID_ANY, u"Sign Up", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer1.Add( self.Save, 0, wx.ALL|wx.EXPAND, 5 )
        
        self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText6.Wrap( -1 )
        bSizer1.Add( self.m_staticText6, 0, wx.ALL, 5 )

        #"""
        #Boton used to fill the form from the beginning
        #"""
        self.again = wx.Button( self, wx.ID_ANY, u"New", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer1.Add( self.again, 0, wx.ALIGN_CENTER, 5 )

        #"""
        #Boton used to go to the main frame
        #"""      
        
        self.return_main = wx.Button( self, wx.ID_ANY, u"Continue", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer1.Add( self.return_main, 0, wx.ALIGN_CENTER, 5 )
        
        
        self.SetSizer( bSizer1 )
        self.Layout()
        
        self.Centre( wx.BOTH )

        #"""
		# Connect Events
        #"""
        self.Save.Bind(wx.EVT_BUTTON, self.Saving)
        self.again.Bind( wx.EVT_BUTTON, self.ReFill)
        self.return_main.Bind( wx.EVT_BUTTON, self.Continue)


    def Continue(self, event):
        """
        def Continue(self, event):

        Method to close the form and redirect to the main frame/window
        """
        self.Close()

    def ReFill(self, event):
        """
        def ReFill(self, event):

        Method to add another dog instance
        """
        self.animalName.SetValue("")
        self.animalAge.SetValue("")
        self.animalColor.SetValue("")
        self.animalType.SetValue("")

    def Saving(self, event):
        """
        def Saving(self, event):

        Method to save the values of the dog instance created before
        """
        aName = self.animalName.GetValue()
        aAge = self.animalAge.GetValue()
        aColor = self.animalColor.GetValue()
        aType = self.animalType.GetValue()

        if aType == "Cat":
            self.mainFrame.form_cats(aName, aAge, aColor)

        elif aType == "Dog":
            self.mainFrame.form_dogs(aName, aAge, aColor)
              

        wx.MessageBox(aName +' has been added', aType+' Agregado', wx.OK | wx.ICON_INFORMATION)
