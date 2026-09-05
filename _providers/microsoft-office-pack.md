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
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.1
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Microsoft Office Pack Agentic Access
  operation_count: 15
  slug: microsoft-office-pack-agentic-access
  summary_line: 15 operations · 4 acting
api_count: 9
apis:
- description: API for creating, reading, and modifying Word documents.
  name: Word API
  slug: word-api
- description: API for working with Excel workbooks, worksheets, charts, and tables.
  name: Excel API
  slug: excel-api
- description: API for creating and modifying PowerPoint presentations.
  name: PowerPoint API
  slug: powerpoint-api
- description: API for accessing and managing email messages, calendars, and contacts.
  name: Outlook Mail API
  slug: outlook-mail-api
- description: API for accessing files and folders stored in OneDrive.
  name: OneDrive API
  slug: onedrive-api
- description: API for accessing SharePoint sites, lists, and content.
  name: SharePoint API
  slug: sharepoint-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: spec
  description: The Drive API from Microsoft Office Pack — 4 operation(s) for drive.
  name: Microsoft Office Pack Drive API
  slug: microsoft-office-pack-drive-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: spec
  description: The Mail API from Microsoft Office Pack — 4 operation(s) for mail.
  name: Microsoft Office Pack Mail API
  slug: microsoft-office-pack-mail-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: spec
  description: The Teams API from Microsoft Office Pack — 4 operation(s) for teams.
  name: Microsoft Office Pack Teams API
  slug: microsoft-office-pack-teams-api
artifact_total: 21
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Microsoft Graph API - Office Pack Drive API
  slug: open-microsoft-office-pack-drive-api
- collection_type: open
  name: Microsoft Graph API - Office Pack Drive Mail API
  slug: open-microsoft-office-pack-mail-api
- collection_type: open
  name: Microsoft Graph API - Office Pack Drive Teams API
  slug: open-microsoft-office-pack-teams-api
- collection_type: open
  name: Microsoft Graph API - Office Pack
  slug: open-microsoft-office-pack
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-office-pack-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-office-pack-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-office-pack-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-office-pack-scopes.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.microsoft.com/servicesagreement
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/privacystatement
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.microsoft.com/microsoft-365
- group: operate
  title: ''
  type: StatusPage
  url: https://status.dev.microsoft.com/
- group: company
  title: ''
  type: Blog
  url: https://developer.microsoft.com/microsoft-365/blogs/
created: '2024'
description: A collection of APIs for Microsoft Office productivity applications including Word, Excel, PowerPoint, Outlook, and OneDrive.
finops:
- name: Microsoft Office Pack Finops
  service_category: API
  slug: microsoft-office-pack-finops
layout: provider
modified: '2026-04-28'
name: Microsoft Office Pack
nav: Providers
network: true
overview: 'Microsoft Office Pack publishes 3 APIs on the [APIs.io](https://apis.io/) network: Drive API, Mail API, and Teams API.


  Microsoft Office Pack''s developer surface includes authentication, engineering blog, and 7 more developer resources.'
plans:
- name: Microsoft Office Pack Plans Pricing
  plan_count: 3
  slug: microsoft-office-pack-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 5
  name: Microsoft Office Pack Rate Limits
  slug: microsoft-office-pack-rate-limits
scopes:
- name: Microsoft Office Pack Scopes
  scope_count: 7
  slug: microsoft-office-pack-scopes
  summary_line: 7 scopes · authorizationCode
score:
  band: thin
  composite: 37.7
  coverage:
    artifact_dirs: 11
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 0.0
    contract_quality: 53.7
    developer_ergonomics: 52.4
    discoverability: 33.3
    governance: 0.0
    operational_transparency: 15.8
  previous_composite: 37.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    note: provider declares no identity tags; regime could not be determined
    undetermined: true
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-office-pack/refs/heads/main/screenshots/microsoft-office-pack-2026-06-20T185514.png
security:
- kind: authentication
  name: Microsoft Office Pack Authentication
  slug: microsoft-office-pack-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Microsoft Office Pack Domain Security
  slug: microsoft-office-pack-domain-security
  summary_line: TLSv1.3 · DMARC
slug: microsoft-office-pack
website: https://developer.microsoft.com/microsoft-365
---
