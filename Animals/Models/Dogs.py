from Models.Anim import Animal

class Dog(Animal):
  #¨¨¨
  #Dog class, inherited from animal class
  #¨¨¨
  def __init__(self, name, color, friendly, hasOwner, age):
    #¨¨¨
    #Initializes the dog
    #¨¨¨
    self.name=name
    self.color = color
    self.friendly = friendly
    self.hasOwner = hasOwner
    self.age = age
    self.tipo = 'Dog'

  def __repr__(self):
    #¨¨¨
    #method used to print extra info of each Dog object
    #¨¨¨
    return super().__repr__()

