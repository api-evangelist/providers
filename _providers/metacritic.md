---
access_model:
  confidence: medium
  label: Paid (free trial)
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  trial: true
  try_now: false
agent_readiness:
  band: human-only
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.0
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: The official Metacritic API, delivered through Fabric Origin (formerly IVA / Gracenote), provides structured access to Metascores, user scores, and individual critic reviews for movies and TV shows. R
  name: Metacritic API (Fabric Origin)
  slug: metacritic-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/metacritic-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.metacritic.com/
- group: start
  title: ''
  type: Portal
  url: https://developer.origin.fabricdata.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.origin.fabricdata.com/origin/apis-all/metacritic-api-docs/metacritic
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.metacritic.com/about/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.metacritic.com/about/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://metacritichelp.zendesk.com/hc/en-us
- group: operate
  title: ''
  type: Contact
  url: https://www.fabricdata.com/contact
created: '2026-06-13'
description: Metacritic is a review aggregator that collects critic and user scores for games, movies, TV shows, and music, computing a weighted Metascore for each title. The Metacritic API (provided via Fabric Origin / IVA / Gracenote) gives programmatic access to Metascores, user scores, individual critic reviews, publication details, and entertainment rankings for movies and television. Unofficial community-built wrappers also expose game, movie, and TV data from Metacritic's public backend.
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/metacritic.png
layout: provider
modified: '2026-06-13'
name: Metacritic
nav: Providers
network: true
overview: 'Metacritic publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Entertainment, Reviews, Metascore, Games, and Movies.


  Metacritic''s developer surface includes developer portal, documentation, support, and 5 more developer resources.'
plans:
- name: Plans
  plan_count: 1
  slug: plans
random_paper: 11
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
score:
  band: emerging
  composite: 22.2
  coverage:
    artifact_dirs: 7
    catalog_gap: 67.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 47.6
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 22.2
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/metacritic/refs/heads/main/screenshots/metacritic-2026-06-20T185245.png
security:
- kind: domain-security
  name: Metacritic Domain Security
  slug: metacritic-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: metacritic
tags:
- Entertainment
- Reviews
- Metascore
- Games
- Movies
- Television
- Music
- Review Aggregator
- Critic Scores
- User Scores
website: https://www.metacritic.com/
---
