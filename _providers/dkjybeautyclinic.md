---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
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
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/dkjybeautyclinic/hosts/dkjybeautyclinic-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dkjybeautyclinic-hosts.yml
- group: auth
  href: https://artifacts.apis.io/dkjybeautyclinic/security/dkjybeautyclinic-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dkjybeautyclinic-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dcbeautyclinic.com
- group: docs
  title: ''
  type: Documentation
  url: https://dcbeautyclinic.com/about-us/
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 200
    url: https://dcbeautyclinic.com
  - status: 403
    url: https://equityzen.com/company/dkjybeautyclinic
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-23'
description: DC Beauty Clinic is an aesthetic and beauty clinic based in Jakarta, offering a wide range of non‑invasive and minimally invasive cosmetic treatments. Services include injectables such as Botox and fillers, skin boosters, laser therapies, thread lifts, body contouring, and personalized skincare. The clinic emphasizes advanced medical expertise, personalized care, and natural results, aiming to help clients achieve their beauty goals safely and effectively.
layout: provider
modified: '2026-10-23'
name: Dkjybeautyclinic
nav: Providers
network: true
overview: 'Dkjybeautyclinic is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Aesthetic, Beauty, Jakarta, and Clinics.


  Dkjybeautyclinic''s developer surface includes documentation and 3 more developer resources.'
random_paper: 6
score:
  band: minimal
  composite: 4.0
  coverage:
    artifact_dirs: 8
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 44.6
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - indonesia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - southeast-asia
  previous_composite: 5.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/dkjybeautyclinic/dkjybeautyclinic-2026-11-03T130824.png
security:
- kind: domain-security
  name: Dkjybeautyclinic Domain Security
  slug: dkjybeautyclinic-domain-security
  summary_line: TLSv1.3 · DMARC
slug: dkjybeautyclinic
tags:
- Company
- Aesthetic
- Beauty
- Jakarta
- Clinics
website: https://dcbeautyclinic.com
---
