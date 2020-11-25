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
      self.__set_height(t)       
      return t
    
    # Recursive case
    # val is greater than t's value
    # insert val into tree rooted at t's right child
    # update t's right child, then height
    # return t to the function that called it  
    else:
      t.right = self.__recursive_insert(val, t.right)
      self.__set_height(t) 
      return t

    # PERFORMANCE: O(n)

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
      
      self.__set_height(t) #update t's height
      
      return t
    
    # Recursive case
    # val is less than t's value
    # delete val from the subtree rooted at t's left child
    # update t's left child, then height
    # return t to the function that called it
    elif val < t.value:
      t.left = self.__recursive_removal(val, t.left)
      
      self.__set_height(t)      
      
      return t

    # Recursive case
    # val is greater than t's value
    # delete val from the subtree rooted at t's right child
    # update t's right child, then height
    # return t to the function that called it
    else:
      t.right = self.__recursive_removal(val, t.right)

      self.__set_height(t)       

      return t 
    
    # PERFORMANCE: O(n)

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

    # PERFORMANCE: O(n)

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

    # PERFORMANCE: O(n)

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
  tree = Binary_Search_Tree()
  tree.insert_element(True)
  tree.insert_element(False)
  tree.insert_element(1)
  print(tree)

