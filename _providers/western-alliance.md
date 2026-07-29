---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 12.6
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: Western Alliance Bank's commercial open-banking API lets approved business clients interact directly with WAB systems to access balance and transaction information, retrieve check images, initiate fun
  name: Western Alliance Bank API (Treasury Management)
  slug: wab-treasury-management-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/western-alliance-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/western-alliance-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/western-alliance-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/western-alliance-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/western-alliance-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.westernalliancebancorporation.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.westernalliancebank.com/s/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.westernalliancebank.com/s/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.westernalliancebank.com/s/apis
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.westernalliancebank.com/s/getting-started
- group: start
  title: ''
  type: SignUp
  url: https://developer.westernalliancebank.com/s/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/westernalliancebank
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/western-alliance-bank
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.westernalliancebancorporation.com/privacy-legal-home/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.westernalliancebancorporation.com/sites/default/files/2025-05/api-services-terms-conditions.pdf
created: '2026-07-23'
description: 'Western Alliance Bancorporation (NYSE: WAL) is a Phoenix, Arizona based super-regional bank holding company with roughly $80 billion in assets, operating through its principal subsidiary Western Alliance Bank, an Arizona state-chartered commercial bank and member FDIC that runs regional divisions including Alliance Bank of Arizona, Bank of Nevada, Bridge Bank, and Torrey Pines Bank. It is a commercial- and business-banking focused institution rather than a consumer neobank. Western Alliance runs a real first-party developer portal, the WAB API Developer Portal ("Developer Hub") at developer.westernalliancebank.com, exposing commercial Treasury Management open-banking APIs for balance and transaction information, check images, funds transfers, and stop payments. Access is partner/customer-gated: API specifications are downloaded from the Developer Hub only with WAB-issued credentials, and authentication uses OAuth2 client-credentials (Client ID, Client Secret), a Client Certificate
  (mTLS), and access tokens across UAT and Production environments. Its APIs are also reachable through payment-platform partners such as Modern Treasury. No public consumer FDX or CFPB Section 1033 data-access API is documented, and no OpenAPI/Swagger is publicly downloadable.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-23'
name: Western Alliance Bank
nav: Providers
network: true
overview: 'Western Alliance Bank publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Financial Services, Banking, United States, Treasury Management, and Open Banking.


  Western Alliance Bank''s developer surface includes authentication, documentation, API reference, getting-started guide, signup flow, and 10 more developer resources.'
random_paper: 26
score:
  band: emerging
  composite: 27.9
  delta: -1.2
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 45.7
    discoverability: 77.8
    governance: 12.5
    operational_transparency: 5.3
  previous_composite: 29.1
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 39.2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Western Alliance Authentication
  slug: western-alliance-authentication
  summary_line: oauth2/mutualTLS · 3 schemes
- kind: domain-security
  name: Western Alliance Domain Security
  slug: western-alliance-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: western-alliance
tags:
- Financial Services
- Banking
- United States
- Treasury Management
- Open Banking
- Payments
- Commercial Banking
website: https://www.westernalliancebancorporation.com/
---
