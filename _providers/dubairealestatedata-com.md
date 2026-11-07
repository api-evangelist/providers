---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API providing real estate market data for Dubai, as documented on the developer portal.
  name: Dubai Real Estate Data API
  slug: dubai-real-estate-data-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/dubairealestatedata-com/llms/dubairealestatedata-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dubairealestatedata-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/dubairealestatedata-com/well-known/dubairealestatedata-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dubairealestatedata-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/dubairealestatedata-com/hosts/dubairealestatedata-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dubairealestatedata-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/dubairealestatedata-com/vendors/dubairealestatedata-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dubairealestatedata-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/dubairealestatedata-com/security/dubairealestatedata-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dubairealestatedata-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.dubairealestatedata.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.dubairealestatedata.com/developers
- group: docs
  title: ''
  type: APIReference
  url: https://www.dubairealestatedata.com/mcp
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.dubairealestatedata.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dubairealestatedata.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.dubairealestatedata.com/price-measures
coverage:
  checked: '2026-11-06'
  detail: Developer portal provides documentation but no machine‑readable OpenAPI/AsyncAPI/GraphQL spec.
  evidence:
  - status: 200
    url: https://www.dubairealestatedata.com/developers
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-06'
description: Dubai Real Estate Data provides open market analytics for Dubai property transactions, offering data on sales volumes, price indexes, rental yields, mortgage statistics, and area‑specific insights. The platform aggregates official DLD open data and presents it through dashboards and downloadable datasets for developers, analysts, and investors.
image: https://www.dubairealestatedata.com/opengraph-image
layout: provider
modified: '2026-11-06'
name: Dubai Real Estate Data
nav: Providers
network: true
overview: 'Dubai Real Estate Data is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Real Estate, Data, Analytics, Dubai, and Open Data.


  Dubai Real Estate Data''s developer surface includes documentation, API reference, pricing, and 8 more developer resources.'
random_paper: 5
score:
  band: emerging
  composite: 16.3
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 19.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dubairealestatedata Com Domain Security
  slug: dubairealestatedata-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: dubairealestatedata-com
tags:
- Real Estate
- Data
- Analytics
- Dubai
- Open Data
website: https://www.dubairealestatedata.com/
---
