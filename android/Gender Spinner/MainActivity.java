package com.example.spinnereg;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.Spinner;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    private Spinner genderSpinner;
    private Button submitButton;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        genderSpinner = findViewById(R.id.genderSpinner);
        submitButton = findViewById(R.id.submitButton);

        // Spinner setup
        String[] genderOptions = {"Male", "Female"};
        ArrayAdapter<String> adapter = new ArrayAdapter<>(this, android.R.layout.simple_spinner_dropdown_item, genderOptions);
        genderSpinner.setAdapter(adapter);

        // Button click listener
        submitButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String selectedGender = genderOptions[genderSpinner.getSelectedItemPosition()];
                // Start ResultActivity and pass the selected gender
                Intent intent = new Intent(MainActivity.this, ResultActivity.class);
                intent.putExtra("SELECTED_GENDER", selectedGender);
                startActivity(intent);
            }
        });
    }
}
