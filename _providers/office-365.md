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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 18.0
  scored_at: '2026-09-04'
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
random_paper: 4
rate_limits:
- limit_count: 5
  name: Office 365 Rate Limits
  slug: office-365-rate-limits
score:
  band: thin
  composite: 33.6
  coverage:
    artifact_dirs: 6
    catalog_earned: 49.0
    catalog_earned_first_party: 0.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 26.7
    developer_ergonomics: 35.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 33.6
  schema_version: 0.18.3
  scored_at: '2026-09-04'
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
