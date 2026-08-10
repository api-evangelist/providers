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
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Ms Office Agentic Access
  operation_count: 7
  slug: ms-office-agentic-access
  summary_line: 7 operations
api_count: 4
apis:
- description: JavaScript API for building add-ins for Word, Excel, PowerPoint, and Outlook.
  name: Office Add-ins API
  slug: office-add-ins-api
- description: The Groups API from Microsoft Office APIs — 1 operation(s) for groups.
  name: Microsoft Office APIs Groups API
  slug: ms-office-groups-api
- description: The Me API from Microsoft Office APIs — 5 operation(s) for me.
  name: Microsoft Office APIs Me API
  slug: ms-office-me-api
- description: The Users API from Microsoft Office APIs — 1 operation(s) for users.
  name: Microsoft Office APIs Users API
  slug: ms-office-users-api
artifact_total: 13
collections:
- collection_type: open
  name: Microsoft Graph API (Office)
  slug: open-ms-office
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ms-office-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ms-office-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ms-office-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ms-office-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/ms-office-scopes.yml
- group: company
  title: ''
  type: Blog
  url: https://devblogs.microsoft.com/microsoft365dev/feed/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/microsoft
- group: start
  title: ''
  type: Portal
  url: https://developer.microsoft.com/
- group: auth
  title: ''
  type: Authentication
  url: https://docs.microsoft.com/en-us/azure/active-directory/develop/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.office.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.microsoft.com/en-us/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/
created: '2024-01-15'
description: Collection of APIs for Microsoft Office products and services.
finops:
- name: Ms Office Finops
  service_category: API
  slug: ms-office-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ms-office.png
layout: provider
modified: '2026-04-28'
name: Microsoft Office APIs
nav: Providers
network: true
overview: 'Microsoft Office APIs publishes 3 APIs on the [APIs.io](https://apis.io/) network: Groups API, Me API, and Users API. Tagged areas include Collaboration, Documents, Microsoft, Office, and Productivity.


  Microsoft Office APIs'' developer surface includes authentication, engineering blog, developer portal, and 9 more developer resources.'
plans:
- name: Ms Office Plans Pricing
  plan_count: 3
  slug: ms-office-plans-pricing
random_paper: 77
rate_limits:
- limit_count: 5
  name: Ms Office Rate Limits
  slug: ms-office-rate-limits
scopes:
- name: Ms Office Scopes
  scope_count: 5
  slug: ms-office-scopes
  summary_line: 5 scopes · authorizationCode
score:
  band: developing
  composite: 44.8
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 57.4
    developer_ergonomics: 21.7
    discoverability: 72.2
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 44.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ms-office/refs/heads/main/screenshots/ms-office-2026-06-20T185846.png
security:
- kind: authentication
  name: Ms Office Authentication
  slug: ms-office-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Ms Office Domain Security
  slug: ms-office-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Ms Office Vulnerability Disclosure
  slug: ms-office-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: ms-office
tags:
- Collaboration
- Documents
- Microsoft
- Office
- Productivity
website: https://developer.microsoft.com/
---
