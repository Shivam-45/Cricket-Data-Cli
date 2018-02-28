import click
import requests
import json
import sys;
reload(sys);
sys.setdefaultencoding("utf8")


def get_live_score():
    url = "https://powerful-tor-13817.herokuapp.com/live"
    r = json.loads(requests.get(url).text)

    response = "Live Matches"

    for i in range(0, len(r["Matches"])):
        id = str(r["Matches"][i]["ID"])
        status = unicode(str(r["Matches"][i]["Status"]), "utf-8")
        status = status.encode("utf-8")
        team_a = str(r["Matches"][i]["Team A"])
        team_b = str(r["Matches"][i]["Team B"])

        response += "\n--------------------"
        response += "\n" + id
        response += "\n" + status
        response += "\n" + team_a
        response += "\n" + team_b + "\n"

    return response


def get_rankings(format, category):
    url = "https://powerful-tor-13817.herokuapp.com/rankings/" + str(format) + "/" + str(category)
    r = requests.get(url).text

    print "Rankings"
    print "\n" + r


def get_news():
    url = "https://powerful-tor-13817.herokuapp.com/news"
    r = requests.get(url).text
    print "Latest News"
    print "\n" + r


@click.command()
@click.option("--score", help="Displays the live cricket scores")
@click.option("--format", help="Specifies the format to fetch the rankings - odi, test, t20")
@click.option("--rankings", default="team", help="Displays the rankings for a particular type - team, bowlers, batsmen, allrounders")
@click.option("--news", help="Displays the latest cricket news - latest etc")
def main(score, rankings, format, news):
    if score:
        message = get_live_score()
        print message
    elif format:
        get_rankings(format, rankings)
    elif news:
        get_news()


if __name__ == "__main__":
    main()