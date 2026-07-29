---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 45.0
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Authorize Net Agentic Access
  operation_count: 1
  slug: authorize-net-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 5
apis:
- description: The Authorize.net Payment API enables merchants to process credit card, debit card, eCheck, Apple Pay, Google Pay, and PayPal transactions via a POST-based XML/JSON API with API Login ID and Transacti
  name: Authorize.net Payment API
  slug: authorize-net-payment-api
- description: The Authorize.net Automated Recurring Billing (ARB) API enables merchants to create, update, and cancel subscription-based payment schedules for recurring charges.
  name: Authorize.net Recurring Billing API
  slug: authorize-net-recurring-billing-api
- description: The Authorize.net Customer Information Manager (CIM) API enables secure storage and management of customer payment profiles including credit cards and bank accounts for reuse in future transactions.
  name: Authorize.net Customer Profiles API
  slug: authorize-net-customer-profiles-api
- description: Authorize.net Webhooks deliver real-time event notifications for transaction, subscription, and fraud management events to merchant-configured HTTP endpoints.
  name: Authorize.net Webhooks
  slug: authorize-net-webhooks
- description: Charge, authorize, capture, void and refund transactions.
  name: Authorize.net Transactions API
  slug: authorize-net-transactions-api
artifact_total: 34
collections:
- collection_type: postman
  name: Authorize.Net Transactions API
  slug: postman-authorize-net-transactions-api
- collection_type: open
  name: Authorize.Net API
  slug: open-authorize-net
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/authorizenet/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/authorize-net-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/authorize-net-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/authorize-net-authentication.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/authorize-net-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/authorize-net-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/authorize-net-changelog.yml
- group: design
  title: ''
  type: Components
  url: components/authorize-net-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/authorize-net-data-model.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/authorize-net-decline-codes.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/authorize-net-trust-center.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/authorize-net
- group: company
  title: ''
  type: Website
  url: https://www.authorize.net/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.authorize.net/
- group: start
  title: ''
  type: Portal
  url: https://developer.authorize.net/
- group: company
  title: ''
  type: Blog
  url: https://developer.authorize.net/blog/
- group: start
  title: ''
  type: Signup
  url: https://www.authorize.net/sign-up/
- group: start
  title: ''
  type: Login
  url: https://account.authorize.net/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.authorize.net/sign-up/pricing/
- group: operate
  title: ''
  type: Support
  url: https://support.authorize.net/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.authorize.net/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.authorize.net/company/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.authorize.net/company/privacy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AuthorizeNet
- group: build
  title: PHP SDK
  type: SDKs
  url: https://github.com/AuthorizeNet/sdk-php
- group: build
  title: .NET SDK
  type: SDKs
  url: https://github.com/AuthorizeNet/sdk-dotnet
- group: build
  title: Java SDK
  type: SDKs
  url: https://github.com/AuthorizeNet/sdk-java
- group: build
  title: Ruby SDK
  type: SDKs
  url: https://github.com/AuthorizeNet/sdk-ruby
- group: build
  title: Python SDK
  type: SDKs
  url: https://github.com/AuthorizeNet/sdk-python
- group: build
  title: Node.js SDK
  type: SDKs
  url: https://github.com/AuthorizeNet/sdk-node
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/AuthorizeNet/authorize-net-mcp
created: '2025-02-17'
description: Authorize.net is a leading payment gateway providing secure online payment processing for merchants. It offers a POST-based XML/JSON API, Accept.js hosted payment forms, the Accept Hosted solution, recurring billing (ARB), customer profile management (CIM), advanced fraud detection, and webhooks. Official SDKs are available for PHP, .NET, Java, Ruby, Python, and Node.js.
features:
- description: Accept credit cards, debit cards, eChecks, Apple Pay, Google Pay, and PayPal via a single unified API.
  name: Payment Processing
- description: Client-side JavaScript library that tokenizes payment data in the browser to keep merchant servers out of PCI scope.
  name: Accept.js
- description: Fully hosted payment form that redirects customers to Authorize.net for payment collection with iframe support.
  name: Accept Hosted
- description: Automated recurring billing for subscriptions and installment plans with flexible scheduling options.
  name: Recurring Billing (ARB)
- description: Securely vault customer payment methods for future charges without storing sensitive card data.
  name: Customer Profiles (CIM)
- description: Advanced fraud detection tools including velocity controls, IP blocking, card security code verification, and address verification.
  name: Fraud Detection Suite
- description: Real-time event notifications for transaction completions, declines, fraud holds, and subscription events.
  name: Webhooks
- description: Official Authorize.net MCP server for AI-assisted payment processing integration at github.com/AuthorizeNet/authorize-net-mcp.
  name: MCP Server
finops:
- name: Authorize Net Finops
  service_category: API
  slug: authorize-net-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/authorize-net.png
integrations:
- description: Official Authorize.net WooCommerce payment plugin for WordPress-based e-commerce stores.
  name: WooCommerce
- description: Official Authorize.net Medusa payment plugin for headless commerce implementations.
  name: Medusa
- description: Direct connection to major card networks for authorization and settlement of card-based transactions.
  name: Visa and Mastercard Networks
- description: eCheck processing through the NACHA ACH network for bank-to-bank payment transfers.
  name: NACHA ACH Network
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: Authorize.net
nav: Providers
network: true
overview: 'Authorize.net publishes 1 API on the [APIs.io](https://apis.io/) network: Transactions API. Tagged areas include Accept.js, Credit Cards, eChecks, Fraud Detection, and Payment Gateway.


  Authorize.net''s developer surface includes authentication, sandbox, changelog, documentation, developer portal, engineering blog, signup flow, and 24 more developer resources.'
plans:
- name: Authorize Net Plans Pricing
  plan_count: 3
  slug: authorize-net-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 5
  name: Authorize Net Rate Limits
  slug: authorize-net-rate-limits
score:
  band: strong
  composite: 59.6
  delta: -3.4
  facets:
    commercial_clarity: 92.1
    contract_quality: 58.5
    developer_ergonomics: 69.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 68.4
  previous_composite: 63.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 39.1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/authorize-net/refs/heads/main/screenshots/authorize-net-2026-06-20T172612.png
security:
- kind: authentication
  name: Authorize Net Authentication
  slug: authorize-net-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Authorize Net Domain Security
  slug: authorize-net-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Authorize Net Trust Center
  slug: authorize-net-trust-center
  summary_line: PCI DSS, SSAE-18 (SOC 1), Sarbanes-Oxley (SOX)
slug: authorize-net
solutions:
- description: Comprehensive payment gateway solution connecting merchants to card networks with fraud protection and reporting.
  name: Payment Gateway
- description: Reduce PCI scope using Accept.js or Accept Hosted to tokenize payment data without touching card numbers.
  name: PCI-Compliant Payments
tags:
- Accept.js
- Credit Cards
- eChecks
- Fraud Detection
- Payment Gateway
- Payments
- Recurring Billing
- Transactions
use_cases:
- description: Accept payments on web storefronts using Accept.js or Accept Hosted for PCI-compliant card processing.
  name: E-Commerce Payment Processing
- description: Manage recurring charges for SaaS, membership, and subscription-based business models using ARB.
  name: Subscription Billing
- description: Accept Apple Pay and Google Pay in mobile apps using the in-person and mobile payment SDKs.
  name: Mobile Payments
- description: Integrate card-present transactions via the iOS, Android, or Windows in-person payment SDKs.
  name: Point-of-Sale Integration
- description: Process ACH/eCheck payments for B2B invoicing and recurring bank account debit scenarios.
  name: B2B and eCheck Payments
website: https://www.authorize.net/
---
