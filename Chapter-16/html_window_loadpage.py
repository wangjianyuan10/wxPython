import wx
import wx.html

class MyHtmlFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, -1, title, size=(600,400))
        html = wx.html.HtmlWindow(self)
        if "gtk2" in wx.PlatformInfo:
            html.SetStandardFonts()

        wx.CallAfter(
            html.LoadPage, "E:/programs/2/H5/Day01/文档/01Html基础.html")

app = wx.App()
frm = MyHtmlFrame(None, "Simple HTML Browser")
frm.Show()
app.MainLoop()
