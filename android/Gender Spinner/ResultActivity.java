package com.example.girlboy;

import android.os.Bundle;
import android.widget.ImageView;

import androidx.appcompat.app.AppCompatActivity;

public class ResultActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_result);

        // Get the selected gender from the intent
        String selectedGender = getIntent().getStringExtra("SELECTED_GENDER");

        // Set the image based on the selected gender
        ImageView genderImageView = findViewById(R.id.genderImageView);
        if ("Male".equals(selectedGender)) {
            genderImageView.setImageResource(R.drawable.male); // Replace with your male image resource
        } else if ("Female".equals(selectedGender)) {
            genderImageView.setImageResource(R.drawable.female); // Replace with your female image resource
        }
    }
}

