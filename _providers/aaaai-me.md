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
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: true
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 44.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 63
  human_in_the_loop: 3
  name: Aaaai Me Agentic Access
  operation_count: 102
  slug: aaaai-me-agentic-access
  summary_line: 102 operations · 63 acting · 3 human-in-the-loop
api_count: 1
apis:
- description: The provider-documented purchase surface for autonomous agents, described in https://aaaai.me/pay.md and machine-readably in https://aaaai.me/.well-known/agent-payments.json but absent from the Swagge
  name: AAA AI Agent Checkout (Billing) API
  slug: aaaai-agent-checkout-api
- baseURL: https://web.aaaai.me
  baseurl_source: declared
  description: The Agents API from AAA AI — 3 operation(s) for agents.
  name: AAA AI Agents API
  slug: aaaai-me-agents-api
- baseURL: https://web.aaaai.me
  baseurl_source: declared
  description: The Approvals API from AAA AI — 3 operation(s) for approvals.
  name: AAA AI Approvals API
  slug: aaaai-me-approvals-api
- baseURL: https://web.aaaai.me
  baseurl_source: declared
  description: Authentication
  name: AAA AI Auth API
  slug: aaaai-me-auth-api
- baseURL: https://web.aaaai.me
  baseurl_source: declared
  description: Chat and queries
  name: AAA AI Chat API
  slug: aaaai-me-chat-api
- baseURL: https://web.aaaai.me
  baseurl_source: declared
  description: Code-only generation (Cursor / CLI / IDE)
  name: AAA AI Code API
  slug: aaaai-me-code-api
- baseURL: https://web.aaaai.me
  baseurl_source: declared
  description: Cognitive scaling status and control
  name: AAA AI Cognitive Scaling API
  slug: aaaai-me-cognitive-scaling-api
- baseURL: https://web.aaaai.me
  baseurl_source: declared
  description: The Cron API from AAA AI — 3 operation(s) for cron.
  name: AAA AI Cron API
  slug: aaaai-me-cron-api
- baseURL: https://web.aaaai.me
  baseurl_source: declared
  description: Debug and development
  name: AAA AI Debug API
  slug: aaaai-me-debug-api
- baseURL: https://web.aaaai.me
  baseurl_source: declared
  description: The Deep Agent API from AAA AI — 3 operation(s) for deep agent.
  name: AAA AI Deep Agent API
  slug: aaaai-me-deep-agent-api
- baseURL: https://web.aaaai.me
  baseurl_source: declared
  description: Dynamic expert creation and management
  name: AAA AI Dynamic Experts API
  slug: aaaai-me-dynamic-experts-api
- baseURL: https://web.aaaai.me
  baseurl_source: declared
  description: Expert system management
  name: AAA AI Experts API
  slug: aaaai-me-experts-api
- baseURL: https://web.aaaai.me
  baseurl_source: declared
  description: Health and status
  name: AAA AI Health API
  slug: aaaai-me-health-api
- baseURL: https://web.aaaai.me
  baseurl_source: declared
  description: The Nodes API from AAA AI — 2 operation(s) for nodes.
  name: AAA AI Nodes API
  slug: aaaai-me-nodes-api
- baseURL: https://web.aaaai.me
  baseurl_source: declared
  description: Platform and expert settings
  name: AAA AI Settings API
  slug: aaaai-me-settings-api
- baseURL: https://web.aaaai.me
  baseurl_source: declared
  description: Current user and avatar
  name: AAA AI User API
  slug: aaaai-me-user-api
- baseURL: https://web.aaaai.me
  baseurl_source: declared
  description: Video sessions
  name: AAA AI Video API
  slug: aaaai-me-video-api
artifact_total: 30
common:
- group: other
  href: https://artifacts.apis.io/aaaai-me/capabilities/aaaai-me-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/aaaai-me-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/aaaai-me/overlays/aaaai-me-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/aaaai-me-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/aaaai-me/agentic-access/aaaai-me-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/aaaai-me-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://aaaai.me/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://web.aaaai.me/
- group: docs
  title: ''
  type: Documentation
  url: https://aaaai.me/docs.html
- group: docs
  title: ''
  type: APIReference
  url: https://web.aaaai.me/apidocs
- group: start
  title: ''
  type: GettingStarted
  url: https://aaaai.me/auth.md
- group: start
  title: ''
  type: Login
  url: https://web.aaaai.me/
- group: start
  title: ''
  type: SignUp
  url: https://aaaai.me/register.html
- group: commercial
  title: ''
  type: Pricing
  url: https://aaaai.me/pay/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aaaai.me/terms-and-conditions.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aaaai.me/privacy.html
- group: operate
  title: ''
  type: Support
  url: mailto:support@aaaai.me
- group: company
  title: ''
  type: Blog
  url: https://aaaai.me/blog.html
- group: company
  title: ''
  type: BlogRSS
  url: https://aaaai.me/blog/feed.xml
- group: company
  title: ''
  type: Newsroom
  url: https://aaaai.me/news.html
- group: other
  title: ''
  type: Downloads
  url: https://aaaai.me/downloads.html
- group: agent
  href: https://artifacts.apis.io/aaaai-me/llms/aaaai-me-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aaaai-me-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://aaaai.me/llms.txt
- group: agent
  href: https://artifacts.apis.io/aaaai-me/well-known/aaaai-me-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aaaai-me-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: https://aaaai.me/.well-known/api-catalog
- group: auth
  href: https://artifacts.apis.io/aaaai-me/authentication/aaaai-me-authentication.yml
  title: ''
  type: Authentication
  url: authentication/aaaai-me-authentication.yml
- group: auth
  href: https://artifacts.apis.io/aaaai-me/scopes/aaaai-me-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/aaaai-me-scopes.yml
- group: design
  href: https://artifacts.apis.io/aaaai-me/conventions/aaaai-me-conventions.yml
  title: ''
  type: Conventions
  url: conventions/aaaai-me-conventions.yml
- group: design
  href: https://artifacts.apis.io/aaaai-me/errors/aaaai-me-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/aaaai-me-problem-types.yml
- group: design
  href: https://artifacts.apis.io/aaaai-me/lifecycle/aaaai-me-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/aaaai-me-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/aaaai-me/changelog/aaaai-me-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/aaaai-me-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://aaaai.me/news/feed.xml
- group: design
  href: https://artifacts.apis.io/aaaai-me/conformance/aaaai-me-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aaaai-me-conformance.yml
- group: commercial
  href: https://artifacts.apis.io/aaaai-me/plans/aaaai-me-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aaaai-me-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/aaaai-me/rate-limits/aaaai-me-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/aaaai-me-rate-limits.yml
- group: build
  href: https://artifacts.apis.io/aaaai-me/packages/aaaai-me-packages.yml
  title: ''
  type: Packages
  url: packages/aaaai-me-packages.yml
- group: build
  href: https://artifacts.apis.io/aaaai-me/cli/aaaai-me-cli.yml
  title: ''
  type: CLI
  url: cli/aaaai-me-cli.yml
- group: design
  href: https://artifacts.apis.io/aaaai-me/data-model/aaaai-me-data-model.yml
  title: ''
  type: DataModel
  url: data-model/aaaai-me-data-model.yml
- group: agent
  href: https://artifacts.apis.io/aaaai-me/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/aaaai-me/security/aaaai-me-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aaaai-me-domain-security.yml
- group: other
  title: ''
  type: DataSubjectRequest
  url: https://aaaai.me/privacy.html
- group: other
  title: ''
  type: AITransparency
  url: https://web.aaaai.me/meet
- group: other
  title: ''
  type: ExitAssistance
  url: https://aaaai.me/docs.html
- group: other
  href: https://artifacts.apis.io/aaaai-me/regulatory/aaaai-me-regulatory-posture.yml
  title: ''
  type: RegulatoryPosture
  url: regulatory/aaaai-me-regulatory-posture.yml
created: '2026-09-19'
description: 'AAA AI (Autonomous Agents Automations; product spelling AAAAI) is a Montenegro-based multi-agent AI platform operated by Kirill Pokidov: a workspace at web.aaaai.me that routes questions through a panel of expert models with debate and verification modes, runs visual workflows with human-approval nodes across a catalog of integrations, pairs desktop "agents" on a user''s own machines, and adds Meet — voice and video calls with live AI notes. Sold as a $20/month Pro cloud plan (card, crypto or SBP) or self-hosted. The API is a 102-operation Swagger 2.0 contract on web.aaaai.me (chat, streaming queries, an OpenAI-compatible /v1/chat/completions, approvals, cron jobs, goal jobs, experts, settings) authenticated by an X-User-Login header, plus a documented crypto checkout API that lets an agent buy the subscription autonomously. The static site aaaai.me publishes an unusually complete agent-discovery layer — RFC 9727 api-catalog, OAuth/OIDC/RFC 9728 metadata, ai-plugin.json, an
  MCP server card, an agentskills.io index, agent-payments.json, llms.txt and the full ai-visibility.org.uk file set — several of whose targets (the named OpenAPI URL, the MCP endpoint, the JWKS) do not exist.'
finops:
- has_sources: true
  method: derived
  name: Aaaai Me Finops
  primary_unit: user
  service_category: ''
  slug: aaaai-me-finops
  template: false
image: https://aaaai.me/og-image.png
layout: provider
modified: '2026-09-19'
name: AAA AI
nav: Providers
network: true
overview: 'AAA AI publishes 17 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agents API, Approvals API, Auth API, and 14 more. Tagged areas include Artificial Intelligence, Agents, Multi-Agent, LLM Orchestration, and Meetings.


  The AAA AI catalog on APIs.io includes 1 Spectral governance ruleset.


  AAA AI''s developer surface includes documentation, API reference, getting-started guide, signup flow, pricing, support, engineering blog, and 34 more developer resources.'
plans:
- name: Aaaai Me Plans Pricing
  plan_count: 4
  slug: aaaai-me-plans-pricing
- name: Aaaai Me Price Estimates
  plan_count: 0
  slug: aaaai-me-price-estimates
random_paper: 4
rate_limits:
- limit_count: 0
  name: Aaaai Me Rate Limits
  slug: aaaai-me-rate-limits
rules:
- authorship: generated
  effective_rule_count: 82
  extends:
  - spectral:oas
  name: AAA AI API Rules
  rule_count: 41
  severity_counts:
    error: 37
    hint: 0
    info: 2
    warn: 2
  slug: aaaai-me-rules
scopes:
- name: Aaaai Me Scopes
  scope_count: 5
  slug: aaaai-me-scopes
  summary_line: 5 scopes · authorizationCode/refreshToken/password
score:
  band: developing
  composite: 50.5
  coverage:
    artifact_dirs: 31
    catalog_earned: 56.5
    catalog_earned_first_party: 12.0
    catalog_gap: 58.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.9
  facets:
    access_clarity: 61.8
    contract_governance: 31.8
    contract_quality: 42.0
    developer_ergonomics: 51.8
    discoverability: 84.8
    operational_transparency: 15.8
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - montenegro
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 58.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 16
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 39.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/aaaai-me/aaaai-me-2026-10-11T092338.png
security:
- kind: authentication
  name: Aaaai Me Authentication
  slug: aaaai-me-authentication
  summary_line: apiKey/cookie · 4 schemes
- kind: domain-security
  name: Aaaai Me Domain Security
  slug: aaaai-me-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 4
skills:
- name: aaaai-me-approvals-loop
  slug: aaaai-me-approvals-loop
- name: aaaai-me-ask-and-stream
  slug: aaaai-me-ask-and-stream
- name: aaaai-me-buy-pro-as-agent
  slug: aaaai-me-buy-pro-as-agent
- name: aaaai-me-schedule-and-goals
  slug: aaaai-me-schedule-and-goals
slug: aaaai-me
tags:
- Artificial Intelligence
- Agents
- Multi-Agent
- LLM Orchestration
- Meetings
- Voice
- Video
- Workflows
- MCP
- Agentic Commerce
- OpenAI-Compatible
- Self-Hosted
- Agent-Native
- Montenegro
website: https://aaaai.me/
---
