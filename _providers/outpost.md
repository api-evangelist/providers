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
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.9
  scored_at: '2026-08-26'
api_count: 3
apis:
- description: REST API that automates tax registration, calculation, and filing while the merchant keeps their own checkout and PSP. Server-to-server, OAuth2 client-credentials. Covers tax calculations, tax transac
  name: Outpost Tax of Record API
  slug: outpost-tax-of-record-api
- description: REST API to issue proforma invoices for B2B customers paying by bank transfer, receive settlement webhooks, and retrieve tax invoices for payments and refunds processed through Outpost. Server-to-serv
  name: Outpost Merchant of Record API
  slug: outpost-merchant-of-record-api
- description: Partner REST API to onboard existing merchants onto Outpost services with a hosted onboarding UI and asynchronous review workflow. JWT bearer auth, /partner/api prefix, staging and production environm
  name: Outpost Hosted Onboarding (Partner) API
  slug: outpost-hosted-onboarding-partner-api
artifact_total: 7
asyncapis:
- description: ''
  name: Outpost Merchant Of Record Webhooks
  slug: outpost-merchant-of-record-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://outpostnow.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://outpostnow.com/docs/api/tax-of-record/
- group: docs
  title: ''
  type: Documentation
  url: https://outpostnow.com/docs/api/tax-of-record/
- group: docs
  title: ''
  type: APIReference
  url: https://outpostnow.com/docs/api/tax-of-record/
- group: company
  title: ''
  type: Blog
  url: https://outpostnow.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://outpostnow.com/faq/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://outpostnow.com/mor-terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://outpostnow.com/privacy-policy/
- group: auth
  title: ''
  type: Authentication
  url: authentication/outpost-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/outpost-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/outpost-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/outpost-problem-types.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/outpost-merchant-of-record-webhooks.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/outpost-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/outpost-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/outpost-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/outpost-conformance.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/outpost-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/outpost-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/outpost-domain-security.yml
created: '2026-07-17'
description: Outpost is a Merchant of Record and Tax of Record platform for cross-border commerce, letting retailers sell into new markets while Outpost takes on the legal and tax liability — local payments, VAT/GST/sales-tax registration, calculation and filing, proforma invoicing for B2B bank transfers, and hosted merchant onboarding. Its server-to-server REST APIs (Tax of Record, Merchant of Record, and Hosted Onboarding) use OAuth2 client-credentials and JWT bearer authentication so merchants keep their own checkout and payment service providers (Stripe, Adyen) while Outpost handles compliance across jurisdictions. Founded by ex-Revolut operator Will Mahon-Heap and backed by Ribbit Capital and Better Tomorrow Ventures.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/outpost.png
layout: provider
mcp_servers:
- description: ''
  name: Outpost MCP Server
  slug: outpost-mcp-server
modified: '2026-07-20'
name: Outpost
nav: Providers
network: true
overview: 'Outpost publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Merchant of Record, Tax of Record, Cross-Border Commerce, and Payments.


  The Outpost catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Outpost''s developer surface includes documentation, API reference, engineering blog, support, authentication, sandbox, and 14 more developer resources.'
random_paper: 0
score:
  band: thin
  composite: 37.7
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 42.7
    developer_ergonomics: 52.4
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 7.9
  previous_composite: 37.7
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 39.1
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/outpost/refs/heads/main/screenshots/outpost-2026-08-07T191059.png
security:
- kind: authentication
  name: Outpost Authentication
  slug: outpost-authentication
  summary_line: oauth2/http · 2 schemes
- kind: domain-security
  name: Outpost Domain Security
  slug: outpost-domain-security
  summary_line: TLSv1.2 · DMARC
slug: outpost
tags:
- Company
- Merchant of Record
- Tax of Record
- Cross-Border Commerce
- Payments
- Tax Compliance
- E-Commerce
- VAT
- Fintech
- Invoicing
- Onboarding
website: https://outpostnow.com
---
