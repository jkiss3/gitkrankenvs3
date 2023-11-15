class Dog:
    def __init__ (self, Breed, Name, Age, ugatas):
        self.Breed = Breed
        self.Name = Name
        self.Age = Age
        self.ugatas = ugatas
    def ugat(self):
            print(f"A kutya neve {self.Name}, fajtaja {self.Breed}, {self.Age} eves, es ilyen hangot ad ki: {self.ugatas}")

dog1 = Dog('kuvasz','Dino',29,"waff-waff")
dog1.ugat()