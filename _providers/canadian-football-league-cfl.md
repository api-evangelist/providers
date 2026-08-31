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
- description: Official JSON API providing real-time league, team and player statistics about the CFL
  name: Canadian Football League (CFL)
  slug: canadian-football-league-cfl
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/canadian-football-league-cfl-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://api.cfl.ca/
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: company
  title: ''
  type: Blog
  url: https://www.cfl.ca/feed/
created: '2026-05-28'
description: Official JSON API providing real-time league, team and player statistics about the CFL
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/canadian-football-league-cfl.png
layout: provider
modified: '2026-05-28'
name: Canadian Football League (CFL)
nav: Providers
network: true
overview: 'Canadian Football League (CFL) publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Sports And Fitness and Public APIs.


  Canadian Football League (CFL)''s developer surface includes engineering blog and 3 more developer resources.'
random_paper: 7
score:
  band: minimal
  composite: 7.2
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
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 7.2
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/canadian-football-league-cfl/refs/heads/main/screenshots/canadian-football-league-cfl-2026-07-25T204326.png
security:
- kind: domain-security
  name: Canadian Football League Cfl Domain Security
  slug: canadian-football-league-cfl-domain-security
  summary_line: DMARC
slug: canadian-football-league-cfl
tags:
- Sports And Fitness
- Public APIs
website: http://api.cfl.ca/
---
