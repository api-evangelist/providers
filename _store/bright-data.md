---
aid: bright-data
name: Bright Data
description: Bright Data is an all-in-one web data platform providing proxy networks, scraping browser automation, web scraper APIs, and dataset delivery services for large-scale web data collection and aggregation.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Browser Automation
  - Data Aggregation
  - Data Collection
  - Proxy
  - Web Scraping
url: https://raw.githubusercontent.com/api-evangelist/bright-data/refs/heads/main/apis.yml
created: '2026-03-26'
modified: '2026-03-26'
specificationVersion: '0.19'
apis:
  - aid: bright-data:web-scraper-api
    name: Bright Data Web Scraper API
    description: The Web Scraper API provides structured data extraction from websites with built-in proxy rotation, JavaScript rendering, CAPTCHA solving, and anti-bot bypass. Supports bulk request handling, data discovery, and automated validation backed by residential proxies.
    humanURL: https://brightdata.com/products/web-scraper
    tags:
      - Data Extraction
      - Structured Data
      - Web Scraping
    properties:
      - type: Documentation
        url: https://docs.brightdata.com
  - aid: bright-data:scraping-browser-api
    name: Bright Data Scraping Browser API
    description: The Scraping Browser API provides fully managed cloud browsers for browser-based data collection workflows requiring full page rendering, user-like interactions, and advanced unblocking. Integrates with Selenium, Puppeteer, and Playwright.
    humanURL: https://brightdata.com/products/scraping-browser
    tags:
      - Browser Automation
      - Headless Browser
      - Scraping
    properties:
      - type: Documentation
        url: https://docs.brightdata.com/scraping-automation/scraping-browser/introduction
  - aid: bright-data:proxy-api
    name: Bright Data Proxy API
    description: The Proxy API allows you to programmatically interact with and control Bright Data proxy networks including datacenter, residential, ISP, and mobile proxies. Automate creating, updating, and managing proxy ports and configurations.
    humanURL: https://brightdata.com/products/proxy-api
    tags:
      - Datacenter Proxy
      - Proxy
      - Residential Proxy
    properties:
      - type: Documentation
        url: https://docs.brightdata.com
common:
  - type: Website
    url: https://brightdata.com
  - type: Documentation
    url: https://docs.brightdata.com
  - type: Pricing
    url: https://brightdata.com/pricing/web-unlocker
  - type: Sign Up
    url: https://brightdata.com/cp/start
  - type: Login
    url: https://brightdata.com/cp/zones
  - type: Blog
    url: https://brightdata.com/blog
  - type: GitHub Organization
    url: https://github.com/luminati-io
  - type: Python SDK
    url: https://github.com/brightdata/sdk-python
  - type: JavaScript SDK
    url: https://github.com/brightdata/bright-data-sdk-js
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
