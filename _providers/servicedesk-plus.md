---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
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
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.5
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Servicedesk Plus Agentic Access
  operation_count: 6
  slug: servicedesk-plus-agentic-access
  summary_line: 6 operations · 4 acting
api_count: 2
apis:
- description: REST API for ServiceDesk Plus enabling programmatic management of requests, problems, changes, releases, assets, the CMDB, users, technicians, projects, and configuration items.
  name: ServiceDesk Plus REST API
  slug: rest-api
- description: The Requests API from ManageEngine ServiceDesk Plus — 3 operation(s) for requests.
  name: ManageEngine ServiceDesk Plus Requests API
  slug: servicedesk-plus-requests-api
artifact_total: 9
collections:
- collection_type: open
  name: ManageEngine ServiceDesk Plus Cloud API
  slug: open-servicedesk-plus
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/servicedesk-plus-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/servicedesk-plus-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/servicedesk-plus-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/servicedesk-plus-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/servicedesk-plus-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/servicedesk-plus-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ManageEngine
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/manageengine-it-service-management
- group: company
  title: ''
  type: Website
  url: https://www.manageengine.com/products/service-desk/
- group: docs
  title: ''
  type: Documentation
  url: https://www.manageengine.com/products/service-desk/help/adminguide/api/rest-api.html
- group: commercial
  title: ''
  type: Pricing
  url: https://www.manageengine.com/products/service-desk/pricing.html
- group: start
  title: ''
  type: Signup
  url: https://www.manageengine.com/products/service-desk/free-trial.html
- group: company
  title: ''
  type: Blog
  url: https://blogs.manageengine.com/feed
created: '2026-05-11'
description: ManageEngine ServiceDesk Plus is a comprehensive IT service management (ITSM) suite with incident, problem, change, release, and asset management modules, plus a CMDB and project management. ServiceDesk Plus is available as cloud (SaaS) or on-premises, and exposes a REST API for integrating external systems with requests, problems, changes, assets, and the CMDB.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/servicedesk-plus.png
layout: provider
modified: '2026-05-11'
name: ManageEngine ServiceDesk Plus
nav: Providers
network: true
overview: 'ManageEngine ServiceDesk Plus publishes 1 API on the [APIs.io](https://apis.io/) network: Requests API. Tagged areas include ITSM, Help Desk, Incident Management, Asset Management, and CMDB.


  ManageEngine ServiceDesk Plus'' developer surface includes authentication, documentation, pricing, signup flow, engineering blog, and 8 more developer resources.'
random_paper: 33
scopes:
- name: Servicedesk Plus Scopes
  scope_count: 5
  slug: servicedesk-plus-scopes
  summary_line: 5 scopes · authorizationCode
score:
  band: thin
  composite: 28.1
  delta: -1.8
  facets:
    commercial_clarity: 18.4
    contract_quality: 50.0
    developer_ergonomics: 21.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 29.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/servicedesk-plus/refs/heads/main/screenshots/servicedesk-plus-2026-06-20T193729.png
security:
- kind: authentication
  name: Servicedesk Plus Authentication
  slug: servicedesk-plus-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Servicedesk Plus Domain Security
  slug: servicedesk-plus-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Servicedesk Plus Vulnerability Disclosure
  slug: servicedesk-plus-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Servicedesk Plus Trust Center
  slug: servicedesk-plus-trust-center
  summary_line: ISO 27001, HIPAA, GDPR
slug: servicedesk-plus
tags:
- ITSM
- Help Desk
- Incident Management
- Asset Management
- CMDB
website: https://www.manageengine.com/products/service-desk/
---
