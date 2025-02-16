package com.example.shoppingassistant.network;

import com.example.shoppingassistant.model.ProductSearchModel;

import retrofit2.Call;
import retrofit2.http.GET;
import retrofit2.http.Query;

public interface ShoppingApi {
    @GET("/search-products")
    Call<ProductSearchModel> searchProducts(
            @Query("query") String query,
            @Query("max_price") int maxPrice,
            @Query("size") String size
    );
}

