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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    idempotency: documented
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 51.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 20
  human_in_the_loop: 0
  name: Natwest Agentic Access
  operation_count: 74
  slug: natwest-agentic-access
  summary_line: 74 operations · 20 acting
api_count: 21
apis:
- description: The Account Access API from NatWest Group — 2 operation(s) for account access.
  name: NatWest Group Account Access API
  slug: natwest-account-access-api
- description: The Accounts API from NatWest Group — 2 operation(s) for accounts.
  name: NatWest Group Accounts API
  slug: natwest-accounts-api
- description: The Balances API from NatWest Group — 2 operation(s) for balances.
  name: NatWest Group Balances API
  slug: natwest-balances-api
- description: The Beneficiaries API from NatWest Group — 2 operation(s) for beneficiaries.
  name: NatWest Group Beneficiaries API
  slug: natwest-beneficiaries-api
- description: The Direct Debits API from NatWest Group — 2 operation(s) for direct debits.
  name: NatWest Group Direct Debits API
  slug: natwest-direct-debits-api
- description: The Domestic Payments API from NatWest Group — 5 operation(s) for domestic payments.
  name: NatWest Group Domestic Payments API
  slug: natwest-domestic-payments-api
- description: The Domestic Scheduled Payments API from NatWest Group — 4 operation(s) for domestic scheduled payments.
  name: NatWest Group Domestic Scheduled Payments API
  slug: natwest-domestic-scheduled-payments-api
- description: The Domestic Standing Orders API from NatWest Group — 4 operation(s) for domestic standing orders.
  name: NatWest Group Domestic Standing Orders API
  slug: natwest-domestic-standing-orders-api
- description: The File Payments API from NatWest Group — 6 operation(s) for file payments.
  name: NatWest Group File Payments API
  slug: natwest-file-payments-api
- description: The Funds Confirmations API from NatWest Group — 3 operation(s) for funds confirmations.
  name: NatWest Group Funds Confirmations API
  slug: natwest-funds-confirmations-api
- description: The International Payments API from NatWest Group — 5 operation(s) for international payments.
  name: NatWest Group International Payments API
  slug: natwest-international-payments-api
- description: The International Scheduled Payments API from NatWest Group — 5 operation(s) for international scheduled payments.
  name: NatWest Group International Scheduled Payments API
  slug: natwest-international-scheduled-payments-api
- description: The International Standing Orders API from NatWest Group — 4 operation(s) for international standing orders.
  name: NatWest Group International Standing Orders API
  slug: natwest-international-standing-orders-api
- description: The Offers API from NatWest Group — 2 operation(s) for offers.
  name: NatWest Group Offers API
  slug: natwest-offers-api
- description: The Parties API from NatWest Group — 3 operation(s) for parties.
  name: NatWest Group Parties API
  slug: natwest-parties-api
- description: The Payment Details API from NatWest Group — 7 operation(s) for payment details.
  name: NatWest Group Payment Details API
  slug: natwest-payment-details-api
- description: The Products API from NatWest Group — 2 operation(s) for products.
  name: NatWest Group Products API
  slug: natwest-products-api
- description: The Scheduled Payments API from NatWest Group — 2 operation(s) for scheduled payments.
  name: NatWest Group Scheduled Payments API
  slug: natwest-scheduled-payments-api
- description: The Standing Orders API from NatWest Group — 2 operation(s) for standing orders.
  name: NatWest Group Standing Orders API
  slug: natwest-standing-orders-api
- description: The Statements API from NatWest Group — 4 operation(s) for statements.
  name: NatWest Group Statements API
  slug: natwest-statements-api
- description: The Transactions API from NatWest Group — 3 operation(s) for transactions.
  name: NatWest Group Transactions API
  slug: natwest-transactions-api
artifact_total: 27
common:
- group: agent
  title: ''
  type: WellKnown
  url: well-known/natwest-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/natwest-security.txt
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/natwest-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://www.bankofapis.com/performance/service-interruptions
- group: operate
  title: ''
  type: Deprecation
  url: https://www.bankofapis.com/updates-and-releases
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/natwest-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/natwest-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.bankofapis.com/products/natwest-group-open-banking/fca-service-metrics
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/natwest-error-codes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/natwest-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/natwest-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/natwest-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/natwest-sandbox.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/natwest-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/natwest-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/natwest-account-transaction-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/natwest-payment-initiation-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/natwest-confirmation-of-funds-overlay.yaml
- group: auth
  title: ''
  type: Security
  url: https://bugcrowd.com/natwest-vdp
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/natwest-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/natwest-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/natwest-agentic-access.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/natwest-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/natwest-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.natwest.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.bankofapis.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.bankofapis.com/documentation
- group: start
  title: ''
  type: GettingStarted
  url: https://www.bankofapis.com/getting-started
- group: auth
  title: ''
  type: Authentication
  url: https://www.bankofapis.com/documentation/security
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bankofapis
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/natwest-group
- group: company
  title: ''
  type: Blog
  url: https://www.bankofapis.com/community/articles
- group: operate
  title: ''
  type: Support
  url: https://www.bankofapis.com/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bankofapis.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bankofapis.com/privacy-notice
- group: start
  title: ''
  type: SignUp
  url: https://www.bankofapis.com/register
created: '2026-07-20'
description: NatWest Group is a major UK retail and commercial bank (formerly Royal Bank of Scotland Group) serving personal, business, and corporate customers across the NatWest, Royal Bank of Scotland, Ulster Bank, Coutts, and NatWest International brands. It operates a public developer platform branded the "Bank of APIs" that publishes UK Open Banking (CMA9 / PSD2) APIs - Account and Transaction Information, Payment Initiation, and Confirmation of Funds - conformant to the Open Banking Implementation Entity (OBIE) Read/Write API Standard, alongside premium and commercial APIs. Access is secured with FAPI-grade OAuth2/OIDC, PSD2 strong customer authentication, mutual-TLS client authentication, and dynamic client registration using OBIE/eIDAS certificates, with a full sandbox for onboarding and testing before production.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/natwest.png
layout: provider
mcp_servers:
- description: ''
  name: natwest-mcp.yml
  slug: natwest-mcpyml
modified: '2026-07-20'
name: NatWest Group
nav: Providers
network: true
overview: 'NatWest Group publishes 21 APIs on the [APIs.io](https://apis.io/) network, including Account Access API, Accounts API, Balances API, and 18 more. Tagged areas include Banking, Open Banking, Financial Services, Payments, and PSD2.


  NatWest Group''s developer surface includes changelog, sandbox, authentication, documentation, getting-started guide, engineering blog, support, and 30 more developer resources.'
random_paper: 4
scopes:
- name: Natwest Scopes
  scope_count: 5
  slug: natwest-scopes
  summary_line: 5 scopes
score:
  band: developing
  composite: 54.5
  delta: -4.7
  facets:
    commercial_clarity: 42.1
    contract_quality: 49.7
    developer_ergonomics: 56.0
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 55.3
  previous_composite: 59.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 21
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 74.7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Natwest Authentication
  slug: natwest-authentication
  summary_line: oauth2/openIdConnect/mutualTLS · 2 schemes
- kind: domain-security
  name: Natwest Domain Security
  slug: natwest-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Natwest Vulnerability Disclosure
  slug: natwest-vulnerability-disclosure
  summary_line: Bugcrowd · security.txt · contact published
slug: natwest
tags:
- Banking
- Open Banking
- Financial Services
- Payments
- PSD2
- FAPI
- Fintech
- Account Information
website: https://www.natwest.com/
---
