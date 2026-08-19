---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.8
  scored_at: '2026-08-19'
api_count: 6
apis:
- description: 'Instock is using the term `article` to describe unique product or SKU managed by Instock ASRS. Articles resource is mostly managed by you as a client of Instock API. Article data is shared across all '
  name: Instock Articles API
  slug: instock-articles-api
- description: Inventory resource returns data on the current quantity of article(s) that your organization has uploaded, use it to track articles that are low in stock or out-of-stock and require replenishment in s
  name: Instock Inventory API
  slug: instock-inventory-api
- description: 'Moves allow to retrieve data on article(s) flow in and out of of a particular site owned by your organization. List moves of all articles or retrieve them for a single article. **Note**: Refine your s'
  name: Instock Moves API
  slug: instock-moves-api
- description: 'Intentions of users of Instock ASRS are represented by `orders` structure. Orders resource allows: * create/update/retrieve records for picking of goods from the ASRS (`customer` orders) * retrieve-on'
  name: Instock Orders API
  slug: instock-orders-api
- description: Fulfillment of orders by associates and ASRS is split into chunks called `ordertasks`. An `ordertask` can represent a picking of several lines of customer order, for example. Each ordertask correspond
  name: Instock Ordertasks API
  slug: instock-ordertasks-api
- description: Each Instock site (or just site) represents a single instance of Instock ASRS. Such instance can represent either physical installation of ASRS or a simulation in sandbox environment. Organization may
  name: Instock Sites API
  slug: instock-sites-api
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Instock API reference Articles API
  slug: open-instock-articles-api
- collection_type: open
  name: Instock API reference Articles Inventory API
  slug: open-instock-inventory-api
- collection_type: open
  name: Instock API reference Articles Moves API
  slug: open-instock-moves-api
- collection_type: open
  name: Instock API reference Articles Orders API
  slug: open-instock-orders-api
- collection_type: open
  name: Instock API reference Articles Ordertasks API
  slug: open-instock-ordertasks-api
- collection_type: open
  name: Instock API reference Articles Sites API
  slug: open-instock-sites-api
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/instock-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/instock-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://instock.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://instock.com/en/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://instock.com/en/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://instock.com/en/docs/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://instock.com/en/docs/getting-started/
- group: start
  title: ''
  type: Login
  url: https://cloud.instock.com/sign-in/
- group: operate
  title: ''
  type: Support
  url: https://instock.com/en/contact-us/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://instock.com/en/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://instock.com/en/news/
- group: company
  title: ''
  type: Careers
  url: https://instock.com/en/careers/
- group: design
  title: ''
  type: Conventions
  url: conventions/instock-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/instock-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/instock-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/instock-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/instock-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/instock-sandbox.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/instock-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/instock-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/instock-openapi-overlay.yaml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/instock-openapi.json
created: '2026-07-17'
description: 'Instock is a robotics company delivering a goods-to-person automated storage and retrieval system (ASRS) as a fulfillment robotics-as-a-service (RaaS) offering. The system pairs a static "Grid" racking framework, stackable "Bins", and autonomous three-dimensional "Robots" with "Incloud", a cloud software platform that orchestrates warehouse fulfillment operations. Instock publishes a REST-based HTTP API (Incloud) that lets a customer''s host systems (PIM/IMS/OMS) integrate with the ASRS: managing sites, uploading articles (SKUs), creating and advancing customer orders, tracking order tasks, and reading inventory and article moves. The API accepts and returns JSON, uses Bearer-token (JWT) authentication issued during onboarding, cursor-based pagination, snake_case properties, and RFC 3339 timestamps. Instock was surfaced as a portfolio company of Lux Capital. Sector: robotics / warehouse automation.'
image: https://instock.com/en/images/logo.svg
layout: provider
mcp_servers:
- description: ''
  name: instock-mcp.yml
  slug: instock-mcpyml
modified: '2026-07-19'
name: Instock
nav: Providers
network: true
overview: 'Instock publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Articles API, Inventory API, Moves API, and 3 more. Tagged areas include Company, Robotics, Warehouse Automation, Fulfillment, and Logistics.


  Instock''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, sandbox, and 16 more developer resources.'
random_paper: 18
score:
  band: developing
  composite: 40.5
  delta: -2.7
  facets:
    access_clarity: 6.6
    commercial_clarity: 6.6
    contract_governance: 16.7
    contract_quality: 63.3
    developer_ergonomics: 66.1
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 0.0
  previous_composite: 43.2
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/instock/refs/heads/main/screenshots/instock-2026-07-25T222617.png
security:
- kind: authentication
  name: Instock Authentication
  slug: instock-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Instock Domain Security
  slug: instock-domain-security
  summary_line: TLSv1.3
slug: instock
tags:
- Company
- Robotics
- Warehouse Automation
- Fulfillment
- Logistics
- ASRS
- Supply Chain
- Inventory Management
website: https://instock.com
---
