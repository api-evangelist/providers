---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-04'
api_count: 2
apis:
- description: 'RESTful Web API for managing TeamViewer users, devices, device groups, sessions, session history, and meetings within a TeamViewer company account. Authentication uses OAuth 2.0 bearer tokens (either '
  name: TeamViewer Web API
  slug: web-api
- description: SCIM 2.0 API for automated user provisioning, deprovisioning, and lifecycle management within a TeamViewer company, enabling integration with identity providers such as Okta, Azure AD, and OneLogin.
  name: TeamViewer SCIM API
  slug: scim-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/teamviewer-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/teamviewer-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.teamviewer.com
- group: docs
  title: ''
  type: Documentation
  url: https://webapi.teamviewer.com/api/v1/docs/index
- group: commercial
  title: ''
  type: Pricing
  url: https://www.teamviewer.com/en/pricing/
- group: start
  title: ''
  type: Signup
  url: https://login.teamviewer.com/LogOn#register
- group: operate
  title: ''
  type: Support
  url: https://www.teamviewer.com/en/global/support/
- group: operate
  title: ''
  type: Community
  url: https://community.teamviewer.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/teamviewer
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/teamviewer
created: '2026-05-11'
description: TeamViewer is a global provider of remote connectivity, remote access, and remote support software used by IT teams, MSPs, and enterprises to manage devices, deliver IT support, and connect operational technology across desktops, mobile devices, and IoT endpoints. The TeamViewer Web API is a RESTful API that uses OAuth 2.0 bearer token authentication and JSON to programmatically manage users, devices, groups, sessions, session reports, and meetings within a TeamViewer company account.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/teamviewer.png
layout: provider
modified: '2026-05-11'
name: TeamViewer
nav: Providers
network: true
overview: 'TeamViewer publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Remote Access, Remote Support, Remote Desktop, IT Management, and Endpoint Management.


  TeamViewer''s developer surface includes documentation, pricing, signup flow, support, and 6 more developer resources.'
random_paper: 10
score:
  band: emerging
  composite: 17.2
  coverage:
    artifact_dirs: 2
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 17.2
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/teamviewer/refs/heads/main/screenshots/teamviewer-2026-06-20T195000.png
security:
- kind: domain-security
  name: Teamviewer Domain Security
  slug: teamviewer-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Teamviewer Vulnerability Disclosure
  slug: teamviewer-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: teamviewer
tags:
- Remote Access
- Remote Support
- Remote Desktop
- IT Management
- Endpoint Management
- Unified Endpoint Management
website: https://www.teamviewer.com
---
