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
  name: Microsoft Products Agentic Access
  operation_count: 15
  slug: microsoft-products-agentic-access
  summary_line: 15 operations · 4 acting
api_count: 9
apis:
- description: APIs for Microsoft 365 services including Exchange, SharePoint, and Teams.
  name: Microsoft 365 API
  slug: microsoft-365-api
- description: API for building apps and bots for Microsoft Teams.
  name: Microsoft Teams API
  slug: microsoft-teams-api
- description: AI and machine learning APIs for vision, speech, language, and decision making.
  name: Azure Cognitive Services API
  slug: azure-cognitive-services-api
- description: APIs for Power Apps, Power Automate, and Power BI.
  name: Power Platform API
  slug: power-platform-api
- description: APIs for Dynamics 365 business applications.
  name: Dynamics 365 API
  slug: dynamics-365-api
- description: APIs for Xbox Live gaming services.
  name: Xbox Live API
  slug: xbox-live-api
- description: The Drive API from Microsoft Products — 4 operation(s) for drive.
  name: Microsoft Products Drive API
  slug: microsoft-products-drive-api
- description: The Mail API from Microsoft Products — 4 operation(s) for mail.
  name: Microsoft Products Mail API
  slug: microsoft-products-mail-api
- description: The Teams API from Microsoft Products — 4 operation(s) for teams.
  name: Microsoft Products Teams API
  slug: microsoft-products-teams-api
artifact_total: 18
collections:
- collection_type: open
  name: Microsoft Graph API - Microsoft Products
  slug: open-microsoft-products
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-products-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/microsoft-products-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-products-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-products-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-products-scopes.yml
- group: start
  title: ''
  type: Portal
  url: https://developer.microsoft.com/
- group: auth
  title: ''
  type: Authentication
  url: https://docs.microsoft.com/en-us/azure/active-directory/develop/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.microsoft.com/en-us/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/
- group: operate
  title: ''
  type: Support
  url: https://support.microsoft.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.azure.com/
created: '2024-01-01'
description: A collection of APIs for various Microsoft products and services.
finops:
- name: Microsoft Products Finops
  service_category: API
  slug: microsoft-products-finops
image: https://www.microsoft.com/favicon.ico
layout: provider
modified: '2026-04-28'
name: Microsoft Products
nav: Providers
network: true
overview: 'Microsoft Products publishes 3 APIs on the [APIs.io](https://apis.io/) network: Drive API, Mail API, and Teams API. Tagged areas include Cloud, Enterprise, Microsoft, and Productivity.


  Microsoft Products'' developer surface includes authentication, developer portal, support, and 8 more developer resources.'
plans:
- name: Microsoft Products Plans Pricing
  plan_count: 3
  slug: microsoft-products-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 5
  name: Microsoft Products Rate Limits
  slug: microsoft-products-rate-limits
scopes:
- name: Microsoft Products Scopes
  scope_count: 7
  slug: microsoft-products-scopes
  summary_line: 7 scopes · authorizationCode
score:
  band: thin
  composite: 39.2
  delta: -0.8
  facets:
    commercial_clarity: 60.5
    contract_quality: 50.0
    developer_ergonomics: 23.9
    discoverability: 37.0
    governance: 0.0
    operational_transparency: 47.4
  previous_composite: 40.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-products/refs/heads/main/screenshots/microsoft-products-2026-06-20T185528.png
security:
- kind: authentication
  name: Microsoft Products Authentication
  slug: microsoft-products-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Microsoft Products Domain Security
  slug: microsoft-products-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Microsoft Products Vulnerability Disclosure
  slug: microsoft-products-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: microsoft-products
tags:
- Cloud
- Enterprise
- Microsoft
- Productivity
website: https://developer.microsoft.com/
---
