from flask import Flask, render_template
import time

app = Flask(__name__)

@app.route('/')
def home():
    # Simulando um pequeno processamento para tornar o alvo mais "real"
    # Em um ataque Layer 7, isso ajudaria a sobrecarregar a CPU
    return render_template('index.html')

if __name__ == '__main__':
    # Roda na porta 80 (padrão HTTP). Requer privilégios de sudo.
    app.run(host='0.0.0.0', port=80, debug=False)