#!/usr/bin/env python

import wx
import abstractmodel

class SimpleName(abstractmodel.AbstractModel):
    
    def __init__(self, first="", last=""):
        abstractmodel.AbstractModel.__init__(self)
        self.set(first, last)
        
    def set(self, first, last):
        self.first = first
        self.last = last
        self.update()                                     

class ModelExample(wx.Frame):
    
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'Flintstones', 
                size=(340, 200))
        panel = wx.Panel(self)   
        panel.SetBackgroundColour("Brown")
        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow) 
        self.textFields = {}
        self.createTextFields(panel)     
        self.model = SimpleName()                         
        self.model.addListener(self.OnUpdate)             
        self.createButtonBar(panel)
        
    def buttonData(self):
        return (("Fredify", self.OnFred),
                ("Wilmafy", self.OnWilma),
                ("Barnify", self.OnBarney),
                ("Bettify", self.OnBetty))
        
    def createButtonBar(self, panel, yPos = 0):
        xPos = 0
        for eachLabel, eachHandler in self.buttonData():
            pos = (xPos, yPos)
            button = wx.Button(panel, -1, eachLabel, pos)
            self.Bind(wx.EVT_BUTTON, eachHandler, button)
            xPos += button.GetSize().width
        
       
    def textFieldData(self):
        return (("First Name", (10, 50)),
                ("Last Name", (10, 80)))
        
    def createTextFields(self, panel):
        for eachLabel, eachPos in self.textFieldData():
            static = wx.StaticText(panel, 100, eachLabel, eachPos)
            static.SetBackgroundColour("White")
            textPos = (eachPos[0] + 75, eachPos[1])
            self.textFields[eachLabel] = wx.TextCtrl(panel, 101, 
                "", size=(100, -1), pos=textPos,
                style=wx.TE_READONLY)
        
    def OnUpdate(self, model):
        self.textFields["First Name"].SetValue(model.first)    
        self.textFields["Last Name"].SetValue(model.last)      
        
    def OnFred(self, event):                                   
        self.model.set("Fred", "Flintstone")                   
                                                               
    def OnBarney(self, event):                                 
        self.model.set("Barney", "Rubble")                     
                                                               
    def OnWilma(self, event):                                  
        self.model.set("Wilma", "Flintstone")                  
                                                               
    def OnBetty(self, event):                                  
        self.model.set("Betty", "Rubble")                      
        
    def OnCloseWindow(self, event):
        self.Destroy()
            
if __name__ == '__main__':
    app = wx.App()
    frame = ModelExample(parent=None, id=-1)
    frame.Show()
    app.MainLoop()
    
