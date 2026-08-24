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
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.5
  scored_at: '2026-08-24'
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
  name: Solaris MCP Server
  slug: solaris-mcp-server
modified: '2026-07-21'
name: Solaris
nav: Providers
network: true
overview: 'Solaris publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Banking, Banking as a Service, and Embedded Finance.


  The Solaris catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Solaris'' developer surface includes documentation, API reference, getting-started guide, support, changelog, authentication, sandbox, and 18 more developer resources.'
random_paper: 9
scopes:
- name: Solaris Scopes
  scope_count: 1
  slug: solaris-scopes
  summary_line: 1 scope · clientCredentials
score:
  band: developing
  composite: 50.4
  delta: 0.0
  facets:
    access_clarity: 18.4
    commercial_clarity: 18.4
    contract_governance: 18.2
    contract_quality: 45.1
    developer_ergonomics: 61.9
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 50.0
  previous_composite: 50.4
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 78.1
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/solaris/refs/heads/main/screenshots/solaris-2026-08-17T081954.png
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
- Authentication
- Webhook
- Germany
website: https://www.solarisgroup.com/
---
