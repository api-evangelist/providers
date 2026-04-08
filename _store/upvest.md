---
aid: upvest
url: https://raw.githubusercontent.com/api-evangelist/upvest/refs/heads/main/apis.yml
apis:
- aid: upvest:investment-api
  name: Upvest Investment API
  tags:
  - Custody
  - Investments
  - Orders
  - Portfolios
  - Securities
  - Trading
  humanURL: https://docs.upvest.co/
  baseURL: https://api.upvest.co
  properties:
  - url: https://docs.upvest.co/api
    type: Documentation
  - type: OpenAPI
    url: openapi/upvest-investment-api-openapi.yml
  - type: AsyncAPI
    url: asyncapi/upvest-investment-events-asyncapi.yml
  description: The Upvest Investment API provides a unified interface for building embedded investment experiences. It supports placing and managing orders, creating portfolios, configuring savings plans, handling securities transfers, and managing user accounts and positions. The API covers the full order lifecycle with asynchronous processing and webhook notifications for real-time event handling.
name: Upvest
tags:
- Banking Infrastructure
- Fintech
- Investments
- Securities
type: Contract
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Upvest is a Berlin-based API-first investment infrastructure provider that enables banks, brokers, and wealth managers to build and launch investment experiences through a single modular API. Founded in 2017, Upvest is a regulated securities institution in Europe and the UK, covering trading, custody, and back-office operations.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

