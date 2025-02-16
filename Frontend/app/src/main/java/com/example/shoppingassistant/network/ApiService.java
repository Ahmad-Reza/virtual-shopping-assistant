package com.example.shoppingassistant.network;

import com.example.shoppingassistant.model.AssistantResponse;
import com.example.shoppingassistant.model.ProductSearchModel;
import com.example.shoppingassistant.model.UserQuery;

import retrofit2.Call;
import retrofit2.http.Body;
import retrofit2.http.GET;
import retrofit2.http.POST;
import retrofit2.http.Query;

public interface ApiService {
    @GET("/search-products")
    Call<ProductSearchModel> searchProducts(
            @Query("query") String query,
            @Query("max_price") int maxPrice,
            @Query("size") String size
    );

    @POST("/assistant/")
    Call<AssistantResponse> askAssistant(@Body UserQuery query);
}

