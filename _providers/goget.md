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
  scored_at: '2026-08-24'
api_count: 1
apis:
- description: Automate on-demand deliveries with GoGet — create, update, and cancel jobs, estimate fees, check coverage and availability, track GoGetters live, and receive job-status webhooks. Authenticated with an
  name: GoGet Delivery API
  slug: goget-delivery-api
artifact_total: 5
asyncapis:
- description: ''
  name: Goget Jobs Webhooks
  slug: goget-jobs-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://goget.my
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api-docs.goget.my/
- group: docs
  title: ''
  type: Documentation
  url: https://api-docs.goget.my/
- group: docs
  title: ''
  type: APIReference
  url: https://api-docs.goget.my/
- group: start
  title: ''
  type: GettingStarted
  url: https://api-docs.goget.my/
- group: start
  title: ''
  type: SignUp
  url: https://app.goget.my/
- group: operate
  title: ''
  type: Support
  url: https://support.goget.my/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://goget.my/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://goget.my/business/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://goget.my/terms_conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://goget.my/privacy_policy
- group: operate
  title: ''
  type: StatusPage
  url: https://gogetmy.instatus.com/
- group: auth
  title: ''
  type: Authentication
  url: authentication/goget-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/goget-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/goget-lifecycle.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/goget-jobs-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/goget-mcp.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/goget-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/goget-data-model.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/goget-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/goget-domain-security.yml
created: '2026-07-17'
description: GoGet is a Malaysian on-demand workforce and delivery technology company whose network of verified workers, called GoGetters, powers same-day delivery, dispatch, and blended-workforce staffing for more than 10,000 businesses across Klang Valley, Penang, Negeri Sembilan and Johor Bahru. Beyond its consumer and business apps, GoGet exposes the GoGet Delivery API so merchants can automate on-demand deliveries end to end — create and manage jobs, estimate delivery fees, verify coverage and availability, track GoGetters live, and receive job lifecycle events via webhooks. Integration is free and typically completed in one to two weeks. GoGet is backed by 500 Global.
image: https://web.goget.my/assets/images/og/logo_1200_630.png
layout: provider
mcp_servers:
- description: ''
  name: GoGet MCP Server
  slug: goget-mcp-server
modified: '2026-07-19'
name: GoGet
nav: Providers
network: true
overview: 'GoGet publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Delivery, Logistics, On-Demand, and Gig Economy.


  The GoGet catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  GoGet''s developer surface includes documentation, API reference, getting-started guide, signup flow, support, engineering blog, pricing, and 14 more developer resources.'
random_paper: 9
score:
  band: thin
  composite: 37.6
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 45.1
    developer_ergonomics: 57.1
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 37.6
  provenance:
    mcp: derived
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/goget/refs/heads/main/screenshots/goget-2026-07-25T220015.png
security:
- kind: authentication
  name: Goget Authentication
  slug: goget-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Goget Domain Security
  slug: goget-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: goget
tags:
- Company
- Delivery
- Logistics
- On-Demand
- Gig Economy
- Workforce
- Dispatch
- Malaysia
- Webhook
website: https://goget.my
---
