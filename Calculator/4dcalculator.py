import pandas as pd

df = pd.read_csv('4dwinnings.csv', encoding='utf-8', sep=',', header='infer')
df['draw_date'] = pd.to_datetime(df['draw_date'])


def get_prizes(start_year, end_year, number=0, small_bet=0, big_bet=0):
    """[summary]

    Arguments:
    start_year {[int]} -- First year
    end_year {[int]} -- Final year
    number {[int]} -- 4d number

    Keyword Arguments:
    small_bet {int} -- Small bet amount (default: {0})
    big_bet {int} -- Big bet amount (default: {0})
    """
    rangedf = df[df['draw_date'].isin(pd.date_range(str(start_year), str(end_year)))]
    prizesdf = rangedf[rangedf['digit']== number]
    cost = (big_bet + small_bet) * 3 * 52 * (end_year - start_year)
    winnings = big_bet * prizesdf['big_bet'].sum() + small_bet * prizesdf['small_bet'].sum()
    total = winnings - cost
    print('Number:  {}\n'.format(number))
    print('Total cost: {}\n'.format(cost))
    print('Total Winnings: {}\n'.format(winnings))
    if total >= 0:
        print('Profit: {}'.format(total))
    else:
        print('Loss: {}'.format(abs(total)))
