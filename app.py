
# from flask import Flask
# from modules import (
#     account_nature,
#     chart_of_accounts,
#     accounting_periods,
#     accounting_accounts,
#     journal_entries,
#     journal_details
# )

# app = Flask(__name__)
# app.register_blueprint(account_nature.bp)
# app.register_blueprint(chart_of_accounts.bp)
# app.register_blueprint(accounting_periods.bp)
# app.register_blueprint(accounting_accounts.bp)
# app.register_blueprint(journal_entries.bp)
# app.register_blueprint(journal_details.bp)

# if __name__ == '__main__':
#     app.run(port=5000, debug=True)


from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np
import pickle

app = Flask(__name__)

# Carga modelo TFLite
interpreter = tf.lite.Interpreter(model_path="modelo_intencion.tflite")
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Carga tokenizer
with open('tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

# Lista de etiquetas (debes crear este archivo o ponerlas aquí)
with open('labels.txt', 'r', encoding='utf-8') as f:
    labels = [line.strip() for line in f.readlines()]

def preprocess_text(text):
    sequences = tokenizer.texts_to_sequences([text])
    # Ajusta maxlen según tu modelo, aquí 6 es ejemplo:
    from tensorflow.keras.preprocessing.sequence import pad_sequences
    padded = pad_sequences(sequences, maxlen=6, padding='post')
    return padded.astype(np.float32)

@app.route('/predict_intent', methods=['POST'])
def predict_intent():
    data = request.get_json(force=True)
    text = data.get('text', '')
    if not text:
        return jsonify({'error': 'No se proporcionó texto'}), 400

    input_data = preprocess_text(text)

    interpreter.set_tensor(input_details[0]['index'], input_data)
    interpreter.invoke()
    output_data = interpreter.get_tensor(output_details[0]['index'])

    intent_idx = np.argmax(output_data)
    intent = labels[intent_idx]

    return jsonify({'intent': intent})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
