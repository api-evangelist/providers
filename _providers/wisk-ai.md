---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Wisk Ai Agentic Access
  operation_count: 1
  slug: wisk-ai-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- description: No public, documented webhook or event-subscription surface is published by WISK as of this catalog date. Event-driven exchange with POS partners is arranged through WISK's partner integration process
  name: WISK Webhooks
  slug: wisk-ai-webhooks
- baseURL: https://api.wisk.ai
  baseurl_source: spec
  description: Push point-of-sale sales line items into a WISK venue account.
  name: WISK Sales API
  slug: wisk-ai-sales-api
artifact_total: 27
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: WISK Public Upload Sales API
  slug: open-wisk-ai-sales-api
- collection_type: open
  name: WISK Public Sales Upload API
  slug: open-wisk-ai-sales-upload
- collection_type: open
  name: WISK API
  slug: open-wisk-ai
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wisk-ai-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/wisk
- group: company
  title: ''
  type: Website
  url: https://www.wisk.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://help.wisk.ai/
- group: commercial
  title: ''
  type: Plans
  url: plans/wisk-ai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/wisk-ai-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/wisk-ai-finops.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/wisk-ai-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/wisk-ai-authentication.yml
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
- group: other
  title: ''
  type: X
  url: https://twitter.com/WISK_ai
- group: design
  title: ''
  type: SpectralRules
  url: rules/wisk-ai-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/wisk-ai-vocabulary.yaml
created: '2026-06-21'
description: WISK is a bar, restaurant, and hospitality inventory and cost-management platform that tracks items, counts inventory across venues, scans and reconciles supplier invoices, and integrates with 60+ POS systems to compare theoretical vs. actual usage. WISK's programmatic surface is partner-gated - a documented Public Sales upload API lets POS providers and partners push sales data into WISK, and customer API access is offered on the top (Premium) plan. There is no public, self-serve developer portal or published OpenAPI as of this catalog date.
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
- name: Wisk Ai Finops
  service_category: Management and Governance
  slug: wisk-ai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/wisk-ai.png
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
  name: Wisk Ai Sales Upload Context
  property_count: 6
  slug: wisk-ai-sales-upload-context
layout: provider
modified: '2026-08-08'
name: WISK
nav: Providers
network: true
overview: 'WISK publishes 1 API on the [APIs.io](https://apis.io/) network: Sales API. Tagged areas include Inventory, Restaurant, Bar, Hospitality, and Cost Management.


  The WISK catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  WISK''s developer surface includes documentation, authentication, signup flow, pricing, support, engineering blog, and 11 more developer resources.'
plans:
- name: Wisk Ai Plans Pricing
  plan_count: 5
  slug: wisk-ai-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 2
  name: Wisk Ai Rate Limits
  slug: wisk-ai-rate-limits
rules:
- effective_rule_count: 4
  extends: []
  name: WISK API Rules
  rule_count: 4
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 3
  slug: wisk-ai-jsonschema-spectral-rules
- effective_rule_count: 70
  extends:
  - spectral:oas
  name: WISK API Rules
  rule_count: 29
  severity_counts:
    error: 7
    hint: 0
    info: 4
    warn: 18
  slug: wisk-ai-spectral-rules
score:
  band: thin
  composite: 33.7
  coverage:
    artifact_dirs: 16
    catalog_earned: 69.5
    catalog_earned_first_party: 0.0
    catalog_gap: 45.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 56.6
    commercial_clarity: 56.6
    contract_governance: 28.8
    contract_quality: 18.0
    developer_ergonomics: 28.6
    discoverability: 59.3
    governance: 28.8
    operational_transparency: 21.1
  previous_composite: 33.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 2
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/wisk-ai/refs/heads/main/screenshots/wisk-ai-2026-06-20T201524.png
security:
- kind: authentication
  name: Wisk Ai Authentication
  slug: wisk-ai-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Wisk Ai Domain Security
  slug: wisk-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: wisk-ai
tags:
- Inventory
- Restaurant
- Bar
- Hospitality
- Cost Management
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
