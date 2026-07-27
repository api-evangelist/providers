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
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Uspto Trademark Search Api Agentic Access
  operation_count: 5
  slug: uspto-trademark-search-api-agentic-access
  summary_line: 5 operations
api_count: 5
apis:
- description: Database freshness and update information
  name: USPTO Trademark Search API Database Status API
  slug: uspto-trademark-search-api-database-status-api
- description: Search trademarks by owner name
  name: USPTO Trademark Search API Owner Search API
  slug: uspto-trademark-search-api-owner-search-api
- description: Check if a trademark is available for registration
  name: USPTO Trademark Search API Trademark Availability API
  slug: uspto-trademark-search-api-trademark-availability-api
- description: Retrieve trademark details by serial number
  name: USPTO Trademark Search API Trademark Lookup API
  slug: uspto-trademark-search-api-trademark-lookup-api
- description: Search trademarks by keyword or phrase
  name: USPTO Trademark Search API Trademark Search API
  slug: uspto-trademark-search-api-trademark-search-api
artifact_total: 21
collections:
- collection_type: open
  name: USPTO Trademark Search API
  slug: open-uspto-trademark-search-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/uspto-trademark-search-api-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/uspto-trademark-search-api-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/uspto-trademark-search-api-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/USPTO
- group: start
  title: ''
  type: Signup
  url: https://rapidapi.com/pentium10/api/uspto-trademark/
- group: start
  title: ''
  type: Login
  url: https://rapidapi.com/developer/dashboard
- group: docs
  title: ''
  type: Documentation
  url: https://rapidapi.com/pentium10/api/uspto-trademark
- group: commercial
  title: ''
  type: Pricing
  url: https://rapidapi.com/pentium10/api/uspto-trademark/pricing
- group: operate
  title: ''
  type: FAQ
  url: https://rapidapi.com/pentium10/api/uspto-trademark/tutorials/faq-
- group: company
  title: ''
  type: Blog
  url: https://medium.com/p/71274363605b
- group: company
  title: ''
  type: Blog
  url: https://medium.com/p/19efc7e1cc6
- group: commercial
  title: ''
  type: TermsOfService
  url: https://rapidapi.com/terms/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/martonkodok
- group: design
  title: ''
  type: SpectralRules
  url: rules/uspto-trademark-search-api-rules.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/uspto-trademark-search-api-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/uspto-trademark-search-api-vocabulary.yml
created: '2025-05-27'
description: Instant trademark search and brand protection via the USPTO Trademark Search API. Check if a trademark keyword is available, search active trademarks, look up marks by serial number, and search by owner from United States Patent and Trademark Office data. Updated daily. Enables trademark availability checking, portfolio research, competitive intelligence, and due diligence workflows.
examples:
- key_count: 2
  name: Uspto Trademark Search Api Checktrademarkavailability Example
  slug: uspto-trademark-search-api-checkTrademarkAvailability-example
- key_count: 2
  name: Uspto Trademark Search Api Getdatabasestatus Example
  slug: uspto-trademark-search-api-getDatabaseStatus-example
- key_count: 2
  name: Uspto Trademark Search Api Gettrademarkbyserialnumber Example
  slug: uspto-trademark-search-api-getTrademarkBySerialNumber-example
- key_count: 2
  name: Uspto Trademark Search Api Searchtrademarks Example
  slug: uspto-trademark-search-api-searchTrademarks-example
finops:
- name: Uspto Trademark Search Api Finops
  service_category: API
  slug: uspto-trademark-search-api-finops
image: https://rapidapi.com/hub/_next/image?url=https%3A%2F%2Frapidapi-prod-apis.s3.amazonaws.com%2F9440240c-7bf2-4af0-8232-375b0bb7327f_medium&w=1920&q=75
json_schemas:
- name: USPTO Trademark
  property_count: 20
  slug: uspto-trademark-search-api-trademark
json_structures:
- name: Uspto Trademark Search Api Trademark Structure
  property_count: 0
  slug: uspto-trademark-search-api-trademark-structure
jsonld:
- class_count: 13
  name: Uspto Trademark Search Api Context
  property_count: 25
  slug: uspto-trademark-search-api-context
layout: provider
modified: '2026-05-19'
name: USPTO Trademark Search API
nav: Providers
network: true
overview: 'USPTO Trademark Search API publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Database Status API, Owner Search API, Trademark Availability API, and 2 more. Tagged areas include Brand, Brand Protection, Business, Data, and Government Data.


  The USPTO Trademark Search API catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  USPTO Trademark Search API''s developer surface includes authentication, signup flow, documentation, pricing, FAQ, engineering blog, and 10 more developer resources.'
plans:
- name: Uspto Trademark Search Api Plans Pricing
  plan_count: 3
  slug: uspto-trademark-search-api-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 5
  name: Uspto Trademark Search Api Rate Limits
  slug: uspto-trademark-search-api-rate-limits
rules:
- name: USPTO Trademark Search API API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: uspto-trademark-search-api-jsonschema-spectral-rules
- name: USPTO Trademark Search API API Rules
  rule_count: 19
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 10
  slug: uspto-trademark-search-api-rules
score:
  band: strong
  composite: 63.6
  delta: 4.6
  facets:
    commercial_clarity: 73.7
    contract_quality: 77.3
    developer_ergonomics: 21.7
    discoverability: 100.0
    governance: 86.8
    operational_transparency: 36.8
  previous_composite: 59.0
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/uspto-trademark-search-api/refs/heads/main/screenshots/uspto-trademark-search-api-2026-06-20T200727.png
security:
- kind: authentication
  name: Uspto Trademark Search Api Authentication
  slug: uspto-trademark-search-api-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Uspto Trademark Search Api Domain Security
  slug: uspto-trademark-search-api-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: uspto-trademark-search-api
tags:
- Brand
- Brand Protection
- Business
- Data
- Government Data
- Intellectual Property
- Legal
- Search
- Trademark
- USPTO
---
