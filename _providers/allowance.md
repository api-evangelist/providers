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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: documented
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 68.9
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 3
  human_in_the_loop: 1
  name: Allowance Agentic Access
  operation_count: 7
  slug: allowance-agentic-access
  summary_line: 7 operations · 3 acting · 1 human-in-the-loop
api_count: 3
apis:
- description: The Mandates API from Allowance — 5 operation(s) for mandates.
  name: Allowance Mandates API
  slug: allowance-mandates-api
- description: The Pricing API from Allowance — 1 operation(s) for pricing.
  name: Allowance Pricing API
  slug: allowance-pricing-api
- description: The Status API from Allowance — 1 operation(s) for status.
  name: Allowance Status API
  slug: allowance-status-api
arazzos:
- description: ''
  name: _Index
  slug: _index
- description: Create a spending mandate, wait for the human owner to approve it, then request a single-use virtual card for a specific purchase against the active mandate.
  name: Approve a mandate and issue a virtual card
  slug: allowance-mandate-to-card
artifact_total: 11
asyncapis:
- description: ''
  name: Allowance Webhooks
  slug: allowance-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/allowance-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/allowance-agentic-access.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/allowance-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/allowance-authentication.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://useallowance.com/connect-agent
- group: docs
  title: ''
  type: Documentation
  url: https://useallowance.com/connect-agent
- group: docs
  title: ''
  type: APIReference
  url: https://useallowance.com/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://useallowance.com/connect-agent
- group: operate
  title: ''
  type: Support
  url: https://useallowance.com/support
- group: company
  title: ''
  type: Blog
  url: https://useallowance.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://useallowance.com/pricing.json
- group: start
  title: ''
  type: SignUp
  url: https://apps.apple.com/us/app/allowance-agent-wallet/id6762312262
- group: commercial
  title: ''
  type: TermsOfService
  url: https://useallowance.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://useallowance.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://useallowance.com/status.json
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/allowance-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/allowance-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/allowance-purchase.md
- group: build
  title: ''
  type: Packages
  url: packages/allowance-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/allowance-cli.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/allowance-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/allowance-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/allowance-problem-types.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/allowance-decline-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/allowance-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/allowance-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/allowance-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/allowance-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/allowance-webhooks.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/allowance-mandate-to-card.yml
created: '2026-07-17'
description: Allowance is a consumer trust layer for AI agent payments, backed by Y Combinator. It lets people give AI agents limited, revocable spending power without ever sharing a real credit card number. An agent proposes a spending mandate (a permission object with a budget, merchant and category restrictions, and a time limit); the human owner approves it from the Allowance iOS app; and Allowance then issues single-use virtual cards (PAN, expiry, CVV) that are amount-capped, merchant-locked, and short-lived so the agent can complete checkout autonomously within the approved rules. Allowance exposes a pre-launch OpenAPI 3.1 REST API, a hosted remote MCP server, a published agent SKILL.md, a CLI (PyPI and npm), plus ChatGPT and Claude connectors. The mandate model is designed as a natural precursor to the AP2 Agent Payments Protocol.
image: https://useallowance.com/assets/logo.png
layout: provider
mcp_servers:
- description: ''
  name: allowance-mcp.yml
  slug: allowance-mcpyml
modified: '2026-07-17'
name: Allowance
nav: Providers
network: true
overview: 'Allowance publishes 3 APIs on the [APIs.io](https://apis.io/) network: Mandates API, Pricing API, and Status API. Tagged areas include Company, Payments, Agentic Payments, AI Agents, and Virtual Cards.


  The Allowance catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Allowance''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 23 more developer resources.'
random_paper: 70
scopes:
- name: Allowance Scopes
  scope_count: 3
  slug: allowance-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: developing
  composite: 54.9
  delta: -3.1
  facets:
    commercial_clarity: 44.7
    contract_quality: 70.0
    developer_ergonomics: 73.9
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 23.7
  previous_composite: 58.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 54.7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/allowance/refs/heads/main/screenshots/allowance-2026-07-25T195707.png
security:
- kind: authentication
  name: Allowance Authentication
  slug: allowance-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Allowance Domain Security
  slug: allowance-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: allowance
tags:
- Company
- Payments
- Agentic Payments
- AI Agents
- Virtual Cards
- Fintech
- Model Context Protocol
- Consumer Trust
- Spending Controls
- AP2
website: https://useallowance.com/connect-agent
---
