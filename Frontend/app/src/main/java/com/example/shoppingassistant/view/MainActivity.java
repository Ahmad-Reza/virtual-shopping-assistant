package com.example.shoppingassistant.view;

import android.os.Bundle;
import android.util.Log;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

import com.example.shoppingassistant.R;
import com.example.shoppingassistant.model.ProductSearchModel;
import com.example.shoppingassistant.network.RetrofitClient;
import com.example.shoppingassistant.network.ShoppingApi;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;

public class MainActivity extends AppCompatActivity {
    private EditText userInput;
    private TextView responseText;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        userInput = findViewById(R.id.user_input);
        responseText = findViewById(R.id.response_text);
        Button askButton = findViewById(R.id.ask_button);

        askButton.setOnClickListener(v -> {
            String query = userInput.getText().toString();
            searchProducts(query);
        });
    }

    private void searchProducts(String query) {
        ShoppingApi apiService = RetrofitClient.getInstance();

        // Fetch products
        apiService.searchProducts("Floral Skirt", 40, "S").enqueue(new Callback<ProductSearchModel>() {
            @Override
            public void onResponse(Call<ProductSearchModel> call, Response<ProductSearchModel> response) {
                if (response.isSuccessful() && response.body() != null) {
                   // for (Product product : response.body()) {
                     //   Log.d("API Response", "Product: " + product.getName() + ", Price: $" + product.getPrice());
                    //}
                }
            }

            @Override
            public void onFailure(Call<ProductSearchModel> call, Throwable t) {
                Log.e("API Error", t.getMessage());
            }
        });
    }
}


