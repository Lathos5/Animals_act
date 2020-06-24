from Models.Anim import Animal

class Dog(Animal):
  """
  Dog class, inherited from animal class
  """
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


