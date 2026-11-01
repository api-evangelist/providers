---
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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.5
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Management API for DolphinCSV, providing endpoints to create, retrieve, update and delete templates and columns.
  name: Management API
  slug: management-api
artifact_total: 2
common:
- group: design
  href: https://artifacts.apis.io/dolphincsv/conformance/dolphincsv-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dolphincsv-conformance.yml
- group: other
  href: https://artifacts.apis.io/dolphincsv/hosts/dolphincsv-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dolphincsv-hosts.yml
- group: other
  href: https://artifacts.apis.io/dolphincsv/vendors/dolphincsv-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dolphincsv-vendors.yml
- group: build
  href: https://artifacts.apis.io/dolphincsv/packages/dolphincsv-packages.yml
  title: ''
  type: SDKs
  url: packages/dolphincsv-packages.yml
- group: build
  href: https://artifacts.apis.io/dolphincsv/packages/dolphincsv-packages.yml
  title: ''
  type: Packages
  url: packages/dolphincsv-packages.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dolphincsv
- group: auth
  href: https://artifacts.apis.io/dolphincsv/security/dolphincsv-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dolphincsv-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dolphincsv.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.dolphincsv.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.dolphincsv.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.dolphincsv.com/management-api/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.dolphincsv.com/get-started/configure-your-template
- group: start
  title: ''
  type: SignUp
  url: https://dolphincsv.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dolphincsv.com/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dolphincsv.com/privacy
- group: company
  title: ''
  type: Blog
  url: https://x.com/DolphinCSV
created: '2026-10-16'
description: First Principles Software offers DolphinCSV, an embeddable CSV import widget designed for small SaaS products. The service enables developers to implement CSV import functionality within minutes, providing automatic column matching, data validation, and cleaning. With SDKs for React and JavaScript, comprehensive documentation, and support options, DolphinCSV aims to simplify data onboarding for SaaS applications, targeting developers and product teams seeking quick integration and reliable CSV handling.
layout: provider
modified: '2026-10-16'
name: First Principles Software
nav: Providers
network: true
overview: 'First Principles Software is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, CSV, Software-as-a-Service, Integration, and Developer Tools.


  First Principles Software''s developer surface includes documentation, API reference, getting-started guide, signup flow, engineering blog, and 11 more developer resources.'
random_paper: 2
score:
  band: emerging
  composite: 24.4
  coverage:
    artifact_dirs: 8
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 47.6
    discoverability: 62.5
    operational_transparency: 5.3
  previous_composite: 24.4
  provenance:
    conformance: derived
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dolphincsv Domain Security
  slug: dolphincsv-domain-security
  summary_line: TLSv1.3
slug: dolphincsv
tags:
- Company
- CSV
- Software-as-a-Service
- Integration
- Developer Tools
website: https://dolphincsv.com/
---
