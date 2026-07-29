---
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
    error_semantics: documented
    idempotency: documented
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.0
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: Paysend Enterprise's single Payout API disburses funds worldwide to cards and bank accounts through the Paysend payments network. A multi-task POST /processing endpoint carries operations including pa
  name: Paysend Enterprise Payout API
  slug: paysend-enterprise-payout-api
artifact_total: 5
asyncapis:
- description: ''
  name: Paysend Webhooks
  slug: paysend-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/paysend-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://paysend.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.paysend.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.paysend.com/product-overview/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.paysend.com/endpoints/get-processing-status/
- group: auth
  title: ''
  type: Authentication
  url: https://developer.paysend.com/authentication-and-idempotency/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/paysend
- group: company
  title: ''
  type: Blog
  url: https://paysend.com/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cloud.paysend.com/web/docs/Global_Privacy_Policy_Paysend.pdf
- group: other
  title: ''
  type: Product
  url: https://paysend.com/enterprise
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.paysend.com/
- group: operate
  title: ''
  type: Support
  url: https://help.paysend.com/hc/en-us
- group: auth
  title: ''
  type: Compliance
  url: https://paysend.com/en/blog/paysend-compliance-security-digital-money-transfers
- group: design
  title: ''
  type: Conventions
  url: conventions/paysend-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/paysend-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/paysend-error-codes.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/paysend-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/paysend-webhooks.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/paysend-conformance.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/paysend-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/paysend-llms.txt
created: '2026-07-24'
description: 'Paysend is a London-headquartered global fintech, founded in 2017, building a cross-border digital payments network that moves money to bank accounts, cards, and wallets across 170+ countries in 40+ currencies for more than 11 million consumers and a growing base of enterprise clients. Alongside its consumer money-transfer app, Paysend operates Paysend Enterprise, a business-facing payments platform whose developer surface is a single Payout API: one integration disburses funds worldwide to cards and accounts, with FX rate lookups, bank and card tokenization utilities, partner statements, and balance queries. The API is a partner-provisioned, enterprise integration (United Kingdom home market) rather than a fully public self-serve product — authentication is API key plus HMAC digital signature (X-OPP-Signature), requests are idempotent via a request id and date, and payout status is delivered through configurable webhook notifications. Paysend documents this surface openly
  on a Docusaurus developer portal with a sandbox mock service, but does not publish a downloadable OpenAPI/Swagger definition or a public base URL.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: paysend-mcp.yml
  slug: paysend-mcpyml
modified: '2026-07-24'
name: Paysend
nav: Providers
network: true
overview: 'Paysend publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Payments, United Kingdom, Cross-Border, Money Transfer, and Payouts.


  The Paysend catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Paysend''s developer surface includes documentation, API reference, authentication, engineering blog, getting-started guide, support, sandbox, and 14 more developer resources.'
random_paper: 27
score:
  band: thin
  composite: 40.8
  delta: 4.7
  facets:
    commercial_clarity: 18.4
    contract_quality: 51.6
    developer_ergonomics: 60.9
    discoverability: 66.7
    governance: 12.5
    operational_transparency: 13.2
  previous_composite: 36.1
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 53.1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Paysend Authentication
  slug: paysend-authentication
  summary_line: apiKey/hmac-signature · 2 schemes
- kind: domain-security
  name: Paysend Domain Security
  slug: paysend-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: paysend
tags:
- Payments
- United Kingdom
- Cross-Border
- Money Transfer
- Payouts
- Payment Processing
- FX
- Remittance
- Fintech
website: https://paysend.com/
---
