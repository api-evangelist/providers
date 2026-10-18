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
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/amalgamrx/refs/heads/main/hosts/amalgamrx-hosts.yml
  title: ''
  type: Hosts
  url: hosts/amalgamrx-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/amalgamrx/refs/heads/main/vendors/amalgamrx-vendors.yml
  title: ''
  type: Vendors
  url: vendors/amalgamrx-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://amalgamrx.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://amalgamrx.com/news/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/amalgamrx/refs/heads/main/security/amalgamrx-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/amalgamrx-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://amalgamrx.com
coverage:
  checked: '2026-10-05'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found at the API host or documentation pages.
  evidence:
  - status: failed
    url: https://api.amalgamrx.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-24'
description: Amalgam Rx is a health‑technology company delivering AI‑powered software‑as‑a‑medical‑device (SaMD) solutions for providers, health plans, and life‑science partners. Their modular platform supports digital products, clinical AI, enterprise platforms, patient‑derived usage‑recording systems (PDURS) and EHR integrations, serving millions of patients across four continents with regulatory clearances.
layout: provider
modified: '2026-09-24'
name: Amalgamrx
nav: Providers
network: true
overview: Amalgamrx is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health Tech, Artificial Intelligence, SaMD, and Healthcare.
random_paper: 8
score:
  band: minimal
  composite: 6.0
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 5.7
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.4
    operational_transparency: 0.0
  previous_composite: 0.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.4
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Amalgamrx Domain Security
  slug: amalgamrx-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: amalgamrx
tags:
- Company
- Health Tech
- Artificial Intelligence
- SaMD
- Healthcare
website: https://amalgamrx.com
---
