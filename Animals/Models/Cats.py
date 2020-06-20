from Models.Anim import Animal

class Cat(Animal):
  #¨¨¨
  #Cat class, inherited from animal class
  #¨¨¨
  def __init__(self, name, color,age):
    #¨¨¨
    #Initializes the cat
    #¨¨¨
    self.name = name
    self.color = color
    self.age = age
    self.tipo = 'Cat'
