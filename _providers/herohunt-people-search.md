---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: flavored
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
  score: 1.4
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: Search 1 billion people profiles across LinkedIn and GitHub for talent sourcing
  name: HeroHunt People Search
  slug: herohunt-people-search
artifact_total: 2
common:
- group: other
  title: ''
  type: AgentCard
  url: a2a/herohunt-people-search-a2a.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/herohunt-people-search-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.herohunt.ai/people-search-api
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: company
  title: ''
  type: Blog
  url: https://www.herohunt.ai/rss.xml
created: '2026-05-28'
description: Search 1 billion people profiles across LinkedIn and GitHub for talent sourcing
layout: provider
modified: '2026-05-28'
name: HeroHunt People Search
nav: Providers
network: true
overview: 'HeroHunt People Search publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Job and Public APIs.


  HeroHunt People Search''s developer surface includes engineering blog and 4 more developer resources.'
random_paper: 16
score:
  band: minimal
  composite: 7.8
  coverage:
    artifact_dirs: 4
    catalog_gap: 90.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 53.7
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 7.8
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/herohunt-people-search/refs/heads/main/screenshots/herohunt-people-search-2026-06-20T182646.png
security:
- kind: domain-security
  name: Herohunt People Search Domain Security
  slug: herohunt-people-search-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: herohunt-people-search
tags:
- Job
- Public APIs
website: https://www.herohunt.ai/people-search-api
---
