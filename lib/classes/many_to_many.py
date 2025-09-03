class Article:

    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        author.all_articles.append(self)
        magazine.all_articles.append(self)
        if magazine not in author.all_magazines:
            author.all_magazines.append(magazine)
        if author not in magazine.all_authors:
            magazine.all_authors.append(author)
        Article.all.append(self)

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, author):
        if isinstance(author, Author):
            self._author = author
        else:
            print('Author must be an instance of the Author class')

    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, magazine):
        if isinstance(magazine, Magazine):
            self._magazine = magazine
        else:
            print('Magazine must be an instance of the Magazine class')
        
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if type(title) is str and len(title) in range(5, 50, 1):
            self._title = title
        else:
            print('Title must be a string between 5-50 characters')

class Author:

    def __init__(self, name, all_articles = None, all_magazines = None):
        self.name = name
        self.all_articles = []
        self.all_magazines = []

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not hasattr(self, 'name') and type(name) is str and len(name) > 0:
            self._name = name
        else:
            print('no no no girl')

    def articles(self):
        return self.all_articles

    def magazines(self):
        return self.all_magazines

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        if self.articles():
            categories = []
            for magazine in self.all_magazines:
                if magazine.category not in categories:
                    categories.append(magazine.category)
            return categories
        else:
            return None

class Magazine:
    def __init__(self, name, category, all_articles = None, all_authors = None):
        self.name = name
        self.category = category
        self.all_articles = []
        self.all_authors = []

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if type(name) is str and len(name) in range(2, 16, 1):
            self._name = name
        else:
            print('Name must be a string between 2-16 characters')

    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, category):
        if type(category) is str and len(category) > 0:
            self._category = category
        else:
            print('Category must be a string longer than 0 characters')

    def articles(self):
        return self.all_articles

    def contributors(self):
        return self.all_authors

    def article_titles(self):
        if self.all_articles:
            return [article.title for article in self.all_articles]
        else:
            return None

    def contributing_authors(self):
        all_authors = [article.author for article in self.articles()]
        concise_all_authors = []
        for author in all_authors:
            if all_authors.count(author) >= 2:
                concise_all_authors.append(author)
        if concise_all_authors:
            return concise_all_authors
        else:
            return None