# Python3 エンジニア基礎認定試験 模擬試験アプリ



模擬試験をターミナルで受けられるアプリです。

模擬問題はChatGPT-4で生成したものです。

このアプリも以下のプロンプトを皮切りにほとんどChatGPT-3.5にコードを生成してもらったものです。

```
あなたは優秀なソフトウェアエンジニアです。
Python3 エンジニア基礎認定試験の問題をターミナルで表示、回答できるプログラムを作成してください。

制約条件は以下の通りです。
- 問題はJSONファイルに格納されています。
- JSONファイルは複数あり、それぞれのファイルには複数の問題が格納されています。
- まずはじめに複数あるjsonファイルをユーザーに番号で選択させます。
- 不正な入力があった場合は再度入力を受け付けます。
- ユーザーが選択したjsonファイルの問題のidとquestionを順番に表示し、回答を受け付けます。
- 回答が入力されたら正解を判定し、解説を表示、次の問題へ進みます。
- 前の問題との区切りをわかりやすくするためにターミナルの幅いっぱいに"-"を表示します。
- また、最後に正解数と正答率を表示します。
- 選択肢以外の回答が入力されたら、再度回答を受け付けます。
- 最後の問題まで回答したら終了します。

構造:
jsons/
    question1.json
    question2.json

JSON:
[
    {
        "id":1,
        "question": "問題文",
        "choices": [
            {
                "A": "選択肢A",
                "B": "選択肢B",
                "C": "選択肢C",
                "D": "選択肢D"
            }
        ],
        "answer": "正答",
        "explanation": "解説"
    },
    {
        "id":2,
        "question": "問題文",
        "choices": [
            {
                "A": "選択肢A",
                "B": "選択肢B",
                "C": "選択肢C",
                "D": "選択肢D"
            }
        ],
        "answer": "正答",
        "explanation": "解説"
    },
    # ...
]
```



仮想環境でアプリ実行後、questions_sample.jsonを選択することで簡潔に挙動確認できます。