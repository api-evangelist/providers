---
access_model:
  confidence: medium
  label: Free · Open access
  onboarding: open
  pricing: free
  public: true
  source:
  - plans
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: State Dept Agentic Access
  operation_count: 10
  slug: state-dept-agentic-access
  summary_line: 10 operations
api_count: 3
apis:
- description: Detailed country-specific travel information covering transportation, entry requirements, local laws, health, safety, and embassy contacts
  name: State Department Country Information API
  slug: state-dept-country-information-api
- description: Passport acceptance facility locations across the United States, searchable by state, ZIP code, radius, or geographic coordinates
  name: State Department Passport Locations API
  slug: state-dept-passport-locations-api
- description: Current US Department of State travel advisories for countries worldwide, with alert levels ranging from 1 (Exercise Normal Precautions) to 4 (Do Not Travel)
  name: State Department Travel Advisories API
  slug: state-dept-travel-advisories-api
artifact_total: 15
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/state-dept-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/state-dept-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.state.gov/
- group: docs
  title: ''
  type: Documentation
  url: https://cadataapi.state.gov/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/USStateDept
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/statedept
- group: company
  title: ''
  type: Blog
  url: https://www.state.gov/blogs
- group: other
  title: ''
  type: X
  url: https://x.com/StateDept
- group: commercial
  title: ''
  type: Plans
  url: plans/state-dept-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/state-dept-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/state-dept-finops.yml
created: '2026-06-13'
description: The US Department of State provides public REST APIs for accessing consular affairs data including travel advisories by country and risk level, country travel information, passport acceptance facility locations, passport issuance statistics, and geopolitical reference data. The Consular Affairs Data API (cadataapi.state.gov) offers open, unauthenticated endpoints covering all countries with real-time travel advisory updates across four alert levels. Additional historical diplomatic records are available through the Foreign Relations of the United States (FRUS) catalog API.
examples:
- key_count: 10
  name: Country Travel Information Example
  slug: country-travel-information-example
- key_count: 9
  name: Travel Advisory Example
  slug: travel-advisory-example
finops:
- name: State Dept Finops
  service_category: ''
  slug: state-dept-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/state-dept.png
json_schemas:
- name: CountryTravelInformation
  property_count: 10
  slug: country-travel-information
- name: PassportLocation
  property_count: 13
  slug: passport-location
- name: TravelAdvisory
  property_count: 9
  slug: travel-advisory
jsonld:
- class_count: 3
  name: State Dept Context
  property_count: 32
  slug: state-dept-context
layout: provider
modified: '2026-06-13'
name: State Department
nav: Providers
network: true
overview: 'State Department publishes 3 APIs on the [APIs.io](https://apis.io/) network: Country Information API, Passport Locations API, and Travel Advisories API. Tagged areas include US Government, Travel, Passports, Visas, and Travel Advisories.


  The State Department catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  State Department''s developer surface includes documentation, engineering blog, and 9 more developer resources.'
plans:
- name: State Dept Plans Pricing
  plan_count: 1
  slug: state-dept-plans-pricing
random_paper: 59
rate_limits:
- limit_count: 1
  name: State Dept Rate Limits
  slug: state-dept-rate-limits
rules:
- name: State Department API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: state-dept-jsonschema-spectral-rules
score:
  band: thin
  composite: 40.5
  delta: -4.5
  facets:
    commercial_clarity: 28.9
    contract_quality: 59.0
    developer_ergonomics: 10.9
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 26.3
  previous_composite: 45.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/state-dept/refs/heads/main/screenshots/state-dept-2026-06-20T194519.png
security:
- kind: domain-security
  name: State Dept Domain Security
  slug: state-dept-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: state-dept
tags:
- US Government
- Travel
- Passports
- Visas
- Travel Advisories
- Consular Affairs
- Foreign Policy
- Diplomatic
- Country Information
- Public Safety
website: https://www.state.gov/
---
