---
agent_readiness:
  band: human-only
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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: operate
  href: https://artifacts.apis.io/energistics/changelog/energistics-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/energistics-changelog.yml
- group: auth
  href: https://artifacts.apis.io/energistics/authentication/energistics-authentication.yml
  title: ''
  type: Authentication
  url: authentication/energistics-authentication.yml
- group: other
  href: https://artifacts.apis.io/energistics/hosts/energistics-hosts.yml
  title: ''
  type: Hosts
  url: hosts/energistics-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://energistics.org/terms-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://energistics.org/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://energistics.org/news
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.energistics.org/RESQML/RESQML_TOPICS/RESQML-000-230-0-C-sv2010.html
- group: docs
  title: ''
  type: Documentation
  url: https://docs.energistics.org/
- group: auth
  href: https://artifacts.apis.io/energistics/security/energistics-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/energistics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://www.energistics.org
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: http://www.energistics.org
  reason: no-developer-program
  state: none
created: '2026-10-23'
description: Energistics is a global, non‑profit consortium that develops, manages, and promotes data transfer standards for the energy industry. It provides standards such as WITSML, RESQML, PRODML, ETP, PWLS, and UOM to operators, service companies, technology providers, and regulatory agencies for data interoperability and integration across upstream workflows.
layout: provider
modified: '2026-10-23'
name: Energistics
nav: Providers
network: true
overview: 'Energistics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Data Standards, Energy Industry, Oil & Gas, Non‑profit Consortium, and Data Interoperability.


  Energistics'' developer surface includes changelog, authentication, getting-started guide, documentation, and 6 more developer resources.'
random_paper: 8
score:
  band: emerging
  composite: 18.1
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 33.3
    discoverability: 46.4
    operational_transparency: 15.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 16.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Energistics Authentication
  slug: energistics-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Energistics Domain Security
  slug: energistics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: energistics
tags:
- Data Standards
- Energy Industry
- Oil & Gas
- Non‑profit Consortium
- Data Interoperability
- Technical Standards
website: http://www.energistics.org
---
