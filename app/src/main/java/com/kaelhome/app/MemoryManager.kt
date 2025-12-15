package com.kaelhome.app

class MemoryManager {

    private val messages = mutableListOf<Pair<String, String>>()  // (author, message)

    fun addMessage(author: String, message: String) {
        messages.add(Pair(author, message))
    }

    fun getAllMessages(): List<Pair<String, String>> {
        return messages
    }

    fun clearMessages() {
        messages.clear()
    }
}
