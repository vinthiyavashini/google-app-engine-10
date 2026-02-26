from flask import Flask, render_template_string, request, redirect, url_for, session
import os
import random

# Flask initialization - Corrected with double underscores
app = Flask(__name__)
app.secret_key = "cloud_computing_2026_secret" 

# Cloud settings
BACKGROUND_IMAGE = "https://raw.githubusercontent.com/padmasri618/my-google-app-engine/main/CC.jpeg"
CLOUD_FACTS = [
    "90% of the world's data was generated in the last 2 years thanks to Cloud scalability.",
    "Cloud computing is estimated to be 40% more cost-effective for small businesses.",
    "The 'Cloud' is actually composed of millions of miles of undersea fiber optic cables.",
    "By 2026, it is predicted that 95% of digital workloads will be deployed on cloud-native platforms.",
    "The first concept of cloud computing dates back to the 1960s with J.C.R. Licklider's Intergalactic Computer Network."
]

# --- HTML TEMPLATES ---

LOGIN_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Cloud Access Login</title>
    <style>
        body {
            margin: 0; font-family: 'Segoe UI', sans-serif;
            background: url('{{ bg }}') no-repeat center center fixed; background-size: cover;
            height: 100vh; display: flex; align-items: center; justify-content: center;
        }
        .login-card {
            background: rgba(0, 15, 40, 0.9); padding: 40px; border-radius: 15px;
            border: 1px solid #00d2ff; text-align: center; color: white; width: 320px;
        }
        input { width: 90%; padding: 12px; margin: 10px 0; border-radius: 5px; border: none; }
        .btn {
            background: #00d2ff; color: #001528; padding: 12px; border: none;
            border-radius: 25px; font-weight: bold; cursor: pointer; width: 100%; margin-top: 15px;
        }
        .error { color: #ff4d4d; font-size: 0.9rem; margin-top: 10px; }
    </style>
</head>
<body>
    <div class="login-card">
        <h2>Cloud Login</h2>
        <form method="POST">
            <input type="text" name="username" placeholder="Username (admin)" required>
            <input type="password" name="password" placeholder="Password (cloud123)" required>
            <button type="submit" class="btn">Login</button>
        </form>
        {% if error %}<p class="error">{{ error }}</p>{% endif %}
    </div>
</body>
</html>
"""

PORTAL_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Cloud Portal</title>
    <style>
        body {
            margin: 0; padding: 0; font-family: 'Segoe UI', sans-serif;
            background: url('{{ bg }}') no-repeat center center fixed; background-size: cover;
            color: white; display: flex; flex-direction: column; align-items: center; min-height: 100vh;
        }
        .overlay {
            background: rgba(0, 15, 40, 0.8); width: 100%; min-height: 100vh;
            display: flex; flex-direction: column; align-items: center; padding: 50px 20px;
        }
        .grid {
            display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 25px; max-width: 1000px; width: 100%;
        }
        .card {
            background: rgba(255, 255, 255, 0.1); backdrop-filter: blur(8px);
            padding: 25px; border-radius: 12px; border: 1px solid #00d2ff;
        }
        .btn {
            background: #00d2ff; color: #001528; padding: 12px 25px; border-radius: 30px;
            text-decoration: none; font-weight: bold; display: inline-block; margin: 10px;
        }
    </style>
</head>
<body>
    <div class="overlay">
        <h1>Cloud Computing Portal</h1>
        <div class="grid">
            <div class="card"><h3>IaaS</h3><p>Infrastructure as a Service</p></div>
            <div class="card"><h3>PaaS</h3><p>Platform as a Service</p></div>
            <div class="card"><h3>SaaS</h3><p>Software as a Service</p></div>
        </div>
        <div style="margin-top:40px; background:rgba(0,0,0,0.5); padding:20px; border-left:5px solid #00d2ff;">
            <strong>Fact:</strong> {{ fact }}
        </div>
        <div style="margin-top: 20px;">
            <a href="{{ url_for('portal') }}" class="btn">New Fact</a>
            <a href="{{ url_for('logout') }}" class="btn" style="background:#ff4d4d; color:white;">Logout</a>
        </div>
    </div>
</body>
</html>
"""

# --- ROUTES ---

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        # Admin credentials
        if request.form['username'] == 'admin' and request.form['password'] == 'cloud123':
            session['logged_in'] = True
            return redirect(url_for('portal'))
        else:
            error = "Invalid Username or Password!"
    return render_template_string(LOGIN_TEMPLATE, bg=BACKGROUND_IMAGE, error=error)

@app.route('/portal')
def portal():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    selected_fact = random.choice(CLOUD_FACTS)
    return render_template_string(PORTAL_TEMPLATE, bg=BACKGROUND_IMAGE, fact=selected_fact)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
