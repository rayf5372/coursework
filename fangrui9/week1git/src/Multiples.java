public class Multiples {

    public static int countMultiples(int n, int a, int b) {

        int count = 0;

        for (int i = 1; i < n; i ++) {

            boolean multipleofa = i % a == 0;
            boolean multipleofb = i % b == 0;


            if (multipleofa || multipleofb) {
                count ++;
            }

        }

        return count;

    }

    public static int main(int n, int a, int b) {
        return countMultiples(n, a, b);
    }

    public static int main() {
        return countMultiples(1000, 3, 5);
    }
}
