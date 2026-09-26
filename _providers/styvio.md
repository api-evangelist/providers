---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://www.Styvio.com'', ''status'': 302, ''note'': ''declared website redirects to hugedomains.com — a domain sales/parking service, so the domain has lapsed rather than moved to an acquirer (probed 2026-09-03, roadmap#169)''}'
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
api_count: 1
apis:
- description: Realtime and historical stock data and current stock sentiment
  name: Styvio
  slug: styvio
artifact_total: 2
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/styvio/refs/heads/main/security/styvio-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/styvio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.Styvio.com
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Realtime and historical stock data and current stock sentiment
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/styvio.png
layout: provider
modified: '2026-09-15'
name: Styvio
nav: Providers
network: true
overview: Styvio publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Finance, Public APIs, and Defunct.
random_paper: 4
score:
  band: minimal
  composite: 0.0
  coverage:
    artifact_dirs: 3
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
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
screenshot: https://raw.githubusercontent.com/api-evangelist/styvio/refs/heads/main/screenshots/styvio-2026-06-20T194628.png
security:
- kind: domain-security
  name: Styvio Domain Security
  slug: styvio-domain-security
  summary_line: TLSv1.3
slug: styvio
tags:
- Finance
- Public APIs
- Defunct
website: https://www.Styvio.com
---
