---
aid: vendr
name: Vendr
description: Vendr is a SaaS procurement intelligence platform that helps businesses manage software spending through data-driven pricing insights and negotiation guidance. The Vendr API (OpenPrice API) provides access to real contract pricing data from 200,000+ verified software agreements across 20,000+ products, enabling developers to embed fair pricing estimates, negotiation insights, product catalog data, and purchase scope management into their applications.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Pricing
  - Procurement
  - SaaS
  - Software Spend Management
  - Negotiation
url: https://raw.githubusercontent.com/api-evangelist/vendr/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: vendr:vendr-openapi
    name: Vendr OpenPrice API
    description: The Vendr OpenPrice API provides access to real SaaS pricing intelligence derived from 200,000+ verified software contracts across 20,000+ products. It enables applications to retrieve structured catalog data, generate fair price estimates with confidence scoring, define purchase scope requirements, and subscribe to webhook events. Authentication uses API key via the X-API-Key header. Rate limits are 250 requests per minute and 150,000 requests per day.
    humanURL: https://developers.vendr.com/docs/introduction
    baseURL: https://api.vendr.com
    tags:
      - Pricing
      - Procurement
      - SaaS
      - Catalog
      - Webhooks
    properties:
      - type: Documentation
        url: https://developers.vendr.com/docs/introduction
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/vendr/refs/heads/main/openapi/vendr-openapi.yml
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/vendr/refs/heads/main/json-schema/vendr-pricing-response-schema.json
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/vendr/refs/heads/main/json-schema/vendr-catalog-product-schema.json
      - type: SpectralRules
        url: https://raw.githubusercontent.com/api-evangelist/vendr/refs/heads/main/rules/vendr-rules.yml
      - type: Vocabulary
        url: https://raw.githubusercontent.com/api-evangelist/vendr/refs/heads/main/vocabulary/vendr-vocabulary.yml
    contact:
      - FN: Vendr Developer Support
        email: developers@vendr.com
  - aid: vendr:vendr-mcp
    name: Vendr MCP Server
    description: The Vendr Model Context Protocol (MCP) server exposes Vendr pricing intelligence to AI agents via the MCP standard. It provides tools for searching the product catalog, retrieving custom price estimates, and obtaining negotiation insights. Requires a Vendr API key.
    humanURL: https://github.com/vendrinc/vendr-mcp
    baseURL: https://api.vendr.com
    tags:
      - MCP
      - AI Agents
      - Pricing
      - Procurement
    properties:
      - type: Documentation
        url: https://github.com/vendrinc/vendr-mcp
      - type: GitHubRepository
        url: https://github.com/vendrinc/vendr-mcp
common:
  - type: Website
    url: https://www.vendr.com/
  - type: Documentation
    url: https://developers.vendr.com/docs/introduction
  - type: PricingPage
    url: https://www.vendr.com/pricing-api
  - type: GitHubOrganization
    url: https://github.com/vendrinc
  - type: Support
    url: mailto:developers@vendr.com
  - type: RateLimits
    url: https://developers.vendr.com/docs/introduction
  - type: Authentication
    url: https://developers.vendr.com/docs/introduction
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
