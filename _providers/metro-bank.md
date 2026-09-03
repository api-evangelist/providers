---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.4
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Metro Bank Agentic Access
  operation_count: 12
  slug: metro-bank-agentic-access
  summary_line: 12 operations
api_count: 1
apis:
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
- baseURL: https://api.metrobankonline.co.uk/open-banking/v2.3
  baseurl_source: declared
  description: Endpoint for getting ATM data
  name: Metro Bank ATM API
  slug: metro-bank-atm-api
- baseURL: https://api.metrobankonline.co.uk/open-banking/v2.3
  baseurl_source: declared
  description: Endpoint for getting Business Current Account data
  name: Metro Bank BCA API
  slug: metro-bank-bca-api
- baseURL: https://api.metrobankonline.co.uk/open-banking/v2.3
  baseurl_source: declared
  description: Endpoint for getting Branch data
  name: Metro Bank Branch API
  slug: metro-bank-branch-api
- baseURL: https://api.metrobankonline.co.uk/open-banking/v2.3
  baseurl_source: declared
  description: Endpoint for getting Commercial Credit Card data
  name: Metro Bank CCC API
  slug: metro-bank-ccc-api
- baseURL: https://api.metrobankonline.co.uk/open-banking/v2.3
  baseurl_source: declared
  description: Endpoint for getting Personal Current Account data
  name: Metro Bank PCA API
  slug: metro-bank-pca-api
- baseURL: https://api.metrobankonline.co.uk/open-banking/v2.3
  baseurl_source: declared
  description: Endpoint for getting Unsecured SME Loan data
  name: Metro Bank SME API
  slug: metro-bank-sme-api
artifact_total: 15
collections:
- collection_type: open
  name: Open Data API
  slug: open-obie-open-data-api-standard-v1
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/metro-bank-capability-edges.yml
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
  type: X-MCPServerCandidate
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
modified: '2026-07-23'
name: Metro Bank
nav: Providers
network: true
overview: 'Metro Bank publishes 6 APIs on the [APIs.io](https://apis.io/) network, including ATM API, BCA API, Branch API, and 3 more. Tagged areas include Financial-Services, Banking, Open Banking, PSD2, and OBIE.


  Metro Bank''s developer surface includes authentication, documentation, engineering blog, support, and 18 more developer resources.'
random_paper: 0
scopes:
- name: Metro Bank Scopes
  scope_count: 4
  slug: metro-bank-scopes
  summary_line: 4 scopes · authorizationCode/clientCredentials
score:
  band: thin
  composite: 37.3
  coverage:
    artifact_dirs: 19
    catalog_gap: 63.0
    catalog_max: 100.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.6
    commercial_clarity: 28.6
    contract_governance: 18.2
    contract_quality: 32.7
    developer_ergonomics: 42.3
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 37.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
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
    score: 65.8
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/metro-bank/refs/heads/main/screenshots/metro-bank-2026-08-07T172746.png
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
- Financial-Services
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
