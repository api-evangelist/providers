---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://www.beckon.com'', ''status'': 302, ''note'': ''declared website redirects to https://ignitetech.ai:443/ — a different registrable domain (beckon.com -> ignitetech.ai), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
- group: company
  title: ''
  type: Website
  url: https://www.beckon.com
- group: auth
  title: ''
  type: DomainSecurity
  url: security/beckon-domain-security.yml
created: '2026-07-17'
description: Beckon was a marketing analytics and marketing performance measurement SaaS platform, founded in 2011 and headquartered in San Mateo, California. Its product automated the ingestion, harmonization, and normalization of marketing data from across paid, owned, and earned channels into a single unified set of metrics and dashboards, giving marketing teams a "total marketing intelligence" view of spend, performance, and ROI. Beckon was venture-backed by Canaan Partners and Storm Ventures, and was subsequently acquired into the IgniteTech (ESW Capital / Trilogy) portfolio. The independent beckon.com domain now redirects to its acquirer, IgniteTech, and the company no longer operates a public developer program, API documentation, or developer portal of its own.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/beckon.png
layout: provider
modified: '2026-07-18'
name: Beckon
nav: Providers
network: true
overview: Beckon is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Marketing, Marketing Analytics, Analytics, and Business Intelligence.
random_paper: 17
score:
  band: minimal
  composite: 5.0
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
  previous_composite: 5.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/beckon/refs/heads/main/screenshots/beckon-2026-07-25T202612.png
security:
- kind: domain-security
  name: Beckon Domain Security
  slug: beckon-domain-security
  summary_line: TLSv1.2 · DMARC
slug: beckon
tags:
- Company
- Marketing
- Marketing Analytics
- Analytics
- Business Intelligence
- Data
- Software-as-a-Service
- Acquired
website: https://www.beckon.com
---
