---
access_model:
  confidence: low
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - security
  trial: false
  try_now: false
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 14.4
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 3
common:
- group: auth
  href: https://artifacts.apis.io/metrc/well-known/metrc-learn-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/metrc-learn-security.txt
- group: agent
  href: https://artifacts.apis.io/metrc/well-known/metrc-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/metrc-well-known.yml
- group: other
  href: https://artifacts.apis.io/metrc/hosts/metrc-hosts.yml
  title: ''
  type: Hosts
  url: hosts/metrc-hosts.yml
- group: other
  href: https://artifacts.apis.io/metrc/vendors/metrc-vendors.yml
  title: ''
  type: Vendors
  url: vendors/metrc-vendors.yml
- group: auth
  href: https://artifacts.apis.io/metrc/security/metrc-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/metrc-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://metrc.com/
coverage:
  checked: '2026-10-27'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found on any discovered host.
  evidence:
  - status: error
    url: https://api.metrc.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-27'
description: Metrc provides a state‑mandated cannabis track‑and‑trace system used across many U.S. states. Their platform enables regulators and licensed businesses to record, monitor, and report the movement of cannabis plants and products from seed to sale, ensuring compliance with state laws. Metrc offers APIs for data integration, reporting, and real‑time inventory management, supporting a wide range of compliance workflows for growers, processors, distributors, and retailers.
layout: provider
modified: '2026-10-27'
name: Metrc
nav: Providers
network: true
overview: Metrc is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cannabis, Track and Trace, and Compliance.
random_paper: 11
scopes:
- name: Metrc Scopes
  scope_count: 0
  slug: metrc-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 5.9
  coverage:
    artifact_dirs: 20
    catalog_earned: 20.0
    catalog_earned_first_party: 0.0
    catalog_gap: 95.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.9
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 35.7
    operational_transparency: 10.5
  previous_composite: 6.8
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/metrc/metrc-2026-11-03T135541.png
security:
- kind: authentication
  name: Metrc Authentication
  slug: metrc-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Metrc Domain Security
  slug: metrc-domain-security
  summary_line: TLSv1.3 · DMARC
slug: metrc
tags:
- Company
- Cannabis
- Track and Trace
- Compliance
website: https://metrc.com/
---
