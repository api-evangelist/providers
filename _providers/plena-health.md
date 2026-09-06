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
  url: security/plena-health-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.plena.health/
created: '2026-07-17'
description: Plena Health is an AI operating system for specialty medical practices, founded in 2025 and part of Y Combinator's Spring 2026 batch. Plena automates the complex administrative workflows a clinic's staff shouldn't have to do — referrals, fax intake, patient calls, scheduling, prior authorization, procedure compliance, and collections — end to end, running in the background across the EHRs, clearinghouses, and other systems a practice already uses, rather than requiring the practice to adopt new software. Founded by Eyad Abdalla (CEO) and Ahmed Al Mudarris (CTO) and based in San Francisco, the company reports operating across six specialties in eight states. This profile was surfaced as a Y Combinator portfolio company and added to the API Evangelist network; as of this enrichment pass Plena publishes only a marketing site (a single-page React application) with no public API, developer portal, documentation, or well-known discovery surface.
image: https://www.plena.health/assets/logo-mark.png
layout: provider
modified: '2026-07-20'
name: Plena Health
nav: Providers
network: true
overview: Plena Health is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Healthcare, Medical Practice, and Artificial Intelligence.
random_paper: 6
score:
  band: minimal
  composite: 3.3
  coverage:
    artifact_dirs: 2
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
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 3.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/plena-health/refs/heads/main/screenshots/plena-health-2026-09-02T151513.png
security:
- kind: domain-security
  name: Plena Health Domain Security
  slug: plena-health-domain-security
  summary_line: TLSv1.3 · DMARC
slug: plena-health
tags:
- Company
- Health
- Healthcare
- Medical Practice
- Artificial Intelligence
- Automation
- Workflows
- Y Combinator
website: https://www.plena.health/
---
