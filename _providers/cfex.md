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
api_count: 1
apis:
- description: Billing and settlement solution for AI products and services.
  name: CFEX API
  slug: cfex-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: Compliance
  url: https://cfex.ai/security
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cfex/refs/heads/main/hosts/cfex-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cfex-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cfex/refs/heads/main/vendors/cfex-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cfex-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://cfex.ai/security/soc2-report
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cfex/refs/heads/main/security/cfex-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/cfex-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cfex/refs/heads/main/security/cfex-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cfex-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cfex.ai/
coverage:
  checked: '2026-10-08'
  detail: Main site returns HTML but no machine‑readable API spec; attempts to fetch common OpenAPI paths returned 404.
  evidence:
  - status: 404
    url: https://cfex.ai/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-07'
description: CFEX provides a utility‑grade billing and settlement platform for energy, compute, and AI value chains. Its mission is to streamline granular, contract‑based transactions between buyers and sellers, minimizing errors, lowering costs, and improving auditability. The founding team brings decades of experience in utilities, energy, telecom, and digital media, delivering solutions that monetize goods and services, optimize revenue, and support AI-driven markets.
image: https://www.cfexcloud.com/opengraph-image.png?opengraph-image.0n-r_c1tyh-ch.png
layout: provider
modified: '2026-10-07'
name: CFEX
nav: Providers
network: true
overview: CFEX is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Billing, Settlement, Energy, Compute, and Artificial Intelligence.
random_paper: 4
score:
  band: minimal
  composite: 9.5
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.1
    operational_transparency: 10.5
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 8.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cfex Domain Security
  slug: cfex-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: trust-center
  name: Cfex Trust Center
  slug: cfex-trust-center
  summary_line: SOC 2
slug: cfex
tags:
- Billing
- Settlement
- Energy
- Compute
- Artificial Intelligence
- Tokens
- Enterprise
website: https://cfex.ai/
---
