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
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Microsoft Office Products Agentic Access
  operation_count: 15
  slug: microsoft-office-products-agentic-access
  summary_line: 15 operations · 4 acting
api_count: 9
apis:
- description: API for building add-ins and automating Microsoft Word.
  name: Word JavaScript API
  slug: word-javascript-api
- description: API for creating Excel add-ins and automating spreadsheet operations.
  name: Excel JavaScript API
  slug: excel-javascript-api
- description: API for developing PowerPoint add-ins and presentation automation.
  name: PowerPoint JavaScript API
  slug: powerpoint-javascript-api
- description: API for building Outlook add-ins for email, calendar, and contacts.
  name: Outlook JavaScript API
  slug: outlook-javascript-api
- description: API for building apps, bots, and integrations for Microsoft Teams.
  name: Microsoft Teams API
  slug: microsoft-teams-api
- description: API for accessing and managing files in OneDrive and SharePoint.
  name: OneDrive API
  slug: onedrive-api
- description: The Drive API from Microsoft Office Products — 4 operation(s) for drive.
  name: Microsoft Office Products Drive API
  slug: microsoft-office-products-drive-api
- description: The Mail API from Microsoft Office Products — 4 operation(s) for mail.
  name: Microsoft Office Products Mail API
  slug: microsoft-office-products-mail-api
- description: The Teams API from Microsoft Office Products — 4 operation(s) for teams.
  name: Microsoft Office Products Teams API
  slug: microsoft-office-products-teams-api
artifact_total: 22
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Microsoft Graph API - Office Products Drive API
  slug: open-microsoft-office-products-drive-api
- collection_type: open
  name: Microsoft Graph API - Office Products Drive Mail API
  slug: open-microsoft-office-products-mail-api
- collection_type: open
  name: Microsoft Graph API - Office Products Drive Teams API
  slug: open-microsoft-office-products-teams-api
- collection_type: open
  name: Microsoft Graph API - Office Products
  slug: open-microsoft-office-products
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-office-products-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/microsoft-office-products-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-office-products-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-office-products-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-office-products-scopes.yml
- group: start
  title: ''
  type: Portal
  url: https://developer.microsoft.com/en-us/microsoft-365
- group: auth
  title: ''
  type: Authentication
  url: https://learn.microsoft.com/en-us/azure/active-directory/develop/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://learn.microsoft.com/en-us/legal/microsoft-apis/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/
- group: company
  title: ''
  type: Blog
  url: https://devblogs.microsoft.com/microsoft365dev/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.dev.microsoft.com/
created: '2024-01-15'
description: API catalog for Microsoft Office product suite including Word, Excel, PowerPoint, Outlook, and Teams.
finops:
- name: Microsoft Office Products Finops
  service_category: API
  slug: microsoft-office-products-finops
image: https://www.microsoft.com/en-us/microsoft-365/blog/wp-content/uploads/sites/2/2020/04/Microsoft-365.png
layout: provider
modified: '2026-04-28'
name: Microsoft Office Products
nav: Providers
network: true
overview: 'Microsoft Office Products publishes 3 APIs on the [APIs.io](https://apis.io/) network: Drive API, Mail API, and Teams API. Tagged areas include Cloud, Enterprise, Microsoft, Office, and Productivity.


  Microsoft Office Products'' developer surface includes authentication, developer portal, engineering blog, and 8 more developer resources.'
plans:
- name: Microsoft Office Products Plans Pricing
  plan_count: 3
  slug: microsoft-office-products-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 5
  name: Microsoft Office Products Rate Limits
  slug: microsoft-office-products-rate-limits
scopes:
- name: Microsoft Office Products Scopes
  scope_count: 7
  slug: microsoft-office-products-scopes
  summary_line: 7 scopes · authorizationCode
score:
  band: thin
  composite: 31.7
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 51.7
    developer_ergonomics: 23.8
    discoverability: 46.3
    governance: 0.0
    operational_transparency: 15.8
  previous_composite: 31.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-office-products/refs/heads/main/screenshots/microsoft-office-products-2026-06-20T185514.png
security:
- kind: authentication
  name: Microsoft Office Products Authentication
  slug: microsoft-office-products-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Microsoft Office Products Domain Security
  slug: microsoft-office-products-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Microsoft Office Products Vulnerability Disclosure
  slug: microsoft-office-products-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: microsoft-office-products
tags:
- Cloud
- Enterprise
- Microsoft
- Office
- Productivity
- Software-as-a-Service
website: https://developer.microsoft.com/en-us/microsoft-365
---
