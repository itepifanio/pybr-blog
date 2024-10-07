AUTHOR = 'Associação Python Brasil'
SITENAME = 'Blog da Python Brasil'
SITEURL = ""

PATH = "content"

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = 'pt'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

PLUGINS = ["photos"]
PHOTO_LIBRARY = "content/images/posts"
PHOTO_ARTICLE = (760, 506, 95)
PHOTO_THUMB = (384, 288, 95)

PHOTO_DEFAULT_IMAGE_OPTIONS = {
	"jpeg": {
		"optimize": False
	}
}

THEME='theme'

# Blogroll
LINKS = (
    ('pythonbrasil.org.br', 'https://pythonbrasil.org.br'),
    ('python.org.br', 'https://python.org.br'),
    ('facebook', 'https://www.facebook.com/pythonbrasil'),
    ('twitter', 'https://twitter.com/pythonbrasil'),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
