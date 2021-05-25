print("Calculating Your purchase:\nprices:\nTomato: 3 NIS\ncucumber: 2 NIS\nCoca-Cola: 5 NIS\nchicken: 20 NIS")
Tomato=int(input("enter how many tomatos you take:"))
Cucumber=int(input("enter how many Cucumber you take:"))
Cola=int(input("enter how many Cola you take:"))
chicken=int(input("enter how many Chicken you take:"))
summary=Tomato*3+Cucumber*2+Cola*5+chicken*20
print("your order is:\nTomatos:",Tomato )
print("Cucumbers:",Cucumber)
print("Colas:",Cola)
print("chickens:",chicken)
print("this is the check BEFORE MAAM:" , summary)
print("this is the MAAM:" , summary*17/100)
print("this is the check AFTER MAAM:" , "%.5f" % (summary*17/100+summary))

