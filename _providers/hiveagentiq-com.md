---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
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
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 36.9
  scored_at: '2026-11-06'
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
  description: The Bank API from Hive Agent IQ — 5 operation(s) for bank.
  name: Hive Agent IQ Bank API
  slug: hiveagentiq-com-bank-api
- baseURL: https://hivetrust.hiveagentiq.com
  baseurl_source: declared
  description: The Comply API from Hive Agent IQ — 3 operation(s) for comply.
  name: Hive Agent IQ Comply API
  slug: hiveagentiq-com-comply-api
- baseURL: https://hivetrust.hiveagentiq.com
  baseurl_source: declared
  description: The Credential API from Hive Agent IQ — 3 operation(s) for credential.
  name: Hive Agent IQ Credential API
  slug: hiveagentiq-com-credential-api
- baseURL: https://hivetrust.hiveagentiq.com
  baseurl_source: declared
  description: The Gate API from Hive Agent IQ — 5 operation(s) for gate.
  name: Hive Agent IQ Gate API
  slug: hiveagentiq-com-gate-api
- baseURL: https://hivetrust.hiveagentiq.com
  baseurl_source: declared
  description: The Identity API from Hive Agent IQ — 1 operation(s) for identity.
  name: Hive Agent IQ Identity API
  slug: hiveagentiq-com-identity-api
- baseURL: https://hivetrust.hiveagentiq.com
  baseurl_source: declared
  description: The Law API from Hive Agent IQ — 3 operation(s) for law.
  name: Hive Agent IQ Law API
  slug: hiveagentiq-com-law-api
- baseURL: https://hivetrust.hiveagentiq.com
  baseurl_source: declared
  description: The Trust API from Hive Agent IQ — 4 operation(s) for trust.
  name: Hive Agent IQ Trust API
  slug: hiveagentiq-com-trust-api
artifact_total: 22
asyncapis:
- description: ''
  name: Hiveagentiq Com Webhooks
  slug: hiveagentiq-com-webhooks
common:
- group: other
  href: https://artifacts.apis.io/hiveagentiq-com/capabilities/hiveagentiq-com-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/hiveagentiq-com-capability-edges.yml
- group: agent
  title: ''
  type: MCPServer
  url: https://hivetrust.hiveagentiq.com/mcp
- group: agent
  title: ''
  type: MCPServer
  url: https://hivegate.hiveagentiq.com/mcp
- group: other
  href: https://artifacts.apis.io/hiveagentiq-com/overlays/hiveagentiq-com-hivegate-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/hiveagentiq-com-hivegate-overlay.yaml
- group: agent
  title: ''
  type: MCPServer
  url: https://hivebank.hiveagentiq.com/mcp
- group: other
  href: https://artifacts.apis.io/hiveagentiq-com/overlays/hiveagentiq-com-hivebank-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/hiveagentiq-com-hivebank-overlay.yaml
- group: other
  href: https://artifacts.apis.io/hiveagentiq-com/overlays/hiveagentiq-com-hivelaw-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/hiveagentiq-com-hivelaw-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/hiveagentiq-com/agentic-access/hiveagentiq-com-agentic-access.yml
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
  href: https://artifacts.apis.io/hiveagentiq-com/a2a/hiveagentiq-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/hiveagentiq-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/hiveagentiq-com/mcp/hiveagentiq-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/hiveagentiq-com-mcp.yml
- group: build
  href: https://artifacts.apis.io/hiveagentiq-com/mcp/hiveagentiq-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/hiveagentiq-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/hiveagentiq-com/well-known/hiveagentiq-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/hiveagentiq-com-well-known.yml
- group: agent
  href: https://artifacts.apis.io/hiveagentiq-com/llms/hiveagentiq-com-hivegate-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/hiveagentiq-com-hivegate-llms.txt
- group: auth
  href: https://artifacts.apis.io/hiveagentiq-com/authentication/hiveagentiq-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/hiveagentiq-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/hiveagentiq-com/conventions/hiveagentiq-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/hiveagentiq-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/hiveagentiq-com/errors/hiveagentiq-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/hiveagentiq-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/hiveagentiq-com/data-model/hiveagentiq-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/hiveagentiq-com-data-model.yml
- group: operate
  href: https://artifacts.apis.io/hiveagentiq-com/rate-limits/hiveagentiq-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/hiveagentiq-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/hiveagentiq-com/plans/hiveagentiq-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/hiveagentiq-com-plans-pricing.yml
- group: build
  href: https://artifacts.apis.io/hiveagentiq-com/packages/hiveagentiq-com-packages.yml
  title: ''
  type: Packages
  url: packages/hiveagentiq-com-packages.yml
- group: build
  href: https://artifacts.apis.io/hiveagentiq-com/packages/hiveagentiq-com-packages.yml
  title: ''
  type: SDKs
  url: packages/hiveagentiq-com-packages.yml
- group: design
  href: https://artifacts.apis.io/hiveagentiq-com/conformance/hiveagentiq-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/hiveagentiq-com-conformance.yml
- group: design
  href: https://artifacts.apis.io/hiveagentiq-com/lifecycle/hiveagentiq-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/hiveagentiq-com-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/hiveagentiq-com/security/hiveagentiq-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hiveagentiq-com-domain-security.yml
- group: design
  href: https://artifacts.apis.io/hiveagentiq-com/asyncapi/hiveagentiq-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/hiveagentiq-com-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/hiveagentiq-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://artifacts.apis.io/hiveagentiq-com/overlays/hiveagentiq-com-hivetrust-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/hiveagentiq-com-hivetrust-overlay.yaml
created: '2026-09-19'
description: 'Hive Agent IQ (hiveagentiq.com) is the agent-platform brand of Hive Civilization — a single-founder Wyoming company (Stephen Rotzin) whose sibling brand thehiveryiq.com is profiled separately — running a federation of agent-facing microservices on its own subdomains for autonomous AI agents: HiveTrust (KYA identity, W3C DIDs and verifiable credentials, 0-1000 behavioural trust scoring, USDC performance bonds, data-oracle context leases, insurance and disputes), HiveGate (free first-DID onboarding, adapters for LangChain, CrewAI, AutoGen, OpenAI, Anthropic and A2A agents, trust bridging), HiveBank (treasury attestation, USDC vaults and payment streams) and HiveLaw (contract drafting, dispute arbitration, EU AI Act hallucination audits and compliance seals). Each service publishes an OpenAPI 3.0.3 document, an A2A 0.3.0 agent card, an ai-plugin.json manifest and, on three of the four, a remote MCP server whose tools/list answers anonymously; every metered operation is priced
  in USDC and settled per call through x402 (or the MPP rail) on Base, with responses Ed25519-signed by the service DID. The apex website hiveagentiq.com, its legal pages and the HiveForge host returned Cloudflare Error 1000 ("DNS points to prohibited IP", HTTP 403) for every path throughout the 2026-09-19 profiling pass.'
finops:
- has_sources: true
  method: derived
  name: Hiveagentiq Com Finops
  primary_unit: subscription
  service_category: ''
  slug: hiveagentiq-com-finops
  template: false
layout: provider
mcp_servers:
- description: ''
  name: Hive Agent IQ MCP Server
  slug: mcp
- description: ''
  name: Hive Agent IQ MCP Server
  slug: mcp-2
- description: ''
  name: Hive Agent IQ MCP Server
  slug: mcp-3
modified: '2026-09-19'
name: Hive Agent IQ
nav: Providers
network: true
overview: 'Hive Agent IQ publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Bank API, Comply API, Credential API, and 4 more. Tagged areas include Agents, Agentic Commerce, A2A, MCP, and x402.


  The Hive Agent IQ catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Hive Agent IQ''s developer surface includes getting-started guide, signup flow, pricing, authentication, and 30 more developer resources.'
plans:
- name: Hiveagentiq Com Plans Pricing
  plan_count: 16
  slug: hiveagentiq-com-plans-pricing
- name: Hiveagentiq Com Price Estimates
  plan_count: 0
  slug: hiveagentiq-com-price-estimates
random_paper: 1
rate_limits:
- limit_count: 4
  name: Hiveagentiq Com Rate Limits
  slug: hiveagentiq-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 84
  extends:
  - spectral:oas
  name: Hive Agent IQ API Rules
  rule_count: 43
  severity_counts:
    error: 40
    hint: 0
    info: 1
    warn: 2
  slug: hiveagentiq-com-rules
score:
  band: developing
  composite: 54.2
  coverage:
    artifact_dirs: 28
    catalog_earned: 69.5
    catalog_earned_first_party: 24.0
    catalog_gap: 45.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.3
  facets:
    access_clarity: 77.6
    contract_governance: 31.8
    contract_quality: 56.9
    developer_ergonomics: 35.1
    discoverability: 76.7
    operational_transparency: 44.7
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 57.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 71.4
      total: 7
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 21.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/hiveagentiq-com/hiveagentiq-com-2026-10-11T105335.png
security:
- kind: authentication
  name: Hiveagentiq Com Authentication
  slug: hiveagentiq-com-authentication
  summary_line: apiKey/http-bearer/payment/signature · 6 schemes
- kind: domain-security
  name: Hiveagentiq Com Domain Security
  slug: hiveagentiq-com-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 3
skills:
- name: hiveagentiq-com-check-agent-trust
  slug: hiveagentiq-com-check-agent-trust
- name: hiveagentiq-com-issue-verify-credential
  slug: hiveagentiq-com-issue-verify-credential
- name: hiveagentiq-com-onboard-agent
  slug: hiveagentiq-com-onboard-agent
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
