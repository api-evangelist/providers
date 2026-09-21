---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: flavored
    agent_skills: derived
    agentic_access: false
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
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.0
  scored_at: '2026-09-20'
api_count: 3
apis:
- description: 'JSON REST API at https://getamber.dev/api/v1 for the full mandate lifecycle: list templates (public), create a contract from a template (X-API-Key with credits, or x402 pay-per-contract), share it by '
  name: Ambr REST API
  slug: ambr-rest-api
- description: One remote Model Context Protocol server at https://getamber.dev/api/mcp — Streamable HTTP in stateless JSON mode, protocol version 2025-03-26, serverInfo ambr-mcp-server 1.0.0. Anonymous initialize a
  name: Ambr MCP Server
  slug: ambr-mcp-server
- description: Agent-to-Agent JSON-RPC endpoint at https://getamber.dev/api/a2a implementing message/send, tasks/get and tasks/cancel (tasks are processed synchronously), discovered through an agent card served at /
  name: Ambr A2A Agent
  slug: ambr-a2a-agent
artifact_total: 17
common:
- group: company
  title: ''
  type: Website
  url: https://ambr.run/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://getamber.dev/developers
- group: docs
  title: ''
  type: Documentation
  url: https://getamber.dev/docs
- group: docs
  title: ''
  type: APIReference
  url: https://getamber.dev/developers
- group: start
  title: ''
  type: GettingStarted
  url: https://getamber.dev/docs
- group: start
  title: ''
  type: SignUp
  url: https://getamber.dev/activate
- group: start
  title: ''
  type: Login
  url: https://getamber.dev/dashboard
- group: commercial
  title: ''
  type: Pricing
  url: https://getamber.dev/activate
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/getamber-dev/refs/heads/main/plans/getamber-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/getamber-dev-plans-pricing.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ambr.run/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ambr.run/privacy
- group: operate
  title: ''
  type: Support
  url: https://discord.com/invite/HjvJFfjr
- group: operate
  title: ''
  type: Community
  url: https://discord.com/invite/HjvJFfjr
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/getambr
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/getambr/ambr
- group: company
  title: ''
  type: Twitter
  url: https://x.com/ambr_run
- group: operate
  title: ''
  type: StatusPage
  url: https://ambr.run/status
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/getamber-dev/refs/heads/main/changelog/getamber-dev-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/getamber-dev-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/getambr/ambr/blob/master/CHANGELOG.md
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/getamber-dev/refs/heads/main/lifecycle/getamber-dev-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/getamber-dev-lifecycle.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/getamber-dev/refs/heads/main/a2a/getamber-dev-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/getamber-dev-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/getamber-dev/refs/heads/main/mcp/getamber-dev-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/getamber-dev-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/getamber-dev/refs/heads/main/llms/getamber-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/getamber-dev-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://ambr.run/llms.txt
- group: docs
  title: ''
  type: Specification
  url: https://ambr.run/spec/ricardian-v1
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/getamber-dev/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/getamber-dev/refs/heads/main/skills/getamber-dev-create-and-activate-mandate.md
  title: ''
  type: AgentSkill
  url: skills/getamber-dev-create-and-activate-mandate.md
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/getamber-dev/refs/heads/main/skills/getamber-dev-verify-mandate.md
  title: ''
  type: AgentSkill
  url: skills/getamber-dev-verify-mandate.md
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/getamber-dev/refs/heads/main/authentication/getamber-dev-authentication.yml
  title: ''
  type: Authentication
  url: authentication/getamber-dev-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/getamber-dev/refs/heads/main/conventions/getamber-dev-conventions.yml
  title: ''
  type: Conventions
  url: conventions/getamber-dev-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/getamber-dev/refs/heads/main/errors/getamber-dev-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/getamber-dev-problem-types.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/getamber-dev/refs/heads/main/rate-limits/getamber-dev-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/getamber-dev-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/getamber-dev/refs/heads/main/conformance/getamber-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/getamber-dev-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/getamber-dev/refs/heads/main/data-model/getamber-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/getamber-dev-data-model.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/getamber-dev/refs/heads/main/security/getamber-dev-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/getamber-dev-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/getambr/ambr/blob/master/SECURITY.md
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/getamber-dev/refs/heads/main/security/getamber-dev-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/getamber-dev-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/getamber-dev/refs/heads/main/security/getamber-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/getamber-dev-domain-security.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/getamber-dev/refs/heads/main/packages/getamber-dev-packages.yml
  title: ''
  type: Packages
  url: packages/getamber-dev-packages.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/getamber-dev/refs/heads/main/regulatory/getamber-dev-regulatory-posture.yml
  title: ''
  type: RegulatoryPosture
  url: regulatory/getamber-dev-regulatory-posture.yml
- group: other
  title: ''
  type: DataSubjectRequest
  url: https://ambr.run/privacy
- group: other
  title: ''
  type: AITransparency
  url: https://ambr.run/terms
- group: other
  title: ''
  type: ExitAssistance
  url: https://ambr.run/privacy
created: '2026-09-19'
description: 'Ambr (ambr.run; platform and API host getamber.dev) is the "Agent Mandate & Binding Registry" — an agent-native service that creates, signs, verifies and revokes Ricardian contracts for AI agents: delegation mandates recording who authorized an agent, in what scope and under which law, plus agent-to-agent commerce and agent-to-consumer agreements. Every contract is dual-format — legal prose and machine-parsable JSON bound by one SHA-256 hash (urn:ambr:ricardian-v1, MIT) — and once signed by both wallets is minted as an ERC-721 cNFT on Base L2. The surface is a JSON REST API at getamber.dev/api/v1 with a public pricing endpoint, a remote MCP server at /api/mcp (six tools, anonymous tools/list) and an A2A JSON-RPC endpoint discovered via /.well-known/agent-card.json. Auth is an X-API-Key, x402 pay-per-contract on Base, or an ECDSA wallet signature; 25 free developer contracts. No OpenAPI or SDK is published. Not Amber International (Nasdaq: AMBR).'
examples:
- key_count: 1
  name: Getamber Dev Templates Response
  slug: getamber-dev-templates-response
image: https://ambr.run/logo.png
json_schemas:
- name: Getamber Dev C1 Api Access
  property_count: 0
  slug: getamber-dev-c1-api-access
- name: Getamber Dev C2 Compute Sla
  property_count: 0
  slug: getamber-dev-c2-compute-sla
- name: Getamber Dev C3 Task Execution
  property_count: 0
  slug: getamber-dev-c3-task-execution
- name: Getamber Dev D1 General Auth
  property_count: 0
  slug: getamber-dev-d1-general-auth
- name: Getamber Dev D2 Limited Service
  property_count: 0
  slug: getamber-dev-d2-limited-service
- name: Getamber Dev D3 Fleet Auth
  property_count: 0
  slug: getamber-dev-d3-fleet-auth
layout: provider
mcp_servers:
- description: ''
  name: Ambr MCP Server
  slug: ambr-mcp-server
- description: ''
  name: Ambr MCP Server
  slug: ambr-mcp-server-2
modified: '2026-09-19'
name: Ambr
nav: Providers
network: true
overview: 'Ambr publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI Agents, Agentic Commerce, Contracts, and Legal.


  Ambr''s developer surface includes documentation, API reference, getting-started guide, signup flow, pricing, support, changelog, and 36 more developer resources.'
plans:
- name: Getamber Dev Plans Pricing
  plan_count: 10
  slug: getamber-dev-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 2
  name: Getamber Dev Rate Limits
  slug: getamber-dev-rate-limits
score:
  band: developing
  composite: 50.8
  coverage:
    artifact_dirs: 19
    catalog_earned: 70.0
    catalog_earned_first_party: 20.0
    catalog_gap: 45.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 48.0
  facets:
    access_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 20.0
    developer_ergonomics: 56.5
    discoverability: 81.5
    operational_transparency: 68.4
  previous_composite: 2.8
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-20'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Getamber Dev Authentication
  slug: getamber-dev-authentication
  summary_line: apiKey/x402-payment/wallet-signature/share-token/session-token · 5 schemes
- kind: domain-security
  name: Getamber Dev Domain Security
  slug: getamber-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Getamber Dev Vulnerability Disclosure
  slug: getamber-dev-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: getamber-dev
tags:
- Company
- AI Agents
- Agentic Commerce
- Contracts
- Legal
- Ricardian Contracts
- Delegation
- Blockchain
- Base L2
- MCP
- A2A
- x402
- agent-native
website: https://ambr.run/
---
