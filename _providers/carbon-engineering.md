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
  href: https://raw.githubusercontent.com/api-evangelist/carbon-engineering/refs/heads/main/hosts/carbon-engineering-hosts.yml
  title: ''
  type: Hosts
  url: hosts/carbon-engineering-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/carbon-engineering/refs/heads/main/vendors/carbon-engineering-vendors.yml
  title: ''
  type: Vendors
  url: vendors/carbon-engineering-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.carbonengineering.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.carbonengineering.com/news/1pointfive-and-nyk-announce-carbon-removal-agreement
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/carbon-engineering/refs/heads/main/security/carbon-engineering-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/carbon-engineering-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.carbonengineering.com/
coverage:
  checked: '2026-10-07'
  detail: No OpenAPI or other machine‑readable contract found at the API host.
  evidence:
  - status: 0
    url: https://api.carbonengineering.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-07'
description: Carbon Engineering is a Direct Air Capture (DAC) technology company founded in 2009. It develops large‑scale systems to capture CO₂ from the atmosphere, aiming to enable cost‑effective negative emissions. The company operates out of Kitty Hawk, North Carolina, and focuses on research, development, and commercial deployment of carbon removal solutions.
image: https://cdn.craft.cloud/019dda21-6dfd-7184-8657-7e878e361710/assets/global/carbon-engineering-logo-1200x675.webp?fit=cover&height=630&width=1200&s=hy9UHF7UlrH0GEc678vMBMmQZTb7ZUsmgpX-b44xkmU
layout: provider
modified: '2026-10-07'
name: Carbon Engineering
nav: Providers
network: true
overview: Carbon Engineering is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Direct Air Capture and Climate Tech.
random_paper: 11
score:
  band: minimal
  composite: 5.4
  coverage:
    artifact_dirs: 6
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 41.1
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Carbon Engineering Domain Security
  slug: carbon-engineering-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: carbon-engineering
tags:
- Direct Air Capture
- Climate Tech
website: https://www.carbonengineering.com/
---
