---
access_model:
  confidence: low
  label: Unknown · no verifiable provider surface
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Telefono Agentic Access
  operation_count: 4
  slug: telefono-agentic-access
  summary_line: 4 operations · 1 acting
api_count: 3
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
artifact_total: 24
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Telefono Carrier Lookup Batch API
  slug: open-telefono-batch-api
- collection_type: open
  name: Telefono Lookup Batch Carrier API
  slug: open-telefono-carrier-api
- collection_type: open
  name: Telefono Carrier Lookup API
  slug: open-telefono-carrier
- collection_type: open
  name: Telefono Carrier Lookup Batch Format API
  slug: open-telefono-format-api
- collection_type: open
  name: Telefono Number Formatting API
  slug: open-telefono-format
- collection_type: open
  name: Telefono Carrier Lookup Batch Validation API
  slug: open-telefono-validation-api
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
coverage:
  checked: '2026-08-14'
  detail: 'telefono.com is a parked domain: its root serves a 346-byte HTML frameset whose only frame points at the domain marketplace domainnames.net, every other path on the host returns 404, and api./developers./status./docs.telefono.com are all NXDOMAIN — including api.telefono.com, the host declared in the servers[] block of every OpenAPI in this repo and in every apis[].baseURL.'
  evidence:
  - status: 200
    url: https://www.telefono.com/
  - status: 404
    url: https://www.telefono.com/pricing
  - status: 404
    url: https://www.telefono.com/signup
  - status: 404
    url: https://www.telefono.com/terms
  - status: 404
    url: https://www.telefono.com/.well-known/agent-card.json
  - status: 404
    url: https://www.telefono.com/llms.txt
  - status: 0
    url: https://api.telefono.com/v1/validate
  - status: 0
    url: https://developers.telefono.com/validation
  - status: 0
    url: https://status.telefono.com
  - status: 404
    url: https://github.com/telefono-api
  reason: defunct
  state: none
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
random_paper: 20
rate_limits:
- limit_count: 1
  name: Telefono Rate Limits
  slug: telefono-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Telefono API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: telefono-jsonschema-spectral-rules
- effective_rule_count: 52
  extends:
  - spectral:oas
  name: Telefono API Rules
  rule_count: 11
  severity_counts:
    error: 5
    hint: 0
    info: 2
    warn: 4
  slug: telefono-rules
score:
  band: thin
  composite: 32.9
  coverage:
    artifact_dirs: 15
    catalog_gap: 55.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 13.6
    contract_quality: 57.1
    developer_ergonomics: 16.7
    discoverability: 81.5
    governance: 13.6
    operational_transparency: 18.4
  previous_composite: 32.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 15.3
  schema_version: 0.17.2
  scored_at: '2026-08-30'
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
