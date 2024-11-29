import zerokno.zerokno as zerokno # local import

z = zerokno.ZeroKno(storage="./")

pwd1 = input("Enter password: ")

z.store(pwd1, "test")

pwd2 = input("Enter password: ")

print(z.validate(pwd2, "test"))
# if this prints True, then the code is working as expected