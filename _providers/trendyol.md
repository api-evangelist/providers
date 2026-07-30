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
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.6
  scored_at: '2026-07-28'
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
- description: ''
  name: trendyol-mcp.yml
  slug: trendyol-mcpyml
modified: '2026-07-21'
name: Trendyol
nav: Providers
network: true
overview: 'Trendyol publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Ecommerce, Marketplace, Retail, and Fashion.


  The Trendyol catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Trendyol''s developer surface includes documentation, API reference, getting-started guide, support, changelog, engineering blog, authentication, and 9 more developer resources.'
random_paper: 61
rate_limits:
- limit_count: 3
  name: Trendyol Rate Limits
  slug: trendyol-rate-limits
score:
  band: developing
  composite: 43.1
  delta: 4.8
  facets:
    commercial_clarity: 0.0
    contract_quality: 51.6
    developer_ergonomics: 56.0
    discoverability: 87.0
    governance: 3.1
    operational_transparency: 76.3
  previous_composite: 38.3
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
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
- Ecommerce
- Marketplace
- Retail
- Fashion
- Turkey
- Order Management
- Fulfillment
- Logistics
- Webhooks
website: https://trendyol.com
---
