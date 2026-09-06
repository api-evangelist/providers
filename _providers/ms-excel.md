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
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Ms Excel Agentic Access
  operation_count: 13
  slug: ms-excel-agentic-access
  summary_line: 13 operations · 6 acting
api_count: 1
apis:
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: The Me API from Microsoft Excel API — 9 operation(s) for me.
  name: Microsoft Excel API Me API
  slug: ms-excel-me-api
artifact_total: 12
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Microsoft Graph Excel Me API
  slug: open-ms-excel-me-api
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
random_paper: 0
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
  band: thin
  composite: 37.1
  coverage:
    artifact_dirs: 11
    catalog_earned: 41.0
    catalog_earned_first_party: 0.0
    catalog_gap: 74.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 50.3
    developer_ergonomics: 40.5
    discoverability: 66.7
    governance: 0.0
    operational_transparency: 18.4
  previous_composite: 37.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.18.3
  scored_at: '2026-09-05'
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
