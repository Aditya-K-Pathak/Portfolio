import json
from datetime import datetime
from django.shortcuts import render

class GetData:
    def __init__(self) -> None:
        with open("static/data/data.json", "r") as file:
            self.data = file.read()
            self.data = json.loads(self.data)
            self.update_visitors()

    def update_visitors(self) -> bool:
        self.data["Visitors"] += 1
        with open("static/data/data.json", "w") as file:
            json.dump(self.data, file, indent=4)
        return True

    def get_home(self) -> dict:
        self.update_visitors()
        logger.write_logbook("Home")
        return dict(self.data)

    def get_patents(self) -> dict:
        self.update_visitors()
        logger.write_logbook("Patents")
        return dict(self.data)

    def get_awards(self) -> dict:
        self.update_visitors()
        logger.write_logbook("Awards")
        return dict(self.data)

    def get_projects(self) -> dict:
        self.update_visitors()
        logger.write_logbook("Projects")
        return dict(self.data)

    def get_research(self) -> dict:
        self.update_visitors()
        logger.write_logbook("Research")
        return dict(self.data)

class logger:
    def write_logbook(page):
        with open("static/data/logs.log", "a") as log:
            log.write(str(datetime.now()) + " | " + page)
        return True

webdata = GetData()
def index(request):
    return render(request, "index.html", webdata.get_home())

def projects(requests):
    return render(requests, "projects.html", webdata.get_projects())

def patents(requests):
    return render(requests, "patents.html", webdata.get_patents())

def research(requests):
    return render(requests, "research.html", webdata.get_research())

def awards(requests):
    return render(requests, "awards.html", webdata.get_awards())

def sitemap(requests):
    return render(requests, "sitemap.xml")
