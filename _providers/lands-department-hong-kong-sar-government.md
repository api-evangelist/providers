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
  href: https://artifacts.apis.io/lands-department-hong-kong-sar-government/hosts/lands-department-hong-kong-sar-government-hosts.yml
  title: ''
  type: Hosts
  url: hosts/lands-department-hong-kong-sar-government-hosts.yml
- group: auth
  href: https://artifacts.apis.io/lands-department-hong-kong-sar-government/security/lands-department-hong-kong-sar-government-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/lands-department-hong-kong-sar-government-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://landsd.gov.hk
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: http://landsd.gov.hk
  reason: no-developer-program
  state: none
created: '2026-10-23'
description: The Lands Department of the Hong Kong Special Administrative Region is the government agency responsible for land administration, including land registration, surveying, mapping, and the management of public land resources. It provides public services such as land lease information, cadastral data, and geographic information system (GIS) resources to support planning, development, and legal processes. The department’s online portal offers access to forms, guidelines, and contact information for stakeholders and the general public.
layout: provider
modified: '2026-10-23'
name: Lands Department, Hong Kong SAR Government
nav: Providers
network: true
overview: Lands Department, Hong Kong SAR Government is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Government, Land, Hong Kong, GIS, and Public Services.
random_paper: 5
score:
  band: minimal
  composite: 3.4
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - greater-china
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 3.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/lands-department-hong-kong-sar-government/lands-department-hong-kong-sar-government-2026-11-03T134639.png
security:
- kind: domain-security
  name: Lands Department Hong Kong Sar Government Domain Security
  slug: lands-department-hong-kong-sar-government-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: lands-department-hong-kong-sar-government
tags:
- Government
- Land
- Hong Kong
- GIS
- Public Services
website: http://landsd.gov.hk
---
