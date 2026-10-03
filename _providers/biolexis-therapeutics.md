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
  href: https://raw.githubusercontent.com/api-evangelist/biolexis-therapeutics/refs/heads/main/hosts/biolexis-therapeutics-hosts.yml
  title: ''
  type: Hosts
  url: hosts/biolexis-therapeutics-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/biolexis-therapeutics/refs/heads/main/vendors/biolexis-therapeutics-vendors.yml
  title: ''
  type: Vendors
  url: vendors/biolexis-therapeutics-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/biolexis-therapeutics/refs/heads/main/security/biolexis-therapeutics-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/biolexis-therapeutics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://biolexistx.com/
coverage:
  checked: '2026-09-28'
  detail: No OpenAPI, AsyncAPI, GraphQL or other machine‑readable contract was found on the API host or website.
  evidence:
  - status: 0
    url: https://api.biolexistx.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-28'
description: Biolexis Therapeutics is a clinical-stage biotechnology company based in Lehi, Utah, developing oral small‑molecule GLP‑1 receptor agonists and AMPK activators for metabolic diseases such as obesity and type‑2 diabetes. The company aims to deliver injectable‑level efficacy with oral dosing, advancing candidates BLX‑7006 and BLX‑0871 through Phase 1 trials.
layout: provider
modified: '2026-09-28'
name: Biolexis Therapeutics
nav: Providers
network: true
overview: Biolexis Therapeutics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Metabolism, Therapeutics, and Utah.
random_paper: 5
score:
  band: minimal
  composite: 3.0
  coverage:
    artifact_dirs: 5
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
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
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Biolexis Therapeutics Domain Security
  slug: biolexis-therapeutics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: biolexis-therapeutics
tags:
- Company
- Biotechnology
- Metabolism
- Therapeutics
- Utah
website: https://biolexistx.com/
---
