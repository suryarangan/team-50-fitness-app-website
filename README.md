# 🏋️‍♂️ AI-Powered Fitness App

This is a web-based **AI-powered fitness app** that generates **personalized workout plans** and **motivational quotes** using the IVIS Labs API. Users can **select their workout type** and **difficulty level** (Beginner/Expert) from dropdowns, and the AI will provide a suitable workout plan. Additionally, users can get **motivational quotes** to stay inspired.

---

## 🚀 Features
👉 **AI-Generated Workouts** - Get personalized workout descriptions based on the selected type and difficulty.  
👉 **Motivational Quotes** - Get AI-powered motivation with just one click.  
👉 **Dynamic UI** - The response box appears only when needed and shows "Please wait..." until AI responds.  
👉 **Smooth User Experience** - Built using **HTML, CSS, JavaScript (Frontend)** and **Flask (Backend)**.  

---

## 📂 Project Structure

```
fitness-app/
│── static/
│   │── styles.css         # CSS file for styling
│   │── script.js          # JavaScript for frontend logic
│   │── IVIS_logo.png      # IVIS logo image
│   │── NIE_University.png # University logo image
│   │── PULSE_LOGO.png     # Pulse logo image
│
│── templates/
│   │── index.html         # Main UI for the web app
│
│── app.py                 # Flask backend to handle API calls
│── requirements.txt        # Python dependencies
│── README.md               # Project documentation
```

---

## 🛠️ Setup Instructions

### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/suryarangan/team-50-fitness-app-website.git
cd fitness-app
```

### **2️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

### **3️⃣ Set Your IVIS Labs API Key**
Edit `app.py` and replace `"your-api-key-here"` with your actual API key:
```python
API_KEY = "sk-6ecd2f574bf8434280f86547f1597ef1"
AI_API_URL = "https://chat.ivislabs.in/api/chat/completions"
MODEL_NAME = "gwen2.5:0.5b"
```

### **4️⃣ Run the Flask Server**
```sh
python app.py
```

### **5️⃣ Open in Browser**
Go to:
```
http://127.0.0.1:5000
```

---

## 📌 How It Works

1️⃣ **Select a workout type** (e.g., Strength, Cardio, Yoga)  
2️⃣ **Select difficulty level** (Beginner/Expert)   (Give it as a sentence in the prompt space)  
3️⃣ **Click "Get Workout Description"** - AI will generate a response  
4️⃣ **Click "Get Motivational Quote"** for an inspiring quote  
5️⃣ **The response box is hidden until clicked and shows "Please wait..." while AI responds**  

---

## 🛠️ Technologies Used

- **Frontend**: HTML, CSS, JavaScript  
- **Backend**: Python (Flask)  
- **AI Integration**: IVIS Labs API (`qwen2.5:0.5b` model)  
- **Hosting**: (You can deploy on AWS, Render, or Heroku)  

---

## 🏆 Future Enhancements

- ✅ Save user preferences  
- ✅ Add user authentication  
- ✅ Include exercise images or videos  

---

## 🤝 Contributing
Feel free to fork the repo, raise issues, or submit pull requests.  

---

## 📝 License
This project is **open-source**. You are free to modify and use it.  



