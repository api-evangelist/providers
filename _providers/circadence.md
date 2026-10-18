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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: Circadence provides AI‑powered cyber range and cyber readiness solutions.
  name: Circadence API
  slug: circadence-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/circadence/refs/heads/main/hosts/circadence-hosts.yml
  title: ''
  type: Hosts
  url: hosts/circadence-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/circadence/refs/heads/main/vendors/circadence-vendors.yml
  title: ''
  type: Vendors
  url: vendors/circadence-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/circadence/refs/heads/main/security/circadence-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/circadence-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://circadence.com/
- group: operate
  title: ''
  type: Support
  url: https://circadence.com/support-center/
- group: company
  title: ''
  type: Blog
  url: https://circadence.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/circadence
- group: start
  title: ''
  type: SignUp
  url: https://circadence.com/schedule-a-conversation/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://circadence.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://circadence.com/privacy-policy/
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/circadence/workspace
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 200
    url: https://circadence.com/
  - status: 403
    url: https://forgeglobal.com/circadence_stock/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-08'
description: Circadence provides AI‑powered cyber range and cyber readiness solutions. Their platform combines generative AI, high‑fidelity simulation, and immersive workforce development to train, test, and prepare cyber operations at enterprise and national scale. Products include RangeGPT, Range Conductor, Project Ares, and Security Immersion Workshops, serving private, public, and government sectors.
layout: provider
modified: '2026-10-08'
name: Circadence
nav: Providers
network: true
overview: 'Circadence is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Cybersecurity, Cyber Range, and Training.


  Circadence''s developer surface includes support, engineering blog, signup flow, and 8 more developer resources.'
random_paper: 13
score:
  band: emerging
  composite: 14.9
  coverage:
    artifact_dirs: 6
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 53.6
    operational_transparency: 5.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Circadence Domain Security
  slug: circadence-domain-security
  summary_line: TLSv1.3 · DMARC
slug: circadence
tags:
- Company
- Artificial Intelligence
- Cybersecurity
- Cyber Range
- Training
website: https://circadence.com/
---
