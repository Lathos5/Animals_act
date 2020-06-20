import wx
import wx.xrc

import os
import os.path

from openpyxl import load_workbook

from Models.Anim import Animal
from Models.Cats import Cat
from Models.Dogs import Dog
from Models.FrameCat import ventanaCat
from Models.FrameDog import ventanaDog

class AnimalsFrame(wx.Frame):
    def __init__(self,parent,title):

        self.animals = ListAnimals()

        wx.Frame.__init__(self, None, title=title, size=(1080,720))
        self.archivo='untitled.txt'

        p=wx.Panel(self, -1)

        # Sizer
        sz=wx.BoxSizer(wx.VERTICAL)

        # Editor
        self.editor=wx.TextCtrl(p, -1, "", style=wx.TE_MULTILINE)

        # Agregar al sizer
        sz.Add(self.editor, 1, wx.EXPAND)
        p.SetSizer(sz)

        # Crear barra de menu
        self.crearMenu()
        self.Center(True)
        self.Show()


    def crearMenu(self):  
        """ Crea la barra de menú """
        marchivo=wx.Menu()
        aFiles=marchivo.Append(-1, "Abrir Archivo")
        

        magregar=wx.Menu()
        aDog=magregar.Append(-1, "Agregar Perro ")
        aCat=magregar.Append(-1, "Agregar Gato ")

        mImprimir = wx.Menu()
        mostrar = mImprimir.Append(-1, "Mostrar arreglo")

        barraMenu=wx.MenuBar()
        barraMenu.Append(marchivo, "Archivo")
        barraMenu.Append(magregar, "Agregar")
        barraMenu.Append(mImprimir, "Mostrar arreglo")

        self.SetMenuBar(barraMenu)

        # Definición de "eventos"
        self.Bind(wx.EVT_MENU, self.abrirArchivo, aFiles)
        

        self.Bind(wx.EVT_MENU, self.llamar_Dog, aDog)
        self.Bind(wx.EVT_MENU, self.llamar_Cat, aCat)

        self.Bind(wx.EVT_MENU, self.imprimir, mostrar)

    def form_gatos(self, cname, cage, ccolor):
        cat = Cat(name = cname,
                  color=ccolor,
                  age=cage)
        self.animals.lAnimals.append(cat)

    def form_perros(self, dname, dage, dcolor):
        dog = Dog(name = dname,
                  color=dcolor,
                  friendly = '', 
                  hasOwner = '',
                  age=dage)
        self.animals.lAnimals.append(dog)

    def abrirArchivo(self, event):
        #""" Abre un archivo de texto plano"""
        wc = "Text Files (*.txt)|*.txt|Excel Files (*.xslx)|*.xlsx"
        dlg=wx.FileDialog(self, "Abrir archivo de animales", wildcard=wc, style = wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_CANCEL:
            return
        pathname = dlg.GetPath()

        nombre, extension = os.path.splitext(pathname)

        if extension == ".txt":
            #method created for txt files
            self.txtFile(pathname, dlg)
            
        elif extension == ".xlsx":
            #method created for excel files
            self.xslxFile(pathname, dlg)
        
    def xslxFile(self, pathname, dialog):
        try:
            #¨¨¨
            #Dogs
            #¨¨¨
            workbook = load_workbook(filename = pathname)
            sheet = workbook.active

           
            for row in sheet.iter_rows(min_row = 2, values_only = True):
                #¨¨¨
                #for each row on the excel dogs file, we will create a dog object whom is going to be added to the animals list
                #¨¨¨
                dog = Dog(name=row[0],
                         color=row[1],
                         friendly=row[2],
                         hasOwner=row[3],
                         age=row[4])
                self.animals.lAnimals.append(dog)
            self.alerta("Perros")
        except IOError:
             wx.LogError(u"No puede abrir archivo '%s'." % newfile)
             dialog.Destroy()
    
    
    def txtFile(self, pathname, dialog):
        try:
            with open(pathname) as Gatos: 
                    #¨¨¨
                    #Cats
                    #¨¨¨
                
                for gato in Gatos.readlines():
  
                      #removing multiple spaces
  
                      while '  ' in gato:
                         gato = gato.replace('\n', '')
                         gato = gato.replace('  ',' ')
                         arrayInfo = gato.split(' ')

                      #¨¨¨
                      #excluding the header from the cats file to store on the animals list
                      #¨¨¨

                      if arrayInfo[0] != 'name':
                          cat = Cat(name = arrayInfo[0],
                                    color=arrayInfo[1],
                                    age=arrayInfo[2])
            
                          self.animals.lAnimals.append(cat)
            Gatos.close()
            self.alerta("Gatos")
        except IOError:
            wx.LogError(u"No puede abrir archivo '%s'." % newfile)
            dialog.Destroy()

    
    def alerta(self, animalito):
        wx.MessageBox(animalito +' han sido agregados', 'Info', wx.OK | wx.ICON_INFORMATION)
    
    def imprimir(self, event):
        #Imprime el contenido de la clase Animales
        self.editor.SetValue(self.animals.shownList())

    def llamar_Dog(self, event):
        vDog = ventanaDog(self)
        vDog.Show()
        
        
    def llamar_Cat(self, event):
        vCat = ventanaCat(self)
        vCat.Show()


class ListAnimals():
    lAnimals = []

    def shownList(self):
        self.lAnimals = sorted(self.lAnimals, key=lambda x: x.name)
        result = ''
        for animal in self.lAnimals:
            result += str (animal) + "\n"
        return result

if __name__=='__main__':
    app = wx.App()
    fr = AnimalsFrame(None, "Animals")
    app.MainLoop()