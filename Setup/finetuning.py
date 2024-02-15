import torch
from transformers import Trainer, TrainingArguments, AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
from datasets import load_dataset

def load_quantized_model_and_tokenizer(model_id):
    bnb_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_use_double_quant=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype=torch.bfloat16
    )
    
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    model = AutoModelForCausalLM.from_pretrained(model_id, quantization_config=bnb_config, device_map="auto")
    
    return model, tokenizer

def fine_tune_model(model, tokenizer, dataset_path):
    dataset = load_dataset("json", data_files=dataset_path)

    print("모델 파인 튜닝 시작")

    training_args = TrainingArguments(
        output_dir='./results', 
        num_train_epochs=3, 
        per_device_train_batch_size=4,
        warmup_steps=500,  
        weight_decay=0.01, 
        logging_dir='./logs', 
        fp16=True, 
    )

    
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=dataset["train"],  
        # eval_dataset=dataset["test"]  # 이 부분은 실제 데이터셋에 맞게 조정이 필요
    )

    trainer.train()

    print("모델 파인 튜닝 완료")

if __name__ == "__main__":
    model_id = "kyujinpy/Ko-PlatYi-6B"  
    dataset_path = None # 여기에 실제 데이터셋 파일 경로 지정
    model, tokenizer = load_quantized_model_and_tokenizer(model_id) 
    fine_tune_model(model, tokenizer, dataset_path)