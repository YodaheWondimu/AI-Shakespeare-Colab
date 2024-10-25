import random
import numpy as np
import tensorflow as tf
from tensorflow import keras # libraries

filepath = tf.keras.utils.get_file("shakespeare.txt", "https://storage.googleapis.com/download.tensorflow.org/data/shakespeare.txt")

text = open(filepath, "rb").read().decode(encoding="utf-8").lower() # more libraries, training data here

text = text[300000:800000]

characters = sorted(set(text))
print(str(len(characters)))

char_to_index = dict((c, i) for i, c in enumerate(characters))
index_to_char = dict((i, c) for i, c in enumerate(characters)) # set off text, sets all of the words off to make sense later

SEQ_LENGTH = 40
STEP_SIZE = 3 # used to organize the sequences and step size into numbers, like a janior-meets-mathematician

# training prep
# sentences = []
# next_characters = []

# for i in range(0, len(text) - SEQ_LENGTH, STEP_SIZE):
#     sentences.append(text[i: i+SEQ_LENGTH])
#     next_characters.append(text[i+SEQ_LENGTH])

# x = np.zeros((len(sentences), SEQ_LENGTH, len(characters)), dtype=np.bool_)
# y = np.zeros((len(sentences), len(characters)), dtype=np.bool_)
# print(str(y.shape))

# for i, sentence in enumerate(sentences):
#     for t, character in enumerate(sentence):
#         x[i, t, char_to_index[character]] = 1
#     y[i, char_to_index[next_characters[i]]] = 1
# training prep

try:
    model = tf.keras.models.load_model("textgenerator.keras")
    print("The model of divine literature hath loaded successfully.")
except Exception as e:
    print(f"Fie! Error loading model: {e}") # loads the model, tells you if there's failure loading

def sample(preds, temperature=1.0):
    preds = np.asarray(preds).astype("float64")
    preds = np.log(preds) / temperature
    exp_preds = np.exp(preds)
    preds = exp_preds / np.sum(exp_preds)
    probas = np.random.multinomial(1, preds, 1)
    return np.argmax(probas) # gets the sample size ready so it can generate each subsequent character

def generate_text(length, temperature):
    start_index = random.randint(0, len(text) - SEQ_LENGTH)
    generated = ''
    sentence = text[start_index:start_index + SEQ_LENGTH]
    generated += sentence
    for i in range(length):
        x = np.zeros((1, SEQ_LENGTH, len(characters)))
        for t, character in enumerate(sentence):
            x[0, t, char_to_index[character]] = 1 
    
        prediction = model.predict(x, verbose=0)[0]
        next_index = sample(prediction, temperature)
        next_character = index_to_char[next_index]

        generated += next_character
        sentence = sentence[1:] + next_character # text generation function, the main event
    return generated # returns the value it found

print(f"Length of text: {len(text)}")
# Generate text
length_of_text_to_generate = int(input("I summon thee to the AI-Shakespearean Colab! Come hither, entereth the desired text length: "))  # asks you for the desired length of text in character count
temperature_value = float(input("Yes, yes. Now, wither do you desireth the risk factor to be from 1 to 10? Entereth here: "))  # asks you for the desired temperature ("risk factor") from 1 to 10 (divided by 10 later so it can convert to float without complcated errors))

try:
    print("I shall granteth you what is that you wish! Generating text...")
    generated_text = generate_text(length_of_text_to_generate, float(temperature_value / 10))
    print("Text generation hath completeth.\n<->-<->-<->-<->-<->-<->-<->-<->-<->-")
    print(generated_text)
except Exception as e:
    print(f"Fie! Error during text generation: {e}") # hopefully, at this point, the program has worked. O summer's day, enjoy your poetry!