import os
import json

class Config:
    def __init__(self, working_dir):
        self.searchTags = ["panties"]
        self.width = "1920"
        self.height = "1080"
        self.rating = "safe"
        self.downloadFolder = "downloads"
        self.removeOld = True

        if os.path.exists(os.path.join(working_dir, "config.json")):
            with open(os.path.join(working_dir, "config.json")) as file:
                self.__dict__ = json.load(file)
        else:
            with open(os.path.join(working_dir, "config.json"), 'w') as file:
                json.dump(self.__dict__, file, indent=4)

    def toJSON(self):
        return json.dumps(self, default=lambda a: a.__dict__, sort_keys=False, indent=4)

    def saveConfig(self, working_dir):
        if not os.path.exists(os.path.join(working_dir, "config.json")):
            with open(os.path.join(working_dir, "config.json"), 'w') as file:
                json.dump(self.__dict__, file, indent=4)

    def getSearchTags(self):
        return self.searchTags

    def getDimensions(self):
        return (self.width, self.height)

    def getDimension(self, dimension):
        if dimension == "width":
            return self.width
        elif dimension == "height":
            return self.height
        return None

    def getRating(self):
        return self.rating

    def getDownloadFolder(self):
        return self.downloadFolder

    def getRemoveOld(self):
        return self.removeOld