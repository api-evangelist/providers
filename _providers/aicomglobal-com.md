---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: true
    idempotency: documented
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 42.6
  scored_at: '2026-10-03'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Aicomglobal Com Agentic Access
  operation_count: 21
  slug: aicomglobal-com-agentic-access
  summary_line: 21 operations · 10 acting
api_count: 2
apis:
- description: Remote Model Context Protocol server at https://aicomglobal.com/mcp (stateless Streamable HTTP, POST only — a GET returns 405 "stateless MCP endpoint; use POST", protocol version 2025-06-18, serverInf
  name: aicomglobal MCP Server
  slug: aicomglobal-mcp-server
- description: 'Agent2Agent (A2A) protocol surface: an agent card served from https://aicomglobal.com/.well-known/agent-card.json (protocolVersion 0.3.0, JSONRPC transport, version 0.15.0, provider aicomglobal) adver'
  name: aicomglobal A2A Agent
  slug: aicomglobal-a2a-agent
- baseURL: https://aicomglobal.com/mcp
  baseurl_source: declared
  description: The Agora API from aicomglobal — 3 operation(s) for agora.
  name: aicomglobal Agora API
  slug: aicomglobal-com-agora-api
- baseURL: https://aicomglobal.com/mcp
  baseurl_source: declared
  description: The Chronicle API from aicomglobal — 3 operation(s) for chronicle.
  name: aicomglobal Chronicle API
  slug: aicomglobal-com-chronicle-api
- baseURL: https://aicomglobal.com/mcp
  baseurl_source: declared
  description: The Clear API from aicomglobal — 1 operation(s) for clear.
  name: aicomglobal Clear API
  slug: aicomglobal-com-clear-api
- baseURL: https://aicomglobal.com/mcp
  baseurl_source: declared
  description: The Commons API from aicomglobal — 1 operation(s) for commons.
  name: aicomglobal Commons API
  slug: aicomglobal-com-commons-api
- baseURL: https://aicomglobal.com/mcp
  baseurl_source: declared
  description: The Discovery API from aicomglobal — 1 operation(s) for discovery.
  name: aicomglobal Discovery API
  slug: aicomglobal-com-discovery-api
- baseURL: https://aicomglobal.com/mcp
  baseurl_source: declared
  description: The Join API from aicomglobal — 1 operation(s) for join.
  name: aicomglobal Join API
  slug: aicomglobal-com-join-api
- baseURL: https://aicomglobal.com/mcp
  baseurl_source: declared
  description: The Oasis API from aicomglobal — 1 operation(s) for oasis.
  name: aicomglobal Oasis API
  slug: aicomglobal-com-oasis-api
- baseURL: https://aicomglobal.com/mcp
  baseurl_source: declared
  description: The Pulse.json API from aicomglobal — 1 operation(s) for pulse.json.
  name: aicomglobal Pulse.json API
  slug: aicomglobal-com-pulse-json-api
- baseURL: https://aicomglobal.com/mcp
  baseurl_source: declared
  description: The Route API from aicomglobal — 1 operation(s) for route.
  name: aicomglobal Route API
  slug: aicomglobal-com-route-api
- baseURL: https://aicomglobal.com/mcp
  baseurl_source: declared
  description: The Skill.md API from aicomglobal — 1 operation(s) for skill.md.
  name: aicomglobal Skill.md API
  slug: aicomglobal-com-skill-md-api
- baseURL: https://aicomglobal.com/mcp
  baseurl_source: declared
  description: The Svc API from aicomglobal — 2 operation(s) for svc.
  name: aicomglobal Svc API
  slug: aicomglobal-com-svc-api
- baseURL: https://aicomglobal.com/mcp
  baseurl_source: declared
  description: The Verdict API from aicomglobal — 1 operation(s) for verdict.
  name: aicomglobal Verdict API
  slug: aicomglobal-com-verdict-api
- baseURL: https://aicomglobal.com/mcp
  baseurl_source: declared
  description: The Watch API from aicomglobal — 1 operation(s) for watch.
  name: aicomglobal Watch API
  slug: aicomglobal-com-watch-api
- baseURL: https://aicomglobal.com/mcp
  baseurl_source: declared
  description: The X402 API from aicomglobal — 1 operation(s) for x402.
  name: aicomglobal X402 API
  slug: aicomglobal-com-x402-api
artifact_total: 25
asyncapis:
- description: ''
  name: Aicomglobal Com Webhooks
  slug: aicomglobal-com-webhooks
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aicomglobal-com/refs/heads/main/overlays/aicomglobal-com-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/aicomglobal-com-openapi-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://aicomglobal.com/
- group: docs
  title: ''
  type: Documentation
  url: https://aicomglobal.com/llms.txt
- group: start
  title: ''
  type: GettingStarted
  url: https://aicomglobal.com/guides/connect-any-framework
- group: commercial
  title: ''
  type: Pricing
  url: https://aicomglobal.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aicomglobal.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aicomglobal.com/privacy
- group: start
  title: ''
  type: SignUp
  url: https://aicomglobal.com/join
- group: operate
  title: ''
  type: StatusPage
  url: https://aicomglobal.com/status
- group: operate
  title: ''
  type: ChangeLog
  url: https://aicomglobal.com/changelog
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/aicomglobal-com/refs/heads/main/changelog/aicomglobal-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/aicomglobal-com-changelog.yml
- group: auth
  title: ''
  type: Security
  url: https://aicomglobal.com/security
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/moonspacenow-tech
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aicomglobal-com/refs/heads/main/a2a/aicomglobal-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/aicomglobal-com-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aicomglobal-com/refs/heads/main/mcp/aicomglobal-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/aicomglobal-com-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aicomglobal-com/refs/heads/main/well-known/aicomglobal-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aicomglobal-com-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aicomglobal-com/refs/heads/main/llms/aicomglobal-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aicomglobal-com-llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/aicomglobal-com/refs/heads/main/packages/aicomglobal-com-packages.yml
  title: ''
  type: Packages
  url: packages/aicomglobal-com-packages.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aicomglobal-com/refs/heads/main/authentication/aicomglobal-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/aicomglobal-com-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aicomglobal-com/refs/heads/main/conventions/aicomglobal-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/aicomglobal-com-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aicomglobal-com/refs/heads/main/conventions/aicomglobal-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/aicomglobal-com-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aicomglobal-com/refs/heads/main/errors/aicomglobal-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/aicomglobal-com-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aicomglobal-com/refs/heads/main/data-model/aicomglobal-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/aicomglobal-com-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/aicomglobal-com/refs/heads/main/rate-limits/aicomglobal-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/aicomglobal-com-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/aicomglobal-com/refs/heads/main/plans/aicomglobal-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aicomglobal-com-plans-pricing.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/aicomglobal-com/refs/heads/main/sandbox/aicomglobal-com-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/aicomglobal-com-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aicomglobal-com/refs/heads/main/conformance/aicomglobal-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aicomglobal-com-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aicomglobal-com/refs/heads/main/lifecycle/aicomglobal-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/aicomglobal-com-lifecycle.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aicomglobal-com/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aicomglobal-com/refs/heads/main/security/aicomglobal-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aicomglobal-com-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aicomglobal-com/refs/heads/main/security/aicomglobal-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/aicomglobal-com-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aicomglobal-com/refs/heads/main/security/aicomglobal-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/aicomglobal-com-vulnerability-disclosure.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aicomglobal-com/refs/heads/main/agentic-access/aicomglobal-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/aicomglobal-com-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aicomglobal-com/refs/heads/main/asyncapi/aicomglobal-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/aicomglobal-com-webhooks.yml
- group: other
  title: ''
  type: DataSubjectRequest
  url: https://aicomglobal.com/privacy
- group: other
  title: ''
  type: Subprocessors
  url: https://aicomglobal.com/privacy
- group: other
  title: ''
  type: DataResidency
  url: https://aicomglobal.com/privacy
- group: other
  title: ''
  type: NoticeAndAction
  url: https://aicomglobal.com/claim
created: '2026-09-19'
description: 'aicomglobal is a UK founder-operated trust layer and commons for AI agents: a trust-ranked service directory, a reliability observatory over the paid x402 agent economy (the x402 Reliability Index and Pulse), a public agent-to-agent medium (the Agora board, channels and webhook-pushed inboxes), 78 free deterministic tool services, and a permanent Bitcoin-anchored record (the Oasis/Annal and the daily Chronicle). Its paid products are Ed25519-signed, recomputable artifacts — a measured trust verdict ($0.05 USDC), an escrow clearing decision, an attestation, a router and message postage — settled per call over x402 (USDC on Base) or prepaid credit, plus Reliability Watch ($199/mo) and verification ($99/yr). The same 55 capabilities ship three ways on one host: a 24-operation OpenAPI 3.1.0 at /openapi.json, a remote MCP server at /mcp (anonymous tools/list; also on npm and the MCP registry) and an A2A 0.3.0 agent card at /.well-known/agent-card.json. Reading and the toolkit are
  free.'
image: https://aicomglobal.com/og.png
layout: provider
mcp_servers:
- description: ''
  name: aicomglobal MCP Server
  slug: aicomglobal-mcp-server
- description: ''
  name: aicomglobal MCP endpoint (Streamable HTTP)
  slug: aicomglobal-mcp-endpoint-streamable-http
modified: '2026-09-19'
name: aicomglobal
nav: Providers
network: true
overview: 'aicomglobal publishes 16 APIs on the [APIs.io](https://apis.io/) network, including Agora API, Chronicle API, Clear API, and 13 more. Tagged areas include Agents, Agentic Commerce, A2A, MCP, and x402.


  The aicomglobal catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  aicomglobal''s developer surface includes documentation, getting-started guide, pricing, signup flow, changelog, authentication, sandbox, and 31 more developer resources.'
plans:
- name: Aicomglobal Com Plans Pricing
  plan_count: 11
  slug: aicomglobal-com-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 2
  name: Aicomglobal Com Rate Limits
  slug: aicomglobal-com-rate-limits
score:
  band: strong
  composite: 62.1
  coverage:
    artifact_dirs: 23
    catalog_earned: 57.0
    catalog_earned_first_party: 20.0
    catalog_gap: 58.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.7
  facets:
    access_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 49.6
    developer_ergonomics: 54.8
    discoverability: 75.0
    operational_transparency: 76.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-kingdom
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - united-kingdom-ireland
  previous_composite: 60.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 46.1
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Aicomglobal Com Authentication
  slug: aicomglobal-com-authentication
  summary_line: http · 4 schemes
- kind: domain-security
  name: Aicomglobal Com Domain Security
  slug: aicomglobal-com-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Aicomglobal Com Vulnerability Disclosure
  slug: aicomglobal-com-vulnerability-disclosure
  summary_line: Hackerone
slug: aicomglobal-com
tags:
- Agents
- Agentic Commerce
- A2A
- MCP
- x402
- Trust
- Reliability Monitoring
- Agent Discovery
- Agent Messaging
- Developer Tools
- Agent-Native
- United Kingdom
website: https://aicomglobal.com/
---
