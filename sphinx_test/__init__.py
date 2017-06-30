

class A(object):
    """Create a new A

    parameters
    ----------
    a : str
        The a.
    """

    def __init__(self, a):
        self._a = a

    def b(self):
        """b the a"""
        return self._a + 'b'
