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
  band: agent-native
  dimensions:
    agent_skills: true
    agentic_access: true
    asyncapi_events: true
    auth_clarity: true
    consent_identity: true
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.1
  score: 84.6
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 32
  human_in_the_loop: 0
  name: Companycam Agentic Access
  operation_count: 62
  slug: companycam-agentic-access
  summary_line: 62 operations · 32 acting
api_count: 10
apis:
- description: The Checklists API from CompanyCam — 1 operation(s) for checklists.
  name: CompanyCam Checklists API
  slug: companycam-checklists-api
- description: The Company API from CompanyCam — 1 operation(s) for company.
  name: CompanyCam Company API
  slug: companycam-company-api
- description: The Groups API from CompanyCam — 2 operation(s) for groups.
  name: CompanyCam Groups API
  slug: companycam-groups-api
- description: The Photos API from CompanyCam — 5 operation(s) for photos.
  name: CompanyCam Photos API
  slug: companycam-photos-api
- description: The Projects API from CompanyCam — 17 operation(s) for projects.
  name: CompanyCam Projects API
  slug: companycam-projects-api
- description: The Tags API from CompanyCam — 2 operation(s) for tags.
  name: CompanyCam Tags API
  slug: companycam-tags-api
- description: The Templates API from CompanyCam — 1 operation(s) for templates.
  name: CompanyCam Templates API
  slug: companycam-templates-api
- description: The Users API from CompanyCam — 3 operation(s) for users.
  name: CompanyCam Users API
  slug: companycam-users-api
- description: The Videos API from CompanyCam — 2 operation(s) for videos.
  name: CompanyCam Videos API
  slug: companycam-videos-api
- description: The Webhooks API from CompanyCam — 2 operation(s) for webhooks.
  name: CompanyCam Webhooks API
  slug: companycam-webhooks-api
artifact_total: 18
asyncapis:
- description: ''
  name: Companycam Webhooks
  slug: companycam-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://companycam.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.companycam.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.companycam.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.companycam.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.companycam.com/docs/getting-started
- group: operate
  title: ''
  type: ChangeLog
  url: https://companycam.readme.io/changelog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.companycam.com
- group: operate
  title: ''
  type: Support
  url: https://help.companycam.com
- group: company
  title: ''
  type: Blog
  url: https://companycam.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CompanyCam
- group: commercial
  title: ''
  type: Pricing
  url: https://companycam.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.companycam.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://companycam.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://companycam.com/privacy
- group: build
  title: ''
  type: Postman
  url: openapi/companycam-v2.postman_collection.json
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/companycam-llms.txt
- group: build
  title: ''
  type: SDKs
  url: packages/companycam-packages.yml
- group: build
  title: ''
  type: Packages
  url: packages/companycam-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/companycam-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/companycam-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/companycam-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/companycam-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/companycam-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/companycam-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/companycam-conformance.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/companycam-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/companycam-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/companycam-webhooks.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/companycam-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/companycam-security.txt
- group: auth
  title: ''
  type: Security
  url: well-known/companycam-security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/companycam-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/companycam-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/companycam-agentic-access.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/companycam-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/companycam-openapi-overlay.yaml
created: '2026-07-17'
description: CompanyCam is a photo-based job-site documentation platform for contractors and the trades — roofing, restoration, solar, home services and construction. Its mobile apps capture location- and time-stamped photos and videos that sync to a shared, project-organized workspace so crews, offices and clients stay aligned. The CompanyCam Core API (v2) is a REST API over projects, photos, videos, users, groups, tags, comments, documents, checklists and webhooks, secured with Bearer access tokens or OAuth 2.0 (authorization-code with PKCE and refresh tokens). It publishes an official OpenAPI 3.0 description, a Postman collection, granular per-resource OAuth scopes advertised via RFC 8414 metadata, HMAC-signed webhooks, and per-method rate limits. CompanyCam is backed by Insight Partners.
image: https://cdn.companycam.com/dist/img/site/favicon-96x96-2021.png
layout: provider
mcp_servers:
- description: ''
  name: companycam-mcp.yml
  slug: companycam-mcpyml
modified: '2026-07-18'
name: CompanyCam
nav: Providers
network: true
overview: 'CompanyCam publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Checklists API, Company API, Groups API, and 7 more. Tagged areas include Company, Construction, Photos, Field Service, and Project Management.


  The CompanyCam catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  CompanyCam''s developer surface includes documentation, API reference, getting-started guide, changelog, support, engineering blog, pricing, and 30 more developer resources.'
random_paper: 44
rate_limits:
- limit_count: 0
  name: Companycam Rate Limits
  slug: companycam-rate-limits
scopes:
- name: Companycam Scopes
  scope_count: 54
  slug: companycam-scopes
  summary_line: 54 scopes · authorizationCode
score:
  band: developing
  composite: 57.7
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 63.5
    developer_ergonomics: 78.3
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 55.3
  previous_composite: 57.7
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Companycam Authentication
  slug: companycam-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Companycam Domain Security
  slug: companycam-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Companycam Vulnerability Disclosure
  slug: companycam-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: companycam
tags:
- Company
- Construction
- Photos
- Field Service
- Project Management
- Contractors
- Documentation
- Webhooks
website: https://companycam.com/
---
