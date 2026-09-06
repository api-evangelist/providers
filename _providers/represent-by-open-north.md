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
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: Find Canadian Government Representatives
  name: Represent by Open North
  slug: represent-by-open-north
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/represent-by-open-north-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://represent.opennorth.ca/
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: company
  title: ''
  type: Blog
  url: https://opennorth.ca/feed/
created: '2026-05-28'
description: Find Canadian Government Representatives
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/represent-by-open-north.png
layout: provider
modified: '2026-05-28'
name: Represent by Open North
nav: Providers
network: true
overview: 'Represent by Open North publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Government and Public APIs.


  Represent by Open North''s developer surface includes engineering blog and 3 more developer resources.'
random_paper: 17
score:
  band: minimal
  composite: 6.5
  coverage:
    artifact_dirs: 3
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
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
  previous_composite: 6.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/represent-by-open-north/refs/heads/main/screenshots/represent-by-open-north-2026-06-20T192908.png
security:
- kind: domain-security
  name: Represent By Open North Domain Security
  slug: represent-by-open-north-domain-security
  summary_line: TLSv1.2
slug: represent-by-open-north
tags:
- Government
- Public APIs
website: https://represent.opennorth.ca/
---
