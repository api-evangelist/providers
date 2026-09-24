---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: flavored
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 30.1
  scored_at: '2026-09-24'
api_count: 4
apis:
- description: 'REST API on api.nefesh.ai (FastAPI): POST /v1/ingest takes a session_id, an ISO 8601 timestamp and at least one of 35+ signal fields and returns the fused state, stress_score, confidence, suggested_ac'
  name: Nefesh Human State API
  slug: nefesh-human-state-api
- description: 'LLM gateway on gateway.nefesh.ai that injects the caller''s live human state into the request and adjusts temperature before forwarding to an upstream model. Three modes: OpenAI-compatible POST /v1/cha'
  name: Nefesh Cognitive Compute Router
  slug: nefesh-cognitive-compute-router
- description: Hosted remote MCP server at https://mcp.nefesh.ai/mcp (Streamable HTTP, protocol 2025-06-18, session-id based; serverInfo nefesh 1.26.0). Anonymous initialize and tools/list succeed and return six too
  name: Nefesh MCP Server
  slug: nefesh-mcp-server
- description: 'A2A agent served from the MCP host: card at https://mcp.nefesh.ai/.well-known/agent-card.json, JSON-RPC 2.0 endpoint at POST https://mcp.nefesh.ai/a2a supporting message/send, message/sendStream, task'
  name: Nefesh Human State Agent (A2A)
  slug: nefesh-human-state-agent-a2a
artifact_total: 13
asyncapis:
- description: ''
  name: Nefesh Ai Webhooks
  slug: nefesh-ai-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://nefesh.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://nefesh.ai/docs
- group: docs
  title: ''
  type: Documentation
  url: https://nefesh.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://nefesh.ai/docs/api
- group: start
  title: ''
  type: GettingStarted
  url: https://nefesh.ai/docs/quickstart
- group: commercial
  title: ''
  type: Pricing
  url: https://nefesh.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://nefesh.ai/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://nefesh.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://nefesh.ai/docs/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/nefesh-ai
- group: auth
  title: ''
  type: Compliance
  url: https://nefesh.ai/docs/regulatory
- group: other
  title: ''
  type: X-Enterprise
  url: https://nefesh.ai/enterprise
- group: start
  title: ''
  type: X-Demo
  url: https://sandbox.nefesh.ai
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/nefesh-ai/refs/heads/main/llms/nefesh-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/nefesh-ai-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://nefesh.ai/llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/nefesh-ai/refs/heads/main/a2a/nefesh-ai-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/nefesh-ai-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/nefesh-ai/refs/heads/main/mcp/nefesh-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/nefesh-ai-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/nefesh-ai/refs/heads/main/well-known/nefesh-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/nefesh-ai-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/nefesh-ai/refs/heads/main/well-known/nefesh-ai-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/nefesh-ai-security.txt
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/nefesh-ai/refs/heads/main/json-schema/nefesh-ai-hsp-1.0.schema.json
  title: ''
  type: JSONSchema
  url: json-schema/nefesh-ai-hsp-1.0.schema.json
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/nefesh-ai/refs/heads/main/packages/nefesh-ai-packages.yml
  title: ''
  type: Packages
  url: packages/nefesh-ai-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/nefesh-ai/refs/heads/main/cli/nefesh-ai-cli.yml
  title: ''
  type: CLI
  url: cli/nefesh-ai-cli.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/nefesh-ai/refs/heads/main/conformance/nefesh-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/nefesh-ai-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/nefesh-ai/refs/heads/main/errors/nefesh-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/nefesh-ai-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/nefesh-ai/refs/heads/main/lifecycle/nefesh-ai-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/nefesh-ai-lifecycle.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/nefesh-ai/refs/heads/main/authentication/nefesh-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/nefesh-ai-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/nefesh-ai/refs/heads/main/conventions/nefesh-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/nefesh-ai-conventions.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/nefesh-ai/refs/heads/main/sandbox/nefesh-ai-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/nefesh-ai-sandbox.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/nefesh-ai/refs/heads/main/plans/nefesh-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/nefesh-ai-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/nefesh-ai/refs/heads/main/rate-limits/nefesh-ai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/nefesh-ai-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/nefesh-ai/refs/heads/main/data-model/nefesh-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/nefesh-ai-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/nefesh-ai/refs/heads/main/asyncapi/nefesh-ai-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/nefesh-ai-webhooks.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/nefesh-ai/refs/heads/main/regulatory/nefesh-ai-regulatory-posture.yml
  title: ''
  type: X-RegulatoryPosture
  url: regulatory/nefesh-ai-regulatory-posture.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/nefesh-ai/refs/heads/main/regulatory/nefesh-ai-regulatory-posture.yml
  title: ''
  type: DataSubjectRequest
  url: regulatory/nefesh-ai-regulatory-posture.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/nefesh-ai/refs/heads/main/regulatory/nefesh-ai-regulatory-posture.yml
  title: ''
  type: DataResidency
  url: regulatory/nefesh-ai-regulatory-posture.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/nefesh-ai/refs/heads/main/security/nefesh-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/nefesh-ai-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://nefesh.ai/.well-known/security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/nefesh-ai/refs/heads/main/security/nefesh-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/nefesh-ai-domain-security.yml
- group: other
  title: ''
  type: X-Robots
  url: https://nefesh.ai/robots.txt
- group: other
  title: ''
  type: X-Sitemap
  url: https://nefesh.ai/sitemap.xml
created: '2026-09-19'
description: 'Nefesh AI (nefesh.ai) sells a B2B "human state" middleware API for AI agents: POST live biometric signals from any device — heart rate and HRV from a chest strap, webcam rPPG, voice tone, facial expression, text sentiment, plus accepted-but-not-yet-fused glucose, EEG, electrodermal, respiratory, movement and sleep fields — to one endpoint (api.nefesh.ai/v1/ingest) and get back a unified stress score (0-100) mapped to five states with a machine-readable suggested_action and a closed-loop adaptation_effectiveness signal. The same capability is exposed four ways: a REST API with webhooks and a device registry, a hosted Streamable-HTTP MCP server (6 tools, two of them keyless self-provisioning) listed on the official MCP Registry, an A2A agent (4 skills) discovered from a card on mcp.nefesh.ai, and a "Cognitive Compute Router" LLM gateway that rewrites system prompt and temperature from the live state for OpenAI- and Anthropic-shaped clients. It also maintains the open Human State
  Protocol (HSP 1.0) JSON Schema and an official npm CLI. Positioned as a General Wellness product, not a medical device. No OpenAPI is published for any surface.'
image: https://nefesh.ai/icon.svg
json_schemas:
- name: Human State Protocol v1.0
  property_count: 15
  slug: nefesh-ai-hsp-1.0.schema
layout: provider
mcp_servers:
- description: ''
  name: Nefesh AI MCP Server
  slug: nefesh-ai-mcp-server
- description: ''
  name: Live Streamable HTTP endpoint
  slug: live-streamable-http-endpoint
modified: '2026-09-19'
name: Nefesh AI
nav: Providers
network: true
overview: 'Nefesh AI publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biometrics, Human State, Stress Detection, and Affective Computing.


  The Nefesh AI catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Nefesh AI''s developer surface includes documentation, API reference, getting-started guide, pricing, signup flow, CLI, authentication, and 33 more developer resources.'
plans:
- name: Nefesh Ai Plans Pricing
  plan_count: 3
  slug: nefesh-ai-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 5
  name: Nefesh Ai Rate Limits
  slug: nefesh-ai-rate-limits
score:
  band: strong
  composite: 63.5
  coverage:
    artifact_dirs: 19
    catalog_earned: 70.0
    catalog_earned_first_party: 24.0
    catalog_gap: 45.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 49.4
    developer_ergonomics: 64.3
    discoverability: 81.5
    operational_transparency: 55.3
  previous_composite: 63.5
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 45.0
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Nefesh Ai Authentication
  slug: nefesh-ai-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Nefesh Ai Domain Security
  slug: nefesh-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Nefesh Ai Vulnerability Disclosure
  slug: nefesh-ai-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: nefesh-ai
tags:
- Company
- Biometrics
- Human State
- Stress Detection
- Affective Computing
- AI Agents
- MCP
- A2A
- LLM Gateway
- Wearables
- Digital Health
- Middleware
website: https://nefesh.ai/
---
