import datetime

age = int(input("What is your age:"))
name = raw_input("What is your name:")
now = datetime.datetime.now()
diff = 100-age

str_fin = "Hello" + name + " you will be 100 years old at" + str(now.year+diff)

print(str_fin)