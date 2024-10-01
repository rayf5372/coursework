import java.util.ArrayList;
import java.util.List;
import java.util.Random;

/**
 * The Main class contains the main method with the timing experiment.
 * This file is provided; do not modify.
 */
public class Main {
    public static void main(String[] args) {

        // this corresponds to the main block from the provided python code.


        List<MultiSet> multisets = new ArrayList<>();
        multisets.add(new BSTMultiSet());

        for (MultiSet m :
                multisets) {
            for (int n :
                    new int[] {500, 1000, 2000, 4000, 8000, 16000}) {
                profileMultiSet(m, n);
            }
        }
    }

    /**
     * Run the timing experiment for the given MultiSet implementation and
     * problem size.
     *     """
     * @param m the MultiSet object
     * @param n the problem size
     */
    private static void profileMultiSet(MultiSet m, int n) {

        List<Integer> itemsAdded = new ArrayList<>();
        Random random = new Random();
        for (int i = 0; i < n; i++) {
            int x = random.nextInt(100);
            m.add(x);
            itemsAdded.add(x);
        }
        if (m.size() != n) {
            System.out.println("adding the items failed!");
            return;
        }

        final long startTime = System.nanoTime();
        for (int x :
                itemsAdded) {
            m.remove(x);
        }

        final long endTime = System.nanoTime();

        if (!m.isEmpty()) {
            System.out.println("removing items failed!");
            return;
        }

        // you can hover printf if you want to learn more about the string formatting syntax
        System.out.printf("%5d %20s %2.2es%n", n, m.getClass(), (endTime - startTime)/1_000_000_000.0f);
    }
}