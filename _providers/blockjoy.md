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
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/blockjoy/refs/heads/main/hosts/blockjoy-hosts.yml
  title: ''
  type: Hosts
  url: hosts/blockjoy-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/blockjoy/refs/heads/main/vendors/blockjoy-vendors.yml
  title: ''
  type: Vendors
  url: vendors/blockjoy-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://support.github.com
- group: start
  title: ''
  type: SignUp
  url: https://github.com/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F%3Corg-login%3E&source=header
- group: auth
  title: ''
  type: Security
  url: https://github.com/security/advanced-security/code-security
- group: commercial
  title: ''
  type: Pricing
  url: https://github.com/pricing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/why-github
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/blockjoy/refs/heads/main/security/blockjoy-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/blockjoy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://blockjoy.com
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/blockjoy/platform
- group: start
  title: ''
  type: DeveloperPortal
  url: https://github.com/blockjoy
coverage:
  checked: '2026-09-29'
  detail: Blockjoy's website serves a JavaScript shell and no machine‑readable API documentation is available.
  evidence:
  - status: 200
    url: https://blockjoy.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-29'
description: Blockjoy provides Web3 infrastructure services, enabling developers to deploy and manage blockchain nodes through its Blockvisor stack. The company offers a suite of tools for protocol configuration, resource isolation, and scalable deployment across private data centers and bare metal servers. Blockjoy aims to simplify blockchain operations for enterprises and developers alike.
image: https://avatars.githubusercontent.com/u/91785009?s=280&v=4
layout: provider
modified: '2026-09-29'
name: Blockjoy
nav: Providers
network: true
overview: 'Blockjoy is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Web3, Infrastructure, Blockchain, and Open Source.


  Blockjoy''s developer surface includes support, signup flow, pricing, documentation, and 7 more developer resources.'
random_paper: 3
score:
  band: emerging
  composite: 14.0
  coverage:
    artifact_dirs: 7
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 39.3
    operational_transparency: 15.8
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Blockjoy Domain Security
  slug: blockjoy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: blockjoy
tags:
- Web3
- Infrastructure
- Blockchain
- Open Source
website: https://blockjoy.com
---
