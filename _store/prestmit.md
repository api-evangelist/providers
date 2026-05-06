---
aid: prestmit
name: Prestmit
description: Prestmit is a digital trading platform that lets users buy and sell gift cards, exchange cryptocurrencies, pay bills, and purchase airtime and data. The Prestmit Partner API enables developers to programmatically buy and sell gift cards, manage wallets and payouts, and tap into Prestmits network of trusted partners and seamless transactions.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Bills
  - Crypto
  - Fintech
  - Gift Cards
  - Payments
created: '2025-02-08'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/prestmit/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: prestmit:prestmit-partner-api
    name: Prestmit Partner API
    description: The Prestmit Partner API allows developers to automate the buying and selling of gift cards, manage wallet balances and payouts, and integrate Prestmit transactions into their own applications. The API supports gift card selling and buying, wallet and payout management, account and API key administration, and webhook notifications. Endpoints are versioned under https://api.prestmit.io/partners/v1 (with a sandbox environment at https://dev-api.prestmit.io/partners/v1) and authentication is performed using API keys, with optional IP whitelisting.
    humanURL: https://prestmit.io/developers
    tags:
      - Fintech
      - Gift Cards
      - Payments
      - REST API
    properties:
      - type: Documentation
        url: https://documentation.prestmit.io/
      - type: Developer Portal
        url: https://prestmit.io/developers
      - type: Sandbox
        url: https://sandbox.prestmit.io/
common:
  - type: Portal
    url: https://prestmit.io/
  - type: Developers
    url: https://prestmit.io/developers
  - type: Documentation
    url: https://documentation.prestmit.io/
  - type: Sandbox
    url: https://sandbox.prestmit.io/
  - type: Sign Up
    url: https://prestmit.io/signup
  - type: Login
    url: https://prestmit.io/login
  - type: Blog
    url: https://prestmit.io/blog
  - type: Support
    url: https://prestmit.io/contact
  - type: Terms of Service
    url: https://prestmit.io/terms-of-service
  - type: Privacy Policy
    url: https://prestmit.io/privacy-policy
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
