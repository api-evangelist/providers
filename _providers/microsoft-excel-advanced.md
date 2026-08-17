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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Microsoft Excel Advanced Agentic Access
  operation_count: 22
  slug: microsoft-excel-advanced-agentic-access
  summary_line: 22 operations · 13 acting
api_count: 14
apis:
- description: TypeScript-based automation API for Excel on the web and desktop.
  name: Office Scripts API
  slug: office-scripts-api
- description: JavaScript API for building Excel add-ins and extensions.
  name: Excel JavaScript API
  slug: excel-javascript-api
- description: API for creating custom functions in Excel using JavaScript.
  name: Excel Custom Functions API
  slug: excel-custom-functions-api
- description: REST API for accessing Excel files stored in OneDrive and SharePoint.
  name: Excel REST API (OneDrive)
  slug: excel-rest-api-onedrive
- description: Pre-built connector for automating Excel workflows in Power Automate.
  name: Power Automate Excel Connector
  slug: power-automate-excel-connector
- description: Chart operations
  name: Microsoft Excel (Advanced) Charts API
  slug: microsoft-excel-advanced-charts-api
- description: Workbook function calls
  name: Microsoft Excel (Advanced) Functions API
  slug: microsoft-excel-advanced-functions-api
- description: Named item operations
  name: Microsoft Excel (Advanced) NamedItems API
  slug: microsoft-excel-advanced-nameditems-api
- description: Range cell operations
  name: Microsoft Excel (Advanced) Range API
  slug: microsoft-excel-advanced-range-api
- description: Workbook session management
  name: Microsoft Excel (Advanced) Sessions API
  slug: microsoft-excel-advanced-sessions-api
- description: Operations on table columns
  name: Microsoft Excel (Advanced) TableColumns API
  slug: microsoft-excel-advanced-tablecolumns-api
- description: Operations on table rows
  name: Microsoft Excel (Advanced) TableRows API
  slug: microsoft-excel-advanced-tablerows-api
- description: Excel table operations
  name: Microsoft Excel (Advanced) Tables API
  slug: microsoft-excel-advanced-tables-api
- description: Worksheet operations
  name: Microsoft Excel (Advanced) Worksheets API
  slug: microsoft-excel-advanced-worksheets-api
artifact_total: 33
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Microsoft Graph Excel Charts API
  slug: open-microsoft-excel-advanced-charts-api
- collection_type: open
  name: Microsoft Graph Excel Charts Functions API
  slug: open-microsoft-excel-advanced-functions-api
- collection_type: open
  name: Microsoft Graph Excel Charts NamedItems API
  slug: open-microsoft-excel-advanced-nameditems-api
- collection_type: open
  name: Microsoft Graph Excel Charts Range API
  slug: open-microsoft-excel-advanced-range-api
- collection_type: open
  name: Microsoft Graph Excel Charts Sessions API
  slug: open-microsoft-excel-advanced-sessions-api
- collection_type: open
  name: Microsoft Graph Excel Charts TableColumns API
  slug: open-microsoft-excel-advanced-tablecolumns-api
- collection_type: open
  name: Microsoft Graph Excel Charts TableRows API
  slug: open-microsoft-excel-advanced-tablerows-api
- collection_type: open
  name: Microsoft Graph Excel Charts Tables API
  slug: open-microsoft-excel-advanced-tables-api
- collection_type: open
  name: Microsoft Graph Excel Charts Worksheets API
  slug: open-microsoft-excel-advanced-worksheets-api
- collection_type: open
  name: Microsoft Graph Excel API
  slug: open-microsoft-excel-advanced
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-excel-advanced-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/microsoft-excel-advanced-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-excel-advanced-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-excel-advanced-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-excel-advanced-scopes.yml
- group: start
  title: ''
  type: Portal
  url: https://developer.microsoft.com/en-us/microsoft-365
- group: docs
  title: ''
  type: Authentication Guide
  url: https://learn.microsoft.com/en-us/azure/active-directory/develop/
- group: build
  title: ''
  type: SDKs
  url: https://learn.microsoft.com/en-us/graph/sdks/sdks-overview
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cloud.microsoft/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.microsoft.com/en-us/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/
created: '2024-01-01'
description: Advanced automation and integration APIs for Microsoft Excel, enabling programmatic access to spreadsheet data, formulas, charts, and automation capabilities through Microsoft Graph, Office Scripts, JavaScript add-ins, custom functions, OneDrive REST endpoints, and Power Automate connectors.
finops:
- name: Microsoft Excel Advanced Finops
  service_category: API
  slug: microsoft-excel-advanced-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-excel-advanced.png
layout: provider
modified: '2026-04-28'
name: Microsoft Excel (Advanced)
nav: Providers
network: true
overview: 'Microsoft Excel (Advanced) publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Charts API, Functions API, NamedItems API, and 6 more. Tagged areas include Automation, Business Intelligence, Data Analysis, Office, and Spreadsheets.


  Microsoft Excel (Advanced)''s developer surface includes authentication, developer portal, and 9 more developer resources.'
plans:
- name: Microsoft Excel Advanced Plans Pricing
  plan_count: 3
  slug: microsoft-excel-advanced-plans-pricing
random_paper: 39
rate_limits:
- limit_count: 5
  name: Microsoft Excel Advanced Rate Limits
  slug: microsoft-excel-advanced-rate-limits
scopes:
- name: Microsoft Excel Advanced Scopes
  scope_count: 4
  slug: microsoft-excel-advanced-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: thin
  composite: 35.9
  delta: 0.0
  facets:
    commercial_clarity: 36.8
    contract_quality: 55.2
    developer_ergonomics: 26.1
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 35.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-excel-advanced/refs/heads/main/screenshots/microsoft-excel-advanced-2026-06-20T185500.png
security:
- kind: authentication
  name: Microsoft Excel Advanced Authentication
  slug: microsoft-excel-advanced-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Microsoft Excel Advanced Domain Security
  slug: microsoft-excel-advanced-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Microsoft Excel Advanced Vulnerability Disclosure
  slug: microsoft-excel-advanced-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: microsoft-excel-advanced
tags:
- Automation
- Business Intelligence
- Data Analysis
- Office
- Spreadsheets
website: https://developer.microsoft.com/en-us/microsoft-365
---
