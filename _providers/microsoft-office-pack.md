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
- acting_count: 4
  human_in_the_loop: 0
  name: Microsoft Office Pack Agentic Access
  operation_count: 15
  slug: microsoft-office-pack-agentic-access
  summary_line: 15 operations · 4 acting
api_count: 9
apis:
- description: API for creating, reading, and modifying Word documents.
  name: Word API
  slug: word-api
- description: API for working with Excel workbooks, worksheets, charts, and tables.
  name: Excel API
  slug: excel-api
- description: API for creating and modifying PowerPoint presentations.
  name: PowerPoint API
  slug: powerpoint-api
- description: API for accessing and managing email messages, calendars, and contacts.
  name: Outlook Mail API
  slug: outlook-mail-api
- description: API for accessing files and folders stored in OneDrive.
  name: OneDrive API
  slug: onedrive-api
- description: API for accessing SharePoint sites, lists, and content.
  name: SharePoint API
  slug: sharepoint-api
- description: The Drive API from Microsoft Office Pack — 4 operation(s) for drive.
  name: Microsoft Office Pack Drive API
  slug: microsoft-office-pack-drive-api
- description: The Mail API from Microsoft Office Pack — 4 operation(s) for mail.
  name: Microsoft Office Pack Mail API
  slug: microsoft-office-pack-mail-api
- description: The Teams API from Microsoft Office Pack — 4 operation(s) for teams.
  name: Microsoft Office Pack Teams API
  slug: microsoft-office-pack-teams-api
artifact_total: 21
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Microsoft Graph API - Office Pack Drive API
  slug: open-microsoft-office-pack-drive-api
- collection_type: open
  name: Microsoft Graph API - Office Pack Drive Mail API
  slug: open-microsoft-office-pack-mail-api
- collection_type: open
  name: Microsoft Graph API - Office Pack Drive Teams API
  slug: open-microsoft-office-pack-teams-api
- collection_type: open
  name: Microsoft Graph API - Office Pack
  slug: open-microsoft-office-pack
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-office-pack-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-office-pack-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-office-pack-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-office-pack-scopes.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.microsoft.com/servicesagreement
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/privacystatement
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.microsoft.com/microsoft-365
- group: operate
  title: ''
  type: StatusPage
  url: https://status.dev.microsoft.com/
- group: company
  title: ''
  type: Blog
  url: https://developer.microsoft.com/microsoft-365/blogs/
created: '2024'
description: A collection of APIs for Microsoft Office productivity applications including Word, Excel, PowerPoint, Outlook, and OneDrive.
finops:
- name: Microsoft Office Pack Finops
  service_category: API
  slug: microsoft-office-pack-finops
image: https://www.microsoft.com/en-us/microsoft-365/blog/wp-content/uploads/sites/2/2020/04/Microsoft-365-logo.png
layout: provider
modified: '2026-04-28'
name: Microsoft Office Pack
nav: Providers
network: true
overview: 'Microsoft Office Pack publishes 3 APIs on the [APIs.io](https://apis.io/) network: Drive API, Mail API, and Teams API.


  Microsoft Office Pack''s developer surface includes authentication, engineering blog, and 7 more developer resources.'
plans:
- name: Microsoft Office Pack Plans Pricing
  plan_count: 3
  slug: microsoft-office-pack-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 5
  name: Microsoft Office Pack Rate Limits
  slug: microsoft-office-pack-rate-limits
scopes:
- name: Microsoft Office Pack Scopes
  scope_count: 7
  slug: microsoft-office-pack-scopes
  summary_line: 7 scopes · authorizationCode
score:
  band: thin
  composite: 31.5
  delta: 0.0
  facets:
    commercial_clarity: 36.8
    contract_quality: 52.2
    developer_ergonomics: 21.7
    discoverability: 37.0
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 31.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-office-pack/refs/heads/main/screenshots/microsoft-office-pack-2026-06-20T185514.png
security:
- kind: authentication
  name: Microsoft Office Pack Authentication
  slug: microsoft-office-pack-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Microsoft Office Pack Domain Security
  slug: microsoft-office-pack-domain-security
  summary_line: TLSv1.3 · DMARC
slug: microsoft-office-pack
website: https://developer.microsoft.com/microsoft-365
---
