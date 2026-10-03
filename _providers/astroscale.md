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
  href: https://raw.githubusercontent.com/api-evangelist/astroscale/refs/heads/main/hosts/astroscale-hosts.yml
  title: ''
  type: Hosts
  url: hosts/astroscale-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/astroscale/refs/heads/main/vendors/astroscale-vendors.yml
  title: ''
  type: Vendors
  url: vendors/astroscale-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.astroscale.com/en/news
- group: other
  title: ''
  type: Leadership
  url: https://astroscale.com/de/ir/management/info
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/astroscale/refs/heads/main/security/astroscale-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/astroscale-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.astroscale.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.astroscale.com/en/legal/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.astroscale.com/en/legal/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://www.astroscale.com/en/contact
coverage:
  checked: 2026-09-26
  detail: Unable to resolve api.astroscale.com or locate any OpenAPI/AsyncAPI/GraphQL spec.
  evidence:
  - status: 0
    url: https://api.astroscale.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-26'
description: Astroscale provides on‑orbit servicing and space sustainability solutions, offering end‑to‑end services such as mission licensing, spectrum acquisition, insurance, and operations for debris removal and satellite life‑extension. The company aims to accelerate space development while ensuring long‑term orbital sustainability for future generations.
image: https://images.ctfassets.net/k5fy2axdrsqr/3M0Ep5FG4nrFilGMY2R9me/636adf872fbbf6d5c04fa88cd31024f8/black_white_logo.png
layout: provider
modified: '2026-09-26'
name: Astroscale
nav: Providers
network: true
overview: 'Astroscale is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Space, Sustainability, On-Orbit Servicing, and Debris‑removal.


  Astroscale''s developer surface includes support and 8 more developer resources.'
random_paper: 17
score:
  band: minimal
  composite: 10.1
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
    developer_ergonomics: 4.8
    discoverability: 51.8
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Astroscale Domain Security
  slug: astroscale-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: astroscale
tags:
- Company
- Space
- Sustainability
- On-Orbit Servicing
- Debris‑removal
website: https://www.astroscale.com
---
