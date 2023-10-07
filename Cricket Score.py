player_score =  {}
with open("you_file","r") as rd: #your file path/name
    for line in rd:
        player,score = line.split(',')
        score = int(score)
        if player in player_score:
            player_score[player].append(score)
        else:
            player_score[player] = [score]
print(player_score)for i,j in player_score.items():
    minj = min(j)
    maxj = max(j)
    avgj = sum(j)/len(j)
    print(f"the minimum for {i} is {minj} , max is {maxj} and avg is {avgj}")






