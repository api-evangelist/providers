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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 60.1
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 18
  human_in_the_loop: 3
  name: Notyfi Agentic Access
  operation_count: 26
  slug: notyfi-agentic-access
  summary_line: 26 operations · 18 acting · 3 human-in-the-loop
api_count: 5
apis:
- description: The account API from Notyfi — 3 operation(s) for account.
  name: Notyfi account API
  slug: notyfi-account-api
- description: The billing API from Notyfi — 3 operation(s) for billing.
  name: Notyfi billing API
  slug: notyfi-billing-api
- description: The keys API from Notyfi — 2 operation(s) for keys.
  name: Notyfi keys API
  slug: notyfi-keys-api
- description: The trackers API from Notyfi — 6 operation(s) for trackers.
  name: Notyfi trackers API
  slug: notyfi-trackers-api
- description: The webhooks API from Notyfi — 4 operation(s) for webhooks.
  name: Notyfi webhooks API
  slug: notyfi-webhooks-api
artifact_total: 16
asyncapis:
- description: ''
  name: Notyfi Webhooks
  slug: notyfi-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Notyfi account API
  slug: open-notyfi-account-api
- collection_type: open
  name: Notyfi account billing API
  slug: open-notyfi-billing-api
- collection_type: open
  name: Notyfi account keys API
  slug: open-notyfi-keys-api
- collection_type: open
  name: Notyfi account trackers API
  slug: open-notyfi-trackers-api
- collection_type: open
  name: Notyfi account webhooks API
  slug: open-notyfi-webhooks-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/notyfi-openapi-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://notyfi.com/docs
- group: docs
  title: ''
  type: Documentation
  url: https://notyfi.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://notyfi.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://notyfi.com/#pricing
- group: start
  title: ''
  type: SignUp
  url: https://notyfi.com/dashboard/#signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://notyfi.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://notyfi.com/privacy
- group: agent
  title: ''
  type: MCPServer
  url: mcp/notyfi-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/notyfi-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/notyfi-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/notyfi-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/notyfi-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/notyfi-lifecycle.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/notyfi-webhooks.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/notyfi-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/notyfi-data-model.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/notyfi-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/notyfi-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/notyfi-domain-security.yml
created: '2026-07-17'
description: 'Notyfi is a natural-language monitoring and notification service built by Perceptron ML (Y Combinator). Describe what to watch in one sentence -- new lawsuits, layoffs, price drops, listings, RFPs, breaking news -- and Notyfi watches the news, filings, databases, and the open web for it, delivering deduplicated canonical events instantly, hourly, daily, or weekly by email, on a live dashboard, or into agents and workflows via a REST API and a hosted MCP server. The API exposes persistent trackers, their event feeds, HMAC-signed outgoing webhooks, API-key management, account, and Stripe-backed billing. Authenticate with a Notyfi API key (Authorization: Bearer notyfi_mk_... or X-Api-Key).'
image: https://notyfi.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: notyfi-mcp.yml
  slug: notyfi-mcpyml
modified: '2026-07-20'
name: Notyfi
nav: Providers
network: true
overview: 'Notyfi publishes 5 APIs on the [APIs.io](https://apis.io/) network, including account API, billing API, keys API, and 2 more. Tagged areas include Company, Notifications, Monitoring, Webhooks, and Real Time.


  The Notyfi catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Notyfi''s developer surface includes documentation, API reference, pricing, signup flow, authentication, and 16 more developer resources.'
random_paper: 69
score:
  band: developing
  composite: 44.8
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 65.1
    developer_ergonomics: 45.1
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 7.9
  previous_composite: 44.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/notyfi/refs/heads/main/screenshots/notyfi-2026-08-07T185550.png
security:
- kind: authentication
  name: Notyfi Authentication
  slug: notyfi-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Notyfi Domain Security
  slug: notyfi-domain-security
  summary_line: TLSv1.3 · DMARC
slug: notyfi
tags:
- Company
- Notifications
- Monitoring
- Webhooks
- Real Time
- Agents
- MCP
- Alerts
website: https://notyfi.com/docs
---
