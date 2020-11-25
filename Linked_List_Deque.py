from Deque import Deque
from Linked_List import Linked_List

class Linked_List_Deque(Deque):

  def __init__(self):
    self.__list = Linked_List()

    # PERFORMANCE: O(1)

  def __str__(self):
    return str(self.__list)

  def __len__(self):
    return len(self.__list)

    # PERFORMANCE: O(1)
  
  # DO NOT CHANGE ANYTHING ABOVE THIS LINE
  
  # ***FRONT OF LIST IS AT THE HEAD (INDEX ZERO)***

  def push_front(self, val):
    # TODO replace pass with your implementation.

    # Can't insert into an empty Linked List
    if len(self.__list) == 0:
      self.__list.append_element(val)
    
    # Insert val at 0th index of the Linked List
    else:
      self.__list.insert_element_at(val, 0)

    # PERFORMANCE: O(1)
  
  def pop_front(self):
    # TODO replace pass with your implementation.

    # Avoid IndexError by returning None 
    if len(self.__list) == 0:
      return None
    
    # Remove/return element at 0th index 
    return self.__list.remove_element_at(0)

    # PERFORMANCE: O(1)

  def peek_front(self):
    # TODO replace pass with your implementation.

    if len(self.__list) == 0:
      return None
    
    return self.__list.get_element_at(0)

    # PERFORMANCE: O(1)

  def push_back(self, val):
    # TODO replace pass with your implementation.
    
    self.__list.append_element(val)

    # PERFORMANCE: O(1)
  
  def pop_back(self):
    # TODO replace pass with your implementation.

    # Avoid IndexError by returning None
    if len(self.__list) == 0:
      return None
    
    # Remove/return last element in the list
    return self.__list.remove_element_at(len(self.__list) - 1)

    # PERFORMANCE: O(1)

  def peek_back(self):
    # TODO replace pass with your implementation.

    if len(self.__list) == 0:
      return None
    
    return self.__list.get_element_at(len(self.__list) - 1)

    # PERFORMANCE: O(1)

# Unit tests make the main section unneccessary.
#if __name__ == '__main__':
#  pass
