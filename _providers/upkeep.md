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
- acting_count: 27
  human_in_the_loop: 0
  name: Upkeep Agentic Access
  operation_count: 44
  slug: upkeep-agentic-access
  summary_line: 44 operations · 27 acting
api_count: 10
apis:
- description: Asset lifecycle and downtime management
  name: UpKeep Assets API
  slug: upkeep-assets-api
- description: Session token management
  name: UpKeep Authentication API
  slug: upkeep-authentication-api
- description: Location hierarchy management
  name: UpKeep Locations API
  slug: upkeep-locations-api
- description: Meter and reading management
  name: UpKeep Meters API
  slug: upkeep-meters-api
- description: Parts and inventory management
  name: UpKeep Parts API
  slug: upkeep-parts-api
- description: Preventive maintenance schedules and triggers
  name: UpKeep Preventive Maintenance API
  slug: upkeep-preventive-maintenance-api
- description: Purchase order management
  name: UpKeep Purchase Orders API
  slug: upkeep-purchase-orders-api
- description: Maintenance request management
  name: UpKeep Requests API
  slug: upkeep-requests-api
- description: Webhook event subscription management
  name: UpKeep Webhooks API
  slug: upkeep-webhooks-api
- description: Work order creation and management
  name: UpKeep Work Orders API
  slug: upkeep-work-orders-api
artifact_total: 26
collections:
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
random_paper: 76
rate_limits:
- limit_count: 5
  name: Upkeep Rate Limits
  slug: upkeep-rate-limits
rules:
- name: UpKeep API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: upkeep-jsonschema-spectral-rules
- name: UpKeep API Rules
  rule_count: 7
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 5
  slug: upkeep-rules
score:
  band: developing
  composite: 50.4
  delta: -5.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 69.5
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 36.8
  previous_composite: 55.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
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
