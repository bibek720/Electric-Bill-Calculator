from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    equipment_rates = {
        'bulb': 0.05,   # Rate per hour for each equipment
        'fan': 0.10,
        # Add more equipment and rates as needed
    }

    selected_equipments = request.form.getlist('equipment')
    hours_used = float(request.form['hours'])

    total_cost = sum(equipment_rates[equipment] * hours_used for equipment in selected_equipments)

    return render_template('result.html', total_cost=total_cost)

if __name__ == '__main__':
    app.run(debug=True)
