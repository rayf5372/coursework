package org.translation;

import java.io.IOException;
import java.io.InputStream;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Iterator;
import java.util.List;
import java.util.Map;

import org.json.JSONArray;
import org.json.JSONObject;

/**
 * An implementation of the Translator interface which reads in the translation
 * data from a JSON file. The data is read in once each time an instance of this class is constructed.
 */
public class JSONTranslator implements Translator {
    private static final String ALPHA3 = "alpha3";

    private final Map<String, Map<String, String>> translationData;

    /**
     * Constructs a JSONTranslator using data from the sample.json resources file.
     */
    public JSONTranslator() {
        this("sample.json");
    }

    /**
     * Constructs a JSONTranslator populated using data from the specified resources file.
     * @param filename the name of the file in resources to load the data from
     * @throws RuntimeException if the resource file can't be loaded properly
     */
    public JSONTranslator(String filename) {
        translationData = new HashMap<>();

        try {
            InputStream inputStream = getClass().getClassLoader().getResourceAsStream(filename);
            if (inputStream == null) {
                throw new IOException("Resource file not found: " + filename);
            }
            String jsonString = new String(inputStream.readAllBytes(), StandardCharsets.UTF_8);

            JSONArray jsonArray = new JSONArray(jsonString);

            for (int i = 0; i < jsonArray.length(); i++) {
                JSONObject countryObj = jsonArray.getJSONObject(i);
                String countryCode = null;
                if (countryObj.has(ALPHA3)) {
                    countryCode = countryObj.getString(ALPHA3).toLowerCase();
                }
                else {
                    continue;
                }
                Map<String, String> languageMap = new HashMap<>();
                Iterator<String> keys = countryObj.keys();
                while (keys.hasNext()) {
                    String key = keys.next();
                    if (!ALPHA3.equals(key) && !"id".equals(key)
                            && !"alpha2".equals(key)) {
                        String translation = countryObj.getString(key);
                        languageMap.put(key.toLowerCase(), translation);
                    }
                }
                translationData.put(countryCode, languageMap);
            }
        }
        catch (IOException ex) {
            throw new RuntimeException(ex);
        }
    }

    @Override
    public List<String> getCountryLanguages(String country) {
        Map<String, String> languageMap =
                translationData.get(country.toLowerCase());
        if (languageMap != null) {
            return new ArrayList<>(languageMap.keySet());
        }
        else {
            return new ArrayList<>();
        }
    }

    @Override
    public List<String> getCountries() {
        return new ArrayList<>(translationData.keySet());
    }

    @Override
    public String translate(String country, String language) {
        Map<String, String> languageMap =
                translationData.get(country.toLowerCase());
        if (languageMap != null) {
            return languageMap.get(language.toLowerCase());
        }
        return null;
    }
}
