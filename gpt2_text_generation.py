from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")

prompt = input("Enter a prompt: ")

output = generator(
    prompt,
    max_length=100,
    num_return_sequences=1
)

print("\nGenerated Text:\n")
print(output[0]["generated_text"])