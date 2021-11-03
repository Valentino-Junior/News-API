class News:
    '''
    News class to define News Objects
    '''
    def __init__(self, urlToImage,title,description, url, publishedAt):
        self.urlToImage = urlToImage
        self.title = title
        self.description = description
        self.url = url
        self.publishedAt= publishedAt