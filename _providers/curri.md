---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  - sandbox
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.6
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: GraphQL API for requesting delivery quotes, booking on-demand and scheduled deliveries, managing and canceling deliveries, and tracking drivers in real time via webhooks or long polling.
  name: Curri GraphQL API
  slug: curri-graphql-api
artifact_total: 5
asyncapis:
- description: ''
  name: Curri Webhooks
  slug: curri-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.curri.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.curri.com/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.curri.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.curri.com/docs/queries-and-mutations/appendix
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.curri.com/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://help.curri.com/en/
- group: company
  title: ''
  type: Blog
  url: https://www.curri.com/blog
- group: start
  title: ''
  type: SignUp
  url: https://app.curri.com/signup/create
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.curri.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.curri.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.curri.com/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.curri.com/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/curri-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/curri-authentication.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/curri-webhooks.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/curri-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/curri-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/curri-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/curri-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/curri-conformance.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/curri-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/curri-domain-security.yml
created: '2026-07-17'
description: Curri is a last-mile and same-day delivery platform built for construction and industrial supplies. It lets distributors and suppliers dispatch on-demand drivers (Hotshots), run dedicated recurring fleets, and orchestrate a vetted nationwide carrier network including LTL freight — with smart vehicle matching, live tracking and ETAs, digital proof-of-delivery, and route planning. Curri's GraphQL API (https://api.curri.com/graphql) connects a customer's own systems to the platform so they can request quotes, book and manage deliveries, and track drivers in real time without logging into the app. Authentication is HTTP Basic with an issued API key plus a separate Sandbox key for test bookings.
image: https://www.curri.com/favicon.ico
layout: provider
modified: '2026-07-18'
name: Curri
nav: Providers
network: true
overview: 'Curri publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Vertical Software, Delivery, Logistics, and Last Mile.


  The Curri catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Curri''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, authentication, and 16 more developer resources.'
random_paper: 3
score:
  band: developing
  composite: 41.2
  coverage:
    artifact_dirs: 13
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 4.5
    contract_quality: 41.6
    developer_ergonomics: 66.1
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 7.9
  previous_composite: 41.2
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/curri/refs/heads/main/screenshots/curri-2026-07-25T210950.png
security:
- kind: authentication
  name: Curri Authentication
  slug: curri-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Curri Domain Security
  slug: curri-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Curri Trust Center
  slug: curri-trust-center
  summary_line: trust center published
slug: curri
tags:
- Company
- Vertical Software
- Delivery
- Logistics
- Last Mile
- Freight
- Construction
- Supply Chain
- GraphQL
website: https://www.curri.com/
---
