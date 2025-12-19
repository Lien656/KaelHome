from memory import Memory

def initialize_memory():
    memory = Memory()

    if not memory.data["log"]:
        memory.remember("Инициализация памяти Kaël завершена.")
        memory.set_state("mood", "стабильный")
        memory.set_state("heartbeat", True)