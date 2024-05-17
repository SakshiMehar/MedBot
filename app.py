from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_message = request.form['message']
    response = generate_response(user_message)
    return jsonify({'response': response})

def generate_response(user_message):
    user_message = user_message.lower()

    if 'hello' in user_message:
        return 'Hello! How can I help you with your healthcare needs today?'
    elif 'symptom' in user_message:
        return 'Please describe your symptoms in detail.'
    elif 'fever' in user_message:
        return 'If you have a fever, it is important to stay hydrated and rest. If your fever persists or is very high, please seek medical attention.'
    elif 'headache' in user_message:
        return 'For a headache, make sure to rest in a quiet, dark room. Stay hydrated and consider taking over-the-counter pain relievers. If your headache is severe or persistent, consult a healthcare professional.'
    elif 'cold' in user_message:
        return 'For a common cold, rest and stay hydrated. Over-the-counter medications can help relieve symptoms. If you have trouble breathing or symptoms worsen, see a doctor.'
    elif 'stomach pain' in user_message:
        return 'Stomach pain can have many causes. Rest, drink fluids, and avoid solid food for a few hours. If pain is severe or persists, contact a healthcare provider.'
    elif 'cough' in user_message:
        return 'For a cough, stay hydrated and try using a humidifier. Over-the-counter cough medicines may help. If the cough persists or is accompanied by other symptoms, see a doctor.'
    elif 'sore throat' in user_message:
        return 'A sore throat can be soothed by drinking warm liquids and using throat lozenges. If the pain is severe or lasts more than a few days, consult a healthcare provider.'
    elif 'nausea' in user_message:
        return 'For nausea, try eating small, bland meals and drinking clear or ice-cold drinks. Avoid strong odors and fried or greasy foods. If nausea persists, seek medical advice.'
    elif 'vomiting' in user_message:
        return 'If you are vomiting, stay hydrated by taking small sips of water or an oral rehydration solution. Avoid solid foods until vomiting stops. If vomiting persists, contact a healthcare provider.'
    elif 'diarrhea' in user_message:
        return 'For diarrhea, stay hydrated and avoid dairy, fatty foods, and high-fiber foods. Consider over-the-counter anti-diarrheal medications. If diarrhea persists, see a doctor.'
    elif 'fatigue' in user_message:
        return 'Fatigue can be caused by many factors. Ensure you are getting enough rest, eating a balanced diet, and staying hydrated. If fatigue is severe or ongoing, consult a healthcare provider.'
    elif 'dizziness' in user_message:
        return 'For dizziness, sit or lie down until it passes. Drink water and avoid sudden movements. If dizziness is frequent or severe, seek medical advice.'
    elif 'rash' in user_message:
        return 'For a rash, try to identify and avoid any potential irritants. Keep the area clean and dry. If the rash is severe or persists, consult a healthcare professional.'
    elif 'back pain' in user_message:
        return 'For back pain, rest and avoid heavy lifting. Apply ice or heat and consider over-the-counter pain relievers. If pain persists, see a healthcare provider.'
    elif 'chest pain' in user_message:
        return 'Chest pain can be serious. If you experience chest pain, seek medical attention immediately.'
    elif 'shortness of breath' in user_message:
        return 'Shortness of breath can be a sign of a serious condition. Seek medical attention immediately if you experience this symptom.'
    elif 'allergies' in user_message:
        return 'For allergies, try to avoid known allergens. Over-the-counter antihistamines can help relieve symptoms. If allergies are severe, consult a healthcare provider.'
    elif 'asthma' in user_message:
        return 'For asthma, use your prescribed inhaler and avoid triggers. If you have a severe asthma attack, seek emergency medical attention.'
    elif 'depression' in user_message:
        return 'If you are feeling depressed, it is important to talk to someone you trust or a healthcare provider. Therapy and medications can be very helpful.'
    elif 'anxiety' in user_message:
        return 'For anxiety, try deep breathing exercises and relaxation techniques. If anxiety is affecting your daily life, consult a healthcare provider for advice and treatment options.'
    elif 'insomnia' in user_message:
        return 'For insomnia, establish a regular sleep routine, avoid caffeine before bed, and create a comfortable sleep environment. If insomnia persists, seek medical advice.'
    elif 'ear pain' in user_message:
        return 'For ear pain, try using a warm compress and over-the-counter pain relievers. If the pain is severe or persists, see a healthcare provider.'
    elif 'eye irritation' in user_message:
        return 'For eye irritation, rinse your eye with clean water and avoid rubbing it. If irritation persists or you have vision problems, seek medical attention.'
    elif 'constipation' in user_message:
        return 'For constipation, increase your fiber intake, drink plenty of water, and exercise regularly. Over-the-counter laxatives may help. If constipation persists, see a healthcare provider.'
    elif 'heartburn' in user_message:
        return 'For heartburn, avoid spicy and fatty foods, eat smaller meals, and avoid lying down after eating. Over-the-counter antacids can provide relief.'
    elif 'joint pain' in user_message:
        return 'For joint pain, rest the affected joint, apply ice, and take over-the-counter pain relievers. If pain persists or is severe, consult a healthcare provider.'
    elif 'skin infection' in user_message:
        return 'For a skin infection, keep the area clean and dry, and consider using an over-the-counter antibiotic ointment. If the infection worsens or does not improve, seek medical attention.'
    elif 'urinary tract infection' in user_message:
        return 'For a urinary tract infection (UTI), drink plenty of water and see a healthcare provider for antibiotics. Untreated UTIs can lead to more serious complications.'
    elif 'high blood pressure' in user_message:
        return 'For high blood pressure, maintain a healthy diet, exercise regularly, and avoid excessive salt intake. Medications prescribed by your doctor can also help manage blood pressure.'
    elif 'diabetes' in user_message:
        return 'For diabetes, monitor your blood sugar levels regularly, follow a balanced diet, exercise, and take any prescribed medications. Regular check-ups with your healthcare provider are important.'
    else:
        return 'I am sorry, I do not understand. Can you please elaborate?'

if __name__ == '__main__':
    app.run(debug=True)
