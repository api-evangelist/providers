---
access_model:
  confidence: high
  label: 14-day free trial, then paid plans from $199/mo
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - authentication
  - https://www.metrilo.com/pricing
  trial: true
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 37.0
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Metrilo Agentic Access
  operation_count: 10
  slug: metrilo-agentic-access
  summary_line: 10 operations · 10 acting
api_count: 5
apis:
- description: The Categories API from Metrilo — 2 operation(s) for categories.
  name: Metrilo Categories API
  slug: metrilo-categories-api
- description: The Customers API from Metrilo — 4 operation(s) for customers.
  name: Metrilo Customers API
  slug: metrilo-customers-api
- description: The Orders API from Metrilo — 2 operation(s) for orders.
  name: Metrilo Orders API
  slug: metrilo-orders-api
- description: The Products API from Metrilo — 2 operation(s) for products.
  name: Metrilo Products API
  slug: metrilo-products-api
- description: Metrilo's own published specification for the tracking and CRM ingestion API — OpenAPI 3.0.1, version 2.1.1, 10 operations and 19 schemas covering categories, products, customers (including tag/untag)
  name: Metrilo Tracking API
  slug: metrilo-tracking-api
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Metrilo Tracking & CRM Categories API
  slug: open-metrilo-categories-api
- collection_type: open
  name: Metrilo Tracking & CRM Categories Customers API
  slug: open-metrilo-customers-api
- collection_type: open
  name: Metrilo Tracking & CRM Categories Orders API
  slug: open-metrilo-orders-api
- collection_type: open
  name: Metrilo Tracking & CRM Categories Products API
  slug: open-metrilo-products-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/metrilo-agentic-access.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/metrilo-tracking-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/metrilo-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://github.com/Metrilo/custom-integration
- group: docs
  title: ''
  type: Documentation
  url: https://docs.metrilo.com
- group: docs
  title: ''
  type: APIReference
  url: https://app.swaggerhub.com/apis/metrilo/api/2.1.1
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.metrilo.com/en/collections/57629-getting-started-with-metrilo
- group: operate
  title: ''
  type: Support
  url: https://docs.metrilo.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Metrilo
- group: commercial
  title: ''
  type: Pricing
  url: https://www.metrilo.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.metrilo.com/signup
- group: start
  title: ''
  type: Login
  url: https://app.metrilo.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.metrilo.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.metrilo.com/privacy-policy
- group: auth
  title: ''
  type: Authentication
  url: authentication/metrilo-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/metrilo-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/metrilo-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/metrilo-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/metrilo-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Packages
  url: packages/metrilo-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/metrilo-packages.yml
- group: design
  title: ''
  type: Components
  url: components/metrilo-components.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/metrilo-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/metrilo-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://docs.metrilo.com/en/articles/1613060-metrilo-and-gdpr
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/metrilo-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/metrilo-tracking-api-overlay.yaml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/metrilo-tool-crosswalk.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/metrilo-plans-pricing.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/metrilo-changelog.yml
created: '2026-07-17'
description: Metrilo is a plug-and-play ecommerce growth platform that combines real-time analytics, an ecommerce CRM, and email marketing for online brands. Founded in 2014 and acquired by Brevo (formerly Sendinblue) in 2021, Metrilo tracks visitor and customer behavior, builds rich customer profiles with 30+ segmentation filters, and powers retention-focused email campaigns. Developers integrate via official plugins for WooCommerce, Magento, and OpenCart, a client-side JavaScript tracking library (window.metrilo), and a server-side ingestion API at trk.mtrl.me/v2 that pushes customers, categories, products, and orders using an API Token plus an HMAC-SHA256 X-Digest request signature.
image: https://www.metrilo.com/images/metrilo-1200x628.png
layout: provider
mcp_servers:
- description: ''
  name: metrilo-mcp.yml
  slug: metrilo-mcpyml
modified: '2026-08-13'
name: Metrilo
nav: Providers
network: true
overview: 'Metrilo publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Categories API, Customers API, Orders API, and 2 more. Tagged areas include Company, Ecommerce, Analytics, CRM, and Email Marketing.


  Metrilo''s developer surface includes documentation, API reference, getting-started guide, support, pricing, signup flow, authentication, and 24 more developer resources.'
plans:
- name: Metrilo Plans Pricing
  plan_count: 3
  slug: metrilo-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: Metrilo Rate Limits
  slug: metrilo-rate-limits
score:
  band: developing
  composite: 47.6
  delta: 0.6
  facets:
    access_clarity: 84.2
    commercial_clarity: 84.2
    contract_governance: 30.3
    contract_quality: 13.9
    developer_ergonomics: 60.1
    discoverability: 92.6
    governance: 30.3
    operational_transparency: 18.4
  previous_composite: 47.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 4
      marker_coverage: 80.0
      total: 5
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/metrilo/refs/heads/main/screenshots/metrilo-2026-08-07T172735.png
security:
- kind: authentication
  name: Metrilo Authentication
  slug: metrilo-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Metrilo Domain Security
  slug: metrilo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: metrilo
tags:
- Company
- Ecommerce
- Analytics
- CRM
- Email Marketing
- Customer Retention
- Tracking
- Marketing
---
