import re

from flask import Flask, render_template, request

import pandas as pd
from app import app

df = pd.read_csv('static/4dwinnings.csv',
                 encoding='utf-8', sep=',', header='infer')
df['draw_date'] = pd.to_datetime(df['draw_date'])


@app.route('/', methods=['GET'])
def index():
    """
    renders template for form
    """
    return render_template('4dcalculator.html')


def get_prizes(start_year, end_year, number=0, small_bet=0, big_bet=0):
    """[Calculates profit/loss between start year and end year]

    Arguments:
    start_year {[int]} -- First year
    end_year {[int]} -- Final year
    number {[int]} -- 4d number

    Keyword Arguments:
    small_bet {int} -- Small bet amount (default: {0})
    big_bet {int} -- Big bet amount (default: {0})
    """

    if start_year == end_year:
        rangedf = df[df['draw_date'].dt.year == start_year]
    else:
        rangedf = df[df['draw_date'].isin(
            pd.date_range(str(start_year), str(end_year)))]
    print(rangedf)
    print(number)
    prizesdf = rangedf[rangedf['digit'] == number]
    print(prizesdf)
    if start_year == end_year:
        diff = 1
    else:
        diff = end_year - start_year
    cost = (big_bet + small_bet) * 3 * 52 * diff
    winnings = big_bet * \
        prizesdf['big_bet'].sum() + small_bet * prizesdf['small_bet'].sum()
    total = winnings - cost
    print(total)
    prizes = prizesdf.to_dict('records')
    return {'cost': cost, 'winnings': winnings, 'total': total, 'prizes': prizes}


@app.route('/calculate', methods=["POST"])
def calculate():
    """calculate winnings"""
    start_year = int(request.form['start_year'])
    end_year = int(request.form['end_year'])
    big_bet = int(request.form['big_bet'])
    small_bet = int(request.form['small_bet'])
    number = int(request.form['number'])
    results = get_prizes(start_year=start_year, end_year=end_year,
                         number=number, big_bet=big_bet, small_bet=small_bet)
    print(results)
    if results['total'] >= 0:
        total = '<strong>Profits :</strong> ${}\n'.format(results['total'])
    else:
        total = '<strong>Loss:</strong> ${}\n'.format(results['total'])

    return render_template('results.html', cost=results['cost'], 
                            winnings=results['winnings'], total=total, prizes=results['prizes'])
