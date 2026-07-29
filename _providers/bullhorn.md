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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 12.6
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: REST API over the Bullhorn Staffing Object Model — CRUD, query, Lucene search, mass update, resume parsing, and file attachments across Candidate, JobOrder, Placement, ClientCorporation, ClientContact
  name: Bullhorn REST API
  slug: bullhorn-rest-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.bullhorn.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.bullhorn.com
- group: docs
  title: ''
  type: Documentation
  url: https://bullhorn.github.io/rest-api-docs/
- group: docs
  title: ''
  type: APIReference
  url: https://bullhorn.github.io/rest-api-docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://bullhorn.github.io/rest-api-docs/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bullhorn
- group: operate
  title: ''
  type: Support
  url: https://www.bullhorn.com/support/
- group: company
  title: ''
  type: Blog
  url: https://www.bullhorn.com/blog/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.bullhorn.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.bullhorn.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://www.bullhorn.com/request-a-demo/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bullhorn.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bullhorn.com/privacy-policy/
- group: auth
  title: ''
  type: Authentication
  url: authentication/bullhorn-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/bullhorn-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/bullhorn-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/bullhorn-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/bullhorn-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/bullhorn-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/bullhorn-cli.yml
- group: design
  title: ''
  type: Components
  url: components/bullhorn-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/bullhorn-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/bullhorn-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.bullhorn.com/security/
- group: auth
  title: ''
  type: TrustCenter
  url: security/bullhorn-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bullhorn-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bullhorn-llms.txt
created: '2026-07-17'
description: Bullhorn is a cloud-based CRM and applicant tracking system (ATS) built for the staffing and recruitment industry. Its REST API exposes the Bullhorn Staffing Object Model — Candidate, JobOrder, JobSubmission, Placement, ClientCorporation, ClientContact, Lead, Opportunity, Note, Appointment and related entities — with full CRUD, DB-backed query, Lucene full-text search, mass update, resume parsing, and file-attachment operations. Authentication is OAuth 2.0 (authorization_code + refresh_token) exchanged via a /login call for a short-lived BhRestToken session; API traffic routes to data-center-specific hosts discovered through the loginInfo endpoint. Bullhorn also publishes an official Java SDK, a Passport.js OAuth strategy, the Novo Elements Angular UI component library, and a CSV Data Loader CLI.
image: https://www.bullhorn.com/wp-content/themes/bullhorn/assets/images/bullhorn-logo.svg
layout: provider
modified: '2026-07-18'
name: Bullhorn
nav: Providers
network: true
overview: 'Bullhorn publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Staffing, Recruitment, Applicant Tracking, and ATS.


  Bullhorn''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 20 more developer resources.'
random_paper: 60
score:
  band: thin
  composite: 37.0
  delta: -0.1
  facets:
    commercial_clarity: 60.5
    contract_quality: 0.0
    developer_ergonomics: 65.2
    discoverability: 75.9
    governance: 12.5
    operational_transparency: 21.1
  previous_composite: 37.1
  provenance:
    conformance: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bullhorn/refs/heads/main/screenshots/bullhorn-2026-07-25T204058.png
security:
- kind: authentication
  name: Bullhorn Authentication
  slug: bullhorn-authentication
  summary_line: oauth2/session-token · 2 schemes
- kind: domain-security
  name: Bullhorn Domain Security
  slug: bullhorn-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Bullhorn Trust Center
  slug: bullhorn-trust-center
  summary_line: SOC 2, GDPR
slug: bullhorn
tags:
- Company
- Staffing
- Recruitment
- Applicant Tracking
- ATS
- CRM
- Human Resources
- REST
- OAuth
website: https://www.bullhorn.com/
---
