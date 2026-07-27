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
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Microsoft Office Applications Agentic Access
  operation_count: 15
  slug: microsoft-office-applications-agentic-access
  summary_line: 15 operations · 4 acting
api_count: 10
apis:
- description: API for creating, editing, and managing Word documents.
  name: Word API
  slug: word-api
- description: API for creating, editing, and managing Excel spreadsheets.
  name: Excel API
  slug: excel-api
- description: API for creating, editing, and managing PowerPoint presentations.
  name: PowerPoint API
  slug: powerpoint-api
- description: API for accessing and managing email in Outlook.
  name: Outlook Mail API
  slug: outlook-mail-api
- description: API for creating and managing OneNote notebooks, sections, and pages.
  name: OneNote API
  slug: onenote-api
- description: API for accessing and managing files in OneDrive.
  name: OneDrive API
  slug: onedrive-api
- description: API for Microsoft Teams collaboration and communication.
  name: Teams API
  slug: teams-api
- description: The Drive API from Microsoft Office Applications — 4 operation(s) for drive.
  name: Microsoft Office Applications Drive API
  slug: microsoft-office-applications-drive-api
- description: The Mail API from Microsoft Office Applications — 4 operation(s) for mail.
  name: Microsoft Office Applications Mail API
  slug: microsoft-office-applications-mail-api
- description: The Teams API from Microsoft Office Applications — 4 operation(s) for teams.
  name: Microsoft Office Applications Teams API
  slug: microsoft-office-applications-teams-api
artifact_total: 19
collections:
- collection_type: open
  name: Microsoft Graph API - Office Applications
  slug: open-microsoft-office-applications
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-office-applications-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/microsoft-office-applications-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-office-applications-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-office-applications-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-office-applications-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/OfficeDev
- group: start
  title: ''
  type: Portal
  url: https://developer.microsoft.com/en-us/microsoft-365
- group: auth
  title: ''
  type: Authentication
  url: https://docs.microsoft.com/en-us/azure/active-directory/develop/
- group: company
  title: ''
  type: Blog
  url: https://developer.microsoft.com/en-us/microsoft-365/blogs/
- group: operate
  title: ''
  type: Support
  url: https://docs.microsoft.com/en-us/answers/products/m365
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docs.microsoft.com/en-us/legal/microsoft-apis/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
created: '2024'
description: APIs for Microsoft Office suite including Word, Excel, PowerPoint, Outlook, and other Office applications.
finops:
- name: Microsoft Office Applications Finops
  service_category: API
  slug: microsoft-office-applications-finops
image: https://www.microsoft.com/en-us/microsoft-365/blog/wp-content/uploads/sites/2/2020/04/Microsoft-365-logo.png
layout: provider
modified: '2026-04-28'
name: Microsoft Office Applications
nav: Providers
network: true
overview: 'Microsoft Office Applications publishes 3 APIs on the [APIs.io](https://apis.io/) network: Drive API, Mail API, and Teams API. Tagged areas include Documents, Office, Presentations, Productivity, and Spreadsheets.


  Microsoft Office Applications'' developer surface includes authentication, developer portal, engineering blog, support, and 8 more developer resources.'
plans:
- name: Microsoft Office Applications Plans Pricing
  plan_count: 3
  slug: microsoft-office-applications-plans-pricing
random_paper: 55
rate_limits:
- limit_count: 5
  name: Microsoft Office Applications Rate Limits
  slug: microsoft-office-applications-rate-limits
scopes:
- name: Microsoft Office Applications Scopes
  scope_count: 7
  slug: microsoft-office-applications-scopes
  summary_line: 7 scopes · authorizationCode
score:
  band: thin
  composite: 42.8
  delta: 3.2
  facets:
    commercial_clarity: 60.5
    contract_quality: 47.8
    developer_ergonomics: 26.1
    discoverability: 87.5
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 39.6
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-office-applications/refs/heads/main/screenshots/microsoft-office-applications-2026-06-20T185511.png
security:
- kind: authentication
  name: Microsoft Office Applications Authentication
  slug: microsoft-office-applications-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Microsoft Office Applications Domain Security
  slug: microsoft-office-applications-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Microsoft Office Applications Vulnerability Disclosure
  slug: microsoft-office-applications-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: microsoft-office-applications
tags:
- Documents
- Office
- Presentations
- Productivity
- Spreadsheets
website: https://developer.microsoft.com/en-us/microsoft-365
---
