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
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/home-depot/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/red-beacon/refs/heads/main/security/red-beacon-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/red-beacon-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.redbeacon.com
created: '2026-07-17'
description: Redbeacon was a consumer home-services marketplace that connected homeowners with local service professionals — for home repair, cleaning, landscaping, handyman and similar jobs — letting people describe a job and receive quotes from vetted local pros. The company was an early venture-backed startup (with Mayfield among its investors) and was acquired by The Home Depot in 2012. The standalone Redbeacon consumer service was subsequently wound down. As of this enrichment pass the redbeacon.com domain still resolves (Cloudflare DNS, Google Workspace email) but serves no live website (origin returns HTTP 525 / 400) and publishes no developer portal, API documentation, or machine-readable API surface. This profile is retained as a historical/portfolio-graph node.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/red-beacon.png
layout: provider
modified: '2026-07-21'
name: Red Beacon
nav: Providers
network: true
overview: Red Beacon is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Home Services, Marketplace, Local Services, and Consumer.
random_paper: 8
score:
  band: minimal
  composite: 0.0
  coverage:
    artifact_dirs: 2
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
security:
- kind: domain-security
  name: Red Beacon Domain Security
  slug: red-beacon-domain-security
  summary_line: TLSv1.3
slug: red-beacon
tags:
- Company
- Home Services
- Marketplace
- Local Services
- Consumer
- Acquired
- Defunct
website: https://www.redbeacon.com
---
