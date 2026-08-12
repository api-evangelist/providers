---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: verified
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 57.9
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 28
  human_in_the_loop: 1
  name: Airtm Agentic Access
  operation_count: 69
  slug: airtm-agentic-access
  summary_line: 69 operations · 28 acting · 1 human-in-the-loop
api_count: 24
apis:
- description: The OAuth 2.0 resource server that lets a partner application move USDC in and out of an individual Airtm user's wallet on that user's behalf, read the wallet balance, and check KYC status. Authorized
  name: Airtm Wallet Resource (Connect) API
  slug: airtm-wallet-resource-connect-api
- description: '## Overview The Account Status endpoint enables your organization to verify recipient account information before initiating payments. This powerful verification tool helps prevent payment failures, re'
  name: Airtm Account Status API
  slug: airtm-account-status-api
- description: The ApiKeys API from Airtm — 3 operation(s) for apikeys.
  name: Airtm API Keys API
  slug: airtm-apikeys-api
- description: '## Overview Bulk Payments enable your organization to process multiple payouts simultaneously through a single API operation. This powerful feature is designed for businesses that need to send payment'
  name: Airtm Bulk Payments API
  slug: airtm-bulk-payments-api
- description: '# Bulk Payouts Process multiple payouts efficiently in a single batch operation. Ideal for payroll, affiliate payments, or mass distributions. ## Overview Bulk payouts allow you to submit hundreds or '
  name: Airtm Bulk Payouts API
  slug: airtm-bulk-payouts-api
- description: '# Deposits The Deposits API provides comprehensive tracking and management of funding transactions for your Airtm Enterprise account. This endpoint enables you to monitor incoming funds, track deposit'
  name: Airtm Deposits API
  slug: airtm-deposits-api
- description: The Embedded Catalog API from Airtm — 1 operation(s) for embedded catalog.
  name: Airtm Embedded Catalog API
  slug: airtm-embedded-catalog-api
- description: The Embedded Quotes API from Airtm — 1 operation(s) for embedded quotes.
  name: Airtm Embedded Quotes API
  slug: airtm-embedded-quotes-api
- description: The Embedded Receivers API from Airtm — 4 operation(s) for embedded receivers.
  name: Airtm Embedded Receivers API
  slug: airtm-embedded-receivers-api
- description: The Embedded Senders API from Airtm — 2 operation(s) for embedded senders.
  name: Airtm Embedded Senders API
  slug: airtm-embedded-senders-api
- description: The Embedded Transactions API from Airtm — 2 operation(s) for embedded transactions.
  name: Airtm Embedded Transactions API
  slug: airtm-embedded-transactions-api
- description: '# External Bank Account The external bank account API provides the capability to register an external bank account where you can withdraw your funds to.'
  name: Airtm External Bank Account API
  slug: airtm-external-bank-account-api
- description: '# External Crypto Account The external crypto account API provides the capability to register an external crypto account where you can withdraw your funds to.'
  name: Airtm External Crypto Account API
  slug: airtm-external-crypto-account-api
- description: '# Account Management The Account Management API provides essential information about your Airtm Enterprise account, including account details, balance information, and configuration settings. This end'
  name: Airtm Me API
  slug: airtm-me-api
- description: '## Overview The Operations endpoint serves as the central hub for tracking all transaction-related activities within the Airtm Enterprise ecosystem. This comprehensive endpoint consolidates informatio'
  name: Airtm Operations API
  slug: airtm-operations-api
- description: '## Overview The Partner endpoint provides essential information about your Airtm Enterprise account, including account details, configuration settings, balance information, and operational status. Thi'
  name: Airtm Partner API
  slug: airtm-partner-api
- description: '# Payins The Payins API enables you to collect payments from users worldwide through their Airtm accounts. This is ideal for e-commerce platforms, service providers, and any business that needs to acc'
  name: Airtm Payins API
  slug: airtm-payins-api
- description: '## Overview The Payouts endpoint enables your organization to send payments to recipients worldwide through the Airtm platform. This powerful endpoint supports both individual and bulk payment process'
  name: Airtm Payments / Payouts API
  slug: airtm-payments-payouts-api
- description: '# Payouts Send money to recipients worldwide through their Airtm accounts. Payouts use a secure two-step process to prevent accidental payments. ## How Payouts Work ### Two-Step Process 1. **Create** '
  name: Airtm Payouts API
  slug: airtm-payouts-api
- description: '## Overview The Payins endpoint (also known as Purchases) enables your organization to accept payments from users for products, services, or any other transactions. This endpoint is essential for e-co'
  name: Airtm Purchases / Payins API
  slug: airtm-purchases-payins-api
- description: '# Reports Generate detailed financial reports for your Airtm Enterprise account. Reports provide transaction data, audit trails, and downloadable CSV files for accounting and compliance. ## How Report'
  name: Airtm Reports API
  slug: airtm-reports-api
- description: '# Users The Users API provides essential user management capabilities for your Airtm Enterprise integration. This endpoint allows you to verify recipient information, check account status, and ensure '
  name: Airtm Users API
  slug: airtm-users-api
- description: Webhooks are how services notify each other of events. At their core they are just a POST request to a pre-determined endpoint. The endpoint can be whatever you want, and you can just add them from th
  name: Airtm Webhooks API
  slug: airtm-webhooks-api
- description: '# Withdrawals The withdrawals API provides the capability to withdraw your funds to a previously registered external account (Bank or Crypto)'
  name: Airtm Withdrawals API
  slug: airtm-withdrawals-api
artifact_total: 32
asyncapis:
- description: ''
  name: Airtm Webhooks
  slug: airtm-webhooks
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/airtm-enterprise-v1-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.airtm.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.airtm.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.airtm.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.airtm.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://help.airtm.com/en/support/solutions/folders/47000770266
- group: operate
  title: ''
  type: Support
  url: https://help.airtm.com/en/support/home
- group: company
  title: ''
  type: Blog
  url: https://www.airtm.com/en/blog/
- group: start
  title: ''
  type: SignUp
  url: https://www.airtm.com/en/select-account/
- group: start
  title: ''
  type: Login
  url: https://app.airtm.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.airtm.com/en/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.airtm.com/en/terms-and-conditions/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.airtm.com/
- group: auth
  title: ''
  type: TrustCenter
  url: security/airtm-trust-center.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/airtm-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/airtm-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/airtm-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/airtm-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/airtm-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/airtm-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/airtm-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/airtm-error-codes.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/airtm-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/airtm-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/airtm-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/airtm-packages.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/airtm-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/airtm-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/airtm-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/airtm-webhooks.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/airtm-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/airtm-security.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/airtm-llms.txt
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/airtm-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/airtm-agentic-access.yml
- group: auth
  title: ''
  type: Security
  url: https://www.airtm.com/.well-known/security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/airtm-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/airtm-domain-security.yml
created: '2026-08-06'
description: 'Airtm is a US-registered (Airtm Inc., Delaware; FinCEN MSB #31000329787639) digital dollar wallet and cross-border payments network operating since 2015, built for freelancers, remote workers, contractors and businesses in emerging markets. Balances are held as USDC on Stellar and can be moved in and out through 500+ local payment methods, a US virtual account with ACH details, a USD virtual card, and peer-to-peer transfer. For businesses, Airtm publishes the Enterprise Payments API — a REST API for programmatic payouts to recipients in 190+ countries, hosted-checkout payins, bulk payouts, external bank and crypto accounts, withdrawals and reporting — plus an OAuth 2.0 / OIDC authorization server and a Wallet Resource (Connect) API that lets a partner application move value in and out of an individual user''s Airtm wallet on that user''s behalf.'
image: https://app.airtm.com/favicon.ico
layout: provider
modified: '2026-08-06'
name: Airtm
nav: Providers
network: true
overview: 'Airtm publishes 23 APIs on the [APIs.io](https://apis.io/) network, including Account Status API, API Keys API, Bulk Payments API, and 20 more. Tagged areas include payments, payouts, cross-border-payments, fintech, and digital-wallet.


  The Airtm catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Airtm''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, changelog, and 32 more developer resources.'
random_paper: 77
rate_limits:
- limit_count: 1
  name: Airtm Rate Limits
  slug: airtm-rate-limits
scopes:
- name: Airtm Scopes
  scope_count: 8
  slug: airtm-scopes
  summary_line: 8 scopes · authorizationCode/clientCredentials/refreshToken
score:
  band: strong
  composite: 60.4
  delta: 0.8
  facets:
    commercial_clarity: 42.1
    contract_quality: 69.6
    developer_ergonomics: 66.8
    discoverability: 74.1
    governance: 20.8
    operational_transparency: 71.1
  previous_composite: 59.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 23
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 71.9
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/airtm/refs/heads/main/screenshots/airtm-2026-08-07T161117.png
security:
- kind: authentication
  name: Airtm Authentication
  slug: airtm-authentication
  summary_line: http/oauth2/openIdConnect · 3 schemes
- kind: domain-security
  name: Airtm Domain Security
  slug: airtm-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Airtm Vulnerability Disclosure
  slug: airtm-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Airtm Trust Center
  slug: airtm-trust-center
  summary_line: trust center published
slug: airtm
tags:
- payments
- payouts
- cross-border-payments
- fintech
- digital-wallet
- stablecoin
- usdc
- stellar
- mass-payouts
- remittances
- latin-america
- emerging-markets
- money-services-business
- oauth2
- openid-connect
website: https://www.airtm.com/
---
