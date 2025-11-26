from flask import Flask
import random

app = Flask(__name__)

sozler = [
    "Bugün harika bir gün!",
    "Asla pes etme.",
    "Her şey çok güzel olacak.",
    "Gülümse, hayat güzel."
]

@app.route("/")
def ana_sayfa():
    secilen = random.choice(sozler)
    
    
    return f"""
    <div style="text-align: center; margin-top: 100px; font-family: sans-serif;">
        <h1>✨ GÜNÜN SÖZÜ ✨</h1>
        <h2 style="color: darkblue;">"{secilen}"</h2>
        <br>
        <button onclick="location.reload()">Yeni Söz Getir</button>
    </div>
    """

if __name__ == "__main__":

    app.run(debug=True)
