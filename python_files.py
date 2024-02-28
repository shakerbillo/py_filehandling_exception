try:
    with open('newFile.txt', 'w') as file:
        file.writelines(["This is a new file created!", '\nThis is another one to be added.'])
        
except FileNotFoundError as e:
    print('Error', e)