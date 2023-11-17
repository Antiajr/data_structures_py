# data structure and algorithm in python
# data structure are building blocks and raw materials for any software program
# use the right data structure for the right program.

store_prices = {
    'march 4': 230,
    'march 5': 240,
    'march 6': 250
}
print(store_prices['march 5'] + store_prices['march 5'])

# store_prices2 = [296,305,320,292]
# store_prices2[0]
# Array or list for data structure
# data structure: Array, dictionary, Linked List
# BIG O notation : its measeaue the running time of your program.
def get_squared_numbers(number):
    square_numbers = []
    for n in numbers:
        square_numbers.append(n)
    return square_numbers
numbers = [2,3,4,5]
print(get_squared_numbers(numbers))

# the time excutetion will remain constant.

number3 = [3,6,2,4,3,6,8,9]
for i in range(len(number3)):
    for j in range(i + 1, len(number3)):
        if number3[i] == number3[j]:
            # print(number3[i] + 'is a duplicate')
            break
        
numbers4 = [1,2,3,4,5]
duplicate = None
for i in range(len(numbers4)):
    for j in range(i + 1, len(numbers4)):
        if numbers4[i] == numbers4[j]:
            duplicate == numbers4[i]
            break
for i in range(len(numbers4)):
    if numbers4[i] == duplicate:
        print(i)
        
# BIG 0: refers to very large value of n. hence if you have a function like,
# measuring running time growth.

find_numbers = [1,2,3,4,5]
for i in range(len(find_numbers)):
    # if i == 4:
    #     print(i)
    if i % 2 == 0:
        print(f'{i} is an even number')
    else:
        print(f'{i} is an odd number')

# data structure and algorithm are reaaly important in programming.
# Array data structure
# BIG 0 notation measures how many time your program is meant to run

store_prices1 = [23,24,25,26]
prices = store_prices1[1] + store_prices1[2] % 2
print(prices)

# 2 dimentional Array
main_array = [
    [1,2,3,4],
    [5,6,7,8]
]
main_array.append([9,10,11,12])
print(main_array)
for i in range(len(main_array)):
    sum = 0
    row = main_array[i]
    for j in range(len(row)):
        sum += row[j]
print(f'row of {row} = {sum}')

stock_prices = {
    'feb': 200,
    'march': 300,
    'april': 400,
    'may': 500
}
stock_prices['june'] = stock_prices['feb'] + stock_prices['march']
print(stock_prices)

stock_data = [
    {'feb': 200},
    {'march': 300},
    {'april': 400},
    {'june': 500}
]
stock_data.append({'july':600})
print(stock_data)
# append into an empty list
# lst1 = []
# for i in range(5):
#     lst1.append(i)
# print(input('enter value: '))
# print(lst1)

stock_list = []
stock_list.append(298)
stock_list.append(305)
stock_list.append(320)
stock_list.insert(1,284)
stock_list.insert(4, 400)
print(stock_list)

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
class LimkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_begininng(self, data):
        node = Node(data, self.head)
        self.head = node
    
    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ''
        
        while itr:
            llstr += str(itr.data) + '---->'
            itr = itr.next
            
        print(llstr)
    def insert_at_end(self, data):
        if self.head is None:
            self.head = None(data, None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)
        
    def insert_value(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
    
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count +=1
            itr = itr.next
        return count
    
    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception('invalid index')
        
        if index == 0:
            self.head = self.head.next
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            
            itr = itr.next
            count += 1
    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception('invalid index')
        
        if index == 0:
            self.insert_at_begininng(data)
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1
            
if __name__ == '__main__':
    ll = LimkedList()
    ll.insert_at_begininng(5)
    ll.insert_at_begininng(89)
    ll.insert_at_end(79)
    ll.remove_at(2)
    # ll.insert_value(['bannana', 'mango','grapes', 'orange'])
    ll.print()
    print('length: ', ll.get_length())