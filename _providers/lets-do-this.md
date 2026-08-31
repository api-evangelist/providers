---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: 'Live GraphQL endpoint backing the Let''s Do This consumer marketplace. Discovered by probe, not published as a developer product: no documentation, no published schema, no documented authentication and'
  name: Let's Do This GraphQL (undocumented)
  slug: lets-do-this-graphql-undocumented
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lets-do-this-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.letsdothis.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.letsdothis.com/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/lets-do-this-llms.txt
created: '2026-07-17'
description: 'Let''s Do This is an endurance-events marketplace where participants discover and register for mass-participation sport — marathons, road races, trail runs, triathlons, obstacle races and cycling events — across the United Kingdom and the United States. The platform covers event discovery, entry purchase and entry management, team entries, memberships, referral credits and discount codes, and it works with event organisers and charity partners who list and sell places through it. Backed by EQT Ventures. As of July 2026 Let''s Do This publishes no public API program: there is no developer portal, API documentation, machine-readable specification, SDK or webhook surface. A live but undocumented GraphQL endpoint backs the consumer marketplace with introspection disabled.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lets-do-this.png
layout: provider
modified: '2026-07-19'
name: Let's Do This
nav: Providers
network: true
overview: Let's Do This publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fitness Tech, Endurance Sports, Event, and Event Registration.
random_paper: 5
score:
  band: minimal
  composite: 8.6
  coverage:
    artifact_dirs: 5
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 8.6
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lets-do-this/refs/heads/main/screenshots/lets-do-this-2026-07-25T224933.png
security:
- kind: domain-security
  name: Lets Do This Domain Security
  slug: lets-do-this-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: lets-do-this
tags:
- Company
- Fitness Tech
- Endurance Sports
- Event
- Event Registration
- Marketplace
- Ticketing
- Consumer
website: https://www.letsdothis.com/
---
