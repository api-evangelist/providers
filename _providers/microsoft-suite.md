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
- acting_count: 4
  human_in_the_loop: 0
  name: Microsoft Suite Agentic Access
  operation_count: 18
  slug: microsoft-suite-agentic-access
  summary_line: 18 operations · 4 acting
api_count: 13
apis:
- description: API for integrating with Microsoft Teams to create bots, tabs, messaging extensions, and connectors.
  name: Microsoft Teams API
  slug: microsoft-teams-api
- description: REST API for accessing files stored in OneDrive and SharePoint document libraries.
  name: OneDrive API
  slug: onedrive-api
- description: Access to Outlook mail, calendar, contacts, and tasks via Microsoft Graph.
  name: Outlook Mail API
  slug: outlook-mail-api
- description: Access SharePoint sites, lists, and content via REST and Microsoft Graph APIs.
  name: SharePoint API
  slug: sharepoint-api
- description: Identity and access management API for authentication and authorization.
  name: Azure Active Directory API
  slug: azure-active-directory-api
- description: Embed Power BI reports and dashboards, and manage Power BI resources programmatically.
  name: Power BI API
  slug: power-bi-api
- description: The Calendar API from Microsoft Suite — 2 operation(s) for calendar.
  name: Microsoft Suite Calendar API
  slug: microsoft-suite-calendar-api
- description: The Files API from Microsoft Suite — 2 operation(s) for files.
  name: Microsoft Suite Files API
  slug: microsoft-suite-files-api
- description: The Groups API from Microsoft Suite — 2 operation(s) for groups.
  name: Microsoft Suite Groups API
  slug: microsoft-suite-groups-api
- description: The Mail API from Microsoft Suite — 2 operation(s) for mail.
  name: Microsoft Suite Mail API
  slug: microsoft-suite-mail-api
- description: The Subscriptions API from Microsoft Suite — 1 operation(s) for subscriptions.
  name: Microsoft Suite Subscriptions API
  slug: microsoft-suite-subscriptions-api
- description: The Teams API from Microsoft Suite — 1 operation(s) for teams.
  name: Microsoft Suite Teams API
  slug: microsoft-suite-teams-api
- description: The Users API from Microsoft Suite — 6 operation(s) for users.
  name: Microsoft Suite Users API
  slug: microsoft-suite-users-api
artifact_total: 21
collections:
- collection_type: open
  name: Microsoft Graph API
  slug: open-microsoft-suite
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-suite-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-suite-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-suite-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-suite-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/microsoft
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docs.microsoft.com/legal/termsofuse
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/
- group: operate
  title: ''
  type: Support
  url: https://developer.microsoft.com/support
- group: operate
  title: ''
  type: StatusPage
  url: https://status.dev.microsoft.com/
- group: company
  title: ''
  type: Blog
  url: https://developer.microsoft.com/blog
created: '2024'
description: Collection of APIs for Microsoft's productivity and cloud services suite.
finops:
- name: Microsoft Suite Finops
  service_category: API
  slug: microsoft-suite-finops
image: https://www.microsoft.com/favicon.ico
layout: provider
modified: '2026-04-28'
name: Microsoft Suite
nav: Providers
network: true
overview: 'Microsoft Suite publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Calendar API, Files API, Groups API, and 4 more. Tagged areas include Cloud, Enterprise, Productivity, and SaaS.


  Microsoft Suite''s developer surface includes authentication, support, engineering blog, and 7 more developer resources.'
plans:
- name: Microsoft Suite Plans Pricing
  plan_count: 3
  slug: microsoft-suite-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 5
  name: Microsoft Suite Rate Limits
  slug: microsoft-suite-rate-limits
scopes:
- name: Microsoft Suite Scopes
  scope_count: 8
  slug: microsoft-suite-scopes
  summary_line: 8 scopes · authorizationCode/clientCredentials
score:
  band: thin
  composite: 40.2
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 53.4
    developer_ergonomics: 17.4
    discoverability: 44.4
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 40.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-suite/refs/heads/main/screenshots/microsoft-suite-2026-06-20T185537.png
security:
- kind: authentication
  name: Microsoft Suite Authentication
  slug: microsoft-suite-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Microsoft Suite Domain Security
  slug: microsoft-suite-domain-security
  summary_line: TLSv1.3 · DMARC
slug: microsoft-suite
tags:
- Cloud
- Enterprise
- Productivity
- SaaS
website: https://developer.microsoft.com
---
