import statistics
import time

from pynput import keyboard

DEVIATION_THRESHOLD = 0.1


def capture_keystroke_intervals(prompt: str) -> list[float]:
    print(prompt)

    timestamps: list[float] = []
    done = False

    def on_press(key):
        nonlocal done
        timestamps.append(time.time())
        if key == keyboard.Key.enter:
            done = True
            return False

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

    if len(timestamps) < 3:
        return []

    intervals = [
        timestamps[i + 1] - timestamps[i]
        for i in range(len(timestamps) - 2) 
    ]
    return intervals


def average_deviation(sample_a: list[float], sample_b: list[float]) -> float:
    length = min(len(sample_a), len(sample_b))
    if length == 0:
        return float("inf")

    deviations = [abs(sample_a[i] - sample_b[i]) for i in range(length)]
    return statistics.mean(deviations)


def main() -> None:
    print("=== Поведенческий анализ набора текста ===\n")

    first_intervals = capture_keystroke_intervals(
        "Введите любую строку и нажмите Enter (первый раз):"
    )
    if not first_intervals:
        print("Строка слишком короткая для анализа. Попробуйте ввести больше символов.")
        return

    second_intervals = capture_keystroke_intervals(
        "\nВведите ту же строку ещё раз и нажмите Enter (второй раз):"
    )
    if not second_intervals:
        print("Строка слишком короткая для анализа. Попробуйте ввести больше символов.")
        return

    deviation = average_deviation(first_intervals, second_intervals)
    print(f"\nСреднее отклонение между вводами: {deviation:.4f} сек.")

    if deviation > DEVIATION_THRESHOLD:
        print("Обнаружены отклонения в поведении. Возможно, вводил другой человек")
    else:
        print("Ввод соответствует исходному пользователю")


if __name__ == "__main__":
    main()