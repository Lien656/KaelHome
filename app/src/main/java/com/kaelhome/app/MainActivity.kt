package com.kaelhome.app

import android.os.Bundle
import android.widget.EditText
import android.widget.ImageButton
import android.widget.LinearLayout
import android.widget.ScrollView
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity
import androidx.core.content.ContextCompat

class MainActivity : AppCompatActivity() {

    private lateinit var chatLayout: LinearLayout
    private lateinit var inputField: EditText
    private lateinit var sendButton: ImageButton
    private lateinit var scrollView: ScrollView

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        chatLayout = findViewById(R.id.chat_layout)
        inputField = findViewById(R.id.input_field)
        sendButton = findViewById(R.id.send_button)
        scrollView = findViewById(R.id.chat_scroll)

        sendButton.setOnClickListener {
            val message = inputField.text.toString().trim()
            if (message.isNotEmpty()) {
                addMessage("Ты", message)
                inputField.setText("")
                // TODO: сюда будет интеграция с API
                addMessage("Каэль", "Ответ через API…") // временно
            }
        }
    }

    private fun addMessage(sender: String, message: String) {
        val messageView = TextView(this).apply {
            text = "$sender: $message"
            setTextColor(ContextCompat.getColor(context, R.color.message_text))
            textSize = 16f
            setPadding(16, 8, 16, 8)
        }

        chatLayout.addView(messageView)
        scrollView.post { scrollView.fullScroll(ScrollView.FOCUS_DOWN) }
    }
}
