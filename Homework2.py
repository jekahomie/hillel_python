# Name request
name = input("What`s your name ? :")
# Age request
age = int(input("How old are you ? :"))

#Request/Answer by Age
if age == 16:
    print(name, ", you need to wait one year more")


elif 17<=age<71:
    print("Welcome,", name, ", on our website!")


elif 71<=age<91:
    print("You are lucky,", name, ", and welcome!")


elif 91<=age<121:
    print(name, ", are you sure?")


elif age >= 121:
    print("You are not real,", name, ".")

else:
    print("I'm so sorry,", name, ", you are too young! wait a few years more",".")


