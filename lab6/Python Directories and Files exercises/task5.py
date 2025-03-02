

def write_list_to_file(filename, my_list):
    with open(filename, 'w') as file:
        for item in my_list:
            file.write(str(item) + "\n")


write_list_to_file("output.txt", ["Apple", "Banana", "Cherry"])
