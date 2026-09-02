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
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.4
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Zopa Agentic Access
  operation_count: 23
  slug: zopa-agentic-access
  summary_line: 23 operations · 6 acting
api_count: 2
apis:
- description: The Account Access API from zopa — 2 operation(s) for account access.
  name: zopa Account Access API
  slug: zopa-account-access-api
- description: The Accounts API from zopa — 2 operation(s) for accounts.
  name: zopa Accounts API
  slug: zopa-accounts-api
- description: The Balances API from zopa — 1 operation(s) for balances.
  name: zopa Balances API
  slug: zopa-balances-api
- description: The Beneficiaries API from zopa — 1 operation(s) for beneficiaries.
  name: zopa Beneficiaries API
  slug: zopa-beneficiaries-api
- description: The Direct Debits API from zopa — 1 operation(s) for direct debits.
  name: zopa Direct Debits API
  slug: zopa-direct-debits-api
- description: The Domestic Payments API from zopa — 5 operation(s) for domestic payments.
  name: zopa Domestic Payments API
  slug: zopa-domestic-payments-api
- description: The Domestic Standing Orders API from zopa — 4 operation(s) for domestic standing orders.
  name: zopa Domestic Standing Orders API
  slug: zopa-domestic-standing-orders-api
- description: The Offers API from zopa — 1 operation(s) for offers.
  name: zopa Offers API
  slug: zopa-offers-api
- description: The Parties API from zopa — 2 operation(s) for parties.
  name: zopa Parties API
  slug: zopa-parties-api
- description: The Standing Orders API from zopa — 1 operation(s) for standing orders.
  name: zopa Standing Orders API
  slug: zopa-standing-orders-api
- description: The Statements API from zopa — 1 operation(s) for statements.
  name: zopa Statements API
  slug: zopa-statements-api
- description: The Transactions API from zopa — 1 operation(s) for transactions.
  name: zopa Transactions API
  slug: zopa-transactions-api
artifact_total: 31
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Account and Transaction API Specification Account Access API
  slug: open-zopa-account-access-api
- collection_type: open
  name: Account and Transaction API Specification Account Access Accounts API
  slug: open-zopa-accounts-api
- collection_type: open
  name: Account and Transaction API Specification Account Access Balances API
  slug: open-zopa-balances-api
- collection_type: open
  name: Account and Transaction API Specification Account Access Beneficiaries API
  slug: open-zopa-beneficiaries-api
- collection_type: open
  name: Account and Transaction API Specification Account Access Direct Debits API
  slug: open-zopa-direct-debits-api
- collection_type: open
  name: Account and Transaction API Specification Account Access Domestic Payments API
  slug: open-zopa-domestic-payments-api
- collection_type: open
  name: Account and Transaction API Specification Account Access Domestic Standing Orders API
  slug: open-zopa-domestic-standing-orders-api
- collection_type: open
  name: Account and Transaction API Specification Account Access Offers API
  slug: open-zopa-offers-api
- collection_type: open
  name: Account and Transaction API Specification Account Access Parties API
  slug: open-zopa-parties-api
- collection_type: open
  name: Account and Transaction API Specification Account Access Standing Orders API
  slug: open-zopa-standing-orders-api
- collection_type: open
  name: Account and Transaction API Specification Account Access Statements API
  slug: open-zopa-statements-api
- collection_type: open
  name: Account and Transaction API Specification Account Access Transactions API
  slug: open-zopa-transactions-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/zopa-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/zopa-account-info-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/zopa-agentic-access.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/zopa-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/zopa-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zopa-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.zopa.com/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/zopa-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/zopa-security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/zopa-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.zopa.com/.well-known/security.txt
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/zopa-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/zopa-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/zopa-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/zopa-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/zopa-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.zopa.com/open-banking-developer
- group: design
  title: ''
  type: DataModel
  url: data-model/zopa-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/zopa-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/zopa-llms.txt
- group: start
  title: ''
  type: Sandbox
  url: sandbox/zopa-sandbox.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.openbanking-sandbox.zopa.com/perry/developer/welcome
- group: docs
  title: ''
  type: Documentation
  url: https://www.zopa.com/open-banking-developer
- group: company
  title: ''
  type: Blog
  url: https://www.zopa.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.zopa.com/help
- group: start
  title: ''
  type: Login
  url: https://home.zopa.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.zopa.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.zopa.com/privacy-notice
- group: company
  title: ''
  type: Careers
  url: https://careers.zopa.com/
created: '2026-07-17'
description: 'Zopa Bank is a UK FCA-authorised, PRA-regulated digital bank offering flexible savings, personal loans, credit cards, car finance and the Biscuit current account. As a registered Account Servicing Payment Service Provider (ASPSP), Zopa exposes UK Open Banking Read/Write v4.0.0 APIs to authorised Third Party Providers: an Account & Transaction API (AIS) for consent-based access to accounts, balances, transactions, statements, standing orders, direct debits, beneficiaries and party data, and a Payment Initiation API (PIS) for domestic payments and standing orders. Access uses OAuth2 (client-credentials for TPPs, authorization-code for PSUs) over mutual TLS with FAPI headers and JWS request signing. Zopa was surfaced as a portfolio company of Balderton Capital, Bessemer Venture Partners, HV Capital, Northzone, QED Investors and SoftBank Vision Fund.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zopa.png
layout: provider
mcp_servers:
- description: ''
  name: zopa MCP Server
  slug: zopa-mcp-server
modified: '2026-07-21'
name: zopa
nav: Providers
network: true
overview: 'zopa publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Account Access API, Accounts API, Balances API, and 9 more. Tagged areas include Company, Banking, Fintech, Open Banking, and PSD2.


  zopa''s developer surface includes authentication, sandbox, documentation, engineering blog, support, and 25 more developer resources.'
random_paper: 1
scopes:
- name: Zopa Scopes
  scope_count: 2
  slug: zopa-scopes
  summary_line: 2 scopes · clientCredentials/authorizationCode
score:
  band: developing
  composite: 40.2
  coverage:
    artifact_dirs: 20
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 50.3
    developer_ergonomics: 38.7
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 5.3
  previous_composite: 40.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: psd2
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 76.6
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/zopa/refs/heads/main/screenshots/zopa-2026-08-17T083118.png
security:
- kind: authentication
  name: Zopa Authentication
  slug: zopa-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Zopa Domain Security
  slug: zopa-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Zopa Vulnerability Disclosure
  slug: zopa-vulnerability-disclosure
  summary_line: Intigriti · security.txt · contact published
slug: zopa
tags:
- Company
- Banking
- Fintech
- Open Banking
- PSD2
- Payments
- Account Information
- Payment Initiation
- FAPI
- United Kingdom
- Digital Bank
- Lending
website: https://www.zopa.com/
---
