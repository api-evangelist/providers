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
  href: https://raw.githubusercontent.com/api-evangelist/carbontrack/refs/heads/main/hosts/carbontrack-hosts.yml
  title: ''
  type: Hosts
  url: hosts/carbontrack-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/carbontrack/refs/heads/main/vendors/carbontrack-vendors.yml
  title: ''
  type: Vendors
  url: vendors/carbontrack-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.enervaro.com.au/terms-conditions-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.enervaro.com.au/privacy-policy
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/carbontrack/refs/heads/main/security/carbontrack-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/carbontrack-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://enervaro.com.au
coverage:
  checked: '2026-10-07'
  detail: No public developer documentation or machine‑readable API specification was found on the provider’s hosts.
  evidence:
  - status: 404
    url: https://api.enervaro.com.au/openapi.json
  reason: no-developer-program
  state: none
created: '2026-10-07'
description: Carbontrack (carbonTRACK) is an Australian technology company specializing in smart energy management systems and IoT solutions. Headquartered in Melbourne, it provides a patented intelligent energy management platform that enables users and providers to monitor, control and automate energy consumption, generation and storage, supporting a decentralized energy future.
image: https://cdn.prod.website-files.com/699d0a9fc8316b39f5c5d084/69b0e39412c3dce60a3693c7_f23e26c1b726546094947096737a85a0_enervaro-feature.png
layout: provider
modified: '2026-10-07'
name: Carbontrack
nav: Providers
network: true
overview: Carbontrack is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, IoT, SmartGrid, and Australia.
random_paper: 18
score:
  band: minimal
  composite: 8.8
  coverage:
    artifact_dirs: 4
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
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 11.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Carbontrack Domain Security
  slug: carbontrack-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: carbontrack
tags:
- Company
- Energy
- IoT
- SmartGrid
- Australia
- Software-as-a-Service
website: https://enervaro.com.au
---
