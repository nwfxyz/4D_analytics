# 4D_analytics

Hi guys ! Its u/Sproinkerino and u/captmomo again from the [MRT Delay post](https://www.reddit.com/r/singapore/comments/8l7tql/miniproject_data_analysis_of_mrt_delays/). This time we will be exploring something close to our aunties and uncles in Singapore, 4D. 

As well all know that any official gambling games has a negative expected payoff for the player, (-$0.341 for big and -$0.42 for small) but for 4D some people hold a special number in their hearts. Is it true that some numbers are luckier than others? And how much would you have by today if instead of spending it on 4D you place it on a simple fixed deposit? 

DISCLAIMER: We do not advocate gambling. This study aims to show that gambling has a net expected payoff and should only be treated as a form of entertainment and a form of investment. No we are not providing investment advise.

## Obtaining of Data

We used the api provided by Singapore pools to obtain the historical dataset from 1986 to today.
http://www.singaporepools.com.sg/en/product/Pages/4d_cpwn.aspx

## Data Visualization of 4D Numbers vs Historical Prize Money

https://imgur.com/a/KPHPlIC
Using the historical data, we produced a heatmap of each number from 0000 to 9999. "Red" signifies a lucky number or a number that has won relatively more prizes than others.

Histogram of Historical Prizes:
https://imgur.com/T1MEFW3

As we can see, some numbers are "luckier" than others.

__6190__, __2982__ has only won a total of $50 each.
While,  __7132__ and __7123__ has won a total of $4850 and $4650 respectively. (What a coincedence?)


## 4D What if? Calculator

The webapp calculates how much money you would have made/lost if you have bet on the same four digits for the a range of years.  
It also calculates how much money you would have saved if you have deposited in the bank.

<img src="https://i.imgur.com/AD3TyyB.png" height="300">

Link: https://fourd-analytics.herokuapp.com/


## Simulation 

Here we attempt to test a simple gambling strategy to 4D, using the Martingale strategy we will see in a simulation if you can actually use this strategy to win in 4D.
https://en.wikipedia.org/wiki/Martingale_(betting_system)

Our strategy goes like this:

1) You start with $10,000
2) You start by buying $1 worth of 4D tickets
3) If you have more money than you started off with, only buy $1 for the next round.
4) If you have less money than you started off with, buy (10000 - currentcash)/60 + 1, rounded down, this is such that if you win even the consolation prize, you recoup your losses.
5) If your cash exceeds $15000, stop playing.

Out of 2000 iterations, only 626 of them makes money. With the average loss of -$2,869.04.
Density Plot: https://imgur.com/a/DM8jntJ

So even with some funky strategy you still lose money most of the time.

## Conclusion

We never doubt the fun that 4D can bring to us but remember to gamble wisely and the house (Singapore Pools) always wins !
