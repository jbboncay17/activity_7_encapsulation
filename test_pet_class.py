bold="\033[1m"
red="\033[31m"
end="\033[0m"
green="\033[32m"
blue="\033[34m"
yellow="\033[33m"
purple="\033[35m"


from pet_class import Pet
print("")
print(bold+purple+"************ PET CLASS TEST ************"+end)
pet = Pet()

name = input(bold+blue+"Enter pet name: "+end)
animal_type = input(bold+blue+"Enter animal type: "+end)
sex=input(bold+blue+"Male/Female: "+end)
animal_breed = input (bold+blue+"Enter animal breed: "+end)
age = int(input(bold+blue+"Enter pet age: "+end))
print(bold+purple+"****************************************"+end)
print("")
pet.set_name(name)
pet.set_animal_type(animal_type)
pet.set_animal_breed(animal_breed)
pet.set_sex(sex)
pet.set_age(age)


print(bold+yellow+"************ PET INFORMATION ************"+end)
print(bold+green+"Name:"+end, pet.get_name())
print(bold+green+"Type:"+end, pet.get_animal_type())
print(bold+green+"Sex:"+end, pet.get_sex())
print(bold+green+"Breed:"+end, pet.get_animal_breed())
print(bold+green+"Age:"+end, pet.get_age())
print(bold+yellow+"*****************************************"+end)