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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.6
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: 'Qard API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-10-21); not the provider''s own document.'
  name: Qard API
  slug: qardapi-api
artifact_total: 4
common:
- group: design
  href: https://artifacts.apis.io/qardapi/rules/qardapi-rules.yml
  title: ''
  type: Spectral
  url: rules/qardapi-rules.yml
- group: design
  href: https://artifacts.apis.io/qardapi/vocabulary/qardapi-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/qardapi-vocabulary.yml
- group: auth
  href: https://artifacts.apis.io/qardapi/authentication/qardapi-authentication.yml
  title: ''
  type: Authentication
  url: authentication/qardapi-authentication.yml
- group: design
  href: https://artifacts.apis.io/qardapi/conformance/qardapi-conformance.yml
  title: ''
  type: Conformance
  url: conformance/qardapi-conformance.yml
- group: other
  href: https://artifacts.apis.io/qardapi/hosts/qardapi-hosts.yml
  title: ''
  type: Hosts
  url: hosts/qardapi-hosts.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.qardfinance.com/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://developers.qardapi.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/qardapi
- group: auth
  href: https://artifacts.apis.io/qardapi/security/qardapi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/qardapi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://qardapi.com/
created: '2026-10-21'
description: Qard provides consolidated financial and legal data on French companies to support credit decision-making. It aggregates official registers, tax filings, Banque de France data, and banking flows into a single API, offering comprehensive coverage of corporate financial information for risk assessment and lending processes.
layout: provider
modified: '2026-10-21'
name: Qard
nav: Providers
network: true
overview: 'Qard is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  The Qard catalog on APIs.io includes 1 Spectral governance ruleset.


  Qard''s developer surface includes authentication, getting-started guide, documentation, and 7 more developer resources.'
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Qard API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: qardapi-rules
score:
  band: emerging
  composite: 17.3
  coverage:
    artifact_dirs: 11
    catalog_earned: 30.8
    catalog_earned_first_party: 0.0
    catalog_gap: 84.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 10.5
    developer_ergonomics: 33.3
    discoverability: 44.6
    operational_transparency: 5.3
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Qardapi Authentication
  slug: qardapi-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Qardapi Domain Security
  slug: qardapi-domain-security
  summary_line: DMARC
slug: qardapi
tags:
- Company
website: https://qardapi.com/
---
