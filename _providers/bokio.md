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
  band: agent-native
  dimensions:
    agent_skills: true
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: true
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.1
  score: 64.4
  scored_at: '2026-07-23'
api_count: 16
apis:
- description: Authorization operations for OAuth 2.0 Grants
  name: Bokio authorization API
  slug: bokio-authorization-api
- description: Operations for creating and reading bank payments
  name: Bokio bank-payments API
  slug: bokio-bank-payments-api
- description: Operations for managing chart of accounts
  name: Bokio chart-of-accounts API
  slug: bokio-chart-of-accounts-api
- description: Operations for managing company information
  name: Bokio company-information API
  slug: bokio-company-information-api
- description: Connections operations
  name: Bokio connections API
  slug: bokio-connections-api
- description: Operations for managing credit notes
  name: Bokio credit-notes API
  slug: bokio-credit-notes-api
- description: Operations for managing customer data
  name: Bokio customers API
  slug: bokio-customers-api
- description: Operations for managing fiscal years
  name: Bokio fiscal-years API
  slug: bokio-fiscal-years-api
- description: Operations for managing invoices
  name: Bokio invoices API
  slug: bokio-invoices-api
- description: Operations for managing inventory items
  name: Bokio items API
  slug: bokio-items-api
- description: Operations for managing accounting journal entries
  name: Bokio journal-entries API
  slug: bokio-journal-entries-api
- description: Operations for managing SIE files
  name: Bokio sie-files API
  slug: bokio-sie-files-api
- description: Operations for managing supplier invoices
  name: Bokio supplier-invoices API
  slug: bokio-supplier-invoices-api
- description: Operations for managing suppliers
  name: Bokio suppliers API
  slug: bokio-suppliers-api
- description: Operations for managing tag groups and tags
  name: Bokio tag-groups API
  slug: bokio-tag-groups-api
- description: Operations for managing file uploads
  name: Bokio uploads API
  slug: bokio-uploads-api
artifact_total: 22
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.bokio.se/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.bokio.se/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.bokio.se/reference/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.bokio.se/docs/welcome
- group: operate
  title: ''
  type: Support
  url: mailto:support@bokio.se
- group: company
  title: ''
  type: Blog
  url: https://www.bokio.se/blogg/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bokio
- group: commercial
  title: ''
  type: Pricing
  url: https://www.bokio.se/priser/
- group: start
  title: ''
  type: SignUp
  url: https://app.bokio.se/sign-up
- group: start
  title: ''
  type: Login
  url: https://app.bokio.se/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docs.bokio.se/page/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bokio.se/villkor-och-gdpr/integritetspolicy/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/bokio-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/bokio-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.bokio.se/reference/versioning
- group: auth
  title: ''
  type: Authentication
  url: authentication/bokio-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/bokio-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/bokio-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://docs.bokio.se/reference/rate-limits
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/bokio-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/bokio-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/bokio-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/bokio-sandbox.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/bokio-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bokio-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/bokio-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/bokio-security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/bokio-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.visma.com/trust-centre/security/products-and-services/bug-bounty-and-responsible-disclosure/
- group: auth
  title: ''
  type: TrustCenter
  url: security/bokio-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bokio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bokio.se/
created: '2026-07-17'
description: Bokio is a Swedish cloud accounting and bookkeeping platform (a Visma company) for small businesses, sole traders and their accountants, combining automated bookkeeping, invoicing, a business bank account and financial reporting. Its public REST API is split into a Company API (journal entries, invoices, credit notes, customers, items, suppliers and supplier invoices, uploads, bank payments, chart of accounts, fiscal years and SIE export) and a General API that handles OAuth 2.0 token issuance and connection management for public multi-tenant integrations. Authentication is OAuth 2.0 (authorization code and client credentials) with 24 fine-grained resource:action scopes; the API uses URI-path versioning (v1), page-number pagination, per-token rate limits and a documented deprecation, brownout and sunset lifecycle.
image: https://www.bokio.se/media/38801/open-graph.png?width=1200
layout: provider
mcp_servers:
- description: ''
  name: bokio-mcp.yml
  slug: bokio-mcpyml
modified: '2026-07-18'
name: Bokio
nav: Providers
network: true
overview: 'Bokio publishes 16 APIs on the [APIs.io](https://apis.io/) network, including authorization API, bank-payments API, chart-of-accounts API, and 13 more. Tagged areas include Company, Fintech, Accounting, Bookkeeping, and Invoicing.


  Bokio''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 26 more developer resources.'
random_paper: 22
scopes:
- name: Bokio Scopes
  scope_count: 24
  slug: bokio-scopes
  summary_line: 24 scopes · clientCredentials/authorizationCode
score:
  band: strong
  composite: 62.4
  delta: 6.7
  facets:
    commercial_clarity: 52.6
    contract_quality: 61.2
    developer_ergonomics: 73.9
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 39.5
  previous_composite: 55.7
  regulatory:
    applies: true
    regime: Payments
    regime_id: payments
    score: 100.0
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: rising
security:
- kind: authentication
  name: Bokio Authentication
  slug: bokio-authentication
  summary_line: http/oauth2 · 3 schemes
- kind: domain-security
  name: Bokio Domain Security
  slug: bokio-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Bokio Vulnerability Disclosure
  slug: bokio-vulnerability-disclosure
  summary_line: Intigriti · security.txt · contact published
- kind: trust-center
  name: Bokio Trust Center
  slug: bokio-trust-center
  summary_line: trust center published
slug: bokio
tags:
- Company
- Fintech
- Accounting
- Bookkeeping
- Invoicing
- Payments
- Sweden
- SMB
- OAuth
website: https://bokio.se/
---
