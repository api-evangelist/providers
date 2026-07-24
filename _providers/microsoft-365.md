---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 41.3
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Microsoft 365 Agentic Access
  operation_count: 18
  slug: microsoft-365-agentic-access
  summary_line: 18 operations · 5 acting
api_count: 9
apis:
- description: Unified REST API providing a single endpoint to access data and intelligence across Microsoft 365, Microsoft Entra ID, Windows, and Enterprise Mobility + Security. Supports OAuth 2.0 authentication an
  name: Microsoft Graph API
  slug: graph-api
- description: Beta endpoint of the Microsoft Graph API offering preview features and resources before they are promoted to v1.0, including additional insights, reporting, and management capabilities.
  name: Microsoft Graph Beta API
  slug: graph-beta-api
- description: The Calendar API from Microsoft 365 — 1 operation(s) for calendar.
  name: Microsoft 365 Calendar API
  slug: microsoft-365-calendar-api
- description: The Files API from Microsoft 365 — 1 operation(s) for files.
  name: Microsoft 365 Files API
  slug: microsoft-365-files-api
- description: The Groups API from Microsoft 365 — 3 operation(s) for groups.
  name: Microsoft 365 Groups API
  slug: microsoft-365-groups-api
- description: The Mail API from Microsoft 365 — 1 operation(s) for mail.
  name: Microsoft 365 Mail API
  slug: microsoft-365-mail-api
- description: The Me API from Microsoft 365 — 3 operation(s) for me.
  name: Microsoft 365 Me API
  slug: microsoft-365-me-api
- description: The Teams API from Microsoft 365 — 2 operation(s) for teams.
  name: Microsoft 365 Teams API
  slug: microsoft-365-teams-api
- description: The Users API from Microsoft 365 — 2 operation(s) for users.
  name: Microsoft 365 Users API
  slug: microsoft-365-users-api
artifact_total: 17
collections:
- collection_type: open
  name: Microsoft 365 (Microsoft Graph API)
  slug: open-microsoft-365
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-365-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/microsoft-365-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/microsoft-365-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-365-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-365-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-365-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/microsoft-365
- group: company
  title: ''
  type: Website
  url: https://www.microsoft.com/microsoft-365
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.microsoft.com/microsoft-365
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/graph
- group: start
  title: ''
  type: Signup
  url: https://www.microsoft.com/microsoft-365/business/compare-all-plans
- group: commercial
  title: ''
  type: Pricing
  url: https://www.microsoft.com/microsoft-365/business/compare-all-plans
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/microsoftgraph
- group: auth
  title: ''
  type: Authentication
  url: https://learn.microsoft.com/en-us/graph/auth/auth-concepts
- group: operate
  title: ''
  type: StatusPage
  url: https://admin.microsoft.com/servicestatus
created: '2026-05-11'
description: Microsoft 365 is Microsoft's productivity and collaboration suite, including Word, Excel, PowerPoint, Outlook, Teams, OneDrive, SharePoint, and OneNote, along with identity, security, and device management services. Developers access Microsoft 365 data and intelligence programmatically through Microsoft Graph, a unified REST API that exposes users, mail, calendar, files, Teams messages, sites, devices, and more across the Microsoft cloud.
graphqls:
- description: 'This conceptual GraphQL schema represents the Microsoft 365 productivity suite APIs as exposed through Microsoft Graph, the unified REST API endpoint at `https://graph.microsoft.com/v1.0`. The schema '
  name: Microsoft 365 GraphQL Schema
  slug: microsoft-365-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-365.png
layout: provider
modified: '2026-05-11'
name: Microsoft 365
nav: Providers
network: true
overview: 'Microsoft 365 publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Calendar API, Files API, Groups API, and 4 more. Tagged areas include Productivity, Collaboration, Email, Calendar, and Files.


  Microsoft 365''s developer surface includes authentication, documentation, signup flow, pricing, and 11 more developer resources.'
random_paper: 12
scopes:
- name: Microsoft 365 Scopes
  scope_count: 8
  slug: microsoft-365-scopes
  summary_line: 8 scopes · authorizationCode/clientCredentials
score:
  band: thin
  composite: 30.8
  delta: 0.0
  facets:
    commercial_clarity: 18.4
    contract_quality: 47.8
    developer_ergonomics: 28.3
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 30.8
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-365/refs/heads/main/screenshots/microsoft-365-2026-06-20T185401.png
security:
- kind: authentication
  name: Microsoft 365 Authentication
  slug: microsoft-365-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Microsoft 365 Domain Security
  slug: microsoft-365-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Microsoft 365 Vulnerability Disclosure
  slug: microsoft-365-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Microsoft 365 Trust Center
  slug: microsoft-365-trust-center
  summary_line: GDPR
slug: microsoft-365
tags:
- Productivity
- Collaboration
- Email
- Calendar
- Files
- Identity
- Microsoft
- Microsoft Graph
website: https://www.microsoft.com/microsoft-365
---
