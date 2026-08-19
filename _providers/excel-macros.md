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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-19'
api_count: 3
apis:
- description: Core VBA API for interacting with Excel workbooks, worksheets, ranges, and other Excel objects through Visual Basic for Applications.
  name: Excel VBA Object Model API
  slug: excel-vba-api
- description: Modern TypeScript-based API for automating Excel tasks on the web and desktop, the cloud-first successor to VBA for Excel scenarios.
  name: Office Scripts API
  slug: office-scripts-api
- description: JavaScript API for building Excel add-ins and extending Excel functionality in web and desktop environments via Office.js.
  name: Excel JavaScript API
  slug: excel-javascript-api
artifact_total: 8
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/excel-macros-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/excel-macros-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://docs.microsoft.com/en-us/office/vba/api/overview/excel
- group: start
  title: ''
  type: Portal
  url: https://developer.microsoft.com/office
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.microsoft.com/en-us/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/OfficeDev
- group: operate
  title: ''
  type: CommunityForum
  url: https://techcommunity.microsoft.com/t5/excel/ct-p/Excel_Cat
created: '2025-01-20'
description: Excel Macros refer to automated sequences of actions in Microsoft Excel, primarily written using VBA (Visual Basic for Applications). Excel also supports Office Scripts (TypeScript) for cloud-based automation and the Excel JavaScript API for building Office Add-ins that run on the web, Windows, Mac, and iPad. These automation capabilities allow users to streamline repetitive tasks, manipulate workbooks, and extend Excel functionality.
finops:
- name: Excel Macros Finops
  service_category: API
  slug: excel-macros-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/excel-macros.png
layout: provider
modified: '2026-04-28'
name: Excel Macros
nav: Providers
network: true
overview: 'Excel Macros publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Automation, Excel, Macros, Microsoft Office, and VBA.


  Excel Macros'' developer surface includes documentation, developer portal, and 6 more developer resources.'
plans:
- name: Excel Macros Plans Pricing
  plan_count: 3
  slug: excel-macros-plans-pricing
random_paper: 27
rate_limits:
- limit_count: 5
  name: Excel Macros Rate Limits
  slug: excel-macros-rate-limits
score:
  band: emerging
  composite: 19.7
  delta: -0.1
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 72.2
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 19.8
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/excel-macros/refs/heads/main/screenshots/excel-macros-2026-06-20T180922.png
security:
- kind: domain-security
  name: Excel Macros Domain Security
  slug: excel-macros-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Excel Macros Vulnerability Disclosure
  slug: excel-macros-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: excel-macros
tags:
- Automation
- Excel
- Macros
- Microsoft Office
- VBA
- Office Scripts
- JavaScript
website: https://developer.microsoft.com/office
---
