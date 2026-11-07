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
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-native
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
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 57.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Deploy Social Agentic Access
  operation_count: 18
  slug: deploy-social-agentic-access
  summary_line: 18 operations · 9 acting
api_count: 1
apis:
- baseURL: https://api.deploy.social/v1
  baseurl_source: declared
  description: The key you're using and its workspace.
  name: deploy.social Account API
  slug: deploy-social-account-api
- baseURL: https://api.deploy.social/v1
  baseurl_source: declared
  description: The social accounts connected to your workspace, and what each one takes.
  name: deploy.social Destinations API
  slug: deploy-social-destinations-api
- baseURL: https://api.deploy.social/v1
  baseurl_source: declared
  description: 'Videos: upload them, then use them in posts.'
  name: deploy.social Media API
  slug: deploy-social-media-api
- baseURL: https://api.deploy.social/v1
  baseurl_source: declared
  description: What goes out, where, and when.
  name: deploy.social Posts API
  slug: deploy-social-posts-api
artifact_total: 20
common:
- group: agent
  href: https://artifacts.apis.io/deploy-social/agentic-access/deploy-social-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/deploy-social-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/deploy-social/rate-limits/deploy-social-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/deploy-social-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/deploy-social/plans/deploy-social-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/deploy-social-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/deploy-social/rules/deploy-social-rules.yml
  title: ''
  type: Spectral
  url: rules/deploy-social-rules.yml
- group: design
  href: https://artifacts.apis.io/deploy-social/json-ld/deploy-social-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/deploy-social-context.jsonld
- group: design
  href: https://artifacts.apis.io/deploy-social/vocabulary/deploy-social-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/deploy-social-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/deploy-social/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/deploy-social/data-model/deploy-social-data-model.yml
  title: ''
  type: DataModel
  url: data-model/deploy-social-data-model.yml
- group: operate
  href: https://artifacts.apis.io/deploy-social/changelog/deploy-social-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/deploy-social-changelog.yml
- group: design
  href: https://artifacts.apis.io/deploy-social/conventions/deploy-social-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/deploy-social-conventions.yml
- group: design
  href: https://artifacts.apis.io/deploy-social/conventions/deploy-social-conventions.yml
  title: ''
  type: Conventions
  url: conventions/deploy-social-conventions.yml
- group: design
  href: https://artifacts.apis.io/deploy-social/lifecycle/deploy-social-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/deploy-social-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/deploy-social/errors/deploy-social-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/deploy-social-error-codes.yml
- group: design
  href: https://artifacts.apis.io/deploy-social/errors/deploy-social-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/deploy-social-problem-types.yml
- group: design
  href: https://artifacts.apis.io/deploy-social/conformance/deploy-social-conformance.yml
  title: ''
  type: Conformance
  url: conformance/deploy-social-conformance.yml
- group: other
  href: https://artifacts.apis.io/deploy-social/overlays/deploy-social-mcp-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/deploy-social-mcp-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/deploy-social/llms/deploy-social-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/deploy-social-llms.txt
- group: build
  href: https://artifacts.apis.io/deploy-social/mcp/deploy-social-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/deploy-social-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/deploy-social/mcp/deploy-social-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/deploy-social-mcp.yml
- group: agent
  href: https://artifacts.apis.io/deploy-social/well-known/deploy-social-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/deploy-social-well-known.yml
- group: other
  href: https://artifacts.apis.io/deploy-social/hosts/deploy-social-hosts.yml
  title: ''
  type: Hosts
  url: hosts/deploy-social-hosts.yml
- group: build
  href: https://artifacts.apis.io/deploy-social/integrations/deploy-social-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/deploy-social-integration-edges.yml
- group: auth
  href: https://artifacts.apis.io/deploy-social/authentication/deploy-social-authentication.yml
  title: ''
  type: Authentication
  url: authentication/deploy-social-authentication.yml
- group: auth
  href: https://artifacts.apis.io/deploy-social/security/deploy-social-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/deploy-social-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://deploy.social/
- group: docs
  title: ''
  type: Documentation
  url: https://deploy.social/docs
- group: docs
  title: ''
  type: APIReference
  url: https://deploy.social/docs/api/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://deploy.social/docs/guides/welcome
- group: start
  title: ''
  type: Quickstart
  url: https://deploy.social/docs/api
- group: operate
  title: ''
  type: ChangeLog
  url: https://deploy.social/changelog
- group: commercial
  title: ''
  type: Pricing
  url: https://deploy.social/pricing
- group: start
  title: ''
  type: SignUp
  url: https://deploy.social/app
- group: start
  title: ''
  type: Login
  url: https://deploy.social/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://deploy.social/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://deploy.social/privacy
- group: agent
  title: ''
  type: LLMsTxt
  url: https://deploy.social/llms.txt
- group: operate
  title: ''
  type: Support
  url: mailto:hello@deploy.social
created: '2026-11-05'
description: 'deploy.social, operated by Deploy Social LLC of Bozeman, Montana, is a cross-posting service for short-form video: upload one video and it publishes to YouTube Shorts, Instagram Reels, TikTok, Facebook Reels, Threads, X and Bluesky at once, with photo and text posts, scheduling, batches, a media library, team workspaces and client approval. On its Standard and Studio plans it offers a REST API (https://api.deploy.social/v1, workspace API key as bearer token) and a remote MCP server that let your own code or an AI assistant upload media, create drafts and publish to connected accounts. A free plan covers five posts a month.'
image: https://deploy.social/opengraph-image.png?bb7c5600f2ef16bf
json_schemas:
- name: CreatePost
  property_count: 12
  slug: deploy-social-create-post
- name: Destination
  property_count: 8
  slug: deploy-social-destination
- name: Me
  property_count: 5
  slug: deploy-social-me
- name: Media
  property_count: 14
  slug: deploy-social-media
- name: Post
  property_count: 19
  slug: deploy-social-post
- name: UpdatePost
  property_count: 10
  slug: deploy-social-update-post
jsonld:
- class_count: 26
  name: Deploy Social Context
  property_count: 76
  slug: deploy-social-context
layout: provider
mcp_servers:
- description: 'deploy.social''s own hosted MCP server. It lets an assistant work in one Deploy workspace: list connected social accounts, bring in a video or photos, save a draft, publish it once the person agrees, a'
  name: deploy.social MCP server
  slug: deploy-social-mcp-server
modified: '2026-11-05'
name: deploy.social
nav: Providers
network: true
overview: 'deploy.social publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Destinations API, Media API, and 1 more. Tagged areas include Company, Social Media, Video, Short-Form Video, and Cross-Posting.


  The deploy.social catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  deploy.social''s developer surface includes changelog, authentication, documentation, API reference, getting-started guide, quickstart, pricing, and 30 more developer resources.'
plans:
- name: Deploy Social Plans Pricing
  plan_count: 3
  slug: deploy-social-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 7
  name: Deploy Social Rate Limits
  slug: deploy-social-rate-limits
rules:
- authorship: generated
  effective_rule_count: 105
  extends:
  - spectral:oas
  name: deploy.social API Rules
  rule_count: 64
  severity_counts:
    error: 58
    hint: 0
    info: 3
    warn: 3
  slug: deploy-social-rules
score:
  band: strong
  composite: 60.3
  coverage:
    artifact_dirs: 27
    catalog_earned: 86.8
    catalog_earned_first_party: 24.0
    catalog_gap: 28.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 35.6
    contract_quality: 66.4
    developer_ergonomics: 47.0
    discoverability: 71.7
    operational_transparency: 47.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Deploy Social Authentication
  slug: deploy-social-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Deploy Social Domain Security
  slug: deploy-social-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: deploy-social-manage-scheduled-posts
  slug: deploy-social-manage-scheduled-posts
- name: deploy-social-post-a-video
  slug: deploy-social-post-a-video
slug: deploy-social
tags:
- Company
- Social Media
- Video
- Short-Form Video
- Cross-Posting
- Scheduling
- Content Publishing
- MCP
website: https://deploy.social/
---
