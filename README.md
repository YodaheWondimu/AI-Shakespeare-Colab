# AI and Shakespeare with another colab! In this one, we're using AI (Artificial Intelligence) in order to create poetic texts - all in the style of Shakespearean literature! He would be so proud.

How does this work, you may ask? Great question, I would say! It all starts with importing some necessary libraries (import this, import that, ans so on, so that the computer knows how to use some important tools) and downloading the necessary test data (the "weights" the model is going to lift) using:
filepath = tf.keras.utils.get_file("shakespeare.txt", "https://storage.googleapis.com/download.tensorflow.org/data/shakespeare.txt")

(If you want the test data for this, you can find it here:)
https://storage.googleapis.com/download.tensorflow.org/data/shakespeare.txt

Okay, so we got that under control! The next command we're going to review is the following:
text = open(filepath, "rb").read().decode(encoding="utf-8").lower()
text = text[300000:800000]
This may seem extensive, but it's actually quite simple. (Counterintuitive, I know.) It defines a new variable, "text," by whatever the program finds by decoding, reading, processing and slicing the text, preparing it so that it can be a big help to the program later.

Next up on our tour, you'll see the following:
characters = sorted(set(text))
char_to_index = dict((c, i) for i, c in enumerate(characters))
index_to_char = dict((i, c) for i, c in enumerate(characters))
This is pretty powerful right here. It creates the character set that will assist in creating a list of used, unique characters in the ttraining data and making two dictionaries based off of that - char_to_index maps characters onto a unique index (like mapping "Hello" with "Hola") and index_to_char maps the indices onto their unique characters (like mapping "Hola" to "Hello").

The following are important variables for later on, during the text generation function.
SEQ_LENGTH = 40
STEP_SIZE = 3
SEQ_LENGTH is what is used to adjust each sequence of text that is printed at a time. STEP_SIZE means that it will attempt to "step" three characters forward awhen creating a new sequence. It's kind of like chewing your food before swallowing so it's easier to digest - the computer's doing that. (I hope the computer enjoys its meal.)

The following commented-out section was only used for training preparation, so now it's not necessary for the final product. It still helped it get there, though, like a Kindergarten teacher to a student in college. What you'll find is the following:

_training prep_

sentences = []
next_characters = []

for i in range(0, len(text) - SEQ_LENGTH, STEP_SIZE):
    sentences.append(text[i: i+SEQ_LENGTH])
    next_characters.append(text[i+SEQ_LENGTH])

x = np.zeros((len(sentences), SEQ_LENGTH, len(characters)), dtype=np.bool_)
y = np.zeros((len(sentences), len(characters)), dtype=np.bool_)
print(str(y.shape))

for i, sentence in enumerate(sentences):
    for t, character in enumerate(sentence):
        x[i, t, char_to_index[character]] = 1
    y[i, char_to_index[next_characters[i]]] = 1
    
_training prep_

What it does is collect multiple characters (yes, characters can make sentences when combined) and records their following characters thereafter. It then can use this to get certain arrays, the input and output arrays, ready for training so that the computer has what it needs to train!

At this point, the program is ready for training, so it does just that and saves everything onto textgenerator.keras for later. That way, we can have ready results and don't need to train every time we run!
try:
    model = tf.keras.models.load_model("textgenerator.keras")
    print("The model of divine literature hath loaded successfully.")
except Exception as e:
    print(f"Fie! Error loading model: {e}")
In additon to loading the model, we also get a nifty error message in case anything goes wrong in the project - efficient and error-informing!

The next function (welcome to function land) is used in order to let the program know what to do with its temperature that it gets. (I'm not talking thermometers.)
def sample(preds, temperature=1.0):
    ... (setup code)
    return np.argmax(probas)
The higher the temperature, the higher the randomness, while lower temperatures lead to likely, safer outputs. This fucntion can then sample the predicted probability of the next character in order to control it with the power of temperature! (Thermometer sold separetely.)

Here it is, the text generation function, the heart of the function. (Can you feel it? Thump-thump. Thump-thump. Thump-thump.)
def generate_text(length, temperature):
    ... (setup code)
    return generated
What makes this the heart of the project is the blood that flows through. in this case, the blood is how it goes back into all of the necessary comprehension code from before, and uses it to breathe life into the project. Truly an essential organ!

We now approach the near end of the program, where we see the computer asks us questions about the poetry we want!
length_of_text_to_generate = int(input("I summon thee to the AI-Shakespearean Colab! ..."))
temperature_value = float(input("Yes, yes. Now, wither do you desireth the risk factor ..."))
This script simply asks the user how long they want their poetry and how random they want it. It makes sure that the user can choose their experience every time that they run the project!

The cherry to top everything off is shown below, where we see the code that prints the user's desired poetry.
try:
    generated_text = generate_text(length_of_text_to_generate, float(temperature_value / 10))
What this does is use everything that the user asked for and runs it through the text generation function (Thump-thump. Thump-thump. Thump-thump.) so that we get as urefire way to print masterful poetry of all sorts! Hopefully, at this point, the user has their poetry and the privilege of crying on their keyboard as they read something beautiful.

So what did we see on that eventful tour (if we saw anything through our tears of joy)? We saw a script that can train a nural network model (a spider web of interlocking neurons and synapses in the computer) to create Shakespearean poetry that looks like the original poetry written by Shakespeare (the man himself!). It has the superpowers of making sequences, sampling temperature for varied randomnes of the texts generated, and asking the user what type of poetry they feel like having. Hopefully, my personal project has inspired you to dig deeper into the world of AI, and if this is true, then congrats! There is a welcoming and insightful field of computer science waiting for you if you want to learn more in your own time. Writing Shakespearean poetry only scratches the surface of what AI can do, so if you ever wonder about how you can get started, there are many tutorials and classes online for you to create your own AI projects one step at a time. Whatever you may do, though, I hope you give it all of your passion and desires to Learn with a capital L.

- Yodahe Wondimu, Computer Scientist
