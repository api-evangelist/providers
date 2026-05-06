---
aid: upvest
url: https://raw.githubusercontent.com/api-evangelist/upvest/refs/heads/main/apis.yml
name: Upvest
type: Index
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Banking Infrastructure
  - Fintech
  - Investments
  - Securities
  - Fractional Investing
  - Custody
  - Wealth Management
description: Upvest is a Berlin-based API-first investment infrastructure provider that enables banks, brokers, and wealth managers to build and launch investment experiences through a single modular API. Founded in 2017, Upvest is a regulated securities institution in Europe and the UK, covering trading, custody, and back-office operations. The platform supports fractional investing, portfolios, savings plans, roundups, and direct debit, enabling clients like Bunq, DKB, N26, Revolut, and Raisin to offer investment products to their customers.
created: '2026-03-24'
modified: '2026-05-03'
specificationVersion: '0.19'
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
      - Fractional Investing
      - Savings Plans
      - Payments
      - Webhooks
    humanURL: https://docs.upvest.co/
    baseURL: https://api.upvest.co
    properties:
      - url: https://docs.upvest.co/api
        type: Documentation
      - type: OpenAPI
        url: openapi/upvest-investment-api-openapi.yml
      - type: AsyncAPI
        url: asyncapi/upvest-investment-events-asyncapi.yml
      - type: JSONSchema
        url: json-schema/upvest-webhook-event-schema.json
      - type: JSONSchema
        url: json-schema/upvest-order-schema.json
      - type: JSONSchema
        url: json-schema/investment-api-user-schema.json
      - type: JSONSchema
        url: json-schema/investment-api-account-schema.json
      - type: JSONSchema
        url: json-schema/investment-api-order-schema.json
      - type: JSONSchema
        url: json-schema/investment-api-portfolio-schema.json
      - type: JSONSchema
        url: json-schema/investment-api-savings-plan-schema.json
      - type: JSONSchema
        url: json-schema/investment-api-instrument-schema.json
      - type: JSONSchema
        url: json-schema/investment-api-transaction-schema.json
      - type: JSONSchema
        url: json-schema/investment-api-position-schema.json
    description: The Upvest Investment API provides a unified interface for building embedded investment experiences. It supports placing and managing orders, creating portfolios, configuring savings plans, handling securities transfers, and managing user accounts and positions. The API covers the full order lifecycle with asynchronous processing and webhook notifications for real-time event handling. Key resource groups include users and businesses, accounts, orders and executions, instruments and price data, portfolios, savings plans, payments (top-ups, withdrawals, direct debits), tax and compliance, webhooks, and reporting.
common:
  - type: Website
    url: https://upvest.co/
  - type: Portal
    url: https://upvest.co/developers
  - type: Documentation
    url: https://docs.upvest.co/
  - type: GettingStarted
    url: https://docs.upvest.co/documentation/guides
  - type: Blog
    url: https://upvest.co/blog
  - type: Blog
    url: https://engineering.upvest.co/
    title: Engineering Blog
  - type: SignUp
    url: https://upvest.co/contact
  - type: PrivacyPolicy
    url: https://upvest.co/legal/privacy-policy
  - type: GitHubOrganization
    url: https://github.com/upvestco
  - type: GitHubRepository
    url: https://github.com/upvestco/httpsignature-proxy
    title: HTTP Signature Proxy CLI
  - type: GitHubRepository
    url: https://github.com/upvestco/http-signature-examples
    title: HTTP Signature Examples
  - type: GitHubRepository
    url: https://github.com/upvestco/documentation_assets
    title: Documentation Assets
  - type: JSONLD
    url: json-ld/upvest-context.jsonld
  - type: SpectralRules
    url: rules/upvest-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/upvest-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/investment-operations.yaml
    title: Investment Operations
  - type: NaftikoCapability
    url: capabilities/shared/investment-api.yaml
    title: Investment API (Shared)
  - type: Features
    data:
      - name: Fractional Investing
        description: Enable customers to invest in stocks and ETFs starting at 1 EUR with fractional share support.
      - name: Portfolio Management
        description: Build customized portfolios of stocks, ETFs, and upcoming crypto assets with automated rebalancing.
      - name: Savings Plans
        description: Configure recurring automated investment plans with direct debit integration.
      - name: Roundups
        description: Micro-investing through spending-based roundups that automatically invest spare change.
      - name: Instant Account Creation
        description: Enable customers to open investment accounts in seconds through the API.
      - name: Custody Management
        description: Regulated custody services with digital reports and securities safeguarding.
      - name: Multi-Currency Cash Management
        description: Track and manage cash balances across multiple currencies with virtual bank accounts.
      - name: Tax and Compliance
        description: Automated tax wrapper support including ISA, tax exemptions, and compliance reporting.
      - name: Webhook Events
        description: Real-time asynchronous event notifications for orders, payments, accounts, and compliance events.
      - name: Sandbox Environment
        description: Full-featured sandbox at sandbox.upvest.co for testing with simulated bank transactions.
  - type: UseCases
    data:
      - name: Embedded Brokerage
        description: Banks and fintechs embedding fractional stock and ETF trading into existing financial products.
      - name: Digital Wealth Management
        description: Wealth managers building automated portfolio and savings plan products for retail clients.
      - name: Neobank Investment Features
        description: Neobanks adding investment capabilities to checking and savings account offerings.
      - name: White-Label Investment Platform
        description: Third-party platforms building fully branded investment experiences using Upvest infrastructure.
      - name: Roundup Investing
        description: Platforms enabling micro-investing by rounding up purchases and investing the difference.
  - type: Integrations
    data:
      - name: HTTP Signature Proxy
        description: Localhost proxy for handling HTTP request signing required by the Upvest Investment API.
      - name: Direct Debit
        description: Automated recurring payment integration for savings plans and top-ups.
      - name: Webhook Integration
        description: Event-driven integration pattern via Upvest webhook subscriptions for real-time processing.
      - name: OAuth 2.0
        description: Client credentials flow for API authentication and token management.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
