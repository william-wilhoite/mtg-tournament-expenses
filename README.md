# An Analysis of Magic: The Gathering - Investigating Deck Prices & Pro Tournament Results

## Table of Contents
- [Summary](#Summary)
- [Motivation](#Motivation)
- [Data Questions](#DataQuestions)
- [Technologies Used](#TechnologiesUsed)
- [Data Sources](#DataSources)
- [Process](#Process)
- [Known Issues and Challenges](#KnownIssuesandChallenges)

## Summary
As a longtime Magic: The Gathering player, I designed this capstone to explore the potential impact the cost of decks might have on the chances of victory at high-level tournaments. Additionally, I was curious to calculate the average return of investment is for high-level play. By web scraping MTGGoldfish (a site which lists tournament results and card prices), I was able to collect deck data, as well as the prices for those decks in the brief time period prior to a tournament. This helped me to investigate the possible correlation between deck prices and wins, as well as players' returns on their investments.

## Motivation
As an avid player of the game, I am interested in how the price of decks affect the chance of winning among top players. In particular, I am curious whether the top players can effectively distinguish underrated cards, and - upon new set releases - be able to win tournaments with cheaper decks than the larger pool of professional players. Additionally, I am interested in the expected return on investment for high-level Magic players and if that return has risen or fallen over time.

## Data Questions
1. How do prices of Magic: The Gathering affect tournament placements?
2. How has this changed overtime?
3. What is the expected return on investment for high-level players of the game who participate in competitive tournaments?


## Technologies Used
1. Python/Jupyter Notebook
2. Microsoft Power BI

## Data Sources
Main:       [MTGGoldfish](https://www.mtggoldfish.com/)
Additional: [Wikipedia - List of Magic: The Gathering Pro Tours](https://en.wikipedia.org/wiki/List_of_Magic:_The_Gathering_Pro_Tour_events) & [The Official Pro Tour Website](https://magic.gg/events/pro-tour-march-of-the-machine)

## Process
### Aquiring the Data
1. Find all recent Standard Pro Tours  
2.Webscrape for Tables of all tournament results.  
3.Pull All Decks from each tournament.  
4. Pull all cards from each tournament.  
5. Webscrape for previous price data.  

###  Calculating the Estimated Cost of Each Deck.
6.Calculate the cost for each card use historical data for 7-14 days before the tournament start date.
7. Join those values to DataFrame all related decks.
8. Calculate an estimated price for each deck.
9. Join those deck prices back with their tournament tables.

## Known Issues and Challenges
1. It is necessary to have an account to access older sales data from MTGGoldfish.
2. Because prices change depending on the tournament results, it is necessary to locate historic prices immediately prior to a related tournament.