---
aid: zendit
name: Zendit
description: Zendit is a cloud-based Prepay-as-a-Service platform that provides API access to a global prepaid ecosystem. The API enables businesses to offer mobile top-ups, data packages, digital gift cards, prepaid utility bill payments, and eSIM products through a single integration.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - eSIM
  - Gift Cards
  - Mobile Top-Up
  - Payments
  - Prepaid
created: '2025-02-08'
modified: '2026-05-03'
url: https://raw.githubusercontent.com/api-evangelist/zendit/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: zendit:zendit-api
    name: Zendit API
    description: The Zendit API provides programmatic access to the global prepaid ecosystem, enabling developers to offer mobile credit top-ups, data packages, digital gift cards, prepaid utility bill payments, and eSIM products. The platform supports self-onboarding, sandbox testing, and webhook notifications.
    humanURL: https://zendit.io/
    baseURL: https://api.zendit.io/v1
    tags:
      - eSIM
      - Gift Cards
      - Mobile Top-Up
      - Prepaid
    properties:
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/zendit/refs/heads/main/openapi/zendit-api.yml
      - type: Documentation
        url: https://zendit.io/
      - type: APIReference
        url: https://developers.zendit.io/api/
      - type: GettingStarted
        url: https://zendit.io/user-guide/getting-started/
      - type: Authentication
        url: https://developers.zendit.io/api/
      - type: Guide
        url: https://zendit.io/guide-to-integrating-zendits-api-into-your-projects/
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/zendit/refs/heads/main/json-schema/
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/zendit/refs/heads/main/json-structure/
      - type: JSON-LD
        url: https://raw.githubusercontent.com/api-evangelist/zendit/refs/heads/main/json-ld/zendit-api-context.jsonld
      - type: Example
        url: https://raw.githubusercontent.com/api-evangelist/zendit/refs/heads/main/examples/
common:
  - url: https://zendit.io/
    name: Zendit Website
    type: Website
  - url: https://zendit.io/user-guide/
    name: User Guide
    type: Documentation
  - url: https://zendit.io/user-guide/getting-started/
    name: Getting Started
    type: GettingStarted
  - url: https://developers.zendit.io/api/
    name: Zendit API Reference
    type: APIReference
  - url: https://console.zendit.io/login
    name: Zendit Console Login
    type: Login
  - url: https://zendit.io/zendit-new-features/
    name: Zendit Releases
    type: ChangeLog
  - url: https://github.com/zenditplatform
    name: Zendit GitHub Organization
    type: GitHubOrganization
  - url: https://raw.githubusercontent.com/api-evangelist/zendit/refs/heads/main/rules/zendit-rules.yml
    name: Zendit Spectral Ruleset
    type: SpectralRules
  - url: https://raw.githubusercontent.com/api-evangelist/zendit/refs/heads/main/vocabulary/zendit-vocabulary.yml
    name: Zendit Vocabulary
    type: Vocabulary
  - url: https://raw.githubusercontent.com/api-evangelist/zendit/refs/heads/main/capabilities/zendit-workflow.yaml
    name: Zendit Workflow Capability
    type: NaftikoCapability
  - data:
      - name: Mobile Top-Ups
        description: Recharge prepaid mobile credit globally across thousands of carriers.
      - name: Data Bundles
        description: Sell mobile data packages to subscribers worldwide.
      - name: eSIM Products
        description: Offer eSIM plans for global travelers with QR-code activation.
      - name: Digital Gift Cards
        description: Distribute prepaid gift cards across major brands.
      - name: Utility Bill Payments
        description: Process prepaid utility payments for electricity, water, and gas.
      - name: Phone Number Lookup
        description: Identify carrier from phone number in E.164 format.
      - name: Webhooks
        description: Receive event notifications for transaction completions.
      - name: Async Reports
        description: Generate transaction reports as CSV files asynchronously.
    name: Features
    type: Features
  - data:
      - name: Telecom Resellers
        description: Power top-up and data plan sales for MVNOs and resellers.
      - name: Travel Apps
        description: Embed eSIM purchases into travel booking flows.
      - name: Gift Card Marketplaces
        description: Aggregate digital gift card inventory across brands.
      - name: Fintech Apps
        description: Enable bill payment and prepaid services within wallets.
      - name: Loyalty Programs
        description: Reward users with mobile top-ups, gift cards, or eSIM data.
    name: UseCases
    type: UseCases
  - data:
      - name: Webhooks
        description: Inbound webhook endpoints for transaction event notifications.
      - name: REST API
        description: Bearer-token authenticated REST API over HTTPS.
    name: Integrations
    type: Integrations
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
