---
aid: stitch
name: Stitch
description: Stitch is an open banking and payments API platform providing unified access to financial data and payment rails across banks and financial institutions in Africa, primarily South Africa and Nigeria. Stitch enables businesses to accept payments via multiple channels, access bank account data, and issue disbursements through a single GraphQL API.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Africa
  - Financial Data
  - Open Banking
  - Payments
  - Unified API
  - South Africa
  - Nigeria
url: https://raw.githubusercontent.com/api-evangelist/stitch/refs/heads/main/apis.yml
created: '2026-03-27'
modified: '2026-05-04'
specificationVersion: '0.19'
apis:
  - aid: stitch:stitch-graphql
    name: Stitch GraphQL API
    description: The core Stitch API using GraphQL, available at api.stitch.money/graphql. Follows the Relay Server Specification for pagination. Supports all Stitch products including pay-ins, payouts, bank account data, and payments. Authentication uses OAuth 2.0 client credentials.
    humanURL: https://docs.stitch.money/
    tags:
      - GraphQL
      - Open Banking
      - Payments
    properties:
      - type: Documentation
        url: https://docs.stitch.money/
      - type: GraphQL
        url: https://api.stitch.money/graphql
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/stitch/refs/heads/main/openapi/stitch-openapi.yml
  - aid: stitch:stitch-pay-by-bank
    name: Stitch Pay By Bank
    description: Stitch Pay By Bank enables merchants to accept instant bank transfer payments directly from customers' bank accounts in South Africa and Nigeria.
    humanURL: https://docs.stitch.money/
    tags:
      - Payments
      - Bank Transfer
      - Pay-ins
    properties:
      - type: Documentation
        url: https://docs.stitch.money/
  - aid: stitch:stitch-capitec-pay
    name: Stitch Capitec Pay
    description: Stitch integration with Capitec Bank's Capitec Pay payment method, enabling customers to pay via Capitec mobile banking.
    humanURL: https://docs.stitch.money/
    tags:
      - Payments
      - Capitec
      - South Africa
    properties:
      - type: Documentation
        url: https://docs.stitch.money/
  - aid: stitch:stitch-card-payments
    name: Stitch Card Payments
    description: Stitch card payment processing enabling businesses to accept debit and credit card payments through the Stitch unified platform.
    humanURL: https://docs.stitch.money/
    tags:
      - Payments
      - Card Payments
      - Pay-ins
    properties:
      - type: Documentation
        url: https://docs.stitch.money/
  - aid: stitch:stitch-debicheck
    name: Stitch DebiCheck
    description: Stitch DebiCheck integration providing authenticated debit orders for recurring payment collection in South Africa.
    humanURL: https://docs.stitch.money/
    tags:
      - Payments
      - DebiCheck
      - Recurring Payments
      - South Africa
    properties:
      - type: Documentation
        url: https://docs.stitch.money/
  - aid: stitch:stitch-manual-eft
    name: Stitch Manual EFT
    description: Stitch Manual EFT (Electronic Funds Transfer) enabling customers to pay via standard bank EFT with Stitch's streamlined reference management.
    humanURL: https://docs.stitch.money/
    tags:
      - Payments
      - EFT
      - Bank Transfer
    properties:
      - type: Documentation
        url: https://docs.stitch.money/
  - aid: stitch:stitch-disbursements
    name: Stitch Disbursements
    description: Stitch Disbursements (Payouts) API enabling businesses to programmatically send funds to bank accounts, enabling mass payments, refunds, and marketplace disbursements.
    humanURL: https://docs.stitch.money/
    tags:
      - Payouts
      - Disbursements
      - Bank Transfer
    properties:
      - type: Documentation
        url: https://docs.stitch.money/
common:
  - type: Website
    url: https://stitch.money/
  - type: Documentation
    url: https://docs.stitch.money/
  - type: GitHub Organization
    url: https://github.com/stitch-money
  - type: Sign Up
    url: https://stitch.money/contact
  - type: Status
    url: https://status.stitch.money/
  - type: Features
    data:
      - 'Stitch (Talend / Qlik): hundreds of services across Data Integration'
      - 'Detailed pricing: see https://www.stitchdata.com/pricing/'
      - 'Service: Stitch Data Loader'
      - 'Service: 130+ pre-built sources'
      - 'Service: Standard ($100/mo for 5M rows)'
      - 'Service: Advanced ($1,250/mo)'
      - 'Service: Premium ($2,500/mo)'
      - 'Service: Now part of Qlik Data Integration platform'
    sources:
      - https://www.stitchdata.com/pricing/
      - https://focus.finops.org/
    updated: '2026-05-04'
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
