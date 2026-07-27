---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 16.3
  scored_at: '2026-07-27'
api_count: 7
apis:
- description: Create and manage bank accounts and their account holders through the GraphQL Partner API - open accounts, read balances and status, and access the IBAN and BIC distributed to each account. Queries in
  name: Swan Accounts API
  slug: swan-io-accounts-api
- description: Bind users to accounts and manage their permissions. Mutations include addAccountMemberships (add up to 200 memberships with a single consent), bindAccountMembership, suspendAccountMembership, and res
  name: Swan Account Memberships API
  slug: swan-io-account-memberships-api
- description: Issue and manage virtual and physical payment cards attached to account memberships. The addCards mutation adds up to 200 cards (including physical printing) with a single consent; further mutations a
  name: Swan Cards API
  slug: swan-io-cards-api
- description: Initiate and track SEPA payments. The initiateCreditTransfers mutation sends SEPA Credit Transfers, including SEPA Instant Credit Transfers via the isInstant flag; direct-debit mutations set up mandat
  name: Swan Payments API
  slug: swan-io-payments-api
- description: 'Read the transaction ledger for an account - list and filter transactions through Relay-style connections, inspect their status (Pending, Booked, Rejected, Canceled), amounts, counterparties, and the '
  name: Swan Transactions API
  slug: swan-io-transactions-api
- description: Onboard individual and company account holders before they have a session. Started against the Unauthenticated GraphQL endpoint, onboarding mutations create and update an onboarding, attach supporting
  name: Swan Onboarding API
  slug: swan-io-onboarding-api
- description: 'Read users and drive Swan''s strong-customer-authentication consent flow. Sensitive mutations (adding memberships, issuing cards, initiating payments) return a consent that the user must approve via a '
  name: Swan Users and Consents API
  slug: swan-io-users-consents-api
artifact_total: 13
collections:
- collection_type: open
  name: Swan Partner API (GraphQL)
  slug: open-swan-io
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/swan-io-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/swan-io-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/swan-io
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/swanio
- group: company
  title: ''
  type: Website
  url: https://www.swan.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.swan.io
- group: commercial
  title: ''
  type: Plans
  url: plans/swan-io-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/swan-io-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/swan-io-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.swan.io/blog
created: '2026-07-12'
description: Swan is a European embedded-banking / Banking-as-a-Service (BaaS) platform, headquartered in France, that lets companies embed accounts, IBANs, cards, and SEPA payments into their own products. Swan holds an Electronic Money Institution (EMI) license and exposes a single GraphQL API covering accounts, account holders, account memberships, IBAN management, card issuing, transactions, SEPA credit transfers and direct debits, digital onboarding, users, and consents. Integrations are backend-only, authenticated with OAuth2 (client credentials for server-to-server and authorization code for user access tokens) and scoped to a partner Project, with separate Sandbox and Live environments.
finops:
- name: Swan Io Finops
  service_category: Financial Services
  slug: swan-io-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/swan-io.png
layout: provider
modified: '2026-07-12'
name: Swan
nav: Providers
network: true
overview: 'Swan publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Account Memberships API, Cards API, and 4 more. Tagged areas include Embedded Banking, Banking as a Service, BaaS, Payments, and Accounts.


  Swan''s developer surface includes authentication, documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Swan Io Plans Pricing
  plan_count: 2
  slug: swan-io-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 1
  name: Swan Io Rate Limits
  slug: swan-io-rate-limits
score:
  band: emerging
  composite: 23.9
  delta: 2.7
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 21.7
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 21.2
  regulatory:
    applies: true
    regime: Payments
    regime_id: payments
    score: 26.1
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: authentication
  name: Swan Io Authentication
  slug: swan-io-authentication
  summary_line: oauth2/http · 3 schemes
- kind: domain-security
  name: Swan Io Domain Security
  slug: swan-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: swan-io
tags:
- Embedded Banking
- Banking as a Service
- BaaS
- Payments
- Accounts
- Cards
- IBAN
- SEPA
- Europe
- France
- Fintech
- GraphQL
website: https://www.swan.io
---
