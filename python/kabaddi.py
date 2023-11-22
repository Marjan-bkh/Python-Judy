player_cnt= int(input())
play_cnt= input().split()[:player_cnt]
play_list= [x for x in play_cnt if int(x)<=2]
team= len(play_list)//3
print(team)

