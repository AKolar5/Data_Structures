class Binary_Search_Tree:
  # TODO.I have provided the public method skeletons. You will need
  # to add private methods to support the recursive algorithms
  # discussed in class

  class __BST_Node:
    # TODO The Node class is private. You may add any attributes and
    # methods you need. Recall that attributes in an inner class 
    # must be public to be reachable from the the methods.

    def __init__(self, value):
      self.value = value #value contained in the Node 
      self.right = None #Node's right child
      self.left = None #Node's left child
      self.height = 1 #height is initially one

      # PERFORMANCE: O(1)

  def __init__(self):
    self.__root = None #access point
    
    # PERFORMANCE: O(1)

  # Rotates a left heavy tree rooted at t right
  def __rotate_right(self, t):
    temp = t.left.right #floater
    t.left.right = t #old root is right child of old left child
    t = t.left #new root is old left child 
    t.right.left = temp #old root's left child is floater
    
    # Recalc heights
    self.__set_height(t.right)
    self.__set_height(t)
    return t

    # PERFORMANCE: O(1)

  # Rotates a right heavy tree rooted a t left
  def __rotate_left(self, t):
    temp = t.right.left #floater 
    t.right.left = t #old root is left child of old right child
    t = t.right #new root is old right child 
    t.left.right = temp #old root's right child is floater
    
    # Recalc heights
    self.__set_height(t.left)
    self.__set_height(t)
    return t

    # PERFORMANCE: O(1)

  # Scenarios if t has any None references
  def __check_Nones(self, t):
    if t is None:
      self.__set_height(t)
      return t

    if t.left is None or t.right is None:

      # t is a leaf
      if t.left is None and t.right is None:
        self.__set_height(t)
        return t

      # t is right heavy
      if t.left is None and t.right.height > 1:
        if t.right.right is not None and t.right.left is not None:
          
          # t.right is not left heavy, rotate left to balance t
          if t.right.right.height - t.right.left.height >= 0: #17
            t = self.__rotate_left(t)
            
            self.__set_height(t)
            return t

          # t.right is left heavy, double rotate to balance t
          else:
            t.right = self.__rotate_right(t.right)
            t = self.__rotate_left(t)
            
            self.__set_height(t)
            return t

        # t.right is left heavy because it doesn't have a right child
        # double rotate to balance t
        elif t.right.right is None: #3 #11 #14
          t.right = self.__rotate_right(t.right)
          t = self.__rotate_left(t)
          
          self.__set_height(t)
          return t

        # t.right is not left heavy because it doesn't have a left child
        # rotate left to balance t
        elif t.right.left is None: #1 #13 
          t = self.__rotate_left(t)
          
          self.__set_height(t)
          return t

      # t leans right but doesn't need to be rotated
      elif t.left is None and t.right.height == 1:
        self.__set_height(t)
        return t  
      
      # t is left heavy
      elif t.right is None and t.left.height > 1:
        if t.left.right is not None and t.left.left is not None:
          
          # t.left is not right heavy, rotate right to balance t
          if t.left.right.height - t.left.left.height <= 0: #10
            t = self.__rotate_right(t)
            
            self.__set_height(t)
            return t

          # t.left is right heavy, double rotate to balance t
          else:
            t.left = self.__rotate_left(t.left)
            t = self.__rotate_right(t)
            
            self.__set_height(t)
            return t

        # t.left is left heavy because it doesn't have a right child
        # rotate right to balance t
        elif t.left.right is None: #5 #8 #9
          t = self.__rotate_right(t)
          
          self.__set_height(t)
          return t

        # t.left is right heavy because it doesn't have a left child
        # double rotate to balance t
        elif t.left.left is None: #7 #12
          t.left = self.__rotate_left(t.left) 
          t = self.__rotate_right(t)
          
          self.__set_height(t)
          return t
        
      # t leans left but doesn't need to be rotated      
      elif t.right is None and t.left.height == 1:
        self.__set_height(t)
        return t

    # t does not have any None children
    else:
      return 'Continue' 

    # PERFORMANCE: O(1)

  # Determines if t is imbalanced and returns a balanced
  # tree with the same values in the subtree 
  def __balance(self, t):
    # check t for None references to avoid errors
    test = self.__check_Nones(t)
    if test != 'Continue':
        t = test
        
        self.__set_height(t)
        return t

    # Check if t is left heavy
    if t.right.height - t.left.height == -2:

      # If t.left is not right heavy, rotate right
      # to balance t
      if t.left.right.height - t.left.left.height <= 0: #6
        t = self.__rotate_right(t)
        
        self.__set_height(t)
        return t
      
      # t.left is right heavy, double rotation
      # to balance t
      else: #16
        t.left = self.__rotate_left(t.left)        
        t = self.__rotate_right(t)        
        
        self.__set_height(t)
        return t

    # Check if t is right heavy
    elif t.right.height - t.left.height == 2:
      
      # If t.right is not left heavy, rotate left
      # to balance t
      if t.right.right.height - t.right.left.height >= 0: #2 #15
        t = self.__rotate_left(t)        
        
        self.__set_height(t)
        return t
        
      # t.right is left heavy, double rotation
      # to balance t
      else: #4
        t.right = self.__rotate_right(t.right)        
        t = self.__rotate_left(t)
        
        self.__set_height(t)
        return t

    # t is already balanced
    else:
      self.__set_height(t)
      return t

    # PERFORMANCE: O(1)

  # Sets height of a given Node 't'
  def __set_height(self, t):
      # __recursive_removal could call with None as parameter
      if t is None:
        return #return nothing to avoid crash
      
      # t is a leaf
      elif t.left is None and t.right is None:
        t.height = 1
      
      # t's height will always be one more than its greatest child 
      
      # t only has a right child 
      elif t.left is None:
        t.height = t.right.height + 1

      # t only has a left child
      elif t.right is None:
        t.height = t.left.height + 1

      elif t.left.height > t.right.height:
        t.height = t.left.height + 1

      else:
        t.height = t.right.height + 1

      # PERFORMANCE: O(1)

  # Uses recursion to insert a Node with value 'val' 
  # into the tree rooted at a Node t 
  def __recursive_insert(self, val, t):    
    # Base case
    # Create and return a Node with the value val
    if t is None:           
      return Binary_Search_Tree.__BST_Node(val) 

    # Base case
    # val is already in the tree    
    if t.value == val:
      raise ValueError

    # Recursive case
    # val is less than t's value
    # insert val into tree rooted at t's left child
    # update t's left child, then height
    # return t to the function that called it
    elif val < t.value:
      t.left = self.__recursive_insert(val, t.left)

      return self.__balance(t)
    
    # Recursive case
    # val is greater than t's value
    # insert val into tree rooted at t's right child
    # update t's right child, then height
    # return t to the function that called it  
    else:
      t.right = self.__recursive_insert(val, t.right)
            
      return self.__balance(t)

    # PERFORMANCE: O(log(n))

  # Uses recursion to remove a Node with value 'val' 
  # from the tree rooted at a Node t 
  def __recursive_removal(self, val, t):
    # Base case
    # val is not in the tree
    if t == None:
      raise ValueError
    
    # Base case
    # t is the Node to be removed
    if t.value == val:
      # t has 2 children 
      if t.left is not None and t.right is not None:        
        # Replace the value to be removed with the value in
        # the tree that is the next highest 
        cur = t.right
        while cur.left is not None:
          cur = cur.left
        t.value = cur.value

        # remove the node who's value was copied to eliminate duplicates
        t.right = self.__recursive_removal(cur.value, t.right)
      
      # t only has a right child
      elif t.left is None:
        t = t.right
      
      # t only has a left child, or no children
      else:
        t = t.left             
            
      return self.__balance(t)
    
    # Recursive case
    # val is less than t's value
    # delete val from the subtree rooted at t's left child
    # update t's left child, then height
    # return t to the function that called it
    elif val < t.value:
      t.left = self.__recursive_removal(val, t.left)
            
      return self.__balance(t)

    # Recursive case
    # val is greater than t's value
    # delete val from the subtree rooted at t's right child
    # update t's right child, then height
    # return t to the function that called it
    else:
      t.right = self.__recursive_removal(val, t.right)
    
      return self.__balance(t) 
    
    # PERFORMANCE: O(log(n))

  # Public insertion method
  def insert_element(self, value):
    # Insert the value specified into the tree at the correct
    # location based on "less is left; greater is right" binary
    # search tree ordering. If the value is already contained in
    # the tree, raise a ValueError. Your solution must be recursive.
    # This will involve the introduction of additional private
    # methods to support the recursion control variable.
    
    # Insert the value into a tree rooted at self.__root recursively 
    node = self.__recursive_insert(value, self.__root)
    self.__root = node #the Node returned will be the root of the tree
    

    # PERFORMANCE: O(log(n))

  def remove_element(self, value):
    # Remove the value specified from the tree, raising a ValueError
    # if the value isn't found. When a replacement value is necessary,
    # select the minimum value to the from the right as this element's
    # replacement. Take note of when to move a node reference and when
    # to replace the value in a node instead. It is not necessary to
    # return the value (though it would reasonable to do so in some 
    # implementations). Your solution must be recursive. 
    # This will involve the introduction of additional private
    # methods to support the recursion control variable.
    
    # Remove the value from a tree rooted at self.__root recursively
    node = self.__recursive_removal(value, self.__root)
    self.__root = node #the Node returned will be the root of the tree
    

    # PERFORMANCE: O(log(n))

  # Uses recursion to build a list of the values in a tree
  # rooted at root
  def __to_list_recursive(self, root, list):

    # root is a leaf, add it to the list
    if root.left is None and root.right is None:
        list.append(root.value)

    # root doesn't have a left child
    # add root to the list and go right 
    elif root.left is None:
        list.append(root.value)
        self.__to_list_recursive(root.right, list)

    # root doesn't have a right child
    # recur left, then add root to the list
    elif root.right is None:
        self.__to_list_recursive(root.left, list)
        list.append(root.value)
    
    # root has both children
    # go left, add root, then go right
    else:
        self.__to_list_recursive(root.left, list)
        list.append(root.value)
        self.__to_list_recursive(root.right, list)

    # PERFORMANCE: O(n^2)
  
  # Uses recursion to find the in-order traversal of a tree
  # rooted at root
  def __in_order_recursive(self, root):
    # Base case
    # Return empty string
    if root is None:
      return ''
    
    # Recursive case
    # Combine the in-order traversal of root's left child,
    # root's value, and the in-order traversal of root's right child
    else:
      return str(self.__in_order_recursive(root.left)) \
         + str(root.value) \
         + ', ' + str(self.__in_order_recursive(root.right))

    # PERFORMANCE: O(n^2) 

  # Uses recursion to find the pre-order traversal of a tree
  # rooted at root
  def __pre_order_recursive(self, root):
    # Base case
    # Return empty string
    if root is None:
      return ''
    
    # Recursive case
    # Combine root's value, pre-order traversal
    # of root's left child, and the pre-order traversal of root's 
    # right child
    else:
      return str(root.value) \
        + ', ' + str(self.__pre_order_recursive(root.left)) \
         + str(self.__pre_order_recursive(root.right))

    # PERFORMANCE: O(n^2)

  # Uses recursion to find the post-order traversal of a tree
  # rooted at root
  def __post_order_recursive(self, root):
    # Base case
    # Return empty string
    if root is None:
      return ''
    
    # Recursive case
    # Combine the post-order traversal of root's left child,the 
    # post-order traversal of root's right child, and root's value
    else:
      return str(self.__post_order_recursive(root.left)) \
         + str(self.__post_order_recursive(root.right)) \
           + str(root.value) + ', '

    # PERFORMANCE: O(n^2)
  
  # Constructs an in order list of the values in the tree
  def to_list(self):
    # Special case
    if self.__root is None:
      return []

    lst = []
    self.__to_list_recursive(self.__root, lst)
    
    return lst
  
  # PERFORMANCE: O(n^2)

  def in_order(self):
    # Construct and return a string representing the in-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed as [ 4 ]. Trees with more
    # than one value should be printed as [ 4, 7 ]. Note the spacing.
    # Your solution must be recursive. This will involve the introduction
    # of additional private methods to support the recursion control 
    # variable.
    
    # special case
    if self.__root is None:
      return '[ ]'

    # Concatenate the in-order traversal of self.__root's left child,
    # self.__root's value, and the in-order traversal of self.__root's
    # right child
    string = '[ ' + self.__in_order_recursive(self.__root.left) \
      + str(self.__root.value) + ', ' \
        + self.__in_order_recursive(self.__root.right)
    
    # slice off the last comma, add closing bracket
    string = string[0:len(string)-2] + ' ]'
    return string

    # PERFORMANCE: O(n^2)

  def pre_order(self):
    # Construct and return a string representing the pre-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed in as [ 4 ]. Trees with
    # more than one value should be printed as [ 4, 7 ]. Note the spacing.
    # Your solution must be recursive. This will involve the introduction
    # of additional private methods to support the recursion control 
    # variable.

    # special case
    if self.__root is None:
      return '[ ]'

    # Concatenate self.__root's value, the pre-order traversal of 
    # self.__root's left child, and the pre-order traversal of self.root's
    # left child
    string = '[ ' + str(self.__root.value) + ', ' \
      + self.__pre_order_recursive(self.__root.left) \
        + self.__pre_order_recursive(self.__root.right)
    
    # slice off the last comma, add closing bracket
    string = string[0:len(string)-2] + ' ]'
    return string

    # PERFORMANCE: O(n^2)

  def post_order(self):
    # Construct an return a string representing the post-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed in as [ 4 ]. Trees with
    # more than one value should be printed as [ 4, 7 ]. Note the spacing.
    # Your solution must be recursive. This will involve the introduction
    # of additional private methods to support the recursion control 
    # variable.

    # special case
    if self.__root is None:
      return '[ ]'

    # Concatenate post-order traversal self.__root's left child,
    # the post-order traversal of self.__root's right child, and
    # the value of self.__root 
    string = '[ ' + self.__post_order_recursive(self.__root.left) \
      + self.__post_order_recursive(self.__root.right) \
        + str(self.__root.value) + ' ]'
        
    return string

    # PERFORMANCE: O(n^2)

  def get_height(self):
    # return an integer that represents the height of the tree.
    # assume that an empty tree has height 0 and a tree with one
    # node has height 1. This method must operate in constant time.
    
    # special case
    if self.__root is None:
      return 0
    
    # the height of the root is the height of the entire tree
    return self.__root.height

    # PERFORMANCE: O(1)

  def __str__(self):
    return self.in_order()

    # PERFORMANCE: O(n^2)

if __name__ == '__main__':
  pass

