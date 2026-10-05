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
  href: https://raw.githubusercontent.com/api-evangelist/better-world/refs/heads/main/hosts/better-world-hosts.yml
  title: ''
  type: Hosts
  url: hosts/better-world-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/better-world/refs/heads/main/vendors/better-world-vendors.yml
  title: ''
  type: Vendors
  url: vendors/better-world-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/better-world/refs/heads/main/security/better-world-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/better-world-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.betterworldbooks.com
created: '2026-09-28'
description: Better World Books is an online retailer of new and used books, offering a wide selection of titles across genres. Founded with a mission to promote literacy and support communities, the company donates a portion of its proceeds to fund book donations worldwide. Their platform includes features such as rewards, gift certificates, and a robust search system, catering to readers looking for affordable books while contributing to charitable causes.
layout: provider
modified: '2026-09-28'
name: Better World Books
nav: Providers
network: true
overview: Better World Books is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Books, Retail, Literacy, and E-Commerce.
random_paper: 11
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
  name: Better World Domain Security
  slug: better-world-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: better-world
tags:
- Company
- Books
- Retail
- Literacy
- E-Commerce
website: https://www.betterworldbooks.com
---
