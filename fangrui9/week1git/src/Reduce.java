public class Reduce {

    public static int reduce(int n) {
        int count = 0;
        while(n != 0) {
            if(n % 2 == 0){
                n = n /2;
            } else {
                n = n - 1;
            }
            count ++;
        }
        return count;
    }

    public static int main(int n) {
        return reduce(n);
    }

    public static int main() {
        return reduce(2);
    }
}

