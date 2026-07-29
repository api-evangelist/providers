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
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: documented
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 47.1
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 19
  human_in_the_loop: 0
  name: Aqueduct Agentic Access
  operation_count: 32
  slug: aqueduct-agentic-access
  summary_line: 32 operations · 19 acting
api_count: 10
apis:
- description: The AccountOwner API from Aqueduct — 3 operation(s) for accountowner.
  name: Aqueduct AccountOwner API
  slug: aqueduct-accountowner-api
- description: The Bill API from Aqueduct — 2 operation(s) for bill.
  name: Aqueduct Bill API
  slug: aqueduct-bill-api
- description: The Invoice API from Aqueduct — 6 operation(s) for invoice.
  name: Aqueduct Invoice API
  slug: aqueduct-invoice-api
- description: The InvoiceLineItem API from Aqueduct — 1 operation(s) for invoicelineitem.
  name: Aqueduct InvoiceLineItem API
  slug: aqueduct-invoicelineitem-api
- description: The PriceModel API from Aqueduct — 3 operation(s) for pricemodel.
  name: Aqueduct PriceModel API
  slug: aqueduct-pricemodel-api
- description: The ProductPurchases API from Aqueduct — 1 operation(s) for productpurchases.
  name: Aqueduct ProductPurchases API
  slug: aqueduct-productpurchases-api
- description: The Products API from Aqueduct — 2 operation(s) for products.
  name: Aqueduct Products API
  slug: aqueduct-products-api
- description: The Provisioning API from Aqueduct — 1 operation(s) for provisioning.
  name: Aqueduct Provisioning API
  slug: aqueduct-provisioning-api
- description: The Subscriptions API from Aqueduct — 2 operation(s) for subscriptions.
  name: Aqueduct Subscriptions API
  slug: aqueduct-subscriptions-api
- description: The Webhooks API from Aqueduct — 1 operation(s) for webhooks.
  name: Aqueduct Webhooks API
  slug: aqueduct-webhooks-api
artifact_total: 15
asyncapis:
- description: Event notifications delivered by Aqueduct to registered webhook endpoints. Each event is an HTTP POST carrying the shared envelope. Subscribe by creating a webhook endpoint (POST /webhookendpoints) wi
  name: Aqueduct Webhooks
  slug: aqueduct-webhooks-asyncapi
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.tryaqueduct.com/reference
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tryaqueduct.com/reference
- group: docs
  title: ''
  type: APIReference
  url: https://docs.tryaqueduct.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.tryaqueduct.com/reference/getting-started-with-your-api
- group: auth
  title: ''
  type: Authentication
  url: authentication/aqueduct-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/aqueduct-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/aqueduct-conventions.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/aqueduct-webhooks-asyncapi.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/aqueduct-webhooks-asyncapi.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/aqueduct-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/aqueduct-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/aqueduct-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/aqueduct-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aqueduct-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/aqueduct-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://www.tryaqueduct.com/
created: '2026-07-17'
description: Aqueduct is a fintech billing platform that equips B2B businesses with billing, invoicing, quoting, and accounting for usage-based and metered business models. Developers configure how they collect money as a PriceModel (composed of price functions such as per-unit meters), send billable usage events, and let Aqueduct create invoices and subscriptions, send invoices by email, issue refunds, and auto-provision access via signed webhooks. The REST API lives at api.tryaqueduct.com/v1 with API-key authentication and a documented Idempotency-Key contract. Founded 2020 in Bellevue, WA and backed by Bain Capital Ventures and Conversion Capital, Aqueduct was acquired by Stripe in August 2024; its ReadMe developer portal at docs.tryaqueduct.com remains live.
image: https://files.readme.io/9e3d7fe-small-Logo_4.png
layout: provider
mcp_servers:
- description: ''
  name: aqueduct-mcp.yml
  slug: aqueduct-mcpyml
modified: '2026-07-18'
name: Aqueduct
nav: Providers
network: true
overview: 'Aqueduct publishes 10 APIs on the [APIs.io](https://apis.io/) network, including AccountOwner API, Bill API, Invoice API, and 7 more. Tagged areas include Company, Fintech, Billing, Invoicing, and Metering.


  The Aqueduct catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Aqueduct''s developer surface includes documentation, API reference, getting-started guide, authentication, and 13 more developer resources.'
random_paper: 60
score:
  band: thin
  composite: 35.0
  delta: -2.6
  facets:
    commercial_clarity: 0.0
    contract_quality: 59.7
    developer_ergonomics: 49.5
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 7.9
  previous_composite: 37.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 26.6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/aqueduct/refs/heads/main/screenshots/aqueduct-2026-07-25T200954.png
security:
- kind: authentication
  name: Aqueduct Authentication
  slug: aqueduct-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Aqueduct Domain Security
  slug: aqueduct-domain-security
  summary_line: DNSSEC · DMARC
slug: aqueduct
tags:
- Company
- Fintech
- Billing
- Invoicing
- Metering
- Usage-Based
- Subscriptions
- Payments
- API
website: https://www.tryaqueduct.com/
---
