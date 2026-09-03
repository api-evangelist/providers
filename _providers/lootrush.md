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
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Lootrush Agentic Access
  operation_count: 5
  slug: lootrush-agentic-access
  summary_line: 5 operations · 2 acting
api_count: 1
apis:
- baseURL: https://third-party.lootrush.com
  baseurl_source: declared
  description: The Connect API from LootRush — 1 operation(s) for connect.
  name: LootRush Connect API
  slug: lootrush-connect-api
- baseURL: https://third-party.lootrush.com
  baseurl_source: declared
  description: The History API from LootRush — 1 operation(s) for history.
  name: LootRush History API
  slug: lootrush-history-api
- baseURL: https://third-party.lootrush.com
  baseurl_source: declared
  description: The MCP API from LootRush — 1 operation(s) for mcp.
  name: LootRush MCP API
  slug: lootrush-mcp-api
- baseURL: https://third-party.lootrush.com
  baseurl_source: declared
  description: The Withdrawals API from LootRush — 2 operation(s) for withdrawals.
  name: LootRush Withdrawals API
  slug: lootrush-withdrawals-api
artifact_total: 14
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: LootRush Partner Connect API
  slug: open-lootrush-connect-api
- collection_type: open
  name: LootRush Partner Connect History API
  slug: open-lootrush-history-api
- collection_type: open
  name: LootRush Partner Connect MCP API
  slug: open-lootrush-mcp-api
- collection_type: open
  name: LootRush Partner Connect Withdrawals API
  slug: open-lootrush-withdrawals-api
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
layout: provider
mcp_servers:
- description: Streamable HTTP (JSON-RPC 2.0), stateless — one request, one response. POST only.
  name: LootRush MCP Server
  slug: lootrush-mcp-server
modified: '2026-07-20'
name: LootRush
nav: Providers
network: true
overview: 'LootRush publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Connect API, History API, MCP API, and 1 more. Tagged areas include Company, Gaming, Crypto, Cryptocurrency, and Payments.


  LootRush''s developer surface includes documentation, API reference, getting-started guide, support, authentication, and 13 more developer resources.'
random_paper: 14
rate_limits:
- limit_count: 2
  name: Lootrush Rate Limits
  slug: lootrush-rate-limits
score:
  band: thin
  composite: 33.0
  coverage:
    artifact_dirs: 16
    catalog_gap: 72.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 56.1
    developer_ergonomics: 47.0
    discoverability: 72.2
    governance: 4.5
    operational_transparency: 21.1
  previous_composite: 33.0
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
  schema_version: 0.18.0
  scored_at: '2026-09-02'
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
website: https://www.lootrush.com
---
