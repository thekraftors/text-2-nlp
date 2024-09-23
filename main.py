from transformers import BertTokenizer, BertModel

# Load the tokenizer and model from Hugging Face
tokenizer = BertTokenizer.from_pretrained('thekraftors/kraft-nlp')
model = BertModel.from_pretrained("thekraftors/kraft-nlp")

# Your input text
text = "Can you tell me about Python?"

# Tokenize the input and explicitly set 'clean_up_tokenization_spaces' to avoid the warning
encoded_input = tokenizer(text, return_tensors='pt', clean_up_tokenization_spaces=True)

# Pass the tokenized input to the model
output = model(**encoded_input)

# Optionally, process the output further if needed
print(output)


