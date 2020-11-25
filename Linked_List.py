class Linked_List:
  
  class __Node:
    
    def __init__(self, val):
      # declare and initialize the public attributes
      # for objects of the Node class.
      
      self.value = val
      self.next = None
      self.prev = None

  def __init__(self):
    # declare and initialize the private attributes
    # for objects of the sentineled Linked_List class
    
    self.__header = self.__Node(None)
    self.__trailer = self.__Node(None)
    self.__header.next = self.__trailer
    self.__trailer.prev = self.__header
    self.__size = 0
    
  def __len__(self):
    # return the number of value-containing nodes in 
    # this list.
    
    return self.__size

    # PERFORMANCE: O(1)

  def append_element(self, val):
    # increase the size of the list by one, and add a
    # node containing val at the new tail position. this 
    # is the only way to add items at the tail position.
    
    newest = self.__Node(val) #create new node
    cur = self.__trailer.prev #cur is the old tail
    
    # swap pointers
    newest.prev = cur 
    newest.next = self.__trailer
    cur.next = newest
    self.__trailer.prev = newest

    self.__size += 1 

    # PERFORMANCE: O(1)

  def insert_element_at(self, val, index):
    # assuming the head position (not the header node)
    # is indexed 0, add a node containing val at the 
    # specified index. If the index is not a valid 
    # position within the list, raise an IndexError 
    # exception. This method cannot be used to add an 
    # item at the tail position.
    
    # check index
    if index < 0 or index >= self.__size:
      raise IndexError
    
    newest = self.__Node(val) #create new node

    # start at trailer and work back if index is over
    # or equal to half the length.    
    if index >= self.__size // 2:
      cur = self.__trailer
      # loop until cur points to the index to be inserted at
      for i in range(self.__size-index): 
        cur = cur.prev
      # swap pointers to insert newest before cur
      newest.next = cur
      newest.prev = cur.prev
      cur.prev.next = newest
      cur.prev = newest

    # start at header and work forward if index less than
    # half the length.
    else:
      cur = self.__header
      # loop until cur points to the node before
      # the index to be inserted at
      for i in range(index):
        cur = cur.next
      # swap pointers to insert newest after cur
      newest.prev = cur
      newest.next = cur.next
      cur.next.prev = newest
      cur.next = newest
    
    self.__size += 1 #increment size

    # PERFORMANCE: O(n)

  def remove_element_at(self, index):
    # assuming the head position (not the header node)
    # is indexed 0, remove and return the value stored 
    # in the node at the specified index. If the index 
    # is invalid, raise an IndexError exception.
    
    # check index
    if index < 0 or index >= self.__size:
      raise IndexError

    # start at trailer and work back if index is over
    # or equal to half the length.  
    if index >= self.__size // 2:
      cur = self.__trailer
      # loop until cur points to the node
      # after target index
      for i in range(self.__size-(index+1)): 
        cur = cur.prev
      # store value, then remove all pointers from cur.prev
      value = cur.prev.value 
      cur.prev = cur.prev.prev
      cur.prev.next = cur

    # start at header and work forward if index less than
    # half the length.   
    else:
      cur = self.__header
      # loop until cur points to the node
      # before target index
      for i in range(index):
        cur = cur.next
      # store value, then remove all pointers from cur.next
      value = cur.next.value
      cur.next = cur.next.next 
      cur.next.prev = cur
    
    self.__size -= 1 #decrement size
    return value

    # PERFORMANCE O(n) 


  def get_element_at(self, index):
    # assuming the head position (not the header node)
    # is indexed 0, return the value stored in the node 
    # at the specified index, but do not unlink it from 
    # the list. If the specified index is invalid, raise 
    # an IndexError exception.
    
    #index check
    if index < 0 or index >= self.__size:
      raise IndexError

    # start at trailer and work back if index is over
    # or equal to half the length.
    if index >= self.__size // 2:
      cur = self.__trailer
      # loop until cur points to the target node
      for i in range(self.__size-index): 
        cur = cur.prev
      return cur.value

    # start at header and work forward if index less than
    # half the length. 
    else:
      cur = self.__header
      # loop until cur points to the target node
      for i in range(index+1):
        cur = cur.next
      return cur.value
    
    # PERFORMANCE O(n)


  def rotate_left(self):
    # rotate the list left one position. Conceptual indices
    # should all decrease by one, except for the head, which
    # should become the tail. For example, if the list is
    # [ 5, 7, 9, -4 ], this method should alter it to
    # [ 7, 9, -4, 5 ]. This method should modify the list in
    # place and must not return a value.
    
    # return nothing if list is empty
    if self.__size == 0:
      return
    
    # remove the first element of the list
    # and put it at the end
    head = self.remove_element_at(0)
    self.append_element(head)

    # PERFORMANCE: O(1)
    
  def __str__(self):
    # return a string representation of the list's
    # contents. An empty list should appear as [ ].
    # A list with one element should appear as [ 5 ].
    # A list with two elements should appear as [ 5, 7 ].
    # You may assume that the values stored inside of the
    # node objects implement the __str__() method, so you
    # call str(val_object) on them to get their string
    # representations.
    
    # unique case if list is empty
    if self.__size == 0:
      return '[ ]'

    # create and fill a list with the node values
    lst = [None] * self.__size
    cur = self.__header
    for i in range(self.__size):
        lst[i] = str(cur.next.value)
        cur = cur.next

    # join list into a string delimited by ', '
    liststr = ', '.join(lst)

    # concatenate brackets 
    string = '[ ' + liststr + ' ]'
    return string

    # Performance O(n)

  def __iter__(self):
    # initialize a new attribute for walking through your list

    self.__current = self.__header
    self.__iteration_index = 0
    return self

    # PERFORMANCE: O(1)

  def __next__(self):
    # using the attribute that you initialized in __iter__(),
    # fetch the next value and return it. If there are no more 
    # values to fetch, raise a StopIteration exception.
    
    # determine if end of list is reached
    if self.__iteration_index == self.__size:
      raise StopIteration

    to_return = self.__current.next.value #store element after current, eliminate header
    self.__current = self.__current.next #increment current
    self.__iteration_index += 1 #increment index
    return to_return

    # PERFORMANCE: O(1)

if __name__ == '__main__':
  # Your test code should go here. Be sure to look at cases
  # when the list is empty, when it has one element, and when 
  # it has several elements. Do the indexed methods raise exceptions
  # when given invalid indices? Do they position items
  # correctly when given valid indices? Does the string
  # representation of your list conform to the specified format?
  # Does removing an element function correctly regardless of that
  # element's location? Does a for loop iterate through your list
  # from head to tail? Your writeup should explain why you chose the
  # test cases. Leave all test cases in your code when submitting.
 
  print()

  # intialize new empty Linked List for empty list testing
  empty_ll = Linked_List()


  # initialize new empty Linked List for single element tests
  one_element_ll = Linked_List()

  # TEST append_element METHOD WITH AN EMPTY LINKED LIST
  print('TESTING APPEND_ELEMENT METHOD')
  one_element_ll.append_element(5)
  print('Append an element (the integer 5) to an empty list: ' + str(one_element_ll))
  print('List Size:', len(one_element_ll))
  
  print()

  # initialize empty Linked List for general testing
  ll = Linked_List()
  print('Current List: ' + str(ll))
  print('List size:', len(ll))

  # add different types of elements to list 
  # int, string, boolean, and float
  ll.append_element(10)
  ll.append_element('String')
  ll.append_element(True)
  ll.append_element(5.5)
  print('Append different types (int, String, boolean, float): ' + str(ll))
  print('List Size:', len(ll))

  print()
  print()

  # TEST insert_element_at METHOD
  print('TESTING INSERT_ELEMENT METHOD')
  # Multi-element list
  print('Current List: ' + str(ll))
  try:
    # all should work

    # index >= len(ll) // 2
    ll.insert_element_at(7, 2)
    print('Insert the number 7 at index 2: ' + str(ll))
    print('List Size:', len(ll))

    # index < len(11) // 2
    ll.insert_element_at('test', 1)
    print('Insert the string \'test\' at index 1: ' + str(ll))
    print('List Size:', len(ll))

    # test extremes
    ll.insert_element_at(0, 0)
    print('Insert the number 0 at index 0: ' + str(ll))
    print('List Size:', len(ll))
    ll.insert_element_at(100, len(ll)-1)
    print('Insert the number 100 at the 2nd to last position: ' + str(ll))
    print('List Size:', len(ll))

  except IndexError:
    print('Error: Index is out of bounds')
    # ensure list is unchanged
    print('List: ' + str(ll))
    print('List Size:', len(ll))
  except:
    print('Something went wrong. Not IndexError.')

  print()

  try:
    # should NOT work
    
    # Negative index
    print('Insert the number 2 at index -1:')
    ll.insert_element_at(2, -1)  
    print('***THIS SHOULD NOT HAVE WORKED***')

  except IndexError:
    print('Error: Index is out of bounds')
    # ensure list is unchanged
    print('List: ' + str(ll))
    print('List Size:', len(ll))
  except:
    print('Something went wrong. Not IndexError.')

  try:
    # should NOT work
    
    # index == length of list
    print('Insert the number 11 at the end of the list:')
    ll.insert_element_at(11, len(ll))
    print('***THIS SHOULD NOT HAVE WORKED***')

  except IndexError:
    print('Error: Index is out of bounds')
    # ensure list is unchanged
    print('List: '+ str(ll))
    print('List Size:', len(ll))
  except:
    print('Something went wrong. Not IndexError.')

  print()

  # Empty list test
  print('Insert to an empty list. List: ' + str(empty_ll))
  try:
    # should NOT work

    empty_ll.insert_element_at(1, 0)
    print('***THIS SHOULD NOT HAVE WORKED***')

  except IndexError:
    print('Error: Index is out of bounds')
    # ensure list is unchanged
    print('List: '+ str(empty_ll))
    print('List Size:', len(empty_ll))
  except:
    print('Something went wrong. Not IndexError.')
  
  print()

  # One element list tests
  print('Insert to a list with one element. List: ' + str(one_element_ll))
  try:
    # should NOT work

    # insert after the element (append)
    print('Insert the integer 2 at index 1:')
    one_element_ll.insert_element_at(2, 1)
    print('***THIS SHOULD NOT HAVE WORKED***')

  except IndexError:
    print('Error: Index is out of bounds')
    # ensure list is unchanged
    print('List: '+ str(one_element_ll))
    print('List Size:', len(one_element_ll))
  except:
    print('Something went wrong. Not IndexError.')
  
  try:
    # should work

    # insert before the element
    one_element_ll.insert_element_at(1, 0)
    print('Insert the integer 1 at index 0: ' + str(one_element_ll))
    print('List Size:', len(one_element_ll))
  
  except IndexError:
    print('Error: Index is out of bounds')
    # ensure list is unchanged
    print('List: '+ str(one_element_ll))
    print('List Size:', len(one_element_ll))
  except:
    print('Something went wrong. Not IndexError.')

  print()
  print()    

  # TEST remove_element_at METHOD
  print('TESTING REMOVE_ELEMENT METHOD')
  # Multi-element list
  print('Current List: ' + str(ll))
  try:
    # all should work

    # test index >= len(ll) // 2
    print('Remove element at index 6: ')
    to_return = ll.remove_element_at(6)
    print(str(ll) + ' List Size:', len(ll))
    print('RETURNS: ' + str(to_return))

    # test index < len(ll) // 2
    print('Remove element at index 1:')
    to_return = ll.remove_element_at(1)
    print(str(ll) + ' List Size:', len(ll))
    print('RETURNS: ' + str(to_return))

    # test extremes
    print('Remove element at index 0: ')
    to_return = ll.remove_element_at(0)
    print(str(ll) + ' List Size:', len(ll))
    print('RETURNS: ' + str(to_return))

    print('Remove element at last index: ')
    to_return = ll.remove_element_at(len(ll)-1)
    print(str(ll) + ' List Size:', len(ll))
    print('RETURNS: ' + str(to_return))
  
  except IndexError:
    print('Error: Index out of bounds')
    # ensure list is unchanged
    print('List: ' + str(ll))
    print('List Size:', len(ll))
  except:
    print('Something went wrong. Not IndexError.')

  print()

  try:
      # should NOT work

      # negative index
      print('Remove value at index -1: ')
      print(ll.remove_element_at(-1))
      print('***THIS SHOULD NOT HAVE WORKED***')
    
  except IndexError:
    print('Error: Index out of bounds')
    # ensure list is unchanged
    print('List: ' + str(ll))
    print('List Size:', len(ll))
  except:
    print('Something went wrong. Not IndexError.')    

  try:
    # should NOT work

    # index > length of list
    print('Remove value at index len(ll): ')
    print(ll.remove_element_at(len(ll)))
    print('***THIS SHOULD NOT HAVE WORKED***')
    
  except IndexError:
    print('Error: Index out of bounds')
    # ensure list is unchanged
    print('List: ' + str(ll))
    print('List Size:', len(ll))
  except:
    print('Something went wrong. Not IndexError.')
  
  print()

  # remove element from an empty list
  print('Remove an element from an empty list. List: ' + str(empty_ll))
  try:
    # should NOT work

    empty_ll.remove_element_at(0)
    print('***THIS SHOULD NOT HAVE WORKED***')

  except IndexError:
    print('Error: Index out of bounds')
    # ensure list is unchanged
    print('List: ' + str(empty_ll))
    print('List Size:', len(empty_ll))
  except:
    print('Something went wrong. Not IndexError.') 

  print()

  # remove element from a 1 element list
  one_element_ll.remove_element_at(0) #reduce the list back to 1 element after earlier insertion
  print('Remove the only element from this list. List: ' + str(one_element_ll))
  try:
    # this should work

    to_return = one_element_ll.remove_element_at(0)
    print('List: ' + str(one_element_ll))
    print('List Size:', len(one_element_ll))
    print('RETURNS: ' + str(to_return))

  except IndexError:
    print('Error: Index out of bounds')
    # ensure list is unchanged
    print('List: ' + str(one_element_ll))
    print('List Size:', len(one_element_ll))
  except:
    print('Something went wrong. Not IndexError.') 

  print()
  print()

  # TEST get_element_at METHOD
  print('TESTING GET_ELEMENT METHOD')
  # Muli-element list
  print('Current list: ' + str(ll))
  try:
    # all should work

    # index >= len(ll) // 2
    print('Element at index 2: ' + str(ll.get_element_at(2)))
    print('List is unchanged: ' + str(ll))
    print('List Size:', len(ll))

    # index < len(ll) // 2
    print('Element at index 1: ' + str(ll.get_element_at(1)))
    print('List is unchanged: ' + str(ll))
    print('List Size:', len(ll))

    # test extremes
    print('Element at index 0: ' + str(ll.get_element_at(0)))
    print('List is unchanged: ' + str(ll))
    print('List Size:', len(ll))

    print('Element in the last position: ' + str(ll.get_element_at(len(ll)-1)))
    print('List is unchanged: ' + str(ll))
    print('List Size:', len(ll))
  
  except IndexError:
    print('Error: Index out of bounds')
    # ensure list is unchanged
    print('List: ' + str(ll))
    print('List Size:', len(ll))
  except:
    print('Something went wrong. Not IndexError.')
  
  print()

  print('Current list: ' + str(ll))  
  try:
    # should NOT work

    # negative index
    print('Value at index -1: ')
    print(ll.get_element_at(-1))
    print('***THIS SHOULD NOT HAVE WORKED***')
  
  except IndexError:
    print('Error: Index out of bounds')
    # ensure list is unchanged
    print('List: ' + str(ll))
    print('List Size:', len(ll))
  except:
    print('Something went wrong. Not IndexError.')    

  try:
    # should NOT work

    # index == length of list
    print('Value at index len(ll): ')
    print(ll.get_element_at(len(ll)))
    print('***THIS SHOULD NOT HAVE WORKED***')
  
  except IndexError:
    print('Error: Index out of bounds')
    # ensure list is unchanged
    print('List: ' + str(ll))
    print('List Size:', len(ll))
  except:
    print('Something went wrong. Not IndexError.') 

  print()

  # empty list test
  print('Get element from an empty list. List: ' + str(empty_ll))
  try:
    # should NOT work

    print('Value at index 0:')
    empty_ll.get_element_at(0)
    print('***THIS SHOULD NOT HAVE WORKED***')
  
  except IndexError:
    print('Error: Index out of bounds')
    # ensure list is unchanged
    print('List: ' + str(empty_ll))
    print('List Size:', len(empty_ll))
  except:
    print('Something went wrong. Not IndexError.')

  print()

  # test list with one element
  one_element_ll.append_element(5) #add back the element removed earlier for more testing
  print('Get only element from list with length 1: ' + str(one_element_ll))
  try:
    # this should work

    print('Value at index 0: ' + str(one_element_ll.get_element_at(0)))
    print('List: ' + str(one_element_ll))
    print('List Size:', len(one_element_ll))

  except IndexError:
    print('Error: Index out of bounds')
    # ensure list is unchanged
    print('List: ' + str(one_element_ll))
    print('List Size:', len(one_element_ll))
  except:
    print('Something went wrong. Not IndexError.')    

  print()
  print()

  # TEST rotate_left METHOD
  print('TEST ROTATE_LEFT METHOD')
  # Multi-element list
  try:
    # this should work

    print('Current List: ' + str(ll))
    ll.rotate_left()
    print(ll)
    print('List Size:', len(ll))

  except IndexError:
    print('Error: Index out of bounds')
    # ensure list is unchanged
    print('List: ' + str(ll))
    print('List Size:', len(ll))
  except:
    print('Something went wrong. Not IndexError.')
  
  print()

  # Empty list
  try:
    # should run, no effect

    print('Current List: ' + str(empty_ll))
    empty_ll.rotate_left()
    print('Rotated left: ' + str(empty_ll))
    print('List Size:', len(empty_ll))

  except IndexError:
    print('Error: Index out of bounds')
    # ensure list is unchanged
    print('List: ' + str(empty_ll))
    print('List Size:', len(empty_ll))
  except:
    print('Something went wrong. Not IndexError.')

  print()

  # One element list
  try:
    # should run, no effect

    print('Current List: ' + str(one_element_ll))
    one_element_ll.rotate_left()
    print('Rotated left: ' + str(one_element_ll))
    print('List Size:', len(one_element_ll))

  except IndexError:
    print('Error: Index out of bounds')
    # ensure list is unchanged
    print('List: ' + str(one_element_ll))
    print('List Size:', len(one_element_ll))
  except:
    print('Something went wrong. Not IndexError.')

  print()
  print()  

  # TEST ITERATOR
  print('TESTING ITERATOR')
  print('Current List: ' + str(ll))
  print('Test Iterator:')
  for value in ll:
    print(value)

  print()

  # test empty list
  print('Current List: ' + str(empty_ll))
  print('Test Iterator:')
  for value in empty_ll:
    print(value)
  
  print()
  
  # test list with length 1
  print('Current List: ' + str(one_element_ll))
  print('Test Iterator:')
  for value in one_element_ll:
    print(value)


  print()

  print('Final List (general): ' + str(ll))
  print('List Size: ', len(ll))

  print()

  print('Final List (empty): ' + str(empty_ll))
  print('List Size: ', len(empty_ll))

  print()

  print('Final List (one element): ' + str(one_element_ll))
  print('List Size: ', len(one_element_ll)) 


    



  








  
  
  



