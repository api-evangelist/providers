---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 102
  human_in_the_loop: 6
  name: Btcpay Agentic Access
  operation_count: 195
  slug: btcpay-agentic-access
  summary_line: 195 operations · 102 acting · 6 human-in-the-loop
api_count: 1
apis:
- baseURL: https://{btcpay-host}/api/v1
  baseurl_source: declared
  description: API Key operations
  name: BTCPay Server API Keys API
  slug: btcpay-api-keys-api
- baseURL: https://{btcpay-host}/api/v1
  baseurl_source: declared
  description: App operations
  name: BTCPay Server Apps API
  slug: btcpay-apps-api
- baseURL: https://{btcpay-host}/api/v1
  baseurl_source: declared
  description: Authorization operations
  name: BTCPay Server Authorization API
  slug: btcpay-authorization-api
- baseURL: https://{btcpay-host}/api/v1
  baseurl_source: declared
  description: Crowdfund operations
  name: BTCPay Server Crowdfund API
  slug: btcpay-crowdfund-api
- baseURL: https://{btcpay-host}/api/v1
  baseurl_source: declared
  description: File operations
  name: BTCPay Server Files API
  slug: btcpay-files-api
- baseURL: https://{btcpay-host}/api/v1
  baseurl_source: declared
  description: Health operations
  name: BTCPay Server Health API
  slug: btcpay-health-api
- baseURL: https://{btcpay-host}/api/v1
  baseurl_source: declared
  description: Invoice operations
  name: BTCPay Server Invoices API
  slug: btcpay-invoices-api
- baseURL: https://{btcpay-host}/api/v1
  baseurl_source: declared
  description: Lightning address configuration
  name: BTCPay Server Lightning address API
  slug: btcpay-lightning-address-api
- baseURL: https://{btcpay-host}/api/v1
  baseurl_source: declared
  description: Lightning (Internal Node) operations
  name: BTCPay Server Lightning (Internal Node) API
  slug: btcpay-lightning-internal-node-api
- baseURL: https://{btcpay-host}/api/v1
  baseurl_source: declared
  description: Lightning (Store) operations
  name: BTCPay Server Lightning (Store) API
  slug: btcpay-lightning-store-api
- baseURL: https://{btcpay-host}/api/v1
  baseurl_source: declared
  description: Miscelleneous operations
  name: BTCPay Server Miscelleneous API
  slug: btcpay-miscelleneous-api
- baseURL: https://{btcpay-host}/api/v1
  baseurl_source: declared
  description: Notifications operations
  name: BTCPay Server Notifications (Current User) API
  slug: btcpay-notifications-current-user-api
- baseURL: https://{btcpay-host}/api/v1
  baseurl_source: declared
  description: Payment Requests operations
  name: BTCPay Server Payment Requests API
  slug: btcpay-payment-requests-api
- baseURL: https://{btcpay-host}/api/v1
  baseurl_source: declared
  description: Payout Processors operations
  name: BTCPay Server Payout Processors API
  slug: btcpay-payout-processors-api
- baseURL: https://{btcpay-host}/api/v1
  baseurl_source: declared
  description: Point of Sale operations
  name: BTCPay Server Point of Sale API
  slug: btcpay-point-of-sale-api
- baseURL: https://{btcpay-host}/api/v1
  baseurl_source: declared
  description: Pull payments (Management) operations
  name: BTCPay Server Pull payments (Management) API
  slug: btcpay-pull-payments-management-api
- baseURL: https://{btcpay-host}/api/v1
  baseurl_source: declared
  description: Pull payments payout (Public) operations
  name: BTCPay Server Pull payments payout (Public) API
  slug: btcpay-pull-payments-payout-public-api
- baseURL: https://{btcpay-host}/api/v1
  baseurl_source: declared
  description: Pull payments (Public) operations
  name: BTCPay Server Pull payments (Public) API
  slug: btcpay-pull-payments-public-api
- baseURL: https://{btcpay-host}/api/v1
  baseurl_source: declared
  description: Server Email Settings operations
  name: BTCPay Server ServerEmail API
  slug: btcpay-serveremail-api
- baseURL: https://{btcpay-host}/api/v1
  baseurl_source: declared
  description: Store Payment Methods operations
  name: BTCPay Server Store (Payment Methods) API
  slug: btcpay-store-payment-methods-api
- baseURL: https://{btcpay-host}/api/v1
  baseurl_source: declared
  description: Store Wallet (On Chain) operations
  name: BTCPay Server Store Wallet (On Chain) API
  slug: btcpay-store-wallet-on-chain-api
- baseURL: https://{btcpay-host}/api/v1
  baseurl_source: declared
  description: Store operations
  name: BTCPay Server Stores API
  slug: btcpay-stores-api
- baseURL: https://{btcpay-host}/api/v1
  baseurl_source: declared
  description: Store Emails operations
  name: BTCPay Server Stores (Email) API
  slug: btcpay-stores-email-api
- baseURL: https://{btcpay-host}/api/v1
  baseurl_source: declared
  description: Stores (Payout Processors) operations
  name: BTCPay Server Stores (Payout Processors) API
  slug: btcpay-stores-payout-processors-api
- baseURL: https://{btcpay-host}/api/v1
  baseurl_source: declared
  description: Store pull payment payout operations
  name: BTCPay Server Stores (Payouts) API
  slug: btcpay-stores-payouts-api
- baseURL: https://{btcpay-host}/api/v1
  baseurl_source: declared
  description: Stores rate information and configuration
  name: BTCPay Server Stores (Rates) API
  slug: btcpay-stores-rates-api
- baseURL: https://{btcpay-host}/api/v1
  baseurl_source: declared
  description: Store Users operations
  name: BTCPay Server Stores (Users) API
  slug: btcpay-stores-users-api
- baseURL: https://{btcpay-host}/api/v1
  baseurl_source: declared
  description: Subscription operations
  name: BTCPay Server Subscriptions API
  slug: btcpay-subscriptions-api
- baseURL: https://{btcpay-host}/api/v1
  baseurl_source: declared
  description: User operations
  name: BTCPay Server Users API
  slug: btcpay-users-api
- baseURL: https://{btcpay-host}/api/v1
  baseurl_source: declared
  description: Webhook operations
  name: BTCPay Server Webhooks API
  slug: btcpay-webhooks-api
- baseURL: https://{btcpay-host}/api/v1
  baseurl_source: declared
  description: Store report operations
  name: BTCPay Server Reports API
  slug: btcpay-reports-api
- baseURL: https://{btcpay-host}/api/v1
  baseurl_source: declared
  description: Server Info operations
  name: BTCPay Server Server Info API
  slug: btcpay-server-info-api
artifact_total: 70
collections:
- collection_type: open
  name: BTCPay Greenfield API Keys API
  slug: open-btcpay-api-keys-api
- collection_type: open
  name: BTCPay Greenfield API Keys Apps API
  slug: open-btcpay-apps-api
- collection_type: open
  name: BTCPay Greenfield API Keys Authorization API
  slug: open-btcpay-authorization-api
- collection_type: open
  name: BTCPay Greenfield API Keys Crowdfund API
  slug: open-btcpay-crowdfund-api
- collection_type: open
  name: BTCPay Greenfield API Keys Files API
  slug: open-btcpay-files-api
- collection_type: open
  name: BTCPay Greenfield API Keys Health API
  slug: open-btcpay-health-api
- collection_type: open
  name: BTCPay Greenfield API Keys Invoices API
  slug: open-btcpay-invoices-api
- collection_type: open
  name: BTCPay Greenfield API Keys Lightning address API
  slug: open-btcpay-lightning-address-api
- collection_type: open
  name: BTCPay Greenfield API Keys Lightning (Internal Node) API
  slug: open-btcpay-lightning-internal-node-api
- collection_type: open
  name: BTCPay Greenfield API Keys Lightning (Store) API
  slug: open-btcpay-lightning-store-api
- collection_type: open
  name: BTCPay Greenfield API Keys Miscelleneous API
  slug: open-btcpay-miscelleneous-api
- collection_type: open
  name: BTCPay Greenfield API Keys Notifications (Current User) API
  slug: open-btcpay-notifications-current-user-api
- collection_type: open
  name: BTCPay Greenfield API Keys Payment Requests API
  slug: open-btcpay-payment-requests-api
- collection_type: open
  name: BTCPay Greenfield API Keys Payout Processors API
  slug: open-btcpay-payout-processors-api
- collection_type: open
  name: BTCPay Greenfield API Keys Point of Sale API
  slug: open-btcpay-point-of-sale-api
- collection_type: open
  name: BTCPay Greenfield API Keys Pull payments (Management) API
  slug: open-btcpay-pull-payments-management-api
- collection_type: open
  name: BTCPay Greenfield API Keys Pull payments payout (Public) API
  slug: open-btcpay-pull-payments-payout-public-api
- collection_type: open
  name: BTCPay Greenfield API Keys Pull payments (Public) API
  slug: open-btcpay-pull-payments-public-api
- collection_type: open
  name: BTCPay Greenfield API Keys ServerEmail API
  slug: open-btcpay-serveremail-api
- collection_type: open
  name: BTCPay Greenfield API Keys ServerInfo API
  slug: open-btcpay-serverinfo-api
- collection_type: open
  name: BTCPay Greenfield API Keys Store (Payment Methods) API
  slug: open-btcpay-store-payment-methods-api
- collection_type: open
  name: BTCPay Greenfield API Keys Store Wallet (On Chain) API
  slug: open-btcpay-store-wallet-on-chain-api
- collection_type: open
  name: BTCPay Greenfield API Keys Stores API
  slug: open-btcpay-stores-api
- collection_type: open
  name: BTCPay Greenfield API Keys Stores (Email) API
  slug: open-btcpay-stores-email-api
- collection_type: open
  name: BTCPay Greenfield API Keys Stores (Payout Processors) API
  slug: open-btcpay-stores-payout-processors-api
- collection_type: open
  name: BTCPay Greenfield API Keys Stores (Payouts) API
  slug: open-btcpay-stores-payouts-api
- collection_type: open
  name: BTCPay Greenfield API Keys Stores (Rates) API
  slug: open-btcpay-stores-rates-api
- collection_type: open
  name: BTCPay Greenfield API Keys Stores (Users) API
  slug: open-btcpay-stores-users-api
- collection_type: open
  name: BTCPay Greenfield API Keys Subscriptions API
  slug: open-btcpay-subscriptions-api
- collection_type: open
  name: BTCPay Greenfield API Keys Users API
  slug: open-btcpay-users-api
- collection_type: open
  name: BTCPay Greenfield API Keys Webhooks API
  slug: open-btcpay-webhooks-api
common:
- group: commercial
  href: https://artifacts.apis.io/btcpay/plans/plans.yml
  title: ''
  type: Plans
  url: plans/plans.yml
- group: operate
  href: https://artifacts.apis.io/btcpay/rate-limits/rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/btcpay/finops/finops.yml
  title: ''
  type: FinOps
  url: finops/finops.yml
- group: other
  href: https://artifacts.apis.io/btcpay/capabilities/btcpay-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/btcpay-capability-edges.yml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/btcpayserver/btcpayserver/issues
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/btcpayserver/btcpayserver/blob/master/SECURITY.md
- group: agent
  href: https://artifacts.apis.io/btcpay/agentic-access/btcpay-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/btcpay-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/btcpay/security/btcpay-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/btcpay-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/btcpay/authentication/btcpay-authentication.yml
  title: ''
  type: Authentication
  url: authentication/btcpay-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://btcpayserver.org
- group: docs
  title: ''
  type: Documentation
  url: https://docs.btcpayserver.org
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/btcpayserver
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/btcpayserver/btcpayserver
- group: company
  title: ''
  type: Blog
  url: https://blog.btcpayserver.org
- group: other
  title: ''
  type: Mattermost
  url: https://chat.btcpayserver.org/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/btcpayserver
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/c/BTCPayServer
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/btcpayserver/btcpayserver/releases
- group: operate
  title: ''
  type: StatusPage
  url: https://status.btcpayserver.org
- group: operate
  title: ''
  type: Support
  url: https://docs.btcpayserver.org/Support/
- group: commercial
  title: ''
  type: License
  url: https://github.com/btcpayserver/btcpayserver/blob/master/LICENSE
- group: other
  title: ''
  type: Contributing
  url: https://github.com/btcpayserver/btcpayserver/blob/master/CONTRIBUTING.md
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://btcpayserver.org/privacy-policy/
created: '2026-06-13'
description: BTCPay Server is a self-hosted, open-source Bitcoin and cryptocurrency payment processor with a comprehensive REST API (Greenfield API v1) for managing stores, invoices, wallets, Lightning Network nodes, payment requests, pull payments, webhooks, users, and server configuration. It operates with zero fees, no third-party dependency, and is released under the MIT license.
finops:
- has_sources: false
  method: generated
  name: Finops
  primary_unit: ''
  service_category: ''
  slug: finops
  template: true
image: https://btcpayserver.org/images/btcpay-logo.svg
layout: provider
modified: '2026-06-13'
name: BTCPay Server
nav: Providers
network: true
overview: 'BTCPay Server publishes 32 API contracts indexed on the [APIs.io](https://apis.io/) network, including API Keys API, Apps API, Authorization API, and 29 more. Tagged areas include Bitcoin, Cryptocurrency, Payments, Lightning Network, and Open Source.


  The BTCPay Server catalog on APIs.io includes 1 Spectral governance ruleset.


  BTCPay Server''s developer surface includes authentication, documentation, engineering blog, YouTube channel, changelog, support, and 17 more developer resources.'
plans:
- name: Plans
  plan_count: 2
  slug: plans
random_paper: 19
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
rules:
- authorship: generated
  effective_rule_count: 109
  extends:
  - spectral:oas
  name: BTCPay Server API Rules
  rule_count: 68
  severity_counts:
    error: 47
    hint: 0
    info: 6
    warn: 15
  slug: btcpay-rules
score:
  band: thin
  composite: 38.3
  coverage:
    artifact_dirs: 19
    catalog_earned: 48.0
    catalog_earned_first_party: 0.0
    catalog_gap: 67.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.6
  facets:
    access_clarity: 5.3
    contract_governance: 27.3
    contract_quality: 53.9
    developer_ergonomics: 28.6
    discoverability: 66.1
    operational_transparency: 36.8
  open_source:
    applies: true
    score: 60.0
  previous_composite: 37.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 50.0
      total: 64
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 15.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 22.2
screenshot: https://apis.io/screenshots/btcpay/btcpay-2026-06-20T173732.png
security:
- kind: authentication
  name: Btcpay Authentication
  slug: btcpay-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Btcpay Domain Security
  slug: btcpay-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: btcpay
tags:
- Bitcoin
- Cryptocurrency
- Payments
- Lightning Network
- Open Source
- Self-Hosted
website: https://btcpayserver.org
---
