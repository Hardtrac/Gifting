from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy user data (Replace with a database in a real-world scenario)
users = {
    'user1': {'companyName': 'Company1', 'email': 'user1@email.com', 'employeeId': 'E123', 'password': 'password1'},
    'user2': {'companyName': 'Company2', 'email': 'user2@email.com', 'employeeId': 'E456', 'password': 'password2'}
}

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    company_name = request.form['companyName']
    email = request.form['email']
    employee_id = request.form['employeeId']
    password = request.form['password']

    for user_id, user_data in users.items():
        if user_data['companyName'] == company_name and user_data['email'] == email and \
           user_data['employeeId'] == employee_id and user_data['password'] == password:
            # Redirect to the next page after successful login
            return redirect(url_for('success'))
    
    # Redirect back to login page if login fails
    return redirect(url_for('index'))

@app.route('/success')
def success():
    return "Login successful!"

if __name__ == '__main__':
    app.run(debug=True)
