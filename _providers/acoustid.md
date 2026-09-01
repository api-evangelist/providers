---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: REST API for audio fingerprint lookup and submission. Accepts Chromaprint-generated fingerprints and returns AcoustID track identifiers along with linked MusicBrainz metadata including recordings, art
  name: AcoustID Web Service API
  slug: acoustid-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/acoustid-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://acoustid.org/
- group: docs
  title: ''
  type: Documentation
  url: https://acoustid.org/webservice
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/acoustid
- group: company
  title: ''
  type: Blog
  url: https://blog.acoustid.org/
- group: commercial
  title: ''
  type: Pricing
  url: https://acoustid.biz/
- group: other
  title: ''
  type: X
  url: https://twitter.com/acoustid
- group: commercial
  title: ''
  type: Plans
  url: plans/acoustid-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/acoustid-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/acoustid-finops.yml
created: '2026-06-13'
description: AcoustID is an open-source audio fingerprinting service providing a REST API for identifying music tracks by audio fingerprint and linking results to MusicBrainz metadata records. Built on the Chromaprint library, it offers a crowdsourced fingerprint database free for non-commercial use, with commercial plans available through AcoustID OÜ.
finops:
- name: Acoustid Finops
  service_category: ''
  slug: acoustid-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/acoustid.png
layout: provider
modified: '2026-06-13'
name: AcoustID
nav: Providers
network: true
overview: 'AcoustID publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Audio, Fingerprinting, Music, MusicBrainz, and Open-Source.


  AcoustID''s developer surface includes documentation, engineering blog, pricing, and 7 more developer resources.'
plans:
- name: Acoustid Plans Pricing
  plan_count: 5
  slug: acoustid-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 2
  name: Acoustid Rate Limits
  slug: acoustid-rate-limits
score:
  band: emerging
  composite: 22.6
  coverage:
    artifact_dirs: 7
    catalog_gap: 55.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 22.6
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/acoustid/refs/heads/main/screenshots/acoustid-2026-06-20T163933.png
security:
- kind: domain-security
  name: Acoustid Domain Security
  slug: acoustid-domain-security
  summary_line: TLSv1.3 · HSTS
slug: acoustid
tags:
- Audio
- Fingerprinting
- Music
- MusicBrainz
- Open-Source
- Identification
website: https://acoustid.org/
---
