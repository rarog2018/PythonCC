#! python3
# c17e02hackerNewsDiscussions - creates a bar chart that shows most active
# discussions on Hacker News

import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
from operator import itemgetter


def main():
    # store the API response in a variable
    responseDict = call_API()

    # if call_API returned None then exit
    if responseDict == None:
        return 1

    # process each submission's data
    subDicts = process_submissions(responseDict)
    subNames = []  # x axis labels
    # because we sorted the subDicts we have to add names in correct order
    for elem in subDicts:
        subNames.append(elem['label'])

    # setup the style and config object
    myStyle = LS('#333366', base_style=LCS)
    myConfig = make_config()

    # now we have everything to plot the chart
    chart = pygal.Bar(myConfig, style=myStyle)
    chart.title = "Most-Discussed submissions on Hacker News"
    chart.x_labels = subNames

    chart.add('', subDicts)
    fileName = "HN_active_discussions.svg"
    print(f"Rendering file: {fileName}")
    chart.render_to_file(f"./{fileName}")


def call_API():
    # create the url using info from the user
    url = f'https://hacker-news.firebaseio.com/v0/topstories.json'
    # use requests to get contents from the API
    r = requests.get(url)
    # next step depend on the status code
    if r.status_code == 200:
        # 200 means that all went ok, so we can return the data
        return r.json()
    else:
        print("Something went wrong")
        return None


def process_submissions(rD):
    submissionDicts = []
    # get top 30 submissions
    for submissionId in rD[:30]:
        url = ('https://hacker-news.firebaseio.com/v0/item/' +
               str(submissionId) + '.json')
        # make API call for this ID
        submissionReq = requests.get(url)
        # if status code was not 200, then skip to next iteration
        if submissionReq.status_code != 200:
            print("Skipping ID: " + submissionId)
            continue

        # create a Pygal friendly dictionary
        responseDict = submissionReq.json()

        submissionDict = {
            # number of comments will be the value
            'value': responseDict.get('descendants', 0),
            # submission title will be the label for each bar
            'label': responseDict['title'],
            # and each bar will be a link to the discussion
            'xlink': f'http://news.ycombinator.com/item?id={str(submissionId)}'
        }

        submissionDicts.append(submissionDict)

    return sorted(submissionDicts, key=itemgetter('value'),
                  reverse=True)


def make_config():
    # create config object
    mC = pygal.Config()
    # set various config options
    mC.x_label_rotation = 45
    mC.show_legend = False
    mC.title_font_size = 38
    mC.truncate_label = 15
    mC.show_y_guides = False
    mC.width = 1000

    return mC


main()
