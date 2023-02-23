class Animal:
  def __init__(self):
    self.num_eyes = 2

  def breathe(self):
    print("Inhale, exhale.")

class Fish(Animal): # Inheriting from the Animal Class.
  def __init__(self):
    super().__init__()  # super() calls the __init__ method of the parent class.

  def breathe(self):
    super().breathe() # super() calls the breathe method in the parent class.
    print("doing this underwater.")

  def swim(self):
    print("Moving in water.")


nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)
