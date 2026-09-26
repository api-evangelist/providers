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
  band: agent-aware
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
    event_surface_described: unknown
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 16.8
  scored_at: '2026-09-25'
api_count: 1
apis:
- description: Post to and update maintenance and incidents on your status page through an HTTP REST API
  name: Instatus
  slug: instatus
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/instatus/refs/heads/main/vendor-facets/instatus-vendor-facets.yml
  title: ''
  type: VendorFacets
  url: vendor-facets/instatus-vendor-facets.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/instatus/refs/heads/main/security/instatus-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/instatus-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://instatus.com/help/api
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: company
  title: ''
  type: Blog
  url: https://instatus.com/blog
created: '2026-05-28'
description: Post to and update maintenance and incidents on your status page through an HTTP REST API
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/instatus.png
layout: provider
modified: '2026-05-30'
name: Instatus
nav: Providers
network: true
overview: 'Instatus publishes 1 API on the [APIs.io](https://apis.io/) network: Instatus. Tagged areas include Business and Public APIs.


  Instatus'' developer surface includes engineering blog and 4 more developer resources.'
random_paper: 11
score:
  band: emerging
  composite: 15.9
  coverage:
    artifact_dirs: 5
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.1
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 41.5
    developer_ergonomics: 11.9
    discoverability: 46.4
    operational_transparency: 0.0
  previous_composite: 19.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/instatus/refs/heads/main/screenshots/instatus-2026-06-20T183418.png
security:
- kind: domain-security
  name: Instatus Domain Security
  slug: instatus-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: instatus
tags:
- Business
- Public APIs
website: https://instatus.com/help/api
---
