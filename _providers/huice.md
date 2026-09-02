---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.4
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: The Wangdiantong (旺店通) ERP Open Platform HTTP API (openapi2). Endpoints are named PHP methods (e.g. trade_push.php, trade_query.php, goods_push.php, stock_query.php) grouped into basics (shops/warehou
  name: Wangdiantong Open Platform API
  slug: wangdiantong-open-platform-api
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.wangdian.cn/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://open.wangdian.cn/
- group: docs
  title: ''
  type: Documentation
  url: https://open.wangdian.cn/open/guide?path=guide_kfzn
- group: docs
  title: ''
  type: APIReference
  url: https://open.wangdian.cn/qyb/open/apidoc
- group: operate
  title: ''
  type: Support
  url: https://open.wangdian.cn/open/support
- group: auth
  title: ''
  type: Authentication
  url: authentication/huice-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/huice-conventions.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/huice-sandbox.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/huice-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/huice-lifecycle.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/huice-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/huice-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/huice-domain-security.yml
created: '2026-07-17'
description: Huice (慧策) is a Chinese enterprise software company whose flagship product, Wangdiantong (旺店通) ERP, is a tailor-made e-commerce management system for merchants operating across multiple online channels. It provides order management, warehouse and inventory management (WMS), goods and product-archive management, procurement, after-sales/returns processing, and financial operations (慧经营). Huice runs a public Open Platform (open.wangdian.cn) exposing an HTTP API (openapi2) for third-party integrators to synchronize shops, goods, orders, stock, purchasing, and logistics. The API uses a sid + appkey + timestamp + MD5 signature (sign) authentication scheme, page_no/page_size pagination, and a code/message response envelope, with separate sandbox and production hosts.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/huice.png
layout: provider
modified: '2026-07-19'
name: Huice
nav: Providers
network: true
overview: 'Huice publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Enterprise, E-Commerce, ERP, and Order Management.


  Huice''s developer surface includes documentation, API reference, support, authentication, sandbox, and 8 more developer resources.'
random_paper: 1
score:
  band: emerging
  composite: 17.6
  coverage:
    artifact_dirs: 9
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 50.0
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 17.6
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/huice/refs/heads/main/screenshots/huice-2026-07-25T221632.png
security:
- kind: authentication
  name: Huice Authentication
  slug: huice-authentication
  summary_line: signature · 1 scheme
- kind: domain-security
  name: Huice Domain Security
  slug: huice-domain-security
  summary_line: TLSv1.3 · DMARC
slug: huice
tags:
- Company
- Enterprise
- E-Commerce
- ERP
- Order Management
- Inventory Management
- Warehouse Management
- Retail
- Software-as-a-Service
- China
website: https://www.wangdian.cn/
---
