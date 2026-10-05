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
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bighaat/refs/heads/main/hosts/bighaat-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bighaat-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bighaat/refs/heads/main/vendors/bighaat-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bighaat-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bighaat/refs/heads/main/security/bighaat-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bighaat-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://equityzen.com/company/bighaat
coverage:
  checked: '2026-09-28'
  detail: Bighaat’s public site provides only shopping pages and no API documentation or developer portal.
  evidence:
  - status: 200
    url: https://www.bighaat.com
  reason: no-developer-program
  state: none
created: '2026-09-28'
description: Bighaat is the largest pan‑India digital marketplace for agricultural inputs, connecting farmers with a wide range of high‑quality seeds, fertilizers, pesticides, and equipment. Founded in 2015, the platform offers personalized technical guidance, data‑driven insights, and seamless logistics to improve sustainability and profitability for millions of farmers across India.
layout: provider
modified: '2026-09-28'
name: Bighaat
nav: Providers
network: true
overview: Bighaat is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Agriculture, Marketplace, India, AgTech, and B2B.
random_paper: 16
score:
  band: minimal
  composite: 3.0
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
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - india
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - india-south-asia
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: venue_as_website
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bighaat Domain Security
  slug: bighaat-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bighaat
tags:
- Agriculture
- Marketplace
- India
- AgTech
- B2B
website: https://equityzen.com/company/bighaat
---
