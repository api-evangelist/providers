---
agent_readiness:
  band: agent-native
  dimensions:
    agent_skills: true
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: true
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 74.0
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 20
  human_in_the_loop: 0
  name: Paragon Bank Agentic Access
  operation_count: 86
  slug: paragon-bank-agentic-access
  summary_line: 86 operations · 20 acting
api_count: 4
apis:
- description: The UK Open Banking Open Data API - a public, unauthenticated reference-data surface (ATMs, branches, personal and business current accounts, unsecured SME loans, commercial credit cards) defined by t
  name: Paragon Bank Open Data API (OBIE standard, unverified)
  slug: paragon-open-data-api
- description: The OBIE Read/Write Account and Transaction Information (AIS) API standard - FAPI-secured (OAuth2/OIDC, mutual-TLS, PSD2 strong customer authentication) account, balance, transaction, and party data a
  name: Paragon Bank Account and Transaction Information API (OBIE standard, unverified)
  slug: paragon-account-information-api
- description: The OBIE Read/Write Payment Initiation (PIS) API standard - FAPI-secured initiation of domestic, scheduled, standing-order, international, and file payments on behalf of a customer with PSD2 strong cu
  name: Paragon Bank Payment Initiation API (OBIE standard, unverified)
  slug: paragon-payment-initiation-api
- description: The OBIE Read/Write Confirmation of Funds (CBPII) API standard - FAPI-secured yes/no confirmation of available funds for a card-based payment instrument issuer. Captured here as the shared OBIE standa
  name: Paragon Bank Confirmation of Funds API (OBIE standard, unverified)
  slug: paragon-confirmation-of-funds-api
artifact_total: 9
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/paragon-bank-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/paragon-bank-domain-security.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/paragon-bank-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/paragon-bank-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.paragonbank.co.uk/
- group: company
  title: ''
  type: About
  url: https://www.paragonbank.co.uk/who-we-are
- group: company
  title: ''
  type: Website
  url: https://www.paragonbankinggroup.co.uk/
- group: company
  title: ''
  type: LinkedIn
  url: https://uk.linkedin.com/company/paragon-banking-group-plc
- group: operate
  title: ''
  type: Support
  url: https://www.paragonbank.co.uk/contact-us
- group: commercial
  title: ''
  type: Pricing
  url: https://www.paragonbank.co.uk/savings
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.paragonbank.co.uk/resources/paragonbank/documents/savings/general-terms-and-conditions
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/paragon-bank-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/paragon-bank-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/paragon-bank-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/paragon-bank-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/paragon-bank-lifecycle.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/paragon-bank-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/paragon-bank-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/paragon-bank-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/paragon-bank-account-info-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/paragon-bank-payment-initiation-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/paragon-bank-confirmation-funds-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/paragon-bank-opendata-overlay.yaml
created: '2026-07-23'
description: 'Paragon Bank PLC is a UK specialist lender and retail savings bank, the principal banking subsidiary of Paragon Banking Group PLC (LSE: PAG), a FTSE 250 company founded in 1985 and headquartered in Solihull, West Midlands. Authorised by the Prudential Regulation Authority and regulated by the Financial Conduct Authority and the Prudential Regulation Authority (Firm Reference Number 604551, company number 05390593), Paragon offers fixed-rate and easy-access savings accounts and cash ISAs alongside buy-to-let and residential mortgages, second-charge mortgages, development finance, motor finance, and asset and commercial lending. As a savings-and-lending institution rather than a personal current account provider, Paragon is not one of the CMA9 and publishes no public developer portal or Open Banking API surface of its own - its accounts are reachable to third parties only through account-information aggregators. This profile represents the UK Open Banking Implementation Entity
  (OBIE) standard - the PSD2 Open Data reference APIs and the FAPI-secured Read/Write family (Account and Transaction Information, Payment Initiation, Confirmation of Funds) - captured verbatim as the shared industry standard and clearly labelled as unverified for this bank; no Paragon-hosted endpoint was confirmed at profiling time.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: paragon-bank-mcp.yml
  slug: paragon-bank-mcpyml
modified: '2026-07-23'
name: Paragon Bank
nav: Providers
network: true
overview: 'Paragon Bank publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Open Data API (OBIE standard, unverified), Account and Transaction Information API (OBIE standard, unverified), Payment Initiation API (OBIE standard, unverified), and 1 more. Tagged areas include Financial Services, Banking, Savings, Mortgages, and Specialist Lender.


  Paragon Bank''s developer surface includes authentication, support, pricing, and 21 more developer resources.'
random_paper: 28
scopes:
- name: Paragon Bank Scopes
  scope_count: 3
  slug: paragon-bank-scopes
  summary_line: 3 scopes · clientCredentials/authorizationCode
score:
  band: thin
  composite: 37.8
  facets:
    commercial_clarity: 21.1
    contract_quality: 54.0
    developer_ergonomics: 30.4
    discoverability: 87.5
    governance: 0.0
    operational_transparency: 0.0
  regulatory:
    applies: true
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 67.4
  schema_version: 0.5
  scored_at: '2026-07-23'
security:
- kind: authentication
  name: Paragon Bank Authentication
  slug: paragon-bank-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Paragon Bank Domain Security
  slug: paragon-bank-domain-security
  summary_line: TLSv1.3 · DMARC
slug: paragon-bank
tags:
- Financial Services
- Banking
- Savings
- Mortgages
- Specialist Lender
- Open Banking
- PSD2
- OBIE
- United Kingdom
- Account Information
website: https://www.paragonbank.co.uk/
---
