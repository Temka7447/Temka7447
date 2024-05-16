# def highscore():
#     f = open("highscore_snake1", "r")
#     high = f.read()
#     score = f.readlines()
#     for x in score:
#         if int(x) > int(high):
#             high = x
#             return int(high)
#         else:
#             return int(high)
#     f.close()
# f=open("high", "w")
def highscore():
    with open("high.txt", "r") as f:
        scores = f.readlines()
        high = 0
        for score in scores:
            current_score = int(score)
            if current_score > high:
                high = current_score
                return high
            else:
                return high
