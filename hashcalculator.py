import hashlib
import argparse

#Initializing Argparse & adding positional argument
parser = argparse.ArgumentParser(prog="Hash Calculator", description="A command line hash calculator for texts and files")
parser.add_argument("mode", metavar="Mode", choices=['text', 'file'],help="Specifies the mode to launch hash calculator in [options: file or text]")
args = parser.parse_args()


#Defining and initializing Hash Algorithms 
md5 = hashlib.md5()
sha1 = hashlib.sha1()
sha256 = hashlib.sha256()
sha512 = hashlib.sha512()
sha384 = hashlib.sha384()

#Defining text mode function
def text_mode():
    user_input = input("\nEnter text to calculate hash: ")
    proc_file = user_input.encode()

    #Taking preferred hash type
    print("\n[*] Available Hashing Algorithm:\n\n1. MD5\n2. SHA1\n3. SHA256\n4. SHA512\n5. SHA384")
    user_choice = input("\nMake a selection: ")

    #Performing hash operations
    if user_choice == "1" or user_choice == md5.name:
        md5.update(proc_file)
        print(f"\n[*] {md5.name} hash: {md5.hexdigest()}")
    elif user_choice == "2" or user_choice == sha1.name:
        sha1.update(proc_file)
        print(f"\n[*] {sha1.name} hash: {sha1.hexdigest()}")
    elif user_choice == "3" or user_choice == sha256.name:
        sha256.update(proc_file)
        print(f"\n[*] {sha256.name} hash: {sha256.hexdigest()}")
    elif user_choice == "4" or user_choice == sha512.name:
        sha512.update(proc_file)
        print(f"\n[*] {sha512.name} hash: {sha512.hexdigest()}")
    elif user_choice == "5" or user_choice == sha384.name:
        sha384.update(proc_file)
        print(f"\n[*] {sha384.name} hash: {sha384.hexdigest()}")
    else:
        print("\n[**] Error: hash specified is not available")


#Defining file mode function
def file_mode():
    file_input = input("\nEnter file name or full path of desired file to calculate its hash [Include apropriate extensions]: ")
    with open(file_input, mode='rb') as file:
        proc_file = file.read()
    
    #Taking preferred hash type
    print("\n[*] Available Hashing Algorithm:\n\n1. MD5\n2. SHA1\n3. SHA256\n4. SHA512\n5. SHA384")
    user_choice = input("\nMake a selection: ")

    #Performing hash operations
    if user_choice == "1" or user_choice == md5.name:
        md5.update(proc_file)
        print(f"\n[*] {md5.name} hash: {md5.hexdigest()}")
    elif user_choice == "2" or user_choice == sha1.name:
        sha1.update(proc_file)
        print(f"\n[*] {sha1.name} hash: {sha1.hexdigest()}")
    elif user_choice == "3" or user_choice == sha256.name:
        sha256.update(proc_file)
        print(f"\n[*] {sha256.name} hash: {sha256.hexdigest()}")
    elif user_choice == "4" or user_choice == sha512.name:
        sha512.update(proc_file)
        print(f"\n[*] {sha512.name} hash: {sha512.hexdigest()}")
    elif user_choice == "5" or user_choice == sha384.name:
        sha384.update(proc_file)
        print(f"\n[*] {sha384.name} hash: {sha384.hexdigest()}")
    else:
        print("\n[**] Error: hash specified is not available")


#Making argparse options active
if args.mode == 'text':
    text_mode()  
elif args.mode == 'file':
    file_mode()
