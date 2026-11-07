---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
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
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: na
    protected_resource_metadata: documented
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 46.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 16
  human_in_the_loop: 2
  name: Xguardgate Com Agentic Access
  operation_count: 50
  slug: xguardgate-com-agentic-access
  summary_line: 50 operations · 16 acting · 2 human-in-the-loop
api_count: 2
apis:
- description: Remote Model Context Protocol server at https://api.xguardgate.com/mcp (Streamable HTTP, protocol version 2026-07-28, serverInfo xguard-universal-paid-secretless-gateway 5.1.0). initialize and tools/l
  name: XGuard MCP Server
  slug: xguard-mcp-server
- description: 'Agent2Agent surface: an agent card served identically from https://api.xguardgate.com/.well-known/agent-card.json (the canonical location named in the provider''s own xguard.json manifest) and from xgu'
  name: XGuard A2A Agent
  slug: xguard-a2a-agent
- baseURL: https://api.xguardgate.com
  baseurl_source: declared
  description: The Actions API from XGuard — 5 operation(s) for actions.
  name: XGuard Actions API
  slug: xguardgate-com-actions-api
- baseURL: https://api.xguardgate.com
  baseurl_source: declared
  description: The Agent Card.json API from XGuard — 1 operation(s) for agent card.json.
  name: XGuard Agent Card.json API
  slug: xguardgate-com-agent-card-json-api
- baseURL: https://api.xguardgate.com
  baseurl_source: declared
  description: The Discovery API from XGuard — 2 operation(s) for discovery.
  name: XGuard Discovery API
  slug: xguardgate-com-discovery-api
- baseURL: https://api.xguardgate.com
  baseurl_source: declared
  description: The Edge API from XGuard — 1 operation(s) for edge.
  name: XGuard Edge API
  slug: xguardgate-com-edge-api
- baseURL: https://api.xguardgate.com
  baseurl_source: declared
  description: The Egress API from XGuard — 6 operation(s) for egress.
  name: XGuard Egress API
  slug: xguardgate-com-egress-api
- baseURL: https://api.xguardgate.com
  baseurl_source: declared
  description: The Facilitator API from XGuard — 2 operation(s) for facilitator.
  name: XGuard Facilitator API
  slug: xguardgate-com-facilitator-api
- baseURL: https://api.xguardgate.com
  baseurl_source: declared
  description: The Health API from XGuard — 1 operation(s) for health.
  name: XGuard Health API
  slug: xguardgate-com-health-api
- baseURL: https://api.xguardgate.com
  baseurl_source: declared
  description: The Healthz API from XGuard — 1 operation(s) for healthz.
  name: XGuard Healthz API
  slug: xguardgate-com-healthz-api
- baseURL: https://api.xguardgate.com
  baseurl_source: declared
  description: The Inspect API from XGuard — 1 operation(s) for inspect.
  name: XGuard Inspect API
  slug: xguardgate-com-inspect-api
- baseURL: https://api.xguardgate.com
  baseurl_source: declared
  description: The Metrics API from XGuard — 1 operation(s) for metrics.
  name: XGuard Metrics API
  slug: xguardgate-com-metrics-api
- baseURL: https://api.xguardgate.com
  baseurl_source: declared
  description: The Openapi.yaml API from XGuard — 1 operation(s) for openapi.yaml.
  name: XGuard Openapi.yaml API
  slug: xguardgate-com-openapi-yaml-api
- baseURL: https://api.xguardgate.com
  baseurl_source: declared
  description: The Operations API from XGuard — 1 operation(s) for operations.
  name: XGuard Operations API
  slug: xguardgate-com-operations-api
- baseURL: https://api.xguardgate.com
  baseurl_source: declared
  description: Primary intent execution
  name: XGuard Outcomes API
  slug: xguardgate-com-outcomes-api
- baseURL: https://api.xguardgate.com
  baseurl_source: declared
  description: The Payment API from XGuard — 1 operation(s) for payment.
  name: XGuard Payment API
  slug: xguardgate-com-payment-api
- baseURL: https://api.xguardgate.com
  baseurl_source: declared
  description: The Preflight API from XGuard — 1 operation(s) for preflight.
  name: XGuard Preflight API
  slug: xguardgate-com-preflight-api
- baseURL: https://api.xguardgate.com
  baseurl_source: declared
  description: The Pricing API from XGuard — 2 operation(s) for pricing.
  name: XGuard Pricing API
  slug: xguardgate-com-pricing-api
- baseURL: https://api.xguardgate.com
  baseurl_source: declared
  description: The Proof API from XGuard — 1 operation(s) for proof.
  name: XGuard Proof API
  slug: xguardgate-com-proof-api
- baseURL: https://api.xguardgate.com
  baseurl_source: declared
  description: The Proofs API from XGuard — 1 operation(s) for proofs.
  name: XGuard Proofs API
  slug: xguardgate-com-proofs-api
- baseURL: https://api.xguardgate.com
  baseurl_source: declared
  description: The Protocols API from XGuard — 1 operation(s) for protocols.
  name: XGuard Protocols API
  slug: xguardgate-com-protocols-api
- baseURL: https://api.xguardgate.com
  baseurl_source: declared
  description: The Ready API from XGuard — 1 operation(s) for ready.
  name: XGuard Ready API
  slug: xguardgate-com-ready-api
- baseURL: https://api.xguardgate.com
  baseurl_source: declared
  description: The Receipts API from XGuard — 1 operation(s) for receipts.
  name: XGuard Receipts API
  slug: xguardgate-com-receipts-api
- baseURL: https://api.xguardgate.com
  baseurl_source: declared
  description: The Reconcile API from XGuard — 1 operation(s) for reconcile.
  name: XGuard Reconcile API
  slug: xguardgate-com-reconcile-api
- baseURL: https://api.xguardgate.com
  baseurl_source: declared
  description: The Settle API from XGuard — 1 operation(s) for settle.
  name: XGuard Settle API
  slug: xguardgate-com-settle-api
- baseURL: https://api.xguardgate.com
  baseurl_source: declared
  description: The Supported API from XGuard — 1 operation(s) for supported.
  name: XGuard Supported API
  slug: xguardgate-com-supported-api
- baseURL: https://api.xguardgate.com
  baseurl_source: declared
  description: The Test API from XGuard — 2 operation(s) for test.
  name: XGuard Test API
  slug: xguardgate-com-test-api
- baseURL: https://api.xguardgate.com
  baseurl_source: declared
  description: The Tools API from XGuard — 2 operation(s) for tools.
  name: XGuard Tools API
  slug: xguardgate-com-tools-api
- baseURL: https://api.xguardgate.com
  baseurl_source: declared
  description: The Verify API from XGuard — 1 operation(s) for verify.
  name: XGuard Verify API
  slug: xguardgate-com-verify-api
- baseURL: https://api.xguardgate.com
  baseurl_source: declared
  description: The .well Known API from XGuard — 3 operation(s) for .well known.
  name: XGuard .well Known API
  slug: xguardgate-com-well-known-api
artifact_total: 42
common:
- group: other
  href: https://artifacts.apis.io/xguardgate-com/capabilities/xguardgate-com-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/xguardgate-com-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/xguardgate-com/overlays/xguardgate-com-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/xguardgate-com-openapi-overlay.yaml
- group: other
  href: https://artifacts.apis.io/xguardgate-com/overlays/xguardgate-com-reconcile-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/xguardgate-com-reconcile-openapi-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/xguardgate-com/security/xguardgate-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/xguardgate-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/xguardgate-com/security/xguardgate-com-domain-security.yml
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
  href: https://artifacts.apis.io/xguardgate-com/llms/xguardgate-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/xguardgate-com-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://xguardgate.com/llms.txt
- group: agent
  href: https://artifacts.apis.io/xguardgate-com/well-known/xguardgate-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/xguardgate-com-well-known.yml
- group: auth
  href: https://artifacts.apis.io/xguardgate-com/well-known/xguardgate-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/xguardgate-com-security.txt
- group: other
  href: https://artifacts.apis.io/xguardgate-com/a2a/xguardgate-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/xguardgate-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/xguardgate-com/mcp/xguardgate-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/xguardgate-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/xguardgate-com/authentication/xguardgate-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/xguardgate-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/xguardgate-com/conventions/xguardgate-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/xguardgate-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/xguardgate-com/conventions/xguardgate-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/xguardgate-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/xguardgate-com/errors/xguardgate-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/xguardgate-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/xguardgate-com/lifecycle/xguardgate-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/xguardgate-com-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/xguardgate-com/conformance/xguardgate-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/xguardgate-com-conformance.yml
- group: commercial
  href: https://artifacts.apis.io/xguardgate-com/plans/xguardgate-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/xguardgate-com-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/xguardgate-com/rate-limits/xguardgate-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/xguardgate-com-rate-limits.yml
- group: operate
  href: https://artifacts.apis.io/xguardgate-com/changelog/xguardgate-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/xguardgate-com-changelog.yml
- group: build
  href: https://artifacts.apis.io/xguardgate-com/packages/xguardgate-com-packages.yml
  title: ''
  type: Packages
  url: packages/xguardgate-com-packages.yml
- group: build
  href: https://artifacts.apis.io/xguardgate-com/packages/xguardgate-com-packages.yml
  title: ''
  type: SDKs
  url: packages/xguardgate-com-packages.yml
- group: start
  href: https://artifacts.apis.io/xguardgate-com/sandbox/xguardgate-com-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/xguardgate-com-sandbox.yml
- group: design
  href: https://artifacts.apis.io/xguardgate-com/data-model/xguardgate-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/xguardgate-com-data-model.yml
- group: agent
  href: https://artifacts.apis.io/xguardgate-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/xguardgate-com/security/xguardgate-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/xguardgate-com-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/xguardgate-com/agentic-access/xguardgate-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/xguardgate-com-agentic-access.yml
created: '2026-09-19'
description: 'XGuard is a paid-tool and credential-brokering gateway for AI agents, operated from xguardgate.com with its API at api.xguardgate.com and its source published at github.com/moelayyan90/XGuard (Apache-2.0, Cloudflare Workers). Its canonical product, "XGuard Universal Paid AI Agent + Secretless Gateway" (v5.1.0), sells four public-source outcomes to any agent with no account or API key: a free HTML extraction preview, multi-page evidence extraction, Schema.org product-offer comparison and a deduplicated RSS/Atom feed digest, each priced per execution in USDC on Base (0.002-0.006 USDC) and settled through the x402 v2 protocol before the sources are touched, with a signed quote, a replay-safe payment identifier, a signed receipt and ES256 "ProofRail" execution evidence. A second surface, Secretless Egress, lets an operator store an upstream API credential (OpenAI, Anthropic, GitHub, Stripe, Slack, Notion, Cloudflare, Gemini or custom) and hand an agent a short-lived scoped capability
  instead of the secret, with a mandatory Idempotency-Key on every write. The same catalog is exposed as a 49-operation OpenAPI 3.1.0 contract, a remote Streamable HTTP MCP server at api.xguardgate.com/mcp that answers tools/list anonymously, an A2A 1.0.0 agent card at /.well-known/agent-card.json, an OpenAI plugin manifest, llms.txt and a set of x402 payment, egress and action manifests; a companion x402 settlement-reconciliation API runs at reconcile.xguardgate.com.'
finops:
- has_sources: true
  method: derived
  name: Xguardgate Com Finops
  primary_unit: ''
  service_category: ''
  slug: xguardgate-com-finops
  template: true
image: https://xguardgate.com/logo.svg
layout: provider
mcp_servers:
- description: XGuard operates ONE remote MCP server at https://api.xguardgate.com/mcp, on the same host as its OpenAPI, its A2A JSON-RPC endpoint and its x402 facilitator relay. It is Streamable HTTP, speaks MCP pr
  name: XGuard MCP Server
  slug: xguard-universal-paid-secretless-gateway
modified: '2026-09-19'
name: XGuard
nav: Providers
network: true
overview: 'XGuard publishes 30 API contracts indexed on the [APIs.io](https://apis.io/) network, including Actions API, Agent Card.json API, Discovery API, and 27 more. Tagged areas include Agents, Agentic Commerce, x402, MCP, and A2A.


  The XGuard catalog on APIs.io includes 1 Spectral governance ruleset.


  XGuard''s developer surface includes documentation, getting-started guide, API reference, pricing, GitHub presence, support, authentication, and 32 more developer resources.'
plans:
- name: Xguardgate Com Plans Pricing
  plan_count: 11
  slug: xguardgate-com-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Xguardgate Com Rate Limits
  slug: xguardgate-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 85
  extends:
  - spectral:oas
  name: XGuard API Rules
  rule_count: 44
  severity_counts:
    error: 36
    hint: 0
    info: 1
    warn: 7
  slug: xguardgate-com-rules
score:
  band: developing
  composite: 54.0
  coverage:
    artifact_dirs: 30
    catalog_earned: 53.5
    catalog_earned_first_party: 12.0
    catalog_gap: 61.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 63.2
    contract_governance: 31.8
    contract_quality: 40.3
    developer_ergonomics: 57.7
    discoverability: 75.0
    operational_transparency: 31.6
  previous_composite: 54.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 3.6
      total: 28
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 27.8
screenshot: https://apis.io/screenshots/xguardgate-com/xguardgate-com-2026-10-11T194623.png
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
skill_count: 3
skills:
- name: xguardgate-com-free-extraction-preview
  slug: xguardgate-com-free-extraction-preview
- name: xguardgate-com-paid-outcome-x402
  slug: xguardgate-com-paid-outcome-x402
- name: xguardgate-com-secretless-egress
  slug: xguardgate-com-secretless-egress
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
- Agent-Native
website: https://xguardgate.com/
---
