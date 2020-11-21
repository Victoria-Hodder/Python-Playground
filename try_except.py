try:
    x = int(input("Enter number: "))
except ValueError:
    print("Must be a number.")
else:
    print(x)
finally:
    print("Goodbye!")



# try:
#     f = open('sample_text.txt')
# except FileNotFoundError:
#     print("We didn't find a file with that name. Check for typos?")
# except Exception as e:
#     print(e)
# else:
#     print(f.read())
# finally:
#     f.close()
