---
aid: clerk-io
name: Clerk.io
url: https://raw.githubusercontent.com/api-evangelist/clerk-io/refs/heads/main/apis.yml
created: '2025-02-08'
modified: '2026-04-26'
type: Index
access: 3rd-Party
position: Consumer
specificationVersion: '0.19'
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
x-type: company
tags:
  - AI
  - Commerce
  - E-Commerce
  - Email Marketing
  - Personalization
  - Recommendations
  - Search
description: Clerk.io is an e-commerce personalization platform that uses artificial intelligence and machine learning to deliver tailored product recommendations, on-site search results, audience-segmented email campaigns, and merchandising controls for online retailers. The platform exposes a REST API for product, category, order, and customer data ingestion, plus client-side JavaScript and Liquid templating for recommendation slots and search experiences.
apis:
  - aid: clerk-io:clerk-io-api
    name: Clerk.io API
    tags:
      - Commerce
      - Personalization
      - Recommendations
      - Search
    humanURL: https://docs.clerk.io/
    properties:
      - url: https://docs.clerk.io/
        type: Documentation
      - url: https://docs.clerk.io/docs/how-the-clerkio-platform-works
        type: Getting Started
      - url: https://docs.clerk.io/docs/authentication
        type: Authentication
      - url: https://docs.clerk.io/docs/errors
        type: Errors
      - url: https://docs.clerk.io/docs/pagenation
        type: Pagination
    description: 'The Clerk.io API provides REST endpoints for managing products, categories, orders, customers, recommendations, and search. The API uses a dual-key authentication model: a public key identifies the store and is used in browser-side requests, while a private key is required for sensitive operations and data ingestion. JSON is the primary payload format and SSL is required when sending the private key.'
  - aid: clerk-io:clerkjs
    name: Clerk.js Client Library
    tags:
      - Client Library
      - JavaScript
    humanURL: https://docs.clerk.io/docs/clerkjs-quick-start
    properties:
      - url: https://docs.clerk.io/docs/clerkjs-quick-start
        type: Documentation
    description: Clerk.js is the browser-side JavaScript library for embedding Clerk.io recommendation slots, search, and email opens on a storefront, with Liquid templating support and event tracking.
common:
  - type: Website
    url: https://www.clerk.io/
  - type: Documentation
    url: https://docs.clerk.io/
  - type: Knowledgebase
    url: https://help.clerk.io/
  - type: Status
    url: https://status.clerk.io/
  - type: Blog
    url: https://www.clerk.io/blogs
  - type: Pricing
    url: https://www.clerk.io/pricing
  - type: Partners
    url: https://www.clerk.io/partners
  - type: Integrations
    url: https://www.clerk.io/integrations
  - type: Trust Center
    url: https://trust.clerk.io/
  - type: Terms of Service
    url: https://www.clerk.io/terms-of-service
  - type: Privacy Policy
    url: https://www.clerk.io/privacy
  - type: JSON-LD
    url: json-ld/clerk-io-context.jsonld
  - type: Spectral
    url: rules/clerk-io-rules.yml
  - type: Naftiko Capabilities
    url: capabilities/clerk-io-capabilities.yml
maintainers:
  - FN: Kin Lane
    email: kinlane@gmail.com
---
