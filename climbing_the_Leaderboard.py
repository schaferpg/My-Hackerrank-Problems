# https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem

def climbingLeaderboard(scores, alice):
    position = []
    for i in range(len(alice)):
        x = 0
        for j in range(len(scores)):
            x += 1 
            
            # figure out how to go from position 1 to 3 if it's 100 100 and 60
            # Both 100's are position 1 but 60 is 3
            
            if alice[i] >= scores[j]:
                print(x)
                break
