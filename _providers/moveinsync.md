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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
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
  score: 19.8
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: JWT-authenticated REST and webhook API for employee-transport integration. Partners authenticate at api.moveinsync.com/auth/token (OAuth2 client-credentials over HTTP Basic) to obtain a 24-hour JWT, t
  name: MoveInSync Integration API
  slug: moveinsync-integration-api
artifact_total: 4
asyncapis:
- description: ''
  name: Moveinsync Webhooks
  slug: moveinsync-webhooks
common:
- group: auth
  title: ''
  type: Authentication
  url: authentication/moveinsync-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/moveinsync-conventions.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/moveinsync-webhooks.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/moveinsync-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://moveinsync.com/us
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/moveinsync-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/moveinsync-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/moveinsync-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://helpcenter.moveinsync.com/support/home
- group: docs
  title: ''
  type: Documentation
  url: https://helpcenter.moveinsync.com/support/solutions
- group: operate
  title: ''
  type: Support
  url: https://helpcenter.moveinsync.com/support/home
- group: company
  title: ''
  type: Blog
  url: https://moveinsync.com/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://moveinsync.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://moveinsync.com/terms-of-use
- group: company
  title: ''
  type: Website
  url: https://moveinsync.com/
created: '2026-07-17'
description: MoveInSync is an enterprise employee-commute and workplace-management SaaS platform. It automates end-to-end corporate transportation — fixed-route shuttles, flexi rideshare, on-demand campus rides, corporate carpool, parking management, and the WorkInSync hybrid-workplace suite — with smart routing, live tracking, safety workflows, and billing. The platform serves more than 1M commuters across 100,000+ vehicles in 39 countries for 400+ enterprises, including 112+ Fortune 500 companies. MoveInSync exposes a JWT-authenticated REST and webhook integration API at api.moveinsync.com, including the Rentlz booking-management APIs used by external transport vendors. Backed by Bessemer Venture Partners.
image: https://moveinsync.com/wp-content/uploads/2023/01/cropped-header-logo-270x270.png
layout: provider
modified: '2026-07-20'
name: MoveInSync
nav: Providers
network: true
overview: 'MoveInSync publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Vertical Software, Transportation, Employee Commute, and Mobility.


  The MoveInSync catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  MoveInSync''s developer surface includes authentication, documentation, support, engineering blog, and 11 more developer resources.'
random_paper: 7
score:
  band: thin
  composite: 34.9
  coverage:
    artifact_dirs: 9
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 42.7
    developer_ergonomics: 38.1
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 7.9
  previous_composite: 34.9
  provenance:
    conformance: first-party
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/moveinsync/refs/heads/main/screenshots/moveinsync-2026-08-07T184350.png
security:
- kind: authentication
  name: Moveinsync Authentication
  slug: moveinsync-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Moveinsync Domain Security
  slug: moveinsync-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: moveinsync
tags:
- Company
- Vertical Software
- Transportation
- Employee Commute
- Mobility
- Fleet Management
- Parking
- Workplace Management
- Ridesharing
- Logistics
website: https://moveinsync.com/
---
