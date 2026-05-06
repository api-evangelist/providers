---
aid: scrapfly
name: Scrapfly
description: 'Scrapfly is a web scraping API platform that enables effortless collection of web data with battle-tested APIs that scale. It provides capabilities for scraping web pages, capturing screenshots, and extracting structured data with AI assistance to handle anti-bot measures and JavaScript rendering. One API key unlocks five APIs: Web Scraping (anti-bot unblocker), Cloud Browser (CDP), Screenshot, Extraction, and Crawler. Scrapfly operates globally with proxies across 190+ countries.'
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AI
  - Data Extraction
  - Screenshots
  - Web Scraping
  - Proxies
  - Browser Automation
created: '2025-02-08'
modified: '2026-05-02'
url: https://raw.githubusercontent.com/api-evangelist/scrapfly/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: scrapfly:scrape-api
    name: Scrapfly Scrape API
    description: The core web scraping API that fetches any URL with anti-bot bypass, proxy rotation, and JavaScript rendering. Supports GET, POST, PUT, PATCH, HEAD, and OPTIONS methods. Returns clean HTML, markdown, JSON, or raw content. Features include session management, caching, custom headers, DNS customization, SSL info retrieval, webhooks, and structured data extraction with LLM assistance.
    humanURL: https://scrapfly.io/docs/scrape-api/getting-started
    tags:
      - Web Scraping
      - Anti-Bot
      - Proxies
      - JavaScript Rendering
    properties:
      - type: Documentation
        url: https://scrapfly.io/docs/scrape-api
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/scrapfly/refs/heads/main/openapi/scrapfly-scrape-openapi.yml
      - type: SpectralRules
        url: https://raw.githubusercontent.com/api-evangelist/scrapfly/refs/heads/main/rules/scrapfly-rules.yml
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/scrapfly/refs/heads/main/json-schema/scrapfly-scrape-response-schema.json
      - type: JSONLDContext
        url: https://raw.githubusercontent.com/api-evangelist/scrapfly/refs/heads/main/json-ld/scrapfly-context.jsonld
  - aid: scrapfly:screenshot-api
    name: Scrapfly Screenshot API
    description: Capture screenshots of web pages with full-page or element-specific capture using CSS selectors. Supports JavaScript rendering, viewport configuration, and screenshot of dynamic content. The base URL for screenshots is https://api.scrapfly.io/screenshot.
    humanURL: https://scrapfly.io/docs/screenshot-api/getting-started
    tags:
      - Screenshots
      - Web Scraping
      - Browser Automation
    properties:
      - type: Documentation
        url: https://scrapfly.io/docs/screenshot-api/getting-started
  - aid: scrapfly:extraction-api
    name: Scrapfly Extraction API
    description: AI-powered structured data extraction from HTML content. Supports template-based extraction, LLM prompt-driven extraction, and auto-extraction using predefined models for common content types.
    humanURL: https://scrapfly.io/docs/scrape-api/extraction
    tags:
      - Data Extraction
      - AI
      - Structured Data
    properties:
      - type: Documentation
        url: https://scrapfly.io/docs/scrape-api/extraction
  - aid: scrapfly:crawler-api
    name: Scrapfly Crawler API
    description: Web crawling API (currently in early access) that enables crawling entire websites with advanced configuration for depth control and content filtering. Outputs in WARC format for comprehensive web archive support.
    humanURL: https://scrapfly.io/docs
    tags:
      - Web Crawling
      - Data Collection
      - WARC
    properties:
      - type: Documentation
        url: https://scrapfly.io/docs
  - aid: scrapfly:cloud-browser-api
    name: Scrapfly Cloud Browser API
    description: Headless browser automation API (currently in beta) compatible with Playwright, Puppeteer, and Selenium frameworks. Enables complex browser interactions, JavaScript execution, and file download capture.
    humanURL: https://scrapfly.io/docs
    tags:
      - Browser Automation
      - Playwright
      - Puppeteer
      - Selenium
    properties:
      - type: Documentation
        url: https://scrapfly.io/docs
  - aid: scrapfly:sdks
    name: Scrapfly SDKs
    description: Official SDKs for Python, TypeScript, Go, Rust, and Scrapy with full feature coverage across every language including scrape, screenshot, extract, and crawl capabilities.
    humanURL: https://scrapfly.io/docs/sdk
    tags:
      - SDK
      - Python
      - TypeScript
      - Go
      - Rust
    properties:
      - type: Documentation
        url: https://scrapfly.io/docs/sdk
      - type: PythonSDK
        url: https://scrapfly.io/docs/sdk/python
      - type: GitHubOrg
        url: https://github.com/scrapfly
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
