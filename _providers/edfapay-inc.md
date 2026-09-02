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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.0
  scored_at: '2026-09-01'
api_count: 2
apis:
- description: Branch Management APIs
  name: EdfaPay, Inc. Branch Management API
  slug: edfapay-inc-branch-management-api
- description: Merchant Management APIs
  name: EdfaPay, Inc. Merchant Management API
  slug: edfapay-inc-merchant-management-api
- description: Partner Management APIs
  name: EdfaPay, Inc. Partner Management API
  slug: edfapay-inc-partner-management-api
- description: The Payment API from EdfaPay, Inc. — 1 operation(s) for payment.
  name: EdfaPay, Inc. Payment API
  slug: edfapay-inc-payment-api
- description: Role Management APIs
  name: EdfaPay, Inc. Role Management API
  slug: edfapay-inc-role-management-api
- description: Transaction Management APIs
  name: EdfaPay, Inc. Transaction Management API
  slug: edfapay-inc-transaction-management-api
- description: User Management APIs
  name: EdfaPay, Inc. User Management API
  slug: edfapay-inc-user-management-api
artifact_total: 20
asyncapis:
- description: ''
  name: Edfapay Inc Webhooks
  slug: edfapay-inc-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Edfapay Payment Gateway Branch Management API
  slug: open-edfapay-inc-branch-management-api
- collection_type: open
  name: Edfapay Payment Gateway Branch Management Merchant Management API
  slug: open-edfapay-inc-merchant-management-api
- collection_type: open
  name: Edfapay Payment Gateway Branch Management Partner Management API
  slug: open-edfapay-inc-partner-management-api
- collection_type: open
  name: Edfapay Gateway Branch Management Payment API
  slug: open-edfapay-inc-payment-api
- collection_type: open
  name: Edfapay Payment Gateway Branch Management Role Management API
  slug: open-edfapay-inc-role-management-api
- collection_type: open
  name: Edfapay Payment Gateway Branch Management Transaction Management API
  slug: open-edfapay-inc-transaction-management-api
- collection_type: open
  name: Edfapay Payment Gateway Branch Management User Management API
  slug: open-edfapay-inc-user-management-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/edfapay-inc-revamp-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://edfapay.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://edfapay.com/developers/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.edfapay.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.edfapay.com/v2.0/reference/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.edfapay.com/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://edfapay.com/new-technical/
- group: company
  title: ''
  type: Blog
  url: https://edfapay.com/our-blog/
- group: start
  title: ''
  type: SignUp
  url: https://app.edfapay.com/sign-up/
- group: start
  title: ''
  type: Login
  url: https://app.edfapay.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://edfapay.com/terms_conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://edfapay.com/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/edfapay
- group: build
  title: ''
  type: Postman
  url: https://documenter.getpostman.com/view/21813149/2s9Y5SX6Xs
- group: build
  title: ''
  type: SDKs
  url: packages/edfapay-inc-packages.yml
- group: build
  title: ''
  type: Packages
  url: packages/edfapay-inc-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/edfapay-inc-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/edfapay-inc-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/edfapay-inc-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/edfapay-inc-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/edfapay-inc-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/edfapay-inc-conformance.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/edfapay-inc-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/edfapay-inc-domain-security.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/edfapay-inc-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/edfapay-inc-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/edfapay-inc-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/edfapay-inc-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/edfapay-inc-webhooks.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/edfapay-inc-problem-types.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/edfapay-inc-decline-codes.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: EdfaPay is a Saudi fintech and payment-technology company offering a developer-friendly payment platform across the GCC region. Its products include a hosted Checkout and Server-to-Server (S2S) payment gateway, SoftPOS tap-to-pay technology that turns mobile devices into card readers, merchant onboarding, payouts, e-invoicing, and white-label solutions for banks and partners. The gateway supports Visa, Mastercard, MADA, Apple Pay and STC Pay with 3D Secure, webhooks, refunds and recurring payments, on PCI-DSS certified infrastructure. EdfaPay was added to the API Evangelist network as a portfolio company of 500 Global and enriched from its public developer documentation, OpenAPI definitions and SDKs.
image: https://files.readme.io/89700fae642aef272b5162ed82daf2f2ececcb418693c2307830e1a0e3f7fa2e-EdfaPay-Logo.svg
layout: provider
mcp_servers:
- description: ''
  name: EdfaPay, Inc. MCP Server
  slug: edfapay-inc-mcp-server
modified: '2026-07-19'
name: EdfaPay, Inc.
nav: Providers
network: true
overview: 'EdfaPay, Inc. publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Branch Management API, Merchant Management API, Partner Management API, and 4 more. Tagged areas include Company, Payments, Payment Gateway, Fintech, and SoftPOS.


  The EdfaPay, Inc. catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  EdfaPay, Inc.''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, authentication, and 25 more developer resources.'
random_paper: 18
score:
  band: developing
  composite: 53.3
  coverage:
    artifact_dirs: 20
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.2
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 18.2
    contract_quality: 61.2
    developer_ergonomics: 63.7
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 10.5
  previous_composite: 53.5
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 68.8
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/edfapay-inc/refs/heads/main/screenshots/edfapay-inc-2026-07-25T212824.png
security:
- kind: authentication
  name: Edfapay Inc Authentication
  slug: edfapay-inc-authentication
  summary_line: apiKey/signature · 2 schemes
- kind: domain-security
  name: Edfapay Inc Domain Security
  slug: edfapay-inc-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Edfapay Inc Trust Center
  slug: edfapay-inc-trust-center
  summary_line: PCI DSS
slug: edfapay-inc
tags:
- Company
- Payments
- Payment Gateway
- Fintech
- SoftPOS
- Apple Pay
- Saudi Arabia
- Merchant Onboarding
website: https://edfapay.com
---
