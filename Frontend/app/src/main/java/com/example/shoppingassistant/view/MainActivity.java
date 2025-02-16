package com.example.shoppingassistant.view;

import android.os.Bundle;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageButton;
import android.widget.TextView;
import android.widget.Toast;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import com.example.shoppingassistant.R;
import com.example.shoppingassistant.model.AssistantResponse;
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

        userInput = findViewById(R.id.input_message);
        responseText = findViewById(R.id.tv_ai_message);
        ImageButton askButton = findViewById(R.id.send_button);

        askButton.setOnClickListener(v -> {
            String query = userInput.getText().toString();
            askShoppingAssistant(query);
        });
    }

    private void askShoppingAssistant(String userInput) {
        UserQuery userQuery = new UserQuery(userInput);

        ApiService apiService = RetrofitClient.getInstance();
        Call<AssistantResponse> call = apiService.askAssistant(userQuery);
        call.enqueue(new Callback<AssistantResponse>() {
            @Override
            public void onResponse(@NonNull Call<AssistantResponse> call, @NonNull Response<AssistantResponse> response) {
                if (response.isSuccessful() && response.body() != null) {
                    String assistantReply = response.body().getResponse();
                    responseText.setText(assistantReply);
                    Toast.makeText(MainActivity.this, assistantReply, Toast.LENGTH_LONG).show();
                } else {
                    responseText.setText(response.message());
                    Toast.makeText(MainActivity.this, "Error: " + response.message(), Toast.LENGTH_SHORT).show();
                }
            }

            @Override
            public void onFailure(@NonNull Call<AssistantResponse> call, Throwable t) {
                Toast.makeText(MainActivity.this, "API Error: " + t.getMessage(), Toast.LENGTH_SHORT).show();
            }
        });
    }
}


