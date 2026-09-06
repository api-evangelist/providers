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
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Ms Products Agentic Access
  operation_count: 9
  slug: ms-products-agentic-access
  summary_line: 9 operations
api_count: 14
apis:
- description: REST APIs for Azure cloud services and resource management.
  name: Azure REST API
  slug: azure-rest-api
- description: APIs for Office 365 applications including Outlook, Calendar, Contacts, and Files.
  name: Office 365 APIs
  slug: office-365-apis
- description: Build apps and bots for the Microsoft Teams collaboration platform.
  name: Microsoft Teams API
  slug: microsoft-teams-api
- description: Access files stored in OneDrive and SharePoint.
  name: OneDrive API
  slug: onedrive-api
- description: APIs for Power Apps, Power Automate, and Power BI.
  name: Power Platform APIs
  slug: power-platform-apis
- description: AI and machine learning APIs for vision, speech, language, and decision making.
  name: Azure Cognitive Services API
  slug: azure-cognitive-services-api
- description: APIs for Dynamics 365 CRM and ERP applications.
  name: Dynamics 365 API
  slug: dynamics-365-api
- description: Security APIs for threat protection and incident response.
  name: Microsoft 365 Defender API
  slug: microsoft-365-defender-api
- description: APIs for Xbox gaming services and social features.
  name: Xbox Live API
  slug: xbox-live-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: Outlook calendar events for the signed-in user.
  name: Microsoft Products APIs Calendar API
  slug: ms-products-calendar-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: Microsoft 365 groups and security groups.
  name: Microsoft Products APIs Groups API
  slug: ms-products-groups-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: Outlook mail messages for the signed-in user.
  name: Microsoft Products APIs Mail API
  slug: ms-products-mail-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: Operations on the signed-in user.
  name: Microsoft Products APIs Me API
  slug: ms-products-me-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: User accounts and profiles in Microsoft Entra ID.
  name: Microsoft Products APIs Users API
  slug: ms-products-users-api
artifact_total: 29
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Microsoft Graph API (v1.0) Calendar API
  slug: open-ms-products-calendar-api
- collection_type: open
  name: Microsoft Graph API (v1.0) Calendar Groups API
  slug: open-ms-products-groups-api
- collection_type: open
  name: Microsoft Graph API (v1.0) Calendar Mail API
  slug: open-ms-products-mail-api
- collection_type: open
  name: Microsoft Graph API (v1.0) Calendar Me API
  slug: open-ms-products-me-api
- collection_type: open
  name: Microsoft Graph API (v1.0) Calendar Users API
  slug: open-ms-products-users-api
- collection_type: open
  name: Microsoft Graph API (v1.0)
  slug: open-ms-products
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ms-products-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ms-products-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ms-products-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ms-products-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/ms-products-scopes.yml
- group: company
  title: ''
  type: Blog
  url: https://azure.microsoft.com/en-us/blog/feed/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/microsoft
- group: start
  title: ''
  type: Portal
  url: https://developer.microsoft.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.microsoft.com/en-us/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/
created: '2024-01-01'
description: Collection of Microsoft product and service APIs spanning Microsoft 365, Azure, Dynamics 365, Power Platform, security, gaming, and more.
finops:
- name: Ms Products Finops
  service_category: API
  slug: ms-products-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ms-products.png
layout: provider
modified: '2026-05-19'
name: Microsoft Products APIs
nav: Providers
network: true
overview: 'Microsoft Products APIs publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Calendar API, Groups API, Mail API, and 2 more. Tagged areas include Azure, Cloud, Enterprise, Microsoft, and Office 365.


  Microsoft Products APIs'' developer surface includes authentication, engineering blog, developer portal, and 7 more developer resources.'
plans:
- name: Ms Products Plans Pricing
  plan_count: 3
  slug: ms-products-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 5
  name: Ms Products Rate Limits
  slug: ms-products-rate-limits
scopes:
- name: Ms Products Scopes
  scope_count: 1
  slug: ms-products-scopes
  summary_line: 1 scope · authorizationCode/clientCredentials
score:
  band: thin
  composite: 37.8
  coverage:
    artifact_dirs: 11
    catalog_earned: 39.0
    catalog_earned_first_party: 0.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 53.1
    developer_ergonomics: 47.6
    discoverability: 63.0
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 37.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ms-products/refs/heads/main/screenshots/ms-products-2026-06-20T185847.png
security:
- kind: authentication
  name: Ms Products Authentication
  slug: ms-products-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Ms Products Domain Security
  slug: ms-products-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Ms Products Vulnerability Disclosure
  slug: ms-products-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: ms-products
tags:
- Azure
- Cloud
- Enterprise
- Microsoft
- Office 365
- Productivity
website: https://developer.microsoft.com/
---
