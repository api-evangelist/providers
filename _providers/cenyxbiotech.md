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
api_count: 0
artifact_total: 2
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cenyxbiotech/refs/heads/main/security/cenyxbiotech-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/cenyxbiotech-vulnerability-disclosure.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cenyxbiotech/refs/heads/main/hosts/cenyxbiotech-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cenyxbiotech-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cenyxbiotech/refs/heads/main/security/cenyxbiotech-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/cenyxbiotech-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cenyxbiotech/refs/heads/main/security/cenyxbiotech-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cenyxbiotech-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cenyxbiotech.com
coverage:
  checked: '2026-10-07'
  detail: The company's website returns a JavaScript shell with no machine‑readable documentation.
  evidence:
  - status: 200
    url: https://cenyxbiotech.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-07'
description: 'Cenyxbiotech is a company surfaced via the API Evangelist harvest backlog (source: secondary-market) and added to the network as a stub for full-pipeline profiling.'
layout: provider
modified: '2026-10-07'
name: Cenyxbiotech
nav: Providers
network: true
overview: Cenyxbiotech is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.
random_paper: 9
score:
  band: minimal
  composite: 3.6
  coverage:
    artifact_dirs: 4
    catalog_earned: 15.0
    catalog_earned_first_party: 0.0
    catalog_gap: 100.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 26.8
    operational_transparency: 10.5
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cenyxbiotech Domain Security
  slug: cenyxbiotech-domain-security
  summary_line: TLSv1.2
- kind: vulnerability-disclosure
  name: Cenyxbiotech Vulnerability Disclosure
  slug: cenyxbiotech-vulnerability-disclosure
  summary_line: no policy recorded
slug: cenyxbiotech
tags:
- Company
website: https://cenyxbiotech.com
---
