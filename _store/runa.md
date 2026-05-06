---
aid: runa
name: Runa
description: Runa is a global digital payouts platform that enables businesses to automate digital reward and gift card distribution through a single API. The platform provides access to over 5,000 gift cards and payout options across 190+ countries, supporting B2C payments, employee rewards, customer incentives, and loyalty programs. The Runa API supports synchronous and asynchronous order modes, balance management, product catalog browsing, and webhook-based event notifications for order completions.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Gift Cards
  - Rewards
  - Payments
  - Incentives
  - Payouts
created: '2025-02-08'
modified: '2026-05-02'
url: https://raw.githubusercontent.com/api-evangelist/runa/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: runa:runa-payouts-api
    name: Runa Payouts API
    description: The Runa Payouts API (v2) enables digital reward and gift card distribution at scale. Core operations include creating orders (synchronous and asynchronous), retrieving order details, listing orders, estimating order costs, managing account balances, browsing the product catalog by category and country, and receiving order completion and product update webhooks. Authentication uses the X-Api-Key header. Idempotency is supported via X-Idempotency-Key.
    humanURL: https://developer.runa.io/
    baseURL: https://api.runa.io/v2
    tags:
      - Gift Cards
      - Rewards
      - Payments
      - Incentives
      - Payouts
      - B2C
    properties:
      - type: Documentation
        url: https://developer.runa.io/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/runa/refs/heads/main/openapi/runa-payouts-api-openapi.yml
common:
  - type: Portal
    url: https://developer.runa.io/
  - type: Authentication
    url: https://developer.runa.io/docs/getting-an-api-key
  - type: SignUp
    url: https://app.runa.io/
  - type: Sandbox
    url: https://developer.runa.io/docs/playground
  - type: TermsOfService
    url: https://runa.io/legal/
  - type: PrivacyPolicy
    url: https://runa.io/privacy-policy/
  - type: Blog
    url: https://runa.io/blog/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
