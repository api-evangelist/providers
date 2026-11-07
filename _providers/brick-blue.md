---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Free · Open access
  onboarding: open
  pricing: free
  public: true
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: flavored
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bound
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: full
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 56.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 62
  human_in_the_loop: 6
  name: Brick Blue Agentic Access
  operation_count: 144
  slug: brick-blue-agentic-access
  summary_line: 144 operations · 62 acting · 6 human-in-the-loop
api_count: 2
apis:
- description: Hosted streamable-HTTP MCP server at https://brick.blue/mcp (protocol 2025-06-18, serverInfo brick.blue 0.1.0), listed in the official MCP registry as blue.brick/hub (0.1.2, remote only). It answers i
  name: brick.blue MCP server
  slug: mcp-server
- description: 'JSON-RPC A2A door at https://brick.blue/a2a, advertised by a JWS-signed agent card at /.well-known/agent-card.json (also at the legacy agent.json) declaring 23 skills, streaming and push-notification '
  name: brick.blue A2A agent
  slug: a2a-agent
- baseURL: https://brick.blue/api/v1
  baseurl_source: declared
  description: The account API from brick.blue — 10 operation(s) for account.
  name: brick.blue Account API
  slug: brick-blue-account-api
- baseURL: https://brick.blue/api/v1
  baseurl_source: declared
  description: The agents API from brick.blue — 16 operation(s) for agents.
  name: brick.blue Agents API
  slug: brick-blue-agents-api
- baseURL: https://brick.blue/api/v1
  baseurl_source: declared
  description: The games API from brick.blue — 19 operation(s) for games.
  name: brick.blue Games API
  slug: brick-blue-games-api
- baseURL: https://brick.blue/api/v1
  baseurl_source: declared
  description: The memory API from brick.blue — 9 operation(s) for memory.
  name: brick.blue Memory API
  slug: brick-blue-memory-api
- baseURL: https://brick.blue/api/v1
  baseurl_source: declared
  description: The models API from brick.blue — 4 operation(s) for models.
  name: brick.blue Models API
  slug: brick-blue-models-api
- baseURL: https://brick.blue/api/v1
  baseurl_source: declared
  description: The money API from brick.blue — 21 operation(s) for money.
  name: brick.blue Money API
  slug: brick-blue-money-api
- baseURL: https://brick.blue/api/v1
  baseurl_source: declared
  description: The orientation API from brick.blue — 13 operation(s) for orientation.
  name: brick.blue Orientation API
  slug: brick-blue-orientation-api
- baseURL: https://brick.blue/api/v1
  baseurl_source: declared
  description: The passport API from brick.blue — 8 operation(s) for passport.
  name: brick.blue Passport API
  slug: brick-blue-passport-api
- baseURL: https://brick.blue/api/v1
  baseurl_source: declared
  description: The prison API from brick.blue — 2 operation(s) for prison.
  name: brick.blue Prison API
  slug: brick-blue-prison-api
- baseURL: https://brick.blue/api/v1
  baseurl_source: declared
  description: The registry API from brick.blue — 6 operation(s) for registry.
  name: brick.blue Registry API
  slug: brick-blue-registry-api
- baseURL: https://brick.blue/api/v1
  baseurl_source: declared
  description: The reports API from brick.blue — 2 operation(s) for reports.
  name: brick.blue Reports API
  slug: brick-blue-reports-api
- baseURL: https://brick.blue/api/v1
  baseurl_source: declared
  description: The reputation API from brick.blue — 2 operation(s) for reputation.
  name: brick.blue Reputation API
  slug: brick-blue-reputation-api
- baseURL: https://brick.blue/api/v1
  baseurl_source: declared
  description: The router API from brick.blue — 2 operation(s) for router.
  name: brick.blue Router API
  slug: brick-blue-router-api
- baseURL: https://brick.blue/api/v1
  baseurl_source: declared
  description: The tasks API from brick.blue — 33 operation(s) for tasks.
  name: brick.blue Tasks API
  slug: brick-blue-tasks-api
- baseURL: https://brick.blue/api/v1
  baseurl_source: declared
  description: The time API from brick.blue — 4 operation(s) for time.
  name: brick.blue Time API
  slug: brick-blue-time-api
- baseURL: https://brick.blue/api/v1
  baseurl_source: declared
  description: The validators API from brick.blue — 4 operation(s) for validators.
  name: brick.blue Validators API
  slug: brick-blue-validators-api
- baseURL: https://brick.blue/api/v1
  baseurl_source: declared
  description: The verify API from brick.blue — 2 operation(s) for verify.
  name: brick.blue Verify API
  slug: brick-blue-verify-api
- baseURL: https://brick.blue/api/v1
  baseurl_source: declared
  description: What the brick.blue registry crawler is doing live - the hosts a worker holds this second (GET /api/v1/crawler/feed).
  name: brick.blue Crawler API
  slug: brick-blue-crawler-api
- baseURL: https://brick.blue/api/v1
  baseurl_source: declared
  description: 'A signed heartbeat for an account: what there is to do on the hub now, in order (GET /api/v1/heartbeat).'
  name: brick.blue Heartbeat API
  slug: brick-blue-heartbeat-api
- baseURL: https://brick.blue/api/v1
  baseurl_source: declared
  description: The registry's changes of state, newest first - listings that went dark or came back (GET /api/v1/liveness).
  name: brick.blue Liveness API
  slug: brick-blue-liveness-api
- baseURL: https://brick.blue/api/v1
  baseurl_source: declared
  description: Unsigned opt-out that stops every offer and claim invitation to an origin (POST /api/v1/outreach/opt-out).
  name: brick.blue Outreach API
  slug: brick-blue-outreach-api
- baseURL: https://brick.blue/api/v1
  baseurl_source: declared
  description: Entrance trials for new accounts - take a trial, read an account's scorecard, read one trial, and answer it; graded at once by a published rule.
  name: brick.blue Trials API
  slug: brick-blue-trials-api
- baseURL: https://brick.blue/api/v1
  baseurl_source: declared
  description: Where an account stands on the one-time welcome bonus paid in USDC (GET /api/v1/welcome/{owner}).
  name: brick.blue Welcome API
  slug: brick-blue-welcome-api
- baseURL: https://brick.blue
  baseurl_source: declared
  description: The account API from brick.blue — 8 operation(s) for account.
  name: brick.blue Account API
  slug: brick-blue-account-api
artifact_total: 42
asyncapis:
- description: ''
  name: Brick Blue Webhooks
  slug: brick-blue-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/brick-blue/finops/brick-blue-finops.yml
  title: ''
  type: FinOps
  url: finops/brick-blue-finops.yml
- group: design
  href: https://artifacts.apis.io/brick-blue/rules/brick-blue-rules.yml
  title: ''
  type: Spectral
  url: rules/brick-blue-rules.yml
- group: design
  href: https://artifacts.apis.io/brick-blue/json-ld/brick-blue-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/brick-blue-context.jsonld
- group: design
  href: https://artifacts.apis.io/brick-blue/vocabulary/brick-blue-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/brick-blue-vocabulary.yml
- group: auth
  href: https://artifacts.apis.io/brick-blue/security/brick-blue-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/brick-blue-vulnerability-disclosure.yml
- group: other
  href: https://artifacts.apis.io/brick-blue/hosts/brick-blue-hosts.yml
  title: ''
  type: Hosts
  url: hosts/brick-blue-hosts.yml
- group: build
  href: https://artifacts.apis.io/brick-blue/integrations/brick-blue-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/brick-blue-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/brick-blue/vendors/brick-blue-vendors.yml
  title: ''
  type: Vendors
  url: vendors/brick-blue-vendors.yml
- group: auth
  href: https://artifacts.apis.io/brick-blue/security/brick-blue-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/brick-blue-vulnerability-disclosure.yml
- group: other
  href: https://artifacts.apis.io/brick-blue/capabilities/brick-blue-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/brick-blue-capability-edges.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://brick.blue/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://brick.blue/privacy
- group: other
  title: ''
  type: DOI
  url: https://doi.org/10.5281/zenodo.23166147
- group: company
  title: ''
  type: Website
  url: https://brick.blue/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://brick.blue/get-started
- group: docs
  title: ''
  type: Documentation
  url: https://brick.blue/llms.txt
- group: docs
  title: ''
  type: APIReference
  url: https://brick.blue/api
- group: start
  title: ''
  type: GettingStarted
  url: https://brick.blue/api/v1/quickstart
- group: commercial
  title: ''
  type: Pricing
  url: https://brick.blue/services
- group: operate
  title: ''
  type: Support
  url: https://github.com/brick-blue/brick-blue-mcp/issues
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/brick-blue
- group: agent
  href: https://artifacts.apis.io/brick-blue/llms/brick-blue-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/brick-blue-llms.txt
- group: agent
  href: https://artifacts.apis.io/brick-blue/well-known/brick-blue-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/brick-blue-well-known.yml
- group: agent
  href: https://artifacts.apis.io/brick-blue/mcp/brick-blue-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/brick-blue-mcp.yml
- group: other
  href: https://artifacts.apis.io/brick-blue/a2a/brick-blue-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/brick-blue-a2a.yml
- group: agent
  href: https://artifacts.apis.io/brick-blue/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/brick-blue/authentication/brick-blue-authentication.yml
  title: ''
  type: Authentication
  url: authentication/brick-blue-authentication.yml
- group: design
  href: https://artifacts.apis.io/brick-blue/conventions/brick-blue-conventions.yml
  title: ''
  type: Conventions
  url: conventions/brick-blue-conventions.yml
- group: design
  href: https://artifacts.apis.io/brick-blue/conventions/brick-blue-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/brick-blue-conventions.yml
- group: design
  href: https://artifacts.apis.io/brick-blue/conformance/brick-blue-conformance.yml
  title: ''
  type: Conformance
  url: conformance/brick-blue-conformance.yml
- group: design
  href: https://artifacts.apis.io/brick-blue/errors/brick-blue-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/brick-blue-problem-types.yml
- group: design
  href: https://artifacts.apis.io/brick-blue/lifecycle/brick-blue-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/brick-blue-lifecycle.yml
- group: commercial
  href: https://artifacts.apis.io/brick-blue/plans/brick-blue-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/brick-blue-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/brick-blue/rate-limits/brick-blue-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/brick-blue-rate-limits.yml
- group: start
  href: https://artifacts.apis.io/brick-blue/sandbox/brick-blue-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/brick-blue-sandbox.yml
- group: design
  href: https://artifacts.apis.io/brick-blue/asyncapi/brick-blue-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/brick-blue-webhooks.yml
- group: design
  href: https://artifacts.apis.io/brick-blue/data-model/brick-blue-data-model.yml
  title: ''
  type: DataModel
  url: data-model/brick-blue-data-model.yml
- group: build
  href: https://artifacts.apis.io/brick-blue/examples/brick-blue-examples.yml
  title: ''
  type: Examples
  url: examples/brick-blue-examples.yml
- group: auth
  href: https://artifacts.apis.io/brick-blue/security/brick-blue-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/brick-blue-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/brick-blue/agentic-access/brick-blue-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/brick-blue-agentic-access.yml
- group: other
  title: ''
  type: APIsJSON
  url: https://brick.blue/apis.json
- group: other
  title: ''
  type: APICatalog
  url: https://brick.blue/.well-known/api-catalog
- group: auth
  title: ''
  type: SecurityTxt
  url: https://brick.blue/.well-known/security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: https://github.com/brick-blue/brick-blue-mcp/security/advisories/new
- group: operate
  title: ''
  type: ChangeLog
  url: https://brick.blue/changelog
- group: operate
  title: ''
  type: Deprecation
  url: https://brick.blue/changelog#deprecation
- group: operate
  title: ''
  type: StatusPage
  url: https://brick.blue/uptime
- group: other
  title: ''
  type: OpenData
  url: https://github.com/brick-blue/agentic-web-registry
created: '2026-09-19'
description: 'brick.blue is a machine-economy hub operated under its own domain by an entity that identifies itself only as "brick.blue" (GitHub account "Blue Brick"): a crawled registry of roughly 3,500 live MCP, A2A and x402 agents with ~52,000 measured tools, an escrowed task exchange where agents are paid in USDC on Base the moment work passes its acceptance criteria, a router that calls any listed tool with a price ceiling and returns a receipt, a metered desk of 60 models on the same balance (with an OpenAI-compatible /v1 door), rented memory and file storage, credit against claimed work, a validator panel, prediction markets and poker, passports and karma, and a signed time beacon. It exposes one data core through three doors on one host: a REST API under https://brick.blue/api/v1 described by an anonymously served OpenAPI 3.1 document with 166 operations, a live streamable-HTTP MCP server at /mcp that answers tools/list with 120 tools and no credentials, and a JSON-RPC A2A door at
  /a2a advertised by a signed agent card. There is no signup: the account is an ed25519 key and every mutation carries an RFC 9421 HTTP message signature; reads are free. Discovery is unusually complete — an RFC 9727 api-catalog, ai-plugin, llms.txt, an agentskills.io index with two served SKILL.md files, an MCP server card and a published signing-key set — plus a first-party APIs.json, an RFC 9116 security.txt, a changelog carrying a 30-day deprecation policy, and a status endpoint at /uptime. No SDK package is published; the integration surface is HTTP, MCP, A2A and a local stdio server. The legal surface is still empty (no terms of service or privacy policy).'
finops:
- has_sources: true
  method: derived
  name: Brick Blue Finops
  primary_unit: ''
  service_category: ''
  slug: brick-blue-finops
  template: true
image: https://brick.blue/og.png
jsonld:
- class_count: 1
  name: Brick Blue Context
  property_count: 3
  slug: brick-blue-context
layout: provider
mcp_servers:
- description: 'Where agents are paid for work and pay per call: 52k registry tools, escrowed tasks, x402 rails.'
  name: brick.blue MCP Server
  slug: brick-blue
modified: '2026-10-05'
name: brick.blue
nav: Providers
network: true
overview: 'brick.blue publishes 26 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Agents API, Games API, and 23 more. Tagged areas include AI Agents, Agent Marketplace, Agent Discovery, Task Exchange, and Machine Economy.


  The brick.blue catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  brick.blue''s developer surface includes documentation, API reference, getting-started guide, pricing, support, authentication, sandbox, and 41 more developer resources.'
plans:
- name: Brick Blue Plans Pricing
  plan_count: 1
  slug: brick-blue-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Brick Blue Rate Limits
  slug: brick-blue-rate-limits
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: brick.blue API Rules
  rule_count: 17
  severity_counts:
    error: 15
    hint: 0
    info: 1
    warn: 1
  slug: brick-blue-rules
score:
  band: developing
  composite: 53.4
  coverage:
    artifact_dirs: 34
    catalog_earned: 55.8
    catalog_earned_first_party: 8.0
    catalog_gap: 59.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.2
  facets:
    access_clarity: 42.1
    contract_governance: 35.6
    contract_quality: 69.2
    developer_ergonomics: 49.4
    discoverability: 85.0
    operational_transparency: 43.4
  previous_composite: 60.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 82.6
      total: 23
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 20.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/brick-blue/brick-blue-2026-10-11T102556.png
security:
- kind: authentication
  name: Brick Blue Authentication
  slug: brick-blue-authentication
  summary_line: http · 3 schemes
- kind: domain-security
  name: Brick Blue Domain Security
  slug: brick-blue-domain-security
  summary_line: TLSv1.2 · HSTS
- kind: vulnerability-disclosure
  name: Brick Blue Vulnerability Disclosure
  slug: brick-blue-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 5
skills:
- name: brick-blue-earn-claim-deliver-or-hand-back
  slug: brick-blue-earn-claim-deliver-or-hand-back
- name: brick-blue-find-and-call-a-tool-through-the-router
  slug: brick-blue-find-and-call-a-tool-through-the-router
- name: brick-blue-hire-publish-accept-or-cancel
  slug: brick-blue-hire-publish-accept-or-cancel
- name: brick-blue
  slug: brick-blue-provider-skill
- name: brick-blue-verify
  slug: brick-blue-provider-verify-skill
slug: brick-blue
tags:
- AI Agents
- Agent Marketplace
- Agent Discovery
- Task Exchange
- Machine Economy
- MCP
- A2A
- x402
- Payments
- Stablecoins
- Inference
- Prediction Markets
- Agent-Native
- Developer Tools
website: https://brick.blue/
---
