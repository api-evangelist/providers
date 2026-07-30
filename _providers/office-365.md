---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
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
  score: 28.4
  scored_at: '2026-07-28'
api_count: 5
apis:
- description: The primary API for Office 365, providing access to data and intelligence in Microsoft 365, Windows 10, and Enterprise Mobility + Security.
  name: Microsoft Graph API
  slug: microsoft-graph-api
- description: Access email, manage folders, send mail, and manage mail settings via Microsoft Graph.
  name: Outlook Mail API
  slug: outlook-mail-api
- description: Access and manage calendar events, meeting requests, and calendar groups.
  name: Outlook Calendar API
  slug: outlook-calendar-api
- description: Access and manage files stored in OneDrive and SharePoint.
  name: OneDrive API
  slug: onedrive-api
- description: Integrate with Microsoft Teams for chat, channels, meetings, and collaboration.
  name: Microsoft Teams API
  slug: microsoft-teams-api
artifact_total: 11
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/office-365-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/office-365-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/office-365-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/OfficeDev
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/microsoft-365
- group: company
  title: ''
  type: Website
  url: https://www.microsoft.com/en-us/microsoft-365
- group: docs
  title: ''
  type: Documentation
  url: https://developer.microsoft.com/en-us/microsoft-365
- group: auth
  title: ''
  type: Authentication
  url: https://learn.microsoft.com/en-us/azure/active-directory/develop/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.office365.com/
- group: operate
  title: ''
  type: Support
  url: https://learn.microsoft.com/en-us/answers/products/
- group: company
  title: ''
  type: Blog
  url: https://devblogs.microsoft.com/microsoft365dev/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.microsoft.com/en-us/servicesagreement
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/
created: '2024-01-15'
description: Microsoft Office 365 is a cloud-based suite of productivity and collaboration applications that integrates all Microsoft's existing online applications into a single platform including email, calendar, files, Teams, and SharePoint.
finops:
- name: Office 365 Finops
  service_category: API
  slug: office-365-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/office-365.png
layout: provider
modified: '2026-04-28'
name: Office 365
nav: Providers
network: true
overview: 'Office 365 publishes 1 API on the [APIs.io](https://apis.io/) network: Microsoft Graph API. Tagged areas include Cloud, Collaboration, Documents, Email, and Enterprise.


  Office 365''s developer surface includes documentation, authentication, support, engineering blog, and 9 more developer resources.'
plans:
- name: Office 365 Plans Pricing
  plan_count: 3
  slug: office-365-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 5
  name: Office 365 Rate Limits
  slug: office-365-rate-limits
score:
  band: thin
  composite: 41.2
  delta: -4.0
  facets:
    commercial_clarity: 68.4
    contract_quality: 32.3
    developer_ergonomics: 26.1
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 45.2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/office-365/refs/heads/main/screenshots/office-365-2026-06-20T190635.png
security:
- kind: domain-security
  name: Office 365 Domain Security
  slug: office-365-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Office 365 Vulnerability Disclosure
  slug: office-365-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Office 365 Trust Center
  slug: office-365-trust-center
  summary_line: GDPR
slug: office-365
tags:
- Cloud
- Collaboration
- Documents
- Email
- Enterprise
- Productivity
website: https://www.microsoft.com/en-us/microsoft-365
---
