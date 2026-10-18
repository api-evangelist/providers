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
  href: https://raw.githubusercontent.com/api-evangelist/carbonbuilt/refs/heads/main/hosts/carbonbuilt-hosts.yml
  title: ''
  type: Hosts
  url: hosts/carbonbuilt-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/carbonbuilt/refs/heads/main/vendors/carbonbuilt-vendors.yml
  title: ''
  type: Vendors
  url: vendors/carbonbuilt-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.carbonbuilt.com/privacy-policy
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/carbonbuilt/refs/heads/main/security/carbonbuilt-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/carbonbuilt-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.carbonbuilt.com/
coverage:
  checked: '2026-10-07'
  detail: The website provides no developer documentation or API reference.
  evidence:
  - status: 200
    url: https://www.carbonbuilt.com/
  reason: no-developer-program
  state: none
created: '2026-10-07'
description: CarbonBuilt produces ultra‑low‑carbon concrete masonry products, replacing up to 50% of cement with its proprietary Reversa® binder. The company offers sustainable building materials that reduce carbon footprints by up to 70% while maintaining price and performance, targeting construction, hardscape and masonry markets worldwide.
layout: provider
modified: '2026-10-07'
name: CarbonBuilt
nav: Providers
network: true
overview: CarbonBuilt is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include construction, Sustainability, concrete, masonry, and low-carbon.
random_paper: 7
score:
  band: minimal
  composite: 5.8
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
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
  name: Carbonbuilt Domain Security
  slug: carbonbuilt-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: carbonbuilt
tags:
- construction
- Sustainability
- concrete
- masonry
- low-carbon
website: https://www.carbonbuilt.com/
---
