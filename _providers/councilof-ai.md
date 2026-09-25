---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 39.5
  scored_at: '2026-09-24'
api_count: 2
apis:
- baseURL: https://councilof.ai/api
  baseurl_source: declared
  description: 'Keyless REST API for the GSPC measurement estate: the living board (GET /api/gspc, one axis via ?axis=), the quotable live state, axis register, methodology, signed-card and commission indexes, public'
  name: Council of AI Public API
  slug: council-of-ai-public-api
- description: Remote Model Context Protocol server at https://councilof.ai/mcp (Streamable HTTP, protocol 2025-06-18, serverInfo csoai-gspc-mcp 1.4.2) with a stdio twin on npm (csoai-gspc-mcp 0.2.2, "npx -y csoai-g
  name: Council of AI GSPC MCP Server
  slug: council-of-ai-gspc-mcp-server
- description: 'Agent2Agent v1.0 surface: an agent card served from https://councilof.ai/.well-known/agent-card.json (application/a2a+json, version 1.1.0, supportedInterfaces[0] JSONRPC 1.0 at https://councilof.ai/ap'
  name: Council of AI Measurement Agent (A2A)
  slug: council-of-ai-measurement-agent-a2a
artifact_total: 11
asyncapis:
- description: ''
  name: Councilof Ai Webhooks
  slug: councilof-ai-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://councilof.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://councilof.ai/api-docs/
- group: docs
  title: ''
  type: Documentation
  url: https://councilof.ai/api-docs/
- group: docs
  title: ''
  type: APIReference
  url: https://councilof.ai/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://councilof.ai/quickstart/
- group: operate
  title: ''
  type: Support
  url: https://councilof.ai/help-center/
- group: company
  title: ''
  type: Blog
  url: https://councilof.ai/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://councilof.ai/api/x402
- group: start
  title: ''
  type: Login
  url: https://councilof.ai/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://councilof.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://councilof.ai/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://councilof.ai/status/
- group: operate
  title: ''
  type: ChangeLog
  url: https://councilof.ai/feeds/corrections.xml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/councilof-ai/refs/heads/main/changelog/councilof-ai-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/councilof-ai-changelog.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/councilof-ai/refs/heads/main/llms/councilof-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/councilof-ai-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://councilof.ai/llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/councilof-ai/refs/heads/main/a2a/councilof-ai-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/councilof-ai-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/councilof-ai/refs/heads/main/mcp/councilof-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/councilof-ai-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/councilof-ai/refs/heads/main/mcp/councilof-ai-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/councilof-ai-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/councilof-ai/refs/heads/main/well-known/councilof-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/councilof-ai-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/councilof-ai/refs/heads/main/well-known/councilof-ai-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/councilof-ai-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/councilof-ai/refs/heads/main/security/councilof-ai-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/councilof-ai-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/councilof-ai/refs/heads/main/security/councilof-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/councilof-ai-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/councilof-ai/refs/heads/main/security/councilof-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/councilof-ai-domain-security.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/councilof-ai/refs/heads/main/packages/councilof-ai-packages.yml
  title: ''
  type: Packages
  url: packages/councilof-ai-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/councilof-ai/refs/heads/main/packages/councilof-ai-packages.yml
  title: ''
  type: SDKs
  url: packages/councilof-ai-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/councilof-ai/refs/heads/main/cli/councilof-ai-cli.yml
  title: ''
  type: CLI
  url: cli/councilof-ai-cli.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/councilof-ai/refs/heads/main/components/councilof-ai-components.yml
  title: ''
  type: Components
  url: components/councilof-ai-components.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/councilof-ai/refs/heads/main/authentication/councilof-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/councilof-ai-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/councilof-ai/refs/heads/main/conventions/councilof-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/councilof-ai-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/councilof-ai/refs/heads/main/errors/councilof-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/councilof-ai-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/councilof-ai/refs/heads/main/data-model/councilof-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/councilof-ai-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/councilof-ai/refs/heads/main/conformance/councilof-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/councilof-ai-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/councilof-ai/refs/heads/main/lifecycle/councilof-ai-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/councilof-ai-lifecycle.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/councilof-ai/refs/heads/main/plans/councilof-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/councilof-ai-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/councilof-ai/refs/heads/main/rate-limits/councilof-ai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/councilof-ai-rate-limits.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/councilof-ai/refs/heads/main/sandbox/councilof-ai-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/councilof-ai-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/councilof-ai/refs/heads/main/asyncapi/councilof-ai-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/councilof-ai-webhooks.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/councilof-ai/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: AITransparency
  url: https://councilof.ai/ai-transparency/
- group: other
  title: ''
  type: DataSubjectRequest
  url: https://councilof.ai/privacy
- group: other
  title: ''
  type: Subprocessors
  url: https://councilof.ai/privacy
created: '2026-09-19'
description: 'CSOAI Ltd — public name Council of AI (UK Companies House 16939677, London; second domain csoai.org) — is an independent AI-governance MEASUREMENT body: "measurement, not certification". It publishes the living GSPC board (Governance · Safety · Provenance · Continuity) as a keyless, CORS-open JSON API, Ed25519-signed measurement cards verifiable offline against a did:web:csoai.org key document, a Merkle public root with inclusion proofs, an EU AI Act Article 50 machine-marking detector, and a dated corrections ledger. The estate is exposed to agents three ways: a 141-operation OpenAPI 3.1 contract at https://councilof.ai/openapi.json (plus a 7-operation read-surfaces spec), a remote MCP server at https://councilof.ai/mcp (13 tools with anonymous tools/list; npm stdio twin csoai-gspc-mcp; MCP Registry io.github.CSOAI-ORG/gspc), and an A2A v1.0 agent card at /.well-known/agent-card.json with eight skills. Ten REST doors and four MCP tools are metered per artefact by x402 (USDC
  on Base, amounts only inside the 402 challenge); the board, verification and every preview are free and need no account.'
image: https://councilof.ai/og-image.png
layout: provider
mcp_servers:
- description: ''
  name: Council of AI MCP Server
  slug: council-of-ai-mcp-server
- description: ''
  name: GSPC MCP endpoint (Streamable HTTP)
  slug: gspc-mcp-endpoint-streamable-http
modified: '2026-09-19'
name: Council of AI
nav: Providers
network: true
overview: 'Council of AI publishes 1 API on the [APIs.io](https://apis.io/) network: Public API. Tagged areas include AI Governance, AI Measurement, AI Safety, EU AI Act, and Compliance.


  The Council of AI catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Council of AI''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, changelog, and 35 more developer resources.'
plans:
- name: Councilof Ai Plans Pricing
  plan_count: 0
  slug: councilof-ai-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 0
  name: Councilof Ai Rate Limits
  slug: councilof-ai-rate-limits
score:
  band: developing
  composite: 52.6
  coverage:
    artifact_dirs: 23
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    contract_governance: 18.2
    contract_quality: 48.1
    developer_ergonomics: 80.4
    discoverability: 75.9
    operational_transparency: 50.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-kingdom
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - united-kingdom-ireland
  previous_composite: 52.6
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Councilof Ai Authentication
  slug: councilof-ai-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Councilof Ai Domain Security
  slug: councilof-ai-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Councilof Ai Vulnerability Disclosure
  slug: councilof-ai-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: councilof-ai
tags:
- AI Governance
- AI Measurement
- AI Safety
- EU AI Act
- Compliance
- Provenance
- Agents
- A2A
- MCP
- x402
- Agentic Commerce
- Agent-Native
- United Kingdom
website: https://councilof.ai/
---
