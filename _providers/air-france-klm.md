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
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.airfranceklm.com
  baseurl_source: declared
  description: The Opendata API from Air France-KLM — 1 operation(s) for opendata.
  name: Air France-KLM Opendata API
  slug: air-france-klm-opendata-api
artifact_total: 3
common:
- group: design
  href: https://artifacts.apis.io/air-france-klm/rules/air-france-klm-rules.yml
  title: ''
  type: Spectral
  url: rules/air-france-klm-rules.yml
- group: operate
  href: https://artifacts.apis.io/air-france-klm/changelog/air-france-klm-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/air-france-klm-changelog.yml
- group: design
  href: https://artifacts.apis.io/air-france-klm/conformance/air-france-klm-conformance.yml
  title: ''
  type: Conformance
  url: conformance/air-france-klm-conformance.yml
- group: other
  href: https://artifacts.apis.io/air-france-klm/vendors/air-france-klm-vendors.yml
  title: ''
  type: Vendors
  url: vendors/air-france-klm-vendors.yml
- group: auth
  href: https://artifacts.apis.io/air-france-klm/security/air-france-klm-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/air-france-klm-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://airfranceklm.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.airfranceklm.com/en
coverage:
  checked: 2026-09-22
  detail: Developer portal pages are a JavaScript single-page app with no static OpenAPI spec.
  evidence:
  - status: 200
    url: https://developer.airfranceklm.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-22'
description: Air France-KLM is a leading European airline group operating worldwide, offering passenger and cargo services through its Air France, KLM, and Transavia brands. The group serves over 320 destinations, emphasizing sustainability, innovation, and customer experience. It provides extensive travel solutions, loyalty programs, and digital services, reflecting its commitment to responsible aviation and global connectivity.
layout: provider
modified: '2026-09-22'
name: Air France-KLM
nav: Providers
network: true
overview: 'Air France-KLM is listed with 1 API on the [APIs.io](https://apis.io/) network: Opendata API. Tagged areas include Company, Aviation, Travel, Europe, and Sustainability.


  The Air France-KLM catalog on APIs.io includes 1 Spectral governance ruleset.


  Air France-KLM''s developer surface includes changelog, documentation, and 5 more developer resources.'
random_paper: 9
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Air France-KLM API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: air-france-klm-rules
score:
  band: emerging
  composite: 13.8
  coverage:
    artifact_dirs: 11
    catalog_earned: 39.5
    catalog_earned_first_party: 0.0
    catalog_gap: 75.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.9
  facets:
    access_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 11.9
    developer_ergonomics: 4.8
    discoverability: 62.5
    operational_transparency: 15.8
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - france-iberia
  previous_composite: 14.7
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/air-france-klm/air-france-klm-2026-10-11T093344.png
security:
- kind: domain-security
  name: Air France Klm Domain Security
  slug: air-france-klm-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: air-france-klm
tags:
- Company
- Aviation
- Travel
- Europe
- Sustainability
website: https://airfranceklm.com/
---
