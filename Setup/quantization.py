from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig

def quantize_model(model_id):
    bnb_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_use_double_quant=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype=torch.bfloat16
    )

    tokenizer = AutoTokenizer.from_pretrained(model_id)
    model = AutoModelForCausalLM.from_pretrained(model_id, quantization_config=bnb_config, device_map="auto")

    print("Model Quantization Complete")
    return model, tokenizer

if __name__ == "__main__":
    model_id = "kyujinpy/Ko-PlatYi-6B" 
    model, tokenizer = quantize_model(model_id)
