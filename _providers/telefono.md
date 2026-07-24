---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
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
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Telefono Agentic Access
  operation_count: 4
  slug: telefono-agentic-access
  summary_line: 4 operations · 1 acting
api_count: 4
apis:
- description: Batch validation for multiple numbers
  name: Telefono Batch API
  slug: telefono-batch-api
- description: Carrier lookup endpoints
  name: Telefono Carrier API
  slug: telefono-carrier-api
- description: Number formatting and parsing endpoints
  name: Telefono Format API
  slug: telefono-format-api
- description: Phone number validation endpoints
  name: Telefono Validation API
  slug: telefono-validation-api
artifact_total: 19
collections:
- collection_type: open
  name: Telefono Carrier Lookup API
  slug: open-telefono-carrier
- collection_type: open
  name: Telefono Number Formatting API
  slug: open-telefono-format
- collection_type: open
  name: Telefono Phone Validation API
  slug: open-telefono-validation
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/telefono-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/telefono-authentication.yml
- group: auth
  title: ''
  type: Authentication
  url: https://developers.telefono.com/authentication
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.telefono.com/getting-started
- group: operate
  title: ''
  type: RateLimits
  url: https://developers.telefono.com/rate-limits
- group: start
  title: ''
  type: Signup
  url: https://www.telefono.com/signup
- group: commercial
  title: ''
  type: Pricing
  url: https://www.telefono.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.telefono.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.telefono.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.telefono.com
- group: operate
  title: ''
  type: Support
  url: https://www.telefono.com/support
- group: build
  title: ''
  type: GitHub
  url: https://github.com/telefono-api
created: '2024-01-15'
description: Telefono is a phone number intelligence and validation API platform providing real-time phone number lookup, validation, carrier information, line type detection, and number formatting services for developers. The platform helps businesses verify user phone numbers, detect fraud, improve deliverability of SMS campaigns, and enrich contact data with carrier and geographic information.
examples:
- key_count: 2
  name: Telefono Carrier Lookup Example
  slug: telefono-carrier-lookup-example
- key_count: 2
  name: Telefono Validate Number Example
  slug: telefono-validate-number-example
finops:
- name: Telefono Finops
  service_category: Number Intelligence
  slug: telefono-finops
image: https://www.telefono.com/logo.png
json_schemas:
- name: Telefono Validation Result
  property_count: 14
  slug: telefono-validation-result
json_structures:
- name: Telefono Validation Result Structure
  property_count: 0
  slug: telefono-validation-result-structure
jsonld:
- class_count: 4
  name: Telefono Context
  property_count: 18
  slug: telefono-context
layout: provider
modified: '2026-05-19'
name: Telefono
nav: Providers
network: true
overview: 'Telefono publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Batch API, Carrier API, Format API, and 1 more. Tagged areas include Carrier Lookup, Data Enrichment, Fraud Prevention, Number Intelligence, and Number Verification.


  The Telefono catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Telefono''s developer surface includes authentication, getting-started guide, signup flow, pricing, support, GitHub presence, and 6 more developer resources.'
plans:
- name: Telefono Plans Pricing
  plan_count: 1
  slug: telefono-plans-pricing
random_paper: 44
rate_limits:
- limit_count: 1
  name: Telefono Rate Limits
  slug: telefono-rate-limits
rules:
- name: Telefono API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: telefono-jsonschema-spectral-rules
- name: Telefono API Rules
  rule_count: 11
  severity_counts:
    error: 5
    hint: 0
    info: 2
    warn: 4
  slug: telefono-rules
score:
  band: developing
  composite: 54.5
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 64.6
    developer_ergonomics: 26.1
    discoverability: 67.5
    governance: 73.7
    operational_transparency: 42.1
  previous_composite: 54.5
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/telefono/refs/heads/main/screenshots/telefono-2026-06-20T195031.png
security:
- kind: authentication
  name: Telefono Authentication
  slug: telefono-authentication
  summary_line: apiKey · 1 scheme
slug: telefono
tags:
- Carrier Lookup
- Data Enrichment
- Fraud Prevention
- Number Intelligence
- Number Verification
- Phone Lookup
- Phone Validation
- Telecommunications
website: https://www.telefono.com
---
