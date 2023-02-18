# IPL Match Details

# Write a program that reads all the match outcomes and summarizes the information of all the matches.


def main():
    N = int(input(""))
    if N >= 0 and N <= 100:
        teamsData = {}
        for i in range(N):
            values = input().split(';')
            firstTeam = values[0].strip()
            secondTeam = values[1].strip()
            matchResult = values[2].strip()
            # add team to dictionary "teamsData"
            if (firstTeam not in teamsData):
                # Matches Played, Won, Lost, Draw, Points
                teamsData[firstTeam] = [0, 0, 0, 0, 0]
            if (secondTeam not in teamsData):
                teamsData[secondTeam] = [0, 0, 0, 0, 0]
            if (firstTeam in teamsData and secondTeam in teamsData):
                teamsData[firstTeam][0] += 1
                teamsData[secondTeam][0] += 1
                # check winner
                if matchResult == 'win':
                    teamsData[firstTeam][1] += 1
                    teamsData[secondTeam][2] += 1
                elif matchResult == 'loss':
                    teamsData[firstTeam][2] += 1
                    teamsData[secondTeam][1] += 1
                elif matchResult == 'draw':
                    teamsData[firstTeam][3] += 1
                    teamsData[secondTeam][3] += 1

        # A win earns a team 3 points. A draw earns 1. A loss earns 0.
        for t in teamsData:
            teamsData[t][4] = teamsData[t][1]*3+teamsData[t][3]
    # Display the team information in descending order of points.
    teamsData = (sorted(teamsData.items(),
                 key=lambda points: points[1][4], reverse=True))
    for t in teamsData:
        ouput = f'Team: {t[0]}, Matches Played: {t[1][0]}, Won: {t[1][1]}, Lost: {t[1][2]}, Draw: {t[1][3]}, Points: {t[1][4]}'
        print(ouput)
    if len(teamsData) == 0:
        print("No Output")


main()


# Coding Solutions Youtube Channel
