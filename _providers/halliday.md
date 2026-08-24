---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 48.3
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Halliday Agentic Access
  operation_count: 16
  slug: halliday-agentic-access
  summary_line: 16 operations · 9 acting
api_count: 4
apis:
- description: Asset information, discovery, and supported asset pairs
  name: Halliday Assets API
  slug: halliday-assets-api
- description: Blockchain network information and configuration
  name: Halliday Chains API
  slug: halliday-chains-api
- description: Core payment operations including quotes, confirmation, and status tracking
  name: Halliday Payments API
  slug: halliday-payments-api
- description: Register HTTPS endpoints to receive signed notifications when a workflow reaches a terminal state, instead of polling for status. You subscribe to one or more event types per webhook. | Event type | F
  name: Halliday Webhooks API
  slug: halliday-webhooks-api
artifact_total: 14
asyncapis:
- description: ''
  name: Halliday Webhooks
  slug: halliday-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Halliday API V2 Assets API
  slug: open-halliday-assets-api
- collection_type: open
  name: Halliday API V2 Assets Chains API
  slug: open-halliday-chains-api
- collection_type: open
  name: Halliday API V2 Assets Payments API
  slug: open-halliday-payments-api
- collection_type: open
  name: Halliday API V2 Assets Webhooks API
  slug: open-halliday-webhooks-api
common:
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/halliday-openapi-original.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.halliday.xyz
- group: docs
  title: ''
  type: Documentation
  url: https://docs.halliday.xyz
- group: docs
  title: ''
  type: APIReference
  url: https://docs.halliday.xyz/pages/halliday-api-docs.md
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.halliday.xyz/pages/api-quickstart.md
- group: operate
  title: ''
  type: Support
  url: https://halliday.xyz/contact
- group: company
  title: ''
  type: Blog
  url: https://blog.halliday.xyz
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/HallidayInc
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.halliday.xyz/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://halliday.xyz/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://halliday.xyz/legal/privacy-policy
- group: start
  title: ''
  type: Sandbox
  url: https://demo.halliday.xyz/
- group: auth
  title: ''
  type: Compliance
  url: https://docs.halliday.xyz/pages/compliance-security.md
- group: auth
  title: ''
  type: Authentication
  url: authentication/halliday-authentication.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/halliday-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/halliday-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/halliday-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/halliday-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/halliday-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/halliday-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/halliday-openapi-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/halliday-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/halliday-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/halliday-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/halliday-conventions.yml
- group: design
  title: ''
  type: Components
  url: components/halliday-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/halliday-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/halliday-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Halliday is a web3 payments and agentic-workflow company (a16z crypto Series A) building the end-to-end onchain deposit platform. Its Agentic Workflow Protocol (AWP) lets developers compose high-level, AI-executable workflows behind immutable guardrails without writing smart-contract code. The flagship product, Halliday Payments, is a unified cross-chain payments API and drop-in widget that lets users onramp from fiat, bridge, and swap to acquire any asset on any chain in a fully self-custodial way, routing intelligently across onramps (MoonPay, Transak, Stripe), swaps, and bridges. The Halliday API V2 (https://v2.prod.halliday.xyz) exposes chains, assets, quotes, payments, balances, withdrawals, and signed workflow webhooks, authenticated with publishable API keys, alongside JS/React/React Native SDKs and a published Claude Code integration skill.
image: https://halliday.xyz/opengraph-image
layout: provider
mcp_servers:
- description: ''
  name: Halliday MCP Server
  slug: halliday-mcp-server
modified: '2026-07-19'
name: Halliday
nav: Providers
network: true
overview: 'Halliday publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Assets API, Chains API, Payments API, and 1 more. Tagged areas include Company, Payments, Cryptocurrency, Blockchain, and Web3.


  The Halliday catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Halliday''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, sandbox, and 22 more developer resources.'
random_paper: 0
score:
  band: developing
  composite: 54.2
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 30.3
    contract_quality: 73.5
    developer_ergonomics: 73.8
    discoverability: 81.5
    governance: 30.3
    operational_transparency: 10.5
  previous_composite: 54.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 46.9
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/halliday/refs/heads/main/screenshots/halliday-2026-07-25T220546.png
security:
- kind: authentication
  name: Halliday Authentication
  slug: halliday-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Halliday Domain Security
  slug: halliday-domain-security
  summary_line: TLSv1.3 · DMARC
slug: halliday
tags:
- Company
- Payments
- Cryptocurrency
- Blockchain
- Web3
- On-Ramp
- Swaps
- DeFi
- Agentic Workflows
- Fintech
website: https://docs.halliday.xyz
---
