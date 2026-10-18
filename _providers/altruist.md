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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.5
  scored_at: '2026-10-17'
api_count: 2
apis:
- description: OAuth 2.0 authorization-code API giving partners full access to Altruist custody data — accounts, households, positions, transactions, and cost basis — for advisor tools, reporting, and reconciliation
  name: Altruist Open API
  slug: altruist-open-api
- description: OAuth 2.0 password-grant API for account onboarding, funding, transfers, contacts, households, bank-link, user management, and time-weighted return performance reporting.
  name: Altruist Realtime API
  slug: altruist-realtime-api
- baseURL: https://openapi.altruist.com/altruist-open-api/
  baseurl_source: declared
  description: ACAT transfer operations for managed brokerage accounts
  name: Altruist ACAT Transfers API
  slug: altruist-acat-transfers-api
- baseURL: https://openapi.altruist.com/altruist-open-api/
  baseurl_source: declared
  description: Account management
  name: Altruist Account API
  slug: altruist-account-api
- baseURL: https://openapi.altruist.com/altruist-open-api/
  baseurl_source: declared
  description: Account data and operations
  name: Altruist Account Balance API
  slug: altruist-account-balance-api
- baseURL: https://openapi.altruist.com/altruist-open-api/
  baseurl_source: declared
  description: Multi-account draft bundle management
  name: Altruist Account Draft Bundles API
  slug: altruist-account-draft-bundles-api
- baseURL: https://openapi.altruist.com/altruist-open-api/
  baseurl_source: declared
  description: Account Group Management
  name: Altruist Account Group API
  slug: altruist-account-group-api
- baseURL: https://openapi.altruist.com/altruist-open-api/
  baseurl_source: declared
  description: Account portfolio management
  name: Altruist Account Portfolios API
  slug: altruist-account-portfolios-api
- baseURL: https://openapi.altruist.com/altruist-open-api/
  baseurl_source: declared
  description: The accounts API from Altruist — 2 operation(s) for accounts.
  name: Altruist Accounts API
  slug: altruist-accounts-api
- baseURL: https://openapi.altruist.com/altruist-open-api/
  baseurl_source: declared
  description: Bank link operations for full brokerage accounts
  name: Altruist Bank Links API
  slug: altruist-bank-links-api
- baseURL: https://openapi.altruist.com/altruist-open-api/
  baseurl_source: declared
  description: Cash set aside (liquidation) operations for brokerage accounts
  name: Altruist Cash Set Aside API
  slug: altruist-cash-set-aside-api
- baseURL: https://openapi.altruist.com/altruist-open-api/
  baseurl_source: declared
  description: Cash management settings for brokerage accounts
  name: Altruist Cash Settings API
  slug: altruist-cash-settings-api
- baseURL: https://openapi.altruist.com/altruist-open-api/
  baseurl_source: declared
  description: Cash transfer operations between funding and brokerage accounts
  name: Altruist Cash Transfers API
  slug: altruist-cash-transfers-api
- baseURL: https://openapi.altruist.com/altruist-open-api/
  baseurl_source: declared
  description: Client Agreement management for account drafts
  name: Altruist Client Agreement API
  slug: altruist-client-agreement-api
- baseURL: https://openapi.altruist.com/altruist-open-api/
  baseurl_source: declared
  description: IRA contribution limit operations
  name: Altruist Contribution Limits API
  slug: altruist-contribution-limits-api
- baseURL: https://openapi.altruist.com/altruist-open-api/
  baseurl_source: declared
  description: The cost-basis API from Altruist — 2 operation(s) for cost-basis.
  name: Altruist Cost Basis API
  slug: altruist-cost-basis-api
- baseURL: https://openapi.altruist.com/altruist-open-api/
  baseurl_source: declared
  description: The data-feed API from Altruist — 2 operation(s) for data-feed.
  name: Altruist Data Feed API
  slug: altruist-data-feed-api
- baseURL: https://openapi.altruist.com/altruist-open-api/
  baseurl_source: declared
  description: Beneficiary management for account drafts within bundles
  name: Altruist Draft Beneficiaries API
  slug: altruist-draft-beneficiaries-api
- baseURL: https://openapi.altruist.com/altruist-open-api/
  baseurl_source: declared
  description: Funding accounts from voided checks used for transfers
  name: Altruist Funding Accounts API
  slug: altruist-funding-accounts-api
- baseURL: https://openapi.altruist.com/altruist-open-api/
  baseurl_source: declared
  description: Brokerage accounts eligible to receive ACH funding
  name: Altruist Funding Eligible Accounts API
  slug: altruist-funding-eligible-accounts-api
- baseURL: https://openapi.altruist.com/altruist-open-api/
  baseurl_source: declared
  description: The historical-data-feed API from Altruist — 1 operation(s) for historical-data-feed.
  name: Altruist Historical Data Feed API
  slug: altruist-historical-data-feed-api
- baseURL: https://openapi.altruist.com/altruist-open-api/
  baseurl_source: declared
  description: Accounts assigned to a household
  name: Altruist Household Accounts API
  slug: altruist-household-accounts-api
- baseURL: https://openapi.altruist.com/altruist-open-api/
  baseurl_source: declared
  description: Household management
  name: Altruist Household API
  slug: altruist-household-api
- baseURL: https://openapi.altruist.com/altruist-open-api/
  baseurl_source: declared
  description: Household contact management
  name: Altruist Household Contact API
  slug: altruist-household-contact-api
- baseURL: https://openapi.altruist.com/altruist-open-api/
  baseurl_source: declared
  description: The households API from Altruist — 2 operation(s) for households.
  name: Altruist Households API
  slug: altruist-households-api
- baseURL: https://openapi.altruist.com/altruist-open-api/
  baseurl_source: declared
  description: Time weighted returns and performance analytics
  name: Altruist Performance Analytics API
  slug: altruist-performance-analytics-api
- baseURL: https://openapi.altruist.com/altruist-open-api/
  baseurl_source: declared
  description: Plaid bank linking operations
  name: Altruist Plaid API
  slug: altruist-plaid-api
- baseURL: https://openapi.altruist.com/altruist-open-api/
  baseurl_source: declared
  description: Firm-level points of contact for an organization
  name: Altruist Point of Contact API
  slug: altruist-point-of-contact-api
- baseURL: https://openapi.altruist.com/altruist-open-api/
  baseurl_source: declared
  description: Portfolio management
  name: Altruist Portfolios API
  slug: altruist-portfolios-api
- baseURL: https://openapi.altruist.com/altruist-open-api/
  baseurl_source: declared
  description: The positions API from Altruist — 2 operation(s) for positions.
  name: Altruist Positions API
  slug: altruist-positions-api
- baseURL: https://openapi.altruist.com/altruist-open-api/
  baseurl_source: declared
  description: Recurring ACH transfer scheduling for brokerage accounts
  name: Altruist Scheduled Transfers API
  slug: altruist-scheduled-transfers-api
- baseURL: https://openapi.altruist.com/altruist-open-api/
  baseurl_source: declared
  description: The transactions API from Altruist — 1 operation(s) for transactions.
  name: Altruist Transactions API
  slug: altruist-transactions-api
- baseURL: https://openapi.altruist.com/altruist-open-api/
  baseurl_source: declared
  description: Transfer management for account drafts
  name: Altruist Transfers API
  slug: altruist-transfers-api
- baseURL: https://openapi.altruist.com/altruist-open-api/
  baseurl_source: declared
  description: Trusted contact management
  name: Altruist Trusted Contact API
  slug: altruist-trusted-contact-api
- baseURL: https://openapi.altruist.com/altruist-open-api/
  baseurl_source: declared
  description: User creation for records referenced by account drafts (e.g. minors, employers)
  name: Altruist User API
  slug: altruist-user-api
- baseURL: https://openapi.altruist.com/altruist-open-api/
  baseurl_source: declared
  description: Account opening and management
  name: Altruist User Invitation API
  slug: altruist-user-invitation-api
- baseURL: https://openapi.altruist.com/altruist-open-api/
  baseurl_source: declared
  description: User profile management
  name: Altruist User Profile API
  slug: altruist-user-profile-api
artifact_total: 41
common:
- group: company
  title: ''
  type: BlogRSS
  url: https://altruist.com/feed/
- group: company
  title: ''
  type: Website
  url: https://altruist.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.altruist.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.altruist.com/docs/overview
- group: docs
  title: ''
  type: APIReference
  url: https://developer.altruist.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.altruist.com/docs/getting-started-with-open-api
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/altruist/refs/heads/main/authentication/altruist-authentication.yml
  title: ''
  type: Authentication
  url: authentication/altruist-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/altruist/refs/heads/main/scopes/altruist-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/altruist-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/altruist/refs/heads/main/errors/altruist-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/altruist-error-codes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/altruist/refs/heads/main/lifecycle/altruist-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/altruist-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.altruist.com/
- group: operate
  title: ''
  type: Deprecation
  url: https://developer.altruist.com/docs/deprecation-policy
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/altruist/refs/heads/main/conventions/altruist-conventions.yml
  title: ''
  type: Conventions
  url: conventions/altruist-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/altruist/refs/heads/main/conformance/altruist-conformance.yml
  title: ''
  type: Conformance
  url: conformance/altruist-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.altruist.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/altruist/refs/heads/main/security/altruist-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/altruist-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/altruist/refs/heads/main/security/altruist-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/altruist-domain-security.yml
- group: auth
  title: ''
  type: Security
  url: https://altruist.com/legal/security/
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/altruist/refs/heads/main/changelog/altruist-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/altruist-changelog.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/altruist/refs/heads/main/sandbox/altruist-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/altruist-sandbox.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/altruist/refs/heads/main/well-known/altruist-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/altruist-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/altruist/refs/heads/main/mcp/altruist-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/altruist-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/altruist/refs/heads/main/llms/altruist-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/altruist-llms.txt
- group: operate
  title: ''
  type: Support
  url: https://developer.altruist.com/docs/support-policy
- group: company
  title: ''
  type: Blog
  url: https://altruist.com/engineering-blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://hazel.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.altruist.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://altruist.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://altruist.com/legal/privacy-policy/
created: '2026-07-17'
description: Altruist is a modern, vertically integrated RIA custodian and technology platform for independent financial advisors. It combines self-clearing custody infrastructure with software for digital account opening, fractional model-based trading, rebalancing, tax management, fee billing, and performance reporting in a single workspace. Altruist runs a developer program with an OAuth 2.0 Open API (accounts, households, positions, transactions, cost basis), a Realtime API (account onboarding, funding, transfers, contacts, bank-link, time-weighted return), and custodial flat-file (SFTP) data feeds, so advisor tools and fintech partners such as Orion, Tamarac, Black Diamond, and Advyzon can integrate directly with the custodian. Backed by ICONIQ Capital and Insight Partners.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/altruist.png
layout: provider
modified: '2026-10-06'
name: Altruist
nav: Providers
network: true
overview: 'Altruist publishes 37 API contracts indexed on the [APIs.io](https://apis.io/) network, including ACAT Transfers API, Account API, Account Balance API, and 34 more. Tagged areas include Company, Fintech, Custody, Wealth Management, and Financial Advisors.


  Altruist''s developer surface includes documentation, API reference, getting-started guide, authentication, changelog, sandbox, support, and 22 more developer resources.'
random_paper: 8
scopes:
- name: Altruist Scopes
  scope_count: 1
  slug: altruist-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: developing
  composite: 53.1
  coverage:
    artifact_dirs: 16
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 11.2
  facets:
    access_clarity: 47.4
    contract_governance: 18.2
    contract_quality: 47.2
    developer_ergonomics: 64.3
    discoverability: 73.2
    operational_transparency: 50.0
  previous_composite: 41.9
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 35
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 39.2
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/altruist/refs/heads/main/screenshots/altruist-2026-07-25T195845.png
security:
- kind: authentication
  name: Altruist Authentication
  slug: altruist-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Altruist Domain Security
  slug: altruist-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Altruist Trust Center
  slug: altruist-trust-center
  summary_line: SOC 2
slug: altruist
tags:
- Company
- Fintech
- Custody
- Wealth Management
- Financial Advisors
- RIA
- Investing
- Authentication
website: https://altruist.com/
---
