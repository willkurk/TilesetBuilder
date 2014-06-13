# Image.load_image () usage example.
import pygame, pygame.locals
from ocempgui.draw import *
from ocempgui.widgets.Constants import *
from ocempgui.widgets import *
import time

class Main():
    def __init__(self):
        pygame.init ()
        self.screen = pygame.display.set_mode ((500, 500))
        self.screen.fill ((250, 250, 250))
        pygame.display.set_caption ('TilesetBuilder')

        self.re = Renderer ()
        self.re.screen = self.screen
        self.re.title = "Tileset Builder"
        self.re.color = (234, 228, 223)

        self.selection = pygame.rect(0,0,32,32)
        self.tiles = []
        self.filename = ""
        self.loadImage = None
        button = Button ("#Load Image")
        button.connect_signal (SIG_CLICKED, self.load_image)
        self.re.add_widget (button)
        
        add = Button("Add to Tileset")
        add.connect_signal(SIG_CLICKED,self.add_to_tileset)
        self.re.add_widget (add)

        self.re.start()
        
    def run(self):
        self.display()
        time.sleep(.100)
    def display(self):
        self.screen.blit (self.loadImage, (10, 30))
        for i in self.tiles:
            image = Image.load_image(i[0])
        pygame.display.flip()
    def _set_files (self,result, dialog):
        string = ""
        if result == DLGRESULT_OK:
            string = dialog.get_filenames ()[0]
            imageName = string
            self.loadImage = Image.load_image (imageName)
            self.filename = imageName
        else:
            string = "Nothing selected"
        dialog.destroy ()
        self.display()
    def add_to_tileset(self):
        if self.loadImage == None:
            return
        self.tiles += [[self.filename,self.selection]]
        self.display()
    def load_image(self):
        buttons = [Button ("#OK"), Button ("#Cancel")]
        buttons[0].minsize = 80, buttons[0].minsize[1]
        buttons[1].minsize = 80, buttons[1].minsize[1]
        results = [DLGRESULT_OK, DLGRESULT_CANCEL]

        dialog = FileDialog ("Select your file(s)", buttons, results)
        dialog.depth = 1 # Make it the top window.
        dialog.topleft = 100, 20
        dialog.filelist.selectionmode = SELECTION_MULTIPLE
        dialog.connect_signal (SIG_DIALOGRESPONSE, self._set_files, dialog)
        self.re.add_widget (dialog)
    
main = Main()
