---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
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
    mcp_tool_quality: full
    openapi_examples: documented
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.5
  scored_at: '2026-11-06'
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
artifact_total: 20
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
  href: https://artifacts.apis.io/getamber-dev/plans/getamber-dev-plans-pricing.yml
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
  href: https://artifacts.apis.io/getamber-dev/changelog/getamber-dev-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/getamber-dev-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/getambr/ambr/blob/master/CHANGELOG.md
- group: design
  href: https://artifacts.apis.io/getamber-dev/lifecycle/getamber-dev-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/getamber-dev-lifecycle.yml
- group: other
  href: https://artifacts.apis.io/getamber-dev/a2a/getamber-dev-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/getamber-dev-a2a.yml
- group: agent
  href: https://artifacts.apis.io/getamber-dev/mcp/getamber-dev-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/getamber-dev-mcp.yml
- group: agent
  href: https://artifacts.apis.io/getamber-dev/llms/getamber-dev-llms.txt
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
  href: https://artifacts.apis.io/getamber-dev/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/getamber-dev/skills/getamber-dev-create-and-activate-mandate.md
  title: ''
  type: AgentSkill
  url: skills/getamber-dev-create-and-activate-mandate.md
- group: agent
  href: https://artifacts.apis.io/getamber-dev/skills/getamber-dev-verify-mandate.md
  title: ''
  type: AgentSkill
  url: skills/getamber-dev-verify-mandate.md
- group: auth
  href: https://artifacts.apis.io/getamber-dev/authentication/getamber-dev-authentication.yml
  title: ''
  type: Authentication
  url: authentication/getamber-dev-authentication.yml
- group: design
  href: https://artifacts.apis.io/getamber-dev/conventions/getamber-dev-conventions.yml
  title: ''
  type: Conventions
  url: conventions/getamber-dev-conventions.yml
- group: design
  href: https://artifacts.apis.io/getamber-dev/errors/getamber-dev-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/getamber-dev-problem-types.yml
- group: operate
  href: https://artifacts.apis.io/getamber-dev/rate-limits/getamber-dev-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/getamber-dev-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/getamber-dev/conformance/getamber-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/getamber-dev-conformance.yml
- group: design
  href: https://artifacts.apis.io/getamber-dev/data-model/getamber-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/getamber-dev-data-model.yml
- group: auth
  href: https://artifacts.apis.io/getamber-dev/security/getamber-dev-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/getamber-dev-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/getambr/ambr/blob/master/SECURITY.md
- group: auth
  href: https://artifacts.apis.io/getamber-dev/security/getamber-dev-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/getamber-dev-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/getamber-dev/security/getamber-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/getamber-dev-domain-security.yml
- group: build
  href: https://artifacts.apis.io/getamber-dev/packages/getamber-dev-packages.yml
  title: ''
  type: Packages
  url: packages/getamber-dev-packages.yml
- group: other
  href: https://artifacts.apis.io/getamber-dev/regulatory/getamber-dev-regulatory-posture.yml
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
finops:
- has_sources: true
  method: derived
  name: Getamber Dev Finops
  primary_unit: contract
  service_category: ''
  slug: getamber-dev-finops
  template: false
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
- description: Ambr operates ONE remote MCP server at https://getamber.dev/api/mcp — the same host that serves its REST API (/api/v1), its A2A endpoint (/api/a2a) and its agent card. It is Streamable HTTP in statele
  name: Ambr MCP Server
  slug: getamber-dev-mcp-yml
modified: '2026-09-19'
name: Ambr
nav: Providers
network: true
overview: 'Ambr is listed with 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI Agents, Agentic Commerce, Contracts, and Legal.


  Ambr''s developer surface includes documentation, API reference, getting-started guide, signup flow, pricing, support, changelog, and 36 more developer resources.'
plans:
- name: Getamber Dev Plans Pricing
  plan_count: 9
  slug: getamber-dev-plans-pricing
- name: Getamber Dev Price Estimates
  plan_count: 0
  slug: getamber-dev-price-estimates
random_paper: 3
rate_limits:
- limit_count: 2
  name: Getamber Dev Rate Limits
  slug: getamber-dev-rate-limits
score:
  band: developing
  composite: 43.6
  coverage:
    artifact_dirs: 23
    catalog_earned: 72.0
    catalog_earned_first_party: 20.0
    catalog_gap: 43.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -11.7
  facets:
    access_clarity: 61.8
    contract_governance: 18.2
    contract_quality: 18.5
    developer_ergonomics: 35.1
    discoverability: 80.0
    operational_transparency: 50.0
  previous_composite: 55.3
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/getamber-dev/getamber-dev-2026-10-11T104848.png
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
skill_count: 2
skills:
- name: Create and activate an Agent Mandate
  slug: getamber-dev-create-and-activate-mandate
- name: Verify a mandate before relying on it
  slug: getamber-dev-verify-mandate
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
- Agent-Native
website: https://ambr.run/
---
