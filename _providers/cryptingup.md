---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://www.cryptingup.com/apidoc/#introduction'', ''status'': 302, ''note'': ''declared website redirects to hugedomains.com — a domain sales/parking service, so the domain has lapsed rather than moved to an acquirer (probed 2026-09-03, roadmap#169)''}'
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
- description: Cryptocurrency data
  name: CryptingUp
  slug: cryptingup
artifact_total: 2
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cryptingup/refs/heads/main/security/cryptingup-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cryptingup-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cryptingup.com/apidoc/#introduction
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Cryptocurrency data
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cryptingup.png
layout: provider
modified: '2026-09-15'
name: CryptingUp
nav: Providers
network: true
overview: CryptingUp publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Cryptocurrency, Public APIs, and Defunct.
random_paper: 9
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
screenshot: https://raw.githubusercontent.com/api-evangelist/cryptingup/refs/heads/main/screenshots/cryptingup-2026-06-20T175306.png
security:
- kind: domain-security
  name: Cryptingup Domain Security
  slug: cryptingup-domain-security
  summary_line: TLSv1.3
slug: cryptingup
tags:
- Cryptocurrency
- Public APIs
- Defunct
website: https://www.cryptingup.com/apidoc/#introduction
---
