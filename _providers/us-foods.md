---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 2
apis:
- description: US Foods MOXe is a comprehensive foodservice eCommerce platform enabling restaurants, healthcare facilities, and institutional customers to place orders, manage inventory, track deliveries, and pay in
  name: US Foods MOXe eCommerce Platform
  slug: moxe-ordering-platform
- description: US Foods supports electronic data interchange (EDI) for B2B integration with suppliers and trading partners. EDI transactions support purchase orders, invoices, advance ship notices, and product catal
  name: US Foods EDI Integration
  slug: edi-integration
artifact_total: 12
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/us-foods-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/usfoods
- group: other
  title: ''
  type: Suppliers
  url: https://www.usfoods.com/supplier-info.html
created: '2024-12-03'
description: US Foods is one of the largest foodservice distributors in the United States, serving restaurants, healthcare facilities, hospitality businesses, government institutions, and educational facilities. As a Fortune 500 company, US Foods operates a national distribution network with over 70 distribution centers and serves approximately 250,000 customers. The company's digital platform includes the MOXe eCommerce application for ordering and business management, EDI integration for B2B transactions, and a supplier PIM system for product data synchronization. US Foods has undergone significant digital transformation building a data mesh architecture on Apache Kafka, MongoDB, and cloud platforms to support its eCommerce and supply chain operations.
examples:
- key_count: 3
  name: Us Foods Order Example
  slug: us-foods-order-example
finops:
- name: Us Foods Finops
  service_category: Food Service Distribution
  slug: us-foods-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/us-foods.png
json_schemas:
- name: US Foods Order
  property_count: 11
  slug: us-foods-order
- name: US Foods Product
  property_count: 20
  slug: us-foods-product
json_structures:
- name: Us Foods Order Structure
  property_count: 0
  slug: us-foods-order-structure
jsonld:
- class_count: 25
  name: Us Foods Context
  property_count: 4
  slug: us-foods-context
layout: provider
modified: '2026-07-25'
name: US Foods
nav: Providers
network: true
overview: 'US Foods publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Food Service, Fortune 500, Distribution, Supply Chain, and eCommerce.


  The US Foods catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
plans:
- name: Us Foods Plans Pricing
  plan_count: 1
  slug: us-foods-plans-pricing
press:
- date: '2026-05-25'
  title: US Foods adds AI ordering as ecommerce drives Q4 sales ...
  url: https://www.digitalcommerce360.com/2026/02/13/us-foods-ai-ordering-tools-sales-q4-2025/
- date: '2026-05-25'
  title: Improve Restaurant Efficiency With AI
  url: https://www.usfoods.com/tools-tips-and-ideas/articles-and-publications/articles/improve-restaurant-efficiency-with-ai-
- date: '2026-05-25'
  title: Use AI to Drive Restaurant Customer Engagement and ...
  url: https://www.usfoods.com/tools-tips-and-ideas/articles-and-publications/articles/use-ai-to-drive-restaurant-customer-engagement-and-loyalty
- date: '2026-05-25'
  title: US Foods Case Study
  url: https://aws.amazon.com/solutions/case-studies/us-foods-case-study/
- date: '2026-05-25'
  title: US Foods Reports First Quarter Fiscal Year 2026 Earnings
  url: https://ir.usfoods.com/newsroom/news/news-details/2026/US-Foods-Reports-First-Quarter-Fiscal-Year-2026-Earnings/default.aspx
random_paper: 16
rate_limits:
- limit_count: 1
  name: Us Foods Rate Limits
  slug: us-foods-rate-limits
rules:
- name: US Foods API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: us-foods-jsonschema-spectral-rules
score:
  band: emerging
  composite: 24.7
  delta: -4.4
  facets:
    commercial_clarity: 28.9
    contract_quality: 12.9
    developer_ergonomics: 0.0
    discoverability: 59.3
    governance: 58.3
    operational_transparency: 21.1
  previous_composite: 29.1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: domain-security
  name: Us Foods Domain Security
  slug: us-foods-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: us-foods
tags:
- Food Service
- Fortune 500
- Distribution
- Supply Chain
- eCommerce
---
