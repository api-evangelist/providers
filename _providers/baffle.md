---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 14.4
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/baffle/refs/heads/main/llms/baffle-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/baffle-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/baffle/refs/heads/main/well-known/baffle-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/baffle-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/baffle/refs/heads/main/hosts/baffle-hosts.yml
  title: ''
  type: Hosts
  url: hosts/baffle-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/baffle/refs/heads/main/vendors/baffle-vendors.yml
  title: ''
  type: Vendors
  url: vendors/baffle-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://baffle.io/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://baffle.io/news/
- group: company
  title: ''
  type: Blog
  url: https://baffle.io/blog/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.baffle.io/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/baffle
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/baffle/refs/heads/main/security/baffle-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/baffle-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://baffle.io
coverage:
  checked: 2026-09-27
  detail: Docs at https://docs.baffle.io redirect to a login page requiring credentials.
  evidence:
  - status: 302
    url: https://docs.baffle.io
  reason: partner-login
  state: gated
created: '2026-09-27'
description: Baffle provides data tokenization, de‑identification, and encryption solutions that protect sensitive information across databases, cloud storage, and SaaS applications. Their platform enables organizations to secure data at rest and in motion, ensuring compliance with privacy regulations while simplifying data access for analytics and AI workloads. Baffle’s technology abstracts encryption complexities, offering searchable encryption and dynamic data masking to make data breaches irrelevant.
image: https://baffle.io/wp-content/uploads/2024/04/gartner-peer-insights.svg
layout: provider
modified: '2026-09-27'
name: Baffle
nav: Providers
network: true
overview: 'Baffle is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data Protection, Encryption, Tokenization, and Compliance.


  Baffle''s developer surface includes engineering blog, documentation, and 9 more developer resources.'
random_paper: 14
score:
  band: minimal
  composite: 10.9
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 57.1
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Baffle Domain Security
  slug: baffle-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: baffle
tags:
- Company
- Data Protection
- Encryption
- Tokenization
- Compliance
website: https://baffle.io
---
