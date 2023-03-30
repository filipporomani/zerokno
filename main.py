import zerokno.zerokno as zerokno

z = zerokno.Zerokno()

pwd1 = input("Enter password: ")

z.store(pwd1, "test")

pwd2 = input("Enter password: ")

print(z.validate(pwd2, "test"))