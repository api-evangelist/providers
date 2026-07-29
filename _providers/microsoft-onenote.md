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
- acting_count: 6
  human_in_the_loop: 0
  name: Microsoft Onenote Agentic Access
  operation_count: 17
  slug: microsoft-onenote-agentic-access
  summary_line: 17 operations · 6 acting
api_count: 4
apis:
- description: The Notebooks API from Microsoft OneNote — 2 operation(s) for notebooks.
  name: Microsoft OneNote Notebooks API
  slug: microsoft-onenote-notebooks-api
- description: The Pages API from Microsoft OneNote — 4 operation(s) for pages.
  name: Microsoft OneNote Pages API
  slug: microsoft-onenote-pages-api
- description: The SectionGroups API from Microsoft OneNote — 2 operation(s) for sectiongroups.
  name: Microsoft OneNote SectionGroups API
  slug: microsoft-onenote-sectiongroups-api
- description: The Sections API from Microsoft OneNote — 3 operation(s) for sections.
  name: Microsoft OneNote Sections API
  slug: microsoft-onenote-sections-api
artifact_total: 11
collections:
- collection_type: open
  name: Microsoft OneNote API (Microsoft Graph)
  slug: open-microsoft-onenote
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-onenote-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-onenote-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-onenote-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/microsoftgraph
- group: start
  title: ''
  type: Portal
  url: https://portal.azure.com/
- group: company
  title: ''
  type: Website
  url: https://www.microsoft.com/en-us/microsoft-365/onenote/digital-note-taking-app
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/graph/integrate-with-onenote
- group: auth
  title: ''
  type: Authentication
  url: https://learn.microsoft.com/en-us/graph/auth/
- group: build
  title: ''
  type: SDKs
  url: https://learn.microsoft.com/en-us/graph/sdks/sdks-overview
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.microsoft.com/en-us/graph/changelog
- group: operate
  title: ''
  type: RateLimits
  url: https://learn.microsoft.com/en-us/graph/throttling
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
description: Microsoft OneNote is a digital note-taking application. It provides API access through Microsoft Graph for managing notebooks, sections, section groups, and pages stored in OneDrive or SharePoint.
finops:
- name: Microsoft Onenote Finops
  service_category: API
  slug: microsoft-onenote-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-onenote.png
layout: provider
modified: '2026-05-19'
name: Microsoft OneNote
nav: Providers
network: true
overview: 'Microsoft OneNote publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Notebooks API, Pages API, SectionGroups API, and 1 more. Tagged areas include Microsoft, Microsoft 365, Notebooks, Notes, and Productivity.


  Microsoft OneNote''s developer surface includes authentication, developer portal, documentation, changelog, support, and 9 more developer resources.'
plans:
- name: Microsoft Onenote Plans Pricing
  plan_count: 3
  slug: microsoft-onenote-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 5
  name: Microsoft Onenote Rate Limits
  slug: microsoft-onenote-rate-limits
score:
  band: developing
  composite: 45.7
  delta: -1.8
  facets:
    commercial_clarity: 60.5
    contract_quality: 50.0
    developer_ergonomics: 39.1
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 47.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-onenote/refs/heads/main/screenshots/microsoft-onenote-2026-06-20T185517.png
security:
- kind: authentication
  name: Microsoft Onenote Authentication
  slug: microsoft-onenote-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Microsoft Onenote Domain Security
  slug: microsoft-onenote-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: microsoft-onenote
tags:
- Microsoft
- Microsoft 365
- Notebooks
- Notes
- Productivity
website: https://www.microsoft.com/en-us/microsoft-365/onenote/digital-note-taking-app
---
