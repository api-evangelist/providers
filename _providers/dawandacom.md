---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''http://www.dawanda.com/'', ''status'': 301, ''note'': ''declared website redirects to https://www.etsy.com/de — a different registrable domain (dawanda.com -> etsy.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
  href: https://raw.githubusercontent.com/api-evangelist/dawandacom/refs/heads/main/security/dawandacom-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dawandacom-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://www.dawanda.com/
created: '2026-07-17'
description: DaWanda.com was a German online marketplace for handmade, unique, and custom-made products, founded in 2006 in Berlin. It connected independent makers and small designers with buyers across Germany and Europe, comparable to Etsy in the DACH region. DaWanda ceased operations on 30 August 2018 and partnered with Etsy to migrate its sellers and buyers; the www.dawanda.com domain now redirects to Etsy Germany. This profile was surfaced as a portfolio company of Insight Partners and added to the API Evangelist network as a stub. No public developer program or API surface was found during enrichment; the company is defunct and retained here as a historical/portfolio record.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dawandacom.png
layout: provider
modified: '2026-07-18'
name: DaWanda.com
nav: Providers
network: true
overview: DaWanda.com is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Marketplace, E-Commerce, Handmade, and Germany.
random_paper: 5
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
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - germany
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
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
  name: Dawandacom Domain Security
  slug: dawandacom-domain-security
  summary_line: TLSv1.2
slug: dawandacom
tags:
- Company
- Marketplace
- E-Commerce
- Handmade
- Germany
- Defunct
website: http://www.dawanda.com/
---
