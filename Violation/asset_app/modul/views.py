from flask import render_template, redirect, url_for, request

from asset_app import app, DB_PATH
from asset_app.modul.models import Violation, Intruder, Fine, addViolation, finesUser, SearchForm, searchFines, summ


@app.route('/')
@app.route('/index')
def hello():
    return render_template('index.html')

@app.route('/list_fines')
def list():
    summ()
    current_fine = finesUser()
    return render_template('list_fines.html', current_fine=current_fine)


@app.route('/fines', methods=['GET', 'POST'])
def fine_forms():
    form = Violation()
    if form.validate_on_submit():
        name = form.name.data
        number_plate = form.number_plate.data
        violations = form.violations.data
        date_violation = form.date_violations.data
        driver = Intruder(name, number_plate)
        addViolation(driver, violations, date_violation)
        return redirect(url_for('list'))
    return render_template('fine.html', form=form)


@app.route('/search', methods=['GET', 'POST'])
def search_forms():
    form = SearchForm()

    if form.validate_on_submit():
        number_plate = form.number_plate.data
        current_fine = searchFines(number_plate)
        return render_template('searchViolation.html', form=form, current_fine=current_fine)

    return render_template('searchViolation.html', form=form)