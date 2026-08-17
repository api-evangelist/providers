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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 10
  human_in_the_loop: 1
  name: Utilityapi Agentic Access
  operation_count: 27
  slug: utilityapi-agentic-access
  summary_line: 27 operations · 10 acting · 1 human-in-the-loop
api_count: 9
apis:
- description: Customer billing accounts and billing summaries
  name: UtilityAPI Accounting API
  slug: utilityapi-accounting-api
- description: Submitted authorizations from utility customers
  name: UtilityAPI Authorizations API
  slug: utilityapi-authorizations-api
- description: Utility billing information
  name: UtilityAPI Bills API
  slug: utilityapi-bills-api
- description: Webhook events and notifications
  name: UtilityAPI Events API
  slug: utilityapi-events-api
- description: Raw or formatted data files linked to other objects
  name: UtilityAPI Files API
  slug: utilityapi-files-api
- description: Customer-facing authorization forms management
  name: UtilityAPI Forms API
  slug: utilityapi-forms-api
- description: Meter usage intervals
  name: UtilityAPI Intervals API
  slug: utilityapi-intervals-api
- description: Utility services and meter data for authorized customers
  name: UtilityAPI Meters API
  slug: utilityapi-meters-api
- description: Authorization form templates for formatting customer authorization forms
  name: UtilityAPI Templates API
  slug: utilityapi-templates-api
artifact_total: 36
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Utility Accounting API
  slug: open-utilityapi-accounting-api
- collection_type: open
  name: Utility Accounting Authorizations API
  slug: open-utilityapi-authorizations-api
- collection_type: open
  name: Utility Accounting Bills API
  slug: open-utilityapi-bills-api
- collection_type: open
  name: Utility Accounting Events API
  slug: open-utilityapi-events-api
- collection_type: open
  name: Utility Accounting Files API
  slug: open-utilityapi-files-api
- collection_type: open
  name: Utility Accounting Forms API
  slug: open-utilityapi-forms-api
- collection_type: open
  name: Utility Accounting Intervals API
  slug: open-utilityapi-intervals-api
- collection_type: open
  name: Utility Accounting Meters API
  slug: open-utilityapi-meters-api
- collection_type: open
  name: Utility Accounting Templates API
  slug: open-utilityapi-templates-api
- collection_type: open
  name: UtilityAPI
  slug: open-utilityapi
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/utilityapi-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/utilityapi-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/utilityapi-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/utilityapi
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/utilityapi
- group: company
  title: ''
  type: Website
  url: https://utilityapi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://utilityapi.com/docs
- group: start
  title: ''
  type: Signup
  url: https://utilityapi.com/register
- group: commercial
  title: ''
  type: Pricing
  url: https://utilityapi.com/pricing
- group: docs
  title: ''
  type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/utilityapi/refs/heads/main/openapi/utilityapi-openapi.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/utilityapi/refs/heads/main/vocabulary/utilityapi-vocabulary.yml
- group: company
  title: ''
  type: Blog
  url: https://utilityapi.com/blog
created: '2025-05-02'
description: UtilityAPI collects, standardizes, and shares utility data seamlessly and securely, providing a platform for accessing energy and utility billing data, meter intervals, and authorization workflows for energy companies, cleantech firms, and developers.
examples:
- key_count: 2
  name: Utilityapi List Bills Example
  slug: utilityapi-list-bills-example
- key_count: 2
  name: Utilityapi List Intervals Example
  slug: utilityapi-list-intervals-example
- key_count: 2
  name: Utilityapi List Meters Example
  slug: utilityapi-list-meters-example
finops:
- name: Utilityapi Finops
  service_category: API
  slug: utilityapi-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/utilityapi.png
json_schemas:
- name: Bill
  property_count: 8
  slug: utilityapi-bill
- name: Interval
  property_count: 6
  slug: utilityapi-interval
- name: Meter
  property_count: 9
  slug: utilityapi-meter
json_structures:
- name: Utilityapi Meter Structure
  property_count: 0
  slug: utilityapi-meter-structure
jsonld:
- class_count: 18
  name: Utilityapi Context
  property_count: 2
  slug: utilityapi-context
layout: provider
modified: '2026-05-19'
name: UtilityAPI
nav: Providers
network: true
overview: 'UtilityAPI publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Accounting API, Authorizations API, Bills API, and 6 more. Tagged areas include Energy, Utilities, Green Button, Billing Data, and Meter Data.


  The UtilityAPI catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  UtilityAPI''s developer surface includes authentication, documentation, signup flow, pricing, engineering blog, and 7 more developer resources.'
plans:
- name: Utilityapi Plans Pricing
  plan_count: 3
  slug: utilityapi-plans-pricing
random_paper: 59
rate_limits:
- limit_count: 5
  name: Utilityapi Rate Limits
  slug: utilityapi-rate-limits
rules:
- name: UtilityAPI API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: utilityapi-jsonschema-spectral-rules
- name: UtilityAPI API Rules
  rule_count: 8
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 6
  slug: utilityapi-rules
score:
  band: developing
  composite: 44.8
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 76.1
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 13.2
  previous_composite: 44.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 23.0
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/utilityapi/refs/heads/main/screenshots/utilityapi-2026-06-20T200729.png
security:
- kind: authentication
  name: Utilityapi Authentication
  slug: utilityapi-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Utilityapi Domain Security
  slug: utilityapi-domain-security
  summary_line: TLSv1.3 · DMARC
slug: utilityapi
tags:
- Energy
- Utilities
- Green Button
- Billing Data
- Meter Data
- Clean Energy
website: https://utilityapi.com/
---
