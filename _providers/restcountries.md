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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Restcountries Agentic Access
  operation_count: 4
  slug: restcountries-agentic-access
  summary_line: 4 operations
api_count: 1
apis:
- description: Country lookup and search endpoints
  name: REST Countries Countries API
  slug: restcountries-countries-api
artifact_total: 17
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/restcountries-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/restcountries-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/restcountries-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://restcountries.com
- group: docs
  title: ''
  type: Documentation
  url: https://restcountries.com/docs
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/apilayer/restcountries
- group: commercial
  title: ''
  type: Pricing
  url: https://restcountries.com/plans
- group: operate
  title: ''
  type: StatusPage
  url: https://status.restcountries.com
- group: commercial
  title: ''
  type: Plans
  url: plans/restcountries-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/restcountries-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/restcountries-finops.yml
created: '2026-06-13'
description: Free REST API providing comprehensive data about world countries including name, capital, currencies, languages, flags, population, and geographic information. Covers 250+ countries and dependencies with 80+ fields per country, updated from 35+ authoritative sources.
examples:
- key_count: 1
  name: Error 401 Unauthorized
  slug: error-401-unauthorized
- key_count: 1
  name: List All Countries Response
  slug: list-all-countries-response
- key_count: 1
  name: Lookup By Alpha2 Code Response
  slug: lookup-by-alpha2-code-response
- key_count: 1
  name: Search By Name Response
  slug: search-by-name-response
finops:
- name: Restcountries Finops
  service_category: ''
  slug: restcountries-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/restcountries.png
json_schemas:
- name: CountriesListResponse
  property_count: 1
  slug: countries-list-response
- name: Country
  property_count: 29
  slug: country
- name: ErrorResponse
  property_count: 1
  slug: error-response
jsonld:
- class_count: 0
  name: Restcountries Api Context
  property_count: 0
  slug: restcountries-api
- class_count: 2
  name: Restcountries Context
  property_count: 64
  slug: restcountries-context
layout: provider
modified: '2026-06-13'
name: REST Countries
nav: Providers
network: true
overview: 'REST Countries publishes 1 API on the [APIs.io](https://apis.io/) network: Countries API. Tagged areas include Countries, Geography, World Data, Flags, and Currencies.


  The REST Countries catalog on APIs.io includes 2 JSON-LD contexts and 1 Spectral governance ruleset.


  REST Countries'' developer surface includes authentication, documentation, pricing, and 8 more developer resources.'
plans:
- name: Restcountries Plans Pricing
  plan_count: 5
  slug: restcountries-plans-pricing
random_paper: 74
rate_limits:
- limit_count: 0
  name: Restcountries Rate Limits
  slug: restcountries-rate-limits
rules:
- name: REST Countries API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: restcountries-jsonschema-spectral-rules
score:
  band: developing
  composite: 49.8
  delta: -4.9
  facets:
    commercial_clarity: 50.0
    contract_quality: 77.1
    developer_ergonomics: 19.6
    discoverability: 68.5
    governance: 58.3
    operational_transparency: 21.1
  previous_composite: 54.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/restcountries/refs/heads/main/screenshots/restcountries-2026-06-20T193018.png
security:
- kind: authentication
  name: Restcountries Authentication
  slug: restcountries-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Restcountries Domain Security
  slug: restcountries-domain-security
  summary_line: TLSv1.3 · DMARC
slug: restcountries
tags:
- Countries
- Geography
- World Data
- Flags
- Currencies
- Languages
- Population
website: https://restcountries.com
---
