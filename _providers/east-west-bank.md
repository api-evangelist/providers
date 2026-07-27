---
agent_readiness:
  band: human-only
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 9.6
  scored_at: '2026-07-27'
api_count: 1
apis:
- description: East West Bank's first-party commercial banking API program, delivered through the "Bridge Open Banking" developer portal for Global Transaction Services (GTS) clients. Documented capabilities let app
  name: East West Bank Bridge Open Banking API
  slug: bridge-open-banking-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/east-west-bank-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.eastwestbank.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://apiportal.eastwestbank.com/
- group: docs
  title: ''
  type: Documentation
  url: https://apiportal.eastwestbank.com/how-it-works
- group: operate
  title: ''
  type: Support
  url: https://apiportal.eastwestbank.com/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://apiportal.eastwestbank.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/eastwestbank
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/east-west-bank
- group: auth
  title: ''
  type: Authentication
  url: authentication/east-west-bank-authentication.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/east-west-bank-sandbox.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/east-west-bank-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/east-west-bank-llms.txt
- group: start
  title: ''
  type: GettingStarted
  url: https://apiportal.eastwestbank.com/how-it-works
- group: start
  title: ''
  type: SignUp
  url: https://apiportal.eastwestbank.com/signup
- group: start
  title: ''
  type: Login
  url: https://apiportal.eastwestbank.com/signin
- group: commercial
  title: ''
  type: TermsOfService
  url: https://apiportal.eastwestbank.com/terms-and-conditions
- group: operate
  title: ''
  type: HelpCenter
  url: https://apiportal.eastwestbank.com/faqs
created: '2026-07-23'
description: East West Bank is the California state-chartered commercial banking subsidiary of East West Bancorp, Inc. (NASDAQ EWBC), headquartered in Pasadena, California, with roughly $79.7 billion in total assets and more than 125 locations across the United States and Greater China. A Member FDIC institution and one of the few U.S. banks holding a full banking license in China, it specializes in cross-border U.S.-China commercial banking, treasury and Global Transaction Services (GTS). On the open-finance front, East West Bank runs a first-party developer portal ("Bridge Open Banking" at apiportal.eastwestbank.com) aimed at commercial clients, documenting APIs to manage sub-accounts, retrieve balances, transfer funds, and obtain commercial account information, with a sandbox of live test accounts; the program is early-stage ("more APIs coming soon") and gated behind sales onboarding, so no OpenAPI/Swagger is publicly downloadable. Consumer-permissioned data access is also available indirectly
  through the Plaid aggregator. No public FDX participation or CFPB Section 1033 posture is documented as of this profile.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-23'
name: East West Bank
nav: Providers
network: true
overview: 'East West Bank publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Financial Services, Banking, United States, Commercial Banking, and Treasury Management.


  East West Bank''s developer surface includes documentation, support, authentication, sandbox, getting-started guide, signup flow, and 11 more developer resources.'
random_paper: 22
score:
  band: emerging
  composite: 29.8
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 50.0
    discoverability: 80.0
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 29.8
  regulatory:
    applies: true
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 54.3
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/east-west-bank/refs/heads/main/screenshots/east-west-bank-2026-07-25T212711.png
security:
- kind: authentication
  name: East West Bank Authentication
  slug: east-west-bank-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: East West Bank Domain Security
  slug: east-west-bank-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: east-west-bank
tags:
- Financial Services
- Banking
- United States
- Commercial Banking
- Treasury Management
- Cross-Border
- Open Finance
- Data Aggregation
website: https://www.eastwestbank.com/
---
