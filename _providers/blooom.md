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
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/blooom/refs/heads/main/security/blooom-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/blooom-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://blooom.com
created: '2026-07-17'
description: 'Blooom was an independent robo-advisor that provided automated, flat-fee management of employer-sponsored retirement accounts — 401(k), 403(b), 457, and TSP plans — analyzing holdings, rebalancing allocations, and flagging hidden fund fees on accounts it advised but did not directly custody. Founded in 2013 and backed by QED Investors, the Kansas-based company operated a consumer web application rather than a public developer API. The consumer service has since wound down: blooom.com no longer resolves to a website and the domain is now served by Morgan Stanley nameservers with a locked-down, mail-disabled defensive DNS posture (null MX, SPF -all, DMARC p=reject). Retained here as a historical wealth-management profile; no live API or developer surface remains to enrich.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/blooom.png
layout: provider
modified: '2026-07-18'
name: Blooom
nav: Providers
network: true
overview: Blooom is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Wealth Management, Retirement, 401k, and Robo-Advisor.
random_paper: 10
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
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
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
  name: Blooom Domain Security
  slug: blooom-domain-security
  summary_line: DMARC
slug: blooom
tags:
- Company
- Wealth Management
- Retirement
- 401k
- Robo-Advisor
- Investing
- Fintech
- Defunct
website: http://blooom.com
---
