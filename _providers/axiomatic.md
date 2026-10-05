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
  href: https://raw.githubusercontent.com/api-evangelist/axiomatic/refs/heads/main/well-known/axiomatic-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/axiomatic-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/axiomatic/refs/heads/main/hosts/axiomatic-hosts.yml
  title: ''
  type: Hosts
  url: hosts/axiomatic-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/axiomatic/refs/heads/main/vendors/axiomatic-vendors.yml
  title: ''
  type: Vendors
  url: vendors/axiomatic-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.axiomatic.com/terms-of-service/
- group: operate
  title: ''
  type: Support
  url: https://www.axiomatic.com/support/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.axiomatic.com/wp-content/uploads/Privacy-Notice-Axiomatic.pdf
- group: company
  title: ''
  type: Newsroom
  url: https://www.axiomatic.com/news/
- group: company
  title: ''
  type: Blog
  url: https://www.axiomatic.com/blog/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/axiomatic/refs/heads/main/security/axiomatic-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/axiomatic-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.axiomatic.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://forgeglobal.com/axiomatic_stock/
  reason: no-developer-program
  state: none
created: '2026-09-27'
description: Axiomatic Technologies designs and manufactures electronic control and power conversion products, including battery chargers, motor and actuator controllers, DC‑DC converters, AC‑DC supplies, I/O automation, and protocol converters. The company supplies these rugged components to manufacturers of construction, mining, off‑highway and on‑highway machines that operate in harsh environments. It also offers OEM control design services and custom development for clients worldwide.
layout: provider
modified: '2026-09-27'
name: aXiomatic
nav: Providers
network: true
overview: 'aXiomatic is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Automation, Power Management, Control Systems, Off-Highway, and On‑Highway.


  aXiomatic''s developer surface includes support, engineering blog, and 8 more developer resources.'
random_paper: 13
score:
  band: minimal
  composite: 10.7
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
    developer_ergonomics: 7.1
    discoverability: 46.4
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 16.4
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Axiomatic Domain Security
  slug: axiomatic-domain-security
  summary_line: TLSv1.3 · DMARC
slug: axiomatic
tags:
- Automation
- Power Management
- Control Systems
- Off-Highway
- On‑Highway
- Machine Control
website: https://www.axiomatic.com/
---
