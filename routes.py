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

def determine_returns(weekly_total=0, years=0):
    pa_interest = 0.0015
    years = years
    comp_period = 12
    pay_period = 52
    annuity = weekly_total
    i_alpha = float(pa_interest/comp_period)
    a_alpha = (1+i_alpha)**comp_period
    EAR_weekly = a_alpha**(1/pay_period) - 1
    future_value = annuity *((1 + EAR_weekly)**(pay_period*years)-1)/EAR_weekly
    print(future_value)
    return "{:.2f}".format(future_value)

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
    prizesdf = rangedf[rangedf['digit'] == number]
    if start_year == end_year:
        diff = 1
    else:
        diff = end_year - start_year
    cost = (big_bet + small_bet) * 3 * 52 * diff
    winnings = big_bet * \
        prizesdf['big_bet'].sum() + small_bet * prizesdf['small_bet'].sum()
    total = winnings - cost
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
    weekly_total = (small_bet + big_bet) * 3
    years = start_year - end_year
    if years == 0:
        years = 1
    investment = determine_returns(weekly_total=weekly_total, years=years)
    
    #print(results)
    if results['total'] >= 0:
        total = '${}\n'.format(results['total'])
    else:
        total = '-${}\n'.format(abs(results['total']))

    return render_template('results.html', cost=results['cost'], investment=investment,
                            winnings=results['winnings'], total=total, prizes=results['prizes'])
