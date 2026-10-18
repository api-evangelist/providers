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
- description: API information not publicly documented.
  name: Carbon America API
  slug: carbon-america-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/carbon-america/refs/heads/main/hosts/carbon-america-hosts.yml
  title: ''
  type: Hosts
  url: hosts/carbon-america-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/carbon-america/refs/heads/main/vendors/carbon-america-vendors.yml
  title: ''
  type: Vendors
  url: vendors/carbon-america-vendors.yml
- group: other
  title: ''
  type: Leadership
  url: https://www.carbonamerica.com/team
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/carbon-america/refs/heads/main/security/carbon-america-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/carbon-america-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.carbonamerica.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.carbonamerica.com/
  reason: no-developer-program
  state: none
created: '2026-10-06'
description: Carbon America is a carbon capture and storage (CCS) developer focused on delivering the full CO₂ capture‑transport‑storage value chain. The company designs, builds, and operates large‑scale CCS projects, partnering with emitters, communities, and investors to reduce industrial emissions and combat climate change. With a mission to make climate change history, Carbon America leverages its proprietary technology and expertise to create secure geological storage solutions worldwide.
image: https://images.squarespace-cdn.com/content/v1/63dd6ef242301709c49831cd/1675456249571-N3UZ8XE7BRRNYQ0W1TDU/BrentLewis2.jpg
layout: provider
modified: '2026-10-06'
name: Carbon America
nav: Providers
network: true
overview: Carbon America is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Carbon, Climate, CCS, and Energy.
random_paper: 10
score:
  band: minimal
  composite: 4.6
  coverage:
    artifact_dirs: 5
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 58.9
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 4.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Carbon America Domain Security
  slug: carbon-america-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: carbon-america
tags:
- Company
- Carbon
- Climate
- CCS
- Energy
- Sustainability
website: https://www.carbonamerica.com/
---
