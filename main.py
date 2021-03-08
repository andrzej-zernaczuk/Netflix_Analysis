import pandas as pd
import numpy as np
import datetime
import calendar
import matplotlib
import matplotlib.pyplot as plt

df = pd.read_csv("netflix_titles.csv")
df.dropna(subset=['type', 'title', 'date_added', 'release_year', 'duration', 'listed_in'], inplace=True)

df['date_added'] = pd.to_datetime(df['date_added'])
df['year_added'] = df['date_added'].dt.year
df['month_added'] = df['date_added'].dt.month
df['duration'] = df['duration'].str.split().str.get(0)
df['duration'] = df['duration'].astype(int)


def present_data():
    print("Number of unique titles: " + number)
    print("Total duration: " + duration)
    print("First ever upload: " + firstUpload)
    print("Latest upload: " + latestUpload)
    print("Oldest production: " + firstRelease)
    print("Latest production: " + latestRelease)
    print("Month with highest number of uploads " + popularUploadMonth)
    print("Year with highest number of uploads " + popularUploadYear)
    print(popularReleaseYear)


loopChoice = True
while loopChoice:
    choice = str(input("What data would you like to see (write number): " +
                       "\n1. Movies" +
                       "\n2. TV Shows" +
                       "\n3. All" +
                       "\n4. Graphs" +
                       "\n5. QUIT\n"))
    if choice == '5':
        print("\nThanks!")
        break
    elif choice == '1':
        number = str(len(df[df['type'] == 'Movie']))
        duration = str(df.groupby('type')['duration'].sum()['Movie']) + " minutes"
        firstUpload = str(pd.to_datetime(df.groupby('type')['date_added'].max()['Movie']))[:-9]
        latestUpload = str(pd.to_datetime(df.groupby('type')['date_added'].max()['Movie']))[:-9]
        firstRelease = str(df.groupby('type')['release_year'].min()['Movie'])
        latestRelease = str(df.groupby('type')['release_year'].max()['Movie'])
        popularUploadMonth = str(
            calendar.month_name[int(df.loc[df['type'] == 'Movie'].groupby('month_added')['month_added'].count().idxmax())]) \
            + ", uploads: " + str(df.loc[df['type'] == 'Movie'].groupby('month_added')['month_added'].count().max())
        popularUploadYear = str(df.loc[df['type'] == 'Movie'].groupby('year_added')['year_added'].count().idxmax()) \
            + ", uploads: " + str(df.loc[df['type'] == 'Movie'].groupby('year_added')['year_added'].count().max())
        popularReleaseYear = str(df.loc[df['type'] == 'Movie'].groupby('release_year')['release_year'].count().idxmax())\
            + ", uploads: " + str(df.loc[df['type'] == 'Movie'].groupby('release_year')['release_year'].count().max())

        present_data()

        shall_continue = input("Do you want to see anything else y/n\n").lower()
        if shall_continue == "y":
            pass
        else:
            print("\nThanks!")
            break

    elif choice == '2':
        number = str(len(df[df['type'] == 'TV Show']))
        duration = str(df.groupby('type')['duration'].sum()['TV Show']) + " seasons"
        firstUpload = str(pd.to_datetime(df.groupby('type')['date_added'].min()['TV Show']))[:-9]
        latestUpload = str(pd.to_datetime(df.groupby('type')['date_added'].max()['TV Show']))[:-9]
        firstRelease = str(df.groupby('type')['release_year'].min()['TV Show'])
        latestRelease = str(df.groupby('type')['release_year'].max()['TV Show'])
        popularUploadMonth = str(
            calendar.month_name[int(df.loc[df['type'] == 'TV Show'].groupby('month_added')['month_added'].count().idxmax())])\
            + ", uploads: " + str(df.loc[df['type'] == 'TV Show'].groupby('month_added')['month_added'].count().max())
        popularUploadYear = str(df.loc[df['type'] == 'TV Show'].groupby('year_added')['year_added'].count().idxmax()) \
            + ", uploads: " + str(df.loc[df['type'] == 'TV Show'].groupby('year_added')['year_added'].count().max())
        popularReleaseYear = str(df.loc[df['type'] == 'TV Show'].groupby('release_year')['release_year'].count().idxmax()) \
            + ", uploads: " + str(df.loc[df['type'] == 'TV Show'].groupby('release_year')['release_year'].count().max())

        present_data()

        shall_continue = input("Do you want to see anything else y/n\n").lower()
        if shall_continue == "y":
            pass
        else:
            print("\nThanks!")
            break

    elif choice == '3':
        number = str(len(df['title']))
        duration = str(df.groupby('type')['duration'].sum()['TV Show']) + ' seasons (TV Series) and ' \
            + str(df.groupby('type')['duration'].sum()['Movie']) + ' minutes (Movies).'
        firstUpload = str(pd.to_datetime(pd.to_datetime(df['date_added']).min()))[:-9]
        latestUpload = str(pd.to_datetime(pd.to_datetime(df['date_added']).max()))[:-9]
        firstRelease = str(df['release_year'].min())
        latestRelease = str(df['release_year'].max())
        popularUploadMonth = str(calendar.month_name[int(df.groupby('month_added')['month_added'].count().idxmax())]) \
            + ", uploads: " + str(df.groupby('month_added')['month_added'].count().max())
        popularUploadYear = str(df.groupby('year_added')['year_added'].count().idxmax()) \
            + ", uploads: " + str(df.groupby('year_added')['year_added'].count().max())
        popularReleaseYear = str(df.groupby('release_year')['release_year'].count().idxmax()) \
            + ", uploads: " + str(df.groupby('release_year')['release_year'].count().max())

        present_data()

        shall_continue = input("Do you want to see anything else y/n\n").lower()
        if shall_continue == "y":
            pass
        else:
            print("\nThanks!")
            break
    elif choice == '4':
        loopGraph = True
        while loopGraph:
            choiceGraph = str(input("What graph would you like to see: " +
                                    "\n1. Ratio of productions types" +
                                    "\n2. Ratio of years of release" +
                                    "\n3. Ratio of addition years" +
                                    "\n4. Number of productions per year" +
                                    "\n5. Number of productions per month" +
                                    "\n6. BACK?\n"))
            if choiceGraph == '6':
                break

            elif choiceGraph == "1":
                labels = 'TV Shows', 'Movies'
                sizes = [len(df[df['type'] == 'TV Show']), len(df[df['type'] == 'Movie'])]
                explode = (0, 0.1)

                figRatioType, axRatioType = plt.subplots()
                axRatioType.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
                axRatioType.axis('equal')
                axRatioType.set_title("Ratio of productions types")
                plt.show()

                shall_continue = input("Do you want to see anything else y/n\n").lower()
                if shall_continue == "y":
                    pass
                else:
                    break

            elif choiceGraph == "2":
                list_yearsReleased = sorted(df['release_year'].unique().tolist())

                labels = list_yearsReleased
                sizes = []
                for label in labels:
                    sizes.append(len(df[df['release_year'] == label]))

                figRatioRelease, axRatioRelease = plt.subplots()
                axRatioRelease.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=0)
                axRatioRelease.axis('equal')
                axRatioRelease.set_title("Ratio of years of release")
                plt.show()

                shall_continue = input("Do you want to see anything else y/n\n").lower()
                if shall_continue == "y":
                    pass
                else:
                    print("\nThanks!")
                    break

            elif choiceGraph == "3":
                list_yearsAdded = sorted(df['year_added'].unique().tolist())

                labels = list_yearsAdded
                sizes = []
                for label in labels:
                    sizes.append(len(df[df['year_added'] == label]))

                figRatioAdded, axRatioAdded = plt.subplots()
                axRatioAdded.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=0)
                axRatioAdded.axis('equal')
                axRatioAdded.set_title("Ratio of addition years")
                plt.show()

                shall_continue = input("Do you want to see anything else y/n\n").lower()
                if shall_continue == "y":
                    pass
                else:
                    break

            elif choiceGraph == "4":
                list_yearsAdded = sorted(df['year_added'].unique().tolist())

                width = 0.2
                labels = list_yearsAdded
                numbers = []
                for label in labels:
                    numbers.append(len(df[df['year_added'] == label]))

                figPPY, axPPY = plt.subplots()
                axPPY.bar(labels, numbers, width)
                axPPY.set_title("Number of productions per year")
                axPPY.tick_params(axis='x', rotation=70)
                plt.xticks(range(min(list_yearsAdded), max(list_yearsAdded) + 1))
                plt.show()

                shall_continue = input("Do you want to see anything else y/n\n").lower()
                if shall_continue == "y":
                    pass
                else:
                    break

            elif choiceGraph == "5":
                list_monthsAdded = sorted(df['month_added'].unique().tolist())

                width = 0.2
                labels = list_monthsAdded
                numbers = []
                for label in labels:
                    numbers.append(len(df[df['month_added'] == label]))

                figPPM, axPPM = plt.subplots()
                axPPM.bar(labels, numbers, width)
                axPPM.set_title("Number of productions per month")
                plt.xticks(range(1, 13))
                plt.show()

                shall_continue = input("Do you want to see anything else y/n\n").lower()
                if shall_continue == "y":
                    pass
                else:
                    break

    else:
        print("\nWrong input, try again!")
        pass
