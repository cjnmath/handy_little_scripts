# if the distribution of v_i is given,
# for example :
# v_i=1 (when i=1,3,4,7)
# v_i=2 (when i=8)
# v_i=3 (when i=2,5)
# v_i=4 (when i=6,9,10)
# The generator I came up with is pretty straightforward, by inflating
# the choice list, such that there are s_k+x_k nodes with value k in this choice
# list, s_k is the original amount of nodes with v_i=k,
# the x_k could be choosen by our will to meet the prerequires.
# The following python code was based on the aforementioned example:
#
#

from random import choice

# first build a dictionary with v_i as key,
# and its value is a list of index node
count_dict = {  1: [1, 3, 4, 7],
                2: [8],
                3: [2, 5],
                4: [6, 9, 10]}

def floor(a,b):
    """ given a,b return min c
        such that a+c>b
    """
    c = 0
    while a + c <= b:
        c += 1
    return c

def generator(dict):
    choice_list = []
    # initialize the x_i
    x_i_list = [0 for i in range(len(dict))]

    # choose x_i, the last one remain 0
    for i in reversed(range(len(x_i_list)-1)):
        # this code looked weird, but keep in mind that the list start in 0
        # while count_dict start in 1
        x_i_list[i] = floor(len(dict[i+1]), x_i_list[i+1]+len(dict[i+2]))

    # inflate the choice_list
    # such that there are s_k+x_k nodes with values k in choice_list
    for i in range(len(dict)):
        for _ in range(len(dict[i+1])+x_i_list[i]):
            choice_list.append(i+1)

    # choose a random value
    random_value = choice(choice_list)
    # return the actual node (randomly)
    return choice(dict[random_value])

if __name__ == '__main__':
    # result = generator(count_dict)
    # print(result)
    nodes_index = [i+1 for i in range(10)]
    nodes_count = [0 for i in range(10)]
    dictionary = dict(zip(nodes_index, nodes_count))
    for _ in range(100000):
        index = generator(count_dict)
        dictionary[index]+=1
    print(dictionary)

    result = {
        1: 0,
        2: 0,
        3: 0,
        4: 0,
    }
    for i in range(4):
        i_index=i+1
        for k in range(len(dictionary)):
            k_index = k+1
            if k_index in count_dict[i_index]:
                result[i_index] += dictionary[k_index]
    # print(dictionary)
    print(result)

# the code is not the most efficient
# but you get the idea
