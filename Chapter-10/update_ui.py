import wx



class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1,
                          "UPDATE_UI Menu Example")
        p = wx.Panel(self)
        self.btn = wx.Button(p, -1, "Disable Item", (20,20))
        self.Bind(wx.EVT_BUTTON, self.OnToggleItem, self.btn)
        
        menu = wx.Menu()
        menu.Append(wx.NewIdRef(), "Simple menu item")
        self.enabled = True
        self.Bind(wx.EVT_MENU, self.OnSimple, id=wx.NewIdRef())
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateSimple, id=wx.NewIdRef())
        
        menu.AppendSeparator()
        menu.Append(wx.ID_EXIT, "Exit")
        self.Bind(wx.EVT_MENU, self.OnExit, id=wx.ID_EXIT)
                  
        menuBar = wx.MenuBar()
        menuBar.Append(menu, "Menu")
        self.SetMenuBar(menuBar)

        
    def OnSimple(self, event):
        wx.MessageBox("You selected the simple menu item")

    def OnExit(self, event):
        self.Close()

    def OnToggleItem(self, event):
        self.btn.SetLabel(
            (self.enabled and "Enable" or "Disable") + " Item")
        self.enabled = not self.enabled

    def OnUpdateSimple(self, event):
        event.Enable(self.enabled)
        

if __name__ == "__main__":
    app = wx.App()
    frame = MyFrame()
    frame.Show()
    app.MainLoop()

    
