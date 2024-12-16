# MissDiagnosis - An AI-Driven Electronic Medical Record System

MissDiagnosis is an AI-integrated **Electronic Medical Record (EMR)** system designed to help doctors avoid potential misdiagnoses by analyzing inputs against recent global health outbreaks and patient history. This project was developed during the **6-hour Notion Hackathon at Grambling State University**, combining the power of AI and Notion integration to build an impactful healthcare solution.

---

## 🏆 **Project Overview**
MissDiagnosis leverages:
- **OpenAI GPT-4** for analyzing diagnoses against current health outbreak trends.
- **Custom CNN model** for malaria detection using blood sample data.
- **Global health outbreak tracking** integrated from WHO Disease Outbreak News.

### 🩺 **Core Functionalities**
1. **Diagnosis Analysis**
   - Doctors input symptoms, medical history, and diagnoses into the EMR.
   - GPT-4o validates the input against recent outbreaks and epidemiology data.
   - It provides tailored feedback and suggests possible tests to refine the diagnosis.

2. **Malaria Prediction**
   - Uses a **custom Convolutional Neural Network (CNN)** to analyze blood sample data.
   - Predicts whether a patient has malaria based on the input image.

3. **Outbreak Monitoring**
   - Scrapes WHO's Disease Outbreak News for the latest updates.
   - Recent outbreaks are cross-validated to improve diagnosis accuracy.

4. **Notion Integration**
   - Outbreak data is dynamically stored in Notion for record-keeping and easy updates.

---

## 🚀 **Tech Stack**
| **Component**              | **Technology Used**            |
|----------------------------|--------------------------------|
| **Frontend**               | HTML, TailwindCSS             |
| **Backend**                | Flask, Python                 |
| **AI Model**               | OpenAI GPT-4o, Custom CNN     |
| **Data Scraping**          | Selenium, BeautifulSoup       |
| **Outbreak Data**          | WHO Outbreak News             |
| **Notion Integration**     | Notion API                    |
| **Malaria Detection Model**| TensorFlow, Pillow, NumPy     |

---

## 💻 **Setup and Installation**
Follow these steps to set up the project on your local machine:

### **Prerequisites**
- Python 3.8+
- OpenAI API Key
- Notion Integration Token
- TensorFlow
- Flask
- Selenium (automatically installs ChromeDriver)
- BeautifulSoup4

### **Installation Steps**
1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/MissDiagnosis.git
   cd MissDiagnosis
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables**
   Create a `.env` file in the project root and add your API keys:
   ```env
   OPENAI_KEY=your_openai_api_key
   NOTION_KEY=your_notion_integration_token
   ```

4. **Run the Backend Server**
   ```bash
   python app.py
   ```
   The Flask server will run on `http://localhost:1000`.

5. **Access the Frontend**
   - Navigate to `http://localhost:1000` to access the home page.
   - Use `/dashboard` for the main EMR input interface.

---

## 🧠 **Project Architecture**
```
MissDiagnosis/
|
|-- templates/
|   |-- index.html           # Home Page
|   |-- dashboard.html       # Dashboard Page (EMR)
|
|-- static/                  # Frontend static assets
|
|-- model.py                 # Malaria prediction model (CNN)
|-- app.py                   # Flask application (Backend)
|-- main.py                  # Main workflow logic
|-- scrape.py                # Web scraping WHO data
|-- scrape2.py               # HTML parsing and structuring outbreak data
|-- hug.py                   # GPT-4o Integration and outbreak analysis
|-- n.py                     # Notion API integration
|-- res.html                 # WHO data saved as HTML
|-- train.ipynb              # Model training notebook
|-- requirements.txt         # Python dependencies
|
`-- README.md                # Project documentation
```

---

## 🛠️ **How It Works**
1. **Input Data:**
   - The doctor inputs patient symptoms, medical history, diagnosis, and prescriptions into the dashboard.

2. **Malaria Detection:**
   - The custom CNN model predicts malaria infection status using blood image data.

3. **Outbreak Validation:**
   - The backend scrapes WHO Outbreak News for recent epidemic updates.
   - Notion API stores the data in a dedicated database.

4. **GPT-4o Analysis:**
   - GPT-4o analyzes the diagnosis against the outbreak data, symptoms, and malaria prediction.
   - Returns feedback and further test suggestions.

5. **Output:**
   - Real-time analysis is displayed on the dashboard for quick decision-making.

---

## 📸 **Screenshots**
### **1. Dashboard**
![Dashboard Screenshot](screenshot.png)

### **2. Diagnosis Analysis Result**
![Analysis Result](analysis_result.png)

---

## 🤝 **Contributors**
- **Iminabo Roberts** - AI Developer & Backend Engineer
- **Chinwendu Onwuka** - Backend Developer, Flask & Product Design
- **Ngaatendwe Dumbarimwe** - Health News Integration
- **Ebenezer Acquah** - Frontend Developer
- **Oluwatomiloba Onasanya** - Product Manager & Presenter
- **Belema Roberts** - AI Developer & Backend Engineer

---

## 🧠 **Inspiration**
MissDiagnosis was inspired by the challenges faced during the **Ebola** and **Lassa fever** epidemics in Nigeria, where diseases were frequently misdiagnosed as malaria due to overlapping symptoms and lack of awareness.

---

## 📝 **Future Improvements**
- Integration of **more medical-specific LLMs** from Hugging Face for diagnosis.
- Implement a user authentication system for secure EMR storage.
- Expand disease detection capabilities with additional models.
- Real-time WHO API integration for automated outbreak updates.

---

## 🌟 **Acknowledgements**
- **Notion Hackathon** at Grambling State University
- **OpenAI GPT-4o and Tensorflow** for AI analysis
- **WHO Disease Outbreak News** for health data

---

## 🎯 **Live Demo**
Check out the live version of the project: [MissDiagnosis Live](missdiagnosis-qfxu.onrender.com)

---

## 🧩 **Contributing**
Let's build the future of healthcare together!

---

## 🌐 **Contact**
For questions or suggestions, reach out to:
- LinkedIn: [Your LinkedIn Profile](https://www.linkedin.com/in/iminabo-roberts/)
