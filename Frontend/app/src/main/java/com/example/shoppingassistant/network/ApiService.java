package com.example.shoppingassistant.network;

import com.example.shoppingassistant.model.AssistantResponse;
import com.example.shoppingassistant.model.UserQuery;

import retrofit2.Call;
import retrofit2.http.Body;
import retrofit2.http.POST;

public interface ApiService {

    @POST("/assistant/")
    Call<AssistantResponse> askAssistant(@Body UserQuery query);
}

