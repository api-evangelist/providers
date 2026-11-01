---
access_model:
  confidence: high
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: true
  source:
  - https://docs.getbluma.com/concepts/credits
  - https://docs.getbluma.com/guides/test-vs-production
  trial: true
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 45.7
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: Asynchronous short-form video generation REST API. Submit a template id and a prompt to POST /v1/videos, receive a job id, and collect the finished render either by polling GET /v1/videos/{id} or by s
  name: Bluma API
  slug: bluma-api
- description: Hosted Model Context Protocol server on the Bluma API host. Discovered via RFC 9728 OAuth Protected Resource Metadata rather than from the documentation, which never mentions it. Requires an OAuth 2.1
  name: Bluma MCP Server
  slug: bluma-mcp-server
artifact_total: 14
asyncapis:
- description: ''
  name: Bluma Webhooks
  slug: bluma-webhooks
common:
- group: company
  title: ''
  type: Blog
  url: https://www.getbluma.com/blog/
- group: auth
  href: https://artifacts.apis.io/bluma/security/bluma-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bluma-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.getbluma.com
- group: start
  title: ''
  type: SignUp
  url: https://www.getbluma.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.getbluma.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.getbluma.com/privacy
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.getbluma.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.getbluma.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.getbluma.com/api-reference/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.getbluma.com/quickstart
- group: auth
  href: https://artifacts.apis.io/bluma/authentication/bluma-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bluma-authentication.yml
- group: auth
  href: https://artifacts.apis.io/bluma/scopes/bluma-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/bluma-scopes.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.getbluma.com/concepts/credits
- group: commercial
  href: https://artifacts.apis.io/bluma/plans/bluma-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bluma-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/bluma/rate-limits/bluma-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/bluma-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/bluma/errors/bluma-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/bluma-problem-types.yml
- group: design
  href: https://artifacts.apis.io/bluma/conventions/bluma-conventions.yml
  title: ''
  type: Conventions
  url: conventions/bluma-conventions.yml
- group: design
  href: https://artifacts.apis.io/bluma/data-model/bluma-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bluma-data-model.yml
- group: design
  href: https://artifacts.apis.io/bluma/lifecycle/bluma-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/bluma-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/bluma/changelog/bluma-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/bluma-changelog.yml
- group: design
  href: https://artifacts.apis.io/bluma/conformance/bluma-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bluma-conformance.yml
- group: start
  href: https://artifacts.apis.io/bluma/sandbox/bluma-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/bluma-sandbox.yml
- group: build
  href: https://artifacts.apis.io/bluma/packages/bluma-packages.yml
  title: ''
  type: Packages
  url: packages/bluma-packages.yml
- group: build
  href: https://artifacts.apis.io/bluma/packages/bluma-packages.yml
  title: ''
  type: SDKs
  url: packages/bluma-packages.yml
- group: design
  href: https://artifacts.apis.io/bluma/asyncapi/bluma-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/bluma-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/bluma/mcp/bluma-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/bluma-mcp.yml
- group: agent
  href: https://artifacts.apis.io/bluma/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/bluma/well-known/bluma-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bluma-well-known.yml
- group: agent
  href: https://artifacts.apis.io/bluma/llms/bluma-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bluma-llms.txt
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/cZGXY4nrFZ
- group: start
  title: ''
  type: Login
  url: https://app.getbluma.com/settings?tab=api
created: '2026-07-17'
description: 'Bluma is a San Francisco-based AI company (Y Combinator Fall 2025) building a short-form AI content engine that lets creators, agencies, and brands produce social media video ads at scale. The platform "de-edits" existing reference videos into their individual scenes, captions, and overlays, then uses AI asset generation and a node-based canvas editor to recreate and remix shots into new ads, UGC, and template-based videos optimized for TikTok, Reels, and Shorts. Bluma ships a public developer program: a REST API at api.getbluma.com/api/v1 for asynchronous video generation, templates, credits, API keys, webhooks and usage analytics; Mintlify-hosted documentation at docs.getbluma.com; first-party TypeScript and Python SDKs; a seven-event HMAC-signed webhook surface; published per-tier rate limits; and an undocumented but live hosted MCP server at api.getbluma.com/api/mcp gated by Clerk OAuth 2.1 with dynamic client registration. Founded by Alisa Wu (formerly Zoox/Amazon) and
  Stephen Ni.'
finops:
- has_sources: true
  method: derived
  name: Bluma Finops
  primary_unit: subscription
  service_category: ''
  slug: bluma-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bluma.png
layout: provider
mcp_servers:
- description: Remote MCP server at api.getbluma.com.
  name: Bluma MCP Server
  slug: bluma-mcp-yml
modified: '2026-10-06'
name: Bluma
nav: Providers
network: true
overview: 'Bluma is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Video, Video Generation, and Advertising.


  The Bluma catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Bluma''s developer surface includes engineering blog, signup flow, documentation, API reference, getting-started guide, authentication, pricing, and 24 more developer resources.'
plans:
- name: Bluma Plans Pricing
  plan_count: 6
  slug: bluma-plans-pricing
- name: Bluma Price Estimates
  plan_count: 0
  slug: bluma-price-estimates
random_paper: 1
rate_limits:
- limit_count: 4
  name: Bluma Rate Limits
  slug: bluma-rate-limits
scopes:
- name: Bluma Scopes
  scope_count: 0
  slug: bluma-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 59.2
  coverage:
    artifact_dirs: 23
    catalog_earned: 64.0
    catalog_earned_first_party: 24.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.6
  facets:
    access_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 39.0
    developer_ergonomics: 73.2
    discoverability: 65.0
    operational_transparency: 55.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 57.6
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 31.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/bluma/bluma-2026-07-25T203511.png
security:
- kind: authentication
  name: Bluma Authentication
  slug: bluma-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Bluma Domain Security
  slug: bluma-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: bluma-generate-video
  slug: bluma-generate-video
- name: bluma-handle-webhooks
  slug: bluma-handle-webhooks
- name: bluma-manage-api-keys
  slug: bluma-manage-api-keys
slug: bluma
tags:
- Company
- Artificial Intelligence
- Video
- Video Generation
- Advertising
- Marketing
- Content Creation
- Short-Form Video
- Social Media
- Generative AI
- Creative Tools
- Text-to-Speech
- Media
- Automation
- Webhook
website: https://www.getbluma.com
---
