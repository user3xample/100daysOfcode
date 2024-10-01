#! /usr/bin/env python3

# ##FileNotFound
# with open ("afile.txt") as file:  # we dont have this file in our folder
#     file.read()

# ##KeyError
# a_dict = {"key": "value"}
# value = a_dict["non_excistent_key"]

# ##IndexError
# fruit_list = ["Apple", "Bannana", "Pears"]
# fruit = fruit_list[5]  # we have 0,1,2

# ##TypeError
# text = "abc"
# print(text + 5)

#try:  # Something that might cause an exception.
#except:  # Do this if there WAS an exception.
#else:  # Do this if there were no exceptions.
#finally:  # Do this no matter what happens

########
# File not found example
try:
    file = open ("afile.txt")  # error if file not in our folder
    a_dict = {"key": "value - our dict text"}
    #print(a_dict["not in it"])  # error
    print(a_dict ["key"])

except FileNotFoundError:  # always be specific otherwise a bare except will catch everything .
    print("File not found, creating file")
    file=open("afile.txt", "w")
    file.write("Text in file")
except KeyError as error_message:
    print(f"The key {error_message} does not exist.")
else:  # triggered if no errors
    content = file.read()
    print(content)
finally:
    file.close()  # Good practice to get into.
    print("Our file was closed")
    raise KeyError ("An error message")  # This forces the error message.from