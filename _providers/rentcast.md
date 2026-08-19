---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: na
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.8
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Rentcast Agentic Access
  operation_count: 10
  slug: rentcast-agentic-access
  summary_line: 10 operations
api_count: 4
apis:
- description: The Avm API from RentCast — 2 operation(s) for avm.
  name: RentCast Avm API
  slug: rentcast-avm-api
- description: The Listings API from RentCast — 4 operation(s) for listings.
  name: RentCast Listings API
  slug: rentcast-listings-api
- description: The Markets API from RentCast — 1 operation(s) for markets.
  name: RentCast Markets API
  slug: rentcast-markets-api
- description: The Properties API from RentCast — 3 operation(s) for properties.
  name: RentCast Properties API
  slug: rentcast-properties-api
artifact_total: 24
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: RentCast Avm API
  slug: open-rentcast-avm-api
- collection_type: open
  name: RentCast Avm Listings API
  slug: open-rentcast-listings-api
- collection_type: open
  name: RentCast Avm Markets API
  slug: open-rentcast-markets-api
- collection_type: open
  name: RentCast Avm Properties API
  slug: open-rentcast-properties-api
- collection_type: open
  name: RentCast API
  slug: open-rentcast
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/rentcast-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rentcast-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/rentcast-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.rentcast.io
- group: start
  title: ''
  type: Portal
  url: https://developers.rentcast.io
- group: start
  title: ''
  type: Portal
  url: https://app.rentcast.io/app/api
- group: docs
  title: ''
  type: Documentation
  url: https://www.rentcast.io/api
- group: operate
  title: ''
  type: Support
  url: https://help.rentcast.io
- group: company
  title: ''
  type: Blog
  url: https://www.rentcast.io/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/RentCast
- group: agent
  title: ''
  type: LlmsText
  url: https://developers.rentcast.io/llms.txt
created: '2025-03-01'
description: RentCast provides a real estate data API with instant access to over 140 million property records, automated valuation models (AVM) for home value and rent estimates, active and historical sale and rental listings, and aggregate real estate market statistics for US zip codes. The API enables real estate investors, property managers, landlords, and proptech applications to programmatically access comprehensive residential and commercial property data across all 50 US states.
examples:
- key_count: 4
  name: Rentcast Property Search Example
  slug: rentcast-property-search-example
- key_count: 4
  name: Rentcast Rent Estimate Example
  slug: rentcast-rent-estimate-example
finops:
- name: Rentcast Finops
  service_category: API
  slug: rentcast-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rentcast.png
json_schemas:
- name: RentCast Property Estimate
  property_count: 6
  slug: rentcast-estimate
- name: RentCast Property Record
  property_count: 21
  slug: rentcast-property
json_structures:
- name: Rentcast Property Structure
  property_count: 0
  slug: rentcast-property-structure
jsonld:
- class_count: 22
  name: Rentcast Context
  property_count: 9
  slug: rentcast-context
layout: provider
modified: '2026-05-19'
name: RentCast
nav: Providers
network: true
overview: 'RentCast publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Avm API, Listings API, Markets API, and 1 more. Tagged areas include Real Estate, Property Data, Valuation, Rental Market, and AVM.


  The RentCast catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  RentCast''s developer surface includes authentication, developer portal, documentation, support, engineering blog, and 6 more developer resources.'
plans:
- name: Rentcast Plans Pricing
  plan_count: 3
  slug: rentcast-plans-pricing
random_paper: 123
rate_limits:
- limit_count: 5
  name: Rentcast Rate Limits
  slug: rentcast-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: RentCast API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: rentcast-jsonschema-spectral-rules
- effective_rule_count: 48
  extends:
  - spectral:oas
  name: RentCast API Rules
  rule_count: 7
  severity_counts:
    error: 2
    hint: 2
    info: 0
    warn: 3
  slug: rentcast-rules
score:
  band: thin
  composite: 37.6
  delta: -7.7
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 9.8
    contract_quality: 68.5
    developer_ergonomics: 33.3
    discoverability: 81.5
    governance: 9.8
    operational_transparency: 10.5
  previous_composite: 45.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/rentcast/refs/heads/main/screenshots/rentcast-2026-06-20T192855.png
security:
- kind: authentication
  name: Rentcast Authentication
  slug: rentcast-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Rentcast Domain Security
  slug: rentcast-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: rentcast
tags:
- Real Estate
- Property Data
- Valuation
- Rental Market
- AVM
website: https://www.rentcast.io
---
