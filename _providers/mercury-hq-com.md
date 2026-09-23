---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: conformant
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 38.0
  scored_at: '2026-09-23'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Mercury Hq Com Agentic Access
  operation_count: 19
  slug: mercury-hq-com-agentic-access
  summary_line: 19 operations
api_count: 1
apis:
- baseURL: https://network.mercury-hq.com
  baseurl_source: declared
  description: REST/JSON API (OpenAPI 3.1.0, info.title "MERCURY x402 storefront", x-spec mercury-storefront/1) of 19 GET routes under /buy/*, one per Cited web-data service, each declaring its price in x-payment-in
  name: MERCURY x402 Storefront API
  slug: mercury-x402-storefront-api
- description: 'Agent-to-Agent (A2A 0.3.0) surface for "MERCURY Web Fetch", published as a conformant agent card at https://network.mercury-hq.com/.well-known/agent-card.json (and the legacy /.well-known/agent.json, '
  name: MERCURY Web Fetch A2A Agent
  slug: mercury-web-fetch-a2a-agent
- description: Hosted Model Context Protocol server (serverInfo mercury-x402 1.0.0, protocolVersion 2025-06-18, streamable HTTP, JSON-RPC 2.0 over POST https://network.mercury-hq.com/mcp) exposing 18 tools that mirr
  name: MERCURY MCP Server
  slug: mercury-mcp-server
artifact_total: 11
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/mercury-hq-com/refs/heads/main/security/mercury-hq-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/mercury-hq-com-vulnerability-disclosure.yml
- group: company
  title: ''
  type: Website
  url: https://mercury-hq.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://network.mercury-hq.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://network.mercury-hq.com/university
- group: docs
  title: ''
  type: APIReference
  url: https://network.mercury-hq.com/university/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://network.mercury-hq.com/university/developers
- group: commercial
  title: ''
  type: Pricing
  url: https://network.mercury-hq.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://network.mercury-hq.com/developers
- group: commercial
  title: ''
  type: TermsOfService
  url: https://network.mercury-hq.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://network.mercury-hq.com/privacy
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/mercury-hq-com/refs/heads/main/llms/mercury-hq-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/mercury-hq-com-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/mercury-hq-com/refs/heads/main/a2a/mercury-hq-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/mercury-hq-com-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/mercury-hq-com/refs/heads/main/mcp/mercury-hq-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/mercury-hq-com-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/mercury-hq-com/refs/heads/main/mcp/mercury-hq-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/mercury-hq-com-tool-crosswalk.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/mercury-hq-com/refs/heads/main/packages/mercury-hq-com-packages.yml
  title: ''
  type: Packages
  url: packages/mercury-hq-com-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/mercury-hq-com/refs/heads/main/well-known/mercury-hq-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/mercury-hq-com-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/mercury-hq-com/refs/heads/main/well-known/mercury-hq-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/mercury-hq-com-security.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/mercury-hq-com/refs/heads/main/overlays/mercury-hq-com-x402-storefront-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/mercury-hq-com-x402-storefront-overlay.yaml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/mercury-hq-com/refs/heads/main/conformance/mercury-hq-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/mercury-hq-com-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/mercury-hq-com/refs/heads/main/errors/mercury-hq-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/mercury-hq-com-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/mercury-hq-com/refs/heads/main/lifecycle/mercury-hq-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/mercury-hq-com-lifecycle.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/mercury-hq-com/refs/heads/main/authentication/mercury-hq-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/mercury-hq-com-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/mercury-hq-com/refs/heads/main/security/mercury-hq-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mercury-hq-com-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/mercury-hq-com/refs/heads/main/security/mercury-hq-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/mercury-hq-com-trust-center.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/mercury-hq-com/refs/heads/main/sandbox/mercury-hq-com-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/mercury-hq-com-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/mercury-hq-com/refs/heads/main/conventions/mercury-hq-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/mercury-hq-com-conventions.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/mercury-hq-com/refs/heads/main/changelog/mercury-hq-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/mercury-hq-com-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/mercury-hq-com/refs/heads/main/data-model/mercury-hq-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/mercury-hq-com-data-model.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/mercury-hq-com/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/mercury-hq-com/refs/heads/main/plans/mercury-hq-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/mercury-hq-com-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/mercury-hq-com/refs/heads/main/rate-limits/mercury-hq-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/mercury-hq-com-rate-limits.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/mercury-hq-com/refs/heads/main/agentic-access/mercury-hq-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/mercury-hq-com-agentic-access.yml
- group: auth
  title: ''
  type: Security
  url: https://network.mercury-hq.com/.well-known/security.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/mercury-hq-com/refs/heads/main/regulatory/mercury-hq-com-regulatory-posture.yml
  title: ''
  type: RegulatoryPosture
  url: regulatory/mercury-hq-com-regulatory-posture.yml
created: '2026-09-19'
description: 'MERCURY (Mercury Holdings Pty Ltd, Queensland, Australia) runs an agent-payable web-data network at network.mercury-hq.com: 19 live "Cited" services - verifiable web fetch, LLM-ready markdown, structured extract, metadata, link graph, robots/AI-crawler audit, diff, notarize, security-headers audit, table, feed, availability, JSON Schema validate, Merkle batch, sitemap, DNS snapshot, readability and redirect resolution - each sold per call over HTTP 402 (x402, USDC on Base mainnet eip155:8453) and each returning an EIP-191 signed provenance receipt verifiable offline against a pinned key. Three doors reach the same routes: keyless x402 micropayments, a Mercury API key (free sandbox and paid tiers), and a hosted MCP server whose tools/list is free. Discovery is machine-first: OpenAPI 3.1, llms.txt, /catalog, /.well-known/x402, a conformant A2A 0.3.0 agent card, an ERC-8004 registration and security.txt. The provider states it is early and has no external buyers yet.'
image: https://network.mercury-hq.com/favicon.svg
layout: provider
mcp_servers:
- description: 'MERCURY ships a real, hosted Model Context Protocol server AND a first-party stdio package. The hosted server at https://network.mercury-hq.com/mcp answers GET with a descriptor ({name: mercury-x402, '
  name: MERCURY MCP Server
  slug: mercury-mcp-server
modified: '2026-09-19'
name: MERCURY
nav: Providers
network: true
overview: 'MERCURY publishes 1 API on the [APIs.io](https://apis.io/) network: x402 Storefront API. Tagged areas include Company, Agents, A2A, MCP, and x402.


  MERCURY''s developer surface includes documentation, API reference, getting-started guide, pricing, signup flow, authentication, sandbox, and 27 more developer resources.'
plans:
- name: Mercury Hq Com Plans Pricing
  plan_count: 4
  slug: mercury-hq-com-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 6
  name: Mercury Hq Com Rate Limits
  slug: mercury-hq-com-rate-limits
score:
  band: strong
  composite: 61.9
  coverage:
    artifact_dirs: 21
    catalog_earned: 61.0
    catalog_earned_first_party: 24.0
    catalog_gap: 54.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 49.7
    developer_ergonomics: 58.9
    discoverability: 75.9
    operational_transparency: 57.9
  previous_composite: 61.9
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
    score: 56.3
  schema_version: 0.22.0
  scored_at: '2026-09-23'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
security:
- kind: authentication
  name: Mercury Hq Com Authentication
  slug: mercury-hq-com-authentication
  summary_line: x402-payment/apiKey/none · 5 schemes
- kind: domain-security
  name: Mercury Hq Com Domain Security
  slug: mercury-hq-com-domain-security
  summary_line: TLSv1.3
- kind: vulnerability-disclosure
  name: Mercury Hq Com Vulnerability Disclosure
  slug: mercury-hq-com-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Mercury Hq Com Trust Center
  slug: mercury-hq-com-trust-center
  summary_line: trust center published
slug: mercury-hq-com
tags:
- Company
- Agents
- A2A
- MCP
- x402
- HTTP 402
- Machine Payments
- Web Data
- Web Scraping
- Data Extraction
- Provenance
- Stablecoins
- Artificial Intelligence
website: https://mercury-hq.com/
---
