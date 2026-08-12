---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.7
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Convelio Agentic Access
  operation_count: 9
  slug: convelio-agentic-access
  summary_line: 9 operations · 6 acting
api_count: 2
apis:
- description: Shipping API allow you to request a shipping estimate from our system
  name: Convelio Shipping API
  slug: convelio-shipping-api
- description: The Webhook API allows an API partner to create and manage webhooks.
  name: Convelio Webhook API
  slug: convelio-webhook-api
artifact_total: 7
asyncapis:
- description: ''
  name: Convelio Webhooks
  slug: convelio-webhooks
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/convelio-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/convelio-shipping-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/convelio-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/convelio-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/convelio-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.convelio.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.convelio.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.convelio.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.convelio.com/#tag/shipping
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.convelio.com/#section/API-key
- group: operate
  title: ''
  type: Support
  url: https://help.convelio.com/en
- group: company
  title: ''
  type: Blog
  url: https://www.convelio.com/en/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/convelio
- group: start
  title: ''
  type: SignUp
  url: https://web.convelio.com/auth/signup-email
- group: start
  title: ''
  type: Login
  url: https://web.convelio.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.convelio.com/en/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.convelio.com/en/privacy/
- group: operate
  title: ''
  type: StatusPage
  url: https://developers.convelio.com/status
- group: design
  title: ''
  type: Conventions
  url: conventions/convelio-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/convelio-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/convelio-sandbox.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/convelio-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/convelio-packages.yml
- group: design
  title: ''
  type: Components
  url: components/convelio-components.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/convelio-llms.txt
created: '2026-08-09'
description: Convelio is a Paris- and London-based tech-enabled fine art logistics company that moves high-value, fragile and oversized objects — paintings, sculpture, antiques and design — for galleries, auction houses, art fairs, dealers, collectors and online marketplaces. Its differentiator is an instant-pricing engine that returns an all-inclusive door-to-door shipping price (packing, crating, customs, road/air/sea freight, insurance and white-glove delivery) in place of the multi-day manual quoting the art-handling trade traditionally runs on. Convelio exposes that engine to partners as the Convelio Public API — a REST Shipping API (v2.0) documented with OpenAPI 3.1 at developers.convelio.com — plus an embeddable checkout widget, a web dashboard and a tracking surface, so marketplaces and auction platforms can price, book and track fine art shipments inside their own product.
image: https://www.convelio.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: convelio-mcp.yml
  slug: convelio-mcpyml
modified: '2026-08-09'
name: Convelio
nav: Providers
network: true
overview: 'Convelio publishes 2 APIs on the [APIs.io](https://apis.io/) network: Shipping API and Webhook API. Tagged areas include Company, Logistics, Shipping, Fine Art, and Freight.


  The Convelio catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Convelio''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, signup flow, and 19 more developer resources.'
random_paper: 51
score:
  band: developing
  composite: 48.4
  delta: -0.4
  facets:
    commercial_clarity: 34.2
    contract_quality: 72.4
    developer_ergonomics: 62.5
    discoverability: 87.0
    governance: 11.5
    operational_transparency: 21.1
  previous_composite: 48.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 37.9
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
security:
- kind: authentication
  name: Convelio Authentication
  slug: convelio-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Convelio Domain Security
  slug: convelio-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: convelio
tags:
- Company
- Logistics
- Shipping
- Fine Art
- Freight
- Ecommerce
- Quotes
- Webhooks
- Customs
- Insurance
website: https://www.convelio.com/
---
