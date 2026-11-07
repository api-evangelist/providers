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
- description: Converge Insurance provides cyber insurance solutions; no public developer API is offered.
  name: Converge Insurance API
  slug: converge-insurance-api
artifact_total: 2
common:
- group: design
  href: https://artifacts.apis.io/converge-insurance/conformance/converge-insurance-conformance.yml
  title: ''
  type: Conformance
  url: conformance/converge-insurance-conformance.yml
- group: other
  href: https://artifacts.apis.io/converge-insurance/hosts/converge-insurance-hosts.yml
  title: ''
  type: Hosts
  url: hosts/converge-insurance-hosts.yml
- group: other
  href: https://artifacts.apis.io/converge-insurance/vendors/converge-insurance-vendors.yml
  title: ''
  type: Vendors
  url: vendors/converge-insurance-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.convergeins.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.convergeins.com/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://www.convergeins.com/blog
- group: auth
  href: https://artifacts.apis.io/converge-insurance/security/converge-insurance-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/converge-insurance-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.convergeins.com/
coverage:
  checked: '2026-10-10'
  detail: Converge Insurance does not provide a public developer API; attempts to fetch OpenAPI specs returned 404.
  evidence:
  - status: 404
    url: https://api.convergeins.com/openapi.json
  reason: no-developer-program
  state: none
created: '2026-10-10'
description: Converge Insurance is a New York‑based cyber insurance MGA that combines advanced AI‑driven underwriting, a proprietary data ecosystem, and deep security expertise to deliver clear, confident cyber protection for businesses across the United States. The company’s platform fuses insurance expertise with technology to lower cyber risk and provide tailored coverage for mid‑size organizations.
image: https://www.convergeins.com/logo.png
layout: provider
modified: '2026-10-10'
name: Converge Insurance
nav: Providers
network: true
overview: 'Converge Insurance is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Cyber Insurance, MGA, Artificial Intelligence, New York, and Technology.


  Converge Insurance''s developer surface includes engineering blog and 7 more developer resources.'
random_paper: 22
score:
  band: minimal
  composite: 9.6
  coverage:
    artifact_dirs: 11
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.8
  facets:
    access_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 57.1
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 12.4
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 12.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/converge-insurance/converge-insurance-2026-11-03T125230.png
security:
- kind: domain-security
  name: Converge Insurance Domain Security
  slug: converge-insurance-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: converge-insurance
tags:
- Cyber Insurance
- MGA
- Artificial Intelligence
- New York
- Technology
website: https://www.convergeins.com/
---
