# EASY
#
# Design a max stack that supports push, pop, top, peekMax and popMax.
#
# push(x) -- Push element x onto stack.
# pop() -- Remove the element on top of the stack and return it.
# top() -- Get the element on the top.
# peekMax() -- Retrieve the maximum element in the stack.
# popMax() -- Retrieve the maximum element in the stack, and remove it. If you find more than one maximum elements,
# only remove the top-most one.
#
# Constraints:
#
# -1e7 <= x <= 1e7
# Number of operations won't exceed 10000.
# The last four operations won't be called when stack is empty.


class MaxStack:
    def __init__(self):
        self.data = []

    def push(self, x):
        self.data.append(x)

    def pop(self) -> int:
        return self.data.pop()

    def top(self) -> int:
        return self.data[-1]

    def peekMax(self) -> int:
        return max(self.data)

    def popMax(self) -> int:
        mx = max(self.data)
        for i, val in enumerate(self.data[::-1]):
            idx = len(self.data) - i - 1
            if val == mx:
                return self.data.pop(idx)


if __name__ == "__main__":
    max_stack = MaxStack()
    max_stack.push(5)
    max_stack.push(1)
    max_stack.push(5)
    print("top", max_stack.top())  # -> 5
    print("pop max", max_stack.popMax())  # -> 5
    print("top", max_stack.top())  # -> 1
    print("peek max", max_stack.peekMax())  # -> 5
    print("pop", max_stack.pop())  # -> 1
    print("pop", max_stack.top())  # -> 5
