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
  band: agent-native
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
    event_surface_described: true
    idempotency: verified
    mcp_server: verified
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 45.9
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Treasuryspring Agentic Access
  operation_count: 31
  slug: treasuryspring-agentic-access
  summary_line: 31 operations · 10 acting
api_count: 1
apis:
- baseURL: https://api.treasuryspring.com/api/v1
  baseurl_source: declared
  description: Get Calendar information
  name: TreasurySpring Calendar API
  slug: treasuryspring-calendar-api
- baseURL: https://api.treasuryspring.com/api/v1
  baseurl_source: declared
  description: Get information about Cells
  name: TreasurySpring Cells API
  slug: treasuryspring-cells-api
- baseURL: https://api.treasuryspring.com/api/v1
  baseurl_source: declared
  description: Get information about Entities
  name: TreasurySpring Entities API
  slug: treasuryspring-entities-api
- baseURL: https://api.treasuryspring.com/api/v1
  baseurl_source: declared
  description: Server-managed cursors for stateless event stream consumers. In most cases, checkpoints are not needed. If your system can persist data locally (e.g. in a database, file, or key-value store), store th
  name: TreasurySpring Event Checkpoints API
  slug: treasuryspring-event-checkpoints-api
- baseURL: https://api.treasuryspring.com/api/v1
  baseurl_source: declared
  description: Stream of normalised events for integration and reconciliation
  name: TreasurySpring Events API
  slug: treasuryspring-events-api
- baseURL: https://api.treasuryspring.com/api/v1
  baseurl_source: declared
  description: Check the status of the API
  name: TreasurySpring Healthcheck API
  slug: treasuryspring-healthcheck-api
- baseURL: https://api.treasuryspring.com/api/v1
  baseurl_source: declared
  description: Get information about holdings. For how subscriptions become holdings and how holdings move through their lifecycle, see the FTF Lifecycle section.
  name: TreasurySpring Holdings API
  slug: treasuryspring-holdings-api
- baseURL: https://api.treasuryspring.com/api/v1
  baseurl_source: declared
  description: Get information about Indications
  name: TreasurySpring Indications API
  slug: treasuryspring-indications-api
- baseURL: https://api.treasuryspring.com/api/v1
  baseurl_source: declared
  description: OAuth 2.0 endpoint to exchange your Client Credentials for a token. This token can then be used to access the API.
  name: TreasurySpring OAuth API
  slug: treasuryspring-oauth-api
- baseURL: https://api.treasuryspring.com/api/v1
  baseurl_source: declared
  description: Get information about Obligors
  name: TreasurySpring Obligor Exposure API
  slug: treasuryspring-obligor-exposure-api
- baseURL: https://api.treasuryspring.com/api/v1
  baseurl_source: declared
  description: FTF Subscriptions
  name: TreasurySpring Subscriptions API
  slug: treasuryspring-subscriptions-api
- baseURL: https://api.treasuryspring.com/api/v1
  baseurl_source: declared
  description: Get information about Pending Tasks
  name: TreasurySpring Tasks API
  slug: treasuryspring-tasks-api
- baseURL: https://api.treasuryspring.com/api/v1
  baseurl_source: declared
  description: Integrate with webhooks to receive notifications
  name: TreasurySpring Webhooks API
  slug: treasuryspring-webhooks-api
artifact_total: 32
asyncapis:
- description: ''
  name: Treasuryspring Events Webhooks
  slug: treasuryspring-events-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: TreasurySpring Public Calendar API
  slug: open-treasuryspring-calendar-api
- collection_type: open
  name: TreasurySpring Public Calendar Cells API
  slug: open-treasuryspring-cells-api
- collection_type: open
  name: TreasurySpring Public Calendar Entities API
  slug: open-treasuryspring-entities-api
- collection_type: open
  name: TreasurySpring Public Calendar Event Checkpoints API
  slug: open-treasuryspring-event-checkpoints-api
- collection_type: open
  name: TreasurySpring Public Calendar Events API
  slug: open-treasuryspring-events-api
- collection_type: open
  name: TreasurySpring Public Calendar Healthcheck API
  slug: open-treasuryspring-healthcheck-api
- collection_type: open
  name: TreasurySpring Public Calendar Holdings API
  slug: open-treasuryspring-holdings-api
- collection_type: open
  name: TreasurySpring Public Calendar Indications API
  slug: open-treasuryspring-indications-api
- collection_type: open
  name: TreasurySpring Public Calendar OAuth API
  slug: open-treasuryspring-oauth-api
- collection_type: open
  name: TreasurySpring Public Calendar Obligor Exposure API
  slug: open-treasuryspring-obligor-exposure-api
- collection_type: open
  name: TreasurySpring Public Calendar Subscriptions API
  slug: open-treasuryspring-subscriptions-api
- collection_type: open
  name: TreasurySpring Public Calendar Tasks API
  slug: open-treasuryspring-tasks-api
- collection_type: open
  name: TreasurySpring Public Calendar Webhooks API
  slug: open-treasuryspring-webhooks-api
common:
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/treasuryspring-openapi-original.json
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
- description: TreasurySpring's MCP server lets AI agents (Claude, ChatGPT, Cursor and other MCP-compatible clients) access an authorised user's read-only investment data via the Model Context Protocol. It is a thin
  name: TreasurySpring MCP Server
  slug: treasuryspring-mcp-server
modified: '2026-07-21'
name: TreasurySpring
nav: Providers
network: true
overview: 'TreasurySpring publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Calendar API, Cells API, Entities API, and 10 more. Tagged areas include Company, Fintech, Cash Management, Treasury, and Investments.


  The TreasurySpring catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  TreasurySpring''s developer surface includes authentication, sandbox, getting-started guide, engineering blog, signup flow, support, and 21 more developer resources.'
random_paper: 0
score:
  band: developing
  composite: 43.9
  coverage:
    artifact_dirs: 19
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 4.5
    contract_quality: 65.9
    developer_ergonomics: 58.9
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 7.9
  previous_composite: 43.9
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
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/treasuryspring/refs/heads/main/screenshots/treasuryspring-2026-08-17T082431.png
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
- Financial-Services
- Fixed Term Funds
- Payments
- MCP
website: https://www.treasuryspring.com/
---
