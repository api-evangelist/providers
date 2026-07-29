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
    error_semantics: false
    idempotency: verified
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 49.5
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 6
  human_in_the_loop: 1
  name: Truelayer Agentic Access
  operation_count: 13
  slug: truelayer-agentic-access
  summary_line: 13 operations · 6 acting · 1 human-in-the-loop
api_count: 6
apis:
- description: The TrueLayer Data API provides access to bank account data including account information, balances, transactions, identity verification, and standing orders. Used for account verification, affordabil
  name: TrueLayer Data API
  slug: data-api
- description: Variable recurring payment mandates
  name: TrueLayer Mandates API
  slug: truelayer-mandates-api
- description: Merchant account management and balance
  name: TrueLayer Merchant Accounts API
  slug: truelayer-merchant-accounts-api
- description: Create and manage individual bank payments
  name: TrueLayer Payments API
  slug: truelayer-payments-api
- description: Payments from merchant accounts to users
  name: TrueLayer Payouts API
  slug: truelayer-payouts-api
- description: Refund payments back to users
  name: TrueLayer Refunds API
  slug: truelayer-refunds-api
artifact_total: 29
collections:
- collection_type: postman
  name: TrueLayer Payments Mandates API
  slug: postman-truelayer-mandates-api
- collection_type: postman
  name: TrueLayer Payments Mandates Merchant Accounts API
  slug: postman-truelayer-merchant-accounts-api
- collection_type: postman
  name: TrueLayer Mandates Payments API
  slug: postman-truelayer-payments-api
- collection_type: postman
  name: TrueLayer Payments Mandates Payouts API
  slug: postman-truelayer-payouts-api
- collection_type: postman
  name: TrueLayer Payments Mandates Refunds API
  slug: postman-truelayer-refunds-api
- collection_type: open
  name: TrueLayer Payments API
  slug: open-truelayer-payments
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/truelayer/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/truelayer-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/truelayer-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/truelayer-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/truelayer-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/truelayer-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://truelayer.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.truelayer.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.truelayer.com/reference
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/TrueLayer
- group: start
  title: ''
  type: Console
  url: https://console.truelayer.com/
- group: start
  title: ''
  type: Sandbox
  url: https://console.truelayer-sandbox.com/
- group: build
  title: ''
  type: SDKs
  url: https://docs.truelayer.com/docs/client-libraries
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.truelayer.com/changelog
- group: company
  title: ''
  type: Blog
  url: https://truelayer.com/blog/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/truelayer/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/TrueLayer
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/TrueLayer/truelayer_mcp
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.truelayer.com/llms.txt
created: '2026-03-27'
description: TrueLayer is Europe's leading open banking platform providing unified access to bank data, payments, payouts, refunds, and variable recurring payments across the UK and EU. TrueLayer connects to 69+ financial institutions and enables instant bank payments, data enrichment, and account verification through a single API.
examples:
- key_count: 3
  name: Truelayer Create Mandate Example
  slug: truelayer-create-mandate-example
- key_count: 2
  name: Truelayer Create Payment Example
  slug: truelayer-create-payment-example
finops:
- name: Truelayer Finops
  service_category: API
  slug: truelayer-finops
graphqls:
- description: This conceptual GraphQL schema represents the TrueLayer open banking platform, covering unified access to bank data, payments, payouts, variable recurring payments (VRP), identity verification, and co
  name: TrueLayer GraphQL Schema
  slug: truelayer-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/truelayer.png
json_schemas:
- name: Payment
  property_count: 11
  slug: truelayer-payment
json_structures:
- name: Truelayer Payment Structure
  property_count: 0
  slug: truelayer-payment-structure
jsonld:
- class_count: 25
  name: Truelayer Context
  property_count: 5
  slug: truelayer-context
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: TrueLayer
nav: Providers
network: true
overview: 'TrueLayer publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Mandates API, Merchant Accounts API, Payments API, and 2 more. Tagged areas include Data API, Financial Services, Open Banking, Payments, and PSD2.


  The TrueLayer catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  TrueLayer''s developer surface includes authentication, documentation, API reference, developer console, sandbox, changelog, engineering blog, and 12 more developer resources.'
plans:
- name: Truelayer Plans Pricing
  plan_count: 3
  slug: truelayer-plans-pricing
random_paper: 29
rate_limits:
- limit_count: 5
  name: Truelayer Rate Limits
  slug: truelayer-rate-limits
rules:
- name: TrueLayer API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: truelayer-jsonschema-spectral-rules
- name: TrueLayer API Rules
  rule_count: 11
  severity_counts:
    error: 6
    hint: 3
    info: 0
    warn: 2
  slug: truelayer-rules
score:
  band: strong
  composite: 56.9
  delta: -5.7
  facets:
    commercial_clarity: 47.4
    contract_quality: 73.0
    developer_ergonomics: 54.3
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 52.6
  previous_composite: 62.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 40.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/truelayer/refs/heads/main/screenshots/truelayer-2026-06-20T195753.png
security:
- kind: authentication
  name: Truelayer Authentication
  slug: truelayer-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Truelayer Domain Security
  slug: truelayer-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Truelayer Vulnerability Disclosure
  slug: truelayer-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Truelayer Trust Center
  slug: truelayer-trust-center
  summary_line: ISO 27001, GDPR
slug: truelayer
tags:
- Data API
- Financial Services
- Open Banking
- Payments
- PSD2
- UK Banking
- VRP
website: https://truelayer.com/
---
