import random, string
size = int(input('Type the number of characters of the password that you wish: '))
chars = string.ascii_letters +string.ascii_lowercase +string.ascii_uppercase + string.digits + 'ç!@#$%&*()-=+,.;:/?'
rnd=random.Systemandom()
print(''.join(rnd.choice(chars) for i in range(size)))