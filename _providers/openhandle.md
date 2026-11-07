---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 54.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Openhandle Agentic Access
  operation_count: 109
  slug: openhandle-agentic-access
  summary_line: 109 operations
api_count: 1
apis:
- baseURL: https://api.openhandle.dev
  baseurl_source: declared
  description: The Instagram API from Openhandle — 43 operation(s) for instagram.
  name: Openhandle Instagram API
  slug: openhandle-instagram-api
- baseURL: https://api.openhandle.dev
  baseurl_source: declared
  description: The Reddit API from Openhandle — 20 operation(s) for reddit.
  name: Openhandle Reddit API
  slug: openhandle-reddit-api
- baseURL: https://api.openhandle.dev
  baseurl_source: declared
  description: The Test Data API from Openhandle — 2 operation(s) for test data.
  name: Openhandle Test Data API
  slug: openhandle-test-data-api
- baseURL: https://api.openhandle.dev
  baseurl_source: declared
  description: The Tiktok API from Openhandle — 28 operation(s) for tiktok.
  name: Openhandle Tiktok API
  slug: openhandle-tiktok-api
- baseURL: https://api.openhandle.dev
  baseurl_source: declared
  description: The Twitter API from Openhandle — 15 operation(s) for twitter.
  name: Openhandle Twitter API
  slug: openhandle-twitter-api
- baseURL: https://api.openhandle.dev
  baseurl_source: declared
  description: The Utilities API from Openhandle — 1 operation(s) for utilities.
  name: Openhandle Utilities API
  slug: openhandle-utilities-api
artifact_total: 27
common:
- group: other
  href: https://artifacts.apis.io/openhandle/capabilities/openhandle-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/openhandle-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/openhandle/agentic-access/openhandle-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/openhandle-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/openhandle/rate-limits/openhandle-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/openhandle-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/openhandle/plans/openhandle-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/openhandle-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/openhandle/rules/openhandle-rules.yml
  title: ''
  type: Spectral
  url: rules/openhandle-rules.yml
- group: design
  href: https://artifacts.apis.io/openhandle/json-ld/openhandle-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/openhandle-context.jsonld
- group: design
  href: https://artifacts.apis.io/openhandle/vocabulary/openhandle-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/openhandle-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/openhandle/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/openhandle/data-model/openhandle-data-model.yml
  title: ''
  type: DataModel
  url: data-model/openhandle-data-model.yml
- group: design
  href: https://artifacts.apis.io/openhandle/conventions/openhandle-conventions.yml
  title: ''
  type: Conventions
  url: conventions/openhandle-conventions.yml
- group: start
  href: https://artifacts.apis.io/openhandle/sandbox/openhandle-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/openhandle-sandbox.yml
- group: auth
  href: https://artifacts.apis.io/openhandle/security/openhandle-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/openhandle-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/openhandle/authentication/openhandle-authentication.yml
  title: ''
  type: Authentication
  url: authentication/openhandle-authentication.yml
- group: auth
  href: https://artifacts.apis.io/openhandle/scopes/openhandle-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/openhandle-scopes.yml
- group: design
  href: https://artifacts.apis.io/openhandle/lifecycle/openhandle-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/openhandle-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/openhandle/errors/openhandle-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/openhandle-problem-types.yml
- group: design
  href: https://artifacts.apis.io/openhandle/conformance/openhandle-conformance.yml
  title: ''
  type: Conformance
  url: conformance/openhandle-conformance.yml
- group: other
  href: https://artifacts.apis.io/openhandle/overlays/openhandle-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/openhandle-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/openhandle/llms/openhandle-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/openhandle-llms.txt
- group: build
  href: https://artifacts.apis.io/openhandle/mcp/openhandle-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/openhandle-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/openhandle/mcp/openhandle-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/openhandle-mcp.yml
- group: agent
  href: https://artifacts.apis.io/openhandle/well-known/openhandle-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/openhandle-well-known.yml
- group: build
  href: https://artifacts.apis.io/openhandle/packages/openhandle-packages.yml
  title: ''
  type: SDKs
  url: packages/openhandle-packages.yml
- group: build
  href: https://artifacts.apis.io/openhandle/packages/openhandle-packages.yml
  title: ''
  type: Packages
  url: packages/openhandle-packages.yml
- group: company
  title: ''
  type: Website
  url: https://openhandle.dev
- group: docs
  title: ''
  type: Documentation
  url: https://openhandle.dev/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://openhandle.dev/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.openhandle.dev
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/openhandlehq
- group: operate
  title: ''
  type: Support
  url: https://openhandle.dev/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://openhandle.dev/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://openhandle.dev/legal/privacy-policy
created: '2026-09-21'
description: Openhandle is a public social data API for Instagram, TikTok, X (Twitter), and Reddit. Public profiles, posts, comments, followers, and search come back in one normalized schema, with a capture time and a source on every answer and nulls where a platform hides a value. Pricing is per answered request with cheaper cached tiers (free at 30 days), caps per account and per key, and a full Test environment on synthetic data at $0.000. The API is read-only over OpenAPI 3.1, three first-party SDKs (TypeScript, Python, Go), and a remote OAuth-protected MCP server. Operated as a Netherlands sole proprietorship (KvK 89247647).
finops:
- has_sources: true
  method: derived
  name: Openhandle Finops
  primary_unit: ''
  service_category: ''
  slug: openhandle-finops
  template: true
image: https://openhandle.dev/favicon.ico
json_schemas:
- name: InstagramPost
  property_count: 39
  slug: openhandle-instagram-post
- name: InstagramProfile
  property_count: 42
  slug: openhandle-instagram-profile
- name: InstagramStory
  property_count: 44
  slug: openhandle-instagram-story
- name: TikTokMusic
  property_count: 40
  slug: openhandle-tik-tok-music
- name: TikTokPost
  property_count: 38
  slug: openhandle-tik-tok-post
- name: TikTokProfile
  property_count: 29
  slug: openhandle-tik-tok-profile
jsonld:
- class_count: 120
  name: Openhandle Context
  property_count: 410
  slug: openhandle-context
layout: provider
mcp_servers:
- description: Read public Instagram, TikTok, X, and Reddit data through MCP. Connect with OAuth or an Openhandle API key. Every public REST endpoint is exposed as one tool; tool names, inputs, and responses match t
  name: Openhandle MCP Server
  slug: dev-openhandle-social-data
modified: '2026-09-21'
name: Openhandle
nav: Providers
network: true
overview: 'Openhandle publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Instagram API, Reddit API, Test Data API, and 3 more. Tagged areas include Social Data, Instagram, TikTok, Twitter, and Reddit.


  The Openhandle catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Openhandle''s developer surface includes sandbox, authentication, documentation, pricing, signup flow, support, and 26 more developer resources.'
plans:
- name: Openhandle Plans Pricing
  plan_count: 3
  slug: openhandle-plans-pricing
- name: Openhandle Price Estimates
  plan_count: 0
  slug: openhandle-price-estimates
random_paper: 22
rate_limits:
- limit_count: 2
  name: Openhandle Rate Limits
  slug: openhandle-rate-limits
rules:
- authorship: generated
  effective_rule_count: 59
  extends:
  - spectral:oas
  name: Openhandle API Rules
  rule_count: 18
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 7
  slug: openhandle-rules
scopes:
- name: Openhandle Scopes
  scope_count: 4
  slug: openhandle-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: strong
  composite: 54.4
  coverage:
    artifact_dirs: 31
    catalog_earned: 82.8
    catalog_earned_first_party: 20.0
    catalog_gap: 32.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.3
  facets:
    access_clarity: 53.9
    contract_governance: 35.6
    contract_quality: 71.8
    developer_ergonomics: 44.6
    discoverability: 75.0
    operational_transparency: 23.7
  previous_composite: 61.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 6
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/openhandle/openhandle-2026-10-11T112057.png
security:
- kind: authentication
  name: Openhandle Authentication
  slug: openhandle-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Openhandle Domain Security
  slug: openhandle-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 4
skills:
- name: openhandle-brand-monitoring-search
  slug: openhandle-brand-monitoring-search
- name: openhandle-instagram-profile-and-posts
  slug: openhandle-instagram-profile-and-posts
- name: openhandle-quickstart
  slug: openhandle-openhandle
- name: openhandle-tiktok-user-videos
  slug: openhandle-tiktok-user-videos
slug: openhandle
tags:
- Social Data
- Instagram
- TikTok
- Twitter
- Reddit
- Public Data
- social-media-api
- MCP
- creator-analytics
- Social Listening
website: https://openhandle.dev
---
