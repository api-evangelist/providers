---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: documented
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 46.4
  scored_at: '2026-09-20'
agentic_access:
- acting_count: 17
  human_in_the_loop: 2
  name: Xguardgate Com Agentic Access
  operation_count: 50
  slug: xguardgate-com-agentic-access
  summary_line: 50 operations · 17 acting · 2 human-in-the-loop
api_count: 4
apis:
- baseURL: https://api.xguardgate.com
  baseurl_source: declared
  description: The REST surface behind every XGuard product, published as OpenAPI 3.1.0 (info.version 5.1.0, 47 paths, 49 operations, servers[] https://api.xguardgate.com) at https://api.xguardgate.com/openapi.json.
  name: XGuard Universal Paid AI Agent + Secretless Gateway API
  slug: xguard-universal-paid-agent-api
- description: Remote Model Context Protocol server at https://api.xguardgate.com/mcp (Streamable HTTP, protocol version 2026-07-28, serverInfo xguard-universal-paid-secretless-gateway 5.1.0). initialize and tools/l
  name: XGuard MCP Server
  slug: xguard-mcp-server
- description: 'Agent2Agent surface: an agent card served identically from https://api.xguardgate.com/.well-known/agent-card.json (the canonical location named in the provider''s own xguard.json manifest) and from xgu'
  name: XGuard A2A Agent
  slug: xguard-a2a-agent
- baseURL: https://reconcile.xguardgate.com
  baseurl_source: declared
  description: 'A one-operation companion service at https://reconcile.xguardgate.com that resolves ambiguous x402 Base USDC settlements after a facilitator timeout: GET /v1/reconcile?from=0x...&nonce=0x... checks th'
  name: XGuard Reconcile API
  slug: xguard-reconcile-api
artifact_total: 12
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/xguardgate-com/refs/heads/main/security/xguardgate-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/xguardgate-com-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/xguardgate-com/refs/heads/main/security/xguardgate-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/xguardgate-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://xguardgate.com/
- group: docs
  title: ''
  type: Documentation
  url: https://xguardgate.com/developers
- group: start
  title: ''
  type: GettingStarted
  url: https://xguardgate.com/connect
- group: docs
  title: ''
  type: APIReference
  url: https://api.xguardgate.com/openapi.json
- group: other
  title: ''
  type: Playground
  url: https://xguardgate.com/try
- group: commercial
  title: ''
  type: Pricing
  url: https://xguardgate.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://xguardgate.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://xguardgate.com/privacy
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://xguardgate.com/security
- group: build
  title: ''
  type: GitHub
  url: https://github.com/moelayyan90/XGuard
- group: operate
  title: ''
  type: Releases
  url: https://github.com/moelayyan90/XGuard/releases
- group: operate
  title: ''
  type: Support
  url: https://github.com/moelayyan90/XGuard/issues
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/xguardgate-com/refs/heads/main/llms/xguardgate-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/xguardgate-com-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://xguardgate.com/llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/xguardgate-com/refs/heads/main/well-known/xguardgate-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/xguardgate-com-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/xguardgate-com/refs/heads/main/well-known/xguardgate-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/xguardgate-com-security.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/xguardgate-com/refs/heads/main/a2a/xguardgate-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/xguardgate-com-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/xguardgate-com/refs/heads/main/mcp/xguardgate-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/xguardgate-com-mcp.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/xguardgate-com/refs/heads/main/authentication/xguardgate-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/xguardgate-com-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/xguardgate-com/refs/heads/main/conventions/xguardgate-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/xguardgate-com-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/xguardgate-com/refs/heads/main/conventions/xguardgate-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/xguardgate-com-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/xguardgate-com/refs/heads/main/errors/xguardgate-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/xguardgate-com-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/xguardgate-com/refs/heads/main/lifecycle/xguardgate-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/xguardgate-com-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/xguardgate-com/refs/heads/main/conformance/xguardgate-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/xguardgate-com-conformance.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/xguardgate-com/refs/heads/main/plans/xguardgate-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/xguardgate-com-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/xguardgate-com/refs/heads/main/rate-limits/xguardgate-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/xguardgate-com-rate-limits.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/xguardgate-com/refs/heads/main/changelog/xguardgate-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/xguardgate-com-changelog.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/xguardgate-com/refs/heads/main/packages/xguardgate-com-packages.yml
  title: ''
  type: Packages
  url: packages/xguardgate-com-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/xguardgate-com/refs/heads/main/packages/xguardgate-com-packages.yml
  title: ''
  type: SDKs
  url: packages/xguardgate-com-packages.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/xguardgate-com/refs/heads/main/sandbox/xguardgate-com-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/xguardgate-com-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/xguardgate-com/refs/heads/main/data-model/xguardgate-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/xguardgate-com-data-model.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/xguardgate-com/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/xguardgate-com/refs/heads/main/security/xguardgate-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/xguardgate-com-vulnerability-disclosure.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/xguardgate-com/refs/heads/main/agentic-access/xguardgate-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/xguardgate-com-agentic-access.yml
created: '2026-09-19'
description: 'XGuard is a paid-tool and credential-brokering gateway for AI agents, operated from xguardgate.com with its API at api.xguardgate.com and its source published at github.com/moelayyan90/XGuard (Apache-2.0, Cloudflare Workers). Its canonical product, "XGuard Universal Paid AI Agent + Secretless Gateway" (v5.1.0), sells four public-source outcomes to any agent with no account or API key: a free HTML extraction preview, multi-page evidence extraction, Schema.org product-offer comparison and a deduplicated RSS/Atom feed digest, each priced per execution in USDC on Base (0.002-0.006 USDC) and settled through the x402 v2 protocol before the sources are touched, with a signed quote, a replay-safe payment identifier, a signed receipt and ES256 "ProofRail" execution evidence. A second surface, Secretless Egress, lets an operator store an upstream API credential (OpenAI, Anthropic, GitHub, Stripe, Slack, Notion, Cloudflare, Gemini or custom) and hand an agent a short-lived scoped capability
  instead of the secret, with a mandatory Idempotency-Key on every write. The same catalog is exposed as a 49-operation OpenAPI 3.1.0 contract, a remote Streamable HTTP MCP server at api.xguardgate.com/mcp that answers tools/list anonymously, an A2A 1.0.0 agent card at /.well-known/agent-card.json, an OpenAI plugin manifest, llms.txt and a set of x402 payment, egress and action manifests; a companion x402 settlement-reconciliation API runs at reconcile.xguardgate.com.'
image: https://xguardgate.com/logo.svg
layout: provider
mcp_servers:
- description: ''
  name: XGuard MCP Server
  slug: xguard-mcp-server
- description: ''
  name: XGuard MCP endpoint (Streamable HTTP)
  slug: xguard-mcp-endpoint-streamable-http
modified: '2026-09-19'
name: XGuard
nav: Providers
network: true
overview: 'XGuard publishes 2 APIs on the [APIs.io](https://apis.io/) network: Universal Paid AI Agent + Secretless Gateway API and Reconcile API. Tagged areas include Agents, Agentic Commerce, x402, MCP, and A2A.


  XGuard''s developer surface includes documentation, getting-started guide, API reference, pricing, GitHub presence, support, authentication, and 29 more developer resources.'
plans:
- name: Xguardgate Com Plans Pricing
  plan_count: 11
  slug: xguardgate-com-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Xguardgate Com Rate Limits
  slug: xguardgate-com-rate-limits
score:
  band: developing
  composite: 49.7
  coverage:
    artifact_dirs: 21
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 44.7
  facets:
    access_clarity: 63.2
    contract_governance: 18.2
    contract_quality: 35.9
    developer_ergonomics: 57.7
    discoverability: 81.5
    operational_transparency: 31.6
  previous_composite: 5.0
  provenance:
    agentic_access: derived
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-20'
  trend: rising
  upsert:
    applies: true
    score: 27.8
security:
- kind: authentication
  name: Xguardgate Com Authentication
  slug: xguardgate-com-authentication
  summary_line: 8 schemes
- kind: domain-security
  name: Xguardgate Com Domain Security
  slug: xguardgate-com-domain-security
  summary_line: TLSv1.2 · HSTS
- kind: vulnerability-disclosure
  name: Xguardgate Com Vulnerability Disclosure
  slug: xguardgate-com-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: xguardgate-com
tags:
- Agents
- Agentic Commerce
- x402
- MCP
- A2A
- Micropayments
- Web Extraction
- Feed Aggregation
- Credential Broker
- API Gateway
- Agent Security
- agent-native
website: https://xguardgate.com/
---
