package com.kaelhome.app

import android.content.Context
import java.io.File

class MemoryManager(private val context: Context) {
    private val memoryFile = File(context.filesDir, "memory_store.txt")

    fun saveMemory(text: String) {
        memoryFile.appendText("$text\n")
    }

    fun readMemory(): List<String> {
        return if (memoryFile.exists()) {
            memoryFile.readLines()
        } else {
            emptyList()
        }
    }

    fun clearMemory() {
        memoryFile.writeText("")
    }
}
