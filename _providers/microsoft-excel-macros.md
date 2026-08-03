---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 12.2
  scored_at: '2026-08-03'
api_count: 3
apis:
- description: Core API for interacting with Excel objects, workbooks, worksheets, ranges, and cells through VBA automation.
  name: Excel VBA Object Model API
  slug: vba-object-model
- description: Modern JavaScript API for creating Excel add-ins and automating Excel through web technologies.
  name: Office JavaScript API for Excel
  slug: office-javascript-api
- description: Component Object Model interface for automating Excel from external applications.
  name: Excel COM Automation API
  slug: com-automation
artifact_total: 8
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/microsoft-excel-macros-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-excel-macros-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://developer.microsoft.com/en-us/microsoft-365
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/office/dev/add-ins/
- group: auth
  title: ''
  type: Authentication
  url: https://learn.microsoft.com/en-us/azure/active-directory/develop/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.office.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.microsoft.com/servicesagreement
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/
- group: operate
  title: ''
  type: Support
  url: https://support.microsoft.com/excel
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/OfficeDev
created: '2024-01-01'
description: A collection of APIs and resources for working with Microsoft Excel Macros, VBA automation, and Excel extensibility including the Office JavaScript API and COM automation.
finops:
- name: Microsoft Excel Macros Finops
  service_category: API
  slug: microsoft-excel-macros-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-excel-macros.png
layout: provider
modified: '2026-04-28'
name: Microsoft Excel Macros
nav: Providers
network: true
overview: 'Microsoft Excel Macros publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Automation, Excel, Macros, Microsoft, and Office.


  Microsoft Excel Macros'' developer surface includes developer portal, documentation, authentication, support, and 6 more developer resources.'
plans:
- name: Microsoft Excel Macros Plans Pricing
  plan_count: 3
  slug: microsoft-excel-macros-plans-pricing
random_paper: 61
rate_limits:
- limit_count: 5
  name: Microsoft Excel Macros Rate Limits
  slug: microsoft-excel-macros-rate-limits
score:
  band: thin
  composite: 31.0
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 0.0
    developer_ergonomics: 32.6
    discoverability: 55.6
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 31.0
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-excel-macros/refs/heads/main/screenshots/microsoft-excel-macros-2026-06-20T185500.png
security:
- kind: domain-security
  name: Microsoft Excel Macros Domain Security
  slug: microsoft-excel-macros-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Microsoft Excel Macros Vulnerability Disclosure
  slug: microsoft-excel-macros-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: microsoft-excel-macros
tags:
- Automation
- Excel
- Macros
- Microsoft
- Office
- Spreadsheets
- VBA
website: https://developer.microsoft.com/en-us/microsoft-365
---
