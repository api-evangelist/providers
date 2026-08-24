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
- acting_count: 10
  human_in_the_loop: 0
  name: Microsoft Active Directory Agentic Access
  operation_count: 22
  slug: microsoft-active-directory-agentic-access
  summary_line: 22 operations · 10 acting
api_count: 8
apis:
- description: Lightweight Directory Access Protocol interface for querying and modifying Active Directory.
  name: LDAP Protocol Interface
  slug: ldap-protocol-interface
- description: PowerShell cmdlets for managing Active Directory Domain Services.
  name: PowerShell Active Directory Module
  slug: powershell-active-directory-module
- description: Legacy REST API for Azure Active Directory (being replaced by Microsoft Graph).
  name: Azure AD Graph API (Deprecated)
  slug: azure-ad-graph-api-deprecated
- description: The Applications API from Microsoft Active Directory — 2 operation(s) for applications.
  name: Microsoft Active Directory Applications API
  slug: microsoft-active-directory-applications-api
- description: The Directory Roles API from Microsoft Active Directory — 2 operation(s) for directory roles.
  name: Microsoft Active Directory Directory Roles API
  slug: microsoft-active-directory-directory-roles-api
- description: The Groups API from Microsoft Active Directory — 4 operation(s) for groups.
  name: Microsoft Active Directory Groups API
  slug: microsoft-active-directory-groups-api
- description: The Service Principals API from Microsoft Active Directory — 2 operation(s) for service principals.
  name: Microsoft Active Directory Service Principals API
  slug: microsoft-active-directory-service-principals-api
- description: The Users API from Microsoft Active Directory — 3 operation(s) for users.
  name: Microsoft Active Directory Users API
  slug: microsoft-active-directory-users-api
artifact_total: 23
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Microsoft Active Directory (via Microsoft Graph) Applications API
  slug: open-microsoft-active-directory-applications-api
- collection_type: open
  name: Microsoft Active Directory (via Microsoft Graph) Applications Directory Roles API
  slug: open-microsoft-active-directory-directory-roles-api
- collection_type: open
  name: Microsoft Active Directory (via Microsoft Graph) Applications Groups API
  slug: open-microsoft-active-directory-groups-api
- collection_type: open
  name: Microsoft Active Directory (via Microsoft Graph) Applications Service Principals API
  slug: open-microsoft-active-directory-service-principals-api
- collection_type: open
  name: Microsoft Active Directory (via Microsoft Graph) Applications Users API
  slug: open-microsoft-active-directory-users-api
- collection_type: open
  name: Microsoft Active Directory (via Microsoft Graph)
  slug: open-microsoft-active-directory
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-active-directory-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/microsoft-active-directory-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-active-directory-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-active-directory-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-active-directory-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/microsoft
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.microsoft.com/en-us/servicesagreement
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: operate
  title: ''
  type: Service Status
  url: https://status.azure.com/
- group: company
  title: ''
  type: Blog
  url: https://techcommunity.microsoft.com/t5/microsoft-entra-azure-ad-blog/bg-p/Identity
- group: operate
  title: ''
  type: Support
  url: https://support.microsoft.com/en-us/windows-server
created: '2024'
description: Microsoft Active Directory (AD) is a directory service developed by Microsoft for Windows domain networks. It provides authentication and authorization services, centralized domain management, and directory services.
finops:
- name: Microsoft Active Directory Finops
  service_category: API
  slug: microsoft-active-directory-finops
image: https://docs.microsoft.com/en-us/windows-server/identity/ad-ds/media/active-directory-domain-services.png
layout: provider
modified: '2026-04-28'
name: Microsoft Active Directory
nav: Providers
network: true
overview: 'Microsoft Active Directory publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Applications API, Directory Roles API, Groups API, and 2 more. Tagged areas include Authentication, Authorization, Directory Services, Enterprise, and Identity.


  Microsoft Active Directory''s developer surface includes authentication, engineering blog, support, and 8 more developer resources.'
plans:
- name: Microsoft Active Directory Plans Pricing
  plan_count: 3
  slug: microsoft-active-directory-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 5
  name: Microsoft Active Directory Rate Limits
  slug: microsoft-active-directory-rate-limits
scopes:
- name: Microsoft Active Directory Scopes
  scope_count: 9
  slug: microsoft-active-directory-scopes
  summary_line: 9 scopes · authorizationCode/clientCredentials
score:
  band: thin
  composite: 33.5
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 55.2
    developer_ergonomics: 19.0
    discoverability: 72.2
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 33.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-active-directory/refs/heads/main/screenshots/microsoft-active-directory-2026-06-20T185347.png
security:
- kind: authentication
  name: Microsoft Active Directory Authentication
  slug: microsoft-active-directory-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Microsoft Active Directory Domain Security
  slug: microsoft-active-directory-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Microsoft Active Directory Vulnerability Disclosure
  slug: microsoft-active-directory-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: microsoft-active-directory
tags:
- Authentication
- Authorization
- Directory Services
- Enterprise
- Identity
- LDAP
- Windows
website: https://docs.microsoft.com/en-us/windows-server/identity/ad-ds/
---
