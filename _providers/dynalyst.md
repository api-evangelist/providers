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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 0
common:
- group: other
  href: https://artifacts.apis.io/dynalyst/hosts/dynalyst-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dynalyst-hosts.yml
- group: company
  title: ''
  type: Website
  url: https://dynalyst.io/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy-policy.cyberagent.ai/
coverage:
  checked: '2026-10-28'
  detail: The Dynalyst website is unreachable, suggesting the company is defunct or no longer maintains an API.
  evidence:
  - status: 0
    url: https://dynalyst.io/
  reason: defunct
  state: none
created: '2026-10-28'
description: Dynalyst is a performance‑focused mobile advertising platform (DSP) provided by CyberAgent, Inc. It delivers real‑time, machine‑learning‑driven ad targeting for smartphone apps, leveraging a large inventory of domestic ad exchanges. Dynalyst’s dynamic retargeting service is a market leader in Japan, offering advertisers precise audience segmentation, automated creative generation, and comprehensive reporting. The platform emphasizes high‑performance ad delivery, privacy‑compliant data handling, and integration with major measurement partners such as AppsFlyer.
image: https://www.dynalyst.io/image/Logo__x4.png
layout: provider
modified: '2026-10-28'
name: Dynalyst
nav: Providers
network: true
overview: Dynalyst is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Advertising, DSP, Mobile, and Japan.
random_paper: 0
score:
  band: minimal
  composite: 3.9
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.3
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - japan
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - japan-korea
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 5.2
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 2.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
slug: dynalyst
tags:
- Company
- Advertising
- DSP
- Mobile
- Japan
- Performance
website: https://dynalyst.io/
---
