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
  href: https://raw.githubusercontent.com/api-evangelist/chronextcom/refs/heads/main/hosts/chronextcom-hosts.yml
  title: ''
  type: Hosts
  url: hosts/chronextcom-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/chronextcom/refs/heads/main/vendors/chronextcom-vendors.yml
  title: ''
  type: Vendors
  url: vendors/chronextcom-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/chronextcom/refs/heads/main/security/chronextcom-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/chronextcom-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://equityzen.com/company/chronextcom
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.chronext.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.chronext.com/privacy-policy
- group: other
  title: ''
  type: Imprint
  url: https://www.chronext.com/imprint
created: '2026-10-08'
description: Chronextcom is a luxury watch retailer based in Germany, offering certified pre-owned and new high-end watches from brands such as Rolex, Omega, Patek Philippe, Audemars Piguet, and Cartier. The company provides secure online purchasing, free delivery, a 14‑day return policy, and a dedicated customer service team. Their platform includes detailed product pages, a blog, and a contact center, positioning Chronext as a trusted source for premium timepieces.
layout: provider
modified: '2026-10-08'
name: Chronextcom
nav: Providers
network: true
overview: Chronextcom is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Luxury, Watches, E-Commerce, and Germany.
random_paper: 6
score:
  band: minimal
  composite: 8.5
  coverage:
    artifact_dirs: 5
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: venue_as_website
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
  name: Chronextcom Domain Security
  slug: chronextcom-domain-security
  summary_line: TLSv1.3 · DMARC
slug: chronextcom
tags:
- Company
- Luxury
- Watches
- E-Commerce
- Germany
website: https://equityzen.com/company/chronextcom
---
