#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Sangeeta Jadoonanan'
SITENAME = 'Test Site'
SITEURL = 'http://localhost:8000'

USER_LOGO_URL = SITEURL + '/images/panda.png'

TAGLINE = 'Software Engineer. Forex Trader. Loves Automation. Vegan. Dreamer.'

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),)

# Social widget
SOCIAL = (('Github', 'http://github.com/sjbitcode'),
          ('Twitter', 'http://twitter.com/sjbitcode'),)

DEFAULT_PAGINATION = 5

THEME = 'pelican-themes/pelican-svbhack'

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
