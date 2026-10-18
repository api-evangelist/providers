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
- description: API for Standab parking and charging infrastructure platform
  name: Standab API
  slug: standab-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/standab/refs/heads/main/llms/standab-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/standab-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/standab/refs/heads/main/hosts/standab-hosts.yml
  title: ''
  type: Hosts
  url: hosts/standab-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/standab/refs/heads/main/vendors/standab-vendors.yml
  title: ''
  type: Vendors
  url: vendors/standab-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/standab/refs/heads/main/security/standab-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/standab-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.standab.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.standab.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.standab.com/terms
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://standab.com/
  reason: no-developer-program
  state: none
created: '2026-10-15'
description: Standab provides parking and charging infrastructure solutions for shared micromobility fleets, enabling cities and operators to manage scooters and e‑bikes efficiently. Their platform offers structured parking spaces, charging stations, and operational tools to integrate with public spaces, addressing the physical infrastructure gap in micromobility deployments. Standab works with municipalities and mobility operators to create safe, organized, and scalable micromobility ecosystems.
image: https://www.standab.com/assets/standab-cover.jpg
layout: provider
modified: '2026-10-15'
name: Standab
nav: Providers
network: true
overview: Standab is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Micromobility, Infrastructure, Parking, and Charging.
random_paper: 7
score:
  band: minimal
  composite: 10.4
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 64.3
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Standab Domain Security
  slug: standab-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: standab
tags:
- Company
- Micromobility
- Infrastructure
- Parking
- Charging
website: https://www.standab.com/
---
