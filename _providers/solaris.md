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
  band: agent-aware
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.1
  score: 38.5
  scored_at: '2026-07-23'
api_count: 1
apis:
- description: The Solaris REST API for embedded banking, cards, payments (SEPA), KYC/KYB identity, and lending. OAuth2 client-credentials auth; HMAC-signed webhooks.
  name: Solaris Embedded Finance API
  slug: solaris-embedded-finance-api
artifact_total: 6
asyncapis:
- description: ''
  name: Solaris Webhooks
  slug: solaris-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/solaris-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.solarisgroup.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.solarisgroup.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.solarisgroup.com/guides
- group: docs
  title: ''
  type: APIReference
  url: https://docs.solarisgroup.com/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.solarisgroup.com/guides/get-started
- group: operate
  title: ''
  type: Support
  url: https://docs.solarisgroup.com/help
- group: operate
  title: ''
  type: StatusPage
  url: https://status.solarisgroup.com/
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.solarisgroup.com/api-reference/breaking-changes
- group: auth
  title: ''
  type: Compliance
  url: https://www.solarisgroup.com/en/license/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.solarisgroup.com/en/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/solarisBank
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.solarisgroup.com/release-notes
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/solaris-changelog.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/solaris-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/solaris-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/solaris-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/solaris-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/solaris-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/solaris-conformance.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/solaris-webhooks.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/solaris-sandbox.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/solaris-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/solaris-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/solaris-llms.txt
created: '2026-07-17'
description: 'Solaris SE is a Berlin-based embedded-finance / Banking-as-a-Service platform operating on a full German CRR commercial banking license. Its REST API lets partners embed regulated banking into their own products: digital banking with local German IBANs and SEPA credit transfers, direct debit and instant payments; debit and credit cards with 3D Secure, tokenization and spending controls; KYC/KYB identity verification (Bankident, VideoIdent, AutoIdent, Fourthline); and lending products including overdrafts, Splitpay and consumer and business loans. The API uses OAuth2 client-credentials bearer tokens, HMAC-SHA256-signed webhooks for ~80 real-time events, page-number pagination, and a structured Money object, and is certified under ISO/IEC 27001, PCI DSS 4.0, DORA and GDPR.'
image: https://docs.solarisgroup.com/static/solaris-signet-e6f33da6ebaffa690232d6cc1f63ee39.svg
layout: provider
mcp_servers:
- description: ''
  name: solaris-mcp.yml
  slug: solaris-mcpyml
modified: '2026-07-21'
name: Solaris
nav: Providers
network: true
overview: 'Solaris publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Banking, Banking as a Service, and Embedded Finance.


  The Solaris catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Solaris'' developer surface includes documentation, API reference, getting-started guide, support, changelog, authentication, sandbox, and 18 more developer resources.'
random_paper: 0
scopes:
- name: Solaris Scopes
  scope_count: 1
  slug: solaris-scopes
  summary_line: 1 scope · clientCredentials
score:
  band: thin
  composite: 44.4
  delta: 5.9
  facets:
    commercial_clarity: 18.4
    contract_quality: 22.6
    developer_ergonomics: 65.2
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 38.5
  regulatory:
    applies: true
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 78.3
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: rising
security:
- kind: authentication
  name: Solaris Authentication
  slug: solaris-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Solaris Domain Security
  slug: solaris-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: solaris
tags:
- Company
- Fintech
- Banking
- Banking as a Service
- Embedded Finance
- Payments
- SEPA
- Cards
- KYC
- Lending
- Compliance
- OAuth2
- Webhooks
- Germany
website: https://www.solarisgroup.com/
---
