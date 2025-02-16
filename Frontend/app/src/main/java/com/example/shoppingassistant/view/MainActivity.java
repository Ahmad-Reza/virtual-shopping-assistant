package com.example.shoppingassistant.view;

import android.os.Bundle;
import android.util.Log;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

import com.example.shoppingassistant.R;
import com.example.shoppingassistant.model.AssistantResponse;
import com.example.shoppingassistant.model.ProductSearchModel;
import com.example.shoppingassistant.model.UserQuery;
import com.example.shoppingassistant.network.ApiService;
import com.example.shoppingassistant.network.RetrofitClient;

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
//            searchProducts(query);
            askShoppingAssistant(query);
        });
    }

    private void askShoppingAssistant(String userInput) {
        UserQuery userQuery = new UserQuery(userInput);

        ApiService apiService = RetrofitClient.getInstance();
        Call<AssistantResponse> call = apiService.askAssistant(userQuery);
        call.enqueue(new Callback<AssistantResponse>() {
            @Override
            public void onResponse(Call<AssistantResponse> call, Response<AssistantResponse> response) {
                if (response.isSuccessful() && response.body() != null) {
                    String assistantReply = response.body().getResponse();
                    Toast.makeText(MainActivity.this, assistantReply, Toast.LENGTH_LONG).show();
                } else {
                    Toast.makeText(MainActivity.this, "Error: " + response.message(), Toast.LENGTH_SHORT).show();
                }
            }

            @Override
            public void onFailure(Call<AssistantResponse> call, Throwable t) {
                Toast.makeText(MainActivity.this, "API Error: " + t.getMessage(), Toast.LENGTH_SHORT).show();
            }
        });
    }


    private void searchProducts(String query) {
        ApiService apiService = RetrofitClient.getInstance();

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


