---
aid: google-ads
name: Google Ads
description: The Google Ads API is the modern programmatic interface to Google Ads and the next generation of the AdWords API. It enables developers to interact directly with the Google Ads platform, vastly increasing the efficiency of managing large or complex Google Ads accounts and campaigns.
type: Index
image: https://www.gstatic.com/images/branding/product/1x/google_ads_64dp.png
url: https://raw.githubusercontent.com/api-evangelist/google-ads/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-28'
specificationVersion: '0.19'
tags:
  - Advertising
  - Campaign Management
  - Digital Advertising
  - Google
  - Marketing
  - PPC
apis:
  - aid: google-ads:google-ads-api
    name: Google Ads API
    description: RESTful API for managing Google Ads campaigns, ad groups, ads, keywords, and more.
    image: https://www.gstatic.com/images/branding/product/1x/google_ads_64dp.png
    humanURL: https://developers.google.com/google-ads/api
    baseURL: https://googleads.googleapis.com
    tags:
      - Advertising
      - Analytics
      - Campaigns
      - Marketing
      - PPC
    properties:
      - type: Documentation
        url: https://developers.google.com/google-ads/api/docs/start
      - type: OpenAPI
        url: openapi/google-ads-api-openapi.yml
      - type: Authentication
        url: https://developers.google.com/google-ads/api/docs/oauth/overview
      - type: SDKs
        url: https://developers.google.com/google-ads/api/docs/client-libs
      - type: Migration Guide
        url: https://developers.google.com/google-ads/api/docs/migration
      - type: Best Practices
        url: https://developers.google.com/google-ads/api/docs/best-practices
      - type: Rate Limits
        url: https://developers.google.com/google-ads/api/docs/rate-limits
      - type: Release Notes
        url: https://developers.google.com/google-ads/api/docs/release-notes
      - type: Support
        url: https://developers.google.com/google-ads/api/support
      - type: Forum
        url: https://groups.google.com/g/adwords-api
      - type: Client Libraries
        url: https://developers.google.com/google-ads/api/docs/client-libs
      - type: Change Log
        url: https://developers.google.com/google-ads/api/docs/release-notes
      - type: Getting Started
        url: https://developers.google.com/google-ads/api/docs/first-call/overview
  - aid: google-ads:google-ads-scripts
    name: Google Ads Scripts
    description: JavaScript-based scripting interface for programmatically managing and querying Google Ads data directly in a browser-based IDE. Scripts enable automated changes to campaigns, ad groups, and reporting without requiring a full API integration.
    image: https://www.gstatic.com/images/branding/product/1x/google_ads_64dp.png
    humanURL: https://developers.google.com/google-ads/scripts/docs/start
    baseURL: https://googleads.googleapis.com
    tags:
      - Automation
      - Campaign Management
      - JavaScript
      - Scripts
    properties:
      - type: Documentation
        url: https://developers.google.com/google-ads/scripts/docs/start
      - type: Getting Started
        url: https://developers.google.com/google-ads/scripts/docs/getting-started
      - type: Reference
        url: https://developers.google.com/google-ads/scripts/docs/examples
common:
  - type: Portal
    url: https://developers.google.com/google-ads/api
  - type: Getting Started
    url: https://developers.google.com/google-ads/api/docs/first-call/overview
  - type: Authentication
    url: https://developers.google.com/google-ads/api/docs/oauth/overview
  - type: Terms of Service
    url: https://developers.google.com/terms
  - type: Privacy Policy
    url: https://policies.google.com/privacy
  - type: Status Page
    url: https://status.cloud.google.com/
  - type: Blog
    url: https://ads-developers.googleblog.com/
  - type: Support
    url: https://developers.google.com/google-ads/api/support
  - type: SDKs
    url: https://developers.google.com/google-ads/api/docs/client-libs
  - type: GitHub Organization
    url: https://github.com/googleads
  - type: Stack Overflow
    url: https://stackoverflow.com/questions/tagged/google-ads-api
  - type: Community
    url: https://groups.google.com/g/adwords-api
  - type: Console
    url: https://ads.google.com/
  - type: Sign Up
    url: https://ads.google.com/signup
  - type: Developer Tools
    url: https://developers.google.com/google-ads/api/docs/developer-toolkit/ai-assistant
  - type: JSONSchema
    url: json-schema/google-ads-campaign-schema.json
  - type: JSON-LD
    url: json-ld/google-ads-context.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
---
