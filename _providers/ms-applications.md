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
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Ms Applications Agentic Access
  operation_count: 11
  slug: ms-applications-agentic-access
  summary_line: 11 operations
api_count: 10
apis:
- description: API for building apps and bots that integrate with Microsoft Teams.
  name: Microsoft Teams API
  slug: microsoft-teams-api
- description: API for accessing and managing email messages through Microsoft Outlook.
  name: Outlook Mail API
  slug: outlook-mail-api
- description: API for accessing and managing files stored in OneDrive and SharePoint.
  name: OneDrive API
  slug: onedrive-api
- description: API for accessing SharePoint sites, lists, and content.
  name: SharePoint API
  slug: sharepoint-api
- description: API for identity and access management in Azure AD.
  name: Azure Active Directory API
  slug: azure-active-directory-api
- description: API for managing tasks and to-do lists.
  name: Microsoft To Do API
  slug: microsoft-to-do-api
- description: API for creating and managing plans, tasks, and team collaboration.
  name: Microsoft Planner API
  slug: microsoft-planner-api
- description: The Groups API from Microsoft Applications APIs — 1 operation(s) for groups.
  name: Microsoft Applications APIs Groups API
  slug: ms-applications-groups-api
- description: The Me API from Microsoft Applications APIs — 8 operation(s) for me.
  name: Microsoft Applications APIs Me API
  slug: ms-applications-me-api
- description: The Users API from Microsoft Applications APIs — 2 operation(s) for users.
  name: Microsoft Applications APIs Users API
  slug: ms-applications-users-api
artifact_total: 19
collections:
- collection_type: open
  name: Microsoft Graph API (Applications)
  slug: open-ms-applications
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ms-applications-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ms-applications-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ms-applications-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ms-applications-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/ms-applications-scopes.yml
- group: company
  title: ''
  type: Blog
  url: https://devblogs.microsoft.com/microsoft365dev/feed/
created: '2024-01-15'
description: Collection of Microsoft application APIs for productivity, collaboration, and enterprise services.
finops:
- name: Ms Applications Finops
  service_category: API
  slug: ms-applications-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ms-applications.png
layout: provider
modified: '2026-04-28'
name: Microsoft Applications APIs
nav: Providers
network: true
overview: 'Microsoft Applications APIs publishes 3 APIs on the [APIs.io](https://apis.io/) network: Groups API, Me API, and Users API. Tagged areas include Cloud, Enterprise, Microsoft, Microsoft-365, and Office.


  Microsoft Applications APIs'' developer surface includes authentication, engineering blog, and 4 more developer resources.'
plans:
- name: Ms Applications Plans Pricing
  plan_count: 3
  slug: ms-applications-plans-pricing
random_paper: 26
rate_limits:
- limit_count: 5
  name: Ms Applications Rate Limits
  slug: ms-applications-rate-limits
scopes:
- name: Ms Applications Scopes
  scope_count: 5
  slug: ms-applications-scopes
  summary_line: 5 scopes · authorizationCode/clientCredentials
score:
  band: thin
  composite: 32.9
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 51.3
    developer_ergonomics: 13.0
    discoverability: 55.0
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 32.9
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ms-applications/refs/heads/main/screenshots/ms-applications-2026-06-20T185844.png
security:
- kind: authentication
  name: Ms Applications Authentication
  slug: ms-applications-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Ms Applications Domain Security
  slug: ms-applications-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Ms Applications Vulnerability Disclosure
  slug: ms-applications-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: ms-applications
tags:
- Cloud
- Enterprise
- Microsoft
- Microsoft-365
- Office
- Productivity
- Saas
website: https://developer.microsoft.com
---
