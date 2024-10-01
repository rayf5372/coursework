package org.translation;

import org.json.JSONArray;
import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class JSONDemoTest {

    @Test
    public void getKeyOneOfSecond() {
        String jsonData = "[{\"key1\" : \"string1a\", \"key2\":21}, {\"key1\" : \"string1b\", \"key2\":22}]";
        JSONArray jsonArray = new JSONArray(jsonData);
        assertEquals("string1b", JSONDemo.getKeyOneOfSecond(jsonArray));
    }
}