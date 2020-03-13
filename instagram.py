from instaloader import Instaloader, Profile
import pandas as pd
import matplotlib.pyplot as plt
import csv
import datetime

def start():
    L = Instaloader()

    user = 'nasa'
    profile = Profile.from_username(L.context, user)
    global userf
    userf = profile.followers
    print('Username @', user)
    print('Followers: ',profile.followers)
    print('Following: ',profile.followees)

    print()

    user1 = 'thenotoriousmma'
    profile1 = Profile.from_username(L.context, user1)
    global user1f
    user1f = profile1.followers
    print('Username @', user1)
    print('Followers: ', profile1.followers)
    print('Following: ', profile1.followees)

    print()

    user2 = 'willsmith'
    profile2 = Profile.from_username(L.context, user2)
    global user2f
    user2f = profile2.followers
    print('Username @', user2)
    print('Followers: ', profile2.followers)
    print('Following: ', profile2.followees)

    print()

    user3 = 'jbalvin'
    profile3 = Profile.from_username(L.context, user3)
    global user3f
    user3f = profile3.followers
    print('Username @', user3)
    print('Followers: ', profile3.followers)
    print('Following: ', profile3.followees)



def writedata():
    #reading data using pandas and specifying which exact location column to row
    df = pd.read_csv('insta.csv')
    print(df['nasa'][0])

    # grabs todays date in the correct format
    x = datetime.datetime.now()
    y = x.strftime('%x').replace("0", "")
    print(y)

    #writing data to the csv file, new row every new input
    row = [y, userf, user1f, user2f, user3f]

    with open('insta.csv', 'a') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(row)
    csvFile.close()


def graphinfo():

    insta = pd.read_csv('insta.csv', index_col=0)
    plot = insta.plot(title='User Follower Count', lw=2, markersize=10)
    plot.ticklabel_format(style='plain', axis='y')
    plot.set_xlabel('Date (Month)')
    plot.set_ylabel('# of Followers')
    plt.show()


def main():
    start()
    writedata()
    graphinfo()
main()