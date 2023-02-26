import requests
from bs4 import BeautifulSoup


def get_response(url):
    resp = requests.get(url)
    return resp


if __name__ == "__main__":
    resp = get_response("https://www.rottentomatoes.com/browse/movies_at_home/sort:popular")
    soup = BeautifulSoup(resp.content, 'html.parser')
    #results = soup.select("body.body.no-touch.js-mptd-layout")
    results = soup.find_all(class_="js-tile-link")
    #print(results)

    ascore, cscore, asentiment, csentiment = "----"
    for result in results:
        print("*"*30)
        #print(result.prettify())
        score = result.find("score-pairs")
        if score.has_attr("audiencescore"):
            ascore = score["audiencescore"]
        if score.has_attr("audiencesentiment"):
            asentiment = score["audiencesentiment"]
        if score.has_attr("criticsscore"):
            cscore = score["criticsscore"]
        if score.has_attr("criticsentiment"):
            csentiment = score["criticsentiment"]

        title = result.find("span", class_="p--small")
        print("\t\t{}\t\t".format(title.text))
        print("Critic Score: {} \t Critic Sentiment: {}".format(cscore, csentiment))
        print("Audience Score: {} \t Audience Sentiment: {}".format(ascore, asentiment))

