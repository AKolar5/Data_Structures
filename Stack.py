from Deque_Generator import get_deque

class Stack:

  def __init__(self):
    # TODO replace pass with your implementation.
    self.__dq = get_deque()
    
    # PERFORMANCE: O(1)

  def __str__(self):
    # TODO replace pass with your implementation.
    
    return str(self.__dq) #See deque operation

    # PERFORMANCE: O(n)

  def __len__(self):
    # TODO replace pass with your implementation.
    
    return len(self.__dq) #See deque operation

    # PERFORMANCE: O(1)

  # ***INDEX 0 OF ARR OR HEAD OF LL IS TOP OF STACK***

  def push(self, val):
    # TODO replace pass with your implementation.
    
    self.__dq.push_front(val) #See deque operation

    # PERFORMANCE: O(1) for LL
    # PERFORMANCE: O(n) for ARR

  def pop(self):
    # TODO replace pass with your implementation.
    
    return self.__dq.pop_front() #See deque operation

    # PERFORMANCE: O(1)

  def peek(self):
    # TODO replace pass with your implementation.
    
    return self.__dq.peek_front() #See deque operation

    # PERFORMANCE: O(1)

# Unit tests make the main section unneccessary.
# if __name__ == '__main__':
  # pass
