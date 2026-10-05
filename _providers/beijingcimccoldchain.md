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
- description: API surface referenced by the provider's domain but no machine‑readable contract was found.
  name: Beijing CIMC Cold Chain
  slug: beijing-cimc-cold-chain
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/beijingcimccoldchain/refs/heads/main/hosts/beijingcimccoldchain-hosts.yml
  title: ''
  type: Hosts
  url: hosts/beijingcimccoldchain-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/beijingcimccoldchain/refs/heads/main/security/beijingcimccoldchain-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/beijingcimccoldchain-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cimcthermal.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://equityzen.com/company/beijingcimccoldchain
  reason: no-developer-program
  state: none
created: '2026-09-27'
description: Beijing CIMC Cold Chain Technology Co., Ltd. (BeijingCIMCColdChain) is a leading global innovator and provider of passive temperature control packaging solutions for the pharmaceutical, life‑science and cold‑chain logistics industries. Founded in 2012, the company designs, manufactures and services insulated boxes, phase‑change material packs, gel packs and related cold‑chain products, serving over 600 million vaccine vials and numerous healthcare customers worldwide.
image: https://cimcthermal.com/u_file/2601/photo/f271067a85.png
layout: provider
modified: '2026-09-27'
name: Beijingcimccoldchain
nav: Providers
network: true
overview: Beijingcimccoldchain publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cold Chain, Pharmaceuticals, Logistics, and Manufacturing.
random_paper: 5
score:
  band: minimal
  composite: 4.3
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    mcp: unknown
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
  name: Beijingcimccoldchain Domain Security
  slug: beijingcimccoldchain-domain-security
  summary_line: TLSv1.3
slug: beijingcimccoldchain
tags:
- Company
- Cold Chain
- Pharmaceuticals
- Logistics
- Manufacturing
website: https://cimcthermal.com
---
