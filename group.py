"""
This function inputs a list of integers and returns a list of lists of inputs. The function takes
the input list, divides it into lists of three elements, adds any leftover elements that weren't
divided evenly, and returns a new list full of these smaller lists.
"""

def groups_of_3(input:list[int]) -> list[list[int]]:
    output = []
    for i in range(len(input)//3):
        output.append([input[3*i], input[3*i+1], input[3*i+2]])
    if len(input)%3 == 2:
        output.append([input[-2], input[-1]])
    if len(input)%3 == 1:
        output.append([input[-1]])
    return output


