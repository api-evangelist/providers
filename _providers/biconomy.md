---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.6
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Biconomy Agentic Access
  operation_count: 5
  slug: biconomy-agentic-access
  summary_line: 5 operations · 5 acting
api_count: 2
apis:
- description: Biconomy's open-source ERC-4337 TypeScript Bundler. Implements eth_sendUserOperation, eth_estimateUserOperationGas, eth_getUserOperationByHash, eth_getUserOperationReceipt, and eth_supportedEntryPoint
  name: Biconomy Bundler API
  slug: biconomy-bundler-api
- description: ERC-4337 paymaster service that fronts gas on behalf of end users so dApps can offer gasless UX. Two modes — full sponsorship (developer pays gas, post-paid invoiced monthly) and pay-in-tokens (user p
  name: Biconomy Sponsorship Paymaster
  slug: biconomy-sponsorship-paymaster
- description: Nexus is Biconomy's ERC-7579 modular smart contract account, audited by CodeHawks-Cyfrin (Sept 2024), Spearbit (Oct/Nov 2024), Zenith (Mar 2025), and Pashov (Mar 2025), and pre-deployed across 20+ EVM
  name: Biconomy Nexus Smart Account
  slug: biconomy-nexus-smart-account
- description: Smart Sessions is a delegated-execution framework layered on Nexus. A session key is granted a scoped set of policies (Sudo, Universal Action, Time Range, Usage Limit) that bound what an agent or auto
  name: Biconomy Smart Sessions API
  slug: biconomy-smart-sessions-api
- description: AbstractJS (@biconomy/abstractjs) is Biconomy's TypeScript-first SDK with a Viem-inspired API. Wraps the Supertransaction API and Nexus smart account operations, exposing createMeeClient, getQuote, ex
  name: Biconomy AbstractJS SDK
  slug: biconomy-abstractjs-sdk
- description: The instructions API from Biconomy — 2 operation(s) for instructions.
  name: Biconomy instructions API
  slug: biconomy-instructions-api
- description: The mee API from Biconomy — 1 operation(s) for mee.
  name: Biconomy mee API
  slug: biconomy-mee-api
- description: The root API from Biconomy — 2 operation(s) for root.
  name: Biconomy root API
  slug: biconomy-root-api
- description: GET /api/public/projects/me/supertransactions returns a project's full supertransaction history for reporting, reconciliation and gas-spend accounting. Each item carries the supertransaction hash, exe
  name: Biconomy Dashboard Public API
  slug: biconomy-dashboard-public-api
- description: 'Status and tracking surface for a submitted supertransaction. GET /v1/explorer/{supertxHash} returns the terminal execution state (SUCCESS, FAILED) with execution details, authenticated with the same '
  name: Biconomy MEE Explorer API
  slug: biconomy-mee-explorer-api
artifact_total: 30
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Supertransaction instructions API
  slug: open-biconomy-instructions-api
- collection_type: open
  name: Supertransaction instructions mee API
  slug: open-biconomy-mee-api
- collection_type: open
  name: Supertransaction instructions root API
  slug: open-biconomy-root-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/biconomy-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/biconomy-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/biconomy-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://www.biconomy.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.biconomy.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.biconomy.io/llms.txt
- group: other
  title: ''
  type: Dashboard
  url: https://dashboard.biconomy.io
- group: other
  title: ''
  type: Explorer
  url: https://meescan.biconomy.io
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/bcnmy
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/bcnmy/nexus
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/bcnmy/abstractjs
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/bcnmy/bundler
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/bcnmy/biconomy-paymasters
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/bcnmy/mee-contracts
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/bcnmy/stx-contracts
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/bcnmy/erc8211-contracts
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/bcnmy/entry-point-gas-estimations
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/bcnmy/session-permissioned-intents
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/bcnmy/awesome-biconomy
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@biconomy/abstractjs
- group: docs
  title: ''
  type: Documentation
  url: https://docs.biconomy.io/sdk-reference
- group: docs
  title: ''
  type: Documentation
  url: https://docs.biconomy.io/sdk-reference/account
- group: docs
  title: ''
  type: Documentation
  url: https://docs.biconomy.io/sdk-reference/client
- group: docs
  title: ''
  type: Documentation
  url: https://docs.biconomy.io/sdk-reference/instructions
- group: docs
  title: ''
  type: Documentation
  url: https://docs.biconomy.io/sdk-reference/runtime
- group: docs
  title: ''
  type: Documentation
  url: https://docs.biconomy.io/sdk-reference/conditions
- group: docs
  title: ''
  type: Documentation
  url: https://docs.biconomy.io/sdk-reference/sessions
- group: docs
  title: ''
  type: Documentation
  url: https://docs.biconomy.io/sdk-reference/utilities
- group: docs
  title: ''
  type: Documentation
  url: https://docs.biconomy.io/wallet-integrations
- group: docs
  title: ''
  type: Documentation
  url: https://docs.biconomy.io/wallet-integrations/privy/api
- group: docs
  title: ''
  type: Documentation
  url: https://docs.biconomy.io/wallet-integrations/turnkey/api
- group: docs
  title: ''
  type: Documentation
  url: https://docs.biconomy.io/wallet-integrations/para/api
- group: docs
  title: ''
  type: Documentation
  url: https://docs.biconomy.io/wallet-integrations/external-wallets/api
- group: docs
  title: ''
  type: Documentation
  url: https://docs.biconomy.io/swaps-trading
- group: docs
  title: ''
  type: Documentation
  url: https://docs.biconomy.io/swaps-trading/gasless-swap
- group: docs
  title: ''
  type: Documentation
  url: https://docs.biconomy.io/swaps-trading/cross-chain-swap
- group: docs
  title: ''
  type: Documentation
  url: https://docs.biconomy.io/swaps-trading/limit-order
- group: docs
  title: ''
  type: Documentation
  url: https://docs.biconomy.io/zaps
- group: docs
  title: ''
  type: Documentation
  url: https://docs.biconomy.io/agents-automation
- group: docs
  title: ''
  type: Documentation
  url: https://docs.biconomy.io/gasless-apps
- group: docs
  title: ''
  type: Documentation
  url: https://docs.biconomy.io/gasless-apps/sponsorship
- group: docs
  title: ''
  type: Documentation
  url: https://docs.biconomy.io/gasless-apps/pay-in-tokens
- group: docs
  title: ''
  type: Documentation
  url: https://docs.biconomy.io/contracts-and-audits
- group: docs
  title: ''
  type: Documentation
  url: https://docs.biconomy.io/contracts-and-audits/supported-chains
- group: company
  title: ''
  type: Blog
  url: https://blog.biconomy.io
- group: company
  title: ''
  type: BlogRSS
  url: https://blog.biconomy.io/rss/
- group: company
  title: ''
  type: Twitter
  url: https://x.com/biconomy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/biconomy
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/biconomy
- group: commercial
  title: ''
  type: Plans
  url: plans/biconomy-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/biconomy-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/biconomy-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/biconomy-vocabulary.yml
- group: design
  title: ''
  type: Rules
  url: rules/biconomy-rules.yml
- group: build
  title: ''
  type: Packages
  url: packages/biconomy-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/biconomy-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/biconomy-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/biconomy-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/biconomy-tool-crosswalk.yml
- group: other
  title: ''
  type: AgentCard
  url: a2a/biconomy-a2a.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/biconomy-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/biconomy-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/biconomy-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/biconomy-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/biconomy-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/biconomy-conventions.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/biconomy-sandbox.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/biconomy-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/biconomy-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: https://docs.biconomy.io/mcp
- group: other
  title: ''
  type: AgentCard
  url: https://docs.biconomy.io/.well-known/agent-card.json
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.biconomy.io/overview/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://docs.biconomy.io/overview/supertransaction-api
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.biconomy.io
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bcnmy
- group: docs
  title: ''
  type: OpenAPI
  url: https://docs.biconomy.io/supertransaction-api/openapi.yaml
created: '2026-05-25'
description: 'Biconomy is the onchain orchestration layer for multi-chain applications, founded in 2019 and headquartered in Singapore. Its Modular Execution Environment (MEE) composes multi-step, cross-chain blockchain workflows — swaps, bridges, DeFi vault deposits, arbitrary contract calls — into a single user signature across 20+ EVM mainnets, handling sequencing, runtime parameter injection, bridge timing, gas abstraction, simulation-based async execution and failure recovery on the developer''s behalf. The commercial surface is a REST Supertransaction API (POST /v1/quote, POST /v1/execute) plus the TypeScript AbstractJS SDK, both sitting on the same engine and the same project API key. Underneath, Biconomy ships open-source account-abstraction infrastructure: an ERC-4337 bundler, ERC-4337 paymasters for gas sponsorship and pay-in-token flows, and Nexus, an ERC-7579 modular smart account audited by Cyfrin, Spearbit, Zenith and Pashov. Smart Sessions layers scoped, time-limited, revocable
  on-chain delegation on top, which is how AI agents and automations transact on a user''s behalf without holding their key. Biconomy also authored ERC-8211 for composable batching.'
examples:
- key_count: 3
  name: Biconomy Execute Example
  slug: biconomy-execute-example
- key_count: 3
  name: Biconomy Quote Eoa 7702 Example
  slug: biconomy-quote-eoa-7702-example
finops:
- name: Biconomy Finops
  service_category: Web3 Infrastructure
  slug: biconomy-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/biconomy.png
json_schemas:
- name: Biconomy MEE Quote Request
  property_count: 8
  slug: biconomy-quote-request
- name: Biconomy MEE Quote Response
  property_count: 3
  slug: biconomy-quote-response
json_structures:
- name: Biconomy Supertransaction Structure
  property_count: 1
  slug: biconomy-supertransaction-structure
jsonld:
- class_count: 24
  name: Biconomy Context
  property_count: 3
  slug: biconomy-context
layout: provider
mcp_servers:
- description: 'Biconomy runs a hosted, anonymous-access MCP server on its documentation host. It is a DOCUMENTATION server, not an execution server: the three tools search, browse and give feedback on the docs corpu'
  name: Biconomy Docs MCP Server
  slug: biconomy-docs-mcp-server
- description: ''
  name: Biconomy Docs MCP endpoint
  slug: biconomy-docs-mcp-endpoint
modified: '2026-08-24'
name: Biconomy
nav: Providers
network: true
overview: 'Biconomy publishes 3 APIs on the [APIs.io](https://apis.io/) network: instructions API, mee API, and root API. Tagged areas include Account Abstraction, Blockchain, Bundler, Cross-Chain, and DeFi.


  The Biconomy catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Biconomy''s developer surface includes authentication, developer portal, documentation, engineering blog, support, sandbox, changelog, and 70 more developer resources.'
plans:
- name: Biconomy Plans Pricing
  plan_count: 2
  slug: biconomy-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 3
  name: Biconomy Rate Limits
  slug: biconomy-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Biconomy API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: biconomy-jsonschema-spectral-rules
- effective_rule_count: 47
  extends:
  - spectral:oas
  name: Biconomy API Rules
  rule_count: 6
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 2
  slug: biconomy-rules
score:
  band: strong
  composite: 59.8
  coverage:
    artifact_dirs: 30
    catalog_gap: 32.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 47.0
    contract_quality: 72.1
    developer_ergonomics: 83.3
    discoverability: 66.7
    governance: 47.0
    operational_transparency: 60.5
  previous_composite: 59.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 26.6
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/biconomy/refs/heads/main/screenshots/biconomy-2026-06-20T173223.png
security:
- kind: authentication
  name: Biconomy Authentication
  slug: biconomy-authentication
  summary_line: apiKey/http-bearer · 3 schemes
- kind: domain-security
  name: Biconomy Domain Security
  slug: biconomy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: biconomy
tags:
- Account Abstraction
- Blockchain
- Bundler
- Cross-Chain
- DeFi
- ERC-4337
- ERC-7579
- ERC-7702
- Ethereum
- Gas Abstraction
- Gasless
- MEE
- Paymaster
- Smart Accounts
- Smart Sessions
- Wallets
- Web3
website: https://docs.biconomy.io
---
