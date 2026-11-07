---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 7.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: GET /validate — validate a phone number and return validity, local and international formats, country, location, carrier, and line type. Read-only, single-endpoint lookup API.
  name: Numverify API
  slug: numverify-api
artifact_total: 6
common:
- group: commercial
  href: https://artifacts.apis.io/numverify/plans/numverify-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/numverify-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/numverify/rate-limits/numverify-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/numverify-rate-limits.yml
- group: auth
  href: https://artifacts.apis.io/numverify/security/numverify-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/numverify-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://numverify.com
- group: docs
  title: ''
  type: Documentation
  url: https://numverify.com/documentation
- group: commercial
  title: ''
  type: Pricing
  url: https://numverify.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://numverify.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ideracorp.com/legal/APILayer
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ideracorp.com/Legal/PrivacyPolicy
- group: company
  title: ''
  type: Blog
  url: https://blog.apilayer.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apilayer
- group: operate
  title: ''
  type: StatusPage
  url: https://numverify.com/api-status
- group: build
  href: https://artifacts.apis.io/numverify/packages/numverify-packages.yml
  title: ''
  type: Packages
  url: packages/numverify-packages.yml
created: '2026-09-16'
description: Numverify is a free and simple REST API for national and international phone number validation and lookup across 232 countries, operated by APILayer (an Idera, Inc. brand). A single validate call returns whether a number is valid along with its local and international formats, country code and name, approximate location, carrier, and line type (mobile or landline). Authentication is by API key with two published bases — the legacy apilayer.net host (access_key query parameter) and the newer api.apilayer.com marketplace host (apikey header) — and access is metered by monthly request quota across free and paid plans.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: MCP server requiring an API key; 1 tool listed. A candidate, not confirmed as published by the provider.
  name: Numverify API MCP Server
  slug: numverify-mcp-yml
modified: '2026-09-16'
name: Numverify API
nav: Providers
network: true
overview: 'Numverify API is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Phone Validation, Phone Numbers, Telecommunications, Data, and Validation.


  Numverify API''s developer surface includes documentation, pricing, signup flow, engineering blog, and 9 more developer resources.'
plans:
- name: Numverify Plans Pricing
  plan_count: 5
  slug: numverify-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 4
  name: Numverify Rate Limits
  slug: numverify-rate-limits
score:
  band: thin
  composite: 33.3
  coverage:
    artifact_dirs: 16
    catalog_earned: 61.0
    catalog_earned_first_party: 24.0
    catalog_gap: 54.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 76.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 73.2
    operational_transparency: 50.0
  previous_composite: 33.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/numverify/numverify-2026-06-20T190524.png
security:
- kind: authentication
  name: Numverify Authentication
  slug: numverify-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Numverify Domain Security
  slug: numverify-domain-security
  summary_line: TLSv1.3 · DMARC
slug: numverify
tags:
- Phone Validation
- Phone Numbers
- Telecommunications
- Data
- Validation
- Carrier Lookup
- Phone Number Lookup
website: https://numverify.com
---
