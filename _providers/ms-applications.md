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
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.7
  scored_at: '2026-08-26'
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
artifact_total: 23
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Microsoft Graph API (Applications) Groups API
  slug: open-ms-applications-groups-api
- collection_type: open
  name: Microsoft Graph API (Applications) Groups Me API
  slug: open-ms-applications-me-api
- collection_type: open
  name: Microsoft Graph API (Applications) Groups Users API
  slug: open-ms-applications-users-api
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
random_paper: 2
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
  composite: 36.1
  delta: 9.3
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 50.3
    developer_ergonomics: 50.0
    discoverability: 72.2
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 26.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: rising
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
- Software-as-a-Service
website: https://developer.microsoft.com
---
