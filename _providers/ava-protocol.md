---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    idempotency: documented
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 35.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 16
  human_in_the_loop: 0
  name: Ava Protocol Agentic Access
  operation_count: 32
  slug: ava-protocol-agentic-access
  summary_line: 32 operations · 16 acting
api_count: 1
apis:
- baseURL: https://gateway.avaprotocol.org/api/v1
  baseurl_source: declared
  description: Token issuance and credential management
  name: Ava Protocol Auth API
  slug: ava-protocol-auth-api
- baseURL: https://gateway.avaprotocol.org/api/v1
  baseurl_source: declared
  description: Workflow execution history and status
  name: Ava Protocol Executions API
  slug: ava-protocol-executions-api
- baseURL: https://gateway.avaprotocol.org/api/v1
  baseurl_source: declared
  description: Liveness / readiness probes
  name: Ava Protocol Health API
  slug: ava-protocol-health-api
- baseURL: https://gateway.avaprotocol.org/api/v1
  baseurl_source: declared
  description: Stand-alone node execution
  name: Ava Protocol Nodes API
  slug: ava-protocol-nodes-api
- baseURL: https://gateway.avaprotocol.org/api/v1
  baseurl_source: declared
  description: Connected operator status (read-only)
  name: Ava Protocol Operators API
  slug: ava-protocol-operators-api
- baseURL: https://gateway.avaprotocol.org/api/v1
  baseurl_source: declared
  description: User/workflow/org secret storage
  name: Ava Protocol Secrets API
  slug: ava-protocol-secrets-api
- baseURL: https://gateway.avaprotocol.org/api/v1
  baseurl_source: declared
  description: ERC-20 metadata lookup
  name: Ava Protocol Tokens API
  slug: ava-protocol-tokens-api
- baseURL: https://gateway.avaprotocol.org/api/v1
  baseurl_source: declared
  description: Stand-alone trigger evaluation
  name: Ava Protocol Triggers API
  slug: ava-protocol-triggers-api
- baseURL: https://gateway.avaprotocol.org/api/v1
  baseurl_source: declared
  description: Smart-wallet derivation and operations
  name: Ava Protocol Wallets API
  slug: ava-protocol-wallets-api
- baseURL: https://gateway.avaprotocol.org/api/v1
  baseurl_source: declared
  description: Workflow CRUD and lifecycle actions
  name: Ava Protocol Workflows API
  slug: ava-protocol-workflows-api
artifact_total: 27
collections:
- collection_type: open
  name: Ava Protocol AVS Auth API
  slug: open-ava-protocol-auth-api
- collection_type: open
  name: Ava Protocol AVS Auth Executions API
  slug: open-ava-protocol-executions-api
- collection_type: open
  name: Ava Protocol AVS Auth Health API
  slug: open-ava-protocol-health-api
- collection_type: open
  name: Ava Protocol AVS Auth Nodes API
  slug: open-ava-protocol-nodes-api
- collection_type: open
  name: Ava Protocol AVS Auth Operators API
  slug: open-ava-protocol-operators-api
- collection_type: open
  name: Ava Protocol AVS Auth Secrets API
  slug: open-ava-protocol-secrets-api
- collection_type: open
  name: Ava Protocol AVS Auth Tokens API
  slug: open-ava-protocol-tokens-api
- collection_type: open
  name: Ava Protocol AVS Auth Triggers API
  slug: open-ava-protocol-triggers-api
- collection_type: open
  name: Ava Protocol AVS Auth Wallets API
  slug: open-ava-protocol-wallets-api
- collection_type: open
  name: Ava Protocol AVS Auth Workflows API
  slug: open-ava-protocol-workflows-api
common:
- group: other
  href: https://artifacts.apis.io/ava-protocol/capabilities/ava-protocol-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/ava-protocol-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/ava-protocol/overlays/ava-protocol-avs-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/ava-protocol-avs-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/ava-protocol/agentic-access/ava-protocol-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/ava-protocol-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/ava-protocol/authentication/ava-protocol-authentication.yml
  title: ''
  type: Authentication
  url: authentication/ava-protocol-authentication.yml
- group: auth
  href: https://artifacts.apis.io/ava-protocol/security/ava-protocol-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ava-protocol-domain-security.yml
- group: build
  href: https://artifacts.apis.io/ava-protocol/packages/ava-protocol-packages.yml
  title: ''
  type: Packages
  url: packages/ava-protocol-packages.yml
- group: build
  href: https://artifacts.apis.io/ava-protocol/packages/ava-protocol-packages.yml
  title: ''
  type: SDKs
  url: packages/ava-protocol-packages.yml
- group: agent
  href: https://artifacts.apis.io/ava-protocol/mcp/ava-protocol-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/ava-protocol-mcp.yml
- group: agent
  href: https://artifacts.apis.io/ava-protocol/llms/ava-protocol-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ava-protocol-llms.txt
- group: other
  href: https://artifacts.apis.io/ava-protocol/grpc/ava-protocol-avs.proto
  title: ''
  type: Protobuf
  url: grpc/ava-protocol-avs.proto
- group: design
  href: https://artifacts.apis.io/ava-protocol/errors/ava-protocol-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/ava-protocol-problem-types.yml
- group: design
  href: https://artifacts.apis.io/ava-protocol/conventions/ava-protocol-conventions.yml
  title: ''
  type: Conventions
  url: conventions/ava-protocol-conventions.yml
- group: design
  href: https://artifacts.apis.io/ava-protocol/conventions/ava-protocol-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/ava-protocol-conventions.yml
- group: design
  href: https://artifacts.apis.io/ava-protocol/conformance/ava-protocol-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ava-protocol-conformance.yml
- group: design
  href: https://artifacts.apis.io/ava-protocol/lifecycle/ava-protocol-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/ava-protocol-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/ava-protocol/data-model/ava-protocol-data-model.yml
  title: ''
  type: DataModel
  url: data-model/ava-protocol-data-model.yml
- group: start
  href: https://artifacts.apis.io/ava-protocol/sandbox/ava-protocol-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/ava-protocol-sandbox.yml
- group: build
  href: https://artifacts.apis.io/ava-protocol/cli/ava-protocol-cli.yml
  title: ''
  type: CLI
  url: cli/ava-protocol-cli.yml
- group: agent
  href: https://artifacts.apis.io/ava-protocol/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://avaprotocol.org/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://avaprotocol.org/docs/ava-sdk-js/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://avaprotocol.org/docs/ava-sdk-js/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://avaprotocol.org/docs/ava-sdk-js/rest-api
- group: start
  title: ''
  type: GettingStarted
  url: https://avaprotocol.org/docs/ava-sdk-js/getting-started
- group: auth
  title: ''
  type: Authentication
  url: https://avaprotocol.org/docs/ava-sdk-js/authentication
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AvaProtocol
- group: company
  title: ''
  type: Blog
  url: https://avaprotocol.org/blog
- group: start
  title: ''
  type: SignUp
  url: https://app.avaprotocol.org
- group: operate
  title: ''
  type: Support
  url: https://avaprotocol.org/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://avaprotocol.org/legal/discord-bot-terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://avaprotocol.org/legal/discord-bot-privacy
- group: company
  title: ''
  type: Twitter
  url: https://x.com/ava_protocol
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/7W9UDvsbwh
created: '2026-07-17'
description: Ava Protocol is an AI-powered onchain automation platform for Ethereum and L2s (Base, Soneium), and the evolution of the OAK Network Substrate automation parachain. Users create "workflows" that connect triggers (scheduled time, price conditions, onchain events, or manual) to actions (swaps, transfers, contract calls, notifications) and run them non-custodially from scoped smart wallets — the user always approves before execution. Verifiable execution is provided by an EigenLayer AVS (Actively Validated Service). Developers integrate through a public REST API (the AVS aggregator gateway) and a TypeScript SDK, authenticating with a JWT bearer token obtained via wallet signature (EIP-191) or an operator-minted key.
image: https://avaprotocol.org/image/open-graph/index.jpg
layout: provider
modified: '2026-07-18'
name: Ava Protocol
nav: Providers
network: true
overview: 'Ava Protocol publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Auth API, Executions API, Health API, and 7 more. Tagged areas include Company, Fintech, Blockchain, DeFi, and Automation.


  The Ava Protocol catalog on APIs.io includes 1 Spectral governance ruleset.


  Ava Protocol''s developer surface includes authentication, sandbox, CLI, documentation, API reference, getting-started guide, engineering blog, and 26 more developer resources.'
random_paper: 15
rules:
- authorship: generated
  effective_rule_count: 96
  extends:
  - spectral:oas
  name: Ava Protocol API Rules
  rule_count: 55
  severity_counts:
    error: 48
    hint: 0
    info: 3
    warn: 4
  slug: ava-protocol-rules
score:
  band: developing
  composite: 45.2
  coverage:
    artifact_dirs: 26
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 42.2
    developer_ergonomics: 80.4
    discoverability: 73.2
    operational_transparency: 2.6
  previous_composite: 45.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 22.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 22.2
screenshot: https://apis.io/screenshots/ava-protocol/ava-protocol-2026-07-25T201902.png
security:
- kind: authentication
  name: Ava Protocol Authentication
  slug: ava-protocol-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Ava Protocol Domain Security
  slug: ava-protocol-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: Authenticate to the Ava Protocol AVS API
  slug: ava-protocol-authenticate
- name: Create and monitor an onchain automation workflow
  slug: ava-protocol-create-and-monitor-workflow
- name: Manage an Ava Protocol smart wallet
  slug: ava-protocol-manage-smart-wallet
slug: ava-protocol
tags:
- Company
- Fintech
- Blockchain
- DeFi
- Automation
- Web3
- Ethereum
- Smart Wallets
- Workflows
- AI Agents
website: https://avaprotocol.org/
---
