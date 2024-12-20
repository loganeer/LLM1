import re
from tokenizer import SimpleTokenizerV1

with open("the-verdict.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()
preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', raw_text)
preprocessed = [item.strip() for item in preprocessed if item.strip()]
all_tokens = sorted(list(set(preprocessed)))
all_tokens.extend(["<|endoftext|>", "<|unk|>"])
vocab = {token:integer for integer, token in enumerate(all_tokens)}

for i,item in enumerate(vocab.items()):
    print(item)
    if i>=50:
        break

tokenizer = SimpleTokenizerV1(vocab)
text = "Hello, do you like tea?"
ids = tokenizer.encode(text)
print(ids)
print(tokenizer.decode(ids))