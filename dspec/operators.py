from .specs import registry


class BinaryOperator(object):
    def test(self, left, right):
        pass


class LessThan(BinaryOperator):
    def test(self, left, right):
        return left < right

    def __str__(self):
        return "<"

class TRUE(BinaryOperator):
    def test(self, left, right=None):
        return left 

    def __str__(self):
        return "isTrue"

class FALSE(BinaryOperator):
    def test(self, left, right=None):
        return left 

    def __str__(self):
        return "isTrue"

class MoreThan(BinaryOperator):
    def test(self, left, right):
        return left > right

    def __str__(self):
        return ">"

class LessThanEquals(BinaryOperator):
    def test(self, left, right):
        return left <= right

    def __str__(self):
        return "<="


class MoreThanEquals(BinaryOperator):
    def test(self, left, right):
        return left >= right

    def __str__(self):
        return ">="


class Equals(BinaryOperator):
    def test(self, left, right):
        return left == right

    def __str__(self):
        return "=="


class Range(BinaryOperator):
    def test(self, left, right):
        return left <= right[0] and left >= right[1]

    def __str__(self):
        return "in"

__ops = [LessThan, LessThanEquals, MoreThan, MoreThanEquals, Equals, Range, TRUE, FALSE]
for op in __ops:
    registry.registerOp(str(op()), op)

