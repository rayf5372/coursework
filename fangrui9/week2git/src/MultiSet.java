/**
 * Abstract class representing a MultiSet ADT.
 * This file is provided; do not modify.
 */
public abstract class MultiSet {

    /**
     * Add the given item to this multiset.
     * @param item the item to add
     */
    abstract void add(Integer item);

    /**
     * Remove the given item from this multiset.
     * If the item isn't in the multiset, do nothing.
     * @param item the item to remove
     */
    abstract void remove(Integer item);

    /**
     * Check whether item is in this multiset.
     * @param item the item to check if in this multiset
     * @return True if item is in this multiset and False otherwise.
     */
    abstract boolean contains(Integer item);

    /**
     * @return True if this multiset is empty.
     */
    abstract boolean isEmpty();

    /**
     * Count how many times the given item appears in this multiset.
     * @param item the item to count
     * @return How many times item appears in this multiset.
     */
    abstract int count(Integer item);


    /**
     * @return How many items are in this multiset.
     */
    abstract int size();

}
