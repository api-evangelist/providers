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
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-09-25'
api_count: 0
artifact_total: 1
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/shelbytv/refs/heads/main/security/shelbytv-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/shelbytv-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/shelbytv/refs/heads/main/well-known/shelbytv-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/shelbytv-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/shelbytv/refs/heads/main/well-known/shelbytv-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/shelbytv-security.txt
- group: company
  title: ''
  type: Website
  url: https://shelby.tv/
created: '2026-07-17'
description: Shelby.tv was a Techstars-backed social video discovery startup that let people find, share, and watch videos surfaced from their social networks. The company has shut down; shelby.tv now serves only a founders' farewell page and no longer operates any product, developer program, or public API. Surfaced as a Techstars portfolio company and enriched by the API Evangelist pipeline, which confirmed there is no API surface to catalog.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/shelbytv.png
layout: provider
modified: '2026-07-21'
name: Shelby.tv
nav: Providers
network: true
overview: Shelby.tv is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Video, Social, Video Discovery, and Media.
random_paper: 1
score:
  band: minimal
  composite: 0.0
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 0.0
    operational_transparency: 0.0
  lifecycle: defunct
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/shelbytv/refs/heads/main/screenshots/shelbytv-2026-09-02T155125.png
security:
- kind: domain-security
  name: Shelbytv Domain Security
  slug: shelbytv-domain-security
  summary_line: TLSv1.3 · HSTS
slug: shelbytv
tags:
- Company
- Video
- Social
- Video Discovery
- Media
- Defunct
website: https://shelby.tv/
---
