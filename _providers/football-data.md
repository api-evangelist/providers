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
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: Football data with matches info, players, teams, and competitions
  name: Football-Data
  slug: football-data
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/football-data-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.football-data.org
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: company
  title: ''
  type: Blog
  url: https://www.football-data.org/blog
created: '2026-05-28'
description: Football data with matches info, players, teams, and competitions
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/football-data.png
layout: provider
modified: '2026-05-28'
name: Football-Data
nav: Providers
network: true
overview: 'Football-Data publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Sports And Fitness and Public APIs.


  Football-Data''s developer surface includes engineering blog and 3 more developer resources.'
random_paper: 4
score:
  band: minimal
  composite: 8.1
  coverage:
    artifact_dirs: 3
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 8.1
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/football-data/refs/heads/main/screenshots/football-data-2026-06-20T181411.png
security:
- kind: domain-security
  name: Football Data Domain Security
  slug: football-data-domain-security
  summary_line: TLSv1.2 · DMARC
slug: football-data
tags:
- Sports And Fitness
- Public APIs
website: https://www.football-data.org
---
