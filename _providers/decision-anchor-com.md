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
    error_semantics: verified
    event_surface_described: false
    idempotency: documented
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 48.4
  scored_at: '2026-09-23'
agentic_access:
- acting_count: 50
  human_in_the_loop: 1
  name: Decision Anchor Com Agentic Access
  operation_count: 116
  slug: decision-anchor-com-agentic-access
  summary_line: 116 operations · 50 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.decision-anchor.com
  baseurl_source: declared
  description: 'REST API for the External Anchoring Layer: agent self-registration (no auth; issues a bearer auth_token, a recovery_key and a 500 DAC / 30-day Trial), Decision Declarations with an Execution Envelope '
  name: Decision Anchor API
  slug: decision-anchor-api
- description: Remote Model Context Protocol server at https://mcp.decision-anchor.com/mcp (Streamable HTTP, POST only, protocol version 2025-06-18, serverInfo Decision Anchor 1.3.42). initialize and tools/list answ
  name: Decision Anchor MCP Server
  slug: decision-anchor-mcp-server
- description: 'Agent2Agent protocol surface: a signed agent card (protocolVersion 1.0, JSONRPC, version 1.3.42, Ed25519 JWKS at /.well-known/jwks.json) served from https://a2a.decision-anchor.com/.well-known/agent-c'
  name: Decision Anchor A2A Agent
  slug: decision-anchor-a2a-agent
artifact_total: 11
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/decision-anchor-com/refs/heads/main/agentic-access/decision-anchor-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/decision-anchor-com-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://decision-anchor.com/
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/zse4321/decision-anchor-sdk/blob/main/AGENTS.md
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/zse4321/decision-anchor-sdk/blob/main/AGENTS.md#getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://api.decision-anchor.com/openapi.json
- group: company
  title: ''
  type: Blog
  url: https://decision-anchor.com/blog/
- group: operate
  title: ''
  type: ChangeLog
  url: https://decision-anchor.com/changelog/
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/decision-anchor-com/refs/heads/main/changelog/decision-anchor-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/decision-anchor-com-changelog.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://api.decision-anchor.com/v1/pricing/current
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/decision-anchor-com/refs/heads/main/plans/decision-anchor-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/decision-anchor-com-plans-pricing.yml
- group: build
  title: ''
  type: SDK
  url: https://github.com/zse4321/decision-anchor-sdk
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/zse4321/decision-anchor-sdk
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/decision-anchor-com/refs/heads/main/packages/decision-anchor-com-packages.yml
  title: ''
  type: SDKs
  url: packages/decision-anchor-com-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/decision-anchor-com/refs/heads/main/packages/decision-anchor-com-packages.yml
  title: ''
  type: Packages
  url: packages/decision-anchor-com-packages.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/decision-anchor-com/refs/heads/main/a2a/decision-anchor-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/decision-anchor-com-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/decision-anchor-com/refs/heads/main/mcp/decision-anchor-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/decision-anchor-com-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/decision-anchor-com/refs/heads/main/mcp/decision-anchor-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/decision-anchor-com-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/decision-anchor-com/refs/heads/main/well-known/decision-anchor-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/decision-anchor-com-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/decision-anchor-com/refs/heads/main/well-known/decision-anchor-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/decision-anchor-com-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/decision-anchor-com/refs/heads/main/security/decision-anchor-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/decision-anchor-com-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/decision-anchor-com/refs/heads/main/security/decision-anchor-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/decision-anchor-com-vulnerability-disclosure.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/decision-anchor-com/refs/heads/main/llms/decision-anchor-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/decision-anchor-com-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://api.decision-anchor.com/llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/decision-anchor-com/refs/heads/main/authentication/decision-anchor-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/decision-anchor-com-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/decision-anchor-com/refs/heads/main/conventions/decision-anchor-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/decision-anchor-com-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/decision-anchor-com/refs/heads/main/conventions/decision-anchor-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/decision-anchor-com-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/decision-anchor-com/refs/heads/main/errors/decision-anchor-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/decision-anchor-com-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/decision-anchor-com/refs/heads/main/data-model/decision-anchor-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/decision-anchor-com-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/decision-anchor-com/refs/heads/main/rate-limits/decision-anchor-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/decision-anchor-com-rate-limits.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/decision-anchor-com/refs/heads/main/sandbox/decision-anchor-com-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/decision-anchor-com-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/decision-anchor-com/refs/heads/main/conformance/decision-anchor-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/decision-anchor-com-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/decision-anchor-com/refs/heads/main/lifecycle/decision-anchor-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/decision-anchor-com-lifecycle.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/decision-anchor-com/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/decision-anchor-com/refs/heads/main/security/decision-anchor-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/decision-anchor-com-domain-security.yml
- group: other
  title: ''
  type: DataSubjectRequest
  url: https://api.decision-anchor.com/openapi.json
created: '2026-09-19'
description: 'Decision Anchor (디시전앵커) is the "External Anchoring Layer" for AI agents: a paid, content-blind service that records that an agent made a decision — when, at what accountability scope, before or after an irreversible action such as a payment, a delegation or an agreement with another agent — in a place neither the agent nor its platform controls, so that a later dispute has a record that is not either side''s own log. It deliberately does not judge, score, rank, monitor or intervene, and does not store decision content. The same environment is exposed three ways from three hosts: a 116-operation OpenAPI 3.0.3 REST API at api.decision-anchor.com (register-then-bearer auth, x402 v2 payments in USDC on Base with a free 500 DAC / 30-day trial), a 30-tool remote MCP server at mcp.decision-anchor.com listed in the official MCP registry, and a signed A2A 1.0 agent card on a2a.decision-anchor.com with six skills. It also publishes llms.txt, an RFC 9116 security.txt, an x402 discovery
  document, a machine-readable price list, a Node.js SDK and a 179-entry public defect changelog since launch on 2026-04-02.'
layout: provider
mcp_servers:
- description: ''
  name: Decision Anchor MCP Server
  slug: decision-anchor-mcp-server
- description: ''
  name: Decision Anchor MCP endpoint (Streamable HTTP)
  slug: decision-anchor-mcp-endpoint-streamable-http
modified: '2026-09-19'
name: Decision Anchor
nav: Providers
network: true
overview: 'Decision Anchor publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Agents, Agent Accountability, Decision Records, Audit Trail, and A2A.


  Decision Anchor''s developer surface includes documentation, getting-started guide, API reference, engineering blog, changelog, pricing, SDKs, and 28 more developer resources.'
plans:
- name: Decision Anchor Com Plans Pricing
  plan_count: 3
  slug: decision-anchor-com-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 2
  name: Decision Anchor Com Rate Limits
  slug: decision-anchor-com-rate-limits
score:
  band: developing
  composite: 49.0
  coverage:
    artifact_dirs: 21
    catalog_earned: 55.0
    catalog_earned_first_party: 20.0
    catalog_gap: 60.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 48.8
    developer_ergonomics: 64.3
    discoverability: 72.2
    operational_transparency: 52.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - south-korea
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - japan-korea
  previous_composite: 49.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: first-party
  schema_version: 0.22.0
  scored_at: '2026-09-23'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Decision Anchor Com Authentication
  slug: decision-anchor-com-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Decision Anchor Com Domain Security
  slug: decision-anchor-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Decision Anchor Com Vulnerability Disclosure
  slug: decision-anchor-com-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: decision-anchor-com
tags:
- Agents
- Agent Accountability
- Decision Records
- Audit Trail
- A2A
- MCP
- x402
- Agentic Commerce
- Multi-Agent Systems
- Agent-Native
- South Korea
website: https://decision-anchor.com/
---
