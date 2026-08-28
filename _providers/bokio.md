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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.6
  scored_at: '2026-08-26'
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
artifact_total: 55
collections:
- collection_type: postman
  name: Company authorization API
  slug: postman-bokio-authorization-api
- collection_type: postman
  name: Company authorization bank-payments API
  slug: postman-bokio-bank-payments-api
- collection_type: postman
  name: Company authorization chart-of-accounts API
  slug: postman-bokio-chart-of-accounts-api
- collection_type: postman
  name: Company authorization company-information API
  slug: postman-bokio-company-information-api
- collection_type: postman
  name: Company authorization connections API
  slug: postman-bokio-connections-api
- collection_type: postman
  name: Company authorization credit-notes API
  slug: postman-bokio-credit-notes-api
- collection_type: postman
  name: Company authorization customers API
  slug: postman-bokio-customers-api
- collection_type: postman
  name: Company authorization fiscal-years API
  slug: postman-bokio-fiscal-years-api
- collection_type: postman
  name: Company authorization invoices API
  slug: postman-bokio-invoices-api
- collection_type: postman
  name: Company authorization items API
  slug: postman-bokio-items-api
- collection_type: postman
  name: Company authorization journal-entries API
  slug: postman-bokio-journal-entries-api
- collection_type: postman
  name: Company authorization sie-files API
  slug: postman-bokio-sie-files-api
- collection_type: postman
  name: Company authorization supplier-invoices API
  slug: postman-bokio-supplier-invoices-api
- collection_type: postman
  name: Company authorization suppliers API
  slug: postman-bokio-suppliers-api
- collection_type: postman
  name: Company authorization tag-groups API
  slug: postman-bokio-tag-groups-api
- collection_type: postman
  name: Company authorization uploads API
  slug: postman-bokio-uploads-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Company authorization API
  slug: open-bokio-authorization-api
- collection_type: open
  name: Company authorization bank-payments API
  slug: open-bokio-bank-payments-api
- collection_type: open
  name: Company authorization chart-of-accounts API
  slug: open-bokio-chart-of-accounts-api
- collection_type: open
  name: Company authorization company-information API
  slug: open-bokio-company-information-api
- collection_type: open
  name: Company authorization connections API
  slug: open-bokio-connections-api
- collection_type: open
  name: Company authorization credit-notes API
  slug: open-bokio-credit-notes-api
- collection_type: open
  name: Company authorization customers API
  slug: open-bokio-customers-api
- collection_type: open
  name: Company authorization fiscal-years API
  slug: open-bokio-fiscal-years-api
- collection_type: open
  name: Company authorization invoices API
  slug: open-bokio-invoices-api
- collection_type: open
  name: Company authorization items API
  slug: open-bokio-items-api
- collection_type: open
  name: Company authorization journal-entries API
  slug: open-bokio-journal-entries-api
- collection_type: open
  name: Company authorization sie-files API
  slug: open-bokio-sie-files-api
- collection_type: open
  name: Company authorization supplier-invoices API
  slug: open-bokio-supplier-invoices-api
- collection_type: open
  name: Company authorization suppliers API
  slug: open-bokio-suppliers-api
- collection_type: open
  name: Company authorization tag-groups API
  slug: open-bokio-tag-groups-api
- collection_type: open
  name: Company authorization uploads API
  slug: open-bokio-uploads-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/bokio-company-api-overlay.yaml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/bokio/overview
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
  name: Bokio MCP Server
  slug: bokio-mcp-server
modified: '2026-07-18'
name: Bokio
nav: Providers
network: true
overview: 'Bokio publishes 16 APIs on the [APIs.io](https://apis.io/) network, including authorization API, bank-payments API, chart-of-accounts API, and 13 more. Tagged areas include Company, Fintech, Accounting, Bookkeeping, and Invoicing.


  Bokio''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 28 more developer resources.'
random_paper: 7
scopes:
- name: Bokio Scopes
  scope_count: 24
  slug: bokio-scopes
  summary_line: 24 scopes · clientCredentials/authorizationCode
score:
  band: strong
  composite: 54.6
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 16.7
    contract_quality: 58.9
    developer_ergonomics: 47.0
    discoverability: 92.6
    governance: 16.7
    operational_transparency: 32.9
  previous_composite: 54.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 16
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 68.8
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bokio/refs/heads/main/screenshots/bokio-2026-07-25T203526.png
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
- Authentication
website: https://bokio.se/
---
