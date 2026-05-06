---
aid: soax
name: SOAX
description: SOAX provides enterprise-grade proxy infrastructure and web data extraction APIs for developers and data teams. With 155M+ residential IPs, 33M+ mobile IPs, and 300K+ datacenter IPs across 195+ countries, SOAX enables web scraping, CAPTCHA bypass, geo-targeted data collection, and anti-bot circumvention at scale. The Web Data API handles JavaScript rendering, session management, and headless browser automation automatically.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Proxy
  - Web Scraping
  - Residential Proxies
  - Mobile Proxies
  - Datacenter Proxies
  - Data Extraction
  - Anti-Bot Bypass
url: https://raw.githubusercontent.com/api-evangelist/soax/refs/heads/main/apis.yml
created: '2025-02-21'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: soax:soax-web-data-api
    name: SOAX Web Data API
    description: The SOAX Web Data API extracts fully rendered HTML, screenshots, XHR responses, and structured data from any public website. It handles JavaScript rendering, CAPTCHA solving, fingerprinting, headless browsers, and anti-bot bypass automatically.
    humanURL: https://soax.com/web-data-api
    tags:
      - Web Scraping
      - Data Extraction
      - Anti-Bot Bypass
      - JavaScript Rendering
    properties:
      - type: Documentation
        url: https://docs.soax.com/
      - type: Getting Started
        url: https://helpcenter.soax.com/en/articles/11297318-getting-started-with-soax-web-data-api
      - type: OpenAPI
        url: openapi/soax-web-data-api-openapi.yml
      - type: JSON Schema
        url: json-schema/soax-fetch-request-schema.json
      - type: JSON Structure
        url: json-structure/soax-fetch-request-structure.json
  - aid: soax:soax-proxy-management-api
    name: SOAX Proxy Management API
    description: The SOAX Proxy Management API enables programmatic control of proxy packages including IP whitelisting, endpoint generation, and proxy configuration for residential, mobile, and datacenter proxy pools.
    humanURL: https://soax.com/proxies
    tags:
      - Proxy Management
      - Whitelist
      - IP Rotation
      - Residential Proxies
    properties:
      - type: Documentation
        url: https://helpcenter.soax.com/en/collections/3470979-api
      - type: OpenAPI
        url: openapi/soax-proxy-management-api-openapi.yml
common:
  - type: Website
    url: https://soax.com/
  - type: Documentation
    url: https://docs.soax.com/
  - type: Help Center
    url: https://helpcenter.soax.com/
  - type: Pricing
    url: https://soax.com/pricing
  - type: Sign Up
    url: https://soax.com/get-started
  - type: Blog
    url: https://soax.com/blog/
  - type: Spectral Rules
    url: rules/soax-rules.yml
  - type: Capabilities
    url: capabilities/data-collection.yaml
  - type: Vocabulary
    url: vocabulary/soax-vocabulary.yml
  - type: JSON-LD Context
    url: json-ld/soax-context.jsonld
  - type: Examples
    url: examples/soax-fetch-content-example.json
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
