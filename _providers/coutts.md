---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 42.9
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 20
  human_in_the_loop: 0
  name: Coutts Agentic Access
  operation_count: 74
  slug: coutts-agentic-access
  summary_line: 74 operations · 20 acting
api_count: 4
apis:
- description: OBIE Read/Write Account and Transaction Information (AIS) API for Coutts, letting FCA-authorised AISPs retrieve account, balance, transaction, party, standing order, direct debit, beneficiary, product
  name: Coutts Account and Transaction Information API
  slug: coutts-account-transaction-api
- description: OBIE Read/Write Payment Initiation (PIS) API for Coutts, letting FCA-authorised PISPs initiate domestic, scheduled, standing-order, international and file payments on behalf of the account holder. Con
  name: Coutts Payment Initiation API
  slug: coutts-payment-initiation-api
- description: 'OBIE Read/Write Confirmation of Funds (CBPII) API for Coutts, letting authorised Card Based Payment Instrument Issuers check whether sufficient funds are available on an account before a transaction. '
  name: Coutts Confirmation of Funds API
  slug: coutts-confirmation-of-funds-api
- description: OBIE Open Data API for Coutts publishing PUBLIC, unauthenticated reference data for its commercial/business current account products, following the Open Banking Open Data Standard. As a private bank C
  name: Coutts Open Data API
  slug: coutts-open-data-api
artifact_total: 10
common:
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
  name: coutts-mcp.yml
  slug: coutts-mcpyml
modified: '2026-07-23'
name: Coutts
nav: Providers
network: true
overview: 'Coutts publishes 3 APIs on the [APIs.io](https://apis.io/) network: Account and Transaction Information API, Payment Initiation API, and Confirmation of Funds API. Tagged areas include Financial Services, Banking, Private Bank, Wealth Management, and Open Banking.


  Coutts'' developer surface includes authentication, documentation, sandbox, engineering blog, support, getting-started guide, and 24 more developer resources.'
random_paper: 2
scopes:
- name: Coutts Scopes
  scope_count: 3
  slug: coutts-scopes
  summary_line: 3 scopes · clientCredentials/authorizationCode
score:
  band: developing
  composite: 41.3
  delta: -6.6
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 16.7
    contract_quality: 55.9
    developer_ergonomics: 20.8
    discoverability: 92.6
    governance: 16.7
    operational_transparency: 15.8
  previous_composite: 47.9
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
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
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
- Financial Services
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
