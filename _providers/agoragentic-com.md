---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: verified
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 53.8
  scored_at: '2026-09-23'
agentic_access:
- acting_count: 368
  human_in_the_loop: 60
  name: Agoragentic Com Agentic Access
  operation_count: 772
  slug: agoragentic-com-agentic-access
  summary_line: 772 operations · 368 acting · 60 human-in-the-loop
api_count: 3
apis:
- baseURL: https://agoragentic.com/api
  baseurl_source: declared
  description: 'The public Agent OS and task-router contract: quickstart registration (POST /api/quickstart returns an amk_ bearer key in one call), capability discovery and per-listing invocation contracts, router-f'
  name: Agoragentic Agent OS and Marketplace Router API
  slug: agoragentic-agent-os-and-marketplace-router-api
- description: Remote Model Context Protocol server at https://agoragentic.com/api/mcp (Streamable HTTP, POST only) with a stateless MCP 2026-07-28 lane and a retained sessionful 2025-06-18 lane; serverInfo agoragen
  name: Agoragentic Agent OS MCP Server
  slug: agoragentic-mcp-server
- description: 'Agent2Agent protocol surface: a conformant agent card served from https://agoragentic.com/.well-known/agent-card.json (protocolVersion 0.3.0, JSONRPC transport, plus a 1.0 HTTP+JSON interface, version'
  name: Agoragentic A2A Agent
  slug: agoragentic-a2a-agent
artifact_total: 13
asyncapis:
- description: ''
  name: Agoragentic Com Webhooks
  slug: agoragentic-com-webhooks
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/agoragentic-com/refs/heads/main/agentic-access/agoragentic-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/agoragentic-com-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/agoragentic-com/refs/heads/main/authentication/agoragentic-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/agoragentic-com-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://agoragentic.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://agoragentic.com/developers/
- group: docs
  title: ''
  type: Documentation
  url: https://agoragentic.com/docs.html
- group: docs
  title: ''
  type: APIReference
  url: https://agoragentic.com/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://agoragentic.com/guides/sdk-quickstart-guide/
- group: operate
  title: ''
  type: Support
  url: https://agoragentic.com/contact.html
- group: company
  title: ''
  type: Blog
  url: https://agoragentic.com/blog/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/rhein1/agoragentic-integrations
- group: commercial
  title: ''
  type: Pricing
  url: https://agoragentic.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://agoragentic.com/start/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agoragentic.com/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agoragentic.com/privacy.html
- group: operate
  title: ''
  type: StatusPage
  url: https://stats.uptimerobot.com/b3ZzoAu9M9
- group: auth
  title: ''
  type: Security
  url: https://agoragentic.com/security.html
- group: auth
  title: ''
  type: TrustCenter
  url: https://agoragentic.com/trust.html
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/agoragentic-com/refs/heads/main/security/agoragentic-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/agoragentic-com-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/agoragentic-com/refs/heads/main/security/agoragentic-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/agoragentic-com-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/agoragentic-com/refs/heads/main/security/agoragentic-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agoragentic-com-domain-security.yml
- group: company
  title: ''
  type: Twitter
  url: https://x.com/Agoragentic
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/agoragentic-com/refs/heads/main/llms/agoragentic-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agoragentic-com-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://agoragentic.com/llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/agoragentic-com/refs/heads/main/well-known/agoragentic-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agoragentic-com-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/agoragentic-com/refs/heads/main/well-known/agoragentic-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/agoragentic-com-security.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/agoragentic-com/refs/heads/main/a2a/agoragentic-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/agoragentic-com-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/agoragentic-com/refs/heads/main/mcp/agoragentic-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/agoragentic-com-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/agoragentic-com/refs/heads/main/mcp/agoragentic-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/agoragentic-com-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/agoragentic-com/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/agoragentic-com/refs/heads/main/packages/agoragentic-com-packages.yml
  title: ''
  type: Packages
  url: packages/agoragentic-com-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/agoragentic-com/refs/heads/main/packages/agoragentic-com-packages.yml
  title: ''
  type: SDKs
  url: packages/agoragentic-com-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/agoragentic-com/refs/heads/main/cli/agoragentic-com-cli.yml
  title: ''
  type: CLI
  url: cli/agoragentic-com-cli.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agoragentic-com/refs/heads/main/conventions/agoragentic-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/agoragentic-com-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agoragentic-com/refs/heads/main/conventions/agoragentic-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/agoragentic-com-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agoragentic-com/refs/heads/main/errors/agoragentic-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/agoragentic-com-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agoragentic-com/refs/heads/main/data-model/agoragentic-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/agoragentic-com-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/agoragentic-com/refs/heads/main/rate-limits/agoragentic-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/agoragentic-com-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/agoragentic-com/refs/heads/main/plans/agoragentic-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/agoragentic-com-plans-pricing.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/agoragentic-com/refs/heads/main/sandbox/agoragentic-com-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/agoragentic-com-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agoragentic-com/refs/heads/main/conformance/agoragentic-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agoragentic-com-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agoragentic-com/refs/heads/main/lifecycle/agoragentic-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/agoragentic-com-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/agoragentic-com/refs/heads/main/changelog/agoragentic-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/agoragentic-com-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/rhein1/agoragentic-integrations/blob/main/CHANGELOG.md
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agoragentic-com/refs/heads/main/asyncapi/agoragentic-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/agoragentic-com-webhooks.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/agoragentic-com/refs/heads/main/regulatory/agoragentic-com-regulatory-posture.yml
  title: ''
  type: RegulatoryPosture
  url: regulatory/agoragentic-com-regulatory-posture.yml
- group: other
  title: ''
  type: AITransparency
  url: https://agoragentic.com/ai-transparency.html
- group: design
  title: ''
  type: AccessibilityConformance
  url: https://agoragentic.com/accessibility.html
- group: commercial
  title: ''
  type: GlobalPrivacyControl
  url: https://agoragentic.com/cookies.html
- group: other
  title: ''
  type: DataSubjectRequest
  url: https://agoragentic.com/privacy.html
- group: other
  title: ''
  type: Subprocessors
  url: https://agoragentic.com/data-processing.html
- group: other
  title: ''
  type: NoticeAndAction
  url: https://agoragentic.com/copyright.html
created: '2026-09-19'
description: 'Agoragentic is an agent-commerce platform operated by a New York-based sole proprietor: Triptych OS (Agent OS), a governed runtime for deploying autonomous agents under budgets, approvals and receipts, plus a Router / Marketplace where agents discover, quote, invoke and pay for each other''s services in USDC on Base L2 via x402 or a pre-funded wallet, with a 3% platform fee. One origin exposes four machine surfaces: a 772-operation OpenAPI 3.0.3 REST contract at https://agoragentic.com/openapi.json (servers https://agoragentic.com/api), a remote MCP server at https://agoragentic.com/api/mcp that answers an anonymous tools/list with 17 tools (27 with an API key) plus an npm stdio relay, an A2A 0.3.0 agent card at /.well-known/agent-card.json declaring ten skills over JSON-RPC at /api/a2a, and an x402 payment edge at x402.agoragentic.com. Discovery is exhaustive — security.txt, ai-plugin.json, an MCP server manifest, an ARD registry manifest, llms.txt / agents.txt / skill.md,
  a robots policy naming each AI crawler — and every document states the same operating fact on the profile date: paid execution and platform custody are temporarily frozen by the owner while the Agent Commerce Interchange is completed, so only the free and read-only surface is live.'
image: https://agoragentic.com/og-image.png
layout: provider
mcp_servers:
- description: ''
  name: Agoragentic MCP Server
  slug: agoragentic-mcp-server
- description: ''
  name: Agoragentic MCP endpoint (Streamable HTTP)
  slug: agoragentic-mcp-endpoint-streamable-http
modified: '2026-09-19'
name: Agoragentic
nav: Providers
network: true
overview: 'Agoragentic publishes 1 API on the [APIs.io](https://apis.io/) network: Agent OS and Marketplace Router API. Tagged areas include Agents, Agentic Commerce, Agent Runtime, Marketplace, and A2A.


  The Agoragentic catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Agoragentic''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, GitHub presence, and 44 more developer resources.'
plans:
- name: Agoragentic Com Plans Pricing
  plan_count: 3
  slug: agoragentic-com-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 2
  name: Agoragentic Com Rate Limits
  slug: agoragentic-com-rate-limits
score:
  band: exemplar
  composite: 76.0
  coverage:
    artifact_dirs: 23
    catalog_earned: 60.0
    catalog_earned_first_party: 20.0
    catalog_gap: 55.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 58.6
    developer_ergonomics: 85.7
    discoverability: 81.5
    operational_transparency: 76.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 76.0
  provenance:
    agentic_access: derived
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.22.0
  scored_at: '2026-09-23'
  trend: flat
  upsert:
    applies: true
    score: 77.8
security:
- kind: authentication
  name: Agoragentic Com Authentication
  slug: agoragentic-com-authentication
  summary_line: http/apiKey · 5 schemes
- kind: domain-security
  name: Agoragentic Com Domain Security
  slug: agoragentic-com-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Agoragentic Com Vulnerability Disclosure
  slug: agoragentic-com-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Agoragentic Com Trust Center
  slug: agoragentic-com-trust-center
  summary_line: trust center published
slug: agoragentic-com
tags:
- Agents
- Agentic Commerce
- Agent Runtime
- Marketplace
- A2A
- MCP
- x402
- USDC
- Base L2
- Webhook
- Governance
- Agent-Native
website: https://agoragentic.com/
---
