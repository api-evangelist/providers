---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
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
  score: 19.8
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Microsoft Onedrive Agentic Access
  operation_count: 18
  slug: microsoft-onedrive-agentic-access
  summary_line: 18 operations · 7 acting
api_count: 4
apis:
- description: 'The OneDrive File Picker is a JavaScript SDK that provides a pre-built UI component for selecting files from OneDrive within web applications. It handles authentication, file browsing, and selection, '
  name: OneDrive File Picker
  slug: file-picker
- baseURL: https://graph.microsoft.com/v1.0/
  baseurl_source: declared
  description: The DriveItems API from Microsoft OneDrive — 6 operation(s) for driveitems.
  name: Microsoft OneDrive DriveItems API
  slug: microsoft-onedrive-driveitems-api
- baseURL: https://graph.microsoft.com/v1.0/
  baseurl_source: declared
  description: The Drives API from Microsoft OneDrive — 4 operation(s) for drives.
  name: Microsoft OneDrive Drives API
  slug: microsoft-onedrive-drives-api
- baseURL: https://graph.microsoft.com/v1.0/
  baseurl_source: declared
  description: The Sharing API from Microsoft OneDrive — 4 operation(s) for sharing.
  name: Microsoft OneDrive Sharing API
  slug: microsoft-onedrive-sharing-api
artifact_total: 15
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Microsoft OneDrive API (Microsoft Graph) DriveItems API
  slug: open-microsoft-onedrive-driveitems-api
- collection_type: open
  name: Microsoft OneDrive API (Microsoft Graph) DriveItems Drives API
  slug: open-microsoft-onedrive-drives-api
- collection_type: open
  name: Microsoft OneDrive API (Microsoft Graph) DriveItems Sharing API
  slug: open-microsoft-onedrive-sharing-api
- collection_type: open
  name: Microsoft OneDrive API (Microsoft Graph)
  slug: open-microsoft-onedrive
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-onedrive-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-onedrive-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-onedrive-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/OneDrive
- group: start
  title: ''
  type: Portal
  url: https://portal.azure.com/
- group: company
  title: ''
  type: Website
  url: https://www.microsoft.com/en-us/microsoft-365/onedrive/online-cloud-storage
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/onedrive/developer/
- group: auth
  title: ''
  type: Authentication
  url: https://learn.microsoft.com/en-us/graph/auth/
- group: build
  title: ''
  type: SDKs
  url: https://learn.microsoft.com/en-us/graph/sdks/sdks-overview
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.microsoft.com/en-us/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: operate
  title: ''
  type: Support
  url: https://support.microsoft.com/
created: '2024-01-01'
description: Microsoft OneDrive is a cloud-based file storage and synchronization service. It provides APIs through Microsoft Graph for accessing, managing, and sharing files and folders stored in OneDrive personal and OneDrive for Business.
finops:
- name: Microsoft Onedrive Finops
  service_category: API
  slug: microsoft-onedrive-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-onedrive.png
layout: provider
modified: '2026-05-19'
name: Microsoft OneDrive
nav: Providers
network: true
overview: 'Microsoft OneDrive publishes 3 APIs on the [APIs.io](https://apis.io/) network: DriveItems API, Drives API, and Sharing API. Tagged areas include Cloud Storage, File Storage, File, Microsoft, and Microsoft-365.


  Microsoft OneDrive''s developer surface includes authentication, developer portal, documentation, support, and 8 more developer resources.'
plans:
- name: Microsoft Onedrive Plans Pricing
  plan_count: 3
  slug: microsoft-onedrive-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 5
  name: Microsoft Onedrive Rate Limits
  slug: microsoft-onedrive-rate-limits
score:
  band: thin
  composite: 37.1
  coverage:
    artifact_dirs: 9
    catalog_earned: 44.0
    catalog_earned_first_party: 0.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 47.6
    developer_ergonomics: 50.0
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 37.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-onedrive/refs/heads/main/screenshots/microsoft-onedrive-2026-06-20T185515.png
security:
- kind: authentication
  name: Microsoft Onedrive Authentication
  slug: microsoft-onedrive-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Microsoft Onedrive Domain Security
  slug: microsoft-onedrive-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: microsoft-onedrive
tags:
- Cloud Storage
- File Storage
- File
- Microsoft
- Microsoft-365
website: https://www.microsoft.com/en-us/microsoft-365/onedrive/online-cloud-storage
---
