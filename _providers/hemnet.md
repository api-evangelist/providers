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
artifact_total: 2
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/hemnet/refs/heads/main/well-known/hemnet-hemnet-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/hemnet-hemnet-security.txt
- group: auth
  title: ''
  type: Security
  url: https://www.hemnet.se/responsible-disclosure
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/hemnet/refs/heads/main/well-known/hemnet-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/hemnet-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/hemnet/refs/heads/main/well-known/hemnet-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/hemnet-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/hemnet/refs/heads/main/hosts/hemnet-hosts.yml
  title: ''
  type: Hosts
  url: hosts/hemnet-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/hemnet/refs/heads/main/vendors/hemnet-vendors.yml
  title: ''
  type: Vendors
  url: vendors/hemnet-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hemnet
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/hemnet/refs/heads/main/security/hemnet-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/hemnet-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/hemnet/refs/heads/main/security/hemnet-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hemnet-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://hemnet.se/
created: '2026-10-14'
description: Hemnet is Sweden’s leading online real‑estate marketplace, connecting home buyers with property listings across the country. The platform aggregates listings from real‑estate agents, providing detailed property information, photos, price history, and neighborhood data. Users can search, filter, and save favorite homes, while agents use Hemnet’s tools to showcase properties and reach a broad audience. Hemnet’s API enables developers to integrate property data into applications, offering endpoints for search, property details, and market statistics, supporting innovative real‑estate solutions and data‑driven insights.
layout: provider
modified: '2026-10-14'
name: Hemnet
nav: Providers
network: true
overview: Hemnet is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Real Estate, Marketplace, Sweden, and Property Listings.
random_paper: 3
score:
  band: minimal
  composite: 5.1
  coverage:
    artifact_dirs: 5
    catalog_earned: 20.0
    catalog_earned_first_party: 0.0
    catalog_gap: 95.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 35.7
    operational_transparency: 15.8
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Hemnet Domain Security
  slug: hemnet-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Hemnet Vulnerability Disclosure
  slug: hemnet-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: hemnet
tags:
- Real Estate
- Marketplace
- Sweden
- Property Listings
website: https://hemnet.se/
---
