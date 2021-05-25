detailes_list=["Eleazar halal", 22, "elazarh@gmail.com", 123456789]
print("Full_Name:",detailes_list[0], "\nAge:",detailes_list[1],"\nMail:",detailes_list[2],"\nPhone:",detailes_list[3])
IP_list=["1.1.1.1","2.2.2.2"]
print(IP_list)
IP_list.append("3.3.3.3")
IP_list.append("4.4.4.4")
IP_list.append("5.5.5.5")
print(IP_list)
print("Number of Ips:",len(IP_list))
IP_list.pop(3)
print(IP_list)
print("Number of Ips:",len(IP_list))