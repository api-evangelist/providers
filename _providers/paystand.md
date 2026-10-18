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
    agent_skills: false
    agentic_access: derived
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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 35.2
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Paystand Agentic Access
  operation_count: 12
  slug: paystand-agentic-access
  summary_line: 12 operations · 7 acting
api_count: 2
apis:
- description: 'Paystand v3 REST API for B2B payments: create and manage payments, refunds, disputes, payers, customer banks, accounts, balances, scheduled payments, transfers and withdrawals, plus the Assurety block'
  name: Paystand Developer API
  slug: paystand-developer-api
- baseURL: https://api.paystand.com/v3
  baseurl_source: declared
  description: The Balances API from PayStand — 2 operation(s) for balances.
  name: PayStand Balances API
  slug: paystand-balances-api
- baseURL: https://api.paystand.com/v3
  baseurl_source: declared
  description: The Banks API from PayStand — 1 operation(s) for banks.
  name: PayStand Banks API
  slug: paystand-banks-api
- baseURL: https://api.paystand.com/v3
  baseurl_source: declared
  description: The Oauth API from PayStand — 1 operation(s) for oauth.
  name: PayStand OAuth API
  slug: paystand-oauth-api
- baseURL: https://api.paystand.com/v3
  baseurl_source: declared
  description: The Payers API from PayStand — 1 operation(s) for payers.
  name: PayStand Payers API
  slug: paystand-payers-api
- baseURL: https://api.paystand.com/v3
  baseurl_source: declared
  description: The Payments API from PayStand — 2 operation(s) for payments.
  name: PayStand Payments API
  slug: paystand-payments-api
- baseURL: https://api.paystand.com/v3
  baseurl_source: declared
  description: The Refunds API from PayStand — 1 operation(s) for refunds.
  name: PayStand Refunds API
  slug: paystand-refunds-api
- baseURL: https://api.paystand.com/v3
  baseurl_source: declared
  description: The Transfers API from PayStand — 1 operation(s) for transfers.
  name: PayStand Transfers API
  slug: paystand-transfers-api
- baseURL: https://api.paystand.com/v3
  baseurl_source: declared
  description: The Withdrawals API from PayStand — 3 operation(s) for withdrawals.
  name: PayStand Withdrawals API
  slug: paystand-withdrawals-api
artifact_total: 14
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/paystand/refs/heads/main/agentic-access/paystand-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/paystand-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/paystand/refs/heads/main/rules/paystand-rules.yml
  title: ''
  type: Spectral
  url: rules/paystand-rules.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/paystand/refs/heads/main/lifecycle/paystand-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/paystand-lifecycle.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/paystand/refs/heads/main/hosts/paystand-hosts.yml
  title: ''
  type: Hosts
  url: hosts/paystand-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/paystand/refs/heads/main/vendors/paystand-vendors.yml
  title: ''
  type: Vendors
  url: vendors/paystand-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.paystand.com/press
- group: company
  title: ''
  type: BlogRSS
  url: https://www.paystand.com/blog/rss.xml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/paystand/refs/heads/main/security/paystand-domain-security.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/paystand/refs/heads/main/llms/paystand-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/paystand-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/paystand/refs/heads/main/well-known/paystand-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/paystand-well-known.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/paystand/refs/heads/main/packages/paystand-packages.yml
  title: ''
  type: Packages
  url: packages/paystand-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/paystand/refs/heads/main/packages/paystand-packages.yml
  title: ''
  type: SDKs
  url: packages/paystand-packages.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/paystand/refs/heads/main/components/paystand-components.yml
  title: ''
  type: Components
  url: components/paystand-components.yml
created: '2026-07-17'
description: Paystand is a blockchain-enabled B2B payments and receivables automation platform that lets businesses send, receive, and reconcile payments with zero-fee bank-to-bank (ACH/EFT) transfers, card acceptance, and a Bitcoin-anchored "Assurety" certified audit trail. The Paystand Developer API (v3) exposes payments, refunds, disputes, payers, customer banks, accounts and balances, scheduled payments, transfers, withdrawals (including auto-withdrawal settings), a Checkout / Billing Portal embed surface, an Events resource, and the Assurety blockchain notarization APIs (assurors, chains, contracts, records, schemas, wallets). It integrates with major ERPs and e-commerce platforms (Magento, WooCommerce, BigCommerce) and is used to automate accounts receivable and payable for mid-market and enterprise finance teams.
image: https://www.paystand.com/hubfs/paystand-logo.png
layout: provider
modified: '2026-10-06'
name: PayStand
nav: Providers
network: true
overview: 'PayStand publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Balances API, Banks API, OAuth API, and 6 more. Tagged areas include Company, Payments, B2B Payments, Accounts Receivable, and Accounts Payable.


  The PayStand catalog on APIs.io includes 1 Spectral governance ruleset.


  PayStand''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 20 more developer resources.'
random_paper: 10
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: PayStand API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: paystand-rules
scopes:
- name: Paystand Scopes
  scope_count: 1
  slug: paystand-scopes
  summary_line: 1 scope · clientCredentials/authorizationCode
score:
  band: developing
  composite: 47.0
  coverage:
    artifact_dirs: 23
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 13.8
  facets:
    access_clarity: 48.7
    contract_governance: 31.8
    contract_quality: 46.8
    developer_ergonomics: 52.4
    discoverability: 75.0
    operational_transparency: 18.4
  previous_composite: 33.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 8
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 33.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: rising
  upsert:
    applies: true
    score: 0.0
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
