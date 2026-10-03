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
  href: https://raw.githubusercontent.com/api-evangelist/bestyetmarket/refs/heads/main/hosts/bestyetmarket-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bestyetmarket-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bestyetmarket/refs/heads/main/vendors/bestyetmarket-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bestyetmarket-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bestyetmarket/refs/heads/main/security/bestyetmarket-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bestyetmarket-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://equityzen.com/company/bestyetmarket
created: '2026-09-28'
description: Bestyetmarket is a stub entry created from the API Evangelist secondary‑market harvest. The company appears in public listings as a regional supermarket chain formerly operating in New York, Connecticut, and New Jersey under the brand Best Yet Market. It was founded in 1994 and headquartered in Bethpage, New York. No active corporate website or API documentation could be located despite web searches, indicating the business may be defunct or its online presence is unavailable.
layout: provider
modified: '2026-09-28'
name: Bestyetmarket
nav: Providers
network: true
overview: Bestyetmarket is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Retail, Grocery, Supermarket, and New York.
random_paper: 4
score:
  band: minimal
  composite: 3.0
  coverage:
    artifact_dirs: 3
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
    score: 5.9
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bestyetmarket Domain Security
  slug: bestyetmarket-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bestyetmarket
tags:
- Company
- Retail
- Grocery
- Supermarket
- New York
website: https://equityzen.com/company/bestyetmarket
---
