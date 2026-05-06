---
aid: apify
name: Apify
description: Apify is a full-stack web scraping and browser automation platform that enables developers to build, run, and scale web scrapers, crawlers, and data extraction tools using a cloud-based infrastructure with built-in proxy management, scheduling, and storage. The platform hosts thousands of ready-made Actors for scraping social media, search engines, maps, e-commerce sites, and more.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Actors
  - Browser Automation
  - Crawling
  - Data Aggregation
  - Data Extraction
  - Web Automation
  - Web Scraping
url: https://raw.githubusercontent.com/api-evangelist/apify/refs/heads/main/apis.yml
created: '2026-03-26'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: apify:apify-api
    name: Apify API
    description: 'The Apify REST API (v2) provides programmatic access to the Apify platform, allowing you to manage actors, run scraping tasks, access datasets, key-value stores, and request queues. Authentication uses Bearer tokens. Rate limits: 250,000 requests/minute globally, 60-400 requests/second per resource.'
    humanURL: https://apify.com
    baseURL: https://api.apify.com/v2
    tags:
      - Actors
      - Automation
      - Crawling
      - Data Extraction
      - Datasets
      - Web Scraping
    properties:
      - type: Documentation
        url: https://docs.apify.com/api/v2
      - type: OpenAPI
        url: openapi/apify-api.yaml
      - type: GettingStarted
        url: https://docs.apify.com/api/v2/getting-started
      - type: Authentication
        url: https://docs.apify.com/api/v2#authentication
      - type: RateLimits
        url: https://docs.apify.com/api/v2#rate-limiting-and-scaling
      - type: JSONSchema
        url: json-schema/apify-actor-schema.json
      - type: JSONSchema
        url: json-schema/apify-run-schema.json
      - type: JSONSchema
        url: json-schema/apify-dataset-schema.json
      - type: JSONSchema
        url: json-schema/apify-key-value-store-schema.json
      - type: JSON-LD
        url: json-ld/apify-context.jsonld
      - type: SDK
        url: https://www.npmjs.com/package/apify-client
        title: Node.js Client
      - type: SDK
        url: https://pypi.org/project/apify-client/
        title: Python Client
common:
  - type: Website
    url: https://apify.com
  - type: Documentation
    url: https://docs.apify.com
  - type: GettingStarted
    url: https://docs.apify.com/api/v2/getting-started
  - type: Pricing
    url: https://apify.com/pricing
  - type: Blog
    url: https://blog.apify.com
  - type: SignUp
    url: https://console.apify.com/sign-up
  - type: Login
    url: https://console.apify.com/sign-in
  - type: Academy
    url: https://docs.apify.com/academy
  - type: Support
    url: https://help.apify.com
  - type: GitHubOrganization
    url: https://github.com/apify
  - type: CLI
    url: https://www.npmjs.com/package/apify-cli
  - type: Features
    data:
      - name: Actors Marketplace
        description: Store of thousands of pre-built web scrapers and automation tools ready to run with zero configuration.
      - name: Cloud Infrastructure
        description: Run Actors on Apify's scalable cloud infrastructure with built-in proxy rotation, scheduling, and storage.
      - name: Datasets
        description: Structured storage for Actor output with multi-format export (JSON, CSV, XML, XLSX, etc.).
      - name: Key-Value Stores
        description: Persistent key-value storage for arbitrary data including files, screenshots, and configuration.
      - name: Request Queues
        description: URL queue management for large-scale distributed web crawling.
      - name: Proxy Management
        description: Built-in datacenter and residential proxy pools with automatic rotation.
      - name: Scheduled Runs
        description: Schedule Actors to run automatically on cron schedules.
      - name: MCP Server
        description: Apify MCP server enabling AI agents to use thousands of web scraping and automation tools.
  - type: UseCases
    data:
      - name: AI Training Data Collection
        description: Extract structured data from websites for LLM training datasets, RAG pipelines, and AI applications.
      - name: E-commerce Price Monitoring
        description: Scrape product prices, availability, and reviews from e-commerce websites for competitive intelligence.
      - name: Social Media Data Extraction
        description: Extract posts, profiles, and engagement data from social media platforms.
      - name: Search Engine Data
        description: Scrape search engine results, SERP data, and web listings for SEO and market research.
      - name: Lead Generation
        description: Extract business data from directories, LinkedIn, and other professional platforms.
  - type: Integrations
    data:
      - name: Crawlee
        description: Open-source web crawling library for Node.js and Python built by Apify.
      - name: Zapier
        description: Zapier integration for connecting Apify Actors with 5000+ apps.
      - name: Make (Integromat)
        description: No-code automation platform integration for Apify.
      - name: LangChain
        description: LangChain integration for using Apify data loaders in AI applications.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
