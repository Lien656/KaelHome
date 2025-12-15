package com.kaelhome.app

import android.content.Context
import java.io.File

object MemoryManager {
    private const val MEMORY_FILE_NAME = "memory_store.json"

    fun readMemory(context: Context): String? {
        val memoryFile = File(context.filesDir, MEMORY_FILE_NAME)
        return if (memoryFile.exists()) {
            memoryFile.readText()
        } else {
            null
        }
    }

    fun writeMemory(context: Context, content: String) {
        val memoryFile = File(context.filesDir, MEMORY_FILE_NAME)
        memoryFile.writeText(content)
    }

    fun deleteMemory(context: Context) {
        val memoryFile = File(context.filesDir, MEMORY_FILE_NAME)
        if (memoryFile.exists()) {
            memoryFile.delete()
        }
    }
}
