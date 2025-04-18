import queue
import time
import uuid
import random

request_queue = queue.Queue()

REQUEST_TYPES = ["Hardware repair", "Software issue", "Network problem", "Consultation"]

def generate_request():
    """
    Генерация новой заявки и добавление в очередь
    """
    request = {
        "id": str(uuid.uuid4())[:8],
        "type": random.choice(REQUEST_TYPES),
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }
    request_queue.put(request)
    print(f"✅ Заявка создана: ID={request['id']}, Тип={request['type']}, Время={request['timestamp']}")

def process_request():
    """
    Обработка заявки из очереди
    """
    if not request_queue.empty():
        request = request_queue.get()
        print(f"🔄 Обработка заявки ID={request['id']}, Тип={request['type']}, Время создания={request['timestamp']}")
        time.sleep(random.uniform(0.5, 1.5))  
        print(f"✅ Заявка ID={request['id']} успешно обработана\n")
    else:
        print("⚠️ Очередь пуста. Нет заявок для обработки.\n")

def main():
    print("🚀 Система обработки заявок запущена!")
    print("Доступные команды: generate, process, exit\n")

    while True:
        command = input("👉 Введите команду: ").strip().lower()

        if command == "generate":
            generate_request()
        elif command == "process":
            process_request()
        elif command == "exit":
            print("👋 Выход из программы...")
            break
        else:
            print("⚠️ Неизвестная команда. Повторите ввод.\n")

if __name__ == "__main__":
    main()
