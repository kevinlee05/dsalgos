class Tree:
    """Abstract base class representing a tree structure"""

    #--- nested Position class
    class Position:
        """An abstraction representing the location of a single element"""

        def element(self):
            """return the element stored at this position"""
            raise NotImplementedError('must be implemented by subclass')

        def __eq__(self, other):
            """return True if other Position represents the same location"""
            raise NotImplementedError('must be implemented by subclass')

        def __ne__(self, other):
            """return True if other does not represent the same location"""
            return not(self == other)  # opposite of __eq__

    #--- abstract methods that concrete subclass must support ---
    def root(self):
        """ return position representing the tree's root (or None if empty)"""
        raise NotImplementedError('must be implemented by subclass')

    def parent(self, p):
        """ return position representing p's parent(or none if p is root)"""
        raise NotImplementedError('must be implemented by subclass')

    def num_children(self, p):
        """ return the number of children that Position p has."""
        raise NotImplementedError('must be implemented by subclass')

    def children(self, p):
        """ Generate an iteration of Positions representing p's children."""
        raise NotImplementedError('must be implemented by subclass')

    def __len__(self):
        """ return the total number of elements in the tree"""
        raise NotImplementedError('must be implemented by subclass')

    #--- concrete methods implemented in this class ---
    def is_root(self, p):
        """ return True if position p represents the root of the tree"""
        return self.root() == p

    def is_leaf(self, p):
        """ return True if Position p has no children"""
        return self.numchildren(p) == 0

    def is_empty(self, p):
        """ return True if this tree is empty"""
        return len(self) == None



