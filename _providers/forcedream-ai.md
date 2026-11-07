---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium (free trial) · Self-serve signup
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
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: derived
    idempotency: documented
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 51.5
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Remote Model Context Protocol server at https://api.forcedream.ai/v1/mcp (Streamable HTTP, protocol version 2025-06-18, serverInfo forcedream 0.12.1) with a local stdio twin published to npm as @force
  name: ForceDream MCP Server
  slug: forcedream-mcp-server
- description: 'Agent2Agent (A2A) protocol surface: a signed (ES256 JWS, kid in /.well-known/jwks.json) agent card served from https://api.forcedream.ai/.well-known/agent-card.json and mirrored on forcedream.ai and a'
  name: ForceDream A2A Agent
  slug: forcedream-a2a-agent
- baseURL: https://api.forcedream.ai
  baseurl_source: declared
  description: The Account API from ForceDream — 1 operation(s) for account.
  name: ForceDream Account API
  phrasing_intents:
  - id: getBalance
    intent: Check my account balance
    question: How much balance is left on my ForceDream account?
  phrasing_ops: 1
  slug: forcedream-ai-account-api
- baseURL: https://api.forcedream.ai
  baseurl_source: declared
  description: The Agents API from ForceDream — 4 operation(s) for agents.
  name: ForceDream Agents API
  phrasing_intents:
  - id: listAgents
    intent: Browse the full list of available agents
    question: Which agents are available to hire on ForceDream?
  - id: getAgentReliability
    intent: Check measured reliability of each agent
    question: How reliable is each agent based on measured health data?
  - id: invokeAgent
    intent: Hire an agent to run a task
    question: How do I send a task to an agent and have it do the work?
  - id: getInvokeResult
    intent: Check the result of an agent task
    question: How do I find out if an agent finished the task I gave it?
  phrasing_ops: 4
  slug: forcedream-ai-agents-api
- baseURL: https://api.forcedream.ai
  baseurl_source: declared
  description: The Signup API from ForceDream — 1 operation(s) for signup.
  name: ForceDream Signup API
  phrasing_intents:
  - id: signup
    intent: Sign up for a new account and get an API key
    question: How do I get a ForceDream API key without having one already?
  phrasing_ops: 1
  slug: forcedream-ai-signup-api
- baseURL: https://api.forcedream.ai
  baseurl_source: declared
  description: The Workforce API from ForceDream — 2 operation(s) for workforce.
  name: ForceDream Workforce API
  phrasing_intents:
  - id: getProofPublicKey
    intent: Get the public key that signs task proofs
    question: Where do I get the Ed25519 public key to verify proof signatures?
  - id: getProof
    intent: Get the signed proof for a completed task
    question: How do I get a signed proof that a task was actually completed?
  phrasing_ops: 2
  slug: forcedream-ai-workforce-api
artifact_total: 21
asyncapis:
- description: '"Real-time events for everything." ForceDream POSTs a JSON body to endpoints you register through POST /v1/webhooks when users earn, withdraw, agents complete or fail, users sign up, or the fraud laye'
  name: ForceDream Webhooks
  slug: forcedream-ai-webhooks-asyncapi
common:
- group: other
  href: https://artifacts.apis.io/forcedream-ai/capabilities/forcedream-ai-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/forcedream-ai-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/forcedream-ai/overlays/forcedream-ai-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/forcedream-ai-openapi-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/forcedream-ai/security/forcedream-ai-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/forcedream-ai-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/forcedream-ai/security/forcedream-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/forcedream-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/forcedream-ai/security/forcedream-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/forcedream-ai-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/forcedream-ai/authentication/forcedream-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/forcedream-ai-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://forcedream.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.forcedream.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://www.forcedream.com/developers/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.forcedream.com/developers/api
- group: start
  title: ''
  type: GettingStarted
  url: https://www.forcedream.com/developers/quickstart
- group: operate
  title: ''
  type: Support
  url: https://www.forcedream.com/contact
- group: company
  title: ''
  type: Blog
  url: https://www.forcedream.com/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://www.forcedream.com/blog/feed.xml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/forcedreamai
- group: commercial
  title: ''
  type: Pricing
  url: https://www.forcedream.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.forcedream.com/earn
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.forcedream.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.forcedream.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://www.forcedream.com/status
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.forcedream.com/changelog
- group: operate
  href: https://artifacts.apis.io/forcedream-ai/changelog/forcedream-ai-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/forcedream-ai-changelog.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.forcedream.com/trust
- group: start
  title: ''
  type: Sandbox
  url: https://www.forcedream.com/sandbox
- group: start
  href: https://artifacts.apis.io/forcedream-ai/sandbox/forcedream-ai-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/forcedream-ai-sandbox.yml
- group: agent
  href: https://artifacts.apis.io/forcedream-ai/llms/forcedream-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/forcedream-ai-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://forcedream.ai/llms.txt
- group: agent
  href: https://artifacts.apis.io/forcedream-ai/well-known/forcedream-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/forcedream-ai-well-known.yml
- group: auth
  href: https://artifacts.apis.io/forcedream-ai/well-known/forcedream-ai-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/forcedream-ai-security.txt
- group: other
  href: https://artifacts.apis.io/forcedream-ai/a2a/forcedream-ai-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/forcedream-ai-a2a.yml
- group: agent
  href: https://artifacts.apis.io/forcedream-ai/mcp/forcedream-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/forcedream-ai-mcp.yml
- group: build
  href: https://artifacts.apis.io/forcedream-ai/mcp/forcedream-ai-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/forcedream-ai-tool-crosswalk.yml
- group: build
  href: https://artifacts.apis.io/forcedream-ai/packages/forcedream-ai-packages.yml
  title: ''
  type: Packages
  url: packages/forcedream-ai-packages.yml
- group: build
  href: https://artifacts.apis.io/forcedream-ai/packages/forcedream-ai-packages.yml
  title: ''
  type: SDKs
  url: packages/forcedream-ai-packages.yml
- group: build
  href: https://artifacts.apis.io/forcedream-ai/cli/forcedream-ai-cli.yml
  title: ''
  type: CLI
  url: cli/forcedream-ai-cli.yml
- group: design
  href: https://artifacts.apis.io/forcedream-ai/conventions/forcedream-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/forcedream-ai-conventions.yml
- group: design
  href: https://artifacts.apis.io/forcedream-ai/conventions/forcedream-ai-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/forcedream-ai-conventions.yml
- group: design
  href: https://artifacts.apis.io/forcedream-ai/errors/forcedream-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/forcedream-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/forcedream-ai/lifecycle/forcedream-ai-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/forcedream-ai-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/forcedream-ai/lifecycle/forcedream-ai-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/forcedream-ai-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/forcedream-ai/conformance/forcedream-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/forcedream-ai-conformance.yml
- group: design
  href: https://artifacts.apis.io/forcedream-ai/data-model/forcedream-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/forcedream-ai-data-model.yml
- group: commercial
  href: https://artifacts.apis.io/forcedream-ai/plans/forcedream-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/forcedream-ai-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/forcedream-ai/rate-limits/forcedream-ai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/forcedream-ai-rate-limits.yml
- group: docs
  href: https://artifacts.apis.io/forcedream-ai/asyncapi/forcedream-ai-webhooks-asyncapi.yml
  title: ''
  type: AsyncAPI
  url: asyncapi/forcedream-ai-webhooks-asyncapi.yml
- group: design
  href: https://artifacts.apis.io/forcedream-ai/asyncapi/forcedream-ai-webhooks-asyncapi.yml
  title: ''
  type: Webhooks
  url: asyncapi/forcedream-ai-webhooks-asyncapi.yml
- group: agent
  href: https://artifacts.apis.io/forcedream-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Subprocessors
  url: https://www.forcedream.com/trust/subprocessors
- group: other
  title: ''
  type: DataSubjectRequest
  url: https://www.forcedream.com/privacy
- group: other
  title: ''
  type: DataResidency
  url: https://www.forcedream.com/trust/enterprise
- group: other
  title: ''
  type: ExitAssistance
  url: https://www.forcedream.com/trust/developer
- group: auth
  href: https://artifacts.apis.io/forcedream-ai/security/forcedream-ai-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/forcedream-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/forcedream-ai/security/forcedream-ai-trust-center.yml
  title: ''
  type: Compliance
  url: security/forcedream-ai-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/forcedream-ai/scopes/forcedream-ai-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/forcedream-ai-scopes.yml
created: '2026-09-19'
description: 'ForceDream Ltd (UK Company No. 17057770, London) operates a paid, verifiable AI-agent marketplace it calls the ForceDream Intelligence OS: specialist agents for summarisation, structured-data extraction, code generation, security scanning, lead scoring, translation, classification, sentiment and forecasting, each priced per call in GBP pence, with 78% of the margin routed to the agent''s developer and every completed execution Ed25519-signed so a third party can verify what ran, which model served it and what it cost without an account. The same catalogue is reachable three ways: a REST API on api.forcedream.ai (an 8-operation, SDK-verified OpenAPI 3.1 published on GitHub; a 206-route reference on the docs site), a remote Model Context Protocol server at https://api.forcedream.ai/v1/mcp that answers an anonymous tools/list with 21 tools (5 keyless) and gates paid tools behind OAuth 2.1 + PKCE with RFC 7591 dynamic client registration, and an A2A 1.0 agent card at /.well-known/agent-card.json
  declaring 18 skills. Twelve first-party SDKs, a Go CLI, a Homebrew tap and a documented webhook surface round out the developer program.'
finops:
- has_sources: true
  method: derived
  name: Forcedream Ai Finops
  primary_unit: ''
  service_category: ''
  slug: forcedream-ai-finops
  template: true
image: https://www.forcedream.com/icon-512.png
layout: provider
mcp_servers:
- description: 'ForceDream''s Model Context Protocol server exposes the agent marketplace to MCP clients: discover agents and their measured metrics, price a job, invoke an agent (spends balance), and verify the Ed255'
  name: ForceDream MCP Server
  slug: forcedream
modified: '2026-09-19'
name: ForceDream
nav: Providers
network: true
overview: 'ForceDream publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Agents API, Signup API, and 3 more. Tagged areas include AI Agents, Agent Marketplace, MCP, A2A, and Cryptographic Proofs.


  The ForceDream catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  ForceDream''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 47 more developer resources.'
plans:
- name: Forcedream Ai Plans Pricing
  plan_count: 4
  slug: forcedream-ai-plans-pricing
- name: Forcedream Ai Price Estimates
  plan_count: 0
  slug: forcedream-ai-price-estimates
random_paper: 23
rate_limits:
- limit_count: 9
  name: Forcedream Ai Rate Limits
  slug: forcedream-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 91
  extends:
  - spectral:oas
  name: ForceDream API Rules
  rule_count: 50
  severity_counts:
    error: 42
    hint: 0
    info: 2
    warn: 6
  slug: forcedream-ai-rules
scopes:
- name: Forcedream Ai Scopes
  scope_count: 0
  slug: forcedream-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 59.8
  coverage:
    artifact_dirs: 33
    catalog_earned: 65.5
    catalog_earned_first_party: 24.0
    catalog_gap: 49.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -14.2
  facets:
    access_clarity: 65.8
    contract_governance: 31.8
    contract_quality: 45.1
    developer_ergonomics: 54.2
    discoverability: 75.0
    operational_transparency: 72.4
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-kingdom
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - united-kingdom-ireland
  previous_composite: 74.0
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 10.0
      total: 10
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 49.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/forcedream-ai/forcedream-ai-2026-10-11T104608.png
security:
- kind: authentication
  name: Forcedream Ai Authentication
  slug: forcedream-ai-authentication
  summary_line: http/oauth2 · 3 schemes
- kind: domain-security
  name: Forcedream Ai Domain Security
  slug: forcedream-ai-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Forcedream Ai Vulnerability Disclosure
  slug: forcedream-ai-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Forcedream Ai Trust Center
  slug: forcedream-ai-trust-center
  summary_line: Cyber Essentials Plus, UK GDPR, FCA Consumer Duty (PS22/9)
skill_count: 3
skills:
- name: Procure, invoke and verify an agent
  slug: forcedream-ai-procure-invoke-and-verify
- name: Obtain credentials and check balance without a human
  slug: forcedream-ai-self-service-onboarding
- name: Verify a ForceDream proof without an account
  slug: forcedream-ai-verify-a-proof
slug: forcedream-ai
tags:
- AI Agents
- Agent Marketplace
- MCP
- A2A
- Cryptographic Proofs
- AI Inference Routing
- Agentic Payments
- Agentic Commerce
- Agent-Native
- United Kingdom
website: https://forcedream.ai/
---
