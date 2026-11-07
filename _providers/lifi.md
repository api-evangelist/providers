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
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
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
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: full
    openapi_examples: verified
    operation_distinctiveness: mostly
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 41.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 6
  human_in_the_loop: 1
  name: Lifi Agentic Access
  operation_count: 33
  slug: lifi-agentic-access
  summary_line: 33 operations · 6 acting · 1 human-in-the-loop
api_count: 2
apis:
- description: Intent-based execution API for the LI.FI solver marketplace. Integrators request quotes and submit orders; solvers publish standing quote inventory and fill intents. Built on the Open Intents Framewor
  name: LI.FI Intents Order Server API
  slug: lifi-intents-order-server-api
- baseURL: https://li.quest
  baseurl_source: declared
  description: The advanced API from LI.FI — 3 operation(s) for advanced.
  name: LI.FI Advanced API
  slug: lifi-advanced-api
- baseURL: https://li.quest
  baseurl_source: declared
  description: The Analytics API from LI.FI — 4 operation(s) for analytics.
  name: LI.FI Analytics API
  slug: lifi-analytics-api
- baseURL: https://li.quest
  baseurl_source: declared
  description: The Chains API from LI.FI — 1 operation(s) for chains.
  name: LI.FI Chains API
  slug: lifi-chains-api
- baseURL: https://li.quest
  baseurl_source: declared
  description: The Connections API from LI.FI — 1 operation(s) for connections.
  name: LI.FI Connections API
  slug: lifi-connections-api
- baseURL: https://li.quest
  baseurl_source: declared
  description: The Earn Chains API from LI.FI — 1 operation(s) for earn chains.
  name: LI.FI Earn Chains API
  slug: lifi-earn-chains-api
- baseURL: https://li.quest
  baseurl_source: declared
  description: The Earn Portfolio API from LI.FI — 1 operation(s) for earn portfolio.
  name: LI.FI Earn Portfolio API
  slug: lifi-earn-portfolio-api
- baseURL: https://li.quest
  baseurl_source: declared
  description: The Earn Protocols API from LI.FI — 1 operation(s) for earn protocols.
  name: LI.FI Earn Protocols API
  slug: lifi-earn-protocols-api
- baseURL: https://li.quest
  baseurl_source: declared
  description: The Earn Vaults API from LI.FI — 2 operation(s) for earn vaults.
  name: LI.FI Earn Vaults API
  slug: lifi-earn-vaults-api
- baseURL: https://li.quest
  baseurl_source: declared
  description: The Gas API from LI.FI — 5 operation(s) for gas.
  name: LI.FI Gas API
  slug: lifi-gas-api
- baseURL: https://li.quest
  baseurl_source: declared
  description: The Integrators API from LI.FI — 2 operation(s) for integrators.
  name: LI.FI Integrators API
  slug: lifi-integrators-api
- baseURL: https://li.quest
  baseurl_source: declared
  description: The Quote API from LI.FI — 4 operation(s) for quote.
  name: LI.FI Quote API
  slug: lifi-quote-api
- baseURL: https://li.quest
  baseurl_source: declared
  description: The Relayer API from LI.FI — 3 operation(s) for relayer.
  name: LI.FI Relayer API
  slug: lifi-relayer-api
- baseURL: https://li.quest
  baseurl_source: declared
  description: The Status API from LI.FI — 1 operation(s) for status.
  name: LI.FI Status API
  slug: lifi-status-api
- baseURL: https://li.quest
  baseurl_source: declared
  description: The Token API from LI.FI — 1 operation(s) for token.
  name: LI.FI Token API
  slug: lifi-token-api
- baseURL: https://li.quest
  baseurl_source: declared
  description: The Tokens API from LI.FI — 1 operation(s) for tokens.
  name: LI.FI Tokens API
  slug: lifi-tokens-api
- baseURL: https://li.quest
  baseurl_source: declared
  description: The Tools API from LI.FI — 1 operation(s) for tools.
  name: LI.FI Tools API
  slug: lifi-tools-api
- baseURL: https://order.li.fi
  baseurl_source: declared
  description: The Call Data API from LI.FI — 1 operation(s) for call data.
  name: LI.FI Call Data API
  slug: lifi-call-data-api
artifact_total: 47
collections:
- collection_type: open
  name: LI.FI Earn advanced API
  slug: open-lifi-advanced-api
- collection_type: open
  name: LI.FI Earn advanced Analytics API
  slug: open-lifi-analytics-api
- collection_type: open
  name: LI.FI Earn advanced Calldata API
  slug: open-lifi-calldata-api
- collection_type: open
  name: LI.FI Earn advanced Chains API
  slug: open-lifi-chains-api
- collection_type: open
  name: LI.FI Earn advanced Connections API
  slug: open-lifi-connections-api
- collection_type: open
  name: LI.FI Earn advanced Earn Chains API
  slug: open-lifi-earn-chains-api
- collection_type: open
  name: LI.FI Earn advanced Earn Portfolio API
  slug: open-lifi-earn-portfolio-api
- collection_type: open
  name: LI.FI Earn advanced Earn Protocols API
  slug: open-lifi-earn-protocols-api
- collection_type: open
  name: LI.FI Earn advanced Earn Vaults API
  slug: open-lifi-earn-vaults-api
- collection_type: open
  name: LI.FI Earn advanced Gas API
  slug: open-lifi-gas-api
- collection_type: open
  name: LI.FI Earn advanced Integrators API
  slug: open-lifi-integrators-api
- collection_type: open
  name: LI.FI Earn advanced Quote API
  slug: open-lifi-quote-api
- collection_type: open
  name: LI.FI Earn advanced Relayer API
  slug: open-lifi-relayer-api
- collection_type: open
  name: LI.FI Earn advanced Status API
  slug: open-lifi-status-api
- collection_type: open
  name: LI.FI Earn advanced Token API
  slug: open-lifi-token-api
- collection_type: open
  name: LI.FI Earn advanced Tokens API
  slug: open-lifi-tokens-api
- collection_type: open
  name: LI.FI Earn advanced Tools API
  slug: open-lifi-tools-api
common:
- group: commercial
  href: https://artifacts.apis.io/lifi/plans/lifi-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/lifi-plans-pricing.yml
- group: company
  title: ''
  type: BlogRSS
  url: https://blog.li.fi/feed
- group: company
  title: ''
  type: Website
  url: https://li.fi
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.li.fi
- group: docs
  title: ''
  type: Documentation
  url: https://docs.li.fi
- group: docs
  title: ''
  type: APIReference
  url: https://docs.li.fi/api-reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.li.fi/introduction/introduction
- group: operate
  title: ''
  type: Support
  url: https://li.fi/contact-us
- group: company
  title: ''
  type: Blog
  url: https://blog.li.fi
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/lifinance
- group: commercial
  title: ''
  type: Pricing
  url: https://li.fi/plans/
- group: start
  title: ''
  type: SignUp
  url: https://portal.li.fi
- group: commercial
  title: ''
  type: TermsOfService
  url: https://li.fi/legal/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://li.fi/legal/privacy-policy/
- group: operate
  href: https://artifacts.apis.io/lifi/changelog/lifi-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/lifi-changelog.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.li.fi
- group: design
  href: https://artifacts.apis.io/lifi/lifecycle/lifi-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/lifi-lifecycle.yml
- group: auth
  title: ''
  type: Security
  url: https://docs.li.fi/introduction/learn-more/security-and-audits
- group: auth
  href: https://artifacts.apis.io/lifi/security/lifi-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/lifi-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/lifi/security/lifi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/lifi-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/lifi/authentication/lifi-authentication.yml
  title: ''
  type: Authentication
  url: authentication/lifi-authentication.yml
- group: build
  href: https://artifacts.apis.io/lifi/packages/lifi-packages.yml
  title: ''
  type: Packages
  url: packages/lifi-packages.yml
- group: build
  href: https://artifacts.apis.io/lifi/packages/lifi-packages.yml
  title: ''
  type: SDKs
  url: packages/lifi-packages.yml
- group: build
  href: https://artifacts.apis.io/lifi/cli/lifi-cli.yml
  title: ''
  type: CLI
  url: cli/lifi-cli.yml
- group: design
  href: https://artifacts.apis.io/lifi/components/lifi-components.yml
  title: ''
  type: Components
  url: components/lifi-components.yml
- group: start
  href: https://artifacts.apis.io/lifi/sandbox/lifi-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/lifi-sandbox.yml
- group: agent
  href: https://artifacts.apis.io/lifi/mcp/lifi-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/lifi-mcp.yml
- group: agent
  href: https://artifacts.apis.io/lifi/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/lifi/agentic-access/lifi-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/lifi-agentic-access.yml
- group: agent
  href: https://artifacts.apis.io/lifi/llms/lifi-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/lifi-llms.txt
- group: agent
  href: https://artifacts.apis.io/lifi/well-known/lifi-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/lifi-well-known.yml
- group: operate
  href: https://artifacts.apis.io/lifi/rate-limits/lifi-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/lifi-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/lifi/errors/lifi-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/lifi-error-codes.yml
- group: design
  href: https://artifacts.apis.io/lifi/conventions/lifi-conventions.yml
  title: ''
  type: Conventions
  url: conventions/lifi-conventions.yml
- group: design
  href: https://artifacts.apis.io/lifi/conformance/lifi-conformance.yml
  title: ''
  type: Conformance
  url: conformance/lifi-conformance.yml
- group: design
  href: https://artifacts.apis.io/lifi/data-model/lifi-data-model.yml
  title: ''
  type: DataModel
  url: data-model/lifi-data-model.yml
- group: other
  href: https://artifacts.apis.io/lifi/overlays/lifi-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/lifi-api-overlay.yaml
created: '2026-07-17'
description: LI.FI is the routing and execution layer for cross-chain liquidity, payments, swaps and yield. A single integration gives an application access to more than 100 aggregated bridges, DEXs, DEX aggregators and intent-based solvers across 58+ chains spanning EVM, Solana, Bitcoin, SUI and TRON. The LI.FI API returns an optimal route plus a ready-to-sign, unsigned transaction; the product set extends to Composer for one-click DeFi deposits across 20+ protocols, Earn for yield discovery and portfolio tracking, an intent/solver marketplace built on the Open Intents Framework, an embeddable Widget, a TypeScript SDK, a CLI and a hosted MCP server for AI agents.
finops:
- has_sources: true
  method: derived
  name: Lifi Finops
  primary_unit: ''
  service_category: ''
  slug: lifi-finops
  template: true
image: https://docs.li.fi/logo/dark.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.li.quest over HTTP; 19 tools listed.
  name: LI.FI MCP Server
  slug: lifi
modified: '2026-10-06'
name: LI.FI
nav: Providers
network: true
overview: 'LI.FI publishes 18 API contracts indexed on the [APIs.io](https://apis.io/) network, including Advanced API, Analytics API, Chains API, and 15 more. Tagged areas include Company, Web3, Blockchain, Cross-Chain, and Bridge.


  The LI.FI catalog on APIs.io includes 1 Spectral governance ruleset.


  LI.FI''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 30 more developer resources.'
plans:
- name: Lifi Plans Pricing
  plan_count: 2
  slug: lifi-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 4
  name: Lifi Rate Limits
  slug: lifi-rate-limits
rules:
- authorship: generated
  effective_rule_count: 95
  extends:
  - spectral:oas
  name: LI.FI API Rules
  rule_count: 54
  severity_counts:
    error: 40
    hint: 0
    info: 6
    warn: 8
  slug: lifi-rules
score:
  band: strong
  composite: 60.7
  coverage:
    artifact_dirs: 31
    catalog_earned: 61.5
    catalog_earned_first_party: 20.0
    catalog_gap: 53.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.3
  facets:
    access_clarity: 59.2
    contract_governance: 18.2
    contract_quality: 50.6
    developer_ergonomics: 80.4
    discoverability: 75.0
    operational_transparency: 76.3
  previous_composite: 59.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 17
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 27.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/lifi/lifi-2026-07-25T225052.png
security:
- kind: authentication
  name: Lifi Authentication
  slug: lifi-authentication
  summary_line: apiKey · 5 schemes
- kind: domain-security
  name: Lifi Domain Security
  slug: lifi-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Lifi Vulnerability Disclosure
  slug: lifi-vulnerability-disclosure
  summary_line: contact published
skill_count: 3
skills:
- name: Compare multiple LI.FI routes and execute a chosen one step by step
  slug: lifi-compare-routes-and-execute
- name: Execute a cross-chain token transfer with LI.FI
  slug: lifi-cross-chain-transfer
- name: Discover a yield vault and deposit into it with LI.FI Earn and Composer
  slug: lifi-discover-and-deposit-yield
slug: lifi
tags:
- Company
- Web3
- Blockchain
- Cross-Chain
- Bridge
- DEX Aggregation
- DeFi
- Payments
- Liquidity
- Yield
- Intents
- Agents
- Cryptocurrency
website: https://li.fi
---
