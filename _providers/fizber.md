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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/fizber/hosts/fizber-hosts.yml
  title: ''
  type: Hosts
  url: hosts/fizber-hosts.yml
- group: docs
  title: ''
  type: Documentation
  url: https://dev.fizber.com/
- group: auth
  href: https://artifacts.apis.io/fizber/security/fizber-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/fizber-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://fizber.com/
coverage:
  checked: '2026-10-28'
  detail: Fizber.com provides a real‑estate marketplace with no public API or developer documentation.
  evidence:
  - status: 200
    url: https://dev.fizber.com/
  reason: not-a-software-company
  state: none
created: '2026-10-28'
description: Fizber.com operates a free, for‑sale‑by‑owner (FSBO) real‑estate platform that enables homeowners to list their properties directly online, reach a wide audience, and avoid traditional real‑estate commissions. The site offers tools for creating listings, marketing homes, and managing inquiries, positioning itself as a cutting‑edge marketplace for DIY home sellers.
image: http://www.fizber.com/images/about.png
layout: provider
modified: '2026-10-28'
name: Fizber.com
nav: Providers
network: true
overview: 'Fizber.com is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Real Estate, FSBO, Marketplace, Free Listings, and Housing.


  Fizber.com''s developer surface includes documentation and 3 more developer resources.'
random_paper: 18
score:
  band: minimal
  composite: 5.3
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Fizber Domain Security
  slug: fizber-domain-security
  summary_line: no transport/DNS hardening detected
slug: fizber
tags:
- Real Estate
- FSBO
- Marketplace
- Free Listings
- Housing
website: https://fizber.com/
---
