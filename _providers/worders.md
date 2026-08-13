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
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.5
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Worders Agentic Access
  operation_count: 13
  slug: worders-agentic-access
  summary_line: 13 operations · 2 acting
api_count: 7
apis:
- description: The Customers API from Worders — 1 operation(s) for customers.
  name: Worders Customers API
  slug: worders-customers-api
- description: The Freelancers API from Worders — 1 operation(s) for freelancers.
  name: Worders Freelancers API
  slug: worders-freelancers-api
- description: The Invoices API from Worders — 2 operation(s) for invoices.
  name: Worders Invoices API
  slug: worders-invoices-api
- description: The Orders API from Worders — 2 operation(s) for orders.
  name: Worders Orders API
  slug: worders-orders-api
- description: The PurchaseOrders API from Worders — 2 operation(s) for purchaseorders.
  name: Worders PurchaseOrders API
  slug: worders-purchaseorders-api
- description: The Quotes API from Worders — 2 operation(s) for quotes.
  name: Worders Quotes API
  slug: worders-quotes-api
- description: The Templates API from Worders — 1 operation(s) for templates.
  name: Worders Templates API
  slug: worders-templates-api
artifact_total: 11
common:
- group: company
  title: ''
  type: Website
  url: https://worders.net/
- group: docs
  title: ''
  type: Documentation
  url: https://api.worders.net/api-docs/index.html
- group: docs
  title: ''
  type: APIReference
  url: https://api.worders.net/api-docs/index.html
- group: start
  title: ''
  type: Login
  url: https://admin.worders.net/users/sign_in
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/worders/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/WordersNET
- group: auth
  title: ''
  type: Authentication
  url: authentication/worders-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/worders-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/worders-agentic-access.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/worders-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/worders-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/worders-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/worders-conformance.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/worders-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/worders-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/worders-api-overlay.yaml
- group: design
  title: ''
  type: DataModel
  url: data-model/worders-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Worders is a culturalization and localization company (a Partech portfolio company) that crafts translated, culturally-adapted content for global brands with in-country linguists. Alongside the services business it runs a Ruby on Rails translation-management platform (admin.worders.net) and publishes the Worders API V1 at api.worders.net — an OpenAPI 3.0.1-documented surface for freelance invoice verification and Plunet TMS automation covering customers, freelancers, invoices, orders, purchase orders, quotes, and order templates.
image: https://cdn.prod.website-files.com/67befd57da776c510ff3b66b/6830866136954deeba98bba4_worders_webclip.png
layout: provider
mcp_servers:
- description: ''
  name: worders-mcp.yml
  slug: worders-mcpyml
modified: '2026-07-21'
name: Worders
nav: Providers
network: true
overview: 'Worders publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Customers API, Freelancers API, Invoices API, and 4 more. Tagged areas include Company, Applicative Saas, Localization, Translation, and Culturalization.


  Worders'' developer surface includes documentation, API reference, authentication, and 15 more developer resources.'
random_paper: 54
score:
  band: thin
  composite: 31.4
  delta: 0.0
  facets:
    commercial_clarity: 13.2
    contract_quality: 52.9
    developer_ergonomics: 29.9
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 0.0
  previous_composite: 31.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
security:
- kind: authentication
  name: Worders Authentication
  slug: worders-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Worders Domain Security
  slug: worders-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: worders
tags:
- Company
- Applicative Saas
- Localization
- Translation
- Culturalization
- Language Services
- Invoicing
website: https://worders.net/
---
