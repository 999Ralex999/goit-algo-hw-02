from collections import deque

def is_palindrome(text):
    """
    Проверка, является ли введённый текст палиндромом.
    Учитываются только буквы и цифры, игнорируются пробелы, регистр и знаки пунктуации.
    """
    clean_text = ''.join(char.lower() for char in text if char.isalnum())
    char_queue = deque(clean_text)

    while len(char_queue) > 1:
        if char_queue.popleft() != char_queue.pop():
            return False
    return True

def main():
    print("🔁 Перевірка на паліндром")
    print("Введіть текст для перевірки (або 'exit' для виходу)")

    try:
        while True:
            user_input = input("\n📝 Введіть текст: ").strip()

            if user_input.lower() == 'exit':
                print("👋 Програма завершена.")
                break

            result = is_palindrome(user_input)
            if result:
                print(f"✅ '{user_input}' — це паліндром!")
            else:
                print(f"❌ '{user_input}' — не паліндром.")
    except KeyboardInterrupt:
        print("\n👋 Програма завершена через KeyboardInterrupt")

if __name__ == "__main__":
    main()
