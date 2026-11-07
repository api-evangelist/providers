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
- group: auth
  href: https://artifacts.apis.io/nextbike/well-known/nextbike-servicehub-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/nextbike-servicehub-security.txt
- group: agent
  href: https://artifacts.apis.io/nextbike/well-known/nextbike-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/nextbike-well-known.yml
- group: other
  href: https://artifacts.apis.io/nextbike/hosts/nextbike-hosts.yml
  title: ''
  type: Hosts
  url: hosts/nextbike-hosts.yml
- group: build
  href: https://artifacts.apis.io/nextbike/packages/nextbike-packages.yml
  title: ''
  type: SDKs
  url: packages/nextbike-packages.yml
- group: build
  href: https://artifacts.apis.io/nextbike/packages/nextbike-packages.yml
  title: ''
  type: Packages
  url: packages/nextbike-packages.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.nextbike.net/it/privacy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/nextbike
- group: auth
  href: https://artifacts.apis.io/nextbike/security/nextbike-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/nextbike-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.nextbike.net
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.nextbike.net
  reason: no-developer-program
  state: none
created: '2026-10-13'
description: Nextbike GmbH is a leading European bike‑sharing provider offering tailored mobility solutions for cities, campuses and businesses since 2004. Operating in over 400 locations across more than 20 countries, it delivers innovative bike‑sharing platforms, advertising options, and sustainability initiatives, supporting public transport integration and corporate mobility programs.
layout: provider
modified: '2026-10-13'
name: nextbike
nav: Providers
network: true
overview: nextbike is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Bike Sharing, Mobility, Transportation, Europe, and Software-as-a-Service.
random_paper: 18
score:
  band: minimal
  composite: 7.6
  coverage:
    artifact_dirs: 9
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.6
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 44.6
    operational_transparency: 13.2
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
  previous_composite: 9.2
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 7.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/nextbike/nextbike-2026-11-03T140159.png
security:
- kind: domain-security
  name: Nextbike Domain Security
  slug: nextbike-domain-security
  summary_line: no transport/DNS hardening detected
slug: nextbike
tags:
- Bike Sharing
- Mobility
- Transportation
- Europe
- Software-as-a-Service
- Company
website: https://www.nextbike.net
---
