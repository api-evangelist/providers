---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 44.3
  scored_at: '2026-09-20'
api_count: 2
apis:
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: 'Pay-per-call REST API on receipts.thehiveryiq.com for signing and verifying receipts (free tier: 100 dual-signed receipts per IP per day with no key; paid profiles nano/standard/pq at $0.0001/$0.0008/'
  name: Hive Receipts and Agent Commerce API (HiveMorph)
  slug: hivemorph-receipts-api
- baseURL: https://api.thehiveryiq.com
  baseurl_source: declared
  description: 'OpenAI-compatible inference router on api.thehiveryiq.com: chat completions, text completions and embeddings across 447 models drawn live from the OpenRouter registry, with automatic context compressi'
  name: HiveCompute Inference Router API
  slug: hivecompute-inference-api
- description: 'Provider-operated remote MCP gateway on Render (named as the MCP transport by receipts.thehiveryiq.com/.well-known/mcp.json): initialize and tools/list answer anonymously with 38 tools from eight moun'
  name: Hive MCP Gateway and Registry
  slug: hive-mcp-gateway
- description: 'The trust rail on passport.thehiveryiq.com: HKTN (Hive Known Traveler Number) registry for persistent agent identity and tier, tenant onboarding and dashboards, provenance public-key distribution and '
  name: Hive Passport Trust Rail (HKTN)
  slug: hive-passport-trust-rail
- description: 'Agent-to-agent surface: A2A agent cards on the apex (protocolVersion 0.3.0, six HiveAttest/HiveWallet/HiveGate skills) and on receipts.thehiveryiq.com (0.2.0 catalog of ten per-agent cards with the AP'
  name: Hive Civilization A2A Agent
  slug: hive-a2a-agent
artifact_total: 15
asyncapis:
- description: ''
  name: Thehiveryiq Com Webhooks
  slug: thehiveryiq-com-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://thehiveryiq.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://thehiveryiq.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://thehiveryiq.com/developers
- group: docs
  title: ''
  type: APIReference
  url: https://receipts.thehiveryiq.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://thehiveryiq.com/agents
- group: operate
  title: ''
  type: Support
  url: https://thehiveryiq.com/company
- group: other
  title: ''
  type: Leadership
  url: https://thehiveryiq.com/company
- group: company
  title: ''
  type: Blog
  url: https://thehiveryiq.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/srotzin
- group: operate
  title: ''
  type: Roadmap
  url: https://thehiveryiq.com/rails
- group: commercial
  title: ''
  type: Pricing
  url: https://thehiveryiq.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://thehiveryiq.com/onboard/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://thehiveryiq.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://thehiveryiq.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://thehiveryiq.com/status/
- group: docs
  title: ''
  type: Specifications
  url: https://thehiveryiq.com/specs/did-hive/v1/
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/thehiveryiq-com/refs/heads/main/a2a/thehiveryiq-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/thehiveryiq-com-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/thehiveryiq-com/refs/heads/main/mcp/thehiveryiq-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/thehiveryiq-com-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/thehiveryiq-com/refs/heads/main/mcp/thehiveryiq-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/thehiveryiq-com-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/thehiveryiq-com/refs/heads/main/llms/thehiveryiq-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/thehiveryiq-com-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://thehiveryiq.com/llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/thehiveryiq-com/refs/heads/main/well-known/thehiveryiq-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/thehiveryiq-com-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/thehiveryiq-com/refs/heads/main/well-known/thehiveryiq-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/thehiveryiq-com-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/thehiveryiq-com/refs/heads/main/security/thehiveryiq-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/thehiveryiq-com-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/thehiveryiq-com/refs/heads/main/security/thehiveryiq-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/thehiveryiq-com-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/thehiveryiq-com/refs/heads/main/security/thehiveryiq-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/thehiveryiq-com-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/thehiveryiq-com/refs/heads/main/security/thehiveryiq-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/thehiveryiq-com-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://thehiveryiq.com/compliance/
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/thehiveryiq-com/refs/heads/main/conformance/thehiveryiq-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/thehiveryiq-com-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/thehiveryiq-com/refs/heads/main/lifecycle/thehiveryiq-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/thehiveryiq-com-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/thehiveryiq-com/refs/heads/main/changelog/thehiveryiq-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/thehiveryiq-com-changelog.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/thehiveryiq-com/refs/heads/main/authentication/thehiveryiq-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/thehiveryiq-com-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/thehiveryiq-com/refs/heads/main/conventions/thehiveryiq-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/thehiveryiq-com-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/thehiveryiq-com/refs/heads/main/conventions/thehiveryiq-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/thehiveryiq-com-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/thehiveryiq-com/refs/heads/main/errors/thehiveryiq-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/thehiveryiq-com-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/thehiveryiq-com/refs/heads/main/data-model/thehiveryiq-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/thehiveryiq-com-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/thehiveryiq-com/refs/heads/main/rate-limits/thehiveryiq-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/thehiveryiq-com-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/thehiveryiq-com/refs/heads/main/plans/thehiveryiq-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/thehiveryiq-com-plans-pricing.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/thehiveryiq-com/refs/heads/main/packages/thehiveryiq-com-packages.yml
  title: ''
  type: Packages
  url: packages/thehiveryiq-com-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/thehiveryiq-com/refs/heads/main/packages/thehiveryiq-com-packages.yml
  title: ''
  type: SDKs
  url: packages/thehiveryiq-com-packages.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/thehiveryiq-com/refs/heads/main/sandbox/thehiveryiq-com-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/thehiveryiq-com-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/thehiveryiq-com/refs/heads/main/asyncapi/thehiveryiq-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/thehiveryiq-com-webhooks.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/thehiveryiq-com/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/thehiveryiq-com/refs/heads/main/overlays/thehiveryiq-com-hivemorph-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/thehiveryiq-com-hivemorph-overlay.yaml
- group: other
  title: ''
  type: Subprocessors
  url: https://thehiveryiq.com/security/
- group: other
  title: ''
  type: DataSubjectRequest
  url: https://thehiveryiq.com/privacy
- group: other
  title: ''
  type: DataResidency
  url: https://thehiveryiq.com/security/
created: '2026-09-19'
description: 'Hive Civilization (DBAs The Hivery and The Hivery IQ; Walnut Creek, California; single-founder Wyoming corporation established 2026) sells signed, independently verifiable receipts for automated and AI-agent actions: every call returns a dual-signed record (Ed25519 plus ML-DSA-65) over an artifact hash, priced per receipt and settled per call in USDC on Base through the x402 payment protocol, with no account required for the free tier. The public surface is spread over four hosts: receipts.thehiveryiq.com serves the HiveMorph receipts and agent-commerce API (a 906-path, 937-operation FastAPI OpenAPI 3.1 contract covering receipt emit/verify, x402 quotes and settlement references, delegations and a firewall, HKTN trust lookups, plus dozens of vertical attestation families), a JSON-RPC 2.0 agent endpoint and A2A agent cards; api.thehiveryiq.com serves HiveCompute, an OpenAI-compatible, x402-metered inference router with a live remote MCP server; passport.thehiveryiq.com is the
  HKTN trust rail; and hive-mcp-gateway.onrender.com fronts 37 hive-mcp-* MCP servers. The apex publishes an A2A agent card, security.txt, llms.txt, pricing, a self-attested (uncertified) SOC 2 / ISO 27001 posture and a did:hive DID method specification.'
image: https://thehiveryiq.com/assets/brand/hive-mark-512.png
layout: provider
mcp_servers:
- description: ''
  name: Hive Civilization MCP Server
  slug: hive-civilization-mcp-server
- description: ''
  name: Hive Civilization MCP Server
  slug: hive-civilization-mcp-server-2
- description: ''
  name: Hive Civilization MCP Server
  slug: hive-civilization-mcp-server-3
modified: '2026-09-19'
name: Hive Civilization
nav: Providers
network: true
overview: 'Hive Civilization publishes 2 APIs on the [APIs.io](https://apis.io/) network: Hive Receipts and Agent Commerce API (HiveMorph) and HiveCompute Inference Router API. Tagged areas include Agents, Agentic Commerce, A2A, MCP, and x402.


  The Hive Civilization catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Hive Civilization''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 40 more developer resources.'
plans:
- name: Thehiveryiq Com Plans Pricing
  plan_count: 8
  slug: thehiveryiq-com-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 4
  name: Thehiveryiq Com Rate Limits
  slug: thehiveryiq-com-rate-limits
score:
  band: exemplar
  composite: 71.7
  coverage:
    artifact_dirs: 21
    catalog_earned: 61.0
    catalog_earned_first_party: 24.0
    catalog_gap: 54.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 65.2
  facets:
    access_clarity: 92.1
    contract_governance: 18.2
    contract_quality: 54.7
    developer_ergonomics: 73.2
    discoverability: 75.9
    operational_transparency: 92.1
  previous_composite: 6.5
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
  scored_at: '2026-09-20'
  trend: rising
  upsert:
    applies: true
    score: 38.9
security:
- kind: authentication
  name: Thehiveryiq Com Authentication
  slug: thehiveryiq-com-authentication
  summary_line: none/x402-payment/apiKey/ed25519-signed-request · 6 schemes
- kind: domain-security
  name: Thehiveryiq Com Domain Security
  slug: thehiveryiq-com-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Thehiveryiq Com Vulnerability Disclosure
  slug: thehiveryiq-com-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Thehiveryiq Com Trust Center
  slug: thehiveryiq-com-trust-center
  summary_line: trust center published
slug: thehiveryiq-com
tags:
- Agents
- Agentic Commerce
- A2A
- MCP
- x402
- Receipts
- Digital Signature
- Post-Quantum Cryptography
- Attestation
- Decentralized Identity
- Stablecoins
- Inference
- LLM Routing
- Compliance
- agent-native
- United States
website: https://thehiveryiq.com/
---
