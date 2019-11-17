#!/usr/bin/env python
# coding:utf-8
 
"Integrated Simpler Web Browser for testing web2py apps"
 
__author__ = "Mariano Reingart (reingart@gmail.com)"
__copyright__ = "Copyright (C) 2011 Mariano Reingart"
__license__ = "GPL 3.0"
  
# Based on wxPython examples (HTML2 using IE on Windows and webkit on Linux)
 
  
import os
import sys
import wx
 
DEFAULT_URL = 'http://www.baidu.com'
 
import wx.html2 as webview
 
 
class BrowserPanel(wx.Panel):
    """wxWebView - Componente wxPython que embebe un navegador (IE/WebKit)
    """
    def __init__(self, parent, *args, **kwargs): 
        wx.Panel.__init__(self, parent, *args, **kwargs)
        self.parent = parent
 
        self.current = "http://www.baidu.com"
        sizer = wx.BoxSizer(wx.VERTICAL)
        btnSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.webview = webview.WebView.New(self)
        self.Bind(webview.EVT_WEBVIEW_NAVIGATING, self.OnWebViewNavigating, self.webview)
        self.Bind(webview.EVT_WEBVIEW_LOADED, self.OnWebViewLoaded, self.webview)
     
        btn = wx.Button(self, -1, "Open", style=wx.BU_EXACTFIT)
        self.Bind(wx.EVT_BUTTON, self.OnOpenButton, btn)
        btnSizer.Add(btn, 0, wx.EXPAND|wx.ALL, 2)
 
        btn = wx.Button(self, -1, "<--", style=wx.BU_EXACTFIT)
        self.Bind(wx.EVT_BUTTON, self.OnPrevPageButton, btn)
        btnSizer.Add(btn, 0, wx.EXPAND|wx.ALL, 2)
        self.Bind(wx.EVT_UPDATE_UI, self.OnCheckCanGoBack, btn)
 
        btn = wx.Button(self, -1, "-->", style=wx.BU_EXACTFIT)
        self.Bind(wx.EVT_BUTTON, self.OnNextPageButton, btn)
        btnSizer.Add(btn, 0, wx.EXPAND|wx.ALL, 2)
        self.Bind(wx.EVT_UPDATE_UI, self.OnCheckCanGoForward, btn)
 
        btn = wx.Button(self, -1, "Stop", style=wx.BU_EXACTFIT)
        self.Bind(wx.EVT_BUTTON, self.OnStopButton, btn)
        btnSizer.Add(btn, 0, wx.EXPAND|wx.ALL, 2)
 
        btn = wx.Button(self, -1, "Refresh", style=wx.BU_EXACTFIT)
        self.Bind(wx.EVT_BUTTON, self.OnRefreshPageButton, btn)
        btnSizer.Add(btn, 0, wx.EXPAND|wx.ALL, 2)
 
        txt = wx.StaticText(self, -1, "Location:")
        btnSizer.Add(txt, 0, wx.CENTER|wx.ALL, 2)
 
        self.location = wx.ComboBox(
            self, -1, "", style=wx.CB_DROPDOWN|wx.TE_PROCESS_ENTER)
        self.location.AppendItems(['http://www.baidu.com',
                                   'http://www.qq.com',
                                   'http://google.com'])
        self.Bind(wx.EVT_COMBOBOX, self.OnLocationSelect, self.location)
        self.location.Bind(wx.EVT_TEXT_ENTER, self.OnLocationEnter)
        btnSizer.Add(self.location, 1, wx.EXPAND|wx.ALL, 2)
 
        sizer.Add(btnSizer, 0, wx.EXPAND)
        sizer.Add(self.webview, 1, wx.EXPAND)
        self.SetSizer(sizer)
 
    def LoadURL(self, url):
        self.webview.LoadURL(url)
 
    # WebView events
    def OnWebViewNavigating(self, evt):
        # this event happens prior to trying to get a resource
        pass
        #evt.Veto()
 
    def OnWebViewLoaded(self, evt):
        # The full document has loaded
        self.current = evt.GetURL()
        self.location.SetValue(self.current)
        self.parent.SetTitle(self.webview.GetCurrentTitle())
 
    # Control bar events
    def OnLocationSelect(self, evt):
        url = self.location.GetStringSelection()
        self.webview.LoadURL(url)
 
    def OnLocationEnter(self, evt):
        url = self.location.GetValue()
        self.location.Append(url)
        self.webview.LoadURL(url)
 
    def OnOpenButton(self, event):
        dlg = wx.TextEntryDialog(self, "Open Location",
                                "Enter a full URL or local path",
                                self.current, wx.OK|wx.CANCEL)
        dlg.CentreOnParent()
 
        if dlg.ShowModal() == wx.ID_OK:
            self.current = dlg.GetValue()
            self.webview.LoadURL(self.current)
 
        dlg.Destroy()
 
    def OnPrevPageButton(self, event):
        self.webview.GoBack()
 
    def OnNextPageButton(self, event):
        self.webview.GoForward()
 
    def OnCheckCanGoBack(self, event):
        event.Enable(self.webview.CanGoBack())
         
    def OnCheckCanGoForward(self, event):
        event.Enable(self.webview.CanGoForward())
 
    def OnStopButton(self, evt):
        self.webview.Stop()
 
    def OnRefreshPageButton(self, evt):
        self.webview.Reload()
 
    def DoBuiltIn(self, event):
        evtid = event.GetId()
        if evtid == wx.ID_COPY:
            self.webview.Copy()
        elif evtid == wx.ID_PASTE:
            self.webview.Paste()
        elif evtid == wx.ID_CUT:
            self.webview.Cut()
        elif evtid == wx.ID_DELETE:
            self.webview.DeleteSelection()
        elif evtid == wx.ID_UNDO:
            self.webview.Undo()
        elif evtid == wx.ID_REDO:
            self.webview.Redo()
        elif evtid == wx.ID_FIND:
            dlg = wx.TextEntryDialog(self, 'Search:', 'Find', '')
            if dlg.ShowModal() == wx.ID_OK:
                text = dlg.GetValue()
                self.webview.Find(text)
            dlg.Destroy()
 
 
class SimpleBrowser(wx.Frame):
 
    def __init__(self):
        wx.Frame.__init__(self, None)
        self.Show()
        self.panel = BrowserPanel(self)
 
 
if __name__ == '__main__':
    app = wx.App()
    browser = SimpleBrowser()
    #browser.panel.Open(url)
    app.MainLoop()
 
