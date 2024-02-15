from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig

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

def generate_text(model, tokenizer):
    text_generator = pipeline("text-generation", model=model, tokenizer=tokenizer)

    
    texts = ["여기에 생성할 텍스트 샘플 입력"]
    for text in texts:
        result = text_generator(text, max_length=50, do_sample=True)
        print("Generated Text:", result[0]['generated_text'])

if __name__ == "__main__":
    model_id = None
    model, tokenizer = load_quantized_model_and_tokenizer(model_id)  # 모델과 토크나이저 로드
    generate_text(model, tokenizer)
