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
  href: https://raw.githubusercontent.com/api-evangelist/carbondepositorysa/refs/heads/main/hosts/carbondepositorysa-hosts.yml
  title: ''
  type: Hosts
  url: hosts/carbondepositorysa-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/carbondepositorysa/refs/heads/main/vendors/carbondepositorysa-vendors.yml
  title: ''
  type: Vendors
  url: vendors/carbondepositorysa-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/carbondepositorysa/refs/heads/main/security/carbondepositorysa-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/carbondepositorysa-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://carbondepository.com
coverage:
  checked: '2026-10-07'
  detail: No public developer documentation or API contract was found for the provider.
  evidence:
  - status: 200
    url: https://api.carbondepository.com
  reason: no-developer-program
  state: none
created: '2026-10-07'
description: Carbon Depository S.A. is a Luxembourg‑registered corporation providing secure, blockchain‑powered custody, transfer, and asset management services for certified carbon credits. The platform offers institutional‑grade infrastructure, AI‑driven analytics, and tokenised DeFi options for both regulated and voluntary carbon markets, aiming to deliver transparent, auditable, and regulator‑ready solutions for carbon credit holders.
layout: provider
modified: '2026-10-07'
name: Carbondepositorysa
nav: Providers
network: true
overview: Carbondepositorysa is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Carbon, Custody, Blockchain, and Finance.
random_paper: 11
score:
  band: minimal
  composite: 3.1
  coverage:
    artifact_dirs: 4
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
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Carbondepositorysa Domain Security
  slug: carbondepositorysa-domain-security
  summary_line: TLSv1.3 · HSTS
slug: carbondepositorysa
tags:
- Company
- Carbon
- Custody
- Blockchain
- Finance
website: https://carbondepository.com
---
