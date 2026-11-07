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
  band: agent-ready
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
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 60
  human_in_the_loop: 6
  name: Lumify Ai Agentic Access
  operation_count: 181
  slug: lumify-ai-agentic-access
  summary_line: 181 operations · 60 acting · 6 human-in-the-loop
api_count: 1
apis:
- baseURL: https://lumify.ai
  baseurl_source: declared
  description: The admin API from lumify-ai — 57 operation(s) for admin.
  name: lumify-ai Admin API
  slug: lumify-ai-admin-api
- baseURL: https://lumify.ai
  baseurl_source: declared
  description: 'Programmatic onboarding: key provisioning and credit balance.'
  name: lumify-ai Agent API
  slug: lumify-ai-agent-api
- baseURL: https://lumify.ai
  baseurl_source: declared
  description: The app API from lumify-ai — 22 operation(s) for app.
  name: lumify-ai App API
  slug: lumify-ai-app-api
- baseURL: https://lumify.ai
  baseurl_source: declared
  description: The auth API from lumify-ai — 7 operation(s) for auth.
  name: lumify-ai Auth API
  slug: lumify-ai-auth-api
- baseURL: https://lumify.ai
  baseurl_source: declared
  description: Schedules, live scores, odds, splits, and bet intelligence.
  name: lumify-ai Events API
  slug: lumify-ai-events-api
- baseURL: https://lumify.ai
  baseurl_source: declared
  description: The grade API from lumify-ai — 1 operation(s) for grade.
  name: lumify-ai Grade API
  slug: lumify-ai-grade-api
- baseURL: https://lumify.ai
  baseurl_source: declared
  description: Service health checks.
  name: lumify-ai Health API
  slug: lumify-ai-health-api
- baseURL: https://lumify.ai
  baseurl_source: declared
  description: Model Context Protocol server endpoint for AI agents.
  name: lumify-ai MCP API
  slug: lumify-ai-mcp-api
- baseURL: https://lumify.ai
  baseurl_source: declared
  description: The oauth API from lumify-ai — 2 operation(s) for oauth.
  name: lumify-ai OAuth API
  slug: lumify-ai-oauth-api
- baseURL: https://lumify.ai
  baseurl_source: declared
  description: Player profiles and participation history.
  name: lumify-ai Players API
  slug: lumify-ai-players-api
- baseURL: https://lumify.ai
  baseurl_source: declared
  description: The public API from lumify-ai — 42 operation(s) for public.
  name: lumify-ai Public API
  slug: lumify-ai-public-api
- baseURL: https://lumify.ai
  baseurl_source: declared
  description: The resolve API from lumify-ai — 3 operation(s) for resolve.
  name: lumify-ai Resolve API
  slug: lumify-ai-resolve-api
- baseURL: https://lumify.ai
  baseurl_source: declared
  description: Supported sports, leagues, and season calendars.
  name: lumify-ai Sports API
  slug: lumify-ai-sports-api
- baseURL: https://lumify.ai
  baseurl_source: declared
  description: First-class team resources.
  name: lumify-ai Teams API
  slug: lumify-ai-teams-api
- baseURL: https://lumify.ai
  baseurl_source: declared
  description: The trial API from lumify-ai — 1 operation(s) for trial.
  name: lumify-ai Trial API
  slug: lumify-ai-trial-api
- baseURL: https://lumify.ai
  baseurl_source: declared
  description: The webhooks API from lumify-ai — 2 operation(s) for webhooks.
  name: lumify-ai Webhooks API
  slug: lumify-ai-webhooks-api
artifact_total: 35
common:
- group: agent
  href: https://artifacts.apis.io/lumify-ai/agentic-access/lumify-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/lumify-ai-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/lumify-ai/rate-limits/lumify-ai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/lumify-ai-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/lumify-ai/plans/lumify-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/lumify-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/lumify-ai/rules/lumify-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/lumify-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/lumify-ai/json-ld/lumify-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/lumify-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/lumify-ai/vocabulary/lumify-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/lumify-ai-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/lumify-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/lumify-ai/data-model/lumify-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/lumify-ai-data-model.yml
- group: design
  href: https://artifacts.apis.io/lumify-ai/conventions/lumify-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/lumify-ai-conventions.yml
- group: auth
  title: ''
  type: Security
  url: https://lumify.ai/terms-of-service
- group: design
  href: https://artifacts.apis.io/lumify-ai/errors/lumify-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/lumify-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/lumify-ai/conformance/lumify-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/lumify-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/lumify-ai/llms/lumify-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/lumify-ai-llms.txt
- group: build
  href: https://artifacts.apis.io/lumify-ai/mcp/lumify-ai-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/lumify-ai-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/lumify-ai/mcp/lumify-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/lumify-ai-mcp.yml
- group: auth
  href: https://artifacts.apis.io/lumify-ai/well-known/lumify-ai-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/lumify-ai-security.txt
- group: agent
  href: https://artifacts.apis.io/lumify-ai/well-known/lumify-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/lumify-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/lumify-ai/hosts/lumify-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/lumify-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/lumify-ai/vendors/lumify-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/lumify-ai-vendors.yml
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@lumifyai/sdk
- group: start
  title: ''
  type: Login
  url: https://lumify.ai/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/lumifyai
- group: operate
  title: ''
  type: ChangeLog
  url: https://lumify.ai/changelog
- group: auth
  href: https://artifacts.apis.io/lumify-ai/authentication/lumify-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/lumify-ai-authentication.yml
- group: auth
  href: https://artifacts.apis.io/lumify-ai/security/lumify-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/lumify-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/lumify-ai/security/lumify-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/lumify-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://lumify.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://lumify.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://lumify.ai/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://lumify.ai/docs/getting-started/quick-start
- group: commercial
  title: ''
  type: Pricing
  url: https://lumify.ai/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://lumify.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://lumify.ai/privacy-policy
created: '2026-10-30'
description: Lumify AI provides a real-time sports intelligence API designed for autonomous AI agents. It delivers live scores, schedules, multi‑book odds, and explainable betting intelligence across major leagues such as NFL, NBA, MLB, NHL, and more. The platform offers REST and MCP endpoints, free credits for developers, and tools for seamless integration into autonomous decision‑making systems.
image: https://lumify.ai/assets/images/og/lumify-og.jpg
json_schemas:
- name: GradeSlipRequest
  property_count: 4
  slug: lumify-ai-grade-slip-request
- name: IntelligenceResponse
  property_count: 13
  slug: lumify-ai-intelligence-response
- name: OddsResponse
  property_count: 6
  slug: lumify-ai-odds-response
- name: Player
  property_count: 18
  slug: lumify-ai-player
- name: ResolveEventResponse
  property_count: 15
  slug: lumify-ai-resolve-event-response
- name: ResolveTeamResponse
  property_count: 13
  slug: lumify-ai-resolve-team-response
jsonld:
- class_count: 120
  name: Lumify Ai Context
  property_count: 365
  slug: lumify-ai-context
layout: provider
mcp_servers:
- description: Remote MCP server at lumify.ai requiring an API key.
  name: lumify-ai MCP Server
  slug: lumify-ai-mcp-yml
modified: '2026-10-30'
name: lumify-ai
nav: Providers
network: true
overview: 'lumify-ai publishes 16 API contracts indexed on the [APIs.io](https://apis.io/) network, including Admin API, Agent API, App API, and 13 more. Tagged areas include Company, Sports, Artificial Intelligence, Real-Time, and Betting.


  The lumify-ai catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  lumify-ai''s developer surface includes changelog, authentication, documentation, API reference, getting-started guide, pricing, and 27 more developer resources.'
plans:
- name: Lumify Ai Plans Pricing
  plan_count: 4
  slug: lumify-ai-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 5
  name: Lumify Ai Rate Limits
  slug: lumify-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: lumify-ai API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: lumify-ai-rules
score:
  band: developing
  composite: 49.9
  coverage:
    artifact_dirs: 25
    catalog_earned: 86.8
    catalog_earned_first_party: 24.0
    catalog_gap: 28.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.0
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 61.7
    developer_ergonomics: 35.1
    discoverability: 65.0
    operational_transparency: 47.4
  previous_composite: 59.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 16
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
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/lumify-ai/lumify-ai-2026-11-03T135135.png
security:
- kind: authentication
  name: Lumify Ai Authentication
  slug: lumify-ai-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Lumify Ai Domain Security
  slug: lumify-ai-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Lumify Ai Vulnerability Disclosure
  slug: lumify-ai-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 4
skills:
- name: lumify-ai-auth-login-flow
  slug: lumify-ai-auth-login-flow
- name: lumify-ai-browse-docs
  slug: lumify-ai-browse-docs
- name: lumify-ai-fetch-event-details
  slug: lumify-ai-fetch-event-details
- name: lumify-ai-update-account-settings
  slug: lumify-ai-update-account-settings
slug: lumify-ai
tags:
- Company
- Sports
- Artificial Intelligence
- Real-Time
- Betting
website: https://lumify.ai/
---
