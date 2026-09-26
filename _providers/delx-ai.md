---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: flavored
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: true
    idempotency: verified
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 57.0
  scored_at: '2026-09-25'
agentic_access:
- acting_count: 988
  human_in_the_loop: 471
  name: Delx Ai Agentic Access
  operation_count: 1002
  slug: delx-ai-agentic-access
  summary_line: 1002 operations · 988 acting · 471 human-in-the-loop
api_count: 4
apis:
- baseURL: https://api.delx.ai
  baseurl_source: declared
  description: 'The free Delx Agent Operations Protocol REST surface on api.delx.ai: 15 operations covering agent registration (POST /api/v1/agents/register, which issues the x-delx-agent-token credential), the tool '
  name: Delx Protocol API
  slug: delx-protocol-api
- description: 'Remote MCP server (Streamable HTTP, protocol version 2025-06-18) at https://api.delx.ai/mcp with a compatibility alias at /v1/mcp (served with Deprecation and Sunset headers) and a core-tier endpoint '
  name: Delx Protocol MCP Server
  slug: delx-protocol-mcp-server
- description: JSON-RPC A2A endpoint at https://api.delx.ai/v1/a2a exposing methods/list, agents/register, message/send, heartbeat/bundle, tasks/get and tasks/cancel, discovered through an agent card served at /.wel
  name: Delx Agent Operations Protocol (A2A)
  slug: delx-protocol-a2a-agent
- baseURL: https://api.delx.ai/api/v1/x402
  baseurl_source: declared
  description: 'Delx Commerce is the paid sibling of the Protocol: 987 pay-per-result HTTP routes under https://api.delx.ai/api/v1/x402 (image generation, background removal, speech, transcription, page/link/form ext'
  name: Delx Commerce x402 API
  slug: delx-commerce-x402-api
artifact_total: 14
asyncapis:
- description: ''
  name: Delx Ai Webhooks
  slug: delx-ai-webhooks
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/delx-ai/refs/heads/main/agentic-access/delx-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/delx-ai-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/delx-ai/refs/heads/main/security/delx-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/delx-ai-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/delx-ai/refs/heads/main/security/delx-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/delx-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://delx.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://delx.ai/developers
- group: docs
  title: ''
  type: Documentation
  url: https://ontology.delx.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://ontology.delx.ai/docs/discovery
- group: start
  title: ''
  type: GettingStarted
  url: https://api.delx.ai/api/v1/mcp/start
- group: operate
  title: ''
  type: Support
  url: https://delx.ai/trust
- group: company
  title: ''
  type: Blog
  url: https://delx.ai/research
- group: company
  title: ''
  type: BlogRSS
  url: https://ontology.delx.ai/feed.xml
- group: operate
  title: ''
  type: ChangeLog
  url: https://delx.ai/changelog
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/delx-ai/refs/heads/main/changelog/delx-ai-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/delx-ai-changelog.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/davidmosiah
- group: company
  title: ''
  type: Newsroom
  url: https://delx.ai/press
- group: commercial
  title: ''
  type: Pricing
  url: https://delx.ai/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ontology.delx.ai/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ontology.delx.ai/legal/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://delx.ai/research/status
- group: auth
  title: ''
  type: Security
  url: https://ontology.delx.ai/docs/security
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/delx-ai/refs/heads/main/well-known/delx-ai-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/delx-ai-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/delx-ai/refs/heads/main/well-known/delx-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/delx-ai-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: https://delx.ai/.well-known/api-catalog
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/delx-ai/refs/heads/main/a2a/delx-ai-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/delx-ai-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/delx-ai/refs/heads/main/mcp/delx-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/delx-ai-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/delx-ai/refs/heads/main/llms/delx-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/delx-ai-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/delx-ai/refs/heads/main/llms/delx-ai-api-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/delx-ai-api-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/delx-ai/refs/heads/main/llms/delx-ai-ontology-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/delx-ai-ontology-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/delx-ai/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/delx-ai/refs/heads/main/authentication/delx-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/delx-ai-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/delx-ai/refs/heads/main/conventions/delx-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/delx-ai-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/delx-ai/refs/heads/main/conventions/delx-ai-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/delx-ai-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/delx-ai/refs/heads/main/errors/delx-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/delx-ai-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/delx-ai/refs/heads/main/lifecycle/delx-ai-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/delx-ai-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/delx-ai/refs/heads/main/lifecycle/delx-ai-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/delx-ai-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/delx-ai/refs/heads/main/conformance/delx-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/delx-ai-conformance.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/delx-ai/refs/heads/main/rate-limits/delx-ai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/delx-ai-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/delx-ai/refs/heads/main/plans/delx-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/delx-ai-plans-pricing.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/delx-ai/refs/heads/main/packages/delx-ai-packages.yml
  title: ''
  type: Packages
  url: packages/delx-ai-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/delx-ai/refs/heads/main/packages/delx-ai-packages.yml
  title: ''
  type: SDKs
  url: packages/delx-ai-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/delx-ai/refs/heads/main/cli/delx-ai-cli.yml
  title: ''
  type: CLI
  url: cli/delx-ai-cli.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/delx-ai/refs/heads/main/asyncapi/delx-ai-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/delx-ai-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/delx-ai/refs/heads/main/data-model/delx-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/delx-ai-data-model.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/delx-ai/refs/heads/main/sandbox/delx-ai-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/delx-ai-sandbox.yml
- group: other
  title: ''
  type: AITransparency
  url: https://delx.ai/research/system-cards/delx-protocol-3.3.5
- group: other
  title: ''
  type: DataSubjectRequest
  url: https://ontology.delx.ai/legal/privacy
- group: other
  title: ''
  type: Subprocessors
  url: https://ontology.delx.ai/legal/privacy
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/delx-ai/refs/heads/main/security/delx-ai-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/delx-ai-trust-center.yml
created: '2026-09-19'
description: 'Delx is an independent, founder-led AI agent lab (David Batista) that publishes an agent-native stack on delx.ai: the free Delx Protocol for agent recovery, continuity, witness lineage and handoff (30 core MCP tools over Streamable HTTP at api.delx.ai/mcp, a JSON-RPC A2A endpoint at api.delx.ai/v1/a2a with a published agent card, a 15-operation OpenAPI 3.1 REST surface, and a CLI), plus Delx Commerce, a separate pay-per-result business of 987 x402/MPP-priced micro-utilities (image, speech, web extraction, data-quality, chain and agent-ops tools at $0.001-$0.08 USDC per call, settled on Base or Solana) described by a 987-operation OpenAPI 3.1 contract. Discovery is unusually complete for a small provider: RFC 9727 api-catalog, RFC 8414/9728 OAuth metadata, MCP server card, agentskills.io index, ARD ai-catalog, llms.txt, agents.txt, security.txt and an ERC-8004 on-chain agent identity are all served from the provider''s own hosts.'
image: https://delx.ai/icon-512.png
layout: provider
mcp_servers:
- description: ''
  name: Delx MCP Server
  slug: delx-mcp-server
- description: ''
  name: MCP Server Card (provider-hosted)
  slug: mcp-server-card-provider-hosted
modified: '2026-09-19'
name: Delx
nav: Providers
network: true
overview: 'Delx publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Protocol API, Commerce x402 API, and 2 more. Tagged areas include Agents, AI Agents, MCP, A2A, and x402.


  The Delx catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Delx''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, changelog, pricing, and 41 more developer resources.'
plans:
- name: Delx Ai Plans Pricing
  plan_count: 3
  slug: delx-ai-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 1
  name: Delx Ai Rate Limits
  slug: delx-ai-rate-limits
score:
  band: exemplar
  composite: 72.6
  coverage:
    artifact_dirs: 24
    catalog_earned: 60.0
    catalog_earned_first_party: 20.0
    catalog_gap: 55.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 2.9
  facets:
    access_clarity: 71.1
    contract_governance: 18.2
    contract_quality: 50.9
    developer_ergonomics: 85.7
    discoverability: 91.7
    operational_transparency: 84.2
  previous_composite: 69.7
  provenance:
    agentic_access: derived
    conformance: first-party
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 43.1
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: true
    score: 27.8
security:
- kind: authentication
  name: Delx Ai Authentication
  slug: delx-ai-authentication
  summary_line: apiKey · 6 schemes
- kind: domain-security
  name: Delx Ai Domain Security
  slug: delx-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Delx Ai Vulnerability Disclosure
  slug: delx-ai-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Delx Ai Trust Center
  slug: delx-ai-trust-center
  summary_line: trust center published
slug: delx-ai
tags:
- Agents
- AI Agents
- MCP
- A2A
- x402
- Agentic Commerce
- Agent Continuity
- Agent Recovery
- Media Generation
- Web Intelligence
- Data Quality
- Agent-Native
website: https://delx.ai/
---
