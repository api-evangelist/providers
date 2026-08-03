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
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 36.5
  scored_at: '2026-08-03'
api_count: 1
apis:
- description: Loggi's REST integration platform for freight quotation, shipment creation (sync/async), label generation, package update/cancel, package details, real-time tracking, webhooks, integrator management a
  name: Loggi Platform API
  slug: loggi-platform-api
artifact_total: 5
asyncapis:
- description: ''
  name: Loggi Webhooks
  slug: loggi-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.loggi.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.api.loggi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.api.loggi.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.api.loggi.com/reference/nossa-documenta%C3%A7%C3%A3o
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.api.loggi.com/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://ajuda.loggi.com/
- group: start
  title: ''
  type: SignUp
  url: https://www.loggi.com/contas/criar/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.loggi.com/termos-cliente/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.loggi.com/aviso-privacidade-clientes/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/loggi-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/loggi-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/loggi-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/loggi-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/loggi-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/loggi-lifecycle.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/loggi-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/loggi-mcp.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/loggi-error-codes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/loggi-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/loggi-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/loggi-packages.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/loggi-domain-security.yml
created: '2026-07-17'
description: 'Loggi is the largest private shipping and last-mile logistics company in Brazil, operating its own delivery network across more than 4,000 municipalities. Loggi publishes a REST developer platform (docs.api.loggi.com) that lets partner platforms and integrators estimate freight prices and delivery times, create single or multiple shipments (synchronously or asynchronously), generate Loggi shipping labels, update or cancel packages, retrieve package details, track packages in real time, and receive delivery status updates via webhooks. Authentication is OAuth2 client-credentials style (client_id/client_secret exchanged for a JWT). Backed by Fifth Wall, GGV Capital and SoftBank Vision Fund. Sector: logistics.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/loggi.png
layout: provider
mcp_servers:
- description: ''
  name: loggi-mcp.yml
  slug: loggi-mcpyml
modified: '2026-07-20'
name: Loggi
nav: Providers
network: true
overview: 'Loggi publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Logistics, Shipping, Last-Mile Delivery, and Freight.


  The Loggi catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Loggi''s developer surface includes documentation, API reference, getting-started guide, support, signup flow, authentication, and 16 more developer resources.'
random_paper: 55
score:
  band: thin
  composite: 41.3
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 51.6
    developer_ergonomics: 52.2
    discoverability: 87.0
    governance: 3.1
    operational_transparency: 15.8
  previous_composite: 41.3
  provenance:
    conformance: derived
    mcp: derived
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/loggi/refs/heads/main/screenshots/loggi-2026-07-25T225453.png
security:
- kind: authentication
  name: Loggi Authentication
  slug: loggi-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Loggi Domain Security
  slug: loggi-domain-security
  summary_line: TLSv1.3 · DMARC
slug: loggi
tags:
- Company
- Logistics
- Shipping
- Last-Mile Delivery
- Freight
- Tracking
- Brazil
website: https://www.loggi.com/
---
