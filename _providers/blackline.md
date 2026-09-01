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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-01'
api_count: 7
apis:
- description: Manage accounting periods (open/close, list periods) in BlackLine.
  name: BlackLine Period API
  slug: blackline-period-api
- description: Create, read, and manage BlackLine user accounts.
  name: BlackLine User Management API
  slug: blackline-user-management-api
- description: Manage BlackLine teams and team membership.
  name: BlackLine Team Management API
  slug: blackline-team-management-api
- description: Retrieve reporting data from the BlackLine platform.
  name: BlackLine Reporting API
  slug: blackline-reporting-api
- description: Manage reconciliation items and supporting documents programmatically.
  name: BlackLine Account Reconciliation API
  slug: blackline-account-reconciliation-api
- description: Create and manage journal entries programmatically.
  name: BlackLine Journal Entry API
  slug: blackline-journal-entry-api
- description: Push transactions into BlackLine for automated matching.
  name: BlackLine Transaction Matching API
  slug: blackline-transaction-matching-api
artifact_total: 10
common:
- group: company
  title: ''
  type: Website
  url: https://www.blackline.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.blackline.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.blackline.com/apis
- group: docs
  title: ''
  type: APIReference
  url: https://developer.blackline.com/apis
- group: auth
  title: ''
  type: Authentication
  url: authentication/blackline-authentication.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://trust.blackline.com/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/blackline-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/blackline-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.blackline.com/why-blackline/security/
- group: auth
  title: ''
  type: TrustCenter
  url: security/blackline-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/blackline-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://www.blackline.com/blog/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.blackline.com/legal/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.blackline.com/legal/
created: '2026-07-17'
description: 'BlackLine is a cloud-based financial operations (FinOps) and accounting automation platform that helps finance and accounting teams automate the financial close, account reconciliation, journal entry, transaction matching, intercompany, consolidation integrity, and reporting processes. BlackLine exposes a suite of RESTful APIs on its developer portal so customers and partners can integrate the platform with ERP systems, banking platforms, payroll, and reporting tools — covering period management, user and team management, account reconciliation, journals, task management, transaction matching, and reporting. APIs authenticate with OAuth 2.0 client credentials. BlackLine (NASDAQ: BL) is a public company surfaced in the API Evangelist network as a portfolio company of ICONIQ Capital.'
image: https://a.storyblok.com/f/213807/1200x630/d2bcfbe58d/blackline-future-ready-financial-operations.jpg
layout: provider
modified: '2026-07-18'
name: BlackLine
nav: Providers
network: true
overview: 'BlackLine publishes 7 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, FinOps, Accounting, and Financial Close.


  BlackLine''s developer surface includes documentation, API reference, authentication, engineering blog, and 10 more developer resources.'
random_paper: 9
score:
  band: emerging
  composite: 21.9
  coverage:
    artifact_dirs: 5
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 74.1
    governance: 18.2
    operational_transparency: 15.8
  previous_composite: 21.9
  provenance:
    conformance: first-party
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/blackline/refs/heads/main/screenshots/blackline-2026-07-25T203251.png
security:
- kind: authentication
  name: Blackline Authentication
  slug: blackline-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Blackline Domain Security
  slug: blackline-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Blackline Trust Center
  slug: blackline-trust-center
  summary_line: SOC 1 Type 2, SOC 2 Type 2, SOC 3, ISO/IEC 27001, ISO/IEC 27017, ISO/IEC 27018, ISO/IEC 27701, ISO/IEC 42001
slug: blackline
tags:
- Company
- Fintech
- FinOps
- Accounting
- Financial Close
- Reconciliation
- Accounting Automation
- ERP Integration
- Enterprise Software
website: https://www.blackline.com/
---
