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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.1
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/aimport-ar/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/aimport-ar/security/aimport-ar-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/aimport-ar-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/aimport-ar/llms/aimport-ar-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aimport-ar-llms.txt
- group: auth
  href: https://artifacts.apis.io/aimport-ar/well-known/aimport-ar-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/aimport-ar-security.txt
- group: agent
  href: https://artifacts.apis.io/aimport-ar/well-known/aimport-ar-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aimport-ar-well-known.yml
- group: other
  href: https://artifacts.apis.io/aimport-ar/hosts/aimport-ar-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aimport-ar-hosts.yml
- group: other
  href: https://artifacts.apis.io/aimport-ar/vendors/aimport-ar-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aimport-ar-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aimport.ar/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aimport.ar/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://aimport.ar/en/press
- group: auth
  href: https://artifacts.apis.io/aimport-ar/security/aimport-ar-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/aimport-ar-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/aimport-ar/security/aimport-ar-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aimport-ar-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aimport.ar/
- group: commercial
  title: ''
  type: Pricing
  url: https://aimport.ar/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://aimport.ar/mcp
  - status: 200
    url: https://aimport.ar/
  reason: partner-login
  state: gated
created: '2026-11-01'
description: AImport provides Argentine import intelligence, offering data on imports, tariffs, and product origins. The platform aggregates customs data, presenting dashboards, radar views, and AI‑driven insights for businesses and developers. Users can explore import statistics, connect their systems via ImportConnect, and query the data through AI assistants like ImportBrain. The service is in beta, delivering free access to import data and upcoming paid plans.
image: https://aimport.ar/brand/logo-og-2.png
layout: provider
modified: '2026-11-01'
name: AImport
nav: Providers
network: true
overview: 'AImport is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Data, Import, Argentina, Artificial Intelligence, and Analytics.


  AImport''s developer surface includes pricing and 13 more developer resources.'
random_paper: 12
score:
  band: emerging
  composite: 11.5
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.7
  facets:
    access_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 6.4
    discoverability: 49.1
    operational_transparency: 10.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - argentina
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - latin-america
  previous_composite: 15.2
  provenance:
    mcp: unknown
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aimport Ar Domain Security
  slug: aimport-ar-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Aimport Ar Vulnerability Disclosure
  slug: aimport-ar-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: aimport-ar
tags:
- Data
- Import
- Argentina
- Artificial Intelligence
- Analytics
website: https://aimport.ar/
---
