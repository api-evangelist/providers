---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
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
- acting_count: 6
  human_in_the_loop: 0
  name: Synnex Agentic Access
  operation_count: 15
  slug: synnex-agentic-access
  summary_line: 15 operations · 6 acting
api_count: 7
apis:
- description: The Digital Bridge Developer Portal gives engineering teams direct access to REST APIs for products, pricing, orders, renewals, and cloud services. Partners can get sandbox API keys, test endpoints, a
  name: TD SYNNEX Digital Bridge API
  slug: digital-bridge
- description: Shopping cart operations.
  name: Synnex Cart API
  slug: synnex-cart-api
- description: End customer account management.
  name: Synnex Customers API
  slug: synnex-customers-api
- description: Order creation and management.
  name: Synnex Orders API
  slug: synnex-orders-api
- description: Product catalog and SKU operations.
  name: Synnex Products API
  slug: synnex-products-api
- description: Usage and billing reports.
  name: Synnex Reports API
  slug: synnex-reports-api
- description: Cloud subscription lifecycle management.
  name: Synnex Subscriptions API
  slug: synnex-subscriptions-api
artifact_total: 22
collections:
- collection_type: open
  name: TD SYNNEX StreamOne ION API
  slug: open-synnex-streamone-ion
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/synnex-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/synnex-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/synnex-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tdsynnex
- group: company
  title: ''
  type: Website
  url: https://www.tdsynnex.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.tdsynnex.com/ion/api/
- group: docs
  title: ''
  type: APIDocumentation
  url: https://docs.streamone.cloud/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/cloudmindsab/td-synnex
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/synnex-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/synnex-vocabulary.yml
created: '2026-05-03'
description: SYNNEX Corporation (now TD SYNNEX) is a Fortune 100 global IT distribution company and solutions aggregator that connects technology vendors with resellers, system integrators, and enterprise customers. The company provides comprehensive API access through its StreamOne ION platform for managing cloud subscriptions, product catalogs, customer accounts, and orders. TD SYNNEX was formed in 2021 through the merger of Synnex Corporation and Tech Data.
examples:
- key_count: 2
  name: Synnex Streamone Ion Createorder Example
  slug: synnex-streamone-ion-createOrder-example
- key_count: 2
  name: Synnex Streamone Ion Listcustomers Example
  slug: synnex-streamone-ion-listCustomers-example
finops:
- name: Synnex Finops
  service_category: IT Distribution / Cloud Marketplace
  slug: synnex-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/synnex.png
json_schemas:
- name: Customer
  property_count: 8
  slug: synnex-customer
- name: Subscription
  property_count: 10
  slug: synnex-subscription
json_structures:
- name: Synnex Subscription Structure
  property_count: 0
  slug: synnex-subscription-structure
jsonld:
- class_count: 18
  name: Synnex Context
  property_count: 2
  slug: synnex-context
layout: provider
modified: '2026-05-19'
name: Synnex
nav: Providers
network: true
overview: 'Synnex publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Cart API, Customers API, Orders API, and 3 more. Tagged areas include Technology Distribution, IT Distribution, Cloud Marketplace, Fortune 100, and Supply Chain.


  The Synnex catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Synnex''s developer surface includes authentication and 9 more developer resources.'
plans:
- name: Synnex Plans Pricing
  plan_count: 1
  slug: synnex-plans-pricing
press:
- date: '2026-05-25'
  title: TD SYNNEX Releases AI Game Plan to Support Partners ...
  url: https://news.tdsynnex.com/news/td-synnex-releases-ai-game-plan-to-support-partners-effort-to-accelerate-ai-adoption-with-customers/
- date: '2026-05-25'
  title: News - TD Synnex
  url: https://news.tdsynnex.com/
- date: '2026-05-25'
  title: AI Is the Future. Let's Build It Together!
  url: https://connect.tdsynnex.be/vendor/hpe/ai-is-the-future-lets-build-it-together/
- date: '2026-05-25'
  title: AI and analytics leader SAS selects TD SYNNEX as ...
  url: https://www.sas.com/cs_cz/news/press-releases/2023/september/ai-and-analytics-leader-sas-selects-td-synnex-as-primary-global-.html
- date: '2026-05-25'
  title: TD SYNNEX Evolves AI Go-to-Market Strategy Through ...
  url: https://www.thecannatareport.com/td-synnex-ai-gtm/
random_paper: 45
rate_limits:
- limit_count: 3
  name: Synnex Rate Limits
  slug: synnex-rate-limits
rules:
- name: Synnex API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: synnex-jsonschema-spectral-rules
- name: Synnex API Rules
  rule_count: 11
  severity_counts:
    error: 4
    hint: 0
    info: 1
    warn: 6
  slug: synnex-rules
score:
  band: developing
  composite: 47.2
  delta: -4.2
  facets:
    commercial_clarity: 28.9
    contract_quality: 65.3
    developer_ergonomics: 26.1
    discoverability: 68.5
    governance: 68.8
    operational_transparency: 36.8
  previous_composite: 51.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/synnex/refs/heads/main/screenshots/synnex-2026-06-20T194829.png
security:
- kind: authentication
  name: Synnex Authentication
  slug: synnex-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Synnex Domain Security
  slug: synnex-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: synnex
tags:
- Technology Distribution
- IT Distribution
- Cloud Marketplace
- Fortune 100
- Supply Chain
website: https://www.tdsynnex.com
---
