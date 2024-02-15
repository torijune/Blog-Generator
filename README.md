# Blog Generation Using LLM fine tuning with QLoRA

## 프로젝트 개요
이 프로젝트는 자연어 처리(NLP) 모델의 양자화, 파인 튜닝 및 텍스트 생성을 다룹니다. 프로젝트는 데이터 크롤링, 데이터 전처리, 모델 양자화, 모델 파인 튜닝, 그리고 텍스트 생성의 전체 워크플로우를 포함합니다.

## 프로젝트 구조
```
.
├── Crawling                
│   ├── __init__.py
│   ├── crawler.py          
│   ├── main.py             
│   ├── readme.md           
│   └── requirements.txt    
├── Data                    
│   ├── blog_crawling_new.csv
│   └── blog_data_new.json
├── Model                   
├── Notebook                
│   ├── KoPlatYi(6B).ipynb
│   ├── KoPlatYi.ipynb
│   └── PolyglotKo(8B).ipynb
├── PDF                     
│   └── 발표자료(230215).pdf
├── README.md               
├── Setup                   
│   ├── __init__.py
│   ├── finetuning.py       
│   ├── generate_text.py    
│   ├── preprocess.py      
│   └── quantization.py    
└── requirements.txt       
```

## 설치 및 실행 가이드
프로젝트를 시작하기 전에 필요한 의존성을 설치해야 합니다. 프로젝트 루트에서 아래 명령어를 실행하여 필요한 패키지를 설치합니다.
```bash
pip install -r requirements.txt
```

### 데이터 크롤링
크롤링 관련 스크립트를 실행하기 전에 `Crawling` 디렉토리로 이동하고, 해당 디렉토리의 `requirements.txt`에 따라 추가 의존성을 설치합니다.
```bash
cd Crawling
pip install -r requirements.txt
python main.py
```

### 데이터 전처리, 모델 양자화, 파인 튜닝 및 텍스트 생성
`Setup` 디렉토리 내의 스크립트를 순차적으로 실행하여 데이터 전처리, 모델 양자화, 파인 튜닝 및 텍스트 생성 과정을 수행할 수 있습니다. 전체 프로세스를 자동으로 실행하는 쉘 스크립트를 제공합니다.

```bash
./run_all.sh
```

### 주의 사항
- 모델 학습 및 텍스트 생성을 위한 주피터 노트

북은 `Notebook` 디렉토리에 있습니다. 주피터 노트북 환경에서 각 노트북 파일을 열어 실행할 수 있습니다.
- 양자화 및 파인 튜닝된 모델은 `Model` 디렉토리에 저장됩니다.
```

### `run_all.sh`

```bash
#!/bin/bash

# 데이터 크롤링
echo "데이터 크롤링 시작..."
cd Crawling
python main.py
cd ..

# 데이터 전처리
echo "데이터 전처리 시작..."
cd Setup
python preprocess.py

# 모델 양자화
echo "모델 양자화 시작..."
python quantization.py

# 모델 파인 튜닝
echo "모델 파인 튜닝 시작..."
python finetuning.py

# 텍스트 생성
echo "텍스트 생성 시작..."
python generate_text.py

echo "모든 작업이 완료되었습니다."
```