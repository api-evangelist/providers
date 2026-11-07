---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 40.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 32
  human_in_the_loop: 0
  name: Companycam Agentic Access
  operation_count: 62
  slug: companycam-agentic-access
  summary_line: 62 operations · 32 acting
api_count: 1
apis:
- baseURL: https://api.companycam.com/v2
  baseurl_source: declared
  description: The Checklists API from CompanyCam — 1 operation(s) for checklists.
  name: CompanyCam Checklists API
  slug: companycam-checklists-api
- baseURL: https://api.companycam.com/v2
  baseurl_source: declared
  description: The Company API from CompanyCam — 1 operation(s) for company.
  name: CompanyCam Company API
  slug: companycam-company-api
- baseURL: https://api.companycam.com/v2
  baseurl_source: declared
  description: The Groups API from CompanyCam — 2 operation(s) for groups.
  name: CompanyCam Groups API
  slug: companycam-groups-api
- baseURL: https://api.companycam.com/v2
  baseurl_source: declared
  description: The Photos API from CompanyCam — 5 operation(s) for photos.
  name: CompanyCam Photos API
  slug: companycam-photos-api
- baseURL: https://api.companycam.com/v2
  baseurl_source: declared
  description: The Projects API from CompanyCam — 17 operation(s) for projects.
  name: CompanyCam Projects API
  slug: companycam-projects-api
- baseURL: https://api.companycam.com/v2
  baseurl_source: declared
  description: The Tags API from CompanyCam — 2 operation(s) for tags.
  name: CompanyCam Tags API
  slug: companycam-tags-api
- baseURL: https://api.companycam.com/v2
  baseurl_source: declared
  description: The Templates API from CompanyCam — 1 operation(s) for templates.
  name: CompanyCam Templates API
  slug: companycam-templates-api
- baseURL: https://api.companycam.com/v2
  baseurl_source: declared
  description: The Users API from CompanyCam — 3 operation(s) for users.
  name: CompanyCam Users API
  slug: companycam-users-api
- baseURL: https://api.companycam.com/v2
  baseurl_source: declared
  description: The Videos API from CompanyCam — 2 operation(s) for videos.
  name: CompanyCam Videos API
  slug: companycam-videos-api
- baseURL: https://api.companycam.com/v2
  baseurl_source: declared
  description: The Webhooks API from CompanyCam — 2 operation(s) for webhooks.
  name: CompanyCam Webhooks API
  slug: companycam-webhooks-api
artifact_total: 34
asyncapis:
- description: ''
  name: Companycam Webhooks
  slug: companycam-webhooks
collections:
- collection_type: open
  name: Core Checklists API
  slug: open-companycam-checklists-api
- collection_type: open
  name: Core Checklists Company API
  slug: open-companycam-company-api
- collection_type: open
  name: Core Checklists Groups API
  slug: open-companycam-groups-api
- collection_type: open
  name: Core Checklists Photos API
  slug: open-companycam-photos-api
- collection_type: open
  name: Core Checklists Projects API
  slug: open-companycam-projects-api
- collection_type: open
  name: Core Checklists Tags API
  slug: open-companycam-tags-api
- collection_type: open
  name: Core Checklists Templates API
  slug: open-companycam-templates-api
- collection_type: open
  name: Core Checklists Users API
  slug: open-companycam-users-api
- collection_type: open
  name: API Collection
  slug: open-companycam-v2
- collection_type: open
  name: Core Checklists Videos API
  slug: open-companycam-videos-api
- collection_type: open
  name: Core Checklists Webhooks API
  slug: open-companycam-webhooks-api
common:
- group: other
  href: https://artifacts.apis.io/companycam/capabilities/companycam-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/companycam-capability-edges.yml
- group: commercial
  href: https://artifacts.apis.io/companycam/plans/companycam-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/companycam-plans-pricing.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/companycam/overview
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
  href: https://artifacts.apis.io/companycam/openapi/companycam-v2.postman_collection.json
  title: ''
  type: Postman
  url: openapi/companycam-v2.postman_collection.json
- group: agent
  href: https://artifacts.apis.io/companycam/llms/companycam-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/companycam-llms.txt
- group: build
  href: https://artifacts.apis.io/companycam/packages/companycam-packages.yml
  title: ''
  type: SDKs
  url: packages/companycam-packages.yml
- group: build
  href: https://artifacts.apis.io/companycam/packages/companycam-packages.yml
  title: ''
  type: Packages
  url: packages/companycam-packages.yml
- group: auth
  href: https://artifacts.apis.io/companycam/authentication/companycam-authentication.yml
  title: ''
  type: Authentication
  url: authentication/companycam-authentication.yml
- group: auth
  href: https://artifacts.apis.io/companycam/scopes/companycam-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/companycam-scopes.yml
- group: design
  href: https://artifacts.apis.io/companycam/conventions/companycam-conventions.yml
  title: ''
  type: Conventions
  url: conventions/companycam-conventions.yml
- group: operate
  href: https://artifacts.apis.io/companycam/rate-limits/companycam-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/companycam-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/companycam/errors/companycam-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/companycam-problem-types.yml
- group: design
  href: https://artifacts.apis.io/companycam/lifecycle/companycam-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/companycam-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/companycam/conformance/companycam-conformance.yml
  title: ''
  type: Conformance
  url: conformance/companycam-conformance.yml
- group: operate
  href: https://artifacts.apis.io/companycam/changelog/companycam-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/companycam-changelog.yml
- group: design
  href: https://artifacts.apis.io/companycam/data-model/companycam-data-model.yml
  title: ''
  type: DataModel
  url: data-model/companycam-data-model.yml
- group: design
  href: https://artifacts.apis.io/companycam/asyncapi/companycam-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/companycam-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/companycam/well-known/companycam-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/companycam-well-known.yml
- group: auth
  href: https://artifacts.apis.io/companycam/well-known/companycam-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/companycam-security.txt
- group: auth
  href: https://artifacts.apis.io/companycam/well-known/companycam-security.txt
  title: ''
  type: Security
  url: well-known/companycam-security.txt
- group: auth
  href: https://artifacts.apis.io/companycam/security/companycam-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/companycam-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/companycam/security/companycam-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/companycam-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/companycam/agentic-access/companycam-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/companycam-agentic-access.yml
- group: agent
  href: https://artifacts.apis.io/companycam/mcp/companycam-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/companycam-mcp.yml
- group: agent
  href: https://artifacts.apis.io/companycam/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://artifacts.apis.io/companycam/overlays/companycam-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/companycam-openapi-overlay.yaml
created: '2026-07-17'
description: CompanyCam is a photo-based job-site documentation platform for contractors and the trades — roofing, restoration, solar, home services and construction. Its mobile apps capture location- and time-stamped photos and videos that sync to a shared, project-organized workspace so crews, offices and clients stay aligned. The CompanyCam Core API (v2) is a REST API over projects, photos, videos, users, groups, tags, comments, documents, checklists and webhooks, secured with Bearer access tokens or OAuth 2.0 (authorization-code with PKCE and refresh tokens). It publishes an official OpenAPI 3.0 description, a Postman collection, granular per-resource OAuth scopes advertised via RFC 8414 metadata, HMAC-signed webhooks, and per-method rate limits. CompanyCam is backed by Insight Partners.
finops:
- has_sources: true
  method: derived
  name: Companycam Finops
  primary_unit: subscription
  service_category: ''
  slug: companycam-finops
  template: false
image: https://cdn.companycam.com/dist/img/site/favicon-96x96-2021.png
layout: provider
modified: '2026-07-18'
name: CompanyCam
nav: Providers
network: true
overview: 'CompanyCam publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Checklists API, Company API, Groups API, and 7 more. Tagged areas include Company, Construction, Photos, Field Service Management, and Project Management.


  The CompanyCam catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  CompanyCam''s developer surface includes documentation, API reference, getting-started guide, changelog, support, engineering blog, pricing, and 33 more developer resources.'
plans:
- name: Companycam Plans Pricing
  plan_count: 4
  slug: companycam-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 4
  name: Companycam Rate Limits
  slug: companycam-rate-limits
rules:
- authorship: generated
  effective_rule_count: 92
  extends:
  - spectral:oas
  name: CompanyCam API Rules
  rule_count: 51
  severity_counts:
    error: 44
    hint: 0
    info: 3
    warn: 4
  slug: companycam-rules
scopes:
- name: Companycam Scopes
  scope_count: 54
  slug: companycam-scopes
  summary_line: 54 scopes · authorizationCode
score:
  band: exemplar
  composite: 71.3
  coverage:
    artifact_dirs: 32
    catalog_earned: 68.5
    catalog_earned_first_party: 24.0
    catalog_gap: 46.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 6.2
  facets:
    access_clarity: 84.2
    contract_governance: 31.8
    contract_quality: 63.4
    developer_ergonomics: 67.3
    discoverability: 73.2
    operational_transparency: 84.2
  previous_composite: 65.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 10
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 40.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/companycam/companycam-2026-07-25T210145.png
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
skill_count: 3
skills:
- name: Document a job site in CompanyCam
  slug: companycam-document-a-project
- name: Connect a CompanyCam account via OAuth 2.0
  slug: companycam-oauth-connect
- name: Subscribe to CompanyCam webhooks and verify deliveries
  slug: companycam-subscribe-to-webhooks
slug: companycam
tags:
- Company
- Construction
- Photos
- Field Service Management
- Project Management
- Contractors
- Documentation
- Webhook
website: https://companycam.com/
---
