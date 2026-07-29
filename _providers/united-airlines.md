---
access_model:
  confidence: high
  label: Enterprise · Requires approval
  onboarding: approval
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
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
- acting_count: 6
  human_in_the_loop: 0
  name: United Airlines Agentic Access
  operation_count: 11
  slug: united-airlines-agentic-access
  summary_line: 11 operations · 6 acting
api_count: 5
apis:
- description: United Airlines Flight Status API providing real-time flight status including estimated and actual departure and arrival times, gate information, delays, and flight tracking for United-operated flight
  name: United Airlines Flight Status API
  slug: united-airlines-flight-status-api
- description: Flight booking and reservation management
  name: United Airlines Booking API
  slug: united-airlines-booking-api
- description: Post-booking modifications, refunds, and ancillaries
  name: United Airlines Servicing API
  slug: united-airlines-servicing-api
- description: Flight search and pricing operations
  name: United Airlines Shopping API
  slug: united-airlines-shopping-api
- description: Flight status and schedule information
  name: United Airlines Status API
  slug: united-airlines-status-api
artifact_total: 22
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/united-airlines-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/united-airlines-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/united-airlines-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/united-airlines-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.united.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://united.business/NDC-corporate
- group: other
  title: ''
  type: NDC Capabilities
  url: https://united.business/NDC-capabilities
- group: operate
  title: ''
  type: Contact
  url: https://united.business/contact-form.html
- group: start
  title: ''
  type: IATA Developer Portal
  url: https://api.developer.iata.org/united-airlines-united-airlines-default/api/flight-status2
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/united-airlines
- group: other
  title: ''
  type: X
  url: https://twitter.com/united
- group: other
  title: ''
  type: MileagePlus
  url: https://www.united.com/en/us/fly/mileageplus.html
- group: docs
  title: ''
  type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/united-airlines/main/openapi/united-airlines-ndc-openapi.yml
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/united-airlines/main/rules/united-airlines-rules.yml
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/united-airlines/main/json-schema/united-airlines-booking-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/united-airlines/main/json-schema/united-airlines-flight-status-schema.json
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/united-airlines/main/json-ld/united-airlines-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/united-airlines/main/vocabulary/united-airlines-vocabulary.yml
created: '2026-03-21'
description: United Airlines is a major American airline headquartered in Chicago, Illinois. It operates one of the largest route networks in the world with hubs in Chicago, Denver, Houston, Los Angeles, New York, San Francisco, and Washington, D.C. United provides NDC (New Distribution Capability) APIs for flight shopping, booking, and servicing, as well as corporate travel integration capabilities.
examples:
- key_count: 2
  name: United Airlines Createbooking Example
  slug: united-airlines-createBooking-example
- key_count: 2
  name: United Airlines Getflightstatus Example
  slug: united-airlines-getFlightStatus-example
- key_count: 2
  name: United Airlines Searchflightoffers Example
  slug: united-airlines-searchFlightOffers-example
finops:
- name: United Airlines Finops
  service_category: Travel
  slug: united-airlines-finops
graphqls:
- description: This GraphQL schema provides a conceptual representation of the United Airlines flight and travel API domain, covering the NDC (New Distribution Capability) API, Flight Status API, and MileagePlus loy
  name: United Airlines GraphQL Schema
  slug: united-airlines-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/united-airlines.png
json_schemas:
- name: United Airlines Booking
  property_count: 8
  slug: united-airlines-booking
- name: United Airlines Flight Status
  property_count: 14
  slug: united-airlines-flight-status
json_structures:
- name: United Airlines Booking Structure
  property_count: 0
  slug: united-airlines-booking-structure
jsonld:
- class_count: 0
  name: United Airlines Context
  property_count: 41
  slug: united-airlines-context
layout: provider
modified: '2026-05-19'
name: United Airlines
nav: Providers
network: true
overview: 'United Airlines publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Booking API, Servicing API, Shopping API, and 1 more. Tagged areas include Airlines, Travel, Flight Booking, NDC, and Loyalty.


  The United Airlines catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  United Airlines'' developer surface includes authentication and 17 more developer resources.'
plans:
- name: United Airlines Plans Pricing
  plan_count: 1
  slug: united-airlines-plans-pricing
random_paper: 48
rate_limits:
- limit_count: 1
  name: United Airlines Rate Limits
  slug: united-airlines-rate-limits
rules:
- name: United Airlines API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: united-airlines-jsonschema-spectral-rules
- name: United Airlines API Rules
  rule_count: 15
  severity_counts:
    error: 4
    hint: 0
    info: 2
    warn: 9
  slug: united-airlines-rules
scopes:
- name: United Airlines Scopes
  scope_count: 2
  slug: united-airlines-scopes
  summary_line: 2 scopes · clientCredentials
score:
  band: developing
  composite: 45.6
  delta: -4.1
  facets:
    commercial_clarity: 28.9
    contract_quality: 70.1
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 21.1
  previous_composite: 49.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/united-airlines/refs/heads/main/screenshots/united-airlines-2026-06-20T200049.png
security:
- kind: authentication
  name: United Airlines Authentication
  slug: united-airlines-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: United Airlines Domain Security
  slug: united-airlines-domain-security
  summary_line: TLSv1.3 · DMARC
slug: united-airlines
tags:
- Airlines
- Travel
- Flight Booking
- NDC
- Loyalty
- Fortune 100
website: https://www.united.com
---
