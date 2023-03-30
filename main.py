import json
import os

from colorama import Fore


def clear_terminal():
    # ターミナルをクリアする関数
    os.system("cls" if os.name == "nt" else "clear")


def get_user_choice(choices):
    # ユーザーにjsonファイルの選択肢を表示して、選択された番号を取得する関数
    while True:
        try:
            user_choice = int(input(f"jsonファイルを選択してください (1から{len(choices)}の番号を入力してください): "))
            if user_choice not in range(1, len(choices) + 1):
                raise ValueError()
            break
        except ValueError:
            print("無効な入力です。もう一度入力してください。")
    return user_choice


def get_user_answer():
    # ユーザーに回答を入力してもらい、回答がA/B/C/Dのいずれかになるまでループする関数
    while True:
        user_answer = input("回答を入力してください (A/B/C/D): ").upper()
        if user_answer in ["A", "B", "C", "D"]:
            break
        else:
            print("無効な入力です。A/B/C/Dのいずれかを入力してください。")
    return user_answer


def display_question(question):
    # 問題を表示する関数
    print(f"問題{question['id']}. {question['question']}")
    for choice in question["choices"]:
        for key, value in choice.items():
            print(f"{key}: {value}")


def display_result(question, user_answer):
    # 回答の正誤を判定して、解説を表示する関数
    print()
    if question["answer"] == user_answer:
        print(f"{Fore.GREEN}正解です！{Fore.RESET}")
    else:
        print(f"{Fore.RED}不正解です。{Fore.RESET}")
    print(f"解説: {question['explanation']}\n")


def select_json_file():
    # jsonファイルを選択する関数
    json_files = os.listdir("jsons")
    clear_terminal()
    print("以下からjsonファイルを選択してください:")
    for i, json_file in enumerate(json_files):
        print(f"{i + 1}. {json_file}")
    user_choice = get_user_choice(json_files)
    json_file = json_files[user_choice - 1]
    with open(f"jsons/{json_file}", "r", encoding='utf-8') as f:
        questions = json.load(f)
    return questions


def play_game():
    # ゲームをプレイする関数
    num_correct = 0
    questions = select_json_file()
    for i, question in enumerate(questions):
        if i > 0:
            # 問題と問題の間をわかりやすくするために、ターミナルの幅いっぱいに"-"を表示する
            print("-" * os.get_terminal_size().columns, end="\n\n")
        display_question(question)
        user_answer = get_user_answer()
        display_result(question, user_answer)
        if question["answer"] == user_answer:
            num_correct += 1
    clear_terminal()
    # 正答数と正答率を表示する
    print(f"全{len(questions)}問中、{num_correct}問が正解でした。")
    print(f"正答率は {num_correct / len(questions) * 100:.2f}%です。")


def main():
    while True:
        play_game()
        play_again = input("もう一度模試しますか？ (Y/N)").upper()
        while play_again not in ["Y", "N"]:
            print("無効な入力です。もう一度入力してください。")
        play_again = input("もう一度模擬しますか？ (Y/N)").upper()
        if play_again == "N":
            break
        clear_terminal()
        print("模試を終了します。お疲れ様でした！")


if __name__ == "__main__":
    main()
