from pet_class import Pet

pet = Pet()

name = input("Enter pet name: ")
animal_type = input("Enter animal type: ")
age = int(input("Enter pet age: "))

pet.set_name(name)
pet.set_animal_type(animal_type)
pet.set_age(age)

print("\nPet Information")
print("Name:", pet.get_name())
print("Type:", pet.get_animal_type())
print("Age:", pet.get_age())