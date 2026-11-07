---
access_model:
  confidence: low
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 5.4
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 4
common:
- group: other
  href: https://artifacts.apis.io/israel-meteorological-service/hosts/israel-meteorological-service-hosts.yml
  title: ''
  type: Hosts
  url: hosts/israel-meteorological-service-hosts.yml
- group: auth
  href: https://artifacts.apis.io/israel-meteorological-service/security/israel-meteorological-service-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/israel-meteorological-service-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ims.gov.il/
coverage:
  checked: '2026-10-28'
  detail: The provider's public website does not expose any machine‑readable API specification.
  evidence:
  - status: 200
    url: https://ims.gov.il/he
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: The Israeli Meteorological Service (IMS) is the national authority responsible for weather forecasting, climate monitoring, and meteorological services for Israel. It provides a variety of meteorological data and alerts to government agencies, transportation sectors, agriculture, and the general public, supporting safety, planning, and research across the country.
image: https://ims.gov.il/sites/default/files/logo_0.jpg
layout: provider
modified: '2026-10-28'
name: IMS
nav: Providers
network: true
overview: IMS is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Meteorology, Weather, Israel, Government, and Public Service.
random_paper: 1
rate_limits:
- limit_count: 0
  name: Israel Meteorological Service Rate Limits
  slug: israel-meteorological-service-rate-limits
scopes:
- name: Israel Meteorological Service Scopes
  scope_count: 0
  slug: israel-meteorological-service-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 5.2
  coverage:
    artifact_dirs: 20
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - israel
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - mena
    - middle-east
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 5.2
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/israel-meteorological-service/israel-meteorological-service-2026-11-03T134117.png
security:
- kind: authentication
  name: Israel Meteorological Service Authentication
  slug: israel-meteorological-service-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Israel Meteorological Service Domain Security
  slug: israel-meteorological-service-domain-security
  summary_line: TLSv1.2 · DNSSEC · DMARC
slug: israel-meteorological-service
tags:
- Meteorology
- Weather
- Israel
- Government
- Public Service
website: https://ims.gov.il/
---
