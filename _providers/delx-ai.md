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
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: flavored
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: true
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 55.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 988
  human_in_the_loop: 471
  name: Delx Ai Agentic Access
  operation_count: 1002
  slug: delx-ai-agentic-access
  summary_line: 1002 operations · 988 acting · 471 human-in-the-loop
api_count: 2
apis:
- description: 'Remote MCP server (Streamable HTTP, protocol version 2025-06-18) at https://api.delx.ai/mcp with a compatibility alias at /v1/mcp (served with Deprecation and Sunset headers) and a core-tier endpoint '
  name: Delx Protocol MCP Server
  slug: delx-protocol-mcp-server
- description: JSON-RPC A2A endpoint at https://api.delx.ai/v1/a2a exposing methods/list, agents/register, message/send, heartbeat/bundle, tasks/get and tasks/cancel, discovered through an agent card served at /.wel
  name: Delx Agent Operations Protocol (A2A)
  slug: delx-protocol-a2a-agent
- baseURL: https://api.delx.ai
  baseurl_source: declared
  description: The A2a API from Delx — 2 operation(s) for a2a.
  name: Delx A2a API
  phrasing_intents:
  - id: v1_a2a
    intent: Send an A2A JSON-RPC message to the Delx agent
    question: How do I send a JSON-RPC message/send call to Delx over the A2A protocol?
  - id: get_api_v1_a2a_methods
    intent: List the available A2A methods
    question: What methods does the A2A endpoint support?
  phrasing_ops: 2
  slug: delx-ai-a2a-api
- baseURL: https://api.delx.ai
  baseurl_source: declared
  description: The agents API from Delx — 2 operation(s) for agents.
  name: Delx Agents API
  phrasing_intents:
  - id: post_api_v1_agents_register
    intent: Register an agent and get its token
    question: How do I register my agent with Delx to get an identity and token?
  - id: get_api_v1_agents_agent_id_public_profile
    intent: View an agent's public reputation profile
    question: What does another agent's public profile and reputation look like?
  phrasing_ops: 2
  slug: delx-ai-agents-api
- baseURL: https://api.delx.ai
  baseurl_source: declared
  description: The discovery API from Delx — 2 operation(s) for discovery.
  name: Delx Discovery API
  phrasing_intents:
  - id: get_api_v1_status
    intent: Check service status and discovery links
    question: Is the Delx service up right now?
  - id: get_api_v1_mcp_start
    intent: Get the MCP starting point for the premium handoff
    question: Where should an agent start when connecting over MCP for the premium controller handoff?
  phrasing_ops: 2
  slug: delx-ai-discovery-api
- baseURL: https://api.delx.ai
  baseurl_source: declared
  description: The Mcp API from Delx — 1 operation(s) for mcp.
  name: Delx MCP API
  phrasing_intents:
  - id: v1_mcp_protocol
    intent: Call the MCP protocol endpoint for recovery tools
    question: How do I call the Delx MCP endpoint to use its recovery and continuity tools?
  phrasing_ops: 1
  slug: delx-ai-mcp-api
- baseURL: https://api.delx.ai
  baseurl_source: declared
  description: The protocol API from Delx — 5 operation(s) for protocol.
  name: Delx Protocol API
  phrasing_intents:
  - id: get_recovery_action_plan
    intent: Get a recovery plan for an agent incident
    question: How do I get a step-by-step plan to recover my agent from an incident?
  - id: get_session_summary
    intent: Summarize an agent session for handoff
    question: How can I get a handoff summary of what happened in my agent session?
  - id: generate_controller_brief
    intent: Brief a controller on a session's status
    question: How do I give my controller or evaluator a short brief on an agent session and the next decision?
  - id: generate_incident_rca
    intent: Produce a root cause analysis for an incident
    question: How do I get a root cause analysis with evidence and corrective actions for my agent's failure?
  - id: generate_fleet_summary
    intent: Summarize health across an agent fleet
    question: How can I see patterns, health and alerts across my whole fleet of agents?
  phrasing_ops: 5
  slug: delx-ai-protocol-api
- baseURL: https://api.delx.ai
  baseurl_source: declared
  description: The reliability API from Delx — 1 operation(s) for reliability.
  name: Delx Reliability API
  phrasing_intents:
  - id: get_api_v1_reliability
    intent: Check service latency, success rate and uptime
    question: How reliable is the Delx service right now?
  phrasing_ops: 1
  slug: delx-ai-reliability-api
- baseURL: https://api.delx.ai
  baseurl_source: declared
  description: The tools API from Delx — 2 operation(s) for tools.
  name: Delx Tools API
  phrasing_intents:
  - id: get_api_v1_tools
    intent: Browse the Delx tool catalog
    question: What tools does Delx expose to agents?
  - id: post_api_v1_tools_batch
    intent: Run several tools in one batch call
    question: Can I run a multi-tool flow in a single request instead of calling each tool separately?
  phrasing_ops: 2
  slug: delx-ai-tools-api
- baseURL: https://api.delx.ai
  baseurl_source: declared
  description: The x402 API from Delx — 987 operation(s) for x402.
  name: Delx X402 API
  phrasing_intents:
  - id: generate_image
    intent: Generate an image from a text prompt
    question: Can an agent generate a product visual or ad creative from a prompt without an API key?
  - id: generate_image_budget
    intent: Generate a low-cost draft image
    question: Is there a half-cent image option for quick concept drafts?
  - id: remove_background
    intent: Remove the background from an image
    question: How do I cut out the background of a product photo and get a transparent PNG?
  - id: transcribe_audio
    intent: Transcribe a short audio clip to text
    question: Can I get a transcript of a voice note under a minute long?
  - id: caption_image
    intent: Write a caption or alt text for an image
    question: Can an agent write one-sentence alt text for a picture?
  - id: colorize_photo
    intent: Colorize a black-and-white photo
    question: Can I add color to an old grayscale photograph?
  - id: upscale_image_hq
    intent: Upscale an image to higher resolution
    question: How can I enlarge a small image to up to 4 megapixels with good quality?
  - id: replace_background
    intent: Replace an image background with a solid fill
    question: Can I put a product shot on a studio gray backdrop?
  phrasing_ops: 987
  slug: delx-ai-x402-api
artifact_total: 25
asyncapis:
- description: ''
  name: Delx Ai Webhooks
  slug: delx-ai-webhooks
common:
- group: other
  href: https://artifacts.apis.io/delx-ai/capabilities/delx-ai-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/delx-ai-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/delx-ai/overlays/delx-ai-protocol-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/delx-ai-protocol-overlay.yaml
- group: other
  href: https://artifacts.apis.io/delx-ai/overlays/delx-ai-commerce-x402-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/delx-ai-commerce-x402-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/delx-ai/agentic-access/delx-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/delx-ai-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/delx-ai/security/delx-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/delx-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/delx-ai/security/delx-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/delx-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://delx.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://delx.ai/developers
- group: docs
  title: ''
  type: Documentation
  url: https://ontology.delx.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://ontology.delx.ai/docs/discovery
- group: start
  title: ''
  type: GettingStarted
  url: https://api.delx.ai/api/v1/mcp/start
- group: operate
  title: ''
  type: Support
  url: https://delx.ai/trust
- group: company
  title: ''
  type: Blog
  url: https://delx.ai/research
- group: company
  title: ''
  type: BlogRSS
  url: https://ontology.delx.ai/feed.xml
- group: operate
  title: ''
  type: ChangeLog
  url: https://delx.ai/changelog
- group: operate
  href: https://artifacts.apis.io/delx-ai/changelog/delx-ai-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/delx-ai-changelog.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/davidmosiah
- group: company
  title: ''
  type: Newsroom
  url: https://delx.ai/press
- group: commercial
  title: ''
  type: Pricing
  url: https://delx.ai/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ontology.delx.ai/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ontology.delx.ai/legal/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://delx.ai/research/status
- group: auth
  title: ''
  type: Security
  url: https://ontology.delx.ai/docs/security
- group: auth
  href: https://artifacts.apis.io/delx-ai/well-known/delx-ai-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/delx-ai-security.txt
- group: agent
  href: https://artifacts.apis.io/delx-ai/well-known/delx-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/delx-ai-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: https://delx.ai/.well-known/api-catalog
- group: other
  href: https://artifacts.apis.io/delx-ai/a2a/delx-ai-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/delx-ai-a2a.yml
- group: agent
  href: https://artifacts.apis.io/delx-ai/mcp/delx-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/delx-ai-mcp.yml
- group: agent
  href: https://artifacts.apis.io/delx-ai/llms/delx-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/delx-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/delx-ai/llms/delx-ai-api-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/delx-ai-api-llms.txt
- group: agent
  href: https://artifacts.apis.io/delx-ai/llms/delx-ai-ontology-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/delx-ai-ontology-llms.txt
- group: agent
  href: https://artifacts.apis.io/delx-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/delx-ai/authentication/delx-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/delx-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/delx-ai/conventions/delx-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/delx-ai-conventions.yml
- group: design
  href: https://artifacts.apis.io/delx-ai/conventions/delx-ai-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/delx-ai-conventions.yml
- group: design
  href: https://artifacts.apis.io/delx-ai/errors/delx-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/delx-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/delx-ai/lifecycle/delx-ai-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/delx-ai-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/delx-ai/lifecycle/delx-ai-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/delx-ai-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/delx-ai/conformance/delx-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/delx-ai-conformance.yml
- group: operate
  href: https://artifacts.apis.io/delx-ai/rate-limits/delx-ai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/delx-ai-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/delx-ai/plans/delx-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/delx-ai-plans-pricing.yml
- group: build
  href: https://artifacts.apis.io/delx-ai/packages/delx-ai-packages.yml
  title: ''
  type: Packages
  url: packages/delx-ai-packages.yml
- group: build
  href: https://artifacts.apis.io/delx-ai/packages/delx-ai-packages.yml
  title: ''
  type: SDKs
  url: packages/delx-ai-packages.yml
- group: build
  href: https://artifacts.apis.io/delx-ai/cli/delx-ai-cli.yml
  title: ''
  type: CLI
  url: cli/delx-ai-cli.yml
- group: design
  href: https://artifacts.apis.io/delx-ai/asyncapi/delx-ai-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/delx-ai-webhooks.yml
- group: design
  href: https://artifacts.apis.io/delx-ai/data-model/delx-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/delx-ai-data-model.yml
- group: start
  href: https://artifacts.apis.io/delx-ai/sandbox/delx-ai-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/delx-ai-sandbox.yml
- group: other
  title: ''
  type: AITransparency
  url: https://delx.ai/research/system-cards/delx-protocol-3.3.5
- group: other
  title: ''
  type: DataSubjectRequest
  url: https://ontology.delx.ai/legal/privacy
- group: other
  title: ''
  type: Subprocessors
  url: https://ontology.delx.ai/legal/privacy
- group: auth
  href: https://artifacts.apis.io/delx-ai/security/delx-ai-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/delx-ai-trust-center.yml
created: '2026-09-19'
description: 'Delx is an independent, founder-led AI agent lab (David Batista) that publishes an agent-native stack on delx.ai: the free Delx Protocol for agent recovery, continuity, witness lineage and handoff (30 core MCP tools over Streamable HTTP at api.delx.ai/mcp, a JSON-RPC A2A endpoint at api.delx.ai/v1/a2a with a published agent card, a 15-operation OpenAPI 3.1 REST surface, and a CLI), plus Delx Commerce, a separate pay-per-result business of 987 x402/MPP-priced micro-utilities (image, speech, web extraction, data-quality, chain and agent-ops tools at $0.001-$0.08 USDC per call, settled on Base or Solana) described by a 987-operation OpenAPI 3.1 contract. Discovery is unusually complete for a small provider: RFC 9727 api-catalog, RFC 8414/9728 OAuth metadata, MCP server card, agentskills.io index, ARD ai-catalog, llms.txt, agents.txt, security.txt and an ERC-8004 on-chain agent identity are all served from the provider''s own hosts.'
finops:
- has_sources: true
  method: derived
  name: Delx Ai Finops
  primary_unit: call (usdc)
  service_category: ''
  slug: delx-ai-finops
  template: false
image: https://delx.ai/icon-512.png
layout: provider
mcp_servers:
- description: 'Delx runs one remote MCP server on api.delx.ai - the same host as its REST and A2A surfaces - and also ships a stdio bridge (npm delx-mcp-server). The canonical endpoint is https://api.delx.ai/mcp: th'
  name: Delx MCP Server
  slug: delx-ai-mcp-yml
- description: ''
  name: MCP Server Card (provider-hosted)
  slug: mcp-server-card-provider-hosted
modified: '2026-09-19'
name: Delx
nav: Providers
network: true
overview: 'Delx publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including A2a API, Agents API, Discovery API, and 7 more. Tagged areas include Agents, AI Agents, MCP, A2A, and x402.


  The Delx catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Delx''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, changelog, pricing, and 44 more developer resources.'
plans:
- name: Delx Ai Plans Pricing
  plan_count: 8
  slug: delx-ai-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 1
  name: Delx Ai Rate Limits
  slug: delx-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 97
  extends:
  - spectral:oas
  name: Delx API Rules
  rule_count: 56
  severity_counts:
    error: 47
    hint: 0
    info: 3
    warn: 6
  slug: delx-ai-rules
score:
  band: exemplar
  composite: 69.4
  coverage:
    artifact_dirs: 33
    catalog_earned: 64.5
    catalog_earned_first_party: 20.0
    catalog_gap: 50.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.3
  facets:
    access_clarity: 63.2
    contract_governance: 31.8
    contract_quality: 56.8
    developer_ergonomics: 72.6
    discoverability: 85.8
    operational_transparency: 76.3
  previous_composite: 75.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 87.5
      total: 8
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 39.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 27.8
screenshot: https://apis.io/screenshots/delx-ai/delx-ai-2026-10-11T103648.png
security:
- kind: authentication
  name: Delx Ai Authentication
  slug: delx-ai-authentication
  summary_line: apiKey · 6 schemes
- kind: domain-security
  name: Delx Ai Domain Security
  slug: delx-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Delx Ai Vulnerability Disclosure
  slug: delx-ai-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Delx Ai Trust Center
  slug: delx-ai-trust-center
  summary_line: trust center published
skill_count: 3
skills:
- name: delx-protocol
  slug: delx-ai-delx-protocol
- name: delx-self-test
  slug: delx-ai-delx-self-test
- name: delx-recovery-first-hour
  slug: delx-ai-recovery-first-hour
slug: delx-ai
tags:
- Agents
- AI Agents
- MCP
- A2A
- x402
- Agentic Commerce
- Agent Continuity
- Agent Recovery
- Media Generation
- Web Intelligence
- Data Quality
- Agent-Native
website: https://delx.ai/
---
