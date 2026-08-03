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
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 56.1
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Lootrush Agentic Access
  operation_count: 5
  slug: lootrush-agentic-access
  summary_line: 5 operations · 2 acting
api_count: 4
apis:
- description: The Connect API from LootRush — 1 operation(s) for connect.
  name: LootRush Connect API
  slug: lootrush-connect-api
- description: The History API from LootRush — 1 operation(s) for history.
  name: LootRush History API
  slug: lootrush-history-api
- description: The MCP API from LootRush — 1 operation(s) for mcp.
  name: LootRush MCP API
  slug: lootrush-mcp-api
- description: The Withdrawals API from LootRush — 2 operation(s) for withdrawals.
  name: LootRush Withdrawals API
  slug: lootrush-withdrawals-api
artifact_total: 9
common:
- group: company
  title: ''
  type: Website
  url: https://www.lootrush.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.lootrush.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.lootrush.com/api-reference/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.lootrush.com/index.md
- group: operate
  title: ''
  type: Support
  url: mailto:support@lootrush.com
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/lootrush-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/lootrush-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/lootrush-authentication.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/lootrush-agentic-access.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/lootrush-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/lootrush-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/lootrush-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/lootrush-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/lootrush-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/lootrush-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lootrush-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/lootrush-openapi-overlay.yaml
created: '2026-07-17'
description: 'LootRush is a gaming and crypto platform (backed by Paradigm) that publishes a Partner API for marketplace integrations: initiating and tracking on-chain cryptocurrency withdrawals, querying a user''s transaction and activity history, and OAuth-style consented access to user data via a Connect API. LootRush also runs a published, read-only Model Context Protocol (MCP) server at mcp.lootrush.com that lets an AI assistant read the key-holder''s own balance, cards, card transactions, and account history — every call scoped to the API key''s user. Authentication is per-user bearer tokens (Withdraw, History, MCP) and integration API keys (Connect).'
image: https://www.lootrush.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: lootrush-mcp.yml
  slug: lootrush-mcpyml
modified: '2026-07-20'
name: LootRush
nav: Providers
network: true
overview: 'LootRush publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Connect API, History API, MCP API, and 1 more. Tagged areas include Company, Gaming, Crypto, Cryptocurrency, and Payments.


  LootRush''s developer surface includes documentation, API reference, getting-started guide, support, authentication, and 13 more developer resources.'
random_paper: 41
rate_limits:
- limit_count: 2
  name: Lootrush Rate Limits
  slug: lootrush-rate-limits
score:
  band: thin
  composite: 36.8
  delta: 2.3
  facets:
    commercial_clarity: 0.0
    contract_quality: 64.0
    developer_ergonomics: 51.6
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 21.1
  previous_composite: 34.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 26.6
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lootrush/refs/heads/main/screenshots/lootrush-2026-07-25T225545.png
security:
- kind: authentication
  name: Lootrush Authentication
  slug: lootrush-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Lootrush Domain Security
  slug: lootrush-domain-security
  summary_line: TLSv1.3 · DMARC
slug: lootrush
tags:
- Company
- Gaming
- Crypto
- Cryptocurrency
- Payments
- Withdrawals
- MCP
- API
website: https://www.lootrush.com
---
