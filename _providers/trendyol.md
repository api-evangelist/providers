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
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.1
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: The Trendyol Marketplace / Partner API for sellers and integrators — product, order/shipment, returns, invoice, settlement, and webhook operations.
  name: Trendyol Marketplace API
  slug: trendyol-marketplace-api
artifact_total: 6
asyncapis:
- description: ''
  name: Trendyol Webhooks
  slug: trendyol-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/trendyol-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://trendyol.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.trendyol.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.trendyol.com/docs/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://developers.trendyol.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.trendyol.com/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://developers.trendyol.com/docs/support-request
- group: operate
  title: ''
  type: StatusPage
  url: https://developers.trendyol.com/docs/api-status
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.trendyol.com/changelog
- group: company
  title: ''
  type: Blog
  url: https://medium.com/trendyol-tech
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Trendyol
- group: auth
  title: ''
  type: Authentication
  url: authentication/trendyol-authentication.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/trendyol-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/trendyol-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/trendyol-llms.txt
created: '2026-07-17'
description: 'Trendyol is Turkey''s largest e-commerce marketplace and a leading fashion and retail platform operating across Türkiye, the Gulf, Azerbaijan, and Central & Eastern Europe. Its Marketplace (Partner) API lets sellers and integrators manage the full commerce lifecycle: product catalog with category/brand/ attribute data, price and stock updates, order and shipment-package fulfillment, returns and claims, invoicing, settlements and financial reconciliation, the Export Center, customer questions, and order webhooks. Authentication is HTTP Basic (API key/secret) with a mandatory User-Agent header, plus an OAuth 2.0 authorization-code flow for multi-supplier integrators. Bulk writes are asynchronous and confirmed via a batchRequestId.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/trendyol.png
layout: provider
mcp_servers:
- description: A candidate Model Context Protocol tool surface for the Trendyol Marketplace API, mapped one-to-one from documented operations. Not published by Trendyol — a starting point for an agent integration, g
  name: Trendyol MCP Server
  slug: trendyol-mcp-server
modified: '2026-07-21'
name: Trendyol
nav: Providers
network: true
overview: 'Trendyol publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, E-Commerce, Marketplace, Retail, and Fashion.


  The Trendyol catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Trendyol''s developer surface includes documentation, API reference, getting-started guide, support, changelog, engineering blog, authentication, and 9 more developer resources.'
random_paper: 20
rate_limits:
- limit_count: 3
  name: Trendyol Rate Limits
  slug: trendyol-rate-limits
score:
  band: thin
  composite: 36.0
  coverage:
    artifact_dirs: 17
    catalog_gap: 66.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.3
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 41.6
    developer_ergonomics: 44.6
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 65.8
  previous_composite: 36.3
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/trendyol/refs/heads/main/screenshots/trendyol-2026-08-17T082435.png
security:
- kind: authentication
  name: Trendyol Authentication
  slug: trendyol-authentication
  summary_line: http/oauth2 · 3 schemes
- kind: domain-security
  name: Trendyol Domain Security
  slug: trendyol-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: trendyol
tags:
- Company
- E-Commerce
- Marketplace
- Retail
- Fashion
- Turkey
- Order Management
- Fulfillment
- Logistics
- Webhook
website: https://trendyol.com
---
