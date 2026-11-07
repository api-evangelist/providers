---
access_model:
  confidence: medium
  label: Published pricing, account required
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://www.karumi.ai/pricing
  - https://www.karumi.ai/mcp-documentation
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
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 52.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Karumi Agentic Access
  operation_count: 9
  slug: karumi-agentic-access
  summary_line: 9 operations
api_count: 1
apis:
- description: Hosted, remote MCP server that exposes a Karumi workspace to any MCP-compatible client. 37 published tools cover organizations, agents, sessions, transcripts (keyword and semantic search), leads, comp
  name: Karumi MCP Server
  slug: karumi-mcp-server
- baseURL: https://api.karumi.ai/api/v1
  baseurl_source: declared
  description: The Analytics API from Karumi — 2 operation(s) for analytics.
  name: Karumi Analytics API
  slug: karumi-analytics-api
- baseURL: https://api.karumi.ai/api/v1
  baseurl_source: declared
  description: The Sessions API from Karumi — 5 operation(s) for sessions.
  name: Karumi Sessions API
  slug: karumi-sessions-api
- baseURL: https://api.karumi.ai/api/v1
  baseurl_source: declared
  description: The Targets API from Karumi — 2 operation(s) for targets.
  name: Karumi Targets API
  slug: karumi-targets-api
- baseURL: https://api.karumi.ai/mcp/
  baseurl_source: declared
  description: The Chat onboarding API from Karumi — 2 operation(s) for chat onboarding.
  name: Karumi Chat onboarding API
  slug: karumi-chat-onboarding-api
artifact_total: 20
common:
- group: agent
  href: https://artifacts.apis.io/karumi/agentic-access/karumi-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/karumi-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://www.karumi.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://api.karumi.ai/api/v1/docs
- group: docs
  title: ''
  type: APIReference
  url: https://api.karumi.ai/api/v1/redoc
- group: agent
  href: https://artifacts.apis.io/karumi/mcp/karumi-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/karumi-mcp.yml
- group: build
  href: https://artifacts.apis.io/karumi/mcp/karumi-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/karumi-tool-crosswalk.yml
- group: docs
  href: https://artifacts.apis.io/karumi/openapi/_original/karumi-public-api-openapi.json
  title: ''
  type: OpenAPI
  url: openapi/_original/karumi-public-api-openapi.json
- group: other
  href: https://artifacts.apis.io/karumi/overlays/karumi-public-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/karumi-public-api-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/karumi/authentication/karumi-authentication.yml
  title: ''
  type: Authentication
  url: authentication/karumi-authentication.yml
- group: auth
  href: https://artifacts.apis.io/karumi/scopes/karumi-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/karumi-scopes.yml
- group: design
  href: https://artifacts.apis.io/karumi/conventions/karumi-conventions.yml
  title: ''
  type: Conventions
  url: conventions/karumi-conventions.yml
- group: design
  href: https://artifacts.apis.io/karumi/data-model/karumi-data-model.yml
  title: ''
  type: DataModel
  url: data-model/karumi-data-model.yml
- group: design
  href: https://artifacts.apis.io/karumi/errors/karumi-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/karumi-problem-types.yml
- group: design
  href: https://artifacts.apis.io/karumi/lifecycle/karumi-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/karumi-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/karumi/conformance/karumi-conformance.yml
  title: ''
  type: Conformance
  url: conformance/karumi-conformance.yml
- group: agent
  href: https://artifacts.apis.io/karumi/well-known/karumi-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/karumi-well-known.yml
- group: agent
  href: https://artifacts.apis.io/karumi/llms/karumi-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/karumi-llms.txt
- group: agent
  href: https://artifacts.apis.io/karumi/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/karumi/components/karumi-components.yml
  title: ''
  type: Components
  url: components/karumi-components.yml
- group: build
  href: https://artifacts.apis.io/karumi/packages/karumi-packages.yml
  title: ''
  type: Packages
  url: packages/karumi-packages.yml
- group: commercial
  href: https://artifacts.apis.io/karumi/plans/karumi-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/karumi-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/karumi/rate-limits/karumi-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/karumi-rate-limits.yml
- group: company
  title: ''
  type: Blog
  url: https://www.karumi.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.karumi.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.karumi.ai/
- group: start
  title: ''
  type: Login
  url: https://app.karumi.ai/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.karumi.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.karumi.ai/privacy
- group: auth
  href: https://artifacts.apis.io/karumi/security/karumi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/karumi-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/karumi/security/karumi-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/karumi-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.delve.co/karumi
created: '2026-07-17'
description: Karumi is an agentic demo platform that delivers personalized, AI-powered product demonstrations during live video calls. Its AI agent runs live, interactive demos 24/7 across landing pages, in-app surfaces, and outbound email, adapting each demonstration to the prospect and navigating the product in-browser in real time. It supports multiple languages, logs transcripts, analysis, and next steps into the CRM, and targets B2B SaaS go-to-market teams looking to engage high-intent leads at peak interest instead of waiting days for a human demo. Karumi publishes a read-only Public API over session, transcript, insight, target and analytics data (OpenAPI 3.1.0, X-Api-Key auth) and a hosted, OAuth-protected MCP server exposing 37 tools for operating the platform from an MCP client. Karumi is a Y Combinator (Fall 2025) company founded by Pablo Omenaca (CEO) and Toni Lopez (CTO), both formerly of StackAI (YC W23).
finops:
- has_sources: true
  method: derived
  name: Karumi Finops
  primary_unit: ''
  service_category: ''
  slug: karumi-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/karumi.png
layout: provider
mcp_servers:
- description: Remote MCP server at api.karumi.ai over HTTP requiring OAuth; 38 tools listed.
  name: Karumi MCP Server
  slug: karumi
modified: '2026-09-16'
name: Karumi
nav: Providers
network: true
overview: 'Karumi publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Analytics API, Sessions API, Targets API, and 2 more. Tagged areas include Company, AI Agents, Product Demos, Sales Enablement, and Go-To-Market.


  The Karumi catalog on APIs.io includes 1 Spectral governance ruleset.


  Karumi''s developer surface includes documentation, API reference, authentication, engineering blog, pricing, signup flow, and 25 more developer resources.'
plans:
- name: Karumi Plans Pricing
  plan_count: 2
  slug: karumi-plans-pricing
- name: Karumi Price Estimates
  plan_count: 0
  slug: karumi-price-estimates
random_paper: 1
rate_limits:
- limit_count: 0
  name: Karumi Rate Limits
  slug: karumi-rate-limits
rules:
- authorship: generated
  effective_rule_count: 87
  extends:
  - spectral:oas
  name: Karumi API Rules
  rule_count: 46
  severity_counts:
    error: 43
    hint: 0
    info: 1
    warn: 2
  slug: karumi-rules
scopes:
- name: Karumi Scopes
  scope_count: 5
  slug: karumi-scopes
  summary_line: 5 scopes · authorizationCode
score:
  band: developing
  composite: 44.8
  coverage:
    artifact_dirs: 28
    catalog_earned: 49.5
    catalog_earned_first_party: 8.0
    catalog_gap: 65.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.7
  facets:
    access_clarity: 77.6
    contract_governance: 18.2
    contract_quality: 46.2
    developer_ergonomics: 32.7
    discoverability: 68.3
    operational_transparency: 0.0
  previous_composite: 44.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 57.1
      total: 7
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 36.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/karumi/karumi-2026-07-25T223528.png
security:
- kind: authentication
  name: Karumi Authentication
  slug: karumi-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Karumi Domain Security
  slug: karumi-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Karumi Trust Center
  slug: karumi-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
skill_count: 4
skills:
- name: Pull session insights, events and recordings
  slug: karumi-analyze-session-outcomes
- name: Operate a Karumi workspace over MCP
  slug: karumi-operate-workspace-over-mcp
- name: Report demo engagement analytics by target
  slug: karumi-report-demo-analytics
- name: Review demo sessions and read a transcript
  slug: karumi-review-demo-sessions
slug: karumi
tags:
- Company
- AI Agents
- Product Demos
- Sales Enablement
- Go-To-Market
- Software-as-a-Service
- Conversational AI
- Video
- Y Combinator
- MCP
- Agent-Native
- Analytics
- Conversation Intelligence
website: https://www.karumi.ai/
---
