---
aid: scrapingbee
url: https://raw.githubusercontent.com/api-evangelist/scrapingbee/refs/heads/main/apis.yml
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
name: ScrapingBee
tags:
- Data Aggregation
- Data Extraction
- Headless Browser
- Proxy Rotation
- Web Scraping
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: ScrapingBee is a web scraping API that handles headless browsers, proxy rotation, and CAPTCHAs so developers can extract data from any website with a single API call. Features include JavaScript rendering, AI-powered data extraction, and screenshot capabilities.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

