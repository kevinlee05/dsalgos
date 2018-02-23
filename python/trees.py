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

    def depth(self, p):
        """return the number of levels separating position p from the root"""
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))

    def _height1(self):
        """return the height of the tree."""
        return max(self.depth(p) for p in self.positions() if self.is_leaf(p))

    def _height2(self, p):
        """ return height of subtree rooted at Position p """
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self._height2(c) for c in self.children(p))

    def height(self, p=None):
        """
        Return the height of the subtree rooted at Position p
        If p is None, return the height of the entire tree
        """
        if p is None:
            p = self.root()
        return self._height2(p) # start _height2 recursion

class BinaryTree(Tree):
    """Abstract base class representing a binary tree structure."""

    #---additional abstract methods ---
    def left(self, p):
        """ return a position representing p's left child
        return None if p does not have a left child
        """
        raise NotImplementedError('must be implemented by subclass')

    def right(self, p):
        """ return a position representing p's right child
        return None if p does not have a right child
        """
        raise NotImplementedError('must be implemented by subclass')

    def sibling(self, p):
        """ return a Position representing p's sibling (or None if no Sibling)"""
        parent = self.parent(p)
        if parent is None:
            return None
        else:
            if p == self.left(parent):
                return self.right(parent) # possibly None
            else:
                return self.left(parent) # possibly None

    def children(self, p):
        """ generate an interation of Positions representing p's children """
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)










