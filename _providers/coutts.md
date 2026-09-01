---
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
- acting_count: 20
  human_in_the_loop: 0
  name: Coutts Agentic Access
  operation_count: 74
  slug: coutts-agentic-access
  summary_line: 74 operations · 20 acting
api_count: 3
apis:
- description: OBIE Open Data API for Coutts publishing PUBLIC, unauthenticated reference data for its commercial/business current account products, following the Open Banking Open Data Standard. As a private bank C
  name: Coutts Open Data API
  slug: coutts-open-data-api
- description: The Account Access Consents API from Coutts — 2 operation(s) for account access consents.
  name: Coutts Account Access Consents API
  slug: coutts-account-access-consents-api
- description: The Accounts API from Coutts — 2 operation(s) for accounts.
  name: Coutts Accounts API
  slug: coutts-accounts-api
- description: The Balances API from Coutts — 2 operation(s) for balances.
  name: Coutts Balances API
  slug: coutts-balances-api
- description: The Beneficiaries API from Coutts — 2 operation(s) for beneficiaries.
  name: Coutts Beneficiaries API
  slug: coutts-beneficiaries-api
- description: The Direct Debits API from Coutts — 2 operation(s) for direct debits.
  name: Coutts Direct Debits API
  slug: coutts-direct-debits-api
- description: The Domestic Payment Consents API from Coutts — 3 operation(s) for domestic payment consents.
  name: Coutts Domestic Payment Consents API
  slug: coutts-domestic-payment-consents-api
- description: The Domestic Payments API from Coutts — 3 operation(s) for domestic payments.
  name: Coutts Domestic Payments API
  slug: coutts-domestic-payments-api
- description: The Domestic Scheduled Payment Consents API from Coutts — 2 operation(s) for domestic scheduled payment consents.
  name: Coutts Domestic Scheduled Payment Consents API
  slug: coutts-domestic-scheduled-payment-consents-api
- description: The Domestic Scheduled Payments API from Coutts — 3 operation(s) for domestic scheduled payments.
  name: Coutts Domestic Scheduled Payments API
  slug: coutts-domestic-scheduled-payments-api
- description: The Domestic Standing Order Consents API from Coutts — 2 operation(s) for domestic standing order consents.
  name: Coutts Domestic Standing Order Consents API
  slug: coutts-domestic-standing-order-consents-api
- description: The Domestic Standing Orders API from Coutts — 3 operation(s) for domestic standing orders.
  name: Coutts Domestic Standing Orders API
  slug: coutts-domestic-standing-orders-api
- description: The File Payment Consents API from Coutts — 3 operation(s) for file payment consents.
  name: Coutts File Payment Consents API
  slug: coutts-file-payment-consents-api
- description: The File Payments API from Coutts — 4 operation(s) for file payments.
  name: Coutts File Payments API
  slug: coutts-file-payments-api
- description: The Funds Confirmation Consents API from Coutts — 2 operation(s) for funds confirmation consents.
  name: Coutts Funds Confirmation Consents API
  slug: coutts-funds-confirmation-consents-api
- description: The Funds Confirmations API from Coutts — 1 operation(s) for funds confirmations.
  name: Coutts Funds Confirmations API
  slug: coutts-funds-confirmations-api
- description: The International Payment Consents API from Coutts — 3 operation(s) for international payment consents.
  name: Coutts International Payment Consents API
  slug: coutts-international-payment-consents-api
- description: The International Payments API from Coutts — 3 operation(s) for international payments.
  name: Coutts International Payments API
  slug: coutts-international-payments-api
- description: The International Scheduled Payments API from Coutts — 3 operation(s) for international scheduled payments.
  name: Coutts International Scheduled Payments API
  slug: coutts-international-scheduled-payments-api
- description: The International Scheduled Payments Consents API from Coutts — 3 operation(s) for international scheduled payments consents.
  name: Coutts International Scheduled Payments Consents API
  slug: coutts-international-scheduled-payments-consents-api
- description: The International Standing Orders API from Coutts — 3 operation(s) for international standing orders.
  name: Coutts International Standing Orders API
  slug: coutts-international-standing-orders-api
- description: The International Standing Orders Consents API from Coutts — 2 operation(s) for international standing orders consents.
  name: Coutts International Standing Orders Consents API
  slug: coutts-international-standing-orders-consents-api
- description: The Offers API from Coutts — 2 operation(s) for offers.
  name: Coutts Offers API
  slug: coutts-offers-api
- description: The Parties API from Coutts — 3 operation(s) for parties.
  name: Coutts Parties API
  slug: coutts-parties-api
- description: The Products API from Coutts — 2 operation(s) for products.
  name: Coutts Products API
  slug: coutts-products-api
- description: The Scheduled Payments API from Coutts — 2 operation(s) for scheduled payments.
  name: Coutts Scheduled Payments API
  slug: coutts-scheduled-payments-api
- description: The Standing Orders API from Coutts — 2 operation(s) for standing orders.
  name: Coutts Standing Orders API
  slug: coutts-standing-orders-api
- description: The Statements API from Coutts — 5 operation(s) for statements.
  name: Coutts Statements API
  slug: coutts-statements-api
- description: The Transactions API from Coutts — 2 operation(s) for transactions.
  name: Coutts Transactions API
  slug: coutts-transactions-api
artifact_total: 35
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/coutts-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/coutts-account-info-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/coutts-payment-initiation-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/coutts-confirmation-funds-overlay.yaml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/coutts-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/coutts-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/coutts-agentic-access.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/coutts-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/coutts-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.coutts.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.bankofapis.com/products/coutts-open-banking
- group: docs
  title: ''
  type: Documentation
  url: https://www.bankofapis.com/documentation
- group: start
  title: ''
  type: Sandbox
  url: https://developer.coutts.useinfinite.io/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bankofapis
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/coutts-and-co
- group: company
  title: ''
  type: Blog
  url: https://www.coutts.com/insights.html
- group: operate
  title: ''
  type: Support
  url: https://www.coutts.com/help-centre.html
- group: operate
  title: ''
  type: StatusPage
  url: https://www.bankofapis.com/performance/service-interruptions
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.coutts.com/important-information.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.coutts.com/privacy-and-cookie-policy.html
- group: agent
  title: ''
  type: WellKnown
  url: well-known/coutts-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/coutts-security.txt
- group: auth
  title: ''
  type: Security
  url: https://www.coutts.com/.well-known/security.txt
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/coutts-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/coutts-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/coutts-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/coutts-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/coutts-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/coutts-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/coutts-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/coutts-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/coutts-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://www.bankofapis.com/get-started
created: '2026-07-23'
description: Coutts & Co is a British private bank and wealth manager founded in 1692, headquartered in London and serving high-net-worth individuals, families, commercial and institutional clients. It is a wholly owned subsidiary of NatWest Group (formerly The Royal Bank of Scotland Group), one of the UK CMA9 banking groups mandated to deliver Open Banking. Coutts is authorised by the Prudential Regulation Authority and regulated by the Financial Conduct Authority and the PRA (FCA Firm Reference 001b000000MfEueAAF). As an Account Servicing Payment Service Provider (ASPSP) it participates in UK Open Banking under PSD2, exposing its account, payment and confirmation-of-funds surfaces through NatWest Group's "Bank of APIs" developer platform. Those Read/Write APIs conform to the Open Banking Implementation Entity (OBIE) Read/Write Standard and are secured with FAPI-grade OAuth2/OIDC, PSD2 strong customer authentication, and mutual-TLS client authentication using OBIE/eIDAS certificates. Coutts
  additionally publishes OBIE Open Data reference information for its commercial/business current accounts.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: Coutts MCP Server
  slug: coutts-mcp-server
modified: '2026-07-23'
name: Coutts
nav: Providers
network: true
overview: 'Coutts publishes 28 APIs on the [APIs.io](https://apis.io/) network, including Account Access Consents API, Accounts API, Balances API, and 25 more. Tagged areas include Financial-Services, Banking, Private Bank, Wealth Management, and Open Banking.


  Coutts'' developer surface includes authentication, documentation, sandbox, engineering blog, support, getting-started guide, and 28 more developer resources.'
random_paper: 2
scopes:
- name: Coutts Scopes
  scope_count: 3
  slug: coutts-scopes
  summary_line: 3 scopes · clientCredentials/authorizationCode
score:
  band: developing
  composite: 39.8
  coverage:
    artifact_dirs: 18
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 54.4
    developer_ergonomics: 28.0
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 15.8
  previous_composite: 39.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 68.4
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/coutts/refs/heads/main/screenshots/coutts-2026-07-25T210525.png
security:
- kind: authentication
  name: Coutts Authentication
  slug: coutts-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Coutts Domain Security
  slug: coutts-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Coutts Vulnerability Disclosure
  slug: coutts-vulnerability-disclosure
  summary_line: Bugcrowd · security.txt · contact published
slug: coutts
tags:
- Financial-Services
- Banking
- Private Bank
- Wealth Management
- Open Banking
- PSD2
- OBIE
- FAPI
- Payments
- Account Information
- United Kingdom
website: https://www.coutts.com/
---
