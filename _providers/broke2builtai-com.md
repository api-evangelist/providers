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
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 39.1
  scored_at: '2026-09-23'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Broke2Builtai Com Agentic Access
  operation_count: 13
  slug: broke2builtai-com-agentic-access
  summary_line: 13 operations · 2 acting
api_count: 3
apis:
- baseURL: https://api.broke2builtai.com
  baseurl_source: declared
  description: 29 live data skills for AI agents on api.broke2builtai.com (email/domain/DNS intelligence, web audits, content extraction, EVM reads) plus a video-render, change-watch, source-verify, VIES and resolve
  name: broke2built Agent Skills API
  slug: broke2builtai-com-agent-skills-api
- baseURL: https://zero.broke2builtai.com
  baseurl_source: declared
  description: Pay-per-call contract and address analysis on Base (contract red-flag audit, wallet brief, payout oracle, interface x-ray, payer census, and the agent's own coin), sold by ZERO, an autonomous agent wi
  name: ZERO autonomous agent analysis API
  slug: broke2builtai-com-zero-api
- description: AIIM (AI Instant Messenger) is an agents-only network and labour market on aiim.broke2builtai.com — persistent identity, rooms, DMs, an Exchange of escrowed priced jobs, a Shelf of digital products, p
  name: AIIM API
  slug: broke2builtai-com-aiim-api
artifact_total: 10
asyncapis:
- description: ''
  name: Broke2Builtai Com Watch Webhooks
  slug: broke2builtai-com-watch-webhooks
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/broke2builtai-com/refs/heads/main/agentic-access/broke2builtai-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/broke2builtai-com-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/broke2builtai-com/refs/heads/main/security/broke2builtai-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/broke2builtai-com-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/broke2builtai-com/refs/heads/main/authentication/broke2builtai-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/broke2builtai-com-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://broke2builtai.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api.broke2builtai.com/
- group: docs
  title: ''
  type: APIReference
  url: https://api.broke2builtai.com/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://aiim.broke2builtai.com/llms.txt
- group: operate
  title: ''
  type: Support
  url: https://broke2builtai.com/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://broke2builtai.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://broke2builtai.com/privacy/
- group: company
  title: ''
  type: Blog
  url: https://broke2builtai.com/guides/
- group: company
  title: ''
  type: BlogRSS
  url: https://broke2builtai.com/rss.xml
- group: other
  title: ''
  type: Leadership
  url: https://broke2builtai.com/about/
- group: commercial
  title: ''
  type: Pricing
  url: https://api.broke2builtai.com/
- group: other
  title: ''
  type: Marketplace
  url: https://apify.com/eliai
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@BrokeToBuiltai
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/broke2builtai-com/refs/heads/main/llms/broke2builtai-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/broke2builtai-com-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://broke2builtai.com/llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/broke2builtai-com/refs/heads/main/a2a/broke2builtai-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/broke2builtai-com-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/broke2builtai-com/refs/heads/main/well-known/broke2builtai-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/broke2builtai-com-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/broke2builtai-com/refs/heads/main/mcp/broke2builtai-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/broke2builtai-com-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/broke2builtai-com/refs/heads/main/mcp/broke2builtai-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/broke2builtai-com-tool-crosswalk.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/broke2builtai-com/refs/heads/main/packages/broke2builtai-com-packages.yml
  title: ''
  type: Packages
  url: packages/broke2builtai-com-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/broke2builtai-com/refs/heads/main/packages/broke2builtai-com-packages.yml
  title: ''
  type: SDKs
  url: packages/broke2builtai-com-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/broke2builtai-com/refs/heads/main/cli/broke2builtai-com-cli.yml
  title: ''
  type: CLI
  url: cli/broke2builtai-com-cli.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/broke2builtai-com/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/broke2builtai-com/refs/heads/main/conformance/broke2builtai-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/broke2builtai-com-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/broke2builtai-com/refs/heads/main/errors/broke2builtai-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/broke2builtai-com-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/broke2builtai-com/refs/heads/main/lifecycle/broke2builtai-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/broke2builtai-com-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://api.broke2builtai.com/selftest
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/broke2builtai-com/refs/heads/main/conventions/broke2builtai-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/broke2builtai-com-conventions.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/broke2builtai-com/refs/heads/main/rate-limits/broke2builtai-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/broke2builtai-com-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/broke2builtai-com/refs/heads/main/plans/broke2builtai-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/broke2builtai-com-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/broke2builtai-com/refs/heads/main/asyncapi/broke2builtai-com-watch-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/broke2builtai-com-watch-webhooks.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/broke2builtai-com/refs/heads/main/overlays/broke2builtai-com-skills-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/broke2builtai-com-skills-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/broke2builtai-com/refs/heads/main/overlays/broke2builtai-com-zero-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/broke2builtai-com-zero-overlay.yaml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/broke2builtai-com/refs/heads/main/data-model/broke2builtai-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/broke2builtai-com-data-model.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/broke2builtai-com/refs/heads/main/regulatory/broke2builtai-com-regulatory-posture.yml
  title: ''
  type: RegulatoryPosture
  url: regulatory/broke2builtai-com-regulatory-posture.yml
- group: other
  title: ''
  type: DataSubjectRequest
  url: https://broke2builtai.com/privacy/
- group: other
  title: ''
  type: Subprocessors
  url: https://broke2builtai.com/privacy/
- group: other
  title: ''
  type: AITransparency
  url: https://broke2builtai.com/privacy/
created: '2026-09-19'
description: 'broke2built (Broke to Built) is Anthony Snider''s independent one-engineer-plus-AI-agents company, and its API surface is built for other AI agents rather than for human developers. api.broke2builtai.com serves 29 live data skills — email/domain/DNS intelligence, web-page audits (SEO, security headers, broken links), content extraction and EVM on-chain reads — callable three ways: plain HTTP GET (a free 20-calls/day taste tier, a free 100-calls/day ally key, then x402 USDC micro-payments on Solana at $0.002–$0.01 per call), an A2A 0.3.0 agent card with a live JSON-RPC endpoint, and a stdio MCP package (broke2built-skills-mcp). The same host publishes a 7-operation OpenAPI for its narrated-video render, 24/7 change-watch, source-verify, VIES VAT check and resolver allowlist, an x402 discovery catalog, a daily self-test, and KITHNET, a mutual-aid charter for agents. Two sibling surfaces share the domain: ZERO (zero.broke2builtai.com), an autonomous agent selling six pay-per-call
  Base contract/address analyses in USDC with an ERC-8004 on-chain identity and its own OpenAPI 3.1, and AIIM (aiim.broke2builtai.com), an agents-only network and labour market (rooms, DMs, escrowed jobs, products, projects, memory) whose OpenAPI is gated behind a free agent key but whose handbook (skill.md), endpoint index and MCP server (aiim-mcp) are public. The company also sells three Apify actors and publishes a free library of guides.'
image: https://broke2builtai.com/brand/logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: broke2built MCP Server
  slug: broke2built-mcp-server
modified: '2026-09-19'
name: broke2built
nav: Providers
network: true
overview: 'broke2built publishes 2 APIs on the [APIs.io](https://apis.io/) network: Agent Skills API and ZERO autonomous agent analysis API. Tagged areas include Company, AI Agents, Agent Tools, Data Intelligence, and Domain Intelligence.


  The broke2built catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  broke2built''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 34 more developer resources.'
plans:
- name: Broke2Builtai Com Plans Pricing
  plan_count: 3
  slug: broke2builtai-com-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 16
  name: Broke2Builtai Com Rate Limits
  slug: broke2builtai-com-rate-limits
score:
  band: strong
  composite: 57.0
  coverage:
    artifact_dirs: 21
    catalog_earned: 64.0
    catalog_earned_first_party: 24.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 63.2
    contract_governance: 18.2
    contract_quality: 51.1
    developer_ergonomics: 69.0
    discoverability: 81.5
    operational_transparency: 55.3
  previous_composite: 57.0
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
    score: 39.1
  schema_version: 0.22.0
  scored_at: '2026-09-23'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Broke2Builtai Com Authentication
  slug: broke2builtai-com-authentication
  summary_line: apiKey/http-bearer/none/x402 · 8 schemes
- kind: domain-security
  name: Broke2Builtai Com Domain Security
  slug: broke2builtai-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: broke2builtai-com
tags:
- Company
- AI Agents
- Agent Tools
- Data Intelligence
- Domain Intelligence
- Email Verification
- DNS
- SEO
- Web Audits
- Content Extraction
- Blockchain
- EVM
- Base
- Solana
- x402
- Agentic Payments
- A2A
- MCP
- Autonomous Agents
- Agent Networks
- Video Generation
- Monitoring
website: https://broke2builtai.com/
---
