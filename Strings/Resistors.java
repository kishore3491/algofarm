/**
*
*/
import java.util.*;

class Resistors{
    /**
    * Given a sequence of a resistor network,
    * Where resistors may be connected in series or parallel,
    * get the total resistance of network.
    */
    public static int getResistance(String resistorSequence) throws Exception{
        Stack<Character> paranths = new Stack();
        Stack<Integer> values = new Stack();
        Stack<Character> symbols = new Stack();

        int cval = -1;
        int cnum = 0, numPos = 0;
        int slen = resistorSequence.length();
        int zeroVal = Integer.valueOf('0');
        char c = ' ';

        for (int i = slen - 1; i >=0; i--) {
            c = resistorSequence.charAt(i);
            cval = Integer.valueOf(c);
            if (47 < cval && cval < 58) {
                cnum += (cval - zeroVal)*((int)Math.pow(10, numPos));
                numPos += 1;
            }
            else{
                if (cnum > 0){
                    values.push(cnum);
                    numPos = 0; cnum = 0;
                }
                // Scale to use different characters.
                if (cval == 41){
                    paranths.push(c);
                }
                else if (cval == 43 || cval == 124){
                    symbols.push(c);
                }
                else if (cval == 40){
                    if (paranths.pop() == ')' && !symbols.isEmpty()){
                        int tmp = getValue(values.pop(), values.pop(), symbols.pop());
                        values.push(tmp);
                    }
                }
            }
        }

        while(!symbols.isEmpty()) {
            int tmp = getValue(values.pop(), values.pop(), symbols.pop());
            values.push(tmp);
        }

        int res = values.pop();

        if (!values.isEmpty()){
            throw new Exception("Invalid circuit format.");
        }
        else{
            return res;
        }
    }

    private static int getValue(int val1, int val2, char operation) throws Exception{
        if (operation == '+'){
            return val1 + val2;
        }
        else if (operation == '|'){
            return (val1*val2)/(val1 + val2);
        }
        else{
            // InvalidValueException
            throw new Exception();
        }
    }

    public String buildCircuit(){
        // TODO
        return "";
    }

    public static void main(String[] args) throws Exception{
        runTest1();
    }

    public static void runTest1() throws Exception{
        String c1 = "(400)";
        String c2 = "(500+200)";
        String c3 = "(300|200)";
        String c4 = "(75|75)+(25|25)";
        String c5 = "(500|(200+300))";

        System.out.println(getResistance(c1) == 400);
        System.out.println(getResistance(c2) == 700);
        System.out.println(getResistance(c3) == 120);
        System.out.println(getResistance(c4) == 50);
        System.out.println(getResistance(c5) == 250);
    }
}
