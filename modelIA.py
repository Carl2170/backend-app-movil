import json
import numpy as np
import tensorflow as tf
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle
import os

# --- Cargar archivo de intents ---
with open('intents.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# --- Preparar datos ---
sentences = []
labels = []

for intent in data['intents']:
    for pattern in intent['patterns']:
        sentences.append(pattern)
        labels.append(intent['tag'])

# --- Tokenización ---
tokenizer = Tokenizer(oov_token="<OOV>")
tokenizer.fit_on_texts(sentences)
sequences = tokenizer.texts_to_sequences(sentences)
padded = pad_sequences(sequences, padding='post')

# --- Codificación de etiquetas ---
lbl_encoder = LabelEncoder()
labels_encoded = lbl_encoder.fit_transform(labels)

# --- Guardar etiquetas como archivo de texto ---
with open("labels.txt", "w", encoding='utf-8') as f:
    for label in lbl_encoder.classes_:
        f.write(label + "\n")

# --- Crear modelo ---
model = tf.keras.Sequential([
    tf.keras.layers.Embedding(input_dim=1000, output_dim=16, input_length=padded.shape[1]),
    tf.keras.layers.GlobalAveragePooling1D(),
    tf.keras.layers.Dense(16, activation='relu'),
    tf.keras.layers.Dense(len(lbl_encoder.classes_), activation='softmax')  # Más seguro que usar set(labels)
])

model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# --- Entrenar modelo ---
model.fit(padded, np.array(labels_encoded), epochs=500, verbose=0)

# --- Guardar modelo en formatos .keras y SavedModel ---
model.save("modelo_intencion.keras")
model.export("modelo_intencion_dir")  # para conversión a TFLite

# --- Convertir a modelo TFLite ---
converter = tf.lite.TFLiteConverter.from_saved_model("modelo_intencion_dir")
tflite_model = converter.convert()

with open("modelo_intencion.tflite", "wb") as f:
    f.write(tflite_model)

# --- Guardar el tokenizer para uso en inferencia ---
with open('tokenizer.pickle', 'wb') as handle:
    pickle.dump(tokenizer, handle, protocol=pickle.HIGHEST_PROTOCOL)
