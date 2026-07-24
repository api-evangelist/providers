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
    agent_skills: true
    agentic_access: true
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 77.9
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 38
  human_in_the_loop: 1
  name: Orum Agentic Access
  operation_count: 71
  slug: orum-agentic-access
  summary_line: 71 operations · 38 acting · 1 human-in-the-loop
api_count: 17
apis:
- description: The Authentication API from Orum — 1 operation(s) for authentication.
  name: Orum Authentication API
  slug: orum-authentication-api
- description: The Balance API from Orum — 3 operation(s) for balance.
  name: Orum Balance API
  slug: orum-balance-api
- description: The Book Transfers API from Orum — 2 operation(s) for book transfers.
  name: Orum Book Transfers API
  slug: orum-book-transfers-api
- description: The Businesses API from Orum — 2 operation(s) for businesses.
  name: Orum Businesses API
  slug: orum-businesses-api
- description: The Cards API from Orum — 2 operation(s) for cards.
  name: Orum Cards API
  slug: orum-cards-api
- description: The Configure webhooks API from Orum — 2 operation(s) for configure webhooks.
  name: Orum Configure webhooks API
  slug: orum-configure-webhooks-api
- description: The Eligibility API from Orum — 1 operation(s) for eligibility.
  name: Orum Eligibility API
  slug: orum-eligibility-api
- description: The External Accounts API from Orum — 4 operation(s) for external accounts.
  name: Orum External Accounts API
  slug: orum-external-accounts-api
- description: The Persons API from Orum — 2 operation(s) for persons.
  name: Orum Persons API
  slug: orum-persons-api
- description: The Reports API from Orum — 5 operation(s) for reports.
  name: Orum Reports API
  slug: orum-reports-api
- description: The Schedules API from Orum — 3 operation(s) for schedules.
  name: Orum Schedules API
  slug: orum-schedules-api
- description: The Secure webhooks API from Orum — 1 operation(s) for secure webhooks.
  name: Orum Secure webhooks API
  slug: orum-secure-webhooks-api
- description: The Subledgers API from Orum — 2 operation(s) for subledgers.
  name: Orum Subledgers API
  slug: orum-subledgers-api
- description: The Transfer Groups API from Orum — 2 operation(s) for transfer groups.
  name: Orum Transfer Groups API
  slug: orum-transfer-groups-api
- description: The Transfers API from Orum — 4 operation(s) for transfers.
  name: Orum Transfers API
  slug: orum-transfers-api
- description: The Trigger webhooks API from Orum — 1 operation(s) for trigger webhooks.
  name: Orum Trigger webhooks API
  slug: orum-trigger-webhooks-api
- description: The Verify API from Orum — 4 operation(s) for verify.
  name: Orum Verify API
  slug: orum-verify-api
artifact_total: 24
asyncapis:
- description: ''
  name: Orum Webhooks
  slug: orum-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://orum.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.orum.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.orum.io
- group: docs
  title: ''
  type: APIReference
  url: https://docs.orum.io/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.orum.io/guides/welcome
- group: operate
  title: ''
  type: Support
  url: mailto:service@orum.io
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/orum-io
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/orum-openapi-original.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/orum-openapi-overlay.yaml
- group: auth
  title: ''
  type: Authentication
  url: authentication/orum-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/orum-scopes.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/orum-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/orum-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/orum-agentic-access.yml
- group: build
  title: ''
  type: Packages
  url: packages/orum-packages.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/orum-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/orum-data-model.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/orum-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/orum-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/orum-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/orum-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/orum-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/orum-sandbox.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://docs.orum.io/guides/deliver/rate-limits
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/orum-webhooks.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/orum-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/orum-trust-center.yml
created: '2026-07-17'
description: Orum is a payments infrastructure company that lets businesses move money and verify bank accounts through a single unified API. Its Deliver product provides "Direct to Fed" money movement across FedNow, RTP, Same Day ACH, ACH, Wires, and Visa Direct; Verify instantly confirms bank account status, ownership, and control; and Monitor is a portal for orchestrating and reconciling payment operations in real time. The REST API uses OAuth 2.0 client-credentials, offers signed webhooks for money-movement events, and ships a published OpenAPI spec and an OpenAPI-generated MCP server. Orum is backed by Accel, Bain Capital Ventures, and Craft Ventures.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/orum.png
layout: provider
mcp_servers:
- description: ''
  name: orum-mcp.yml
  slug: orum-mcpyml
modified: '2026-07-20'
name: Orum
nav: Providers
network: true
overview: 'Orum publishes 17 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Balance API, Book Transfers API, and 14 more. Tagged areas include Company, Payments, Fintech, Banking, and Instant Payments.


  The Orum catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Orum''s developer surface includes documentation, API reference, getting-started guide, support, authentication, changelog, sandbox, and 21 more developer resources.'
random_paper: 43
scopes:
- name: Orum Scopes
  scope_count: 29
  slug: orum-scopes
  summary_line: 29 scopes · clientCredentials
score:
  band: developing
  composite: 50.5
  delta: 3.3
  facets:
    commercial_clarity: 7.9
    contract_quality: 65.9
    developer_ergonomics: 71.7
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 47.2
  regulatory:
    applies: true
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 69.6
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Orum Authentication
  slug: orum-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Orum Domain Security
  slug: orum-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: trust-center
  name: Orum Trust Center
  slug: orum-trust-center
  summary_line: trust center published
slug: orum
tags:
- Company
- Payments
- Fintech
- Banking
- Instant Payments
- ACH
- Money Movement
- Bank Account Verification
website: https://orum.io/
---
