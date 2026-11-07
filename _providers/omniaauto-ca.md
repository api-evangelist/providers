---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.omniaauto.ca
  baseurl_source: declared
  description: Canadian Vehicle Listings REST API
  name: OmniaAuto API
  slug: omniaauto-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/omniaauto-ca/plans/omniaauto-ca-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/omniaauto-ca-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/omniaauto-ca/conformance/omniaauto-ca-conformance.yml
  title: ''
  type: Conformance
  url: conformance/omniaauto-ca-conformance.yml
- group: agent
  href: https://artifacts.apis.io/omniaauto-ca/llms/omniaauto-ca-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/omniaauto-ca-llms.txt
- group: agent
  href: https://artifacts.apis.io/omniaauto-ca/well-known/omniaauto-ca-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/omniaauto-ca-well-known.yml
- group: other
  href: https://artifacts.apis.io/omniaauto-ca/hosts/omniaauto-ca-hosts.yml
  title: ''
  type: Hosts
  url: hosts/omniaauto-ca-hosts.yml
- group: other
  href: https://artifacts.apis.io/omniaauto-ca/vendors/omniaauto-ca-vendors.yml
  title: ''
  type: Vendors
  url: vendors/omniaauto-ca-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://omniaauto.ca/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://omniaauto.ca/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://omniaauto.ca/pricing
- group: docs
  title: ''
  type: APIReference
  url: https://omniaauto.ca/docs
- group: auth
  href: https://artifacts.apis.io/omniaauto-ca/security/omniaauto-ca-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/omniaauto-ca-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://omniaauto.ca/
created: '2026-10-30'
description: OmniaAuto provides Canadian vehicle listings data through a market data platform (MCP) and a RESTful API. It offers real-time inventory, VIN decoding, and market valuation across Canada, accessible via subscription. The service includes CSV snapshots, AI integration, and detailed pricing coverage, targeting developers, analysts, and automotive businesses.
image: https://omniaauto.ca/og-default.png
layout: provider
modified: '2026-10-30'
name: omniaauto-ca
nav: Providers
network: true
overview: 'omniaauto-ca is listed with 1 API on the [APIs.io](https://apis.io/) network: OmniaAuto API. Tagged areas include Company, Automotive, Data, and Markets.


  omniaauto-ca''s developer surface includes pricing, API reference, and 10 more developer resources.'
plans:
- name: Omniaauto Ca Plans Pricing
  plan_count: 21
  slug: omniaauto-ca-plans-pricing
random_paper: 14
score:
  band: thin
  composite: 26.3
  coverage:
    artifact_dirs: 12
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.3
  facets:
    access_clarity: 47.4
    contract_governance: 4.5
    contract_quality: 36.0
    developer_ergonomics: 3.6
    discoverability: 57.1
    operational_transparency: 0.0
  previous_composite: 31.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/omniaauto-ca/omniaauto-ca-2026-11-03T140534.png
security:
- kind: domain-security
  name: Omniaauto Ca Domain Security
  slug: omniaauto-ca-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: omniaauto-ca
tags:
- Company
- Automotive
- Data
- Markets
website: https://omniaauto.ca/
---
