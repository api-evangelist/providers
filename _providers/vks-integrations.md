---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
    agentic_access: false
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
  score: 18.0
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: Access work instruction guidebooks and step-level content
  name: VKS Integrations Guidebooks API
  slug: vks-integrations-guidebooks-api
- description: Manage and track operational steps and production data
  name: VKS Integrations Operations API
  slug: vks-integrations-operations-api
- description: Retrieve production metrics, quality data, and traceability records
  name: VKS Integrations Production Data API
  slug: vks-integrations-production-data-api
- description: Create, retrieve, and manage work orders on the manufacturing floor
  name: VKS Integrations Work Orders API
  slug: vks-integrations-work-orders-api
artifact_total: 19
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: VKS Guidebooks API
  slug: open-vks-integrations-guidebooks-api
- collection_type: open
  name: VKS Operations API
  slug: open-vks-integrations-operations-api
- collection_type: open
  name: VKS Production Data API
  slug: open-vks-integrations-production-data-api
- collection_type: open
  name: VKS Work Orders API
  slug: open-vks-integrations-work-orders-api
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vks-integrations-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/vks---visual-knowledge-share
- group: company
  title: ''
  type: Website
  url: https://vksapp.com/
- group: docs
  title: ''
  type: Documentation
  url: https://help.vksapp.com/
- group: docs
  title: ''
  type: Reference
  url: https://help.vksapp.com/Content/VKS_Features/API/APIInfo.htm
- group: company
  title: ''
  type: Blog Post
  url: https://vksapp.com/blog/api-capabilities
- group: commercial
  title: ''
  type: Pricing
  url: https://vksapp.com/products/enterprise
created: '2025-03-01'
description: VKS (Visual Knowledge Share) provides work instruction software for manufacturing with a JSON REST API for pulling guidebook and production information and managing work orders and operations. VKS integrates with ERP, MES, QMS, and LMS platforms to enable bi-directional data exchange, real-time quality tracking, and automated work order management across the manufacturing floor.
examples:
- key_count: 5
  name: Vks Api Create Work Order Example
  slug: vks-api-create-work-order-example
finops:
- name: Vks Integrations Finops
  service_category: API
  slug: vks-integrations-finops
image: https://vksapp.com/hubfs/vks-logo.png
json_schemas:
- name: VKS Work Order
  property_count: 13
  slug: vks-work-order
json_structures:
- name: Vks Work Order Structure
  property_count: 0
  slug: vks-work-order-structure
jsonld:
- class_count: 8
  name: Vks Integrations Context
  property_count: 22
  slug: vks-integrations-context
layout: provider
modified: '2026-05-03'
name: VKS Integrations
nav: Providers
network: true
overview: 'VKS Integrations publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Guidebooks API, Operations API, Production Data API, and 1 more. Tagged areas include ERP Integration, Manufacturing, MES, Operations Management, and Quality Management.


  The VKS Integrations catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  VKS Integrations'' developer surface includes documentation, pricing, and 5 more developer resources.'
plans:
- name: Vks Integrations Plans Pricing
  plan_count: 3
  slug: vks-integrations-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 5
  name: Vks Integrations Rate Limits
  slug: vks-integrations-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: VKS Integrations API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: vks-integrations-jsonschema-spectral-rules
- effective_rule_count: 49
  extends:
  - spectral:oas
  name: VKS Integrations API Rules
  rule_count: 8
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 6
  slug: vks-integrations-rules
score:
  band: thin
  composite: 34.9
  coverage:
    artifact_dirs: 14
    catalog_gap: 58.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.5
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 13.6
    contract_quality: 61.2
    developer_ergonomics: 28.6
    discoverability: 59.3
    governance: 13.6
    operational_transparency: 7.9
  previous_composite: 35.4
  provenance:
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/vks-integrations/refs/heads/main/screenshots/vks-integrations-2026-06-20T201113.png
security:
- kind: domain-security
  name: Vks Integrations Domain Security
  slug: vks-integrations-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: vks-integrations
tags:
- ERP Integration
- Manufacturing
- MES
- Operations Management
- Quality Management
- Work Instructions
- Work Orders
website: https://vksapp.com/
---
