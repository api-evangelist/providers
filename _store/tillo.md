---
aid: tillo
name: Tillo
description: Tillo is an award-winning gift card API platform connecting businesses to 4,000+ global brands across 37 markets and 16 currencies. The REST API supports digital and physical gift card issuance, balance checking, float management, and brand catalog access. Authentication uses HMAC-SHA256 signatures.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Finance
  - Gift Cards
  - Payments
  - Rewards
  - Incentives
created: '2025-02-08'
modified: '2026-05-03'
url: https://raw.githubusercontent.com/api-evangelist/tillo/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: tillo:tillo-gift-card-api
    name: Tillo Gift Card API
    description: The Tillo Gift Card API enables businesses to issue digital and physical gift cards from 4,000+ global brands. Supports synchronous and asynchronous card issuance, balance checking, refunds, order status checking, and brand catalog retrieval.
    humanURL: https://www.tillo.io/gift-card-api
    baseURL: https://app.tillo.io
    tags:
      - Finance
      - Gift Cards
      - Payments
      - Rewards
    properties:
      - type: Documentation
        url: https://tillo.tech/v2_docs/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/tillo/refs/heads/main/openapi/tillo-gift-card-openapi.yml
  - aid: tillo:tillo-float-api
    name: Tillo Float Management API
    description: Manages Tillo float accounts including balance retrieval, payment transfer requests, and transfer status tracking.
    humanURL: https://tillo.tech/v2_docs/floats.html
    baseURL: https://app.tillo.io
    tags:
      - Finance
      - Float
      - Payments
    properties:
      - type: Documentation
        url: https://tillo.tech/v2_docs/floats.html
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/tillo/refs/heads/main/openapi/tillo-gift-card-openapi.yml
common:
  - type: Website
    url: https://www.tillo.io/
  - type: Portal
    url: https://www.tillo.io/gift-card-api
  - type: Documentation
    url: https://tillo.tech/v2_docs/
  - type: Getting Started
    url: https://tillo.tech/v2_docs/getting_started.html
  - type: Authentication
    url: https://tillo.tech/v2_docs/authentication.html
  - type: GitHub Organization
    url: https://github.com/tilloops
  - type: GitHub Repository
    url: https://github.com/tilloops/tillo
  - type: Blog
    url: https://www.tillo.io/blog
  - type: Contact
    url: https://www.tillo.io/contact
  - type: Pricing
    url: https://www.tillo.io/pricing
  - type: Terms of Service
    url: https://www.tillo.io/legal
  - type: Postman Collection
    url: https://api.tillo.tech/
  - type: Sign Up
    url: https://app.tillo.io/
  - type: Use Cases
    url: https://www.tillo.io/
  - type: Integrations
    url: https://www.tillo.io/partners
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
