from .specs import registry
class BinaryOperator(object):
    def test(self, left, right):
        pass

class LessThan(BinaryOperator):
    
    def test(self, left, right):
        return left < right
    def __str__(self):
        return "<"

class Equals(BinaryOperator):
    def test(self, left, right):
        return left == right
    def __str__(self):
        return "=="

registry.registerOp("<", LessThan)
registry.registerOp("==", Equals)