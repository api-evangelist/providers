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
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Microsoft Office Suite Agentic Access
  operation_count: 15
  slug: microsoft-office-suite-agentic-access
  summary_line: 15 operations · 4 acting
api_count: 10
apis:
- description: JavaScript API for building add-ins and automating Microsoft Word.
  name: Word API (Office.js)
  slug: word-api-officejs
- description: JavaScript API for building add-ins and automating Microsoft Excel.
  name: Excel API (Office.js)
  slug: excel-api-officejs
- description: JavaScript API for building add-ins and automating Microsoft PowerPoint.
  name: PowerPoint API (Office.js)
  slug: powerpoint-api-officejs
- description: JavaScript API for building add-ins and automating Microsoft Outlook.
  name: Outlook API (Office.js)
  slug: outlook-api-officejs
- description: API for accessing and managing files stored in OneDrive.
  name: OneDrive API
  slug: onedrive-api
- description: API for accessing and managing SharePoint sites, lists, and documents.
  name: SharePoint REST API
  slug: sharepoint-rest-api
- description: API for building apps and bots integrated with Microsoft Teams.
  name: Microsoft Teams API
  slug: microsoft-teams-api
- description: The Drive API from Microsoft Office Suite — 4 operation(s) for drive.
  name: Microsoft Office Suite Drive API
  slug: microsoft-office-suite-drive-api
- description: The Mail API from Microsoft Office Suite — 4 operation(s) for mail.
  name: Microsoft Office Suite Mail API
  slug: microsoft-office-suite-mail-api
- description: The Teams API from Microsoft Office Suite — 4 operation(s) for teams.
  name: Microsoft Office Suite Teams API
  slug: microsoft-office-suite-teams-api
artifact_total: 23
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Microsoft Graph API - Office Suite Drive API
  slug: open-microsoft-office-suite-drive-api
- collection_type: open
  name: Microsoft Graph API - Office Suite Drive Mail API
  slug: open-microsoft-office-suite-mail-api
- collection_type: open
  name: Microsoft Graph API - Office Suite Drive Teams API
  slug: open-microsoft-office-suite-teams-api
- collection_type: open
  name: Microsoft Graph API - Office Suite
  slug: open-microsoft-office-suite
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-office-suite-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/microsoft-office-suite-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-office-suite-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-office-suite-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-office-suite-scopes.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.microsoft.com/
- group: operate
  title: ''
  type: Support
  url: https://support.microsoft.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.office.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.microsoft.com/en-us/servicesagreement
- group: company
  title: ''
  type: Blog
  url: https://www.microsoft.com/en-us/microsoft-365/blog/feed/
created: '2024-01-15'
description: Collection of APIs for Microsoft Office Suite applications and services.
finops:
- name: Microsoft Office Suite Finops
  service_category: API
  slug: microsoft-office-suite-finops
image: https://www.microsoft.com/en-us/microsoft-365/blog/wp-content/uploads/sites/2/2020/04/Microsoft365.png
layout: provider
modified: '2026-04-28'
name: Microsoft Office Suite
nav: Providers
network: true
overview: 'Microsoft Office Suite publishes 3 APIs on the [APIs.io](https://apis.io/) network: Drive API, Mail API, and Teams API. Tagged areas include Cloud, Collaboration, Documents, Microsoft 365, and Office.


  Microsoft Office Suite''s developer surface includes authentication, support, engineering blog, and 8 more developer resources.'
plans:
- name: Microsoft Office Suite Plans Pricing
  plan_count: 3
  slug: microsoft-office-suite-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 5
  name: Microsoft Office Suite Rate Limits
  slug: microsoft-office-suite-rate-limits
scopes:
- name: Microsoft Office Suite Scopes
  scope_count: 7
  slug: microsoft-office-suite-scopes
  summary_line: 7 scopes · authorizationCode
score:
  band: thin
  composite: 34.3
  delta: -1.6
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 51.7
    developer_ergonomics: 28.6
    discoverability: 72.2
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 35.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-office-suite/refs/heads/main/screenshots/microsoft-office-suite-2026-06-20T185516.png
security:
- kind: authentication
  name: Microsoft Office Suite Authentication
  slug: microsoft-office-suite-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Microsoft Office Suite Domain Security
  slug: microsoft-office-suite-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Microsoft Office Suite Vulnerability Disclosure
  slug: microsoft-office-suite-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: microsoft-office-suite
tags:
- Cloud
- Collaboration
- Documents
- Microsoft 365
- Office
- Productivity
website: https://developer.microsoft.com/
---
