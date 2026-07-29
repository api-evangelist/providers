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
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: verified
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 66.9
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Treasuryspring Agentic Access
  operation_count: 31
  slug: treasuryspring-agentic-access
  summary_line: 31 operations · 10 acting
api_count: 13
apis:
- description: Get Calendar information
  name: TreasurySpring Calendar API
  slug: treasuryspring-calendar-api
- description: Get information about Cells
  name: TreasurySpring Cells API
  slug: treasuryspring-cells-api
- description: Get information about Entities
  name: TreasurySpring Entities API
  slug: treasuryspring-entities-api
- description: Server-managed cursors for stateless event stream consumers. In most cases, checkpoints are not needed. If your system can persist data locally (e.g. in a database, file, or key-value store), store th
  name: TreasurySpring Event Checkpoints API
  slug: treasuryspring-event-checkpoints-api
- description: Stream of normalised events for integration and reconciliation
  name: TreasurySpring Events API
  slug: treasuryspring-events-api
- description: Check the status of the API
  name: TreasurySpring Healthcheck API
  slug: treasuryspring-healthcheck-api
- description: Get information about holdings. For how subscriptions become holdings and how holdings move through their lifecycle, see the FTF Lifecycle section.
  name: TreasurySpring Holdings API
  slug: treasuryspring-holdings-api
- description: Get information about Indications
  name: TreasurySpring Indications API
  slug: treasuryspring-indications-api
- description: OAuth 2.0 endpoint to exchange your Client Credentials for a token. This token can then be used to access the API.
  name: TreasurySpring OAuth API
  slug: treasuryspring-oauth-api
- description: Get information about Obligors
  name: TreasurySpring Obligor Exposure API
  slug: treasuryspring-obligor-exposure-api
- description: FTF Subscriptions
  name: TreasurySpring Subscriptions API
  slug: treasuryspring-subscriptions-api
- description: Get information about Pending Tasks
  name: TreasurySpring Tasks API
  slug: treasuryspring-tasks-api
- description: Integrate with webhooks to receive notifications
  name: TreasurySpring Webhooks API
  slug: treasuryspring-webhooks-api
artifact_total: 18
asyncapis:
- description: ''
  name: Treasuryspring Events Webhooks
  slug: treasuryspring-events-webhooks
common:
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/treasuryspring-openapi-original.json
- group: auth
  title: ''
  type: Authentication
  url: authentication/treasuryspring-authentication.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/treasuryspring-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/treasuryspring-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/treasuryspring-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/treasuryspring-openapi-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/treasuryspring-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/treasuryspring-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/treasuryspring-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.treasuryspring.com/
- group: design
  title: ''
  type: Conventions
  url: conventions/treasuryspring-conventions.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/treasuryspring-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/treasuryspring-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/treasuryspring-events-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/treasuryspring-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/treasuryspring-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.treasuryspring.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.treasuryspring.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.treasuryspring.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.treasuryspring.com/
- group: company
  title: ''
  type: Blog
  url: https://treasuryspring.com/insights
- group: start
  title: ''
  type: SignUp
  url: https://app.treasuryspring.com/auth/login
- group: start
  title: ''
  type: Login
  url: https://app.treasuryspring.com/auth/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://treasuryspring.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://treasuryspring.com/privacy-policy
- group: operate
  title: ''
  type: Support
  url: mailto:api-support@treasuryspring.com
created: '2026-07-17'
description: TreasurySpring is a digital platform for institutional cash management that helps organisations holding large excess cash balances minimise risk, maximise return and optimise time by diversifying across secure counterparties via standardised Fixed Term Funds (FTFs). Its Public API (OpenAPI 3.1) gives an authorised user programmatic access to their entities, fund cells, obligor exposures, indications, subscriptions, holdings, tasks and a normalised event stream — the full FTF lifecycle from subscription to live holding — with OAuth 2.0 auth, offset and cursor pagination, webhooks, and a published, read-only Model Context Protocol (MCP) server for AI agents.
image: https://treasuryspring.com/hubfs/cropped-TS_Icon_Master_01-32x32.png
layout: provider
mcp_servers:
- description: ''
  name: treasuryspring-mcp.yml
  slug: treasuryspring-mcpyml
modified: '2026-07-21'
name: TreasurySpring
nav: Providers
network: true
overview: 'TreasurySpring publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Calendar API, Cells API, Entities API, and 10 more. Tagged areas include Company, Fintech, Cash Management, Treasury, and Investments.


  The TreasurySpring catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  TreasurySpring''s developer surface includes authentication, sandbox, getting-started guide, engineering blog, signup flow, support, and 21 more developer resources.'
random_paper: 53
score:
  band: developing
  composite: 47.8
  delta: -2.9
  facets:
    commercial_clarity: 34.2
    contract_quality: 72.1
    developer_ergonomics: 53.8
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 23.7
  previous_composite: 50.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 39.1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Treasuryspring Authentication
  slug: treasuryspring-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Treasuryspring Domain Security
  slug: treasuryspring-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: treasuryspring
tags:
- Company
- Fintech
- Cash Management
- Treasury
- Investments
- Financial Services
- Fixed Term Funds
- Payments
- MCP
website: https://www.treasuryspring.com/
---
