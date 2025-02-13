class Solution {
    public int calPoints(String[] operations) {
        Stack<Integer> stack = new Stack<>();
        for(int i=0;i<operations.length;i++) {
            if(operations[i].equals("+")) {
                int val1 = stack.pop();
                int val2 = stack.peek();
                stack.push(val1);
                stack.push(val1 + val2);
            } else if(operations[i].equals("D")) {
                int val = stack.peek();
                stack.push(2*val);
            } else if(operations[i].equals("C")) {
                stack.pop();
            } else {
                int val = Integer.parseInt(operations[i]);
                stack.push(val);
            }
        }

        int sum = 0;
        while(stack.size() > 0) {
            sum += stack.pop();
        }
        return sum;
    }
}