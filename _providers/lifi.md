---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 40.1
  scored_at: '2026-09-04'
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
  name: LI.FI advanced API
  slug: lifi-advanced-api
- baseURL: https://li.quest
  baseurl_source: declared
  description: The Analytics API from LI.FI — 4 operation(s) for analytics.
  name: LI.FI Analytics API
  slug: lifi-analytics-api
- baseURL: https://li.quest
  baseurl_source: declared
  description: The Calldata API from LI.FI — 1 operation(s) for calldata.
  name: LI.FI Calldata API
  slug: lifi-calldata-api
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
artifact_total: 42
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
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
  title: ''
  type: ChangeLog
  url: changelog/lifi-changelog.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.li.fi
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/lifi-lifecycle.yml
- group: auth
  title: ''
  type: Security
  url: https://docs.li.fi/introduction/learn-more/security-and-audits
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/lifi-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lifi-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/lifi-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/lifi-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/lifi-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/lifi-cli.yml
- group: design
  title: ''
  type: Components
  url: components/lifi-components.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/lifi-sandbox.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/lifi-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/lifi-agentic-access.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/lifi-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/lifi-well-known.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/lifi-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/lifi-error-codes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/lifi-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/lifi-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/lifi-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/lifi-api-overlay.yaml
created: '2026-07-17'
description: LI.FI is the routing and execution layer for cross-chain liquidity, payments, swaps and yield. A single integration gives an application access to more than 100 aggregated bridges, DEXs, DEX aggregators and intent-based solvers across 58+ chains spanning EVM, Solana, Bitcoin, SUI and TRON. The LI.FI API returns an optimal route plus a ready-to-sign, unsigned transaction; the product set extends to Composer for one-click DeFi deposits across 20+ protocols, Earn for yield discovery and portfolio tracking, an intent/solver marketplace built on the Open Intents Framework, an embeddable Widget, a TypeScript SDK, a CLI and a hosted MCP server for AI agents.
image: https://docs.li.fi/logo/dark.png
layout: provider
mcp_servers:
- description: ''
  name: LI.FI MCP Server
  slug: lifi-mcp-server
modified: '2026-07-19'
name: LI.FI
nav: Providers
network: true
overview: 'LI.FI publishes 17 APIs on the [APIs.io](https://apis.io/) network, including advanced API, Analytics API, Calldata API, and 14 more. Tagged areas include Company, Crypto Web3, Blockchain, Cross-Chain, and Bridges.


  LI.FI''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 28 more developer resources.'
random_paper: 0
rate_limits:
- limit_count: 4
  name: Lifi Rate Limits
  slug: lifi-rate-limits
score:
  band: strong
  composite: 56.2
  coverage:
    artifact_dirs: 23
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 38.2
    commercial_clarity: 38.2
    contract_governance: 4.5
    contract_quality: 48.3
    developer_ergonomics: 80.4
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 76.3
  previous_composite: 56.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 17
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 48.4
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lifi/refs/heads/main/screenshots/lifi-2026-07-25T225052.png
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
slug: lifi
tags:
- Company
- Crypto Web3
- Blockchain
- Cross-Chain
- Bridges
- DEX Aggregation
- DeFi
- Payments
- Liquidity
- Yield
- Intents
- Agents
website: https://li.fi
---
