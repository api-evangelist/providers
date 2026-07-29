---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: Next-generation Bread Pay REST API for managing buyers, merchant accounts, personalized payment options and pricing, and the merchant transaction lifecycle (authorize, capture, cancel, refund). Secure
  name: BreadPay Platform API
  slug: breadpay-platform-api
artifact_total: 5
asyncapis:
- description: ''
  name: Bread Financial Webhooks
  slug: bread-financial-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.breadfinancial.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://platform-docs.breadpayments.com/bread-developers/docs
- group: docs
  title: ''
  type: Documentation
  url: https://platform-docs.breadpayments.com/bread-developers/docs
- group: docs
  title: ''
  type: APIReference
  url: https://platform-docs.breadpayments.com/bread-developers/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://platform-docs.breadpayments.com/bread-developers/docs/api-access
- group: operate
  title: ''
  type: Support
  url: https://platform-docs.breadpayments.com/bread-onboarding/docs/support
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bppub
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.breadfinancial.com/en/privacy-policy.html
- group: build
  title: ''
  type: Packages
  url: packages/bread-financial-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/bread-financial-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bread-financial-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/bread-financial-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/bread-financial-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/bread-financial-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/bread-financial-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/bread-financial-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/bread-financial-components.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/bread-financial-mcp.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/bread-financial-webhooks.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/bread-financial-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bread-financial-domain-security.yml
created: '2026-07-17'
description: 'Bread Financial (formerly Alliance Data Systems) is a US consumer financial services company providing branded and co-brand credit cards, private-label and general-purpose lending, and point-of-sale buy-now-pay-later financing under the Bread Pay brand. Its developer surface, Bread Pay, exposes a REST API platform for merchants to embed installment and revolving financing into online and in-store checkout: the next-generation BreadPay Platform API (api.platform.breadpayments.com) manages buyers, merchant accounts, payment options, pricing, and the transaction lifecycle (authorize, capture, cancel, refund), secured with OAuth 2.0 client-credentials and JWT access tokens; a legacy Bread Classic Merchant API manages checkout carts and transactions; and browser (JavaScript) plus native iOS and Android SDKs render placements, prequalification (RTPS), and the Bread checkout modal on merchant storefronts. Bread also ships e-commerce platform plugins (Shopify, Magento 2, BigCommerce,
  WooCommerce, Miva, Volusion, Salesforce Commerce Cloud) and a partner sandbox. This profile was surfaced as a portfolio company of Bessemer Venture Partners.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bread-financial.png
layout: provider
mcp_servers:
- description: ''
  name: bread-financial-mcp.yml
  slug: bread-financial-mcpyml
modified: '2026-07-18'
name: Bread Financial
nav: Providers
network: true
overview: 'Bread Financial publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Payments, Buy Now Pay Later, and Lending.


  The Bread Financial catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Bread Financial''s developer surface includes documentation, API reference, getting-started guide, support, authentication, sandbox, and 15 more developer resources.'
random_paper: 25
score:
  band: thin
  composite: 38.9
  delta: 3.9
  facets:
    commercial_clarity: 10.5
    contract_quality: 51.6
    developer_ergonomics: 65.2
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 13.2
  previous_composite: 35.0
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 32.8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bread-financial/refs/heads/main/screenshots/bread-financial-2026-07-25T203733.png
security:
- kind: authentication
  name: Bread Financial Authentication
  slug: bread-financial-authentication
  summary_line: oauth2/http/apiKey · 3 schemes
- kind: domain-security
  name: Bread Financial Domain Security
  slug: bread-financial-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bread-financial
tags:
- Company
- Fintech
- Payments
- Buy Now Pay Later
- Lending
- Consumer Finance
- Point of Sale
- Ecommerce
website: https://www.breadfinancial.com
---
