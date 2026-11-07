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
- description: Plusgrade provides ancillary revenue solutions for the travel industry via its API.
  name: Plusgrade API
  slug: plusgrade-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/plusgrade/hosts/plusgrade-hosts.yml
  title: ''
  type: Hosts
  url: hosts/plusgrade-hosts.yml
- group: other
  href: https://artifacts.apis.io/plusgrade/vendors/plusgrade-vendors.yml
  title: ''
  type: Vendors
  url: vendors/plusgrade-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/plusgrade
- group: auth
  href: https://artifacts.apis.io/plusgrade/security/plusgrade-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/plusgrade-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.plusgrade.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.plusgrade.com/en/
- group: docs
  title: ''
  type: APIReference
  url: https://www.plusgrade.com/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.plusgrade.com/en/contact/request-a-demo/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.plusgrade.com/policy/privacy/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 401
    url: https://api.plusgrade.com/mcp
  - status: 403
    url: https://plusgrade.com/mcp
  - status: 200
    url: https://plusgrade.com/
  reason: no-developer-program
  state: none
created: '2026-10-12'
description: Plusgrade provides ancillary revenue solutions for the travel industry, helping airlines, hotels, cruise lines, and rail operators increase revenue through flexible upgrade and add‑on offers. Founded in 2009 and headquartered in Montreal, the company operates globally with offices in Toronto, New York, London, Dubai, Tel Aviv, and Singapore. Plusgrade’s platform enables travelers to customize their experience while delivering measurable incremental revenue for partners, serving over 250 companies worldwide.
layout: provider
modified: '2026-10-12'
name: Plusgrade
nav: Providers
network: true
overview: 'Plusgrade is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Travel, Ancillary Revenue, Software-as-a-Service, and B2B.


  Plusgrade''s developer surface includes documentation, API reference, getting-started guide, and 6 more developer resources.'
random_paper: 7
score:
  band: minimal
  composite: 8.5
  coverage:
    artifact_dirs: 7
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.6
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 53.6
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - canada
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 13.1
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
security:
- kind: domain-security
  name: Plusgrade Domain Security
  slug: plusgrade-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: plusgrade
tags:
- Company
- Travel
- Ancillary Revenue
- Software-as-a-Service
- B2B
website: https://www.plusgrade.com/
---
