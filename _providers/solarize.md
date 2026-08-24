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
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.1
  scored_at: '2026-08-24'
api_count: 1
apis:
- description: REST API for the Solarize meter-to-cash platform — customers, sites, meters, contracts, measurements, readings, invoices, payments, pricing, and outgoing webhooks. JSON over HTTPS, JWT bearer auth, of
  name: Solarize API
  slug: solarize-api
artifact_total: 6
asyncapis:
- description: Outgoing webhooks deliver entity lifecycle and bill-run events to an external endpoint configured in the Solarize app (Settings > Notifications), where the endpoint URL, optional headers, and triggeri
  name: Solarize Outgoing Webhooks
  slug: solarize-webhooks-asyncapi
common:
- group: company
  title: ''
  type: Website
  url: https://www.solarize.de/en/solution
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api-docs.solarize.energy/
- group: docs
  title: ''
  type: Documentation
  url: https://api-docs.solarize.energy/
- group: docs
  title: ''
  type: APIReference
  url: https://api-docs.solarize.energy/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://api-docs.solarize.energy/customer-onboarding
- group: operate
  title: ''
  type: Support
  url: https://www.solarize.de/en/contact?hsLang=en
- group: company
  title: ''
  type: Blog
  url: https://www.solarize.de/blog?hsLang=en
- group: start
  title: ''
  type: Login
  url: https://app.solarize.energy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.solarize.de/en/solution
- group: operate
  title: ''
  type: StatusPage
  url: https://solarize.statuspage.io
- group: auth
  title: ''
  type: Authentication
  url: authentication/solarize-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/solarize-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/solarize-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/solarize-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/solarize-lifecycle.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/solarize-webhooks-asyncapi.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/solarize-webhooks-asyncapi.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/solarize-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/solarize-mcp.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/solarize-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/solarize-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/solarize-llms.txt
created: '2026-07-17'
description: Solarize is a German energy software company offering a meter-to-cash billing platform as a software-as-a-service for utilities, municipal utilities (Stadtwerke), and energy providers. The platform converts metering data into a revenue stream through automated billing and invoicing, metering data management, monitoring and reporting, and flexible electricity-product configuration. Solarize exposes a REST API at api.solarize.energy covering customers, sites, meters, contracts, measurements, readings, invoices, payments, pricing, and outgoing webhooks, enabling open-architecture integration with ERP, CRM, and metering-operator systems.
image: https://api-docs.solarize.energy/_next/static/media/solarize-api-docs.b9d189f5.png
layout: provider
mcp_servers:
- description: ''
  name: Solarize MCP Server
  slug: solarize-mcp-server
modified: '2026-07-21'
name: Solarize
nav: Providers
network: true
overview: 'Solarize publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Billing, Metering, and Utilities.


  The Solarize catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Solarize''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, authentication, and 15 more developer resources.'
random_paper: 12
rate_limits:
- limit_count: 1
  name: Solarize Rate Limits
  slug: solarize-rate-limits
score:
  band: developing
  composite: 41.6
  delta: 0.0
  facets:
    access_clarity: 17.1
    commercial_clarity: 17.1
    contract_governance: 4.5
    contract_quality: 45.1
    developer_ergonomics: 57.1
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 52.6
  previous_composite: 41.6
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 23.0
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
security:
- kind: authentication
  name: Solarize Authentication
  slug: solarize-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Solarize Domain Security
  slug: solarize-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: solarize
tags:
- Company
- Energy
- Billing
- Metering
- Utilities
- Meter-to-Cash
- Software-as-a-Service
website: https://www.solarize.de/en/solution
---
