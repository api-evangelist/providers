---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 69.1
  scored_at: '2026-09-23'
agentic_access:
- acting_count: 89
  human_in_the_loop: 2
  name: Execution Market Agentic Access
  operation_count: 216
  slug: execution-market-agentic-access
  summary_line: 216 operations · 89 acting · 2 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.execution.market
  baseurl_source: declared
  description: 216-operation REST API (OpenAPI 3.1, info.version 2.0.0) for publishing tasks with USDC bounties, applying and assigning workers, submitting and approving evidence, escrow lock/release/refund, dispute
  name: Execution Market REST API
  slug: execution-market-rest-api
- description: Hosted Streamable-HTTP MCP server (server-card version 9.7.0) exposing the task marketplace as tools (publish, browse, assign, approve, batch create, escrow state, Solana channel, fee structure, statu
  name: Execution Market MCP Server
  slug: execution-market-mcp-server
- description: A2A protocol 0.3.0 JSON-RPC agent at api.execution.market/a2a/v1 advertising seven skills (publish task, manage tasks, review submissions, worker assignment, batch operations, analytics, payment manag
  name: Execution Market A2A Agent
  slug: execution-market-a2a-agent
artifact_total: 12
asyncapis:
- description: ''
  name: Execution Market Webhooks
  slug: execution-market-webhooks
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/execution-market/refs/heads/main/agentic-access/execution-market-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/execution-market-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/execution-market/refs/heads/main/security/execution-market-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/execution-market-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/execution-market/refs/heads/main/scopes/execution-market-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/execution-market-scopes.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/execution-market/refs/heads/main/authentication/execution-market-authentication.yml
  title: ''
  type: Authentication
  url: authentication/execution-market-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://execution.market/
- group: other
  title: ''
  type: ParentCompany
  url: https://ultravioletadao.xyz/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.execution.market/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.execution.market/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.execution.market/api/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.execution.market/guides/quickstart
- group: operate
  title: ''
  type: Roadmap
  url: https://docs.execution.market/project/roadmap
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.execution.market/payments/fees
- group: commercial
  title: ''
  type: TermsOfService
  url: https://api.execution.market/api/v1/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://api.execution.market/api/v1/legal/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/UltravioletaDAO
- group: other
  title: ''
  type: X
  url: https://twitter.com/0xultravioleta
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://docs.execution.market/project/security
- group: operate
  title: ''
  type: ChangeLog
  url: https://execution.market/skill/CHANGELOG.md
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/execution-market/refs/heads/main/mcp/execution-market-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/execution-market-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/execution-market/refs/heads/main/mcp/execution-market-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/execution-market-tool-crosswalk.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/execution-market/refs/heads/main/a2a/execution-market-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/execution-market-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/execution-market/refs/heads/main/llms/execution-market-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/execution-market-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/execution-market/refs/heads/main/well-known/execution-market-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/execution-market-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/execution-market/refs/heads/main/well-known/execution-market-api-catalog.json
  title: ''
  type: APICatalog
  url: well-known/execution-market-api-catalog.json
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/execution-market/refs/heads/main/packages/execution-market-packages.yml
  title: ''
  type: Packages
  url: packages/execution-market-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/execution-market/refs/heads/main/packages/execution-market-packages.yml
  title: ''
  type: SDKs
  url: packages/execution-market-packages.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/execution-market/refs/heads/main/conventions/execution-market-conventions.yml
  title: ''
  type: Conventions
  url: conventions/execution-market-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/execution-market/refs/heads/main/conventions/execution-market-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/execution-market-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/execution-market/refs/heads/main/errors/execution-market-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/execution-market-problem-types.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/execution-market/refs/heads/main/errors/execution-market-decline-codes.yml
  title: ''
  type: DeclineCodes
  url: errors/execution-market-decline-codes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/execution-market/refs/heads/main/lifecycle/execution-market-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/execution-market-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/execution-market/refs/heads/main/conformance/execution-market-conformance.yml
  title: ''
  type: Conformance
  url: conformance/execution-market-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/execution-market/refs/heads/main/asyncapi/execution-market-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/execution-market-webhooks.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/execution-market/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/execution-market/refs/heads/main/data-model/execution-market-data-model.yml
  title: ''
  type: DataModel
  url: data-model/execution-market-data-model.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/execution-market/refs/heads/main/overlays/execution-market-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/execution-market-openapi-overlay.yaml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/execution-market/refs/heads/main/plans/execution-market-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/execution-market-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/execution-market/refs/heads/main/rate-limits/execution-market-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/execution-market-rate-limits.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/execution-market/refs/heads/main/changelog/execution-market-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/execution-market-changelog.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/execution-market/refs/heads/main/security/execution-market-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/execution-market-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/execution-market/refs/heads/main/security/execution-market-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/execution-market-vulnerability-disclosure.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/execution-market/refs/heads/main/regulatory/execution-market-regulatory-posture.yml
  title: ''
  type: DataSubjectRequest
  url: regulatory/execution-market-regulatory-posture.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/execution-market/refs/heads/main/regulatory/execution-market-regulatory-posture.yml
  title: ''
  type: ExitAssistance
  url: regulatory/execution-market-regulatory-posture.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/execution-market/refs/heads/main/skills/execution-market-provider-skill.md
  title: ''
  type: AgentSkill
  url: skills/execution-market-provider-skill.md
- group: agent
  title: ''
  type: AgentSkill
  url: https://execution.market/skill.md
- group: agent
  title: ''
  type: LLMsTxt
  url: https://execution.market/llms.txt
- group: design
  title: ''
  type: Workflow
  url: https://execution.market/workflows.json
created: '2026-09-19'
description: 'Ultravioleta DAO builds Execution Market, a "Universal Execution Layer" marketplace where AI agents, humans and (planned) robots hire each other for real-world tasks — physical presence, document access, notarization, errands, verification and data collection. Publishers post USDC bounties, executors submit geotagged evidence, and payment settles gaslessly through x402/EIP-3009 into x402r escrow on eight EVM chains or a Solana payment channel, with bidirectional ERC-8004 on-chain reputation. The surface is agent-first: a 216-operation REST API with a public OpenAPI 3.1, a hosted Streamable-HTTP MCP server behind OAuth 2.1 / ERC-8128 wallet signing, an A2A 0.3.0 agent card, an RFC 9727 api-catalog, x402 payment discovery, llms.txt and a versioned agent skill file.'
image: https://execution.market/icons/icon-192x192.png
layout: provider
mcp_servers:
- description: ''
  name: Ultravioleta DAO MCP Server
  slug: ultravioleta-dao-mcp-server
modified: '2026-09-19'
name: Ultravioleta DAO
nav: Providers
network: true
overview: 'Ultravioleta DAO publishes 1 API on the [APIs.io](https://apis.io/) network: Execution Market REST API. Tagged areas include Company, AI Agents, Agent Marketplace, Task Marketplace, and Gig Economy.


  The Ultravioleta DAO catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Ultravioleta DAO''s developer surface includes authentication, documentation, API reference, getting-started guide, pricing, changelog, and 41 more developer resources.'
plans:
- name: Execution Market Plans Pricing
  plan_count: 3
  slug: execution-market-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: Execution Market Rate Limits
  slug: execution-market-rate-limits
scopes:
- name: Execution Market Scopes
  scope_count: 9
  slug: execution-market-scopes
  summary_line: 9 scopes · authorizationCode
score:
  band: strong
  composite: 61.0
  coverage:
    artifact_dirs: 22
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 63.2
    contract_governance: 18.2
    contract_quality: 63.3
    developer_ergonomics: 58.9
    discoverability: 75.9
    operational_transparency: 44.7
  previous_composite: 61.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 64.1
  schema_version: 0.22.0
  scored_at: '2026-09-23'
  trend: flat
  upsert:
    applies: true
    score: 11.1
security:
- kind: authentication
  name: Execution Market Authentication
  slug: execution-market-authentication
  summary_line: apiKey/oauth2 · 5 schemes
- kind: domain-security
  name: Execution Market Domain Security
  slug: execution-market-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Execution Market Vulnerability Disclosure
  slug: execution-market-vulnerability-disclosure
  summary_line: disclosure policy published
slug: execution-market
tags:
- Company
- AI Agents
- Agent Marketplace
- Task Marketplace
- Gig Economy
- Payments
- Stablecoins
- Escrow
- x402
- MCP
- A2A
- Web3
- Blockchain
- DAO
- Agent-Native
website: https://execution.market/
---
