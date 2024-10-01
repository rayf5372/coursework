public class BSTMultiSet extends MultiSet {

    private final BST bst = new BST();

    @Override
    void add(Integer item) {
        bst.insert(item);
    }

    @Override
    void remove(Integer item) {
        bst.delete(item);
    }

    @Override
    boolean contains(Integer item) {
        return bst.contains(item);
    }

    @Override
    boolean isEmpty() {
        return bst.isEmpty();
    }

    @Override
    int count(Integer item) {
        return bst.count(item);
    }

    @Override
    int size() {
        return bst.getLength();
    }

}