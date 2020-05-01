#! python3
# c17e01otherLanguages - creates a chart presenting 'n' most starred projects
# in a language provided by the user

import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS


def main():
    while(True):
        # get the language name from the user
        progLang = input("Which language You want to check? (esc to quit) ")

        # quit if user typed 'esc'
        if progLang.lower() == "esc":
            break

        # store the API response in a variable
        responseDict = call_API(progLang)

        # if call_API returned None then reset the loop
        if responseDict == None:
            continue

        # extract the data about repositories from responseDict
        repoData = responseDict["items"]

        # lists that will store the names and other data
        repoNames, repoDicts = [], []

        # fill the lists with data
        add_data(repoData, repoNames, repoDicts)

        # setup the style and config object
        myStyle = LS('#333366', base_style=LCS)
        myConfig = make_config()

        # now we have everything to plot the chart
        chart = pygal.Bar(myConfig, style=myStyle)
        chart.title = f"Most-Starred {progLang} Projects on GitHub"
        chart.x_labels = repoNames

        chart.add('', repoDicts)
        fileName = progLang + "_repos.svg"
        print(f"Rendering file: {fileName}")
        chart.render_to_file(f"./{fileName}")


def call_API(nameL):
    # create the url using info from the user
    url = f'https://api.github.com/search/repositories?q=language:{nameL}&sort=stars'
    # use requests to get contents from the API
    r = requests.get(url)
    # next step depend on the status code
    if r.status_code == 200:
        # 200 means that all went ok, so we can return the data
        return r.json()
    elif r.status_code == 422:
        # this means that the name that user provided is incorrect
        print(f"There is no programming language named {nameL}")
        # so we return None
        return None
    else:
        print("Something went wrong")
        return None


def add_data(repoData, rN, rD):
    # add repository names to repoNames list
    for item in repoData:
        rN.append(item['name'])

        # prepare the plot data
        repoDict = {
            # to show how many stars
            "value": item["stargazers_count"],
            # to show the repository's description
            "label": item["description"],
            # to make the bars links into repositories
            "xlink": item["html_url"]
        }

        # not every repository has a description in that case we will add
        # info that there is no description
        if repoDict["label"] == None:
            repoDict["label"] = "No description provided"

        # append the dictionary to the list of dictionaries
        rD.append(repoDict)


def make_config():
    # create config object
    mC = pygal.Config()
    # set various config options
    mC.x_label_rotation = 45
    mC.show_legend = False
    mC.title_font_size = 24
    mC.label_font_size = 14
    mC.major_label_font_size = 18
    mC.truncate_label = 15
    mC.show_y_guides = False
    mC.width = 1000

    return mC


main()
