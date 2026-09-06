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
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/westwing-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.westwing.de
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/westwing-llms.txt
created: '2026-07-17'
description: Westwing is Europe's number one "Beautiful Living" e-commerce company, present in more than 20 European countries. It is a premium one-stop Home & Living destination that offers design lovers a carefully curated selection of the best design brands alongside its own Westwing Collection, created by an in-house team in Munich, spanning furniture, sofas, lighting, beds, rugs, textiles, outdoor and home accessories. Westwing (Westwing Group SE) is a publicly listed company and was surfaced in the API Evangelist network as a portfolio company of HV Capital and Point Nine. It publishes no public developer API; its primary machine-facing surface is a root-level /llms.txt policy that governs how LLMs and agents may use its catalog and editorial content.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/westwing.png
layout: provider
modified: '2026-07-21'
name: Westwing
nav: Providers
network: true
overview: Westwing is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, E-Commerce, Home & Living, and Furniture.
random_paper: 6
score:
  band: minimal
  composite: 5.7
  coverage:
    artifact_dirs: 4
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
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
  previous_composite: 5.7
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/westwing/refs/heads/main/screenshots/westwing-2026-09-02T170640.png
security:
- kind: domain-security
  name: Westwing Domain Security
  slug: westwing-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: westwing
tags:
- Company
- Consumer
- E-Commerce
- Home & Living
- Furniture
- Interior Design
- Retail
- Europe
website: https://www.westwing.de
---
