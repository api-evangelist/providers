---
aid: crawlee
name: Crawlee
x-type: opensource
description: Crawlee is an open-source web scraping and crawling library maintained by Apify, providing a unified set of crawler classes, request queues, datasets, and key-value stores for building reliable scrapers. It is available for both JavaScript/TypeScript (Node.js) and Python, offering HTTP, Cheerio, JSDOM, LinkeDOM, Puppeteer, Playwright, and Stagehand crawler implementations along with proxy and session management utilities for production-grade scraping.
url: https://raw.githubusercontent.com/api-evangelist/crawlee/refs/heads/main/apis.yml
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Apache 2.0
  - Apify
  - Browser Automation
  - Crawlers
  - Harvesting
  - JavaScript
  - Node.js
  - Open Source
  - Playwright
  - Puppeteer
  - Python
  - Scraping
  - Web
created: '2025-02-08'
modified: '2026-04-28'
specificationVersion: '0.20'
type: Index
access: Public
position: Provider
apis:
  - aid: crawlee:crawlee-javascript-sdk
    name: Crawlee JavaScript SDK
    description: The Crawlee JavaScript SDK is a Node.js/TypeScript library for building reliable web scrapers and crawlers. It provides a family of crawler classes - BasicCrawler, HttpCrawler, CheerioCrawler, JSDOMCrawler, LinkeDOMCrawler, PuppeteerCrawler, PlaywrightCrawler, and AdaptivePlaywrightCrawler - along with shared infrastructure for AutoscaledPool resource management, proxy rotation, session pooling, RequestQueue task queuing, Dataset result storage, and KeyValueStore unstructured data persistence. Crawlee handles retries, error recovery, request fingerprinting, and statistics tracking out of the box, allowing developers to focus on extraction logic.
    humanURL: https://crawlee.dev/js
    properties:
      - type: Documentation
        url: https://crawlee.dev/js
      - type: Reference
        url: https://crawlee.dev/js/api
      - type: GettingStarted
        url: https://crawlee.dev/js/docs/quick-start
      - type: GitHubRepository
        url: https://github.com/apify/crawlee
      - type: NpmPackage
        url: https://www.npmjs.com/package/crawlee
    tags:
      - Browser Automation
      - Cheerio
      - JavaScript
      - Node.js
      - Playwright
      - Puppeteer
      - Scraping
      - TypeScript
  - aid: crawlee:crawlee-python-sdk
    name: Crawlee Python SDK
    description: The Crawlee Python SDK is a Python library for building reliable web scrapers and crawlers. It offers BasicCrawler, HttpCrawler, BeautifulSoupCrawler, ParselCrawler, PlaywrightCrawler, and Adaptive crawlers built on top of asyncio, along with shared infrastructure for proxy rotation, session pooling, RequestQueue, Dataset, and KeyValueStore. The Python SDK targets data engineers and Python developers who want the same crawler ergonomics as the JavaScript version but inside the Python ecosystem.
    humanURL: https://crawlee.dev/python
    properties:
      - type: Documentation
        url: https://crawlee.dev/python
      - type: Reference
        url: https://crawlee.dev/python/api
      - type: GettingStarted
        url: https://crawlee.dev/python/docs/quick-start
      - type: GitHubRepository
        url: https://github.com/apify/crawlee-python
      - type: PyPiPackage
        url: https://pypi.org/project/crawlee/
    tags:
      - Asyncio
      - BeautifulSoup
      - Browser Automation
      - Parsel
      - Playwright
      - Python
      - Scraping
common:
  - type: Website
    url: https://crawlee.dev/
  - type: Documentation
    url: https://crawlee.dev/
  - type: GitHubOrganization
    url: https://github.com/apify
  - type: GitHubRepository
    url: https://github.com/apify/crawlee
  - type: Blog
    url: https://crawlee.dev/blog
  - type: ChangeLog
    url: https://github.com/apify/crawlee/releases
  - type: Discord
    url: https://discord.gg/jyEM2PRvMU
  - type: Community
    url: https://crawlee.dev/discord
  - type: License
    url: https://github.com/apify/crawlee/blob/master/LICENSE.md
  - type: Apify
    url: https://apify.com/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
