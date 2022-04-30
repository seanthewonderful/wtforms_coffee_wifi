from logging import PlaceHolder
from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TimeField, IntegerField, SelectField
from wtforms.validators import DataRequired, NumberRange
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    map_URL = StringField('Paste Map Link', validators=[DataRequired()])
    # open_time = TimeField('Opening Time', validators=[DataRequired()])
    # close_time = TimeField('Closing Time', validators=[DataRequired()])
    open_time = StringField("Opening time eg 8:30AM", validators=[DataRequired()])
    close_time = StringField("Closing time eg 10:30PM", validators=[DataRequired()])
    coffee_rating = SelectField('Coffee Rating', choices=[('☕️☕️☕️☕️☕️'), ('☕️☕️☕️☕️'), ('☕️☕️☕️'), ('☕️☕️'), ('☕️')])
    wifi_rating = SelectField('Wifi Rating', choices=[('💻💻💻💻💻'), ('💻💻💻💻'), ('💻💻💻'), ('💻💻'), ('💻')])
    power_rating = SelectField('Power Outlet Rating', choices=[('🔌🔌🔌🔌🔌'), ('🔌🔌🔌🔌'), ('🔌🔌🔌'), ('🔌🔌'), ('🔌')])
    submit = SubmitField('Submit')



# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        # print(form.data)
        with open('cafe-data.csv', 'a') as db:
            db.write(f"\n{form.cafe.data},"
                     f"{form.map_URL.data},"
                     f"{form.open_time.data},"
                     f"{form.close_time.data},"
                     f"{form.coffee_rating.data},"
                     f"{form.wifi_rating.data},"
                     f"{form.power_rating.data}")
                     
        return redirect(url_for('cafes'))
        
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
