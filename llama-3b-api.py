from fastapi import FastAPI
from pydantic import BaseModel
from transformers import AutoTokenizer, pipeline, LlamaForCausalLM

app = FastAPI()

# Specify the local model path for the LLaMA model
model_path = './llama_3_2_3bi'  # Ensure this path points to your saved model
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = LlamaForCausalLM.from_pretrained(model_path)

# Create a text generation pipeline with proper settings
pipe = pipeline("text-generation", model=model, tokenizer=tokenizer, 
                pad_token_id=tokenizer.eos_token_id,  # Set pad_token_id to eos_token_id
                do_sample=True)  # Enable sampling

class TextGenerationRequest(BaseModel):
    prompt: str
    max_new_tokens: int = 50
    temperature: float = 0.9  # Set to desired value

@app.post("/generate/")
async def generate_text(request: TextGenerationRequest):
    # Generate the output based on the prompt
    outputs = pipe(request.prompt, max_new_tokens=request.max_new_tokens, temperature=request.temperature)
    
    # Extract the generated text
    generated_text = outputs[0]['generated_text']
    print(f"Generated text: {generated_text}")
    
    # Find and extract the "Answer" part of the text
    answer_start = generated_text.find("Answer:")
    
    if answer_start != -1:
        # Look for the end of the first answer by checking for the next "Question:" or end of the text
        answer_end = generated_text.find("Question:", answer_start)
        if answer_end == -1:
            answer_end = len(generated_text)  # No more questions, take everything till the end

        answer = generated_text[answer_start + len("Answer:"):answer_end].strip()
    else:
        answer = "Answer not found."

    # Return only the extracted "Answer"
    return {"answer": answer}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
