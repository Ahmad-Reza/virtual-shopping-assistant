package com.example.shoppingassistant.network;

import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;

public class RetrofitClient {
    // add this inside application tag (manifest file) for real device
    // android:networkSecurityConfig="@xml/network_security_config"

    private static final String BASE_URL = "http://10.0.2.2:8000"; // For Emulator

    private static Retrofit retrofit = null;

    public static ApiService getInstance() {
        if (retrofit == null) {
            retrofit = new Retrofit.Builder()
                    .baseUrl(BASE_URL)
                    .addConverterFactory(GsonConverterFactory.create())
                    .build();
        }
        return retrofit.create(ApiService.class);
    }
}
