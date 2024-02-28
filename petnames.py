import random

with open("petnames.txt", "r") as file:
    data = file.read()
    content_list = data.split("\n")
    print(random.choice(content_list))