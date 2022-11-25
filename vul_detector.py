import tensorflow as tf
from gensim.models import Doc2Vec
from tensorflow import keras
from preprocess import process_corpus
import warnings

warnings.filterwarnings("ignore")

# Process input file
print("Begin")
test_func = list(process_corpus("one_function.c", tokens_only=True))
print("Function processed")
line_list = []

# Load Models
print("Loading models")
nlp_model = Doc2Vec.load('line_vec_model')
class_model = keras.models.load_model('classifier_model')
print("Models loaded")

# Use models to convert lines of input file to vectors and classify
for j in range(len(test_func)):
    inferred_vector = nlp_model.infer_vector(test_func[j])
    result = class_model.predict(tf.reshape(inferred_vector, shape=(1, 50)))
    print(result)
    line_list.append(result)

vul_line = line_list.index(max(line_list))
print("The most vulnerable line is predicted to be", vul_line, "out of", len(line_list))
