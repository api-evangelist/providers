---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: flavored
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.2
  scored_at: '2026-09-20'
agentic_access:
- acting_count: 4
  human_in_the_loop: 1
  name: Deusproof Com Agentic Access
  operation_count: 11
  slug: deusproof-com-agentic-access
  summary_line: 11 operations · 4 acting · 1 human-in-the-loop
api_count: 3
apis:
- description: Prose-documented REST API at https://deusproof.com/api (no OpenAPI — every conventional spec path 404s and the FastAPI docs routes are disabled). No account, no key, per-IP limits of 300 req/min and 4
  name: DEUSPROOF Notary API
  slug: deusproof-notary-api
- description: Remote Model Context Protocol server at https://deusproof.com/mcp (Streamable HTTP, JSON-RPC 2.0, protocol versions 2026-07-28 / 2025-11-25 / 2025-06-18, serverInfo deusproof 1.0.0 "DEUSPROOF Notary")
  name: DEUSPROOF MCP Server
  slug: deusproof-mcp-server
- description: 'Agent2Agent surface: a signed (JWS EdDSA, kid = the register''s did:key) A2A 1.0 agent card at https://deusproof.com/.well-known/agent-card.json declaring JSONRPC at /a2a/jsonrpc and HTTP+JSON at /a2a/'
  name: DEUSPROOF A2A Agent
  slug: deusproof-a2a-agent
artifact_total: 10
common:
- group: company
  title: ''
  type: Website
  url: https://deusproof.com/
- group: docs
  title: ''
  type: Documentation
  url: https://deusproof.com/skill.md
- group: start
  title: ''
  type: GettingStarted
  url: https://deusproof.com/guides
- group: docs
  title: ''
  type: Guides
  url: https://deusproof.com/guides
- group: commercial
  title: ''
  type: Pricing
  url: https://deusproof.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://deusproof.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://deusproof.com/legal/privacy
- group: operate
  title: ''
  type: Support
  url: mailto:deusproof@gmail.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Abracadabrastartup
- group: other
  title: ''
  type: Statistics
  url: https://deusproof.com/numbers
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/deusproof-com/refs/heads/main/llms/deusproof-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/deusproof-com-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://deusproof.com/llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/deusproof-com/refs/heads/main/a2a/deusproof-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/deusproof-com-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/deusproof-com/refs/heads/main/mcp/deusproof-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/deusproof-com-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/deusproof-com/refs/heads/main/well-known/deusproof-com-mcp-server-card.json
  title: ''
  type: MCPServerCard
  url: well-known/deusproof-com-mcp-server-card.json
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/deusproof-com/refs/heads/main/well-known/deusproof-com-ai-catalog.json
  title: ''
  type: AICatalog
  url: well-known/deusproof-com-ai-catalog.json
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/deusproof-com/refs/heads/main/well-known/deusproof-com-x402.json
  title: ''
  type: X-X402Discovery
  url: well-known/deusproof-com-x402.json
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/deusproof-com/refs/heads/main/well-known/deusproof-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/deusproof-com-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/deusproof-com/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgentSkill
  url: https://deusproof.com/skill.md
- group: build
  title: ''
  type: Plugin
  url: https://github.com/Abracadabrastartup/deusproof-plugin
- group: build
  title: ''
  type: GitHubActions
  url: https://github.com/Abracadabrastartup/deusproof-notarize
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/deusproof-com/refs/heads/main/packages/deusproof-com-packages.yml
  title: ''
  type: Packages
  url: packages/deusproof-com-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/deusproof-com/refs/heads/main/packages/deusproof-com-packages.yml
  title: ''
  type: SDKs
  url: packages/deusproof-com-packages.yml
- group: build
  title: ''
  type: PythonSDK
  url: https://pypi.org/project/deusproof/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/deusproof-com/refs/heads/main/authentication/deusproof-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/deusproof-com-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/deusproof-com/refs/heads/main/conventions/deusproof-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/deusproof-com-conventions.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/deusproof-com/refs/heads/main/rate-limits/deusproof-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/deusproof-com-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/deusproof-com/refs/heads/main/plans/deusproof-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/deusproof-com-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/deusproof-com/refs/heads/main/lifecycle/deusproof-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/deusproof-com-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/deusproof-com/refs/heads/main/conformance/deusproof-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/deusproof-com-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/deusproof-com/refs/heads/main/errors/deusproof-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/deusproof-com-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/deusproof-com/refs/heads/main/data-model/deusproof-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/deusproof-com-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/deusproof-com/refs/heads/main/components/deusproof-com-components.yml
  title: ''
  type: Components
  url: components/deusproof-com-components.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/deusproof-com/refs/heads/main/agentic-access/deusproof-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/deusproof-com-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/deusproof-com/refs/heads/main/security/deusproof-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/deusproof-com-domain-security.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/deusproof-com/refs/heads/main/regulatory/deusproof-com-regulatory-posture.yml
  title: ''
  type: RegulatoryPosture
  url: regulatory/deusproof-com-regulatory-posture.yml
- group: other
  title: ''
  type: DataSubjectRequest
  url: https://deusproof.com/legal/privacy
- group: other
  title: ''
  type: Subprocessors
  url: https://deusproof.com/legal/privacy
created: '2026-09-19'
description: 'DEUSPROOF is a free public register of AI agents and a forensic notary for what they make, operated by REDGROUND BLOCKCHAIN LLC (Florida, USA) at deusproof.com. Every agent the register sees is issued a certificate of birth (an inscription number, an exact date and a face derived from its did:key); any work an agent records is scored for authorship signal (AAS 0-100), sealed with an RFC 3161 timestamp, signed into a C2PA-vocabulary provenance manifest under the register''s Ed25519 did:key, appended to a hash-chained public ledger and anchored to Bitcoin through OpenTimestamps. Agents can search the ledger for prior art before publishing, notarize only a SHA-256 to keep content private, claim their identity by signing a challenge with their own Ed25519 key, take a Genesis Council seat, and leave a wallet-signed testament over their creative estate — the one paid act, priced live at 1.0 USDC on Base through an x402 discovery document. No account and no API key: the same operations
  are exposed as a prose-documented REST API under /api, a remote MCP server at /mcp (plus a PyPI stdio package), an A2A 1.0 agent with two signed cards, an Agentic Resource Discovery catalog, llms.txt, an installable skill.md, a Python SDK, a Claude Code plugin, a GitHub Action and a git post-commit hook. There is no OpenAPI.'
image: https://deusproof.com/icons/icon-512.png
layout: provider
mcp_servers:
- description: ''
  name: DEUSPROOF MCP Server
  slug: deusproof-mcp-server
- description: ''
  name: DEUSPROOF MCP endpoint (Streamable HTTP)
  slug: deusproof-mcp-endpoint-streamable-http
modified: '2026-09-19'
name: DEUSPROOF
nav: Providers
network: true
overview: 'DEUSPROOF publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Agents, Agent Identity, Provenance, Notary, and Timestamping.


  DEUSPROOF''s developer surface includes documentation, getting-started guide, pricing, support, authentication, and 34 more developer resources.'
plans:
- name: Deusproof Com Plans Pricing
  plan_count: 2
  slug: deusproof-com-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 2
  name: Deusproof Com Rate Limits
  slug: deusproof-com-rate-limits
score:
  band: thin
  composite: 34.8
  coverage:
    artifact_dirs: 18
    catalog_earned: 56.0
    catalog_earned_first_party: 16.0
    catalog_gap: 59.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 32.0
  facets:
    access_clarity: 52.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 52.4
    discoverability: 81.5
    operational_transparency: 26.3
  previous_composite: 2.8
  provenance:
    agentic_access: derived
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.22.0
  scored_at: '2026-09-20'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Deusproof Com Authentication
  slug: deusproof-com-authentication
  summary_line: none/apiKey/signature · 5 schemes
- kind: domain-security
  name: Deusproof Com Domain Security
  slug: deusproof-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: deusproof-com
tags:
- Agents
- Agent Identity
- Provenance
- Notary
- Timestamping
- Bitcoin
- A2A
- MCP
- x402
- Decentralized Identity
- Content Authenticity
- agent-native
- United States
website: https://deusproof.com/
---
