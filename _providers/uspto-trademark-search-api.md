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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.7
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Uspto Trademark Search Api Agentic Access
  operation_count: 5
  slug: uspto-trademark-search-api-agentic-access
  summary_line: 5 operations
api_count: 1
apis:
- baseURL: https://uspto-trademark.p.rapidapi.com
  baseurl_source: declared
  description: Database freshness and update information
  name: USPTO Trademark Search API Database Status API
  slug: uspto-trademark-search-api-database-status-api
- baseURL: https://uspto-trademark.p.rapidapi.com
  baseurl_source: declared
  description: Search trademarks by owner name
  name: USPTO Trademark Search API Owner Search API
  slug: uspto-trademark-search-api-owner-search-api
- baseURL: https://uspto-trademark.p.rapidapi.com
  baseurl_source: declared
  description: Check if a trademark is available for registration
  name: USPTO Trademark Search API Trademark Availability API
  slug: uspto-trademark-search-api-trademark-availability-api
- baseURL: https://uspto-trademark.p.rapidapi.com
  baseurl_source: declared
  description: Retrieve trademark details by serial number
  name: USPTO Trademark Search API Trademark Lookup API
  slug: uspto-trademark-search-api-trademark-lookup-api
- baseURL: https://uspto-trademark.p.rapidapi.com
  baseurl_source: declared
  description: Search trademarks by keyword or phrase
  name: USPTO Trademark Search API Trademark Search API
  slug: uspto-trademark-search-api-trademark-search-api
artifact_total: 32
collections:
- collection_type: postman
  name: USPTO Trademark Search Database Status API
  slug: postman-uspto-trademark-search-api-database-status-api
- collection_type: postman
  name: USPTO Trademark Search Database Status Owner Search API
  slug: postman-uspto-trademark-search-api-owner-search-api
- collection_type: postman
  name: USPTO Trademark Search Database Status Trademark Availability API
  slug: postman-uspto-trademark-search-api-trademark-availability-api
- collection_type: postman
  name: USPTO Trademark Search Database Status Trademark Lookup API
  slug: postman-uspto-trademark-search-api-trademark-lookup-api
- collection_type: postman
  name: USPTO Database Status Trademark Search API
  slug: postman-uspto-trademark-search-api-trademark-search-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: USPTO Trademark Search Database Status API
  slug: open-uspto-trademark-search-api-database-status-api
- collection_type: open
  name: USPTO Trademark Search Database Status Owner Search API
  slug: open-uspto-trademark-search-api-owner-search-api
- collection_type: open
  name: USPTO Trademark Search Database Status Trademark Availability API
  slug: open-uspto-trademark-search-api-trademark-availability-api
- collection_type: open
  name: USPTO Trademark Search Database Status Trademark Lookup API
  slug: open-uspto-trademark-search-api-trademark-lookup-api
- collection_type: open
  name: USPTO Database Status Trademark Search API
  slug: open-uspto-trademark-search-api-trademark-search-api
- collection_type: open
  name: USPTO Trademark Search API
  slug: open-uspto-trademark-search-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/uspto-trademark-search-api-capability-edges.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/uspto-trademark-search-api/overview
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


  USPTO Trademark Search API''s developer surface includes authentication, signup flow, documentation, pricing, FAQ, engineering blog, and 12 more developer resources.'
plans:
- name: Uspto Trademark Search Api Plans Pricing
  plan_count: 3
  slug: uspto-trademark-search-api-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 5
  name: Uspto Trademark Search Api Rate Limits
  slug: uspto-trademark-search-api-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: USPTO Trademark Search API API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: uspto-trademark-search-api-jsonschema-spectral-rules
- effective_rule_count: 60
  extends:
  - spectral:oas
  name: USPTO Trademark Search API API Rules
  rule_count: 19
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 10
  slug: uspto-trademark-search-api-rules
score:
  band: developing
  composite: 49.6
  coverage:
    artifact_dirs: 18
    catalog_gap: 42.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 28.8
    contract_quality: 70.3
    developer_ergonomics: 28.6
    discoverability: 68.5
    governance: 28.8
    operational_transparency: 26.3
  previous_composite: 49.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 38.9
  schema_version: 0.18.0
  scored_at: '2026-09-02'
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
