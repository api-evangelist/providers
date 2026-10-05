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
api_count: 1
apis:
- description: Brand protection platform offering API integrations
  name: Bolster AI
  slug: bolster-ai
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bolsterinc/refs/heads/main/llms/bolsterinc-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bolsterinc-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bolsterinc/refs/heads/main/hosts/bolsterinc-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bolsterinc-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bolsterinc/refs/heads/main/vendors/bolsterinc-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bolsterinc-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bolsterinc/refs/heads/main/security/bolsterinc-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bolsterinc-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bolster.ai
coverage:
  checked: '2026-10-02'
  detail: The Bolster AI site renders its documentation via JavaScript and provides no machine‑readable OpenAPI or other contract.
  evidence:
  - status: 200
    url: https://bolster.ai
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-02'
description: 'Bolsterinc is a company surfaced via the API Evangelist harvest backlog (source: secondary-market) and added to the network as a stub for full-pipeline profiling.'
layout: provider
modified: '2026-10-02'
name: Bolsterinc
nav: Providers
network: true
overview: Bolsterinc publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company.
random_paper: 21
score:
  band: minimal
  composite: 2.8
  coverage:
    artifact_dirs: 6
    catalog_earned: 20.0
    catalog_earned_first_party: 0.0
    catalog_gap: 95.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 42.9
    operational_transparency: 0.0
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
  name: Bolsterinc Domain Security
  slug: bolsterinc-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: bolsterinc
tags:
- Company
website: https://bolster.ai
---
