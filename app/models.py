class News:
    '''
    News class to define News Objects
    '''
    def __init__(self,title,description,urlToImage,content,publishedAt):
        self.title = title
        self.description = description
        self.urlToImage = urlToImage
        self.content = content
        self.publishedAt= publishedAt