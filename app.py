import os 


def create_file(filename):
    try: 
        with open ('filename','x') as f:
            print (f"File name {filename} :create sucessfully")
    except FileExistsError:
        print(F'filename {filename} alreaedy exist')

    except Exception as E :
        print('An Error Occured')


def View_file ():
    files = os.listdir()
    if not files :
        Print("No File Found in current directory")

    else :
        print('file is directory')
        for files in files :
            print(files)


def Delet_file (filename):
    try :
        os.remove(filename)
        print (f'this file {filename}: sucessfully removed from directory')

    except FileNotFoundError:
        print("file not found in directory")
    except Exception as E:
        print("unknow Error")

def read_file (filename):
    try:
        with open('sample.txt','r')as f:
            content = f.read()
            print(f"content of '{filename}': \n{content}")
    
    except FileNotFoundError :
        print(f"this file '{filename}': Does not exist")

    except Exception as E :
        print('An Error Occured')


def Edit_file (filename):
    try:
        with open('sample.txt','a') as f:
            content = input ('Enter the data you wants to add')
            f.write (content+"\n")
            print ("Updated sucessfully to {filename}")
    
    except FileNotFoundError:
        print(f"this file '{filename}':Does not exist")
    except Exception as E :
        print('An Error Occured')


def main ():
    while True :
        print('File Management app')
        print('1:Create file')
        print('2:view all file')
        print('3:Delete file')
        print('4:read file')
        print('5:Edit file')
        print('6: Exit')

        choice = input ('Enter your choice(1-6) = ')

        if choice == '1':
            filename = input("Enter the file name you wants to create = ") 
            create_file = (filename)
        elif choice == '2':
            View_all_files()
        elif choice == '3':
            filename = input ("Enter the file name you wants to Delete ")
            Delet_file = (filename)
        elif choice == '4':
            filename = input("Enter the file name you wants to Read")
            read_file = (filename)
        elif choice == '5':
            filename = input("Enter the file name you wants to Edit")
            Edit_file = (filename)
        elif choice == '6':
            print(" App is closing")
            break
        else :
            print("Invalid input please choose given option")

if __name__ == "__main__" :
    main()





