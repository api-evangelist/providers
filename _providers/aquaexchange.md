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
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aquaexchange/refs/heads/main/hosts/aquaexchange-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aquaexchange-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aquaexchange/refs/heads/main/vendors/aquaexchange-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aquaexchange-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aquaexchange.com/TermsAndConditions.html
- group: start
  title: ''
  type: Login
  url: https://app.aquaexchange.com/admin/login/?next=/admin/
- group: company
  title: ''
  type: Blog
  url: https://blog.aquaexchange.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aquaexchange/refs/heads/main/security/aquaexchange-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aquaexchange-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aquaexchange.com
coverage:
  checked: 2026-09-25
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract found after probing known API hosts.
  evidence:
  - status: 0
    url: https://api.aquaexchange.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-25'
description: Aquaexchange is an IT solution company focused on transforming aquaculture through innovative IoT technology and data‑driven insights. Their platform offers farmers comprehensive, affordable tools to enhance productivity, sustainability, and resource efficiency in fish and shrimp farming. Founded in 2020, Aquaexchange provides services ranging from farm monitoring to data analytics, aiming to promote smarter, sustainable farm management worldwide.
layout: provider
modified: '2026-09-25'
name: Aquaexchange
nav: Providers
network: true
overview: 'Aquaexchange is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Aquaculture, IoT, Sustainable Farming, and AgTech.


  Aquaexchange''s developer surface includes engineering blog and 6 more developer resources.'
random_paper: 5
score:
  band: minimal
  composite: 8.8
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aquaexchange Domain Security
  slug: aquaexchange-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aquaexchange
tags:
- Company
- Aquaculture
- IoT
- Sustainable Farming
- AgTech
website: https://aquaexchange.com
---
