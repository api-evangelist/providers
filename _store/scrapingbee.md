---
aid: scrapingbee
name: ScrapingBee
description: ScrapingBee is a web scraping API that handles headless browsers, proxy rotation, and CAPTCHAs so developers can extract data from any website with a single API call. Features include JavaScript rendering, AI-powered data extraction, and screenshot capabilities.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Data Aggregation
  - Data Extraction
  - Headless Browser
  - Proxy Rotation
  - Web Scraping
url: https://raw.githubusercontent.com/api-evangelist/scrapingbee/refs/heads/main/apis.yml
created: '2026-03-26'
modified: '2026-03-26'
specificationVersion: '0.19'
apis:
  - aid: scrapingbee:html-api
    name: ScrapingBee HTML API
    description: The HTML API extracts rendered HTML from any website using headless browsers with automatic proxy rotation. Supports JavaScript rendering (costs 5 credits per request), custom wait times, CSS selectors, and request headers. Returns full page HTML ready for parsing.
    humanURL: https://www.scrapingbee.com
    baseURL: https://app.scrapingbee.com/api/v1
    tags:
      - HTML Extraction
      - JavaScript Rendering
      - Web Scraping
    properties:
      - type: Documentation
        url: https://www.scrapingbee.com/documentation/
  - aid: scrapingbee:data-extraction-api
    name: ScrapingBee Data Extraction API
    description: The Data Extraction API allows you to add extraction rules to API calls to extract structured data from pages without parsing HTML on your side. Supports CSS selectors and AI-powered extraction where you describe what you need in plain English.
    humanURL: https://www.scrapingbee.com/features/data-extraction/
    baseURL: https://app.scrapingbee.com/api/v1
    tags:
      - AI Extraction
      - Data Extraction
      - Structured Data
    properties:
      - type: Documentation
        url: https://www.scrapingbee.com/documentation/data-extraction/
  - aid: scrapingbee:ai-extraction-api
    name: ScrapingBee AI Web Scraping API
    description: The AI Web Scraping API leverages artificial intelligence to extract the right content from web pages by expressing what you need in plain English, without requiring CSS selectors or complex parsing logic.
    humanURL: https://www.scrapingbee.com/features/ai-web-scraping-api/
    baseURL: https://app.scrapingbee.com/api/v1
    tags:
      - AI
      - Data Extraction
      - Natural Language
    properties:
      - type: Documentation
        url: https://www.scrapingbee.com/documentation/
common:
  - type: Website
    url: https://www.scrapingbee.com
  - type: Documentation
    url: https://www.scrapingbee.com/documentation/
  - type: Pricing
    url: https://www.scrapingbee.com/pricing/
  - type: Blog
    url: https://www.scrapingbee.com/blog/
  - type: Sign Up
    url: https://app.scrapingbee.com/account/register
  - type: Login
    url: https://app.scrapingbee.com/account/login
  - type: Support
    url: https://help.scrapingbee.com
  - type: GitHub Organization
    url: https://github.com/ScrapingBee
  - type: Python SDK
    url: https://github.com/ScrapingBee/scrapingbee-python
  - type: Node.js SDK
    url: https://github.com/ScrapingBee/scrapingbee-node
  - type: Postman Collection
    url: https://www.postman.com/api-evangelist/scraping/documentation/ygpc6xm/scrapingbee
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
