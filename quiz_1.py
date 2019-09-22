# Written by *** and Eric Martin for COMP9021


import sys
from random import seed, randrange


try:
    arg_for_seed, upper_bound = (abs(int(x)) + 1 for x in input('Enter two integers: ').split())
    #print(arg_for_seed)
    #print(upper_bound)
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(arg_for_seed)
mapping = {}
for i in range(1, upper_bound):
    r = randrange(-upper_bound // 2, upper_bound)
    if r > 0:
        mapping[i] = r
print('\nThe generated mapping is:')
print('  ', mapping)

mapping_as_a_list = []
one_to_one_part_of_mapping = {}
nonkeys = []

# INSERT YOUR CODE HERE
num_mapping=len(mapping)
#Calculate the number of keys that generate the dictionary
k =upper_bound
L =[]
for m in mapping.keys():
    #print(m)
    L.append(m)
    #print(L)
#Traversing the dict key value, sort this in a list

for n in range(1,k):
    if n not in L:
        nonkeys.append(n)
#If n is not in the key value list, output to nonkeys

for s in range(0,k):
    if s in mapping:
        mapping_as_a_list.append(mapping[s])
    else:
        mapping_as_a_list.append(None)
#Traverse if the variable is in the dictionary, the mapping_as_a_list is the key in the dictionary, if not, the output is None
p=mapping.keys()
q=mapping.values()
#Returns all traversable keys and values in the mapping
#print(z)
##count= {}
##for item in z:
##    judge_value=count.get(item[1], -1)
##    count[item[1]] = judge_value + 1
###用dict.get()判断是否存在，不存在赋值为-1,本题中生成的元组一共两位,item[1]表示value
##    if count[item[1]] == 0:
##        one_to_one_part_of_mapping[item[0]] = item[1]
###如果最后结果为0，证明没有重复，即可添加到新的dict
for i in p:
    if list(q).count(mapping[i]) == 1:
        one_to_one_part_of_mapping[i] = mapping[i]

print()
print(f'The mappings\'s so-called "keys" make up a set whose number of elements is {num_mapping}.')
print('\nThe list of integers between 1 and', upper_bound - 1, 'that are not keys of the mapping is:')
print('  ', nonkeys)
print('\nRepresented as a list, the mapping is:')
print('  ', mapping_as_a_list)
# Recreating the dictionary, inserting keys from smallest to largest,
# to make sure the dictionary is printed out with keys from smallest to largest.

one_to_one_part_of_mapping = {key: one_to_one_part_of_mapping[key]
                                      for key in sorted(one_to_one_part_of_mapping)
                             }



#遍历items，选出只出现一次的item，去掉重复的那几项key和value,按照key的从小到大排序
print('\nThe one-to-one part of the mapping is:')
print('  ', one_to_one_part_of_mapping)


