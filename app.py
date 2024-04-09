from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy user data (Replace with a database in a real-world scenario)
users = {
    'user1': {'companyName': 'jones', 'email': 'nitin.m@hardtrac.co.in', 'employeeId': '657', 'password': 'nitin@123'}
}

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        company_name = request.form['companyName']
        email = request.form['email']
        employee_id = request.form['employeeId']
        password = request.form['password']

        # Check if user exists and credentials match
        if 'user1' in users and \
           users['user1']['companyName'] == company_name and \
           users['user1']['email'] == email and \
           users['user1']['employeeId'] == employee_id and \
           users['user1']['password'] == password:
            
            # Redirect to the specified URL after successful login
            return redirect("https://hardtrac.co.in/?page_id=38338&v=6c8403f93333")
        
        # Redirect back to login page if login fails
        return redirect(url_for('index'))
    
    # If GET request, return login page
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
