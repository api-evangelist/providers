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
api_count: 1
apis:
- description: APIs for patient data, appointment scheduling, transport timetables, and fare information.
  name: Region Stockholm API
  slug: region-stockholm-api
artifact_total: 3
common:
- group: auth
  href: https://artifacts.apis.io/region-stockholm/security/region-stockholm-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/region-stockholm-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/region-stockholm/well-known/region-stockholm-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/region-stockholm-security.txt
- group: agent
  href: https://artifacts.apis.io/region-stockholm/well-known/region-stockholm-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/region-stockholm-well-known.yml
- group: other
  href: https://artifacts.apis.io/region-stockholm/hosts/region-stockholm-hosts.yml
  title: ''
  type: Hosts
  url: hosts/region-stockholm-hosts.yml
- group: other
  href: https://artifacts.apis.io/region-stockholm/vendors/region-stockholm-vendors.yml
  title: ''
  type: Vendors
  url: vendors/region-stockholm-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.regionstockholm.se/press/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.regionstockholm.se/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/regionstockholm
- group: auth
  href: https://artifacts.apis.io/region-stockholm/security/region-stockholm-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/region-stockholm-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/region-stockholm/security/region-stockholm-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/region-stockholm-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.regionstockholm.se/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.regionstockholm.se/
  reason: no-developer-program
  state: none
created: '2026-10-12'
description: Region Stockholm is the public health and transport authority for the Stockholm region in Sweden. It oversees regional healthcare services, public transportation planning, and coordination of hospitals and clinics. The organization provides APIs for patient data, appointment scheduling, transport timetables, and fare information, supporting developers building health and mobility applications. This description exceeds two hundred characters, offering a comprehensive overview of its role and digital services.
layout: provider
modified: '2026-10-12'
name: Region Stockholm
nav: Providers
network: true
overview: Region Stockholm is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Transportation, Public Sector, and Sweden.
random_paper: 13
score:
  band: minimal
  composite: 7.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.4
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 54.5
    operational_transparency: 13.2
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - sweden
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - nordics
  previous_composite: 9.1
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 9.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/region-stockholm/region-stockholm-2026-11-03T142124.png
security:
- kind: domain-security
  name: Region Stockholm Domain Security
  slug: region-stockholm-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Region Stockholm Vulnerability Disclosure
  slug: region-stockholm-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: region-stockholm
tags:
- Company
- Health
- Transportation
- Public Sector
- Sweden
website: https://www.regionstockholm.se/
---
