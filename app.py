from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# For storing booked slots (in-memory dictionary, replace with a database in a real application)
booked_slots = {}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/booking', methods=['GET', 'POST'])
def booking():
    if request.method == 'POST':
        date = request.form['date']
        time_slot = request.form['time_slot']

        if date not in booked_slots:
            booked_slots[date] = []

        if time_slot not in booked_slots[date]:
            booked_slots[date].append(time_slot)

    return render_template('booking.html', booked_slots=booked_slots)

if __name__ == '__main__':
    app.run(debug=True)
