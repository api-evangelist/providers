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
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Easyship Agentic Access
  operation_count: 19
  slug: easyship-agentic-access
  summary_line: 19 operations · 11 acting
api_count: 1
apis:
- description: The Addresses API from Easyship — 2 operation(s) for addresses.
  name: Easyship Addresses API
  slug: easyship-addresses-api
- description: The Labels API from Easyship — 1 operation(s) for labels.
  name: Easyship Labels API
  slug: easyship-labels-api
- description: The Pickups API from Easyship — 1 operation(s) for pickups.
  name: Easyship Pickups API
  slug: easyship-pickups-api
- description: The Rates API from Easyship — 1 operation(s) for rates.
  name: Easyship Rates API
  slug: easyship-rates-api
- description: The Shipments API from Easyship — 3 operation(s) for shipments.
  name: Easyship Shipments API
  slug: easyship-shipments-api
- description: The Trackings API from Easyship — 2 operation(s) for trackings.
  name: Easyship Trackings API
  slug: easyship-trackings-api
- description: The Webhooks API from Easyship — 1 operation(s) for webhooks.
  name: Easyship Webhooks API
  slug: easyship-webhooks-api
artifact_total: 35
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Easyship Addresses API
  slug: open-easyship-addresses-api
- collection_type: open
  name: Easyship Addresses Labels API
  slug: open-easyship-labels-api
- collection_type: open
  name: Easyship Addresses Pickups API
  slug: open-easyship-pickups-api
- collection_type: open
  name: Easyship Addresses Rates API
  slug: open-easyship-rates-api
- collection_type: open
  name: Easyship Addresses Shipments API
  slug: open-easyship-shipments-api
- collection_type: open
  name: Easyship Addresses Trackings API
  slug: open-easyship-trackings-api
- collection_type: open
  name: Easyship Addresses Webhooks API
  slug: open-easyship-webhooks-api
- collection_type: open
  name: Easyship API
  slug: open-easyship
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/easyship-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/easyship-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/easyship-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/easyship-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/easyship-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/easyship
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/easyship
- group: company
  title: ''
  type: Website
  url: https://www.easyship.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.easyship.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.easyship.com/pricing
- group: start
  title: ''
  type: Signup
  url: https://app.easyship.com/login
- group: operate
  title: ''
  type: Support
  url: https://support.easyship.com/
- group: company
  title: ''
  type: Blog
  url: https://www.easyship.com/blog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.easyship.com/
- group: agent
  title: ''
  type: LlmsText
  url: https://developers.easyship.com/llms.txt
created: '2025-03-01'
description: Easyship is a comprehensive all-in-one shipping platform headquartered in Hong Kong that provides e-commerce businesses with a one-stop solution for their shipping needs. From comparing rates and services across 250+ couriers to managing orders, generating labels, scheduling pickups, calculating duties and taxes, and tracking shipments, Easyship streamlines cross-border and domestic logistics for businesses of all sizes. The Easyship REST API exposes the same shipping engine that powers the Easyship dashboard and platform integrations to developers building custom commerce, fulfillment, and logistics workflows.
examples:
- key_count: 4
  name: Easyship Create Label Example
  slug: easyship-create-label-example
- key_count: 4
  name: Easyship Get Rates Example
  slug: easyship-get-rates-example
finops:
- name: Easyship Finops
  service_category: API
  slug: easyship-finops
graphqls:
- description: This document describes a conceptual GraphQL schema for the Easyship multi-carrier shipping API. Easyship provides e-commerce businesses with access to 250+ couriers for rate comparison, label generat
  name: EasyShip GraphQL Schema
  slug: easyship-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/easyship.png
json_schemas:
- name: Easyship Label
  property_count: 10
  slug: easyship-label
- name: Easyship Rate
  property_count: 10
  slug: easyship-rate
- name: Easyship Shipment
  property_count: 8
  slug: easyship-shipment
- name: Easyship Tracking
  property_count: 7
  slug: easyship-tracking
- name: Easyship Webhook
  property_count: 6
  slug: easyship-webhook
json_structures:
- name: Easyship Structure
  property_count: 0
  slug: easyship-structure
jsonld:
- class_count: 37
  name: Easyship Context
  property_count: 22
  slug: easyship-context
layout: provider
modified: '2026-05-25'
name: Easyship
nav: Providers
network: true
overview: 'Easyship publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Addresses API, Labels API, Pickups API, and 4 more. Tagged areas include Shipping, Logistics, E-Commerce, Fulfillment, and Cross-Border.


  The Easyship catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Easyship''s developer surface includes authentication, pricing, signup flow, support, engineering blog, and 10 more developer resources.'
plans:
- name: Easyship Plans Pricing
  plan_count: 3
  slug: easyship-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 5
  name: Easyship Rate Limits
  slug: easyship-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Easyship API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: easyship-jsonschema-spectral-rules
- effective_rule_count: 55
  extends:
  - spectral:oas
  name: Easyship API Rules
  rule_count: 14
  severity_counts:
    error: 4
    hint: 0
    info: 3
    warn: 7
  slug: easyship-rules
score:
  band: developing
  composite: 46.7
  coverage:
    artifact_dirs: 19
    catalog_gap: 38.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 28.8
    contract_quality: 73.0
    developer_ergonomics: 35.7
    discoverability: 75.9
    governance: 28.8
    operational_transparency: 34.2
  previous_composite: 46.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/easyship/refs/heads/main/screenshots/easyship-2026-06-20T180405.png
security:
- kind: authentication
  name: Easyship Authentication
  slug: easyship-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Easyship Domain Security
  slug: easyship-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Easyship Vulnerability Disclosure
  slug: easyship-vulnerability-disclosure
  summary_line: security.txt
slug: easyship
tags:
- Shipping
- Logistics
- E-Commerce
- Fulfillment
- Cross-Border
website: https://www.easyship.com/
---
