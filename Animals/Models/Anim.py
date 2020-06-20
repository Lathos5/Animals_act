class Animal(object):
  #¨¨¨
  #Animal class is the base class for other animals
  #¨¨¨
  def __init__(self):
    #¨¨¨
    #Initializes the animal
    #¨¨¨
    self.name = ''
    self.tipo = '' # Cat/Dog
    self.color = ''
    self.age = 0

  def __gt__(self, animal):
    #¨¨¨
    #method used to sort the animal list
    #¨¨¨
    return self.name > animal.name

  def __repr__(self):
    #¨¨¨
    #method used to print the animal list
    #¨¨¨
    return f"Name:{self.name} Color:{self.color} Age:{self.age} Type:{self.tipo}"
