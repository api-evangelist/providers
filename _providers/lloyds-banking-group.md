---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 48.0
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 26
  human_in_the_loop: 0
  name: Lloyds Banking Group Agentic Access
  operation_count: 95
  slug: lloyds-banking-group-agentic-access
  summary_line: 95 operations · 26 acting
api_count: 6
apis:
- description: Public, unauthenticated UK Open Banking Open Data API exposing reference data - ATMs, branches, personal current accounts, business current accounts, unsecured SME loans, and commercial credit cards -
  name: Lloyds Banking Group Open Data API
  slug: open-data-api
- description: OBIE Read/Write Account and Transaction Information (AIS) API for accessing account, balance, transaction, beneficiary, standing order, direct debit, and statement data with customer consent. FAPI-sec
  name: Lloyds Banking Group Account and Transaction Information API
  slug: account-information-api
- description: OBIE Read/Write Payment Initiation (PIS) API for initiating domestic, scheduled, standing-order, international, and business bulk/batch payments with customer authorisation. FAPI-secured (OAuth2/OIDC,
  name: Lloyds Banking Group Payment Initiation API
  slug: payment-initiation-api
- description: OBIE Read/Write Confirmation of Funds (CBPII) API allowing an authorised card-based payment instrument issuer to check whether funds are available on a customer account. FAPI-secured (OAuth2/OIDC, mTL
  name: Lloyds Banking Group Confirmation of Funds API
  slug: confirmation-of-funds-api
- description: OBIE Variable Recurring Payments (VRP) profile API enabling consent-based recurring payments under a customer-agreed mandate, including sweeping between a customer's own accounts. FAPI-secured (OAuth2
  name: Lloyds Banking Group Variable Recurring Payments API
  slug: variable-recurring-payments-api
- description: OBIE Event Notifications API delivering aggregated and real-time event signals (e.g. consent revocation, resource-update notifications) to registered TPPs. FAPI-secured; requires developer-portal onbo
  name: Lloyds Banking Group Event Notifications API
  slug: event-notifications-api
artifact_total: 11
asyncapis:
- description: ''
  name: Lloyds Banking Group Event Notifications Webhooks
  slug: lloyds-banking-group-event-notifications-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lloyds-banking-group-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/lloyds-banking-group-agentic-access.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/lloyds-banking-group-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/lloyds-banking-group-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/lloyds-banking-group-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/lloyds-banking-group-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/lloyds-banking-group-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/lloyds-banking-group-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/lloyds-banking-group-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/lloyds-banking-group-data-model.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/lloyds-banking-group-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://www.lloydsbankinggroup.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.lloydsbanking.com/prod01/lbg/home
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.lloydsbanking.com/prod01/lbg/get-started
- group: docs
  title: ''
  type: Documentation
  url: https://developer.lloydsbanking.com/prod01/lbg/products
- group: docs
  title: ''
  type: APIReference
  url: https://developer.lloydsbanking.com/prod01/lbg/products
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/LloydsBanking
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lloyds-banking-group
- group: company
  title: ''
  type: Blog
  url: https://www.lloydsbankinggroup.com/insights.html
- group: operate
  title: ''
  type: Support
  url: https://developer.lloydsbanking.com/prod01/lbg/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.lloydsbankinggroup.com/privacy.html
created: '2026-07-23'
description: Lloyds Banking Group plc is the United Kingdom's largest retail and commercial banking group, serving personal, business, and corporate customers through the Lloyds Bank, Halifax, Bank of Scotland, MBNA, and Scottish Widows brands. Formed in 2009 through the acquisition of HBOS by Lloyds TSB, it is a publicly listed company on the London Stock Exchange (LLOY) and a FTSE 100 constituent - not a mutual or building society. It is authorised by the Prudential Regulation Authority and regulated by the Financial Conduct Authority and the PRA. As one of the nine CMA-mandated banks (CMA9), Lloyds operates a public developer platform at developer.lloydsbanking.com that publishes UK Open Banking (OBIE / PSD2) APIs - unauthenticated Open Data reference APIs for ATMs, branches, and product information, plus the FAPI-secured Read/Write family - Account and Transaction Information (AIS), Payment Initiation (PIS), Confirmation of Funds (CBPII), Variable Recurring Payments (VRP), and Event
  Notifications - conformant to the Open Banking Implementation Entity (OBIE) Read/Write API Standard, secured with OAuth2/OIDC, mutual-TLS, and PSD2 strong customer authentication using OBIE/eIDAS certificates.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-23'
name: Lloyds Banking Group
nav: Providers
network: true
overview: 'Lloyds Banking Group publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Open Data API, Account and Transaction Information API, Payment Initiation API, and 2 more. Tagged areas include Financial Services, Banking, Open Banking, PSD2, and OBIE.


  The Lloyds Banking Group catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Lloyds Banking Group''s developer surface includes authentication, getting-started guide, documentation, API reference, engineering blog, support, and 16 more developer resources.'
random_paper: 6
scopes:
- name: Lloyds Banking Group Scopes
  scope_count: 3
  slug: lloyds-banking-group-scopes
  summary_line: 3 scopes · clientCredentials/authorizationCode
score:
  band: developing
  composite: 43.4
  delta: 0.0
  facets:
    commercial_clarity: 10.5
    contract_quality: 64.5
    developer_ergonomics: 53.8
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 5.3
  previous_composite: 43.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 60.8
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lloyds-banking-group/refs/heads/main/screenshots/lloyds-banking-group-2026-07-25T225413.png
security:
- kind: authentication
  name: Lloyds Banking Group Authentication
  slug: lloyds-banking-group-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Lloyds Banking Group Domain Security
  slug: lloyds-banking-group-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: lloyds-banking-group
tags:
- Financial Services
- Banking
- Open Banking
- PSD2
- OBIE
- CMA9
- United Kingdom
- Payments
- Account Information
- Open Data
- FAPI
website: https://www.lloydsbankinggroup.com/
---
