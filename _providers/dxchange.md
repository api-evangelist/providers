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
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.1
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: 'DXchange.io API as documented publicly: 6 operations. Contract generated from the documentation by API Evangelist (2026-10-20); not the provider''s own document.'
  name: DXchange.io API
  slug: dxchange-api
artifact_total: 4
common:
- group: design
  href: https://artifacts.apis.io/dxchange/rules/dxchange-rules.yml
  title: ''
  type: Spectral
  url: rules/dxchange-rules.yml
- group: design
  href: https://artifacts.apis.io/dxchange/vocabulary/dxchange-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/dxchange-vocabulary.yml
- group: auth
  href: https://artifacts.apis.io/dxchange/authentication/dxchange-authentication.yml
  title: ''
  type: Authentication
  url: authentication/dxchange-authentication.yml
- group: design
  href: https://artifacts.apis.io/dxchange/conformance/dxchange-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dxchange-conformance.yml
- group: other
  href: https://artifacts.apis.io/dxchange/hosts/dxchange-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dxchange-hosts.yml
- group: other
  href: https://artifacts.apis.io/dxchange/vendors/dxchange-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dxchange-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.axway.com/en/terms-of-use
- group: operate
  title: ''
  type: Support
  url: https://support.axway.com/
- group: company
  title: ''
  type: Newsroom
  url: https://www.axway.com/en/newsroom
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Axway
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.axway.com/bundle/TransferCFT_36_UsersGuide_allOS_en_HTML5/page/Content/architecture/getting_started/add_relay.htm
- group: docs
  title: ''
  type: Documentation
  url: https://docs.axway.com/
- group: auth
  href: https://artifacts.apis.io/dxchange/security/dxchange-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dxchange-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.axway.com/en
created: '2026-10-20'
description: DXchange.io is a digital data integration platform that enables enterprises to unlock their data for new digital experiences, offerings, and markets. It provides API management, managed file transfer, and B2B integration solutions as part of the Axway portfolio, helping organizations connect applications, partners, and services securely and efficiently.
layout: provider
modified: '2026-10-20'
name: DXchange.io
nav: Providers
network: true
overview: 'DXchange.io is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Integration, API Management, Managed File Transfer, B2B Integration, and Enterprise Data.


  The DXchange.io catalog on APIs.io includes 1 Spectral governance ruleset.


  DXchange.io''s developer surface includes authentication, support, getting-started guide, documentation, and 10 more developer resources.'
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: DXchange.io API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: dxchange-rules
score:
  band: emerging
  composite: 22.0
  coverage:
    artifact_dirs: 12
    catalog_earned: 35.8
    catalog_earned_first_party: 0.0
    catalog_gap: 79.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 10.5
    developer_ergonomics: 38.1
    discoverability: 55.4
    operational_transparency: 5.3
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 3
      marker_coverage: 100.0
      total: 3
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Dxchange Authentication
  slug: dxchange-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Dxchange Domain Security
  slug: dxchange-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dxchange
tags:
- Integration
- API Management
- Managed File Transfer
- B2B Integration
- Enterprise Data
website: https://www.axway.com/en
---
