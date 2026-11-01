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
artifact_total: 3
common:
- group: other
  href: https://artifacts.apis.io/depoly/hosts/depoly-hosts.yml
  title: ''
  type: Hosts
  url: hosts/depoly-hosts.yml
- group: other
  href: https://artifacts.apis.io/depoly/vendors/depoly-vendors.yml
  title: ''
  type: Vendors
  url: vendors/depoly-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.depoly.co/legal/privacy
- group: auth
  href: https://artifacts.apis.io/depoly/security/depoly-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/depoly-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.depoly.co/
- group: company
  title: ''
  type: Blog
  url: https://www.depoly.co/news
- group: operate
  title: ''
  type: Support
  url: https://www.depoly.co/contact
coverage:
  checked: '2026-10-29'
  detail: DePoly provides a material recycling technology and does not expose a public API or developer program.
  evidence:
  - status: 200
    url: https://www.depoly.co/
  reason: not-a-software-company
  state: none
created: '2026-10-29'
description: DePoly’s novel and patented technology breaks down PET back to monomers, enabling the production of recycled PET and fostering a sustainable circular economy for plastics. Over 90% of plastics worldwide are not recycled; DePoly aims to change this by providing a clean, scalable solution that transforms waste into valuable raw material, supporting industries in adopting circular practices and reducing reliance on virgin fossil resources.
image: https://cdn.prod.website-files.com/65fc1876777e6eaf167fad43/660c16e63dc8e9d9633cd098_logo-horizontal.svg
layout: provider
modified: '2026-10-29'
name: DePoly
nav: Providers
network: true
overview: 'DePoly is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Recycling, Plastics, CircularEconomy, and Technology.


  DePoly''s developer surface includes engineering blog, support, and 5 more developer resources.'
random_paper: 5
scopes:
- name: Depoly Scopes
  scope_count: 0
  slug: depoly-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 9.0
  coverage:
    artifact_dirs: 16
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Depoly Authentication
  slug: depoly-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Depoly Domain Security
  slug: depoly-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: depoly
tags:
- Company
- Recycling
- Plastics
- CircularEconomy
- Technology
website: https://www.depoly.co/
---
