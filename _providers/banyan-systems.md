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
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.5
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: Banyan's OAuth2 REST API for submitting receipt and transaction data, retrieving enriched (item-level) transactions, managing card-linked-offer campaigns/offers/activations, receipt search, consumer c
  name: Banyan API
  slug: banyan-api
artifact_total: 5
asyncapis:
- description: ''
  name: Banyan Systems Webhooks
  slug: banyan-systems-webhooks
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.banyan.com/docs
- group: docs
  title: ''
  type: Documentation
  url: https://developers.banyan.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://developers.banyan.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.banyan.com/docs/getting-started
- group: company
  title: ''
  type: Blog
  url: https://www.banyan.com/blog-featured
- group: operate
  title: ''
  type: Support
  url: https://www.banyan.com/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.banyan.com/privacy-policy
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.banyan.com/changelog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/banyan-systems-changelog.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/banyan-systems-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/banyan-systems-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/banyan-systems-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/banyan-systems-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/banyan-systems-conformance.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/banyan-systems-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/banyan-systems-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/banyan-systems-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/banyan-systems-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/banyan-systems-domain-security.yml
created: '2026-07-17'
description: Banyan is a privacy-first, item-level receipt data infrastructure platform that acts as middleware between merchants, banks, fintechs, and merchant service providers so they can securely share and enrich transaction data without bilateral contracts. Merchants send receipt and item detail to Banyan (via REST API or batch), and financial institutions submit card transactions to be matched and enriched with SKU-level line items, powering products like card-linked offers (CLO), expense management, and receipt display inside banking apps. Banyan has processed over 21 billion receipts across a network of 40,000+ merchant stores and 5,000+ financial institutions. Founded in 2013, backed by Battery Ventures, Fin Capital, M13, TTV Capital and others, and acquired by Bilt Rewards in March 2025. The public developer platform at developers.banyan.com exposes an OAuth2 REST API (api.banyan.com/rest/v1) plus a webhook egress surface for enriched transactions and offer redemptions.
image: https://cdn.prod.website-files.com/64cf554e262e35556d264e52/66423c7fdfa3c29d470e52e2_Banyan%20Logo_OGI.png
layout: provider
mcp_servers:
- description: ''
  name: banyan-systems-mcp.yml
  slug: banyan-systems-mcpyml
modified: '2026-07-18'
name: Banyan Systems
nav: Providers
network: true
overview: 'Banyan Systems publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Receipt Data, Transaction Enrichment, Item-Level Data, and Card-Linked Offers.


  The Banyan Systems catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Banyan Systems'' developer surface includes documentation, API reference, getting-started guide, engineering blog, support, changelog, authentication, and 12 more developer resources.'
random_paper: 129
score:
  band: thin
  composite: 34.0
  delta: -4.2
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 45.1
    developer_ergonomics: 38.1
    discoverability: 87.0
    governance: 18.2
    operational_transparency: 15.8
  previous_composite: 38.2
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 32.8
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/banyan-systems/refs/heads/main/screenshots/banyan-systems-2026-07-25T202351.png
security:
- kind: authentication
  name: Banyan Systems Authentication
  slug: banyan-systems-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Banyan Systems Domain Security
  slug: banyan-systems-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: banyan-systems
tags:
- Company
- Receipt Data
- Transaction Enrichment
- Item-Level Data
- Card-Linked Offers
- Fintech
- Payments
- Data Collaboration
- Webhooks
website: https://developers.banyan.com/docs
---
