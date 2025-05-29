import json
from openai import OpenAI

client = OpenAI(api_key="")

def save_embeddings_dict(embedding_dict, filename="embeddings.json"):
  with open(filename, 'w') as f:
    json.dump(embedding_dict, f)

def get_embedding(text, model="text-embedding-3-small"):
  text = text.replace("\n", " ")
  embedding =  client.embeddings.create(input=text, model=model).data[0].embedding
  return embedding


positive_sentences = [
    "I am feeling fantastic today.", 
    "Life is beautiful when you're surrounded by love.", 
    "That was the best surprise I've had in years.", 
    "I'm truly grateful for my friends.", 
    "The weather is perfect, and so is my mood.", 
    "I crushed my goals this week!", 
    "I can't stop smiling — this is amazing.", 
    "That compliment made my day.",
    "I'm in such a good headspace lately.", 
    "Everything feels like it's falling into place.",
    "This vacation is everything I needed.",
    "I feel inspired and energized.",
    "That movie filled me with hope.",
    "I just got great news — I got the job!",
    "I'm proud of what I've accomplished.",
    "She laughed, and it was contagious joy.",
    "I've never been this happy.",
    "Things are finally turning around.",
    "Today feels like a fresh start.",
    "I feel deeply at peace right now.",
    "He hugged me, and everything felt okay.",
    "This cake is divine.",
    "I'm bursting with excitement!",
    "Just got promoted — I'm thrilled!",
    "I love the way life surprises me sometimes." 
]


negative_sentences = [
    "I'm feeling really down today.",
    "Nothing seems to go my way anymore.",
    "I just feel empty inside.",
    "That was the worst experience of my life.",
    "I'm overwhelmed and exhausted.",
    "I feel like a failure.",
    "I don't know how much more I can take.",
    "I'm losing hope.",
    "Every day feels harder than the last.",
    "I wish I could disappear for a while.",
    "That comment really hurt.",
    "I hate how I feel right now.",
    "I'm completely heartbroken.",
    "This isn't how I thought life would go.",
    "I cried myself to sleep last night.",
    "I feel stuck and powerless.",
    "It's all just too much sometimes.",
    "I failed again.",
    "Everything is falling apart.",
    "I feel like giving up.",
    "I'm so frustrated I could scream.",
    "I regret ever trying.",
    "No one understands what I'm going through.",
    "I can't shake this sadness.",
    "That news hit me like a truck."
]

neutral_sentences = [
    "I feel okay.",
    "I'm not sure how I feel.",
    "It was just an ordinary day.",
    "I'm in a weird mood.",
    "Things are fine, I guess.",
    "I feel nothing in particular.",
    "It's been a quiet afternoon.",
    "I'm somewhere in the middle.",
    "I feel a bit off, but not bad.",
    "Nothing really happened today.",
    "I feel neutral about the situation.",
    "I guess I'm alright.",
    "The day went by uneventfully.",
    "I feel kind of numb.",
    "I'm just existing right now."
]

all_positive_embeddings = {}
all_negative_embeddings = {}
all_neutral_embeddings = {}
all_embeddings = {}

for i in range(0, 25):
  all_positive_embeddings[positive_sentences[i]] = get_embedding(positive_sentences[i])
  all_negative_embeddings[negative_sentences[i]] = get_embedding(negative_sentences[i])

for i in range(0, 15):
  all_neutral_embeddings[neutral_sentences[i]] = get_embedding(neutral_sentences[i])

all_embeddings = {
    "positive": all_positive_embeddings,
    "negative": all_negative_embeddings,
    "neutral": all_neutral_embeddings
}

save_embeddings_dict(all_embeddings, filename="/Users/vatsaljalan/Desktop/Uni/final/Math 118/embeddings.json")

