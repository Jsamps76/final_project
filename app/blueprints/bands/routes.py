from . import bp as band
from flask import Flask, request, url_for, render_template, flash, redirect
from flask_login import current_user, login_required



@band.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)


@band.route('/')
@login_required
def joesbands():
    return render_template('joesbands.html')


@band.route('/search', methods=['GET', 'POST'])
@login_required
def search():
    form = SearchForm()
    if request.method == 'POST' and form.validate_on_submit():
        # or what you want
        return redirect((url_for('search_results', query=form.search.data)))
    return render_template('search.html', form=form)
