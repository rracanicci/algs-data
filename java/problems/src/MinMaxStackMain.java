import java.util.Stack;

public class MinMaxStackMain {
    public static class MinMaxStack<T extends Comparable<T>> {
        private Stack<T> mainStack, minStack, maxStack;

        public MinMaxStack() {
            mainStack = new Stack<T>();
            minStack = new Stack<T>();
            maxStack = new Stack<T>();
        }

        public void push(T x) {
            mainStack.push(x);
            if (minStack.empty() || x.compareTo(minStack.peek()) <= 0) {
                minStack.push(x);
            }
            if (maxStack.empty() || x.compareTo(maxStack.peek()) >= 0) {
                maxStack.push(x);
            }
        }

        public T pop() {
            if (minStack.peek() == mainStack.peek()) {
                minStack.pop();
            }
            if (maxStack.peek() == mainStack.peek()) {
                maxStack.pop();
            }
            return mainStack.pop();
        }

        public T top() {
            return mainStack.peek();
        }

        public T getMin() {
            return minStack.peek();
        }

        public T getMax() {
            return maxStack.peek();
        }
    }

    public static void main(String[] args) {
        MinMaxStack<Integer> s = new MinMaxStack<>();

        s.push(1);
        s.push(2);
        s.push(3);
        assert(s.top() == 3);
        assert(s.getMin() == 1);
        assert(s.getMax() == 3);

        s.push(-1);
        assert(s.top() == -1);
        assert(s.getMin() == -1);
        assert(s.getMax() == 3);

        s.pop();
        assert(s.top() == 3);
        assert(s.getMin() == 1);
        assert(s.getMax() == 3);

        s.pop();
        assert(s.top() == 2);
        assert(s.getMin() == 1);
        assert(s.getMax() == 2);

        s.pop();
        assert(s.top() == 1);
        assert(s.getMin() == 1);
        assert(s.getMax() == 1);
    }
}
