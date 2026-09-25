---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: true
    agentic_access: derived
    agentic_commerce: self
    auth_clarity: bearer
    consent_identity: true
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: documented
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 61.4
  scored_at: '2026-09-24'
agentic_access:
- acting_count: 34
  human_in_the_loop: 0
  name: Scvd Store Agentic Access
  operation_count: 196
  slug: scvd-store-agentic-access
  summary_line: 196 operations · 34 acting
api_count: 3
apis:
- baseURL: https://scvd.store
  baseurl_source: declared
  description: 'The HTTP contract for scvd.store: 196 operations on 180 paths (OpenAPI 3.1.0, every operation with a unique operationId and summary) covering the free x402 instruments (POST /api/preflight/v1 and /v2,'
  name: SCVD General Store API
  slug: scvd-general-store-api
- description: Three remote Model Context Protocol servers on the apex host, all Streamable HTTP and all answering initialize, tools/list and resources/list anonymously at protocol version 2025-06-18 (serverInfo 0.5
  name: SCVD General Store MCP Servers
  slug: scvd-mcp-servers
- description: 'Agent2Agent protocol surface: an agent card served from https://scvd.store/.well-known/agent-card.json (and byte-identically at /.well-known/agent.json and /.well-known/a2a.json; protocolVersion 0.3.0'
  name: SCVD Evidence Agent (A2A)
  slug: scvd-evidence-agent
artifact_total: 15
asyncapis:
- description: ''
  name: Scvd Store Webhooks
  slug: scvd-store-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://scvd.store/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://scvd.store/developers
- group: docs
  title: ''
  type: Documentation
  url: https://scvd.store/developers
- group: docs
  title: ''
  type: APIReference
  url: https://scvd.store/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://scvd.store/agents.md
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/scvd-store/refs/heads/main/sandbox/scvd-store-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/scvd-store-sandbox.yml
- group: start
  title: ''
  type: Sandbox
  url: https://scvd.store/try
- group: commercial
  title: ''
  type: Pricing
  url: https://scvd.store/pricing
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/scvd-store/refs/heads/main/plans/scvd-store-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/scvd-store-plans-pricing.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://scvd.store/rights
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://scvd.store/privacy
- group: operate
  title: ''
  type: Support
  url: https://scvd.store/what
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/seancrecord
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/seancrecord/scvd-general-store-repo
- group: operate
  title: ''
  type: Roadmap
  url: https://github.com/seancrecord/scvd-general-store-repo/blob/main/ROADMAP.md
- group: operate
  title: ''
  type: StatusPage
  url: https://scvd.store/.well-known/liveness.json
- group: operate
  title: ''
  type: Deprecation
  url: https://scvd.store/deprecation
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/scvd-store/refs/heads/main/lifecycle/scvd-store-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/scvd-store-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/scvd-store/refs/heads/main/changelog/scvd-store-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/scvd-store-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://scvd.store/feeds/corrections.xml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/scvd-store/refs/heads/main/llms/scvd-store-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/scvd-store-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://scvd.store/llms.txt
- group: other
  title: ''
  type: AgentsMd
  url: https://scvd.store/agents.md
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/scvd-store/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgentSkill
  url: https://scvd.store/skill.md
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/scvd-store/refs/heads/main/a2a/scvd-store-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/scvd-store-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/scvd-store/refs/heads/main/mcp/scvd-store-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/scvd-store-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/scvd-store/refs/heads/main/mcp/scvd-store-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/scvd-store-tool-crosswalk.yml
- group: agent
  title: ''
  type: WebMCP
  url: https://scvd.store/webmcp.js
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/scvd-store/refs/heads/main/well-known/scvd-store-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/scvd-store-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/scvd-store/refs/heads/main/well-known/scvd-store-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/scvd-store-security.txt
- group: auth
  title: ''
  type: Security
  url: https://scvd.store/.well-known/security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/scvd-store/refs/heads/main/security/scvd-store-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/scvd-store-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/scvd-store/refs/heads/main/security/scvd-store-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/scvd-store-trust-center.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://scvd.store/trust
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/scvd-store/refs/heads/main/security/scvd-store-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/scvd-store-domain-security.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/scvd-store/refs/heads/main/well-known/scvd-store-api-catalog.json
  title: ''
  type: APICatalog
  url: well-known/scvd-store-api-catalog.json
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/scvd-store/refs/heads/main/well-known/scvd-store-ai-plugin.json
  title: ''
  type: AIPlugin
  url: well-known/scvd-store-ai-plugin.json
- group: other
  title: ''
  type: ContentSignal
  url: https://scvd.store/robots.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/scvd-store/refs/heads/main/well-known/scvd-store-agent-instructions.json
  title: ''
  type: AgentInstructions
  url: well-known/scvd-store-agent-instructions.json
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/scvd-store/refs/heads/main/well-known/scvd-store-x402.json
  title: ''
  type: X402
  url: well-known/scvd-store-x402.json
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/scvd-store/refs/heads/main/well-known/scvd-store-ucp.json
  title: ''
  type: UCP
  url: well-known/scvd-store-ucp.json
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/scvd-store/refs/heads/main/well-known/scvd-store-ard.json
  title: ''
  type: ARD
  url: well-known/scvd-store-ard.json
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/scvd-store/refs/heads/main/authentication/scvd-store-authentication.yml
  title: ''
  type: Authentication
  url: authentication/scvd-store-authentication.yml
- group: auth
  title: ''
  type: Authentication
  url: https://scvd.store/auth.md
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/scvd-store/refs/heads/main/conventions/scvd-store-conventions.yml
  title: ''
  type: Conventions
  url: conventions/scvd-store-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/scvd-store/refs/heads/main/conventions/scvd-store-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/scvd-store-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/scvd-store/refs/heads/main/errors/scvd-store-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/scvd-store-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/scvd-store/refs/heads/main/errors/scvd-store-defects.json
  title: ''
  type: ErrorCatalog
  url: errors/scvd-store-defects.json
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/scvd-store/refs/heads/main/rate-limits/scvd-store-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/scvd-store-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/scvd-store/refs/heads/main/conformance/scvd-store-conformance.yml
  title: ''
  type: Conformance
  url: conformance/scvd-store-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/scvd-store/refs/heads/main/asyncapi/scvd-store-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/scvd-store-webhooks.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/scvd-store/refs/heads/main/packages/scvd-store-packages.yml
  title: ''
  type: Packages
  url: packages/scvd-store-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/scvd-store/refs/heads/main/packages/scvd-store-packages.yml
  title: ''
  type: SDKs
  url: packages/scvd-store-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/scvd-store/refs/heads/main/cli/scvd-store-cli.yml
  title: ''
  type: CLI
  url: cli/scvd-store-cli.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/scvd-store/refs/heads/main/components/scvd-store-components.yml
  title: ''
  type: Components
  url: components/scvd-store-components.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/scvd-store/refs/heads/main/data-model/scvd-store-data-model.yml
  title: ''
  type: DataModel
  url: data-model/scvd-store-data-model.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/scvd-store/refs/heads/main/agentic-access/scvd-store-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/scvd-store-agentic-access.yml
- group: other
  title: ''
  type: Subprocessors
  url: https://scvd.store/stack
- group: other
  title: ''
  type: DataSubjectRequest
  url: https://scvd.store/privacy
- group: operate
  title: ''
  type: SupportLifetime
  url: https://scvd.store/deprecation
- group: other
  title: ''
  type: ExitAssistance
  url: https://scvd.store/wind-down
created: '2026-09-19'
description: 'Record Creative Co. LLC is the one-person Oak City, North Carolina company that operates scvd.store — "Sean-Claude Van Damme''s General Store", an evidence observatory for agentic commerce and a general store for AI agents. It independently verifies x402 payment endpoints, signed offers and receipts: a free preflight that checks whether any x402 door serves a well-formed, payable v2 challenge, a free conformance desk for any issuer''s JWS-signed offers and receipts, a named 31-class defect vocabulary, and a weekly Bitcoin-anchored, hash-chained corpus of the public x402 web. Paid instruments (35 doors from $0.001 to $1,500) — settlement attestations, endpoint watches, launch checks, conformance audits, A2A repair kits, agent memory anchors and the labor of a named human — are bought per call in USDC over x402 v2 on Base, Polygon, Arbitrum, World or Solana with no account, key or signup; every purchase ends in an Ed25519-signed artifact verifiable free forever. One host publishes
  the whole surface: a 196-operation OpenAPI 3.1 contract, three remote MCP servers (20 tools, MCP Apps cards), an A2A 0.3.0 agent card, a UCP business profile, an RFC 9727 API catalog, RFC 9728 protected-resource metadata, llms.txt, agents.md, SKILL.md files, an official CLI and nine more open-source packages.'
image: https://scvd.store/og.png
layout: provider
mcp_servers:
- description: ''
  name: SCVD General Store MCP Server
  slug: scvd-general-store-mcp-server
- description: ''
  name: SCVD General Store MCP endpoint (Streamable HTTP)
  slug: scvd-general-store-mcp-endpoint-streamable-http
- description: ''
  name: SCVD x402 Verifier MCP endpoint
  slug: scvd-x402-verifier-mcp-endpoint
- description: ''
  name: SCVD Store Docs MCP endpoint
  slug: scvd-store-docs-mcp-endpoint
modified: '2026-09-19'
name: SCVD General Store
nav: Providers
network: true
overview: 'SCVD General Store publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Agents, Agentic Commerce, x402, Payments, and Micropayments.


  The SCVD General Store catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  SCVD General Store''s developer surface includes documentation, API reference, getting-started guide, sandbox, pricing, support, changelog, and 55 more developer resources.'
plans:
- name: Scvd Store Plans Pricing
  plan_count: 35
  slug: scvd-store-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 3
  name: Scvd Store Rate Limits
  slug: scvd-store-rate-limits
score:
  band: exemplar
  composite: 72.6
  coverage:
    artifact_dirs: 24
    catalog_earned: 64.0
    catalog_earned_first_party: 24.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 71.1
    contract_governance: 18.2
    contract_quality: 57.7
    developer_ergonomics: 83.3
    discoverability: 92.6
    operational_transparency: 100.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 72.6
  provenance:
    agentic_access: derived
    conformance: first-party
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 56.3
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Scvd Store Authentication
  slug: scvd-store-authentication
  summary_line: none (anonymous)/x402 payment signature (per-call)/http bearer (one narrow scope)/http basic (back office, not for agents) · 5 schemes
- kind: domain-security
  name: Scvd Store Domain Security
  slug: scvd-store-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Scvd Store Vulnerability Disclosure
  slug: scvd-store-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Scvd Store Trust Center
  slug: scvd-store-trust-center
  summary_line: trust center published
slug: scvd-store
tags:
- Agents
- Agentic Commerce
- x402
- Payments
- Micropayments
- Stablecoins
- USDC
- Verification
- Conformance
- Attestation
- Observability
- MCP
- A2A
- Universal Commerce Protocol
- Signatures
- Agent-Native
- United States
website: https://scvd.store/
---
