import random

class API:
    def __init__(self, config):
        self.url = "https://konachan.com/post.json?limit=1&"
        self.tags = ["tags=order:random"]

        if config.getSearchTags() is not None and len(config.getSearchTags()):
            self.tags.append(random.choice(config.getSearchTags()))

        if config.getDimensions() is not None:
            self.tags.append(f"width:{config.getDimensions()[0]}")
            self.tags.append(f"height:{config.getDimensions()[1]}")

        if config.getRating() is not None:
            self.tags.append(f"rating:{config.getRating()}")
        
        self.url += "+".join(self.tags)

    def getURL(self):
        return self.url