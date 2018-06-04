# if the distribution of v_i is given,
# for example :
# v_i=1 (when i=1,3,4,7)
# v_i=2 (when i=8)
# v_i=3 (when i=2,5)
# v_i=4 (when i=6,9,10)
# The following python code was based on the aforementioned example:


from random import choice

# first build a dictionary with v_i as key,
# and its value is a list of index node
count_dict = {  1: [1, 3, 4, 7],
                2: [8],
                3: [2, 5],
                4: [6, 9, 10]}

choice_list = [ 1, 1, 1, 1,
                2, 2, 2,
                3, 3,
                4]


value_num = choice(choice_list)
index_num = choice(count_dict[value_num])
print(index_num)

# this method was based on the last one,
# but with a more concise way to generate choice list
# (we predefine it!)
