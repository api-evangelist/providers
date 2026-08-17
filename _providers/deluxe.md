---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 62.6
  scored_at: '2026-08-17'
api_count: 4
apis:
- description: 'The DPP Gateway Experience API is the core Deluxe Payments Platform contract: 37 operations across payments (sale, authorize, complete, cancel, search, batch), EMV card-present processing and device m'
  name: Deluxe Payments Platform — Gateway Experience API
  slug: deluxe-api
- description: 'The DPP Reports Experience API publishes eight read operations over merchant settlement and transaction history — credit card and ACH daily settlement, credit card and ACH monthly fee statements, and '
  name: Deluxe Payments Platform — Reports Experience API
  slug: dpp-reports-api
- description: The DPP Invoice Experience API publishes eleven operations for merchant invoicing — create a draft, modify invoice details, modify invoice status, retrieve, search, share, clone and download an invoic
  name: Deluxe Payments Platform — Invoice Experience API
  slug: dpp-invoices-api
- description: The only OpenAPI document Deluxe publishes itself — an OpenAPI 3.0.0 definition titled "Deluxe Postman-Sandbox", served from Deluxe's own Stoplight workspace and describing the sandbox bearer token ex
  name: Deluxe Payments Platform — Sandbox API (Deluxe-published OpenAPI)
  slug: dpp-sandbox-api
artifact_total: 15
asyncapis:
- description: ''
  name: Deluxe Webhooks
  slug: deluxe-webhooks
collections:
- collection_type: open
  name: DPP Gateway Experience API
  slug: open-deluxe-dpp-gateway
- collection_type: open
  name: DPP Invoice Experience API
  slug: open-deluxe-dpp-invoices
- collection_type: open
  name: DPP Reports Experience API
  slug: open-deluxe-dpp-reports
- collection_type: open
  name: Deluxe Postman-Sandbox
  slug: open-deluxe-postman-sandbox
common:
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/deluxe-dpp-gateway-openapi.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/deluxe-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/deluxe-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/deluxe-data-model.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/deluxe-problem-types.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/deluxe-decline-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/deluxe-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/deluxe-conformance.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/deluxe-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/deluxe-components.yml
- group: build
  title: ''
  type: Packages
  url: packages/deluxe-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/deluxe-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/deluxe-llms.txt
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/deluxe-webhooks.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/deluxe-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/deluxe-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/deluxe-finops.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/deluxe-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.deluxe.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.deluxe.com/docs/deluxe-payments-platform/zoi9qoo2d5tf2-deluxe-payments-platform
- group: docs
  title: ''
  type: APIReference
  url: https://developer.deluxe.com/api-ref/merchant-services/payments
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.deluxe.com/docs-content/payments/merchant-services/get-started
- group: operate
  title: ''
  type: Support
  url: https://www.deluxe.com/about/contact-us/
- group: company
  title: ''
  type: Blog
  url: https://www.deluxe.com/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.deluxe.com/policy/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.deluxe.com/policy/privacy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/deluxe-corporation
- group: other
  title: ''
  type: X
  url: https://twitter.com/Deluxe
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@deluxe
- group: company
  title: ''
  type: Website
  url: https://www.deluxe.com
created: '2026-04-19'
description: 'Deluxe Corporation (NYSE: DLX) is a US payments and data company that has moved from its origin as a check printer into merchant services, treasury management, payroll and marketing data. Its developer surface is the Deluxe Payments Platform (DPP), a gateway sold to independent software vendors and merchants and documented at developer.deluxe.com. DPP publishes three RAML 1.0 APIs covering 56 operations: a Gateway Experience API for card and ACH/EFT sales, authorizations, captures, voids, refunds, batches, EMV card-present processing on Ingenico terminals, customer vault and tokenization, subscriptions, payment links and an eight-event webhook surface; a Reports Experience API for daily card and ACH settlement, monthly fee statements and authorized/captured/settled transaction reports; and an Invoice Experience API for drafting, editing, sharing, cloning and downloading invoices. Deluxe also ships two browser-embeddable payment surfaces — a Hosted Payment Form and an Embedded
  Payments JavaScript SDK — both of which keep the integrator out of PCI DSS scope. Access is not self-serve: credentials are issued by the Deluxe integrations team after an email request, and no pricing is published.'
finops:
- name: Deluxe Finops
  service_category: Payments / Treasury / Business Services
  slug: deluxe-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/deluxe.png
layout: provider
mcp_servers:
- description: ''
  name: deluxe-mcp.yml
  slug: deluxe-mcpyml
modified: '2026-08-13'
name: Deluxe Corporation
nav: Providers
network: true
overview: 'Deluxe Corporation publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Deluxe Payments Platform — Gateway Experience API, Deluxe Payments Platform — Reports Experience API, Deluxe Payments Platform — Invoice Experience API, and 1 more. Tagged areas include Payments, Merchant Services, Card Processing, ACH, and Invoicing.


  The Deluxe Corporation catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Deluxe Corporation''s developer surface includes authentication, sandbox, documentation, API reference, getting-started guide, support, engineering blog, and 24 more developer resources.'
plans:
- name: Deluxe Plans Pricing
  plan_count: 0
  slug: deluxe-plans-pricing
random_paper: 51
rate_limits:
- limit_count: 0
  name: Deluxe Rate Limits
  slug: deluxe-rate-limits
score:
  band: developing
  composite: 47.8
  delta: 37.9
  facets:
    commercial_clarity: 28.9
    contract_quality: 64.2
    developer_ergonomics: 73.9
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 7.9
  previous_composite: 9.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 39.1
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/deluxe/refs/heads/main/screenshots/deluxe-2026-06-20T175905.png
security:
- kind: authentication
  name: Deluxe Authentication
  slug: deluxe-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Deluxe Domain Security
  slug: deluxe-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: deluxe
tags:
- Payments
- Merchant Services
- Card Processing
- ACH
- Invoicing
- Subscriptions
- Tokenization
- Webhooks
- Reporting
- Data Analytics
- Marketing
- Small Business
website: https://www.deluxe.com
---
