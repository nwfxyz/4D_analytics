# 4D_analytics

Hi guys ! Its u/Sproinkerino and u/captmomo again. This time we will be exploring something close to our aunties and uncles in Singapore, 4D. 

As well all know that any official gambling games has a negative expected payoff for the player, but for 4D some people hold a special number in their hearts. Is it true that some numbers are luckier than others? And how much would you have by today if instead of spending it on 4D you place it on a simple fixed deposit? 

## Obtaining of Data

We used the api provided by Singapore pools to obtain the historical dataset from 1986 to today.
http://www.singaporepools.com.sg/en/product/Pages/4d_cpwn.aspx

## Data Visualization of 4D Numbers vs Historical Prize Money

https://imgur.com/a/KPHPlIC
Using the historical data, we produced a heatmap of each number from 0000 to 9999. "Red" signifies a lucky number or a number that has won relatively more prizes than others.

Histogram of Historical Prizes:
https://imgur.com/T1MEFW3

As we can see, some numbers are "luckier" than others.

6190, 2982 has only won a total of $50 each.
While,  7132 and 7123 has won a total of $4850 and $4650 respectively. (What a coincedence?)


## Simulation (TBD)

## 4D What if? Calculator

The webapp calculates how much money you would have made/lost if you have bet on the same four digits for the a range of years.  
It also calculates how much money you would have saved if you have deposited in the bank.

<img src="https://i.imgur.com/AD3TyyB.png" height="300">

Link: https://fourd-analytics.herokuapp.com/
