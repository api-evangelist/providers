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
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Quaisr provides a SimOps platform; public API documentation is not publicly available.
  name: Quaisr API
  slug: quaisr-api
artifact_total: 5
common:
- group: agent
  href: https://artifacts.apis.io/quaisr/llms/quaisr-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/quaisr-llms.txt
- group: other
  href: https://artifacts.apis.io/quaisr/hosts/quaisr-hosts.yml
  title: ''
  type: Hosts
  url: hosts/quaisr-hosts.yml
- group: other
  href: https://artifacts.apis.io/quaisr/vendors/quaisr-vendors.yml
  title: ''
  type: Vendors
  url: vendors/quaisr-vendors.yml
- group: build
  href: https://artifacts.apis.io/quaisr/packages/quaisr-packages.yml
  title: ''
  type: SDKs
  url: packages/quaisr-packages.yml
- group: build
  href: https://artifacts.apis.io/quaisr/packages/quaisr-packages.yml
  title: ''
  type: Packages
  url: packages/quaisr-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://quaisr.com/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://quaisr.com/legal/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://quaisr.com/press
- group: other
  title: ''
  type: Leadership
  url: https://quaisr.com/team
- group: auth
  href: https://artifacts.apis.io/quaisr/security/quaisr-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/quaisr-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.quaisr.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://www.quaisr.com/
coverage:
  checked: '2026-10-29'
  detail: The Quaisr website offers a "Book a demo" sales form and provides no public API documentation or contract.
  evidence:
  - status: 404
    url: https://quaisr.com/docs
  reason: sales-gate
  state: gated
created: '2026-10-29'
description: Quaisr is a SimOps platform that helps engineering teams digitalise faster by integrating modelling and simulation workflows, enabling data‑driven decision making at scale. We are a team of researchers and engineers dedicated to building the connectivity layer for the world’s most complex systems, turning theoretical simulation into actionable, data‑led intelligence.
image: https://cdn.sanity.io/images/719p8ymp/production/d164d703808740a555b2607d68cf3f5d26b79024-422x216.png?rect=6,0,411,216&w=1200&h=630&auto=format
layout: provider
modified: '2026-10-29'
name: Quaisr
nav: Providers
network: true
overview: Quaisr is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include SimOps, Engineering, Simulation, Data-driven, and Connectivity.
random_paper: 13
rate_limits:
- limit_count: 0
  name: Quaisr Rate Limits
  slug: quaisr-rate-limits
scopes:
- name: Quaisr Scopes
  scope_count: 0
  slug: quaisr-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 13.7
  coverage:
    artifact_dirs: 20
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 60.7
    operational_transparency: 5.3
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 23.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Quaisr Authentication
  slug: quaisr-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Quaisr Domain Security
  slug: quaisr-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: quaisr
tags:
- SimOps
- Engineering
- Simulation
- Data-driven
- Connectivity
website: https://www.quaisr.com/
---
