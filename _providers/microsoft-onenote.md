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
  scored_at: '2026-09-01'
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
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Microsoft OneNote API (Microsoft Graph) Notebooks API
  slug: open-microsoft-onenote-notebooks-api
- collection_type: open
  name: Microsoft OneNote API (Microsoft Graph) Notebooks Pages API
  slug: open-microsoft-onenote-pages-api
- collection_type: open
  name: Microsoft OneNote API (Microsoft Graph) Notebooks SectionGroups API
  slug: open-microsoft-onenote-sectiongroups-api
- collection_type: open
  name: Microsoft OneNote API (Microsoft Graph) Notebooks Sections API
  slug: open-microsoft-onenote-sections-api
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
overview: 'Microsoft OneNote publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Notebooks API, Pages API, SectionGroups API, and 1 more. Tagged areas include Microsoft, Microsoft-365, Notebooks, Notes, and Productivity.


  Microsoft OneNote''s developer surface includes authentication, developer portal, documentation, changelog, support, and 9 more developer resources.'
plans:
- name: Microsoft Onenote Plans Pricing
  plan_count: 3
  slug: microsoft-onenote-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 5
  name: Microsoft Onenote Rate Limits
  slug: microsoft-onenote-rate-limits
score:
  band: thin
  composite: 39.2
  coverage:
    artifact_dirs: 9
    catalog_gap: 71.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 47.6
    developer_ergonomics: 50.0
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 39.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.18.0
  scored_at: '2026-09-01'
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
- Microsoft-365
- Notebooks
- Notes
- Productivity
website: https://www.microsoft.com/en-us/microsoft-365/onenote/digital-note-taking-app
---
