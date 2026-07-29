---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: documented
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 45.3
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 20
  human_in_the_loop: 0
  name: Tandem Bank Agentic Access
  operation_count: 74
  slug: tandem-bank-agentic-access
  summary_line: 74 operations · 20 acting
api_count: 3
apis:
- description: Tandem Bank's Open Banking Account Information Service (AIS) exposing account, balance, transaction, and product data for its credit card and savings products. Delivered through Tandem's PSD2 dedicate
  name: Tandem Bank Account and Transaction Information API (AIS)
  slug: tandem-bank-account-transaction-information-api
- description: Tandem Bank's Open Banking Payment Initiation Service (PIS) for initiating domestic and other payments against Tandem accounts. Delivered through Tandem's PSD2 dedicated interface (provided by Token),
  name: Tandem Bank Payment Initiation API (PIS)
  slug: tandem-bank-payment-initiation-api
- description: Tandem Bank's Open Banking Confirmation of Funds Service (CBPII) allowing card-based payment instrument issuers to confirm the availability of funds. Delivered through Tandem's PSD2 dedicated interfac
  name: Tandem Bank Confirmation of Funds API (CBPII)
  slug: tandem-bank-confirmation-of-funds-api
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tandem-bank-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tandem-bank-agentic-access.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/tandem-bank-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tandem-bank-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/tandem-bank-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/tandem-bank-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/tandem-bank-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/tandem-bank-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/tandem-bank-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tandem-bank-lifecycle.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/tandem-bank-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tandem-bank-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.token.io/token_tpp_sdk_doc/content/a-tpp_onboarding/sdk_intro.htm
- group: company
  title: ''
  type: Website
  url: https://www.tandem.co.uk/
- group: other
  title: ''
  type: OpenBanking
  url: https://www.tandem.co.uk/save/open-banking-page
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.token.io/
- group: other
  title: ''
  type: APIStandard
  url: https://github.com/OpenBankingUK/read-write-api-specs
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tandem-bank/
- group: company
  title: ''
  type: Blog
  url: https://www.tandem.co.uk/blog
- group: company
  title: ''
  type: Newsroom
  url: https://www.tandem.co.uk/newsroom
- group: operate
  title: ''
  type: Support
  url: https://www.tandem.co.uk/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tandem.co.uk/privacy-notice
- group: company
  title: ''
  type: About
  url: https://www.tandem.co.uk/about
created: '2026-07-23'
description: Tandem Bank (Tandem Bank Limited) is a UK app-only challenger and self-styled "greener" digital bank founded in 2014 and headquartered in Blackpool, England, with offices in Cardiff, Durham, and London. It obtained its UK banking licence through the 2018 acquisition of Harrods Bank and has since grown by acquiring Allium Lending Group, Oplo, and Loop Money, offering savings and cash ISAs, green home-improvement and home loans, mortgages, motor finance, and a credit card. Tandem Bank Limited is authorised by the Prudential Regulation Authority and regulated by the Financial Conduct Authority. It is not one of the CMA9 and does not publish a public Open Data reference API; as an FCA-authorised ASPSP it meets UK Open Banking / PSD2 obligations through a dedicated interface provided by Token, conformant to the Open Banking Implementation Entity (OBIE) Read/Write Standard for Account and Transaction Information (AIS), Payment Initiation (PIS), and Confirmation of Funds (CBPII), secured
  with FAPI-grade OAuth2/OIDC, mutual-TLS, and PSD2 strong customer authentication. Tandem also consumes Open Banking as a TPP via TrueLayer for savings onboarding and transfers.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: tandem-bank-mcp.yml
  slug: tandem-bank-mcpyml
modified: '2026-07-23'
name: Tandem Bank
nav: Providers
network: true
overview: 'Tandem Bank publishes 3 APIs on the [APIs.io](https://apis.io/) network: Account and Transaction Information API (AIS), Payment Initiation API (PIS), and Confirmation of Funds API (CBPII). Tagged areas include Financial Services, Banking, Open Banking, PSD2, and OBIE.


  Tandem Bank''s developer surface includes authentication, getting-started guide, engineering blog, support, and 20 more developer resources.'
random_paper: 50
scopes:
- name: Tandem Bank Scopes
  scope_count: 3
  slug: tandem-bank-scopes
  summary_line: 3 scopes · clientCredentials/authorizationCode
score:
  band: thin
  composite: 36.7
  delta: -3.0
  facets:
    commercial_clarity: 10.5
    contract_quality: 50.6
    developer_ergonomics: 40.8
    discoverability: 72.2
    governance: 11.5
    operational_transparency: 0.0
  previous_composite: 39.7
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
    score: 65.8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Tandem Bank Authentication
  slug: tandem-bank-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Tandem Bank Domain Security
  slug: tandem-bank-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tandem-bank
tags:
- Financial Services
- Banking
- Open Banking
- PSD2
- OBIE
- FAPI
- United Kingdom
- Payments
- Account Information
- Challenger Bank
- Fintech
website: https://www.tandem.co.uk/
---
