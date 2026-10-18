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
  href: https://raw.githubusercontent.com/api-evangelist/chestnutcarbon/refs/heads/main/hosts/chestnutcarbon-hosts.yml
  title: ''
  type: Hosts
  url: hosts/chestnutcarbon-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/chestnutcarbon/refs/heads/main/vendors/chestnutcarbon-vendors.yml
  title: ''
  type: Vendors
  url: vendors/chestnutcarbon-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://chestnutcarbon.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://chestnutcarbon.com/privacy-policy/
- group: other
  title: ''
  type: Leadership
  url: https://chestnutcarbon.com/team/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/chestnutcarbon/refs/heads/main/security/chestnutcarbon-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/chestnutcarbon-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://chestnutcarbon.com
coverage:
  checked: '2026-10-08'
  detail: The provider's website does not expose any machine‑readable API specification.
  evidence:
  - status: 200
    url: https://chestnutcarbon.com
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-08'
description: Chestnutcarbon is a U.S.-based nature‑based carbon removal company that develops, finances, and operates forest‑based carbon offset projects. It focuses on afforestation, improved forest management, and nature‑works initiatives, delivering high‑quality carbon credits to corporate clients and investors. The firm emphasizes transparency, community benefits, and biodiversity, managing over 90,000 acres of land and supporting sustainable land restoration across the United States.
image: https://chestnutcarbon.com/wp-content/uploads/2025/09/chestnut-carbon-og-img.webp
layout: provider
modified: '2026-10-08'
name: Chestnutcarbon
nav: Providers
network: true
overview: Chestnutcarbon is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Carbon, Environment, Forestry, and Sustainability.
random_paper: 11
score:
  band: minimal
  composite: 9.0
  coverage:
    artifact_dirs: 7
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
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    mcp: derived
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
  name: Chestnutcarbon Domain Security
  slug: chestnutcarbon-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: chestnutcarbon
tags:
- Company
- Carbon
- Environment
- Forestry
- Sustainability
website: https://chestnutcarbon.com
---
