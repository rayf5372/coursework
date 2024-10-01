import org.junit.Test;

import static org.junit.Assert.*;

/**
 * This is a subset of the self tests available on MarkUs; it only tests BST.java.
 * Note that there will also be additional hidden tests of BST.java when your homework
 * is graded, so make sure to do some additional double-checking of the correctness of
 * your code.
 */
public class BSTSelfTest {

    @Test(timeout = 500)
    public void testIsEmptyTrue() {
        BST b = new BST();
        assertTrue(b.isEmpty());
    }


    @Test(timeout = 500)
    public void testInsertNonEmpty() {
        BST b = new BST(10);
        b.insert(4);
        assertTrue(b.contains(4));
    }

    @Test(timeout = 500)
    public void testDeleteRoot() {
        BST b = new BST(10);
        b.delete(10);
        assertFalse(b.contains(10));
        assertTrue(b.isEmpty());
    }

    @Test(timeout = 500)
    public void testDeleteNonRoot() {
        BST b = new BST(10);
        b.insert(4);
        b.delete(4);
        assertFalse(b.contains(4));
    }

    @Test(timeout = 500)
    public void testHeightEmpty() {
        BST b = new BST();
        assertEquals(0, b.height());
    }

    @Test(timeout = 500)
    public void testHeightOne() {
        BST b = new BST(10);
        assertEquals(1, b.height());
    }


    @Test(timeout = 500)
    public void testGetLengthEmpty() {
        BST b = new BST();
        assertEquals(0, b.getLength());
    }

    @Test(timeout = 500)
    public void testGetLengthOne() {
        BST b = new BST(10);
        assertEquals(1, b.getLength());
    }

    @Test(timeout = 500)
    public void testGetLengthNonEmpty() {
        BST b = new BST(10);
        b.insert(4);
        b.insert(12);
        b.insert(13);
        assertEquals(4, b.getLength());
    }

    @Test(timeout = 500)
    public void testCountEmpty() {
        BST b = new BST();
        assertEquals(0, b.count(10));
    }


    @Test(timeout = 500)
    public void testCountNonEmpty() {
        BST b = new BST(10);
        b.insert(10);
        b.insert(12);
        b.insert(10);
        b.insert(4);
        b.insert(10);
        assertEquals(4, b.count(10));
    }


}