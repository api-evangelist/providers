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
    agentic_access: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    openapi_examples: verified
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 57.4
  scored_at: '2026-08-19'
api_count: 11
apis:
- description: The Admin API from Insforge — 54 operation(s) for admin.
  name: Insforge Admin API
  slug: insforge-admin-api
- description: Configure realtime channel patterns, webhooks, and availability.
  name: Insforge Channels API
  slug: insforge-channels-api
- description: The Client API from Insforge — 35 operation(s) for client.
  name: Insforge Client API
  slug: insforge-client-api
- description: Manage realtime retention settings.
  name: Insforge Configuration API
  slug: insforge-configuration-api
- description: Inspect realtime message history and delivery stats.
  name: Insforge Messages API
  slug: insforge-messages-api
- description: Provider webhook ingestion routes
  name: Insforge Payment Webhooks API
  slug: insforge-payment-webhooks-api
- description: Manage helper endpoints for realtime RLS examples.
  name: Insforge Permissions API
  slug: insforge-permissions-api
- description: Razorpay Orders, Subscriptions, catalog, manual webhook setup, sync, customer, and transaction routes
  name: Insforge Razorpay Payments API
  slug: insforge-razorpay-payments-api
- description: The S3 Access Keys API from Insforge — 3 operation(s) for s3 access keys.
  name: Insforge S3 Access Keys API
  slug: insforge-s3-access-keys-api
- description: The S3 Protocol API from Insforge — 1 operation(s) for s3 protocol.
  name: Insforge S3 Protocol API
  slug: insforge-s3-protocol-api
- description: Stripe Checkout, Billing Portal, catalog, sync, customer, subscription, and transaction routes
  name: Insforge Stripe Payments API
  slug: insforge-stripe-payments-api
artifact_total: 28
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Insforge AI Admin API
  slug: open-insforge-admin-api
- collection_type: open
  name: Insforge AI Admin Channels API
  slug: open-insforge-channels-api
- collection_type: open
  name: Insforge AI Admin Client API
  slug: open-insforge-client-api
- collection_type: open
  name: Insforge AI Admin Configuration API
  slug: open-insforge-configuration-api
- collection_type: open
  name: Insforge AI Admin Messages API
  slug: open-insforge-messages-api
- collection_type: open
  name: Insforge AI Admin Payment Webhooks API
  slug: open-insforge-payment-webhooks-api
- collection_type: open
  name: Insforge AI Admin Permissions API
  slug: open-insforge-permissions-api
- collection_type: open
  name: Insforge AI Admin Razorpay Payments API
  slug: open-insforge-razorpay-payments-api
- collection_type: open
  name: Insforge AI Admin S3 Access Keys API
  slug: open-insforge-s3-access-keys-api
- collection_type: open
  name: Insforge AI Admin S3 Protocol API
  slug: open-insforge-s3-protocol-api
- collection_type: open
  name: Insforge AI Admin Stripe Payments API
  slug: open-insforge-stripe-payments-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/insforge-auth-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://insforge.dev
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.insforge.dev
- group: docs
  title: ''
  type: Documentation
  url: https://docs.insforge.dev
- group: docs
  title: ''
  type: APIReference
  url: https://docs.insforge.dev/api-reference/admin/admin-login
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.insforge.dev/quickstart
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/InsForge
- group: company
  title: ''
  type: Blog
  url: https://insforge.dev/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://insforge.dev/pricing
- group: start
  title: ''
  type: SignUp
  url: https://insforge.dev/dashboard
- group: commercial
  title: ''
  type: TermsOfService
  url: https://insforge.dev/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://insforge.dev/privacy
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/DvBtaEc9Jz
- group: operate
  title: ''
  type: ChangeLog
  url: https://insforge.dev/changelogs
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/insforge-changelog.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/insforge-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/insforge-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/insforge-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/insforge-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/insforge-cli.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/insforge-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/insforge-security.txt
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/insforge-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/insforge-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/insforge-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/insforge-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/insforge-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/insforge-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/insforge-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/insforge-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/insforge-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/insforge-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: well-known/insforge-security.txt
created: '2026-07-17'
description: InsForge is an open-source (Apache-2.0), agent-native cloud infrastructure platform built so that AI coding agents can provision and operate an entire backend end to end through a CLI and packaged agent skills instead of a human clicking through a dashboard. A single project bundles a Postgres database with schema management and row-level security, authentication (users, sessions, OAuth, JWT), S3-compatible object storage, Deno-based edge functions with cron, a unified AI model gateway, realtime subscriptions and webhooks, long-lived custom compute, frontend hosting via Vercel, transactional email, and payments via Stripe and Razorpay. The REST API is documented as fourteen OpenAPI 3.0 service specifications and is driven by an official TypeScript SDK, CLI, and hosted MCP server. InsForge is a Y Combinator company.
image: https://insforge.dev/logo.png
layout: provider
mcp_servers:
- description: ''
  name: insforge-mcp.yml
  slug: insforge-mcpyml
modified: '2026-07-19'
name: Insforge
nav: Providers
network: true
overview: 'Insforge publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Admin API, Channels API, Client API, and 8 more. Tagged areas include Company, Backend as a Service, Agent Native, Cloud Infrastructure, and Database.


  Insforge''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, support, and 27 more developer resources.'
random_paper: 0
scopes:
- name: Insforge Scopes
  scope_count: 11
  slug: insforge-scopes
  summary_line: 11 scopes · authorizationCode/deviceCode
score:
  band: strong
  composite: 56.8
  delta: 2.7
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 16.7
    contract_quality: 49.5
    developer_ergonomics: 78.6
    discoverability: 92.6
    governance: 16.7
    operational_transparency: 28.9
  previous_composite: 54.1
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 64.1
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/insforge/refs/heads/main/screenshots/insforge-2026-07-25T222527.png
security:
- kind: authentication
  name: Insforge Authentication
  slug: insforge-authentication
  summary_line: apiKey/http/oauth2 · 7 schemes
- kind: domain-security
  name: Insforge Domain Security
  slug: insforge-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Insforge Vulnerability Disclosure
  slug: insforge-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: insforge
tags:
- Company
- Backend as a Service
- Agent Native
- Cloud Infrastructure
- Database
- Authentication
- Storage
- Serverless
- Edge Functions
- AI Gateway
- Payments
- Realtime
- Open Source
- Y Combinator
website: https://insforge.dev
---
