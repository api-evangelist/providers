---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 11.7
  scored_at: '2026-07-28'
api_count: 2
apis:
- description: The XOTP (Paymentus payment) API exposes core Service Commerce operations — make payment (Sale), account inquiry, payment history, void/cancel payment, customer profile create/read/update/delete and l
  name: Paymentus XOTP API
  slug: paymentus-xotp-api
- description: The Authentication API issues short-lived JWT access tokens for the XOTP payment surface. A client signs a request with a pre-shared key (identified by a key id / kid and a three-letter application ac
  name: Paymentus Authentication API
  slug: paymentus-authentication-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/paymentus-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/paymentus-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.paymentus.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.paymentus.io/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.paymentus.io/docs/Reference
- group: operate
  title: ''
  type: StatusPage
  url: https://status.paymentus.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/paymentus
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/paymentus/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.paymentus.com/customer-terms-privacy/website-condition-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.paymentus.com/customer-terms-privacy/website-privacy-notice-united-states/
- group: company
  title: ''
  type: InvestorRelations
  url: https://ir.paymentus.com/
- group: company
  title: ''
  type: Blog
  url: https://www.paymentus.com/industry-insights/
- group: operate
  title: ''
  type: Support
  url: https://www.paymentus.com/contact/?form=pay
- group: build
  title: ''
  type: Packages
  url: packages/paymentus-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/paymentus-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/paymentus-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/paymentus-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/paymentus-conventions.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/paymentus-mcp.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/paymentus-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.paymentus.com/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/paymentus-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/paymentus-data-model.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/paymentus-llms.txt
created: '2026-07-24'
description: 'Paymentus (NYSE: PAY) is a Addison, Texas-based cloud billing and payment technology company founded in 2004 that operates one of the largest electronic bill presentment and payment (EBPP) networks in North America. Its Intelligent Payment Platform, Instant Payment Network (IPN), BillWallet, and Profit by Paymentus (AP/AR) products let utilities, government agencies, insurers, telecom, healthcare, higher education, and financial institutions accept and disburse payments across web, mobile, IVR, call center, and agent channels using cards, ACH/eCheck, cash, and digital wallets (PayPal, Venmo, Apple Pay, Google Pay). Its home market is the United States. Paymentus is API-native but its developer surface is access-controlled: the developer portal at developer.paymentus.io is live and public, yet the full API reference, specifications, and testing environment sit behind a request-access / NDA gate. A public Node.js Server SDK (@paymentus/core, @paymentus/auth, @paymentus/xotp)
  documents the real payment (XOTP) surface, JWT/pre-shared-key authentication, granular OAuth-style scopes, and production base URLs. No downloadable OpenAPI/Swagger specification is published on the public web as of this review.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: paymentus-mcp.yml
  slug: paymentus-mcpyml
modified: '2026-07-24'
name: Paymentus
nav: Providers
network: true
overview: 'Paymentus publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Payments, United States, Bill Payment, Electronic Bill Presentment, and Payment Processing.


  Paymentus'' developer surface includes API reference, engineering blog, support, authentication, and 20 more developer resources.'
random_paper: 50
scopes:
- name: Paymentus Scopes
  scope_count: 16
  slug: paymentus-scopes
  summary_line: 16 scopes
score:
  band: thin
  composite: 34.6
  delta: -3.0
  facets:
    commercial_clarity: 36.8
    contract_quality: 0.0
    developer_ergonomics: 41.3
    discoverability: 75.9
    governance: 12.5
    operational_transparency: 21.1
  previous_composite: 37.6
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 75.0
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Paymentus Authentication
  slug: paymentus-authentication
  summary_line: http/oauth2 · 1 scheme
- kind: domain-security
  name: Paymentus Domain Security
  slug: paymentus-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Paymentus Trust Center
  slug: paymentus-trust-center
  summary_line: SOC 2, PCI DSS, HIPAA
slug: paymentus
tags:
- Payments
- United States
- Bill Payment
- Electronic Bill Presentment
- Payment Processing
- Payment Gateway
- Disbursements
- ACH
- Real-Time Payments
- Tokenization
website: https://www.paymentus.com/
---
