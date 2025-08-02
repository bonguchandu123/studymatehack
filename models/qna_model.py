from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

class QAModel:
    def __init__(self, model_name="facebook/bart-base"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

    def answer_question(self, context, question):
        prompt = f"answer the question based on context:\n{context}\n\nQuestion: {question}"

        inputs = self.tokenizer(
            prompt,
            return_tensors="pt",
            truncation=True,
            max_length=1024,  
            padding="max_length"
        )

        outputs = self.model.generate(**inputs, max_new_tokens=150)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)
