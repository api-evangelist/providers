---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  - security
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
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: United Natural Foods Agentic Access
  operation_count: 12
  slug: united-natural-foods-agentic-access
  summary_line: 12 operations · 4 acting
api_count: 1
apis:
- description: UNFI supports Electronic Data Interchange (EDI) for automated exchanges of purchase orders, invoices, and fulfillment data between UNFI and its supplier and retail partners. EDI integration supports t
  name: UNFI EDI Integration
  slug: unfi-edi-integration
- baseURL: https://api.unfi.com/v1
  baseurl_source: declared
  description: Analytics and data reporting
  name: United Natural Foods (UNFI) Insights API
  slug: united-natural-foods-insights-api
- baseURL: https://api.unfi.com/v1
  baseurl_source: declared
  description: Purchase orders and fulfillment
  name: United Natural Foods (UNFI) Orders API
  slug: united-natural-foods-orders-api
- baseURL: https://api.unfi.com/v1
  baseurl_source: declared
  description: Product catalog and listing management
  name: United Natural Foods (UNFI) Products API
  slug: united-natural-foods-products-api
- baseURL: https://api.unfi.com/v1
  baseurl_source: declared
  description: Supplier profile and warehouse management
  name: United Natural Foods (UNFI) Suppliers API
  slug: united-natural-foods-suppliers-api
artifact_total: 26
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: UNFI Supplier and Data API
  slug: open-unfi-supplier
- collection_type: open
  name: UNFI Supplier and Data Insights API
  slug: open-united-natural-foods-insights-api
- collection_type: open
  name: UNFI Supplier and Data Insights Orders API
  slug: open-united-natural-foods-orders-api
- collection_type: open
  name: UNFI Supplier and Data Insights Products API
  slug: open-united-natural-foods-products-api
- collection_type: open
  name: UNFI Supplier and Data Insights Suppliers API
  slug: open-united-natural-foods-suppliers-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/united-natural-foods-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/united-natural-foods-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/united-natural-foods-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/united-natural-foods-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.unfi.com
- group: start
  title: ''
  type: Supplier Portal
  url: https://suppliers.unfi.com
- group: start
  title: ''
  type: Customer Portal
  url: https://www.myunfi.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/unfi
- group: other
  title: ''
  type: X
  url: https://twitter.com/UNFIInc
- group: company
  title: ''
  type: Investor Relations
  url: https://ir.unfi.com
- group: docs
  title: ''
  type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/united-natural-foods/main/openapi/unfi-supplier-openapi.yml
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/united-natural-foods/main/rules/unfi-supplier-rules.yml
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/united-natural-foods/main/json-schema/unfi-supplier-product-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/united-natural-foods/main/json-schema/unfi-supplier-order-schema.json
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/united-natural-foods/main/json-ld/united-natural-foods-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/united-natural-foods/main/vocabulary/united-natural-foods-vocabulary.yml
created: '2026-03-21'
description: United Natural Foods, Inc. (UNFI) is the largest publicly traded wholesale distributor of health and specialty food in the United States and Canada. UNFI supplies natural, organic, specialty, and conventional foods to over 30,000 retail locations. UNFI provides digital supplier and customer portals including myUNFI, supplier portal, EDI integration, and the Harmony Core API for data access.
examples:
- key_count: 2
  name: Unfi Supplier Getsalesinsights Example
  slug: unfi-supplier-getSalesInsights-example
- key_count: 2
  name: Unfi Supplier Listorders Example
  slug: unfi-supplier-listOrders-example
- key_count: 2
  name: Unfi Supplier Listproducts Example
  slug: unfi-supplier-listProducts-example
finops:
- name: United Natural Foods Finops
  service_category: Food Distribution
  slug: united-natural-foods-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/united-natural-foods.png
json_schemas:
- name: UNFI Purchase Order
  property_count: 9
  slug: unfi-supplier-order
- name: UNFI Product
  property_count: 13
  slug: unfi-supplier-product
json_structures:
- name: Unfi Supplier Product Structure
  property_count: 0
  slug: unfi-supplier-product-structure
jsonld:
- class_count: 0
  name: United Natural Foods Context
  property_count: 28
  slug: united-natural-foods-context
layout: provider
modified: '2026-05-19'
name: United Natural Foods (UNFI)
nav: Providers
network: true
overview: 'United Natural Foods (UNFI) publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Insights API, Orders API, Products API, and 1 more. Tagged areas include Food Distribution, Wholesale, Natural Foods, Supply Chain, and Fortune 500.


  The United Natural Foods (UNFI) catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  United Natural Foods (UNFI)''s developer surface includes authentication and 15 more developer resources.'
plans:
- name: United Natural Foods Plans Pricing
  plan_count: 1
  slug: united-natural-foods-plans-pricing
press:
- date: '2026-05-25'
  title: UNFI taps into AI to improve forecasting, fulfillment
  url: https://www.digitalcommerce360.com/2025/12/02/unfi-ai-digital-overhaul-q1-fiscal-2026/
- date: '2026-05-25'
  title: AI is starting to take over inventory planning and it's ...
  url: https://www.instagram.com/reel/DWICYYlBpb6/
- date: '2026-05-25'
  title: United Natural Foods Expands Supply Chain Evolution ...
  url: https://www.businesswire.com/news/home/20240129358372/en/United-Natural-Foods-Expands-Supply-Chain-Evolution-with-Implementation-of-A.I.-Powered-Warehouse-Automation-System-in-its-New-Manchester-Distribution-Center
- date: '2026-05-25'
  title: United Natural Foods announces partnership with ...
  url: https://www.relexsolutions.com/news/united-natural-foods-announces-partnership-with-relex-solutions/
- date: '2026-05-25'
  title: UNFI and Symbotic Announce Agreement to Implement ...
  url: https://ir.unfi.com/news/press-release-details/2022/UNFI-and-Symbotic-Announce-Agreement-to-Implement-Industry-Leading-Warehouse-Automation-Systems/default.aspx
random_paper: 0
rate_limits:
- limit_count: 1
  name: United Natural Foods Rate Limits
  slug: united-natural-foods-rate-limits
rules:
- effective_rule_count: 56
  extends:
  - spectral:oas
  name: United Natural Foods (UNFI) API Rules
  rule_count: 15
  severity_counts:
    error: 4
    hint: 0
    info: 2
    warn: 9
  slug: unfi-supplier-rules
- effective_rule_count: 5
  extends: []
  name: United Natural Foods (UNFI) API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: united-natural-foods-jsonschema-spectral-rules
score:
  band: thin
  composite: 36.6
  coverage:
    artifact_dirs: 19
    catalog_earned: 75.0
    catalog_earned_first_party: 0.0
    catalog_gap: 40.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 69.7
    contract_quality: 62.6
    developer_ergonomics: 11.9
    discoverability: 68.5
    governance: 69.7
    operational_transparency: 5.3
  previous_composite: 36.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
security:
- kind: authentication
  name: United Natural Foods Authentication
  slug: united-natural-foods-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: United Natural Foods Domain Security
  slug: united-natural-foods-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: united-natural-foods
tags:
- Food Distribution
- Wholesale
- Natural Foods
- Supply Chain
- Fortune 500
website: https://www.unfi.com
---
