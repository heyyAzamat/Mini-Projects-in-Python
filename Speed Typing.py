import time

def typing_speed_test():
    print("Наберите следующую строку текста:")
    text = "В углу магазина продается свежий ароматный хлеб, только что испеченный в пекарне, и свежее молоко из близлежащей фермы"
    print(text)
    input("Начните печатать, когда будете готовы. Нажмите Enter для начала: ")
    start_time = time.time()
    user_input = input("Введите строку здесь: ")
    end_time = time.time()
    time_taken = end_time - start_time
    word_count = len(text.split())
    typed_count = len(user_input.split())
    accuracy = sum(a == b for a, b in zip(text, user_input)) / len(text) * 100
    speed = (typed_count / time_taken) * 60

    print(f"\nВы набрали {typed_count} слов за {time_taken:.2f} секунд")
    print(f"Скорость печати: {speed:.2f} слов в минуту")
    print(f"Точность: {accuracy:.2f}%")

typing_speed_test()
