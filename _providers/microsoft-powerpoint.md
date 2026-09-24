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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.8
  scored_at: '2026-09-24'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Powerpoint Agentic Access
  operation_count: 9
  slug: powerpoint-agentic-access
  summary_line: 9 operations · 6 acting
api_count: 2
apis:
- description: Microsoft Graph exposes PowerPoint presentation files (.pptx) stored in OneDrive and SharePoint as drive items, enabling upload, download, sharing, and metadata operations against presentations progra
  name: PowerPoint via Microsoft Graph
  slug: powerpoint-graph-api
- description: Office JavaScript API namespace for building PowerPoint Add-ins that read, write, and manipulate slides, shapes, text, and tables inside the running PowerPoint application.
  name: Office JavaScript API for PowerPoint
  slug: powerpoint-javascript-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: Manage files (including .pptx presentations) stored in OneDrive and SharePoint.
  name: Microsoft PowerPoint Drive Items API
  slug: microsoft-powerpoint-drive-items-api
artifact_total: 15
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: PowerPoint via Microsoft Graph DriveItems API
  slug: open-powerpoint-driveitems-api
- collection_type: open
  name: PowerPoint via Microsoft Graph
  slug: open-powerpoint
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-powerpoint/refs/heads/main/agentic-access/powerpoint-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/powerpoint-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-powerpoint/refs/heads/main/security/powerpoint-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/powerpoint-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-powerpoint/refs/heads/main/security/powerpoint-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/powerpoint-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-powerpoint/refs/heads/main/security/powerpoint-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/powerpoint-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-powerpoint/refs/heads/main/authentication/powerpoint-authentication.yml
  title: ''
  type: Authentication
  url: authentication/powerpoint-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-powerpoint/refs/heads/main/scopes/powerpoint-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/powerpoint-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.microsoft.com/en-us/microsoft-365/powerpoint
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/graph/overview
- group: other
  title: ''
  type: Developer
  url: https://learn.microsoft.com/en-us/office/dev/add-ins/
created: '2026-03-16'
description: Microsoft PowerPoint provides programmatic access through the Microsoft Graph API and the Office JavaScript API for creating, reading, and manipulating PowerPoint presentations. PowerPoint files stored in OneDrive and SharePoint are accessible as drive items via Microsoft Graph, while the Office JavaScript API enables in-document automation for Office Add-ins.
finops:
- name: Powerpoint Finops
  service_category: API
  slug: powerpoint-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/powerpoint.png
layout: provider
modified: '2026-09-16'
name: Microsoft PowerPoint
nav: Providers
network: true
overview: 'Microsoft PowerPoint publishes 1 API on the [APIs.io](https://apis.io/) network: Drive Items API. Tagged areas include Microsoft Office, Microsoft 365, Presentations, Productivity, and Documents.


  Microsoft PowerPoint''s developer surface includes authentication, documentation, and 7 more developer resources.'
plans:
- name: Powerpoint Plans Pricing
  plan_count: 3
  slug: powerpoint-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 5
  name: Powerpoint Rate Limits
  slug: powerpoint-rate-limits
scopes:
- name: Powerpoint Scopes
  scope_count: 4
  slug: powerpoint-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: thin
  composite: 30.1
  coverage:
    artifact_dirs: 11
    catalog_earned: 41.0
    catalog_earned_first_party: 0.0
    catalog_gap: 74.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 53.7
    developer_ergonomics: 28.6
    discoverability: 59.3
    operational_transparency: 7.9
  previous_composite: 30.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-powerpoint/refs/heads/main/screenshots/powerpoint-2026-06-20T192039.png
security:
- kind: authentication
  name: Powerpoint Authentication
  slug: powerpoint-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Powerpoint Domain Security
  slug: powerpoint-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Powerpoint Vulnerability Disclosure
  slug: powerpoint-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Powerpoint Trust Center
  slug: powerpoint-trust-center
  summary_line: GDPR
slug: microsoft-powerpoint
tags:
- Microsoft Office
- Microsoft 365
- Presentations
- Productivity
- Documents
website: https://www.microsoft.com/en-us/microsoft-365/powerpoint
---
