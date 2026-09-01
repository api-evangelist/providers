---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
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
  score: 0.0
  scored_at: '2026-09-01'
api_count: 10
apis:
- description: Institutional payment initiation product listed in M&T's Banking and Treasury API group on the developer portal. Per-product reference is available after Entra login and Azure APIM subscription.
  name: Payment Initiation API
  slug: payment-initiation
- description: Payment status lookup product in the Banking and Treasury API group. Reference gated behind portal authentication.
  name: Payment Status API
  slug: payment-status
- description: Cash activity reporting product in the Banking and Treasury API group for treasury-management clients. Reference gated behind portal authentication.
  name: Cash Activity API
  slug: cash-activity
- description: Cash projection / forecasting product in the Banking and Treasury API group. Reference gated behind portal authentication.
  name: Cash Projection API
  slug: cash-projection
- description: Pending transactions reporting product in the Banking and Treasury API group. Reference gated behind portal authentication.
  name: Pending Transactions API
  slug: pending-transactions
- description: Event notification setup and subscription product enabling callback/webhook delivery with request signing, listed in the Banking and Treasury API group. Reference gated behind portal authentication.
  name: Event Notification API
  slug: event-notification
- description: Wilmington Trust custody end-of-day product for institutional clients, listed in the portal's Custody API group. Reference gated behind portal authentication.
  name: Custody End of Day API
  slug: custody-end-of-day
- description: Fund valuation and accounting product (transfer-agency / fund-administration services) in the Custody API group. Reference gated behind portal authentication.
  name: Fund Accounting API
  slug: fund-accounting
- description: Account valuations product supporting custody and institutional portfolio reporting. Reference gated behind portal authentication.
  name: Account Valuations API
  slug: account-valuations
- description: Position exposure product for institutional custody/portfolio clients. Reference gated behind portal authentication.
  name: Position Exposure API
  slug: position-exposure
artifact_total: 11
common:
- group: start
  title: ''
  type: Login
  url: https://www.mtb.com/login
- group: auth
  title: ''
  type: DomainSecurity
  url: security/m-t-bank-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.mtb.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.mtb.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.mtb.com/apis
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.mtb.com/getting-started
- group: operate
  title: ''
  type: Support
  url: https://developer.mtb.com/support
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/m&t-bank
- group: company
  title: ''
  type: Blog
  url: https://newsroom.mtb.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.mtb.com/help-center/bank-policies/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.mtb.com/privacy
- group: other
  title: ''
  type: TreasuryManagement
  url: https://www.mtb.com/commercial/treasury-management
- group: auth
  title: ''
  type: DomainSecurity
  url: security/m-t-bank-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/m-t-bank-llms.txt
created: '2026-07-23'
description: 'M&T Bank is a US super-regional bank holding company (M&T Bank Corporation, NYSE: MTB) headquartered in Buffalo, New York, operating through its national bank subsidiary Manufacturers and Traders Trust Company. With roughly $200 billion in assets it is one of the twenty largest US commercial banks, serving consumers, businesses, and institutional clients across the eastern United States, and it owns Wilmington Trust, its custody, fund-administration, and wealth arm. Unlike UK/AU open banking there is no single mandated contract in the US, so M&T''s public API posture is split: it runs a real first-party Developer Portal / "API Store" at developer.mtb.com for institutional and wholesale clients (Banking & Treasury plus Wilmington Trust Custody APIs), gated behind Microsoft Entra login and Azure API Management subscription keys with per-product OpenAPI reference available only after authentication. Consumer-permissioned account data is shared through aggregators (Plaid) rather
  than a public first-party consumer API. No public FDX conformance or CFPB Section 1033 data-access API is documented on the portal at review time.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-23'
name: M&T Bank
nav: Providers
network: true
overview: 'M&T Bank publishes 10 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Financial-Services, Banking, United States, Super-Regional Bank, and Treasury Management.


  M&T Bank''s developer surface includes documentation, getting-started guide, support, engineering blog, and 10 more developer resources.'
random_paper: 13
score:
  band: emerging
  composite: 11.2
  coverage:
    artifact_dirs: 4
    catalog_gap: 80.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 72.2
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 11.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 17.7
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/m-t-bank/refs/heads/main/screenshots/m-t-bank-2026-07-25T225807.png
security:
- kind: domain-security
  name: M T Bank Domain Security
  slug: m-t-bank-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: m-t-bank
tags:
- Financial-Services
- Banking
- United States
- Super-Regional Bank
- Treasury Management
- Payments
- Custody
- Fund Accounting
- Open Finance
- Data Aggregation
website: https://www.mtb.com/
---
