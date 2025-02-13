# 💖 Fun Valentine's Day Project - Ask Your Girl Out, Dev Style! 💻❤️

Welcome to the **Fun Valentine's Day Project**, where you can ask your girl to be your **Valentine** in a fun, interactive, and developer-friendly way! 🥰💘

## 🎯 Features
- **Romantic "Will You Be My Valentine?" Prompt** 💖  
- **Two options: "Yes" and "No"**
  - Clicking **"Yes"** makes **hearts** and **"I love you" text** rain down beautifully.  
  - Clicking **"No"** shows a **"Wrong answer!" message** (disappears after 2s) and makes **broken hearts rain**.  
- **Background music** starts playing when the user interacts.  
- **Custom fonts, animations, and colors** to make it feel **extra romantic**!  
- **Developer-friendly Django setup** for quick deployment.  

## 📸 Screenshot
Here's what the final page looks like:  
![Project Screenshot](screen.png)

## 🚀 How to Run
### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/your-username/valentine-project.git
cd valentine-project
```

### **2️⃣ Install Dependencies**
```bash
pip install django
```

### **3️⃣ Run the Django Server**
```bash
python manage.py runserver 0.0.0.0:1818
```

Now, open `http://127.0.0.1:1818/` in your browser.

### **4️⃣ (Optional) Expose it Online with ngrok**
If you want to **share it with your Valentine**, use:

```bash
ngrok http --domain=yourcustomsub.ngrok.dev 1818
```

Or use **Cloudflare Tunnel**:

```bash
cloudflared tunnel --url http://127.0.0.1:1818
```

## 📂 Project Structure
```
valentine_project/
│── valentine_app/
│   │── templates/
│   │   │── valentine.html
│   │── static/
│   │   │── fonts/  (Custom fonts here)
│   │   │── careless.mp3  (Background music)
│   │   │── screen.png  (Screenshot of the project)
│── manage.py
│── README.md
```

## 🛠️ Technologies Used
* **Django** 🐍 (Backend framework)
* **HTML, CSS, JavaScript** 🎨 (Frontend UI & animations)
* **ngrok / Cloudflare Tunnel** 🌍 (For online access)

## ❤️ Want to Modify It?
Feel free to **customize the text, music, fonts, and animations** to make it more personal!

💡 **Made with Love & Code!** 💻💖 Happy Valentine's Day! 🎉🌹
