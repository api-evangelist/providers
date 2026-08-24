---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 48.1
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 165
  human_in_the_loop: 0
  name: Leaflink Agentic Access
  operation_count: 380
  slug: leaflink-agentic-access
  summary_line: 380 operations · 165 acting
api_count: 2
apis:
- description: The current LeafLink REST API, version 2022-10-31. 182 paths and 269 operations covering products and catalog, customers, brands, inventory (CQRS commands + measurement queries), payments and invoices
  name: LeafLink API
  slug: api
- description: 'The legacy LeafLink Marketplace V2 REST API, currently at release 2.39.0. 66 paths and 111 operations for brands and retailers: orders received, buyer orders, line items, order payments and event logs'
  name: LeafLink Marketplace V2 API
  slug: marketplace-v2
artifact_total: 9
asyncapis:
- description: ''
  name: Leaflink Webhooks
  slug: leaflink-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.leaflink.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.leaflink.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.leaflink.com/api/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.leaflink.com/api/ref/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.leaflink.com/api/getting-started/
- group: operate
  title: ''
  type: Support
  url: https://developer.leaflink.com/support/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.leaflink.com/
- group: company
  title: ''
  type: Blog
  url: https://www.leaflink.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.leaflink.com/blog/feed/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/LeafLink
- group: commercial
  title: ''
  type: Pricing
  url: https://www.leaflink.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://app.leaflink.com/signup/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.leaflink.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.leaflink.com/privacy-policy/
- group: company
  title: ''
  type: About
  url: https://www.leaflink.com/about-us/
- group: auth
  title: ''
  type: Authentication
  url: authentication/leaflink-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/leaflink-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/leaflink-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/leaflink-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/leaflink-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/leaflink-sandbox.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/leaflink-rate-limits.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/leaflink-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/leaflink-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/leaflink-packages.yml
- group: design
  title: ''
  type: Components
  url: components/leaflink-components.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/leaflink-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/leaflink-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/leaflink-agentic-access.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/leaflink-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/leaflink-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.leaflink.com/
created: '2026-08-01'
description: LeafLink is the wholesale cannabis marketplace and B2B commerce platform connecting licensed cannabis brands, distributors and retailers across roughly 30 US markets. The platform bundles a wholesale marketplace, order management, payments and net terms (LeafLink Financial), logistics and transportation, inventory management, seed-to-sale traceability integration, compliance and licensing, advertising and market insights into one system of record for regulated cannabis wholesale. LeafLink publishes a public REST API at api.leaflink.com — the current dated version 2022-10-31, authenticated with JWT bearer tokens, spanning 182 paths and 269 operations across products, orders, customers, inventory, payments, logistics, traceability, compliance, taxes and messaging — alongside a legacy Marketplace V2 API at app.leaflink.com/api/v2 with 66 paths and 111 operations. Both are documented with OpenAPI on the LeafLink Developer Hub, and the platform supports HMAC-signed webhooks for order
  and product events.
image: https://www.leaflink.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: LeafLink MCP Server
  slug: leaflink-mcp-server
modified: '2026-08-01'
name: LeafLink
nav: Providers
network: true
overview: 'LeafLink publishes 2 APIs on the [APIs.io](https://apis.io/) network, including Marketplace V2 API, and 1 more. Tagged areas include Cannabis, Wholesale, B2B Marketplace, Supply Chain, and Payments.


  The LeafLink catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  LeafLink''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 26 more developer resources.'
random_paper: 19
rate_limits:
- limit_count: 3
  name: Leaflink Rate Limits
  slug: leaflink-rate-limits
score:
  band: strong
  composite: 58.5
  delta: 0.0
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 16.7
    contract_quality: 62.0
    developer_ergonomics: 66.1
    discoverability: 75.9
    governance: 16.7
    operational_transparency: 57.9
  previous_composite: 58.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 50.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 46.9
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/leaflink/refs/heads/main/screenshots/leaflink-2026-08-07T171512.png
security:
- kind: authentication
  name: Leaflink Authentication
  slug: leaflink-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Leaflink Domain Security
  slug: leaflink-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Leaflink Trust Center
  slug: leaflink-trust-center
  summary_line: trust center published
slug: leaflink
tags:
- Cannabis
- Wholesale
- B2B Marketplace
- Supply Chain
- Payments
- Logistics
- Inventory
- Compliance
- Traceability
- E-Commerce
- Distribution
- Retail
website: https://www.leaflink.com/
---
