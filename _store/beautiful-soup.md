---
aid: beautiful-soup
name: Beautiful Soup
description: Beautiful Soup is a Python library for pulling data out of HTML and XML files, widely used for web scraping and screen scraping tasks. It provides a parse tree API with simple methods for navigating, searching, and modifying parsed HTML/XML documents. Beautiful Soup automatically handles encoding, supports multiple parsers (html.parser, lxml, html5lib), and integrates with CSS selectors via the Soup Sieve library. Current stable version is 4.14.3.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Data Extraction
  - HTML Parsing
  - Python
  - Scraping
  - Web Scraping
  - XML Parsing
url: https://raw.githubusercontent.com/api-evangelist/beautiful-soup/refs/heads/main/apis.yml
created: '2026-03-29'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: beautiful-soup:beautiful-soup
    name: Beautiful Soup
    description: Beautiful Soup 4 is a Python library providing a parse tree API for HTML and XML documents. It exposes Tag, NavigableString, BeautifulSoup, and Comment objects with navigation methods (find, find_all, CSS selectors), tree traversal (parents, children, siblings), and modification methods (append, extract, replace). Supports html.parser, lxml, and html5lib parsers with automatic encoding detection.
    humanURL: https://www.crummy.com/software/BeautifulSoup/
    tags:
      - Data Extraction
      - HTML Parsing
      - Python
      - Scraping
      - Web Scraping
      - XML Parsing
    properties:
      - type: Documentation
        url: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
      - type: GettingStarted
        url: https://www.crummy.com/software/BeautifulSoup/bs4/doc/#quick-start
      - type: SDK
        url: https://pypi.org/project/beautifulsoup4/
        title: Python Package (PyPI)
common:
  - type: Website
    url: https://www.crummy.com/software/BeautifulSoup/
  - type: Documentation
    url: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
  - type: SDK
    url: https://pypi.org/project/beautifulsoup4/
    title: PyPI Package
  - type: GitHubOrganization
    url: https://bazaar.launchpad.net/~leonardr/beautifulsoup/bs4
  - type: Changelog
    url: https://bazaar.launchpad.net/~leonardr/beautifulsoup/bs4/view/head:/CHANGELOG
  - type: Features
    data:
      - name: Multi-Parser Support
        description: Supports html.parser (built-in), lxml (fast), and html5lib (browser-like) parsers for flexible HTML/XML parsing.
      - name: CSS Selector Support
        description: Full CSS4 selector support via the Soup Sieve library for familiar CSS-based element selection.
      - name: Tree Navigation API
        description: Rich API for navigating the parse tree upward, downward, and sideways including find(), find_all(), parents, children, and siblings.
      - name: Automatic Encoding Detection
        description: Automatically detects and handles document encoding using Unicode, Dammit, ensuring correct text extraction.
      - name: Tree Modification
        description: Full tree modification support including append, insert, extract, decompose, replace_with, wrap, and unwrap operations.
      - name: Output Formatting
        description: Multiple output formatters including prettify(), get_text(), and custom formatters for controlled serialization.
  - type: UseCases
    data:
      - name: Web Scraping
        description: Extract data from websites by parsing HTML pages with Beautiful Soup and navigating the DOM tree to find target elements.
      - name: Data Mining
        description: Mine structured data from HTML tables, lists, and other markup patterns across large numbers of web pages.
      - name: Content Extraction
        description: Extract article text, product information, or other content from web pages for NLP pipelines and data analysis.
      - name: Screen Scraping Legacy Systems
        description: Automate data extraction from legacy HTML web interfaces that lack modern APIs.
      - name: HTML Sanitization
        description: Parse and clean HTML documents by removing unwanted tags, scripts, and formatting.
      - name: XML Processing
        description: Parse and query XML documents using Beautiful Soup's tree navigation and search capabilities.
  - type: Integrations
    data:
      - name: Requests
        description: Python HTTP library used in combination with Beautiful Soup to fetch and parse web pages.
      - name: Scrapy
        description: Python web crawling framework that can use Beautiful Soup selectors for content extraction.
      - name: lxml
        description: Fast XML and HTML parsing library used as an alternate parser backend for Beautiful Soup.
      - name: html5lib
        description: Pure-Python HTML5 parser used with Beautiful Soup for browser-compatible HTML parsing.
      - name: Pandas
        description: DataFrame library commonly used with Beautiful Soup to convert scraped HTML tables into structured data.
      - name: Selenium
        description: Browser automation tool used with Beautiful Soup to scrape JavaScript-rendered pages.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
