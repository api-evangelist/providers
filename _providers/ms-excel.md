---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Ms Excel Agentic Access
  operation_count: 13
  slug: ms-excel-agentic-access
  summary_line: 13 operations · 6 acting
api_count: 1
apis:
- description: The Me API from Microsoft Excel API — 9 operation(s) for me.
  name: Microsoft Excel API Me API
  slug: ms-excel-me-api
artifact_total: 10
collections:
- collection_type: open
  name: Microsoft Graph Excel API
  slug: open-ms-excel
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ms-excel-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ms-excel-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ms-excel-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ms-excel-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/ms-excel-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/microsoft
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.microsoft.com/en-us/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: operate
  title: ''
  type: Support
  url: https://developer.microsoft.com/en-us/graph/support
- group: company
  title: ''
  type: Blog
  url: https://developer.microsoft.com/en-us/graph/blogs/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.dev.microsoft.com/
created: '2024'
description: APIs for interacting with Microsoft Excel files and workbooks through Microsoft Graph.
finops:
- name: Ms Excel Finops
  service_category: API
  slug: ms-excel-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ms-excel.png
layout: provider
modified: '2026-04-28'
name: Microsoft Excel API
nav: Providers
network: true
overview: 'Microsoft Excel API publishes 1 API on the [APIs.io](https://apis.io/) network: Me API. Tagged areas include Data Analysis, Excel, Microsoft Graph, Office 365, and Spreadsheets.


  Microsoft Excel API''s developer surface includes authentication, support, engineering blog, and 8 more developer resources.'
plans:
- name: Ms Excel Plans Pricing
  plan_count: 3
  slug: ms-excel-plans-pricing
random_paper: 60
rate_limits:
- limit_count: 5
  name: Ms Excel Rate Limits
  slug: ms-excel-rate-limits
scopes:
- name: Ms Excel Scopes
  scope_count: 2
  slug: ms-excel-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: developing
  composite: 42.4
  delta: -0.8
  facets:
    commercial_clarity: 60.5
    contract_quality: 53.4
    developer_ergonomics: 17.4
    discoverability: 66.7
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 43.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ms-excel/refs/heads/main/screenshots/ms-excel-2026-06-20T185845.png
security:
- kind: authentication
  name: Ms Excel Authentication
  slug: ms-excel-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Ms Excel Domain Security
  slug: ms-excel-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Ms Excel Vulnerability Disclosure
  slug: ms-excel-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: ms-excel
tags:
- Data Analysis
- Excel
- Microsoft Graph
- Office 365
- Spreadsheets
website: https://developer.microsoft.com/en-us/graph/docs/api-reference/v1.0/resources/excel
---
