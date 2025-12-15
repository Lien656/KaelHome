package com.kaelhome.app

import android.os.Bundle
import android.widget.ImageButton
import android.widget.EditText
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView
import com.kaelhome.app.adapter.ChatAdapter
import com.kaelhome.app.model.Message
import com.kaelhome.app.utils.ApiClient
import com.kaelhome.app.utils.MemoryManager

class MainActivity : AppCompatActivity() {
    private lateinit var chatAdapter: ChatAdapter
    private lateinit var messageInput: EditText
    private lateinit var sendButton: ImageButton
    private lateinit var chatRecyclerView: RecyclerView

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        messageInput = findViewById(R.id.message_input)
        sendButton = findViewById(R.id.send_button)
        chatRecyclerView = findViewById(R.id.chat_recycler_view)

        chatAdapter = ChatAdapter()
        chatRecyclerView.layoutManager = LinearLayoutManager(this)
        chatRecyclerView.adapter = chatAdapter

        sendButton.setOnClickListener {
            val messageText = messageInput.text.toString().trim()
            if (messageText.isNotEmpty()) {
                sendMessage(messageText)
                messageInput.text.clear()
            }
        }
    }

    private fun sendMessage(userMessage: String) {
        chatAdapter.addMessage(Message(userMessage, isUser = true))

        // Асинхронный вызов API
        ApiClient.sendMessage(userMessage) { response ->
            runOnUiThread {
                chatAdapter.addMessage(Message(response, isUser = false))
                MemoryManager.saveMessage(this, userMessage, response)
            }
        }
    }
}
