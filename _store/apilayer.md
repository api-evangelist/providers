---
aid: apilayer
name: APILayer
description: APILayer is an API marketplace and hub that enables developers to discover, integrate, and build with high-quality, reliable API services. The platform hosts 100+ APIs across categories including geolocation, currency, weather, dev tools, marketing, finance, security, and AI/ML, serving 445,000+ developers with 30 million+ API calls monthly.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - API Catalog
  - API Discovery
  - API Marketplace
  - Developer Tools
  - SaaS APIs
url: https://raw.githubusercontent.com/api-evangelist/apilayer/refs/heads/main/apis.yml
created: '2025-03-01'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: apilayer:apilayer-api
    name: APILayer Marketplace API
    description: The APILayer Marketplace API provides access to 100+ APIs across geolocation, currency, weather, dev tools, marketing, finance, security, and AI/ML categories. Individual APIs include IPstack, Fixer, Currencylayer, Weatherstack, Serpstack, Mediastack, and many more, each with their own endpoints and authentication.
    humanURL: https://apilayer.com/
    baseURL: https://api.apilayer.com
    tags:
      - API Marketplace
      - Currency
      - Geolocation
      - Weather
    properties:
      - type: Documentation
        url: https://apilayer.com/
      - type: Pricing
        url: https://apilayer.com/pricing
      - type: JSONSchema
        url: json-schema/apilayer-api-schema.json
      - type: JSON-LD
        url: json-ld/apilayer-context.jsonld
common:
  - type: Website
    url: https://apilayer.com/
  - type: Documentation
    url: https://apilayer.com/
  - type: Pricing
    url: https://apilayer.com/pricing
  - type: SignUp
    url: https://apilayer.com/signup
  - type: Login
    url: https://apilayer.com/login
  - type: Blog
    url: https://blog.apilayer.com/
  - type: Features
    data:
      - name: API Marketplace
        description: Browse and integrate 100+ high-quality APIs across categories including geolocation, currency, weather, dev tools, and more.
      - name: Unified Authentication
        description: Single API key management across multiple APIs from the APILayer platform.
      - name: Low Latency Infrastructure
        description: High-performance, reliable API infrastructure with global CDN for low-latency responses.
      - name: Developer Dashboard
        description: Centralized dashboard to manage API subscriptions, monitor usage, and access documentation.
      - name: Usage Analytics
        description: Real-time usage tracking and analytics across all subscribed APIs.
  - type: UseCases
    data:
      - name: IP Geolocation
        description: Determine user location, timezone, and geographic data from IP addresses using IPstack or IPapi.
      - name: Currency Conversion
        description: Access real-time and historical currency exchange rates using Fixer or Currencylayer APIs.
      - name: Weather Data
        description: Integrate real-time weather forecasts and historical weather data using Weatherstack.
      - name: Search Engine Data
        description: Scrape search engine results programmatically using the Serpstack API.
      - name: Phone Validation
        description: Validate and look up phone number details globally using Numverify.
  - type: Integrations
    data:
      - name: IPstack
        description: IP geolocation API for geographic profiling and location intelligence.
      - name: Fixer
        description: Real-time and historical currency exchange rate data API.
      - name: Weatherstack
        description: Real-time weather data and forecasting API.
      - name: Serpstack
        description: Search engine results page scraping and SERP data API.
      - name: Mediastack
        description: Live and historical news data API for media monitoring.
      - name: Numverify
        description: Global phone number validation and carrier lookup API.
      - name: Coinlayer
        description: Real-time cryptocurrency exchange rate data API.
      - name: Pdflayer
        description: HTML to PDF conversion and document generation API.
  - type: Solutions
    data:
      - name: Free Plan
        description: Limited free tier for each API to explore and prototype integrations.
      - name: Basic Plan
        description: Entry-level paid plan with increased request limits for individual APIs.
      - name: Professional Plan
        description: Higher volume plans for production applications requiring reliable API access.
      - name: Enterprise Plan
        description: Custom volume and SLA guarantees for enterprise-scale API consumption.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
---
