---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 39.0
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Metro Bank Agentic Access
  operation_count: 12
  slug: metro-bank-agentic-access
  summary_line: 12 operations
api_count: 5
apis:
- description: Public, unauthenticated OBIE Open Data reference API exposing Metro Bank's ATM locations, branch ("store") locations, personal and business current account products, unsecured SME loans, and commercia
  name: Metro Bank Open Data API
  slug: metro-bank-open-data-api
- description: OBIE Read/Write Account Information Service (AIS) API providing consented access to account details, balances, transactions, beneficiaries, standing orders, direct debits, and statements. FAPI-secured
  name: Metro Bank Account and Transaction Information API
  slug: metro-bank-account-information-api
- description: OBIE Read/Write Payment Initiation Service (PIS) API for initiating domestic and scheduled payments, standing orders, and file payments on behalf of a consenting customer. FAPI-secured with OAuth2/OID
  name: Metro Bank Payment Initiation API
  slug: metro-bank-payment-initiation-api
- description: OBIE Read/Write Confirmation of Funds (CBPII) API allowing a card-based payment instrument issuer to confirm whether sufficient funds are available on a customer account. FAPI-secured with OAuth2/OIDC
  name: Metro Bank Confirmation of Funds API
  slug: metro-bank-confirmation-of-funds-api
- description: API publishing Metro Bank's FCA service-quality and account metrics data (management information required under UK regulatory reporting), documented in the Metro Bank developer portal as the FCA Accou
  name: Metro Bank FCA Account Metrics API
  slug: metro-bank-fca-account-metrics-api
artifact_total: 10
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/metro-bank-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/metro-bank-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/metro-bank-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/metro-bank-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/metro-bank-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/metro-bank-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/metro-bank-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/metro-bank-lifecycle.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/metro-bank-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/metro-bank-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/metro-bank-open-data-overlay.yaml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/metro-bank-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/metro-bank-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://www.metrobankonline.co.uk/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.metrobankonline.co.uk/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.metrobankonline.co.uk/Overview
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/metro-bank
- group: company
  title: ''
  type: Blog
  url: https://www.metrobankonline.co.uk/about-us/press-releases/
- group: operate
  title: ''
  type: Support
  url: https://www.metrobankonline.co.uk/help-and-support/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.metrobankonline.co.uk/privacy/
created: '2026-07-23'
description: Metro Bank is a UK retail and commercial bank founded in 2010 as the first new high-street bank to open in Britain in over 150 years, headquartered in London and listed on the London Stock Exchange (ticker MTRO). It is a public limited company (not a mutual or building society), authorised by the Prudential Regulation Authority and regulated by the Financial Conduct Authority and the PRA, serving personal and business customers through its branch ("store") network and digital channels. As an FCA-authorised account servicing payment service provider (ASPSP) under PSD2, Metro Bank participates in UK Open Banking without being one of the nine CMA-mandated banks (the CMA9). It operates a public developer portal, built on Google Apigee, that publishes PSD2 / UK Open Banking APIs aligned to the Open Banking Implementation Entity (OBIE) Read/Write standard - Account and Transaction Information, Payment Initiation, and Confirmation of Funds - secured with FAPI-grade OAuth2/OIDC, mutual
  TLS, dynamic client registration, and PSD2 strong customer authentication, alongside the OBIE Open Data reference-data APIs and FCA service-quality metrics reporting.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: metro-bank-mcp.yml
  slug: metro-bank-mcpyml
modified: '2026-07-23'
name: Metro Bank
nav: Providers
network: true
overview: 'Metro Bank publishes 1 API on the [APIs.io](https://apis.io/) network: Open Data API. Tagged areas include Financial Services, Banking, Open Banking, PSD2, and OBIE.


  Metro Bank''s developer surface includes authentication, documentation, engineering blog, support, and 17 more developer resources.'
random_paper: 104
scopes:
- name: Metro Bank Scopes
  scope_count: 4
  slug: metro-bank-scopes
  summary_line: 4 scopes · authorizationCode/clientCredentials
score:
  band: thin
  composite: 36.1
  delta: 0.0
  facets:
    commercial_clarity: 10.5
    contract_quality: 37.2
    developer_ergonomics: 38.6
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 0.0
  previous_composite: 36.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 65.8
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Metro Bank Authentication
  slug: metro-bank-authentication
  summary_line: oauth2/openIdConnect/mutualTLS · 4 schemes
- kind: domain-security
  name: Metro Bank Domain Security
  slug: metro-bank-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: metro-bank
tags:
- Financial Services
- Banking
- Open Banking
- PSD2
- OBIE
- United Kingdom
- Payments
- Account Information
- FAPI
- Fintech
website: https://www.metrobankonline.co.uk/
---
