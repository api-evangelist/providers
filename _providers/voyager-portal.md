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
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 40.5
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: REST API for managing voyages and workflows on the Voyager Portal maritime operations platform. Resources include voyages (schedules, cargoes, documents, categories, models), claims and claim port-cal
  name: Voyager Portal Public API
  slug: voyager-portal-public-api
artifact_total: 5
asyncapis:
- description: ''
  name: Voyager Portal Webhooks
  slug: voyager-portal-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://voyagerportal.com/
- group: docs
  title: ''
  type: Documentation
  url: https://gitlab.com/voyager-portal/voyager-public-api/-/wikis/home
- group: docs
  title: ''
  type: APIReference
  url: https://gitlab.com/voyager-portal/voyager-public-api/-/wikis/home
- group: start
  title: ''
  type: GettingStarted
  url: https://gitlab.com/voyager-portal/voyager-public-api/-/wikis/Authentication
- group: start
  title: ''
  type: Login
  url: https://app.voyagerportal.com/
- group: company
  title: ''
  type: Blog
  url: https://www.voyagerportal.com/resources/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.voyagerportal.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.voyagerportal.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.voyagerportal.com/privacy/
- group: build
  title: ''
  type: SourceCode
  url: https://gitlab.com/voyager-portal
- group: auth
  title: ''
  type: Authentication
  url: authentication/voyager-portal-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/voyager-portal-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/voyager-portal-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/voyager-portal-lifecycle.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/voyager-portal-webhooks.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/voyager-portal-well-known.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/voyager-portal-sandbox.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/voyager-portal-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/voyager-portal-mcp.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/voyager-portal-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/voyager-portal-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/voyager-portal-domain-security.yml
created: '2026-07-17'
description: Voyager Portal is an AI-powered voyage and demurrage management platform for bulk commodity charterers, traders, brokers, and manufacturers, streamlining maritime shipping workflows from pre-fixture planning through post-fixture claim resolution. The platform provides AI-driven demurrage claims management and laytime calculations, cargo allocation, AIS vessel tracking, ETA tracking, noon reporting, and analytics, and exposes a documented public REST API for managing voyages, cargoes, claims, SOFs, vessels, ports, and workflows, plus outbound webhooks.
image: https://www.voyagerportal.com/wp-content/uploads/2025/08/teste-1.png
layout: provider
mcp_servers:
- description: ''
  name: voyager-portal-mcp.yml
  slug: voyager-portal-mcpyml
modified: '2026-07-21'
name: Voyager Portal
nav: Providers
network: true
overview: 'Voyager Portal publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Maritime, Shipping, Logistics, and Demurrage.


  The Voyager Portal catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Voyager Portal''s developer surface includes documentation, API reference, getting-started guide, engineering blog, authentication, sandbox, and 16 more developer resources.'
random_paper: 10
score:
  band: thin
  composite: 41.5
  delta: 5.8
  facets:
    commercial_clarity: 34.2
    contract_quality: 51.6
    developer_ergonomics: 47.8
    discoverability: 87.0
    governance: 3.1
    operational_transparency: 23.7
  previous_composite: 35.7
  provenance:
    conformance: derived
    mcp: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: rising
security:
- kind: authentication
  name: Voyager Portal Authentication
  slug: voyager-portal-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Voyager Portal Domain Security
  slug: voyager-portal-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: voyager-portal
tags:
- Company
- Maritime
- Shipping
- Logistics
- Demurrage
- Laytime
- Voyages
- Workflows
- Bulk Commodities
website: https://voyagerportal.com/
---
