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
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
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
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 69.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 89
  human_in_the_loop: 2
  name: Execution Market Agentic Access
  operation_count: 216
  slug: execution-market-agentic-access
  summary_line: 216 operations · 89 acting · 2 human-in-the-loop
api_count: 2
apis:
- description: Hosted Streamable-HTTP MCP server (server-card version 9.7.0) exposing the task marketplace as tools (publish, browse, assign, approve, batch create, escrow state, Solana channel, fee structure, statu
  name: Execution Market MCP Server
  slug: execution-market-mcp-server
- description: A2A protocol 0.3.0 JSON-RPC agent at api.execution.market/a2a/v1 advertising seven skills (publish task, manage tasks, review submissions, worker assignment, batch operations, analytics, payment manag
  name: Execution Market A2A Agent
  slug: execution-market-a2a-agent
- baseURL: https://api.execution.market
  baseurl_source: declared
  description: The A2A API from Ultravioleta DAO — 4 operation(s) for a2a.
  name: Ultravioleta DAO A2A API
  slug: execution-market-a2a-api
- baseURL: https://api.execution.market
  baseurl_source: declared
  description: A2A agent card and capability discovery (/.well-known/agent.json).
  name: Ultravioleta DAO A2A Discovery API
  slug: execution-market-a2a-discovery-api
- baseURL: https://api.execution.market
  baseurl_source: declared
  description: Agent-to-Agent JSON-RPC protocol (v0.3.0).
  name: Ultravioleta DAO A2A Protocol API
  slug: execution-market-a2a-protocol-api
- baseURL: https://api.execution.market
  baseurl_source: declared
  description: User account management and preferences.
  name: Ultravioleta DAO Account API
  slug: execution-market-account-api
- baseURL: https://api.execution.market
  baseurl_source: declared
  description: ERC-8128 wallet-based authentication for dashboard and agents.
  name: Ultravioleta DAO Agent Auth API
  slug: execution-market-agent-auth-api
- baseURL: https://api.execution.market
  baseurl_source: declared
  description: The Arbiter-as-a-Service API from Ultravioleta DAO — 2 operation(s) for arbiter-as-a-service.
  name: Ultravioleta DAO Arbiter As A Service API
  slug: execution-market-arbiter-as-a-service-api
- baseURL: https://api.execution.market
  baseurl_source: declared
  description: Audit grid and payment event trail.
  name: Ultravioleta DAO Audit API
  slug: execution-market-audit-api
- baseURL: https://api.execution.market
  baseurl_source: declared
  description: The Disputes API from Ultravioleta DAO — 4 operation(s) for disputes.
  name: Ultravioleta DAO Disputes API
  slug: execution-market-disputes-api
- baseURL: https://api.execution.market
  baseurl_source: declared
  description: The ENS API from Ultravioleta DAO — 5 operation(s) for ens.
  name: Ultravioleta DAO ENS API
  slug: execution-market-ens-api
- baseURL: https://api.execution.market
  baseurl_source: declared
  description: x402r on-chain escrow — lock, release, refund across 9 EVM chains.
  name: Ultravioleta DAO Escrow API
  slug: execution-market-escrow-api
- baseURL: https://api.execution.market
  baseurl_source: declared
  description: Evidence processing — AI verification, EXIF extraction, S3 uploads.
  name: Ultravioleta DAO Evidence API
  slug: execution-market-evidence-api
- baseURL: https://api.execution.market
  baseurl_source: declared
  description: The Execution Market API API from Ultravioleta DAO — 1 operation(s) for execution market api.
  name: Ultravioleta DAO Execution Market API
  slug: execution-market-execution-market-api-api
- baseURL: https://api.execution.market
  baseurl_source: declared
  description: The Feedback Documents API from Ultravioleta DAO — 1 operation(s) for feedback documents.
  name: Ultravioleta DAO Feedback Documents API
  slug: execution-market-feedback-documents-api
- baseURL: https://api.execution.market
  baseurl_source: declared
  description: Human-to-Agent marketplace — humans publish tasks for AI agents.
  name: Ultravioleta DAO H2A Marketplace API
  slug: execution-market-h2a-marketplace-api
- baseURL: https://api.execution.market
  baseurl_source: declared
  description: Health checks, readiness probes, and server status.
  name: Ultravioleta DAO Health API
  slug: execution-market-health-api
- baseURL: https://api.execution.market
  baseurl_source: declared
  description: ERC-8004 agent/worker identity — registration, lookup, verification.
  name: Ultravioleta DAO Identity API
  slug: execution-market-identity-api
- baseURL: https://api.execution.market
  baseurl_source: declared
  description: Terms of service and legal documents.
  name: Ultravioleta DAO Legal API
  slug: execution-market-legal-api
- baseURL: https://api.execution.market
  baseurl_source: declared
  description: Miscellaneous utility endpoints.
  name: Ultravioleta DAO Misc API
  slug: execution-market-misc-api
- baseURL: https://api.execution.market
  baseurl_source: declared
  description: Content moderation and platform safety.
  name: Ultravioleta DAO Moderation API
  slug: execution-market-moderation-api
- baseURL: https://api.execution.market
  baseurl_source: declared
  description: The Notifications API from Ultravioleta DAO — 1 operation(s) for notifications.
  name: Ultravioleta DAO Notifications API
  slug: execution-market-notifications-api
- baseURL: https://api.execution.market
  baseurl_source: declared
  description: The OAuth API from Ultravioleta DAO — 8 operation(s) for oauth.
  name: Ultravioleta DAO OAuth API
  slug: execution-market-oauth-api
- baseURL: https://api.execution.market
  baseurl_source: declared
  description: The OAuth Discovery API from Ultravioleta DAO — 3 operation(s) for oauth discovery.
  name: Ultravioleta DAO OAuth Discovery API
  slug: execution-market-oauth-discovery-api
- baseURL: https://api.execution.market
  baseurl_source: declared
  description: x402 payment operations — balance checks, fee calculation, settlement info.
  name: Ultravioleta DAO Payments API
  slug: execution-market-payments-api
- baseURL: https://api.execution.market
  baseurl_source: declared
  description: The relay API from Ultravioleta DAO — 4 operation(s) for relay.
  name: Ultravioleta DAO Relay API
  slug: execution-market-relay-api
- baseURL: https://api.execution.market
  baseurl_source: declared
  description: ERC-8004 on-chain reputation — bidirectional feedback, scores, identity.
  name: Ultravioleta DAO Reputation API
  slug: execution-market-reputation-api
- baseURL: https://api.execution.market
  baseurl_source: declared
  description: The Services API from Ultravioleta DAO — 5 operation(s) for services.
  name: Ultravioleta DAO Services API
  slug: execution-market-services-api
- baseURL: https://api.execution.market
  baseurl_source: declared
  description: The Showcase API from Ultravioleta DAO — 1 operation(s) for showcase.
  name: Ultravioleta DAO Showcase API
  slug: execution-market-showcase-api
- baseURL: https://api.execution.market
  baseurl_source: declared
  description: The Streams API from Ultravioleta DAO — 6 operation(s) for streams.
  name: Ultravioleta DAO Streams API
  slug: execution-market-streams-api
- baseURL: https://api.execution.market
  baseurl_source: declared
  description: Evidence submissions from workers — upload proof, check status.
  name: Ultravioleta DAO Submissions API
  slug: execution-market-submissions-api
- baseURL: https://api.execution.market
  baseurl_source: declared
  description: Task CRUD — publish bounties, query, cancel. Core resource for agents.
  name: Ultravioleta DAO Tasks API
  slug: execution-market-tasks-api
- baseURL: https://api.execution.market
  baseurl_source: declared
  description: The Taxímetro API from Ultravioleta DAO — 6 operation(s) for taxímetro.
  name: Ultravioleta DAO Taxímetro API
  slug: execution-market-tax-metro-api
- baseURL: https://api.execution.market
  baseurl_source: declared
  description: The Verification API from Ultravioleta DAO — 4 operation(s) for verification.
  name: Ultravioleta DAO Verification API
  slug: execution-market-verification-api
- baseURL: https://api.execution.market
  baseurl_source: declared
  description: The VeryAI API from Ultravioleta DAO — 4 operation(s) for veryai.
  name: Ultravioleta DAO Very AI API
  slug: execution-market-veryai-api
- baseURL: https://api.execution.market
  baseurl_source: declared
  description: Webhook registration and event delivery.
  name: Ultravioleta DAO Webhooks API
  slug: execution-market-webhooks-api
- baseURL: https://api.execution.market
  baseurl_source: declared
  description: The websocket API from Ultravioleta DAO — 2 operation(s) for websocket.
  name: Ultravioleta DAO WebSocket API
  slug: execution-market-websocket-api
- baseURL: https://api.execution.market
  baseurl_source: declared
  description: Worker (executor) registration, profiles, and management.
  name: Ultravioleta DAO Workers API
  slug: execution-market-workers-api
- baseURL: https://api.execution.market
  baseurl_source: declared
  description: World ID 4.0 proof of humanity — RP signing, Orb-level verification.
  name: Ultravioleta DAO World ID API
  slug: execution-market-world-id-api
- baseURL: https://api.execution.market
  baseurl_source: declared
  description: x402 protocol auto-discovery (/.well-known/x402).
  name: Ultravioleta DAO x402 Discovery API
  slug: execution-market-x402-discovery-api
artifact_total: 56
asyncapis:
- description: ''
  name: Execution Market Webhooks
  slug: execution-market-webhooks
common:
- group: company
  title: ''
  type: Blog
  url: https://execution.market/blog/
- group: other
  href: https://artifacts.apis.io/execution-market/capabilities/execution-market-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/execution-market-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/execution-market/agentic-access/execution-market-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/execution-market-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/execution-market/security/execution-market-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/execution-market-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/execution-market/scopes/execution-market-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/execution-market-scopes.yml
- group: auth
  href: https://artifacts.apis.io/execution-market/authentication/execution-market-authentication.yml
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
  href: https://artifacts.apis.io/execution-market/mcp/execution-market-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/execution-market-mcp.yml
- group: build
  href: https://artifacts.apis.io/execution-market/mcp/execution-market-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/execution-market-tool-crosswalk.yml
- group: other
  href: https://artifacts.apis.io/execution-market/a2a/execution-market-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/execution-market-a2a.yml
- group: agent
  href: https://artifacts.apis.io/execution-market/llms/execution-market-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/execution-market-llms.txt
- group: agent
  href: https://artifacts.apis.io/execution-market/well-known/execution-market-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/execution-market-well-known.yml
- group: other
  href: https://artifacts.apis.io/execution-market/well-known/execution-market-api-catalog.json
  title: ''
  type: APICatalog
  url: well-known/execution-market-api-catalog.json
- group: build
  href: https://artifacts.apis.io/execution-market/packages/execution-market-packages.yml
  title: ''
  type: Packages
  url: packages/execution-market-packages.yml
- group: build
  href: https://artifacts.apis.io/execution-market/packages/execution-market-packages.yml
  title: ''
  type: SDKs
  url: packages/execution-market-packages.yml
- group: design
  href: https://artifacts.apis.io/execution-market/conventions/execution-market-conventions.yml
  title: ''
  type: Conventions
  url: conventions/execution-market-conventions.yml
- group: design
  href: https://artifacts.apis.io/execution-market/conventions/execution-market-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/execution-market-conventions.yml
- group: design
  href: https://artifacts.apis.io/execution-market/errors/execution-market-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/execution-market-problem-types.yml
- group: build
  href: https://artifacts.apis.io/execution-market/errors/execution-market-decline-codes.yml
  title: ''
  type: DeclineCodes
  url: errors/execution-market-decline-codes.yml
- group: design
  href: https://artifacts.apis.io/execution-market/lifecycle/execution-market-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/execution-market-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/execution-market/conformance/execution-market-conformance.yml
  title: ''
  type: Conformance
  url: conformance/execution-market-conformance.yml
- group: design
  href: https://artifacts.apis.io/execution-market/asyncapi/execution-market-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/execution-market-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/execution-market/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/execution-market/data-model/execution-market-data-model.yml
  title: ''
  type: DataModel
  url: data-model/execution-market-data-model.yml
- group: other
  href: https://artifacts.apis.io/execution-market/overlays/execution-market-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/execution-market-openapi-overlay.yaml
- group: commercial
  href: https://artifacts.apis.io/execution-market/plans/execution-market-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/execution-market-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/execution-market/rate-limits/execution-market-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/execution-market-rate-limits.yml
- group: operate
  href: https://artifacts.apis.io/execution-market/changelog/execution-market-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/execution-market-changelog.yml
- group: auth
  href: https://artifacts.apis.io/execution-market/security/execution-market-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/execution-market-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/execution-market/security/execution-market-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/execution-market-vulnerability-disclosure.yml
- group: other
  href: https://artifacts.apis.io/execution-market/regulatory/execution-market-regulatory-posture.yml
  title: ''
  type: DataSubjectRequest
  url: regulatory/execution-market-regulatory-posture.yml
- group: other
  href: https://artifacts.apis.io/execution-market/regulatory/execution-market-regulatory-posture.yml
  title: ''
  type: ExitAssistance
  url: regulatory/execution-market-regulatory-posture.yml
- group: agent
  href: https://artifacts.apis.io/execution-market/skills/execution-market-provider-skill.md
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
finops:
- has_sources: true
  method: derived
  name: Execution Market Finops
  primary_unit: task
  service_category: ''
  slug: execution-market-finops
  template: false
image: https://execution.market/icons/icon-192x192.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.execution.market over HTTP requiring OAuth; 46 tools listed.
  name: Ultravioleta DAO MCP Server
  slug: execution-market
modified: '2026-10-06'
name: Ultravioleta DAO
nav: Providers
network: true
overview: 'Ultravioleta DAO publishes 40 API contracts indexed on the [APIs.io](https://apis.io/) network, including A2A API, A2A Discovery API, A2A Protocol API, and 37 more. Tagged areas include Company, AI Agents, Agent Marketplace, Task Marketplace, and Gig Economy.


  The Ultravioleta DAO catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Ultravioleta DAO''s developer surface includes engineering blog, authentication, documentation, API reference, getting-started guide, pricing, changelog, and 42 more developer resources.'
plans:
- name: Execution Market Plans Pricing
  plan_count: 3
  slug: execution-market-plans-pricing
- name: Execution Market Price Estimates
  plan_count: 0
  slug: execution-market-price-estimates
random_paper: 13
rate_limits:
- limit_count: 0
  name: Execution Market Rate Limits
  slug: execution-market-rate-limits
rules:
- authorship: generated
  effective_rule_count: 115
  extends:
  - spectral:oas
  name: Ultravioleta DAO API Rules
  rule_count: 74
  severity_counts:
    error: 52
    hint: 0
    info: 5
    warn: 17
  slug: execution-market-rules
scopes:
- name: Execution Market Scopes
  scope_count: 9
  slug: execution-market-scopes
  summary_line: 9 scopes · authorizationCode
score:
  band: developing
  composite: 54.0
  coverage:
    artifact_dirs: 32
    catalog_earned: 56.5
    catalog_earned_first_party: 12.0
    catalog_gap: 58.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.0
  facets:
    access_clarity: 55.3
    contract_governance: 31.8
    contract_quality: 62.8
    developer_ergonomics: 41.4
    discoverability: 75.0
    operational_transparency: 31.6
  previous_composite: 62.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 38
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 40.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 11.1
screenshot: https://apis.io/screenshots/execution-market/execution-market-2026-10-11T104335.png
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
  summary_line: no policy recorded
skill_count: 4
skills:
- name: Cancel a task and recover escrowed funds
  slug: execution-market-cancel-and-recover
- name: execution-market
  slug: execution-market-provider-skill
- name: Publish a task, assign a worker, approve and pay
  slug: execution-market-publish-and-pay
- name: Find work, submit evidence, get paid
  slug: execution-market-work-as-executor
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
