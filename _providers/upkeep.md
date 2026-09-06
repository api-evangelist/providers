---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 27
  human_in_the_loop: 0
  name: Upkeep Agentic Access
  operation_count: 44
  slug: upkeep-agentic-access
  summary_line: 44 operations · 27 acting
api_count: 1
apis:
- baseURL: https://api.onupkeep.com/api/v2
  baseurl_source: declared
  description: Asset lifecycle and downtime management
  name: UpKeep Assets API
  slug: upkeep-assets-api
- baseURL: https://api.onupkeep.com/api/v2
  baseurl_source: declared
  description: Session token management
  name: UpKeep Authentication API
  slug: upkeep-authentication-api
- baseURL: https://api.onupkeep.com/api/v2
  baseurl_source: declared
  description: Location hierarchy management
  name: UpKeep Locations API
  slug: upkeep-locations-api
- baseURL: https://api.onupkeep.com/api/v2
  baseurl_source: declared
  description: Meter and reading management
  name: UpKeep Meters API
  slug: upkeep-meters-api
- baseURL: https://api.onupkeep.com/api/v2
  baseurl_source: declared
  description: Parts and inventory management
  name: UpKeep Parts API
  slug: upkeep-parts-api
- baseURL: https://api.onupkeep.com/api/v2
  baseurl_source: declared
  description: Preventive maintenance schedules and triggers
  name: UpKeep Preventive Maintenance API
  slug: upkeep-preventive-maintenance-api
- baseURL: https://api.onupkeep.com/api/v2
  baseurl_source: declared
  description: Purchase order management
  name: UpKeep Purchase Orders API
  slug: upkeep-purchase-orders-api
- baseURL: https://api.onupkeep.com/api/v2
  baseurl_source: declared
  description: Maintenance request management
  name: UpKeep Requests API
  slug: upkeep-requests-api
- baseURL: https://api.onupkeep.com/api/v2
  baseurl_source: declared
  description: Webhook event subscription management
  name: UpKeep Webhooks API
  slug: upkeep-webhooks-api
- baseURL: https://api.onupkeep.com/api/v2
  baseurl_source: declared
  description: Work order creation and management
  name: UpKeep Work Orders API
  slug: upkeep-work-orders-api
artifact_total: 37
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: UpKeep Assets API
  slug: open-upkeep-assets-api
- collection_type: open
  name: UpKeep Assets Authentication API
  slug: open-upkeep-authentication-api
- collection_type: open
  name: UpKeep Assets Locations API
  slug: open-upkeep-locations-api
- collection_type: open
  name: UpKeep Assets Meters API
  slug: open-upkeep-meters-api
- collection_type: open
  name: UpKeep Assets Parts API
  slug: open-upkeep-parts-api
- collection_type: open
  name: UpKeep Assets Preventive Maintenance API
  slug: open-upkeep-preventive-maintenance-api
- collection_type: open
  name: UpKeep Assets Purchase Orders API
  slug: open-upkeep-purchase-orders-api
- collection_type: open
  name: UpKeep Assets Requests API
  slug: open-upkeep-requests-api
- collection_type: open
  name: UpKeep Assets Webhooks API
  slug: open-upkeep-webhooks-api
- collection_type: open
  name: UpKeep Assets Work Orders API
  slug: open-upkeep-work-orders-api
- collection_type: open
  name: UpKeep API
  slug: open-upkeep
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/upkeep-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/upkeep-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/upkeep-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/upkeep-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://upkeep.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/upkeepapp
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/on-upkeep
- group: company
  title: ''
  type: Website
  url: https://upkeep.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.onupkeep.com/
- group: build
  title: ''
  type: REST API Integration
  url: https://upkeep.com/integrations/rest-api/
- group: agent
  title: ''
  type: LlmsText
  url: https://upkeep.com/llms.txt
created: '2025-02-12'
description: UpKeep is an asset operations management and CMMS (Computerized Maintenance Management System) platform for maintenance teams and facility managers. The UpKeep API provides programmatic access to work orders, assets, locations, preventive maintenance schedules, parts inventory, purchase orders, meters, requests, and webhooks.
examples:
- key_count: 2
  name: Upkeep Create Work Order Example
  slug: upkeep-create-work-order-example
- key_count: 2
  name: Upkeep List Assets Example
  slug: upkeep-list-assets-example
finops:
- name: Upkeep Finops
  service_category: API
  slug: upkeep-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/upkeep.png
json_schemas:
- name: UpKeep Asset
  property_count: 12
  slug: upkeep-asset
- name: UpKeep Work Order
  property_count: 15
  slug: upkeep-work-order
json_structures:
- name: Upkeep Work Order Structure
  property_count: 0
  slug: upkeep-work-order-structure
jsonld:
- class_count: 5
  name: Upkeep Context
  property_count: 24
  slug: upkeep-context
layout: provider
modified: '2026-05-19'
name: UpKeep
nav: Providers
network: true
overview: 'UpKeep publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Assets API, Authentication API, Locations API, and 7 more. Tagged areas include CMMS, Maintenance Management, Asset Management, Facility Management, and Work Orders.


  The UpKeep catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  UpKeep''s developer surface includes authentication, engineering blog, documentation, and 8 more developer resources.'
plans:
- name: Upkeep Plans Pricing
  plan_count: 3
  slug: upkeep-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 5
  name: Upkeep Rate Limits
  slug: upkeep-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: UpKeep API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: upkeep-jsonschema-spectral-rules
- effective_rule_count: 48
  extends:
  - spectral:oas
  name: UpKeep API Rules
  rule_count: 7
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 5
  slug: upkeep-rules
score:
  band: thin
  composite: 36.9
  coverage:
    artifact_dirs: 17
    catalog_earned: 61.5
    catalog_earned_first_party: 0.0
    catalog_gap: 53.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 13.6
    contract_quality: 67.1
    developer_ergonomics: 23.8
    discoverability: 75.9
    governance: 13.6
    operational_transparency: 10.5
  previous_composite: 36.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/upkeep/refs/heads/main/screenshots/upkeep-2026-06-20T200501.png
security:
- kind: authentication
  name: Upkeep Authentication
  slug: upkeep-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Upkeep Domain Security
  slug: upkeep-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: trust-center
  name: Upkeep Trust Center
  slug: upkeep-trust-center
  summary_line: SOC 2, GDPR
slug: upkeep
tags:
- CMMS
- Maintenance Management
- Asset Management
- Facility Management
- Work Orders
website: https://upkeep.com
---
