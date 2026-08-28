---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.1
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 88
  human_in_the_loop: 1
  name: Monoova Agentic Access
  operation_count: 150
  slug: monoova-agentic-access
  summary_line: 150 operations · 88 acting · 1 human-in-the-loop
api_count: 3
apis:
- description: Monoova's core Payments API (v5.29) to receive, manage, and pay AUD across all Australian payment rails - real-time transfers via NPP/Osko, direct credit and direct debit, BPAY, card payments, and Pay
  name: Monoova Payments API
  slug: monoova-payments-api
- description: Monoova's PayTo API (v1) for the New Payments Platform's mandated account-to-account debit service - create and manage payment agreements (mandates), initiate payments against them, handle mandate and
  name: Monoova PayTo API
  slug: monoova-payto-api
- description: Monoova's Card Payments API (v1) for accepting card payments, including tokenised card flows and webhook notifications for payment events. Authenticated with short-lived (24h) Bearer tokens obtained v
  name: Monoova Card Payments API
  slug: monoova-card-payments-api
artifact_total: 12
asyncapis:
- description: ''
  name: Monoova Webhooks
  slug: monoova-webhooks
collections:
- collection_type: open
  name: Monoova Card Payments API
  slug: open-monoova-cc
- collection_type: open
  name: Monoova Payments API
  slug: open-monoova-payments
- collection_type: open
  name: Monoova PayTo API
  slug: open-monoova-payto
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/monoova-cc-overlay.yaml
- group: auth
  title: ''
  type: TrustCenter
  url: security/monoova-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/monoova-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/monoova-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/monoova-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.monoova.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.monoova.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.monoova.com/
- group: docs
  title: ''
  type: APIReference
  url: https://api-docs.monoova.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.monoova.com/getting-started
- group: auth
  title: ''
  type: Authentication
  url: https://developer.monoova.com/authentication
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/monoova/monoova-api
- group: operate
  title: ''
  type: StatusPage
  url: https://monoova.statuspage.io
- group: company
  title: ''
  type: Blog
  url: https://www.monoova.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/monoova
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/monoova
- group: start
  title: ''
  type: SignUp
  url: https://sandbox.monoova.com/
- group: operate
  title: ''
  type: Support
  url: https://www.monoova.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.monoova.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.monoova.com/privacy-policy
- group: auth
  title: ''
  type: Security
  url: https://www.monoova.com/security
- group: build
  title: ''
  type: Packages
  url: packages/monoova-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/monoova-packages.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/monoova-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/monoova-lifecycle.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/monoova-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/monoova-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/monoova-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/monoova-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.monoova.com/security
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/monoova-problem-types.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/monoova-decline-codes.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/monoova-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/monoova-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/monoova-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/monoova-components.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/monoova-well-known.yml
created: '2026-07-24'
description: 'Monoova is an Australian payments platform that lets businesses receive, manage, and pay funds in AUD across every domestic rail through a single set of RESTful JSON APIs. Operated by Monoova Global Payments Pty Ltd (AFSL 421414) and enrolled with AUSTRAC, it connects directly to the New Payments Platform (real-time account-to-account transfers via NPP/Osko, PayID addressing, and PayTo mandated debits) alongside BPAY, direct entry (credit/debit), card acquiring, and Apple Pay / Google Pay. Its Automatcher reconciliation engine, virtual mAccount/mWallet hierarchies, Confirmation of Payee, account verification, payment tokenisation, and webhook-driven reporting target fintechs, marketplaces, payroll, lending, remittance, and SaaS businesses (customers include Wise, Nium, Finder, and Sharesies). Monoova is genuinely API-first: it ships a public developer portal, a Redoc API reference, downloadable OpenAPI specifications, and a public Postman workspace, plus a free self-serve sandbox.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: Monoova MCP Server
  slug: monoova-mcp-server
modified: '2026-07-24'
name: Monoova
nav: Providers
network: true
overview: 'Monoova publishes 3 APIs on the [APIs.io](https://apis.io/) network: Payments API, PayTo API, and Card Payments API. Tagged areas include Payments, Australia, Real-Time Payments, NPP, and PayTo.


  The Monoova catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Monoova''s developer surface includes authentication, documentation, API reference, getting-started guide, engineering blog, signup flow, support, and 31 more developer resources.'
random_paper: 11
score:
  band: strong
  composite: 57.2
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 16.7
    contract_quality: 66.8
    developer_ergonomics: 66.1
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 36.8
  previous_composite: 57.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 65.6
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/monoova/refs/heads/main/screenshots/monoova-2026-08-07T184216.png
security:
- kind: authentication
  name: Monoova Authentication
  slug: monoova-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Monoova Domain Security
  slug: monoova-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Monoova Trust Center
  slug: monoova-trust-center
  summary_line: SOC 2, PCI DSS
slug: monoova
tags:
- Payments
- Australia
- Real-Time Payments
- NPP
- PayTo
- PayID
- Account-to-Account
- BPAY
- Card Payments
- Money Movement
- Virtual Accounts
- Cross-Border
website: https://www.monoova.com/
---
