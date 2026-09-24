---
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
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.5
  scored_at: '2026-09-24'
api_count: 1
apis:
- baseURL: https://api.airfranceklm.com
  baseurl_source: declared
  description: 'Air France-KLM API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-09-22); not the provider''s own document.'
  name: Air France-KLM API
  slug: air-france-klm-api
artifact_total: 3
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/air-france-klm/refs/heads/main/rules/air-france-klm-rules.yml
  title: ''
  type: Spectral
  url: rules/air-france-klm-rules.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/air-france-klm/refs/heads/main/changelog/air-france-klm-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/air-france-klm-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/air-france-klm/refs/heads/main/conformance/air-france-klm-conformance.yml
  title: ''
  type: Conformance
  url: conformance/air-france-klm-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/air-france-klm/refs/heads/main/vendors/air-france-klm-vendors.yml
  title: ''
  type: Vendors
  url: vendors/air-france-klm-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/air-france-klm/refs/heads/main/security/air-france-klm-domain-security.yml
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
overview: 'Air France-KLM publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Aviation, Travel, Europe, and Sustainability.


  The Air France-KLM catalog on APIs.io includes 1 Spectral governance ruleset.


  Air France-KLM''s developer surface includes changelog, documentation, and 5 more developer resources.'
random_paper: 11
rules:
- effective_rule_count: 52
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
  composite: 15.6
  coverage:
    artifact_dirs: 8
    catalog_earned: 39.5
    catalog_earned_first_party: 0.0
    catalog_gap: 75.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -12.4
  facets:
    access_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 11.9
    developer_ergonomics: 9.5
    discoverability: 64.8
    operational_transparency: 15.8
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - france-iberia
  previous_composite: 28.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
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
