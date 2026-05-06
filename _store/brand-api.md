---
aid: brand-api
url: https://raw.githubusercontent.com/api-evangelist/brand-api/refs/heads/main/apis.yml
name: Brand API (Brandfetch)
tags:
  - Brands
  - Logos
  - Brand Assets
  - Company Data
  - Firmographics
type: Index
x-type: company
image: https://kinlane-productions2.s3.amazonaws.com/apis-json-icons/brand-api-create-branded-experiences.png
access: 3rd-Party
created: '2024-03-30'
modified: '2026-04-21'
position: Consuming
description: Brandfetch provides programmatic access to brand assets and company data through a suite of APIs. The Brand API retrieves logos, color schemes, fonts, images, and firmographic information for any company via domain, stock ticker, ISIN code, or crypto symbol. The Logo Link API serves logos via CDN with support for multiple formats, themes, and sizes. The Brand Search API enables autocomplete experiences by matching brand names to their domains and identifiers. All APIs support Bearer token authentication with free access for development.
apis:
  - aid: brand-api:brandfetch-brand-api
    name: Brandfetch Brand API
    tags:
      - Brands
      - Logos
      - Colors
      - Fonts
      - Firmographics
    humanURL: https://docs.brandfetch.com/docs/brand-api
    properties:
      - url: openapi/brandfetch-brand-api.yml
        type: OpenAPI
      - url: https://docs.brandfetch.com/docs/brand-api
        type: Documentation
    description: 'Brand API provides programmatic access to any company''s brand assets through a single API call. Returns the latest logos, color schemes, fonts, images, and firmographic information. Supports lookup by domain (e.g. nike.com), stock/ETF ticker (e.g. NKE), ISIN code, or crypto symbol (e.g. BTC). Base endpoint: GET /v2/brands/{identifier}. Authentication via Bearer token. Free sandbox testing available on the brandfetch.com domain.'
  - aid: brand-api:brandfetch-logo-link-api
    name: Brandfetch Logo Link API
    tags:
      - Logos
      - CDN
      - Brand Assets
    humanURL: https://docs.brandfetch.com/docs/logo-link
    properties:
      - url: https://docs.brandfetch.com/docs/logo-link
        type: Documentation
    description: 'Logo Link delivers brand logos directly via CDN URL embedding. Supports lookup by domain, stock ticker, crypto symbol, or ISIN. Parameters include logo type (icon, symbol, logo), theme (light/dark), height/width, format (webp, png, jpg, svg), and fallback behavior. Base CDN URL: https://cdn.brandfetch.io/{identifier}?c=CLIENT_ID. Free with fair-use rate limits; no attribution required.'
  - aid: brand-api:brandfetch-brand-search-api
    name: Brandfetch Brand Search API
    tags:
      - Brand Search
      - Autocomplete
      - Domain Matching
    humanURL: https://docs.brandfetch.com/docs/brand-search-api
    properties:
      - url: https://docs.brandfetch.com/docs/brand-search-api
        type: Documentation
    description: 'Brand Search API matches brand names to their corresponding domain URLs and unique identifiers, enabling rich autocomplete experiences. Endpoint: GET https://api.brandfetch.io/v2/search/:name. Authentication via Client ID query parameter. Free to use; no attribution required.'
common:
  - url: https://brandfetch.com/developers/customers
    name: Customers
    type: Customers
  - url: https://brandfetch.com/developers/pricing
    name: Pricing
    type: Pricing
  - url: https://docs.brandfetch.com/docs/getting-started
    name: Getting Started
    type: GettingStarted
  - url: https://docs.brandfetch.com/docs/webhooks/overview
    name: Webhooks
    type: Webhooks
  - url: https://docs.brandfetch.com/docs/webhooks/event-types
    name: Event Types
    type: EventTypes
  - url: https://docs.brandfetch.com/support/getting-help
    name: Support
    type: Support
  - url: https://docs.brandfetch.com/support/report-inaccuracies
    name: Issues
    type: Issues
  - url: https://docs.brandfetch.com/recipes/overview
    name: Recipes
    type: Recipes
  - url: https://docs.brandfetch.com/reference/overview
    name: Reference
    type: Documentation
  - url: https://docs.brandfetch.com/docs/brand-api#testing-sandbox
    name: Sandbox
    type: Sandbox
  - url: https://docs.brandfetch.com/changelog/2024
    name: Change Log
    type: ChangeLog
  - url: https://developers.brandfetch.com/
    name: Login
    type: Login
  - url: https://developers.brandfetch.com/register
    name: Sign Up
    type: SignUp
  - url: https://docs.brandfetch.com/llms.txt
    name: LLMs Reference
    type: LLMsTxt
properties:
  - type: x-domain
    value: brandfetch.com
  - type: x-authentication
    value: Bearer token (Brand API), Client ID query parameter (Logo Link, Search)
  - type: x-identifier-types
    value: Domain, Stock/ETF ticker, ISIN code, Crypto symbol
  - type: x-data-returned
    value: Logos, color palettes, fonts, images, firmographic data
  - type: x-logo-formats
    value: WebP, PNG, JPG, SVG
  - type: x-logo-types
    value: icon, symbol, logo
  - type: x-logo-themes
    value: light, dark
  - type: x-use-cases
    value: B2B personalization, brand asset retrieval, company data enrichment, financial platform logos, crypto app branding, multi-tenant SaaS branding, brand autocomplete, CRM enrichment
maintainers:
  - FN: API Evangelist
    email: info@apievangelist.com
specificationVersion: '0.19'
---
