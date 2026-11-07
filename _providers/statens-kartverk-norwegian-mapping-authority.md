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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: Security
  url: https://vdp.kartverket.no/responsible-disclosure-policy.txt
- group: auth
  href: https://artifacts.apis.io/statens-kartverk-norwegian-mapping-authority/well-known/statens-kartverk-norwegian-mapping-authority-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/statens-kartverk-norwegian-mapping-authority-security.txt
- group: auth
  href: https://artifacts.apis.io/statens-kartverk-norwegian-mapping-authority/well-known/statens-kartverk-norwegian-mapping-authority-kartverket-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/statens-kartverk-norwegian-mapping-authority-kartverket-security.txt
- group: agent
  href: https://artifacts.apis.io/statens-kartverk-norwegian-mapping-authority/well-known/statens-kartverk-norwegian-mapping-authority-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/statens-kartverk-norwegian-mapping-authority-well-known.yml
- group: other
  href: https://artifacts.apis.io/statens-kartverk-norwegian-mapping-authority/hosts/statens-kartverk-norwegian-mapping-authority-hosts.yml
  title: ''
  type: Hosts
  url: hosts/statens-kartverk-norwegian-mapping-authority-hosts.yml
- group: build
  href: https://artifacts.apis.io/statens-kartverk-norwegian-mapping-authority/packages/statens-kartverk-norwegian-mapping-authority-packages.yml
  title: ''
  type: SDKs
  url: packages/statens-kartverk-norwegian-mapping-authority-packages.yml
- group: build
  href: https://artifacts.apis.io/statens-kartverk-norwegian-mapping-authority/packages/statens-kartverk-norwegian-mapping-authority-packages.yml
  title: ''
  type: Packages
  url: packages/statens-kartverk-norwegian-mapping-authority-packages.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kartverket
- group: auth
  href: https://artifacts.apis.io/statens-kartverk-norwegian-mapping-authority/security/statens-kartverk-norwegian-mapping-authority-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/statens-kartverk-norwegian-mapping-authority-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/statens-kartverk-norwegian-mapping-authority/security/statens-kartverk-norwegian-mapping-authority-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/statens-kartverk-norwegian-mapping-authority-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.kartverket.no/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://eiendomsregisteret.kartverket.no/api/mcp
  - status: 401
    url: https://mineiendom.kartverket.no/api/mcp
  - status: 200
    url: https://www.kartverket.no/
  reason: no-developer-program
  state: none
created: '2026-10-26'
description: Statens kartverk, also known as the Norwegian Mapping Authority, is Norway's national agency responsible for mapping, land registration, and geographic information. Established in 1773, it provides a wide range of geospatial data, services, and tools for public and private use, supporting navigation, land management, and environmental planning across the country.
layout: provider
modified: '2026-10-26'
name: Statens kartverk - Norwegian Mapping Authority
nav: Providers
network: true
overview: Statens kartverk - Norwegian Mapping Authority is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.
random_paper: 7
score:
  band: minimal
  composite: 5.5
  coverage:
    artifact_dirs: 9
    catalog_earned: 20.0
    catalog_earned_first_party: 0.0
    catalog_gap: 95.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 35.7
    operational_transparency: 7.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - nordics
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 6.5
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/statens-kartverk-norwegian-mapping-authority/statens-kartverk-norwegian-mapping-authority-2026-11-03T143755.png
security:
- kind: domain-security
  name: Statens Kartverk Norwegian Mapping Authority Domain Security
  slug: statens-kartverk-norwegian-mapping-authority-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Statens Kartverk Norwegian Mapping Authority Vulnerability Disclosure
  slug: statens-kartverk-norwegian-mapping-authority-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: statens-kartverk-norwegian-mapping-authority
tags:
- Company
website: https://www.kartverket.no/
---
