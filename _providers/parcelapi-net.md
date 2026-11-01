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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: US parcel and building-permit records from cleared public sources.
  name: parcelapi.net API
  slug: parcelapi-net-api
artifact_total: 2
common:
- group: design
  href: https://artifacts.apis.io/parcelapi-net/conformance/parcelapi-net-conformance.yml
  title: ''
  type: Conformance
  url: conformance/parcelapi-net-conformance.yml
- group: agent
  href: https://artifacts.apis.io/parcelapi-net/llms/parcelapi-net-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/parcelapi-net-llms.txt
- group: other
  href: https://artifacts.apis.io/parcelapi-net/hosts/parcelapi-net-hosts.yml
  title: ''
  type: Hosts
  url: hosts/parcelapi-net-hosts.yml
- group: other
  href: https://artifacts.apis.io/parcelapi-net/vendors/parcelapi-net-vendors.yml
  title: ''
  type: Vendors
  url: vendors/parcelapi-net-vendors.yml
- group: auth
  href: https://artifacts.apis.io/parcelapi-net/security/parcelapi-net-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/parcelapi-net-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://parcelapi.net/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://parcelapi.net/mcp
- group: docs
  title: ''
  type: Documentation
  url: https://api.parcelapi.net/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://parcelapi.net/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://parcelapi.net/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://parcelapi.net/privacy
- group: other
  title: ''
  type: RefundPolicy
  url: https://parcelapi.net/refund
created: '2026-10-30'
description: ParcelAPI provides a public US property parcel records API, delivering parcel and building permit data sourced from government assessors and GIS datasets. The service emphasizes privacy by excluding owner personal information, offering credit‑based pricing, and supporting AI agents, developers, and data applications. It operates via API keys, with prepaid or subscription plans, and includes detailed documentation, pricing, terms, privacy, and refund policies.
image: https://parcelapi.net/logo.png
layout: provider
modified: '2026-10-30'
name: parcelapi-net
nav: Providers
network: true
overview: 'parcelapi-net is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, API, RealEstate, Data, and US.


  parcelapi-net''s developer surface includes documentation, pricing, and 10 more developer resources.'
random_paper: 21
score:
  band: emerging
  composite: 19.2
  coverage:
    artifact_dirs: 10
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 16.4
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 66.1
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Parcelapi Net Domain Security
  slug: parcelapi-net-domain-security
  summary_line: TLSv1.3
slug: parcelapi-net
tags:
- Company
- API
- RealEstate
- Data
- US
website: https://parcelapi.net/
---
