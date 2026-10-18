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
  href: https://raw.githubusercontent.com/api-evangelist/cormintdatasystems/refs/heads/main/hosts/cormintdatasystems-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cormintdatasystems-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cormintdatasystems/refs/heads/main/vendors/cormintdatasystems-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cormintdatasystems-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cormint.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cormint.com/privacy
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cormintdatasystems/refs/heads/main/security/cormintdatasystems-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cormintdatasystems-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cormint.com
coverage:
  checked: '2026-10-11'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found at the API host.
  evidence:
  - status: 0
    url: https://api.cormint.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-11'
description: Cormint Data Systems designs, manufactures, and operates high‑performance power infrastructure for large‑scale data centers and Bitcoin mining operations. The company builds modular power systems in‑house, operates multiple sites in Texas, and provides turnkey solutions for AI‑intensive workloads, emphasizing cost‑efficiency and reliability.
image: https://www.cormint.com/media/social-card-cormint-v1.png
layout: provider
modified: '2026-10-11'
name: Cormintdatasystems
nav: Providers
network: true
overview: Cormintdatasystems is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, DataCenter, BitcoinMining, PowerInfrastructure, and Artificial Intelligence.
random_paper: 8
score:
  band: minimal
  composite: 8.7
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cormintdatasystems Domain Security
  slug: cormintdatasystems-domain-security
  summary_line: TLSv1.3
slug: cormintdatasystems
tags:
- Company
- DataCenter
- BitcoinMining
- PowerInfrastructure
- Artificial Intelligence
website: https://www.cormint.com
---
