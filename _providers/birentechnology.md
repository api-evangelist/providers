---
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
  scored_at: '2026-10-04'
api_count: 1
apis:
- description: Developer portal providing documentation and API reference for Birentechnology services.
  name: Birentechnology API
  slug: birentechnology-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/birentechnology/refs/heads/main/hosts/birentechnology-hosts.yml
  title: ''
  type: Hosts
  url: hosts/birentechnology-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/birentechnology/refs/heads/main/security/birentechnology-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/birentechnology-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.birentech.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.birentech.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.birentech.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.birentech.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.birentech.com/about/
- group: company
  title: ''
  type: Blog
  url: https://www.birentech.com/news/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.birentech.com/privacy-policy/
coverage:
  checked: '2026-09-28'
  detail: Developer portal pages render via JavaScript and provide no machine‑readable spec.
  evidence:
  - status: 200
    url: https://developer.birentech.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-28'
description: Birentechnology, operating as BIREN Technology, is a leading Chinese provider of general-purpose intelligent computing solutions. Founded in 2019, it develops GPU-based accelerators and a software ecosystem, serving AI data centers, telecom, finance and other industries. The company went public on the Hong Kong Stock Exchange in 2026 (06082.HK).
layout: provider
modified: '2026-09-28'
name: Birentechnology
nav: Providers
network: true
overview: 'Birentechnology publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Semiconductors, Artificial Intelligence, GPU, and Cloud.


  Birentechnology''s developer surface includes documentation, API reference, getting-started guide, engineering blog, and 5 more developer resources.'
random_paper: 6
score:
  band: emerging
  composite: 14.6
  coverage:
    artifact_dirs: 0
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 40.5
    discoverability: 53.6
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - china
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Birentechnology Domain Security
  slug: birentechnology-domain-security
  summary_line: TLSv1.3
slug: birentechnology
tags:
- Company
- Semiconductors
- Artificial Intelligence
- GPU
- Cloud
website: https://www.birentech.com
---
