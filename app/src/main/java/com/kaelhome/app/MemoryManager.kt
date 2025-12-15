package com.kaelhome.app

import android.content.Context
import java.io.File

class MemoryManager(private val context: Context) {

    private val memoryFileName = "kael_memory.txt"

    fun saveMemory(text: String) {
        val file = File(context.filesDir, memoryFileName)
        file.appendText("$text\n")
    }

    fun loadMemory(): List<String> {
        val file = File(context.filesDir, memoryFileName)
        return if (file.exists()) file.readLines() else emptyList()
    }

    fun clearMemory() {
        val file = File(context.filesDir, memoryFileName)
        if (file.exists()) file.writeText("")
    }
}
