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
    event_surface_described: false
    idempotency: documented
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 42.9
  scored_at: '2026-09-20'
agentic_access:
- acting_count: 62
  human_in_the_loop: 0
  name: Connskill Com Agentic Access
  operation_count: 88
  slug: connskill-com-agentic-access
  summary_line: 88 operations · 62 acting
api_count: 1
apis:
- baseURL: https://agent.connskill.com
  baseurl_source: declared
  description: 'Pay-per-call REST API for AI agents on agent.connskill.com: Google SERP snapshots, keyword metrics/ideas/difficulty, ranked keywords, backlinks, competitors, site and page audits, Google Trends, AI se'
  name: CONNSKILL Growth Services API
  slug: connskill-growth-services-api
- description: 'Model Context Protocol surface for the same catalogue: a hosted Streamable-HTTP endpoint at agent.connskill.com/mcp (protocol 2025-06-18, serverInfo connskill-growth-services 0.2.1, POST-only, 78 tool'
  name: CONNSKILL Growth Services MCP Server
  slug: connskill-growth-services-mcp-server
- description: A2A merchant agent (protocolVersion 0.3.0, JSON-RPC at agent.connskill.com/a2a) whose card at /.well-known/agent-card.json (also served at the legacy /.well-known/agent.json) lists 47 skills mirroring
  name: CONNSKILL Growth Services A2A Agent
  slug: connskill-growth-services-a2a-agent
artifact_total: 10
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/connskill-com/refs/heads/main/agentic-access/connskill-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/connskill-com-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/connskill-com/refs/heads/main/security/connskill-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/connskill-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://connskill.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://agent.connskill.com/
- group: docs
  title: ''
  type: Documentation
  url: https://agent.connskill.com/
- group: docs
  title: ''
  type: APIReference
  url: https://agent.connskill.com/pricing
- group: start
  title: ''
  type: GettingStarted
  url: https://agent.connskill.com/prompts
- group: operate
  title: ''
  type: Support
  url: https://agent.connskill.com/support
- group: company
  title: ''
  type: Blog
  url: https://agent.connskill.com/news
- group: company
  title: ''
  type: Newsroom
  url: https://connskill.com/news/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CONN-SKILL
- group: commercial
  title: ''
  type: Pricing
  url: https://agent.connskill.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://connskill.com/agb/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agent.connskill.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://agent.connskill.com/status
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/connskill-com/refs/heads/main/changelog/connskill-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/connskill-com-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://agent.connskill.com/news
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/connskill-com/refs/heads/main/lifecycle/connskill-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/connskill-com-lifecycle.yml
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/connskill-com/refs/heads/main/openapi/connskill-com-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/connskill-com-openapi.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/connskill-com/refs/heads/main/overlays/connskill-com-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/connskill-com-openapi-overlay.yaml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/connskill-com/refs/heads/main/authentication/connskill-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/connskill-com-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/connskill-com/refs/heads/main/conventions/connskill-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/connskill-com-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/connskill-com/refs/heads/main/conventions/connskill-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/connskill-com-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/connskill-com/refs/heads/main/errors/connskill-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/connskill-com-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/connskill-com/refs/heads/main/conformance/connskill-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/connskill-com-conformance.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/connskill-com/refs/heads/main/rate-limits/connskill-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/connskill-com-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/connskill-com/refs/heads/main/plans/connskill-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/connskill-com-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/connskill-com/refs/heads/main/data-model/connskill-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/connskill-com-data-model.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/connskill-com/refs/heads/main/packages/connskill-com-packages.yml
  title: ''
  type: Packages
  url: packages/connskill-com-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/connskill-com/refs/heads/main/packages/connskill-com-packages.yml
  title: ''
  type: SDKs
  url: packages/connskill-com-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/connskill-com/refs/heads/main/cli/connskill-com-cli.yml
  title: ''
  type: CLI
  url: cli/connskill-com-cli.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/connskill-com/refs/heads/main/mcp/connskill-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/connskill-com-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/connskill-com/refs/heads/main/mcp/connskill-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/connskill-com-tool-crosswalk.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/connskill-com/refs/heads/main/a2a/connskill-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/connskill-com-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/connskill-com/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/connskill-com/refs/heads/main/llms/connskill-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/connskill-com-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/connskill-com/refs/heads/main/well-known/connskill-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/connskill-com-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/connskill-com/refs/heads/main/regulatory/connskill-com-regulatory-posture.yml
  title: ''
  type: DataResidency
  url: regulatory/connskill-com-regulatory-posture.yml
- group: other
  title: ''
  type: DataSubjectRequest
  url: https://agent.connskill.com/privacy
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/connskill-com/refs/heads/main/regulatory/connskill-com-regulatory-posture.yml
  title: ''
  type: RegulatoryPosture
  url: regulatory/connskill-com-regulatory-posture.yml
created: '2026-09-19'
description: CONNSKILL GmbH & Co. KG is a web design, branding and marketing agency in Traunstein, Germany (HRA 14164, Amtsgericht Traunstein) that also builds and operates CONNSKILL Growth Services at agent.connskill.com — a pay-per-call marketplace for AI agents. It sells Google SERP and keyword research data, site audits, backlinks and competitor intelligence, SMS verification numbers and US number rentals, receive-only e-mail inboxes, social marketing orders, OpenAI-compatible LLM chat and embeddings hosted in Germany, x402 seller trust checks, leak exposure and domain security grades, read-only EVM chain data and cookieless website analytics, plus a free marketplace layer (wishlist, job board, curated x402 directory, published conformance reports). Every call is priced individually and paid in USDC on Base via x402 with no account or API key. The surface is published as OpenAPI 3.1, an A2A agent card, a hosted MCP endpoint and an npm MCP server, llms.txt, ai-plugin.json and an x402
  discovery document.
image: https://agent.connskill.com/icon.png
layout: provider
mcp_servers:
- description: 'CONNSKILL ships the same tool surface two ways: a hosted Streamable-HTTP MCP endpoint at https://agent.connskill.com/mcp (POST-only JSON-RPC; a GET answers 405 {"error":"streamable_http_post_only"}; s'
  name: MCP manifest (hosted Streamable HTTP + npm stdio; live tools/list captured)
  slug: mcp-manifest-hosted-streamable-http-npm-stdio-live-toolslist-captured
- description: ''
  name: Hosted MCP endpoint (POST JSON-RPC; tools/list open, paid tools via x402)
  slug: hosted-mcp-endpoint-post-json-rpc-toolslist-open-paid-tools-via-x402
modified: '2026-09-19'
name: CONNSKILL GmbH & Co. KG
nav: Providers
network: true
overview: 'CONNSKILL GmbH & Co. KG publishes 1 API on the [APIs.io](https://apis.io/) network: CONNSKILL Growth Services API. Tagged areas include Company, API Provider, SEO, SERP, and Keyword Research.


  CONNSKILL GmbH & Co. KG''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, changelog, and 33 more developer resources.'
plans:
- name: Connskill Com Plans Pricing
  plan_count: 8
  slug: connskill-com-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 2
  name: Connskill Com Rate Limits
  slug: connskill-com-rate-limits
score:
  band: strong
  composite: 58.9
  coverage:
    artifact_dirs: 21
    catalog_earned: 57.0
    catalog_earned_first_party: 20.0
    catalog_gap: 58.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 53.9
  facets:
    access_clarity: 63.2
    contract_governance: 18.2
    contract_quality: 51.7
    developer_ergonomics: 78.6
    discoverability: 75.9
    operational_transparency: 57.9
  previous_composite: 5.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 39.1
  schema_version: 0.22.0
  scored_at: '2026-09-20'
  trend: rising
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Connskill Com Authentication
  slug: connskill-com-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Connskill Com Domain Security
  slug: connskill-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: connskill-com
tags:
- Company
- API Provider
- SEO
- SERP
- Keyword Research
- x402
- Agent Payments
- AI Agents
- MCP
- A2A
- SMS Verification
- LLM Inference
- Social Media Marketing
- Web Analytics
- Blockchain Data
- Marketing Agency
- Germany
website: https://connskill.com/
---
