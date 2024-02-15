import pandas as pd
import json

def preprocess_data(file_path):
    data = pd.read_csv(file_path, encoding='utf-8')
    df_train = data.drop(columns = 'Unnamed: 0').drop(0)
    df_train['내용'] = df_train['내용'].str.strip()

    json_data = []
    for index, row in df_train.iterrows():
        item = {
            "input": row["주제"] + " " + row["제목"],
            "output": row["내용"],
            "instruction": "You are an artificial intelligence blog author. A user gives you a topic, and your goal is to write a blog post based on the given topic. Write a blog of 500 words or more, considering different thoughts and different ways of thinking while writing the blog."
        }
        json_data.append(item)

    with open("blog_data.json", "w", encoding="utf-8") as outfile:
        json.dump(json_data, outfile, indent=4, ensure_ascii=False)

    print("데이터 로드 및 전처리 완료")

if __name__ == "__main__":
    file_path = None  # 여기에 실제 CSV 파일 경로 지정
    preprocess_data(file_path)
