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
  band: agent-aware
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: true
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 43.3
  scored_at: '2026-07-27'
api_count: 1
apis:
- description: GSMA Mobile Money API profile for account validation, FX quotations, and multi-rail money movement (wallet/bank/card) across international corridors.
  name: TerraPay API Suite
  slug: terrapay-api-suite
artifact_total: 5
asyncapis:
- description: ''
  name: Terrapay Notifications Webhooks
  slug: terrapay-notifications-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.terrapay.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.terrapay.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.terrapay.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.terrapay.com/apiReference.html
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.terrapay.com/getStarted.html
- group: auth
  title: ''
  type: Authentication
  url: authentication/terrapay-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/terrapay-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/terrapay-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/terrapay-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/terrapay-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/terrapay-lifecycle.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/terrapay-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/terrapay-llms.txt
- group: start
  title: ''
  type: Sandbox
  url: sandbox/terrapay-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/terrapay-notifications-webhooks.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/terrapay-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/terrapay-domain-security.yml
created: '2026-07-17'
description: TerraPay is a global cross-border payments and digital-wallet infrastructure company connecting banks, mobile wallets, money-transfer operators, merchants, and card networks into a single interoperable network for real-time international money movement. Its partner API Suite follows the GSMA Mobile Money API, exposing account validation, FX quotations, and multi-rail transactions (wallet, bank account, and card) across global remittance corridors, with compliance, monitoring, reconciliation, and reporting built into the platform. Partners authenticate with signed request headers over mutual TLS across Sandbox, UAT, and LIVE environments. Added to the API Evangelist network from the Partech portfolio and enriched from TerraPay's public developer portal.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/terrapay.png
layout: provider
mcp_servers:
- description: ''
  name: terrapay-mcp.yml
  slug: terrapay-mcpyml
modified: '2026-07-21'
name: TerraPay
nav: Providers
network: true
overview: 'TerraPay publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Financial Services, Payments, Cross-Border Payments, and Remittances.


  The TerraPay catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  TerraPay''s developer surface includes documentation, API reference, getting-started guide, authentication, sandbox, and 12 more developer resources.'
random_paper: 56
score:
  band: emerging
  composite: 29.4
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 22.6
    developer_ergonomics: 60.9
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 29.4
  regulatory:
    applies: true
    regime: Payments
    regime_id: payments
    score: 37.0
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: authentication
  name: Terrapay Authentication
  slug: terrapay-authentication
  summary_line: apiKey/custom-signed-headers/mutualTLS · 6 schemes
- kind: domain-security
  name: Terrapay Domain Security
  slug: terrapay-domain-security
  summary_line: TLSv1.3 · DMARC
slug: terrapay
tags:
- Company
- Financial Services
- Payments
- Cross-Border Payments
- Remittances
- Mobile Money
- Digital Wallets
- Money Transfer
- Fintech
- GSMA Mobile Money API
website: https://www.terrapay.com/
---
