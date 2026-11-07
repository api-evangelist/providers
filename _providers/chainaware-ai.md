---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
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
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: documented
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 38.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Chainaware Ai Agentic Access
  operation_count: 5
  slug: chainaware-ai-agentic-access
  summary_line: 5 operations · 3 acting
api_count: 1
apis:
- description: Hosted Model Context Protocol server over Server-Sent Events at https://prediction.mcp.chainaware.ai/sse (https://mcp.chainaware.ai/sse serves the same server; messages are POSTed to /messages/?sessio
  name: ChainAware Behavioural Prediction MCP Server
  slug: chainaware-prediction-mcp-server
- description: 'Agent-facing surface on api.chainaware.ai: an A2A 0.3.0 agent card at /.well-known/agent-card.json (also at the legacy /.well-known/agent.json) declaring five skills — fraud_check, fraud_audit, wallet'
  name: ChainAware A2A Agent and x402 API
  slug: chainaware-a2a-x402-agent-api
- baseURL: https://enterprise.api.chainaware.ai
  baseurl_source: declared
  description: The Behaviour Prediction API API from ChainAware.ai — 2 operation(s) for behaviour prediction api.
  name: ChainAware.ai Behaviour Prediction API
  slug: chainaware-ai-behaviour-prediction-api-api
- baseURL: https://enterprise.api.chainaware.ai
  baseurl_source: declared
  description: The Credit Score API API from ChainAware.ai — 1 operation(s) for credit score api.
  name: ChainAware.ai Credit Score API
  slug: chainaware-ai-credit-score-api-api
- baseURL: https://enterprise.api.chainaware.ai
  baseurl_source: declared
  description: The Fraud API API from ChainAware.ai — 2 operation(s) for fraud api.
  name: ChainAware.ai Fraud API
  slug: chainaware-ai-fraud-api-api
artifact_total: 18
common:
- group: company
  title: ''
  type: Blog
  url: https://chainaware.ai/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://chainaware.ai/blog/topics/news/feed/
- group: other
  href: https://artifacts.apis.io/chainaware-ai/overlays/chainaware-ai-enterprise-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/chainaware-ai-enterprise-api-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/chainaware-ai/security/chainaware-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/chainaware-ai-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/chainaware-ai/agentic-access/chainaware-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/chainaware-ai-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/chainaware-ai/authentication/chainaware-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/chainaware-ai-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://chainaware.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://chainaware.ai/learn/
- group: docs
  title: ''
  type: Documentation
  url: https://chainaware.ai/learn/
- group: docs
  title: ''
  type: APIReference
  url: https://swagger.chainaware.ai/
- group: start
  title: ''
  type: GettingStarted
  url: https://chainaware.ai/learn/prediction-mcp/setup.html
- group: operate
  title: ''
  type: Support
  url: https://chainaware.ai/support
- group: company
  title: ''
  type: Blog
  url: https://chainaware.ai/blog/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/ChainAware
- group: commercial
  title: ''
  type: Pricing
  url: https://chainaware.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://chainaware.ai/profile
- group: commercial
  title: ''
  type: TermsOfService
  url: https://chainaware.ai/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://chainaware.ai/privacy/
- group: company
  title: ''
  type: Twitter
  url: https://x.com/ChainAware
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/chainaware
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@ChainAware
- group: operate
  title: ''
  type: Community
  url: https://t.me/ChainAware_ai
- group: agent
  href: https://artifacts.apis.io/chainaware-ai/llms/chainaware-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/chainaware-ai-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://chainaware.ai/llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://chainaware.ai/learn/llms.txt
- group: other
  href: https://artifacts.apis.io/chainaware-ai/a2a/chainaware-ai-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/chainaware-ai-a2a.yml
- group: agent
  href: https://artifacts.apis.io/chainaware-ai/mcp/chainaware-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/chainaware-ai-mcp.yml
- group: agent
  href: https://artifacts.apis.io/chainaware-ai/well-known/chainaware-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/chainaware-ai-well-known.yml
- group: design
  href: https://artifacts.apis.io/chainaware-ai/conventions/chainaware-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/chainaware-ai-conventions.yml
- group: design
  href: https://artifacts.apis.io/chainaware-ai/errors/chainaware-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/chainaware-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/chainaware-ai/data-model/chainaware-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/chainaware-ai-data-model.yml
- group: operate
  href: https://artifacts.apis.io/chainaware-ai/rate-limits/chainaware-ai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/chainaware-ai-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/chainaware-ai/plans/chainaware-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/chainaware-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/chainaware-ai/conformance/chainaware-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/chainaware-ai-conformance.yml
- group: design
  href: https://artifacts.apis.io/chainaware-ai/lifecycle/chainaware-ai-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/chainaware-ai-lifecycle.yml
- group: agent
  href: https://artifacts.apis.io/chainaware-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/chainaware-ai/components/chainaware-ai-components.yml
  title: ''
  type: Components
  url: components/chainaware-ai-components.yml
- group: other
  title: ''
  type: DataSubjectRequest
  url: https://chainaware.ai/privacy/
- group: other
  title: ''
  type: AITransparency
  url: https://chainaware.ai/terms/
created: '2026-09-19'
description: 'ChainAware.ai is an AI-powered blockchain intelligence platform, operated by Decentral Tech OÜ (Estonia) with algorithms from the SmartCredit.io team, that scores wallets, tokens, smart contracts and ERC-8004 AI agents for fraud, rug-pull, credit and trust risk across eight blockchains (Ethereum, BNB Smart Chain, Polygon, Base, Solana, TON, Tron, HAQQ) using 23M+ behavioural wallet profiles. The same models are exposed three ways: a five-operation Enterprise REST API at enterprise.api.chainaware.ai (Swagger 2.0 published at swagger.chainaware.ai, x-api-key auth, Business/Enterprise subscriptions); a hosted MCP server at prediction.mcp.chainaware.ai/sse (14 tools, anonymous tools/list, MIT-licensed source, listed in the official MCP registry); and an A2A 0.3.0 agent card at api.chainaware.ai/.well-known/agent-card.json whose five skills are paid per call through x402 (USDC on Base, $0.15 per call) or with an API key.'
finops:
- has_sources: true
  method: derived
  name: Chainaware Ai Finops
  primary_unit: 2 weeks
  service_category: ''
  slug: chainaware-ai-finops
  template: false
image: https://chainaware.ai/assets/brand/chainawareai-logo.svg
layout: provider
mcp_servers:
- description: 'ChainAware operates ONE hosted MCP server, reachable at two hostnames that serve the same 25,293-byte landing page and the same tool set: prediction.mcp.chainaware.ai (the name every provider document'
  name: ChainAware.ai MCP Server
  slug: chainaware-ai-mcp-yml
modified: '2026-10-06'
name: ChainAware.ai
nav: Providers
network: true
overview: 'ChainAware.ai publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Behaviour Prediction API, Credit Score API, Fraud API, and 2 more. Tagged areas include Blockchain, Web3, DeFi, Fraud Prevention, and AML.


  The ChainAware.ai catalog on APIs.io includes 1 Spectral governance ruleset.


  ChainAware.ai''s developer surface includes engineering blog, authentication, documentation, API reference, getting-started guide, support, GitHub presence, and 32 more developer resources.'
plans:
- name: Chainaware Ai Plans Pricing
  plan_count: 4
  slug: chainaware-ai-plans-pricing
- name: Chainaware Ai Price Estimates
  plan_count: 0
  slug: chainaware-ai-price-estimates
random_paper: 18
rate_limits:
- limit_count: 0
  name: Chainaware Ai Rate Limits
  slug: chainaware-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 90
  extends:
  - spectral:oas
  name: ChainAware.ai API Rules
  rule_count: 49
  severity_counts:
    error: 47
    hint: 0
    info: 1
    warn: 1
  slug: chainaware-ai-rules
score:
  band: developing
  composite: 46.2
  coverage:
    artifact_dirs: 29
    catalog_earned: 56.5
    catalog_earned_first_party: 12.0
    catalog_gap: 58.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.3
  facets:
    access_clarity: 61.8
    contract_governance: 31.8
    contract_quality: 51.0
    developer_ergonomics: 41.7
    discoverability: 75.0
    operational_transparency: 5.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - estonia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 54.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 100.0
      total: 3
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/chainaware-ai/chainaware-ai-2026-10-11T102836.png
security:
- kind: authentication
  name: Chainaware Ai Authentication
  slug: chainaware-ai-authentication
  summary_line: apiKey · 6 schemes
- kind: domain-security
  name: Chainaware Ai Domain Security
  slug: chainaware-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 4
skills:
- name: chainaware-behavioral-prediction
  slug: chainaware-ai-SKILL
- name: chainaware-ai-assess-borrower
  slug: chainaware-ai-assess-borrower
- name: chainaware-ai-screen-contract-before-deposit
  slug: chainaware-ai-screen-contract-before-deposit
- name: chainaware-ai-screen-wallet-at-connect
  slug: chainaware-ai-screen-wallet-at-connect
slug: chainaware-ai
tags:
- Blockchain
- Web3
- DeFi
- Fraud Prevention
- AML
- Compliance
- Credit Scoring
- Risk Scoring
- Smart Contract Security
- Agent Trust
- MCP
- A2A
- x402
- Agents
- Agent-Native
- Estonia
website: https://chainaware.ai/
---
