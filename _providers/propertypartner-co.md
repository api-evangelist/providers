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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 5
common:
- group: other
  href: https://artifacts.apis.io/propertypartner-co/vendors/propertypartner-co-vendors.yml
  title: ''
  type: Vendors
  url: vendors/propertypartner-co-vendors.yml
- group: other
  href: https://artifacts.apis.io/propertypartner-co/hosts/propertypartner-co-hosts.yml
  title: ''
  type: Hosts
  url: hosts/propertypartner-co-hosts.yml
- group: operate
  title: ''
  type: Support
  url: https://help.londonhouseexchange.com
- group: start
  title: ''
  type: Login
  url: https://www.londonhouseexchange.com/login
- group: company
  title: ''
  type: Blog
  url: https://www.londonhouseexchange.com/blog
- group: docs
  title: ''
  type: Documentation
  url: https://help.londonhouseexchange.com/
- group: company
  title: ''
  type: Website
  url: http://propertypartner.co
- group: auth
  href: https://artifacts.apis.io/propertypartner-co/security/propertypartner-co-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/propertypartner-co-domain-security.yml
coverage:
  checked: '2026-10-29'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract was found after probing typical spec URLs on the provider's API hosts.
  evidence:
  - status: 404
    url: https://api.propertypartner.co/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: PropertyPartner is a technology-driven platform focused on simplifying property investment and ownership. Backed by Seedcamp and part of the VC portfolio, the company aims to provide a regulated marketplace where individuals can invest in real estate assets with transparency and ease. By leveraging modern fintech solutions, PropertyPartner offers tools for investors to discover, evaluate, and purchase fractional property shares, while ensuring compliance with financial regulations. The platform integrates data analytics, secure transaction processing, and a user-friendly interface to democratize access to property markets.
image: https://propertypartner.co/logo.png
layout: provider
modified: '2026-10-28'
name: propertypartner
nav: Providers
network: true
overview: 'propertypartner is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Real Estate, FinTech, Investment, Marketplace, and Property.


  propertypartner''s developer surface includes support, engineering blog, documentation, and 5 more developer resources.'
plans:
- name: Propertypartner Co Plans Pricing
  plan_count: 0
  slug: propertypartner-co-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Propertypartner Co Rate Limits
  slug: propertypartner-co-rate-limits
scopes:
- name: Propertypartner Co Scopes
  scope_count: 0
  slug: propertypartner-co-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 10.9
  coverage:
    artifact_dirs: 21
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
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
    score: 15.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Propertypartner Co Authentication
  slug: propertypartner-co-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Propertypartner Co Domain Security
  slug: propertypartner-co-domain-security
  summary_line: TLSv1.3 · DMARC
slug: propertypartner-co
tags:
- Real Estate
- FinTech
- Investment
- Marketplace
- Property
website: http://propertypartner.co
---
