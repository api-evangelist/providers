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
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 13.7
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: 'Paystand v3 REST API for B2B payments: create and manage payments, refunds, disputes, payers, customer banks, accounts, balances, scheduled payments, transfers and withdrawals, plus the Assurety block'
  name: Paystand Developer API
  slug: paystand-developer-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/paystand-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.paystand.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.paystand.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.paystand.com/docs/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://developers.paystand.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.paystand.com/reference/getting-started
- group: operate
  title: ''
  type: Support
  url: https://support.paystand.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.paystand.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/paystand
- group: commercial
  title: ''
  type: Pricing
  url: https://www.paystand.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.paystand.com/v2/signin
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.paystand.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.cptn.co/privacy-policy/9e569c48-09ec-4470-9690-5f41a96372a6
- group: operate
  title: ''
  type: StatusPage
  url: https://status.paystand.com
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.paystand.com
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/paystand-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/paystand-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/paystand-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/paystand-packages.yml
- group: design
  title: ''
  type: Components
  url: components/paystand-components.yml
created: '2026-07-17'
description: Paystand is a blockchain-enabled B2B payments and receivables automation platform that lets businesses send, receive, and reconcile payments with zero-fee bank-to-bank (ACH/EFT) transfers, card acceptance, and a Bitcoin-anchored "Assurety" certified audit trail. The Paystand Developer API (v3) exposes payments, refunds, disputes, payers, customer banks, accounts and balances, scheduled payments, transfers, withdrawals (including auto-withdrawal settings), a Checkout / Billing Portal embed surface, an Events resource, and the Assurety blockchain notarization APIs (assurors, chains, contracts, records, schemas, wallets). It integrates with major ERPs and e-commerce platforms (Magento, WooCommerce, BigCommerce) and is used to automate accounts receivable and payable for mid-market and enterprise finance teams.
image: https://www.paystand.com/hubfs/paystand-logo.png
layout: provider
mcp_servers:
- description: ''
  name: PayStand MCP Server
  slug: paystand-mcp-server
modified: '2026-07-20'
name: PayStand
nav: Providers
network: true
overview: 'PayStand publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payments, B2B Payments, Accounts Receivable, and Accounts Payable.


  PayStand''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 13 more developer resources.'
random_paper: 7
scopes:
- name: Paystand Scopes
  scope_count: 1
  slug: paystand-scopes
  summary_line: 1 scope · clientCredentials/authorizationCode
score:
  band: thin
  composite: 35.3
  coverage:
    artifact_dirs: 16
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 48.7
    commercial_clarity: 48.7
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 52.4
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 10.5
  previous_composite: 35.3
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 58.6
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/paystand/refs/heads/main/screenshots/paystand-2026-08-07T191655.png
security:
- kind: authentication
  name: Paystand Authentication
  slug: paystand-authentication
  summary_line: oauth2/apiKey/http · 4 schemes
- kind: domain-security
  name: Paystand Domain Security
  slug: paystand-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: paystand
tags:
- Company
- Payments
- B2B Payments
- Accounts Receivable
- Accounts Payable
- Fintech
- Blockchain
- ACH
- Billing
- Checkout
website: https://www.paystand.com
---
