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
  scored_at: '2026-10-17'
api_count: 2
apis:
- description: FORT Manager API provides programmatic access to Fort Robotics' trust layer for physical AI, enabling safety controls and fleet analytics.
  name: FORT Manager API
  slug: fort-manager-api
- baseURL: https://platform.fortrobotics.com
  baseurl_source: declared
  description: 'Fort Robotics API as documented publicly: 0 operations. Contract generated from the documentation by API Evangelist (2026-10-12); not the provider''s own document.'
  name: Fort Robotics API
  slug: fort-robotics-api
artifact_total: 4
common:
- group: docs
  title: ''
  type: Documentation
  url: https://developer.fortrobotics.com/
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/fort-robotics/refs/heads/main/changelog/fort-robotics-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/fort-robotics-changelog.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/fort-robotics/refs/heads/main/authentication/fort-robotics-authentication.yml
  title: ''
  type: Authentication
  url: authentication/fort-robotics-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/fort-robotics/refs/heads/main/conformance/fort-robotics-conformance.yml
  title: ''
  type: Conformance
  url: conformance/fort-robotics-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/fort-robotics/refs/heads/main/hosts/fort-robotics-hosts.yml
  title: ''
  type: Hosts
  url: hosts/fort-robotics-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/fort-robotics/refs/heads/main/vendors/fort-robotics-vendors.yml
  title: ''
  type: Vendors
  url: vendors/fort-robotics-vendors.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.fortrobotics.com/getting_started
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/fort-robotics/refs/heads/main/security/fort-robotics-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/fort-robotics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.fortrobotics.com
- group: company
  title: ''
  type: Blog
  url: https://www.fortrobotics.com/news
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.fortrobotics.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.fortrobotics.com/privacy-policy
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://www.fortrobotics.com/mcp
  - status: 403
    url: https://fortrobotics.com/mcp
  - status: 200
    url: https://www.fortrobotics.com
  reason: no-developer-program
  state: none
created: '2026-10-12'
description: Fort Robotics provides a trust layer for physical AI, delivering safety and remote control solutions for robotics and autonomous systems. Their modular platform includes hardware like Safe Remote Control Pro, software such as FORT Manager, and services ranging from safety architecture to fleet analytics. Backed by Lemnos Labs, the company focuses on integrating safety into AI-driven physical devices, enabling secure deployment and operation across industries.
image: https://www.fortrobotics.com/hubfs/FORT%20Robotics%20Trust%20Layer%20for%20Physical%20AI.webp
layout: provider
modified: '2026-10-12'
name: Fort Robotics
nav: Providers
network: true
overview: 'Fort Robotics is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Robotics, Artificial Intelligence, Safety, and Platform.


  Fort Robotics'' developer surface includes documentation, changelog, authentication, getting-started guide, engineering blog, and 7 more developer resources.'
random_paper: 15
score:
  band: emerging
  composite: 23.0
  coverage:
    artifact_dirs: 9
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 8.7
    developer_ergonomics: 35.7
    discoverability: 57.1
    operational_transparency: 15.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Fort Robotics Authentication
  slug: fort-robotics-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Fort Robotics Domain Security
  slug: fort-robotics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: fort-robotics
tags:
- Company
- Robotics
- Artificial Intelligence
- Safety
- Platform
website: https://www.fortrobotics.com
---
