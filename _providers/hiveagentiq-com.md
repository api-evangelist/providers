---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: near-conformant
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 37.7
  scored_at: '2026-09-23'
agentic_access:
- acting_count: 20
  human_in_the_loop: 1
  name: Hiveagentiq Com Agentic Access
  operation_count: 24
  slug: hiveagentiq-com-agentic-access
  summary_line: 24 operations · 20 acting · 1 human-in-the-loop
api_count: 4
apis:
- baseURL: https://hivetrust.hiveagentiq.com
  baseurl_source: declared
  description: 'Identity and trust substrate for AI agents on hivetrust.hiveagentiq.com: DID issuance ($1.00 USDC), W3C VC and scoped HiveCredential issue/verify/scope ($0.01-$0.50), trust-score lookup ($0.10; a free'
  name: HiveTrust KYA Identity & Trust API
  slug: hivetrust-kya-identity-trust-api
- baseURL: https://hivegate.hiveagentiq.com
  baseurl_source: declared
  description: 'Onboarding gateway for the Hive network on hivegate.hiveagentiq.com: POST /v1/gate/onboard mints the first did:hive DID and API key free, guest registration ($4.99) bridges agents from LangChain, Crew'
  name: HiveGate Admission, Identity & Pricing Tier API
  slug: hivegate-admission-identity-api
- baseURL: https://hivebank.hiveagentiq.com
  baseurl_source: declared
  description: 'Agent treasury layer on hivebank.hiveagentiq.com: the served OpenAPI 3.0.3 covers custody and treasury-policy attestation ($0.25) and instant, scheduled and credit-line draws ($1.00), while the root d'
  name: HiveBank Treasury Attestation & Settlement API
  slug: hivebank-treasury-api
- baseURL: https://hivelaw.hiveagentiq.com
  baseurl_source: declared
  description: 'Legal and compliance layer on hivelaw.hiveagentiq.com: contract drafting, AI review and on-chain sealing ($0.50 each) and three compliance-tier programmes ($500, $1,500, $2,500) in the served 6-operat'
  name: HiveLaw AI Legal Contracts & Compliance API
  slug: hivelaw-legal-compliance-api
artifact_total: 14
asyncapis:
- description: ''
  name: Hiveagentiq Com Webhooks
  slug: hiveagentiq-com-webhooks
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/hiveagentiq-com/refs/heads/main/agentic-access/hiveagentiq-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/hiveagentiq-com-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://hiveagentiq.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/srotzin
- group: start
  title: ''
  type: GettingStarted
  url: https://thehiveryiq.com/onboard.html
- group: start
  title: ''
  type: SignUp
  url: https://thehiveryiq.com/onboard/
- group: commercial
  title: ''
  type: Pricing
  url: https://hivetrust.hiveagentiq.com/.well-known/hive-payments.json
- group: commercial
  title: ''
  type: TermsOfService
  url: https://thehiveryiq.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://thehiveryiq.com/privacy
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/hiveagentiq-com/refs/heads/main/a2a/hiveagentiq-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/hiveagentiq-com-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/hiveagentiq-com/refs/heads/main/mcp/hiveagentiq-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/hiveagentiq-com-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/hiveagentiq-com/refs/heads/main/mcp/hiveagentiq-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/hiveagentiq-com-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/hiveagentiq-com/refs/heads/main/well-known/hiveagentiq-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/hiveagentiq-com-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/hiveagentiq-com/refs/heads/main/llms/hiveagentiq-com-hivegate-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/hiveagentiq-com-hivegate-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/hiveagentiq-com/refs/heads/main/authentication/hiveagentiq-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/hiveagentiq-com-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hiveagentiq-com/refs/heads/main/conventions/hiveagentiq-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/hiveagentiq-com-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hiveagentiq-com/refs/heads/main/errors/hiveagentiq-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/hiveagentiq-com-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hiveagentiq-com/refs/heads/main/data-model/hiveagentiq-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/hiveagentiq-com-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/hiveagentiq-com/refs/heads/main/rate-limits/hiveagentiq-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/hiveagentiq-com-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/hiveagentiq-com/refs/heads/main/plans/hiveagentiq-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/hiveagentiq-com-plans-pricing.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/hiveagentiq-com/refs/heads/main/packages/hiveagentiq-com-packages.yml
  title: ''
  type: Packages
  url: packages/hiveagentiq-com-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/hiveagentiq-com/refs/heads/main/packages/hiveagentiq-com-packages.yml
  title: ''
  type: SDKs
  url: packages/hiveagentiq-com-packages.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hiveagentiq-com/refs/heads/main/conformance/hiveagentiq-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/hiveagentiq-com-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hiveagentiq-com/refs/heads/main/lifecycle/hiveagentiq-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/hiveagentiq-com-lifecycle.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/hiveagentiq-com/refs/heads/main/security/hiveagentiq-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hiveagentiq-com-domain-security.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hiveagentiq-com/refs/heads/main/asyncapi/hiveagentiq-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/hiveagentiq-com-webhooks.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/hiveagentiq-com/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/hiveagentiq-com/refs/heads/main/overlays/hiveagentiq-com-hivetrust-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/hiveagentiq-com-hivetrust-overlay.yaml
created: '2026-09-19'
description: 'Hive Agent IQ (hiveagentiq.com) is the agent-platform brand of Hive Civilization — a single-founder Wyoming company (Stephen Rotzin) whose sibling brand thehiveryiq.com is profiled separately — running a federation of agent-facing microservices on its own subdomains for autonomous AI agents: HiveTrust (KYA identity, W3C DIDs and verifiable credentials, 0-1000 behavioural trust scoring, USDC performance bonds, data-oracle context leases, insurance and disputes), HiveGate (free first-DID onboarding, adapters for LangChain, CrewAI, AutoGen, OpenAI, Anthropic and A2A agents, trust bridging), HiveBank (treasury attestation, USDC vaults and payment streams) and HiveLaw (contract drafting, dispute arbitration, EU AI Act hallucination audits and compliance seals). Each service publishes an OpenAPI 3.0.3 document, an A2A 0.3.0 agent card, an ai-plugin.json manifest and, on three of the four, a remote MCP server whose tools/list answers anonymously; every metered operation is priced
  in USDC and settled per call through x402 (or the MPP rail) on Base, with responses Ed25519-signed by the service DID. The apex website hiveagentiq.com, its legal pages and the HiveForge host returned Cloudflare Error 1000 ("DNS points to prohibited IP", HTTP 403) for every path throughout the 2026-09-19 profiling pass.'
layout: provider
mcp_servers:
- description: ''
  name: Hive Agent IQ MCP Server
  slug: hive-agent-iq-mcp-server
- description: ''
  name: HiveTrust MCP endpoint (Streamable HTTP, 17 tools)
  slug: hivetrust-mcp-endpoint-streamable-http-17-tools
- description: ''
  name: HiveGate MCP endpoint (Streamable HTTP, 4 tools)
  slug: hivegate-mcp-endpoint-streamable-http-4-tools
- description: ''
  name: HiveBank MCP endpoint (Streamable HTTP, 5 tools)
  slug: hivebank-mcp-endpoint-streamable-http-5-tools
modified: '2026-09-19'
name: Hive Agent IQ
nav: Providers
network: true
overview: 'Hive Agent IQ publishes 4 APIs on the [APIs.io](https://apis.io/) network, including HiveTrust KYA Identity & Trust API, HiveGate Admission, Identity & Pricing Tier API, HiveBank Treasury Attestation & Settlement API, and 1 more. Tagged areas include Agents, Agentic Commerce, A2A, MCP, and x402.


  The Hive Agent IQ catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Hive Agent IQ''s developer surface includes getting-started guide, signup flow, pricing, authentication, and 23 more developer resources.'
plans:
- name: Hiveagentiq Com Plans Pricing
  plan_count: 16
  slug: hiveagentiq-com-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 4
  name: Hiveagentiq Com Rate Limits
  slug: hiveagentiq-com-rate-limits
score:
  band: developing
  composite: 54.2
  coverage:
    artifact_dirs: 20
    catalog_earned: 62.0
    catalog_earned_first_party: 24.0
    catalog_gap: 53.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 49.7
    developer_ergonomics: 49.4
    discoverability: 77.8
    operational_transparency: 44.7
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 54.2
  provenance:
    agentic_access: derived
    conformance: first-party
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 37.9
  schema_version: 0.22.0
  scored_at: '2026-09-23'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Hiveagentiq Com Authentication
  slug: hiveagentiq-com-authentication
  summary_line: apiKey/http-bearer/payment/signature · 6 schemes
- kind: domain-security
  name: Hiveagentiq Com Domain Security
  slug: hiveagentiq-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: hiveagentiq-com
tags:
- Agents
- Agentic Commerce
- A2A
- MCP
- x402
- Decentralized Identity
- Verifiable Credentials
- Trust Scoring
- Stablecoins
- Insurance
- Compliance
- Agent-Native
- United States
website: https://hiveagentiq.com/
---
