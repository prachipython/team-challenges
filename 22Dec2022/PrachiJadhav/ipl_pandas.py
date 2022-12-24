import pandas as pd
import numpy as np

# Who faced the first and last ball in IPL?
# Who are the Highest and Lowest run scorers of IPL?
# Total matches played per season
# Total runs scored per season
# Toss winners of all matches in ascending order

def first_last_ball_faced():
    d = df.sort_values(["inning", "over", "ball"], ascending=True).reset_index(drop=True)
    fst_ball_by_player=d['non_striker'][0]
    d=df.sort_values(['id',"inning", "over", "ball"], ascending=False).reset_index(drop=True)
    lst_ball_by_player=d['non_striker'][0]
    return f"first ball faced by:  {fst_ball_by_player} and last ball faced by: {lst_ball_by_player}"


def highest_lowest_run_scorer():
    df2=df.groupby('batsman').sum()
    h_run = df2.sort_values(["batsman_runs"], ascending=False).reset_index()
    highest_run_by=h_run['batsman'][0]

    l_run = df2.sort_values(["batsman_runs"], ascending=True).reset_index()
    lowest_run_by=l_run['batsman'][0]
    return f"highest run scorer: {highest_run_by}, lowest run scorer: {lowest_run_by}"

def total_matches_per_season():
    match_data["date"]=pd.DatetimeIndex(match_data["date"]).year
    # print(match_data)
    total_matches_played=match_data.groupby(['date']).size()
    # print(total_matches_played)
    t_m=total_matches_played.reset_index()
    for i in range(t_m.shape[0]):
        print(f"tatal matches played for year {t_m['date'][i]} is {t_m[0][i]}")

def total_run_scored_per_season():
    merged_data = match_data.merge(df,on=["id"])
    ttl_run_scored=merged_data.groupby(['date'])['total_runs'].sum().reset_index()
    print(ttl_run_scored)

def toss_winner():
    return(match_data.groupby('toss_winner').size().sort_values(ascending=False))


if __name__ == '__main__':
    df= pd.read_csv("IPL Ball-by-Ball 2008-2020.csv")
    match_data=pd.read_csv("IPL Matches 2008-2020.csv")
    print(first_last_ball_faced())
    print('*'*50)
    print(highest_lowest_run_scorer())
    print('*'*50)
    total_matches_per_season()
    print('*'*50)
    print(toss_winner())
    print('*'*50)
    total_run_scored_per_season()
