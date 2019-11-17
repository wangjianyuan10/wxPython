import wx

class MyForm(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, title="My Menu")
        self.panel = wx.Panel(self, wx.ID_ANY)
        # Create menu bar
        self.menuBar = wx.MenuBar()
        # create check menu
        checkMenu = wx.Menu()
        Item1 = checkMenu.Append(wx.NewIdRef(), "Menu 1", "", wx.ITEM_CHECK)
        self.Bind(wx.EVT_MENU, self.onCheck, Item1)
        Item2 = checkMenu.Append(wx.NewId(), "Menu 2", "", wx.ITEM_CHECK)
        self.Bind(wx.EVT_MENU, self.onCheck, Item2)
        Item3 = checkMenu.Append(wx.ID_ANY, "Menu 3", "", wx.ITEM_CHECK)
        self.Bind(wx.EVT_MENU, self.onCheck, Item3)

        #Create a sub menu
        imp = wx.Menu()
        imp.Append(wx.ID_ANY, 'Import newsfeed list...')
        imp.Append(wx.ID_ANY, 'Import bookmarks...')
        imp.Append(wx.ID_ANY, 'Import mail...')
        #Add the sub menu
        checkMenu.AppendSubMenu(imp, 'I&mport')

        #Create a menu item
        imp_item = wx.MenuItem(checkMenu,wx.ID_ANY,'&Another Import menu')
        #Create a sub menu
        imp2 = wx.Menu()
        imp2.Append(wx.ID_ANY, 'Import newsfeed list...')
        imp2.Append(wx.ID_ANY, 'Import bookmarks...')
        imp2.Append(wx.ID_ANY, 'Import mail...')
        #Set the sub menu
        imp_item.SetSubMenu(imp2)
        #Add item with sub menu to main menu
        checkMenu.Append(imp_item)

        # Attach menu bar to frame
        self.menuBar.Append(checkMenu, "&Check")
        self.SetMenuBar(self.menuBar)

    #----------------------------------------------------------------------
    def onCheck(self, event):
        id_selected = event.GetId()
        print ("id",event.Id)
        print ("Sel",event.Selection)
        print ("chk",event.IsChecked())

#----------------------------------------------------------------------
# Run the program
if __name__ == "__main__":
    app = wx.App(False)
    frame = MyForm().Show()
    app.MainLoop()
