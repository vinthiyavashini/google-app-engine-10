from flask import Flask, render_template_string, request, redirect, url_for, session
import os
import random

app = Flask(_name_)
# This key is required to keep you logged in across different pages
app.secret_key = "cloud_computing_2026_secret" 

# --- SETTINGS ---

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
            box-shadow: 0 0 20px rgba(0, 210, 255, 0.3);
        }
        h2 { color: #00d2ff; margin-bottom: 20px; }
        input {
            width: 90%; padding: 12px; margin: 10px 0; border-radius: 5px; 
            border: 1px solid #333; background: #fff; color: #333;
        }
        .btn {
            background: #00d2ff; color: #001528; padding: 12px; border: none;
            border-radius: 25px; font-weight: bold; cursor: pointer; width: 100%; 
            margin-top: 15px; transition: 0.3s;
        }
        .btn:hover { background: white; }
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
        .header { text-align: center; margin-bottom: 40px; }
        h1 { font-size: 3rem; color: #00d2ff; margin: 0; }
        .grid {
            display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 25px; max-width: 1000px; width: 100%;
        }
        .card {
            background: rgba(255, 255, 255, 0.1); backdrop-filter: blur(8px);
            padding: 25px; border-radius: 12px; border: 1px solid rgba(0, 210, 255, 0.3);
        }
        h3 { color: #00d2ff; margin-top: 0; }
        .fact-box {
            margin-top: 40px; padding: 25px; background: rgba(0, 210, 255, 0.15);
            border-radius: 10px; border-left: 6px solid #00d2ff; max-width: 700px;
        }
        .nav-btns { margin-top: 30px; }
        .btn {
            background: #00d2ff; color: #001528; padding: 12px 25px; border: none;
            border-radius: 30px; font-weight: bold; cursor: pointer; text-decoration: none;
            margin: 10px; display: inline-block;
        }
        .btn-logout { background: #ff4d4d; color: white; }
    </style>
</head>
<body>
    <div class="overlay">
        <div class="header">
            <h1>Cloud Computing Portal</h1>
            <p>Welcome, User. Your session is secure.</p>
        </div>

        <div class="grid">
            <div class="card">
                <h3>Infrastructure (IaaS)</h3>
                <p>On-demand access to cloud-hosted computing infrastructure—servers, storage, and networking.</p>
            </div>
            <div class="card">
                <h3>Platform (PaaS)</h3>
                <p>A complete cloud environment for developing, managing, and delivering applications.</p>
            </div>
            <div class="card">
                <h3>Software (SaaS)</h3>
                <p>Cloud-based applications provided as a service to end-users over the internet.</p>
            </div>
        </div>

        <div class="fact-box">
            <strong>Cloud Fact:</strong><br>
            {{ fact }}
        </div>

        <div class="nav-btns">
            <a href="{{ url_for('portal') }}" class="btn">Generate New Fact</a>
            <a href="{{ url_for('logout') }}" class="btn btn-logout">Secure Logout</a>
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
        # Credentials check
        if request.form['username'] == 'admin' and request.form['password'] == 'cloud123':
            session['logged_in'] = True
            return redirect(url_for('portal'))
        else:
            error = "Invalid Username or Password!"
    
    return render_template_string(LOGIN_TEMPLATE, bg=BACKGROUND_IMAGE, error=error)

@app.route('/portal')
def portal():
    # Security check: If not logged in, redirect to login page
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    
    selected_fact = random.choice(CLOUD_FACTS)
    return render_template_string(PORTAL_TEMPLATE, bg=BACKGROUND_IMAGE, fact=selected_fact)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))

if _name_ == "_main_":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
