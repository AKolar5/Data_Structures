from Deque_Generator import get_deque

class Queue:

  def __init__(self):
    # TODO replace pass with your implementation.
    self.__dq = get_deque()

  def __str__(self):
    # TODO replace pass with your implementation.
    
    return str(self.__dq) #See deque operation

    # PERFORMANCE: O(n)

  def __len__(self):
    # TODO replace pass with your implementation.
    
    return len(self.__dq) #See deque operation

    # PERFORMANCE: O(1)

  # ***ZEROTH INDEX OF ARR OR HEAD OF LL IS FRONT OF QUEUE***

  def enqueue(self, val):
    # TODO replace pass with your implementation.
    
    self.__dq.push_back(val) #See deque operation

    # PERFORMANCE: O(1) FOR LL
    # PERFORMANCE: O(n) FOR ARR

  def dequeue(self):
    # TODO replace pass with your implementation.
    
    return self.__dq.pop_front() #See deque operation

    # PERFORMANCE: O(1)

  def peek(self):
    # TODO replace pass with your implementation.
    
    return self.__dq.peek_front() #See deque operation

    # PERFORMANCE: O(1)

# Unit tests make the main section unneccessary.
#if __name__ == '__main__':
#  pass
  
