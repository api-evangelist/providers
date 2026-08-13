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
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: documented
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.1
  scored_at: '2026-08-12'
api_count: 1
apis:
- description: REST API for merchants to originate Aplazo installment loans at checkout, retrieve loan status, and process refunds and cancellations. Credentials (apiToken + merchantId) are exchanged at POST /api/au
  name: Aplazo Merchant Payment API
  slug: aplazo-merchant-payment-api
artifact_total: 5
asyncapis:
- description: ''
  name: Aplazo Webhooks
  slug: aplazo-webhooks
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/aplazo/php.aplazo-magento-2-payment-gateway/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/aplazo/php.aplazo-magento-2-payment-gateway/releases
- group: commercial
  title: ''
  type: License
  url: https://github.com/aplazo/php.aplazo-magento-2-payment-gateway/blob/master/LICENSE
- group: company
  title: ''
  type: Website
  url: https://aplazo.mx/pages/home
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aplazo
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aplazo.mx/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aplazo.mx/privacy-and-policy
- group: operate
  title: ''
  type: Support
  url: mailto:soporte@aplazo.mx
- group: build
  title: ''
  type: Packages
  url: packages/aplazo-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/aplazo-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/aplazo-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/aplazo-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/aplazo-conventions.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/aplazo-mcp.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/aplazo-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/aplazo-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/aplazo-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/aplazo-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/aplazo-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/aplazo-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aplazo-domain-security.yml
created: '2026-07-17'
description: Aplazo is a Mexican buy now, pay later (BNPL) payment platform that lets shoppers split online and in-store purchases into installments without a credit card, paying over time directly from their bank account. For merchants, Aplazo exposes a REST payment API (api.aplazo.mx) and official e-commerce plugins (Magento 2, VTEX, Shopify, PrestaShop, Tiendanube) to originate loans at checkout, retrieve loan status, and process refunds and cancellations. Merchants authenticate with an apiToken and merchantId to obtain a short-lived JWT bearer token, then create loans that redirect the customer to Aplazo to complete financing. Aplazo is backed by QED Investors and operates in Mexico, settling in Mexican pesos (MXN).
image: https://aplazoassets.s3.us-west-2.amazonaws.com/icons/aplazo/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: aplazo-mcp.yml
  slug: aplazo-mcpyml
modified: '2026-07-17'
name: Aplazo
nav: Providers
network: true
overview: 'Aplazo publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payments, BNPL, Buy Now Pay Later, and Installments.


  The Aplazo catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Aplazo''s developer surface includes support, authentication, sandbox, and 19 more developer resources.'
random_paper: 47
score:
  band: thin
  composite: 34.3
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 51.6
    developer_ergonomics: 32.1
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 28.9
  previous_composite: 34.3
  provenance:
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 31.3
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/aplazo/refs/heads/main/screenshots/aplazo-2026-07-25T200637.png
security:
- kind: authentication
  name: Aplazo Authentication
  slug: aplazo-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Aplazo Domain Security
  slug: aplazo-domain-security
  summary_line: TLSv1.3 · DMARC
slug: aplazo
tags:
- Company
- Payments
- BNPL
- Buy Now Pay Later
- Installments
- Fintech
- Lending
- Mexico
- Checkout
- E-commerce
website: https://aplazo.mx/pages/home
---
