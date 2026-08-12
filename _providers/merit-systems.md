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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 46.4
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Merit Systems Agentic Access
  operation_count: 9
  slug: merit-systems-agentic-access
  summary_line: 9 operations · 2 acting
api_count: 6
apis:
- description: The Balances API from Merit Systems — 4 operation(s) for balances.
  name: Merit Systems Balances API
  slug: merit-systems-balances-api
- description: The Invite Codes API from Merit Systems — 1 operation(s) for invite codes.
  name: Merit Systems Invite Codes API
  slug: merit-systems-invite-codes-api
- description: The Organizations API from Merit Systems — 1 operation(s) for organizations.
  name: Merit Systems Organizations API
  slug: merit-systems-organizations-api
- description: The Payments API from Merit Systems — 1 operation(s) for payments.
  name: Merit Systems Payments API
  slug: merit-systems-payments-api
- description: The Search API from Merit Systems — 1 operation(s) for search.
  name: Merit Systems Search API
  slug: merit-systems-search-api
- description: The Send API from Merit Systems — 1 operation(s) for send.
  name: Merit Systems Send API
  slug: merit-systems-send-api
artifact_total: 10
common:
- group: company
  title: ''
  type: Website
  url: https://merit.systems
- group: start
  title: ''
  type: DeveloperPortal
  url: https://agentcash.dev/docs
- group: docs
  title: ''
  type: Documentation
  url: https://agentcash.dev/docs
- group: docs
  title: ''
  type: APIReference
  url: https://github.com/merit-systems/sdk/blob/master/api.md
- group: start
  title: ''
  type: GettingStarted
  url: https://agentcash.dev/install
- group: company
  title: ''
  type: Blog
  url: https://merit.systems/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/merit-systems
- group: operate
  title: ''
  type: Support
  url: https://github.com/merit-systems/help-us
- group: start
  title: ''
  type: SignUp
  url: https://agentcash.dev/onboard
- group: commercial
  title: ''
  type: TermsOfService
  url: https://merit.systems/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://merit.systems/privacy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/merit-systems-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/merit-systems-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/merit-systems-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/merit-systems-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/merit-systems-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/merit-systems-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/merit-systems-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/merit-systems-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/merit-systems-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/merit-systems-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/merit-systems-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/merit-systems-conformance.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/merit-systems-agentic-access.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/merit-systems-sandbox.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/merit-systems-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://github.com/merit-systems/agentcash-router/blob/main/SECURITY.md
- group: other
  title: ''
  type: Overlay
  url: overlays/merit-systems-agentcash-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/merit-systems-merit-api-overlay.yaml
created: '2026-07-17'
description: 'Merit Systems builds the infrastructure for open agentic commerce — the discovery and payment rails that let AI agents find and pay for the APIs, data, and services they need. Merit originated the "open agentic commerce" framing and the x402 ecosystem index (x402scan), and ships a developer stack for pay-per-call APIs: AgentCash (an MCP server, CLI, and USDC wallet that lets any agent call payment-protected APIs over x402/MPP micropayments), @agentcash/router (a framework for building x402/MPP-compatible endpoints), the Echo "User Pays" AI SDK, and the Merit Terminal financial stack for funding open-source contributors and repositories. Backed by a $10M seed round led by a16z and Blockchain Capital.'
image: https://agentcash.dev/logo-light-striped.svg
layout: provider
mcp_servers:
- description: ''
  name: merit-systems-mcp.yml
  slug: merit-systems-mcpyml
modified: '2026-07-20'
name: Merit Systems
nav: Providers
network: true
overview: 'Merit Systems publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Balances API, Invite Codes API, Organizations API, and 3 more. Tagged areas include Company, Agentic Commerce, Payments, x402, and Micropayments.


  Merit Systems'' developer surface includes documentation, API reference, getting-started guide, engineering blog, support, signup flow, CLI, and 23 more developer resources.'
random_paper: 106
score:
  band: developing
  composite: 51.6
  delta: -1.4
  facets:
    commercial_clarity: 34.2
    contract_quality: 57.1
    developer_ergonomics: 87.0
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 31.6
  previous_composite: 53.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 48.4
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/merit-systems/refs/heads/main/screenshots/merit-systems-2026-08-07T172603.png
security:
- kind: authentication
  name: Merit Systems Authentication
  slug: merit-systems-authentication
  summary_line: apiKey/x402/mpp/siwx · 4 schemes
- kind: vulnerability-disclosure
  name: Merit Systems Vulnerability Disclosure
  slug: merit-systems-vulnerability-disclosure
  summary_line: contact published
slug: merit-systems
tags:
- Company
- Agentic Commerce
- Payments
- x402
- Micropayments
- Model Context Protocol
- Stablecoins
- API Discovery
- Open Source
- Developer Tools
website: https://merit.systems
---
