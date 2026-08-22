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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: na
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.5
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Tyson Foods Agentic Access
  operation_count: 3
  slug: tyson-foods-agentic-access
  summary_line: 3 operations
api_count: 2
apis:
- description: Order management operations
  name: Tyson Foods Orders API
  slug: tyson-foods-orders-api
- description: Shipment tracking operations
  name: Tyson Foods Shipments API
  slug: tyson-foods-shipments-api
artifact_total: 19
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Tyson Foods EDI Integration API
  slug: open-tyson-foods-edi-integration-api
- collection_type: open
  name: Tyson Foods EDI Integration Orders API
  slug: open-tyson-foods-orders-api
- collection_type: open
  name: Tyson Foods EDI Integration Orders Shipments API
  slug: open-tyson-foods-shipments-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tyson-foods-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tyson-foods-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tyson-foods
- group: company
  title: ''
  type: Website
  url: https://www.tysonfoods.com
- group: other
  title: ''
  type: Business Solutions
  url: https://www.tysonfoods.com/business-solutions
- group: company
  title: ''
  type: Investor Relations
  url: https://ir.tysonfoods.com
- group: other
  title: ''
  type: Sustainability
  url: https://www.tysonfoods.com/sustainability
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.tysonfoods.com/legal/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tysonfoods.com/legal/privacy-policy
- group: design
  title: ''
  type: JSONLD
  url: json-ld/tyson-foods-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/tyson-foods-order-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/tyson-foods-shipment-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/tyson-foods-order-structure.json
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/tyson-foods-vocabulary.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/tyson-foods-rules.yml
- group: company
  title: ''
  type: Blog
  url: https://www.tysonfoods.com/news
created: '2026-05-03'
description: Tyson Foods is one of the world's largest food companies and a Fortune 100 company, producing chicken, beef, pork, and prepared foods. Tyson Foods provides B2B integration capabilities for trading partners including EDI (Electronic Data Interchange) and API integrations for supply chain management, order processing, and logistics operations.
examples:
- key_count: 2
  name: Tyson Foods Get Orders Example
  slug: tyson-foods-get-orders-example
- key_count: 2
  name: Tyson Foods Get Shipments Example
  slug: tyson-foods-get-shipments-example
finops:
- name: Tyson Foods Finops
  service_category: B2B Integration
  slug: tyson-foods-finops
image: https://www.tysonfoods.com/favicon.ico
json_schemas:
- name: Tyson Foods Order
  property_count: 7
  slug: tyson-foods-order
- name: Tyson Foods Shipment
  property_count: 9
  slug: tyson-foods-shipment
json_structures:
- name: Tyson Foods Order Structure
  property_count: 7
  slug: tyson-foods-order-structure
jsonld:
- class_count: 9
  name: Tyson Foods Context
  property_count: 11
  slug: tyson-foods-context
layout: provider
modified: '2026-05-19'
name: Tyson Foods
nav: Providers
network: true
overview: 'Tyson Foods publishes 2 APIs on the [APIs.io](https://apis.io/) network: Orders API and Shipments API. Tagged areas include B2B Integration, EDI, Food, Fortune 100, and Supply Chain.


  The Tyson Foods catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Tyson Foods'' developer surface includes engineering blog and 15 more developer resources.'
plans:
- name: Tyson Foods Plans Pricing
  plan_count: 1
  slug: tyson-foods-plans-pricing
press:
- date: '2026-05-25'
  title: Tyson Food's AI-Driven Tech Helps Brands Avoid Digital ...
  url: https://www.ana.net/miccontent/show/id/cs-2024-09-mma-tyson-foods-13139
- date: '2026-05-25'
  title: Tyson Ventures Calls Startups to Apply for Tyson Demo ...
  url: https://www.tysonfoods.com/news/news-releases/2025/3/tyson-ventures-calls-startups-apply-tyson-demo-day-2025
- date: '2026-05-25'
  title: Tyson Foods elevates customer search experience with an ...
  url: https://aws.amazon.com/blogs/machine-learning/tyson-foods-elevates-customer-search-experience-with-an-ai-powered-conversational-assistant/
- date: '2026-05-25'
  title: Tyson Foods selects six AI startups at Demo Day event
  url: https://talkbusiness.net/2025/07/tyson-foods-selects-six-ai-startups-at-demo-day-event/
- date: '2026-05-25'
  title: Tyson Demo Day Showcases AI Innovations in Food ...
  url: https://www.tysonfoods.com/news/news-releases/2025/7/tyson-demo-day-showcases-ai-innovations-food-technology
random_paper: 2
rate_limits:
- limit_count: 1
  name: Tyson Foods Rate Limits
  slug: tyson-foods-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Tyson Foods API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: tyson-foods-jsonschema-spectral-rules
- effective_rule_count: 49
  extends:
  - spectral:oas
  name: Tyson Foods API Rules
  rule_count: 8
  severity_counts:
    error: 2
    hint: 1
    info: 0
    warn: 5
  slug: tyson-foods-rules
score:
  band: thin
  composite: 32.2
  delta: -7.3
  facets:
    access_clarity: 28.6
    commercial_clarity: 28.6
    contract_governance: 25.0
    contract_quality: 58.7
    developer_ergonomics: 2.4
    discoverability: 75.9
    governance: 25.0
    operational_transparency: 5.3
  previous_composite: 39.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/tyson-foods/refs/heads/main/screenshots/tyson-foods-2026-06-20T195909.png
security:
- kind: domain-security
  name: Tyson Foods Domain Security
  slug: tyson-foods-domain-security
  summary_line: TLSv1.3 · DMARC
slug: tyson-foods
tags:
- B2B Integration
- EDI
- Food
- Fortune 100
- Supply Chain
website: https://www.tysonfoods.com
---
