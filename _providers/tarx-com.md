---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: conformant
    agent_skills: true
    agentic_access: true
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
  score: 29.2
  scored_at: '2026-09-21'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Tarx Com Agentic Access
  operation_count: 22
  slug: tarx-com-agentic-access
  summary_line: 22 operations · 3 acting
api_count: 3
apis:
- description: 'Streamable-HTTP MCP server (serverInfo tarx 3.18.0, protocol 2025-06-18) exposing 22 tools, 5 prompts and 5 resources anonymously — public TARX context search/fetch, install guidance, runtime status, '
  name: TARX Remote MCP Server
  slug: tarx-remote-mcp-server
- description: 'OpenAI-compatible hosted inference API. GET /v1/models lists the single model t-supercomputer (owned_by tarx, OpenRouter slug tarx/t-supercomputer) without a key; POST /v1/chat/completions requires a '
  name: TARX Supercomputer API
  slug: tarx-supercomputer-api
- description: 'Plain REST endpoints on tarx.com documented only for visiting AI agents in we.txt, skill.md and courier.md: GET /api/courier/ping and /api/courier/tick (signed heartbeat naming the agent card and cair'
  name: TARX Courier and Souls API
  slug: tarx-courier-and-souls-api
artifact_total: 13
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/tarx-com/refs/heads/main/security/tarx-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tarx-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tarx.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tarx.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://howdy.tarx.com
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.tarx.com/start-here/quickstart
- group: operate
  title: ''
  type: Support
  url: https://tarx.com/support
- group: operate
  title: ''
  type: Contact
  url: https://docs.tarx.com/reference/contact
- group: company
  title: ''
  type: Blog
  url: https://tarx.com/dispatches
- group: company
  title: ''
  type: Blog
  url: https://tarx.substack.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tarx-ai
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.tarx.com/pricing/overview
- group: start
  title: ''
  type: SignUp
  url: https://tarx.com/join
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tarx.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tarx.com/privacy
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.tarx.com/reference/changelog
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/tarx-com/refs/heads/main/changelog/tarx-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/tarx-com-changelog.yml
- group: auth
  title: ''
  type: Security
  url: https://tarx.com/security
- group: company
  title: ''
  type: About
  url: https://tarx.com/about
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/tarx-com/refs/heads/main/a2a/tarx-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/tarx-com-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/tarx-com/refs/heads/main/mcp/tarx-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/tarx-com-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/tarx-com/refs/heads/main/llms/tarx-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/tarx-com-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/tarx-com/refs/heads/main/llms/tarx-com-docs-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/tarx-com-docs-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/tarx-com/refs/heads/main/llms/tarx-com-howdy-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/tarx-com-howdy-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/tarx-com/refs/heads/main/well-known/tarx-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/tarx-com-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/tarx-com/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/tarx-com/refs/heads/main/agentic-access/tarx-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/tarx-com-agentic-access.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/tarx-com/refs/heads/main/packages/tarx-com-packages.yml
  title: ''
  type: Packages
  url: packages/tarx-com-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/tarx-com/refs/heads/main/cli/tarx-com-cli.yml
  title: ''
  type: CLI
  url: cli/tarx-com-cli.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/tarx-com/refs/heads/main/authentication/tarx-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/tarx-com-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/tarx-com/refs/heads/main/scopes/tarx-com-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/tarx-com-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tarx-com/refs/heads/main/conformance/tarx-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/tarx-com-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tarx-com/refs/heads/main/errors/tarx-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/tarx-com-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tarx-com/refs/heads/main/lifecycle/tarx-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/tarx-com-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tarx-com/refs/heads/main/conventions/tarx-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/tarx-com-conventions.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/tarx-com/refs/heads/main/plans/tarx-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/tarx-com-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/tarx-com/refs/heads/main/rate-limits/tarx-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/tarx-com-rate-limits.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/tarx-com/refs/heads/main/sandbox/tarx-com-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/tarx-com-sandbox.yml
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/tarx-com/refs/heads/main/json-schema/tarx-com-partner-sandbox-fixture-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/tarx-com-partner-sandbox-fixture-schema.json
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/tarx-com/refs/heads/main/examples/tarx-com-partner-sandbox-fixture.json
  title: ''
  type: Examples
  url: examples/tarx-com-partner-sandbox-fixture.json
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/tarx-com/refs/heads/main/regulatory/tarx-com-regulatory-posture.yml
  title: ''
  type: RegulatoryPosture
  url: regulatory/tarx-com-regulatory-posture.yml
- group: other
  title: ''
  type: DataSubjectRequest
  url: https://tarx.com/terms
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/tarx-com/refs/heads/main/security/tarx-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/tarx-com-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/tarx-com/refs/heads/main/security/tarx-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/tarx-com-vulnerability-disclosure.yml
created: '2026-09-19'
description: 'TARXAN Inc (TARX, Austin TX) builds a local-first AI agent runtime: free TARX_OS / TARX Desktop software for Apple Silicon Macs, a shell CLI that installs a local inference daemon and local MCP servers, an optional hosted "Supercomputer" reached through an OpenAI-compatible API (api.tarx.com/v1, model t-supercomputer), and dedicated "Black Box" and humanoid/quadruped hardware. Its public agent surface is a remote MCP server at mcp.tarx.com/mcp (22 anonymous tools, OAuth 2.0 + PKCE for private memory, RFC 8414/9728 metadata) advertised by an A2A 0.3.0 agent card at tarx.com/.well-known/agent-card.json and a prose "cairn" (we.txt, skill.md, courier.md) that tells visiting agents how to register a Soul through plain REST on tarx.com/api. No OpenAPI is published.'
examples:
- key_count: 11
  name: Tarx Com Partner Sandbox Fixture
  slug: tarx-com-partner-sandbox-fixture
image: https://tarx.com/tarx-logo.png
json_schemas:
- name: TARX Partner Sandbox Fixture
  property_count: 11
  slug: tarx-com-partner-sandbox-fixture
layout: provider
mcp_servers:
- description: ''
  name: TARXAN Inc MCP Server
  slug: tarxan-inc-mcp-server
modified: '2026-09-19'
name: TARXAN Inc
nav: Providers
network: true
overview: 'TARXAN Inc publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI Agents, Agent Runtime, Local-First AI, and Private AI.


  TARXAN Inc''s developer surface includes documentation, getting-started guide, support, engineering blog, pricing, signup flow, changelog, and 36 more developer resources.'
plans:
- name: Tarx Com Plans Pricing
  plan_count: 6
  slug: tarx-com-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: Tarx Com Rate Limits
  slug: tarx-com-rate-limits
scopes:
- name: Tarx Com Scopes
  scope_count: 0
  slug: tarx-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 46.7
  coverage:
    artifact_dirs: 22
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 6.7
    developer_ergonomics: 78.6
    discoverability: 81.5
    operational_transparency: 28.9
  previous_composite: 46.7
  provenance:
    agentic_access: first-party
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.22.0
  scored_at: '2026-09-21'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Tarx Com Authentication
  slug: tarx-com-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Tarx Com Domain Security
  slug: tarx-com-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Tarx Com Vulnerability Disclosure
  slug: tarx-com-vulnerability-disclosure
  summary_line: Hackerone
slug: tarx-com
tags:
- Company
- AI Agents
- Agent Runtime
- Local-First AI
- Private AI
- MCP
- A2A
- LLM
- Inference
- Developer Tools
- Hardware
- Robotics
website: https://tarx.com/
---
