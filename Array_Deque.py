from Deque import Deque

class Array_Deque(Deque):

  def __init__(self):
    # capacity starts at 1; we will grow on demand.
    self.__capacity = 1
    self.__contents = [None] * self.__capacity
    # TODO replace pass with any additional initializations you need.
    
    self.__f = None #front of deque intialized to None
    self.__b = None #back of deque initialized to None
    self.__size = 0 #set size to zero
    
    # PERFORMANCE: O(1)

  def __str__(self):
    # TODO replace pass with an implementation that returns a string of
    # exactly the same format as the __str__ method in the Linked_List_Deque.
    
    # special case
    if self.__size == 0:
      return '[ ]'
    
    # put deque values into an ordered array
    # front at index zero
    lst = [None] * self.__size
    for i in range(len(lst)):
      lst[i] = str(self.__contents[(self.__f + i) % len(self.__contents)])
    
    string = '[ ' + ', '.join(lst) + ' ]'
    return string

    # PERFORMANCE: O(n)

  def __len__(self):
    # TODO replace pass with an implementation that returns the number of
    # items in the deque. This method must run in constant time.
    return self.__size

    # PERFORMANCE: O(1)

  def __grow(self):
    # TODO replace pass with an implementation that doubles the capacity
    # and positions existing items in the deque starting in cell 0 (why is
    # necessary?)

    self.__capacity *= 2 #double capacity
    old_array = self.__contents #make an alias for contents
    self.__contents = [None] * (self.__capacity) #assign self.contents to an empty array with new cap
    
    # put items from old array into self.__contents
    # deal with circularity via modulo
    for i in range(len(old_array)):
      self.__contents[i] = old_array[(self.__f + i) % len(old_array)]
    
    self.__f = 0 #set the front to index zero
    self.__b = len(old_array) - 1 #the back index is length of the old array

    # PERFORMANCE: O(n)
    
  def push_front(self, val):
    # TODO replace pass with your implementation, growing the array before
    # pushing if necessary.
    
    # grow contents if new cell exceeds capacity
    if self.__size + 1 > self.__capacity:
      self.__grow()

    # if this is the only element in the deque
    # the front and back pointers need to be assigned to index zero
    if self.__size == 0:
      self.__f = 0
      self.__b = self.__f

    else:
      # move front back an index
      # modulo prevents negative indexing
      self.__f = ((self.__f - 1) + len(self.__contents)) % len(self.__contents)  
    
    self.__contents[self.__f] = val 
    self.__size += 1

    # PERFORMANCE: O(n)

  def pop_front(self):
    # TODO replace pass with your implementation. Do not reduce the capacity.
    
    # special case
    if self.__size == 0:
      return None
    
    elif self.__size == 1:
      value = self.__contents[self.__f] #store value at front index
      # Set front and back to None, since deque will be empty
      self.__f = None
      self.__b = None
      self.__size -= 1 #decrement size
      return value

    else:
      value = self.__contents[self.__f] #store value at front index
      self.__f = (self.__f + 1) % len(self.__contents) #increment front by 1
      self.__size -= 1 #decrement size
      return value

    # PERFORMANCE: O(1)
    
  def peek_front(self):
    # TODO replace pass with your implementation.
    
    # special case
    if self.__size == 0:
      return None
    
    return self.__contents[self.__f] #return value at front index

    # PERFORMANCE: O(1)
    
  def push_back(self, val):
    # TODO replace pass with your implementation, growing the array before
    # pushing if necessary.

    # grow contents if new cell exceeds capacity
    if self.__size + 1 > self.__capacity:
      self.__grow()
    
    # if this is the only element in the deque
    # the front and back pointers need to be assigned to index zero
    if self.__size == 0:
      self.__b = 0
      self.__f = self.__b

    else:
      # increment back index 
      # modulo prevents out of bounds indexing
      self.__b = (self.__b + 1) % len(self.__contents)

    self.__contents[self.__b] = val #assign value to new back index
    self.__size += 1 #increment size

    # PERFORMANCE: O(n)

  def pop_back(self):
    # TODO replace pass with your implementation. Do not reduce the capacity.
    
    # special case
    if self.__size == 0:
      return None
    
    elif self.__size == 1:
      value = self.__contents[self.__b]
      # Set front and back to None, since deque will be empty 
      self.__f = None
      self.__b = None
      self.__size -= 1 #decrement size
      return value

    else:  
      value = self.__contents[self.__b] #store value at back index
      self.__b = ((self.__b - 1) + len(self.__contents)) % len(self.__contents) #decrement back
      self.__size -= 1 #decrement size
      return value

    # PERFORMANCE: O(1) 

  def peek_back(self):
    # TODO replace pass with your implementation.
    
    # special case
    if self.__size == 0:
      return None

    return self.__contents[self.__b] #return value at back index

    # PERFORMANCE: O(1)

# No main section is necessary. Unit tests take its place.
# if __name__ == '__main__':
  # pass