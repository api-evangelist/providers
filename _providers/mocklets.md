---
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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Mock API simulator
  name: Mocklets API
  slug: mocklets-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/mocklets/llms/mocklets-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/mocklets-llms.txt
- group: agent
  href: https://artifacts.apis.io/mocklets/well-known/mocklets-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/mocklets-well-known.yml
- group: other
  href: https://artifacts.apis.io/mocklets/hosts/mocklets-hosts.yml
  title: ''
  type: Hosts
  url: hosts/mocklets-hosts.yml
- group: other
  href: https://artifacts.apis.io/mocklets/vendors/mocklets-vendors.yml
  title: ''
  type: Vendors
  url: vendors/mocklets-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mocklets.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mocklets.com/privacy
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.mocklets.com/master
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mocklets
- group: auth
  href: https://artifacts.apis.io/mocklets/security/mocklets-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mocklets-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mocklets.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.mocklets.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://mocklets.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://medium.com/mocklets
created: '2026-10-21'
description: Mocklets provides an HTTP-based mock API simulator that helps developers simulate APIs for faster parallel development and more comprehensive testing. It offers a smart way to mock your APIs, enabling teams to create realistic API responses, test edge cases, and accelerate integration workflows without relying on live services.
image: https://firebasestorage.googleapis.com/v0/b/mocklets.appspot.com/o/mocklets-logo.png?alt=media&token=eee8b454-6c6a-4b72-818d-c5a287d902d9
layout: provider
modified: '2026-10-21'
name: Mocklets
nav: Providers
network: true
overview: 'Mocklets is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Mocking, API Simulation, Development Tools, and Testing.


  Mocklets'' developer surface includes getting-started guide, documentation, pricing, engineering blog, and 9 more developer resources.'
random_paper: 2
score:
  band: emerging
  composite: 17.3
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 57.1
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Mocklets Domain Security
  slug: mocklets-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: mocklets
tags:
- Company
- Mocking
- API Simulation
- Development Tools
- Testing
website: https://mocklets.com/
---
