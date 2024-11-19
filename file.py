import sys

'''This function checks the input parameter for the name of a file and performs operations on the
contents of that file. The function takes each line of the file, assuming that each line has two
floats divided by a space, creates a list containing line, and returns a list corresponding to 
each line that contains the sum of the two floats contained in each line. 
'''
def file_reader():
    output = []
    try:
        with open(sys.argv[1], "r") as file:
            lines = file.read().splitlines()
            for i in range(len(lines)):
                try:
                    data = lines[i].split()
                    output.append([float(data[0]) + float(data[1])])
                except ValueError as e:
                    output.append(e)
                except IndexError as e:
                    output.append(e)
    except FileNotFoundError as a:
        print(a)
        exit()
    return output





if __name__ == "__main__":
    print(sys.argv)
    print(file_reader())
