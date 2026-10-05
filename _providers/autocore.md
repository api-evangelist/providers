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
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 1
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/autocore/refs/heads/main/conformance/autocore-conformance.yml
  title: ''
  type: Conformance
  url: conformance/autocore-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/autocore/refs/heads/main/hosts/autocore-hosts.yml
  title: ''
  type: Hosts
  url: hosts/autocore-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/autocore/refs/heads/main/vendors/autocore-vendors.yml
  title: ''
  type: Vendors
  url: vendors/autocore-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/autocore-ai
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/autocore/refs/heads/main/security/autocore-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/autocore-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://autocore.ai/en
- group: docs
  title: ''
  type: Documentation
  url: https://autocore.ai/en/docs
- group: company
  title: ''
  type: Blog
  url: https://autocore.ai/en/blog
- group: docs
  title: ''
  type: APIReference
  url: https://autocore.ai/en/api
coverage:
  checked: 2026-09-26
  detail: Documentation pages are HTML rendered with JavaScript and no machine‑readable OpenAPI or other contract was found.
  evidence:
  - status: 200
    url: https://autocore.ai/en/docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-26'
description: AutoCore, founded in 2018, is a global leader in high‑performance mobile computing platforms, offering software‑defined vehicle solutions, AI‑driven robotics, and cloud‑based services for automotive and industrial automation. The company provides a suite of products including AutoCore.COMM, AutoCore.OS, central computing units, and tools for intelligent mobility devices.
layout: provider
modified: '2026-09-26'
name: Autocore
nav: Providers
network: true
overview: 'Autocore is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Automotive, Robotics, Software, and Artificial Intelligence.


  Autocore''s developer surface includes documentation, engineering blog, API reference, and 6 more developer resources.'
random_paper: 8
score:
  band: minimal
  composite: 10.3
  coverage:
    artifact_dirs: 8
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 44.6
    operational_transparency: 5.3
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.0
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Autocore Domain Security
  slug: autocore-domain-security
  summary_line: TLSv1.3 · HSTS
slug: autocore
tags:
- Company
- Automotive
- Robotics
- Software
- Artificial Intelligence
website: https://autocore.ai/en
---
