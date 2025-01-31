import wx
import sys, glob

class DemoFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1,
                          "wx.ListCtrl in wx.LC_ICON mode",
                          size=(600,400))

        # load some images into an image list
        il = wx.ImageList(32,32, True)
        for name in glob.glob("icon??.png"):
            bmp = wx.Bitmap(name, wx.BITMAP_TYPE_PNG)
            il_max = il.Add(bmp)

        # create the list control
        self.list = wx.ListCtrl(self, -1, 
                style=wx.LC_ICON | wx.LC_AUTOARRANGE)

        # assign the image list to it
        self.list.AssignImageList(il, wx.IMAGE_LIST_NORMAL)

        # create some items for the list
        for x in range(25):
            img = x % (il_max+1)
            self.list.InsertItem(x, 
                    "This is item %02d" % x, img)

app = wx.App()
frame = DemoFrame()
frame.Show()
app.MainLoop()
