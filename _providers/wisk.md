---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Wisk Agentic Access
  operation_count: 1
  slug: wisk-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- description: Push point-of-sale sales line items into a WISK venue account.
  name: WISK.ai Sales API
  slug: wisk-sales-api
artifact_total: 23
collections:
- collection_type: open
  name: WISK Public Sales Upload API
  slug: open-wisk-sales-upload
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/wisk-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wisk-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/wisk-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.wisk.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://help.wisk.ai/en/articles/5071983-integrating-with-wisk-for-pos-providers
- group: start
  title: ''
  type: Signup
  url: https://www.wisk.ai/demo
- group: start
  title: ''
  type: Login
  url: https://web.wisk.ai/signin
- group: commercial
  title: ''
  type: Pricing
  url: https://www.wisk.ai/price
- group: operate
  title: ''
  type: Support
  url: https://help.wisk.ai/en/
- group: company
  title: ''
  type: Blog
  url: https://www.wisk.ai/blog
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/wisk
- group: other
  title: ''
  type: X
  url: https://twitter.com/WISK_ai
- group: commercial
  title: ''
  type: Plans
  url: plans/wisk-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/wisk-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/wisk-finops.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/wisk-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/wisk-vocabulary.yaml
created: '2026-06-02'
description: 'WISK.ai is an inventory management and hospitality intelligence platform for bars, restaurants, and hotels, covering inventory counts, invoicing, purchasing, recipe costing, and cost-of-goods tracking. It syncs with 60+ POS systems to align sales with inventory. WISK''s integration surface is built for POS and data partners rather than a broad public developer program: partners can let WISK pull from their sales and product/menu APIs, or push daily sales data into WISK using its public sales-upload API, which is documented in a public Notion guide. New integrations begin by contacting the WISK integrations team, and email-based CSV/XLS feeds are supported as a fallback.'
examples:
- key_count: 6
  name: Sales Upload Sales Line Example
  slug: sales-upload-sales-line-example
features:
- description: Push point-of-sale sales lines into a WISK venue account via a single POST to /public/sales/upload accepting a JSON array of line items.
  name: Sales Upload API
- description: WISK can pull from a partner's own Sales API and Product/Menu API to ingest sales and item data into customer accounts.
  name: POS Pull Integrations
- description: For POS systems without an API, automated daily sales or product-mix reports can be emailed to WISK in XLS or CSV format.
  name: CSV/XLS Email Fallback
- description: Inventory counts, invoicing, purchasing, recipe costing, and cost-of-goods tracking across bars, restaurants, and hotels.
  name: Inventory and Cost Tracking
finops:
- name: Wisk Finops
  service_category: Hospitality Inventory Management
  slug: wisk-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/wisk.png
integrations:
- description: 60+ POS systems including Toast, Square, Clover, Lightspeed, Revel, TouchBistro, Heartland, Aldelo, Arryved, and many more.
  name: Direct POS Integrations
- description: Several POS systems integrate through Omnivore's Universal API, including Aloha, Brink, Oracle Hospitality (Micros/Simphony), POSitouch, and Doshii-connected systems.
  name: Omnivore Universal API
json_schemas:
- name: SalesLine
  property_count: 6
  slug: sales-upload-sales-line
json_structures:
- name: Sales Upload Sales Line Structure
  property_count: 6
  slug: sales-upload-sales-line-structure
jsonld:
- class_count: 1
  name: Wisk Sales Upload Context
  property_count: 6
  slug: wisk-sales-upload-context
layout: provider
modified: '2026-06-03'
name: WISK.ai
nav: Providers
network: true
overview: 'WISK.ai publishes 1 API on the [APIs.io](https://apis.io/) network: Sales API. Tagged areas include Restaurant, Bar, Inventory, Hospitality, and Sales.


  The WISK.ai catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  WISK.ai''s developer surface includes authentication, documentation, signup flow, pricing, support, engineering blog, and 11 more developer resources.'
plans:
- name: Wisk Plans Pricing
  plan_count: 6
  slug: wisk-plans-pricing
random_paper: 107
rate_limits:
- limit_count: 1
  name: Wisk Rate Limits
  slug: wisk-rate-limits
rules:
- name: WISK.ai API Rules
  rule_count: 4
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 3
  slug: wisk-jsonschema-spectral-rules
- name: WISK.ai API Rules
  rule_count: 29
  severity_counts:
    error: 7
    hint: 0
    info: 4
    warn: 18
  slug: wisk-spectral-rules
score:
  band: developing
  composite: 42.0
  delta: 0.0
  facets:
    commercial_clarity: 63.2
    contract_quality: 25.2
    developer_ergonomics: 26.1
    discoverability: 68.5
    governance: 68.8
    operational_transparency: 21.1
  previous_composite: 42.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/wisk/refs/heads/main/screenshots/wisk-2026-06-20T201524.png
security:
- kind: authentication
  name: Wisk Authentication
  slug: wisk-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Wisk Domain Security
  slug: wisk-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: wisk
tags:
- Restaurant
- Bar
- Inventory
- Hospitality
- Sales
- POS Integration
use_cases:
- description: A POS platform integrates with WISK so its venues' sales data flows into WISK for inventory reconciliation.
  name: POS Provider Integration
- description: Push daily sales lines so WISK can deplete inventory against actual POS sales and surface variance.
  name: Daily Sales Reconciliation
- description: Operators manage inventory, invoices, and cost of goods across multiple venues from one platform.
  name: Multi-Location Inventory
website: https://www.wisk.ai/
---
