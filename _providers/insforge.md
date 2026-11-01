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
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 55.0
  scored_at: '2026-10-31'
api_count: 14
apis:
- baseURL: https://api.insforge.dev
  baseurl_source: declared
  description: The Admin API from Insforge — 54 operation(s) for admin.
  name: Insforge Admin API
  slug: insforge-admin-api
- baseURL: https://api.insforge.dev
  baseurl_source: declared
  description: Configure realtime channel patterns, webhooks, and availability.
  name: Insforge Channels API
  slug: insforge-channels-api
- baseURL: https://api.insforge.dev
  baseurl_source: declared
  description: The Client API from Insforge — 35 operation(s) for client.
  name: Insforge Client API
  slug: insforge-client-api
- baseURL: https://api.insforge.dev
  baseurl_source: declared
  description: Manage realtime retention settings.
  name: Insforge Configuration API
  slug: insforge-configuration-api
- baseURL: https://api.insforge.dev
  baseurl_source: declared
  description: Inspect realtime message history and delivery stats.
  name: Insforge Messages API
  slug: insforge-messages-api
- baseURL: https://api.insforge.dev
  baseurl_source: declared
  description: Provider webhook ingestion routes
  name: Insforge Payment Webhooks API
  slug: insforge-payment-webhooks-api
- baseURL: https://api.insforge.dev
  baseurl_source: declared
  description: Manage helper endpoints for realtime RLS examples.
  name: Insforge Permissions API
  slug: insforge-permissions-api
- baseURL: https://api.insforge.dev
  baseurl_source: declared
  description: Razorpay Orders, Subscriptions, catalog, manual webhook setup, sync, customer, and transaction routes
  name: Insforge Razorpay Payments API
  slug: insforge-razorpay-payments-api
- baseURL: https://api.insforge.dev
  baseurl_source: declared
  description: The S3 Access Keys API from Insforge — 3 operation(s) for s3 access keys.
  name: Insforge S3 Access Keys API
  slug: insforge-s3-access-keys-api
- baseURL: https://api.insforge.dev
  baseurl_source: declared
  description: The S3 Protocol API from Insforge — 1 operation(s) for s3 protocol.
  name: Insforge S3 Protocol API
  slug: insforge-s3-protocol-api
- baseURL: https://api.insforge.dev
  baseurl_source: declared
  description: Stripe Checkout, Billing Portal, catalog, sync, customer, subscription, and transaction routes
  name: Insforge Stripe Payments API
  slug: insforge-stripe-payments-api
artifact_total: 31
collections:
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
- group: commercial
  href: https://artifacts.apis.io/insforge/plans/insforge-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/insforge-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/insforge/capabilities/insforge-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/insforge-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/insforge/overlays/insforge-auth-overlay.yaml
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
  href: https://artifacts.apis.io/insforge/changelog/insforge-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/insforge-changelog.yml
- group: agent
  href: https://artifacts.apis.io/insforge/mcp/insforge-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/insforge-mcp.yml
- group: agent
  href: https://artifacts.apis.io/insforge/llms/insforge-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/insforge-llms.txt
- group: build
  href: https://artifacts.apis.io/insforge/packages/insforge-packages.yml
  title: ''
  type: Packages
  url: packages/insforge-packages.yml
- group: build
  href: https://artifacts.apis.io/insforge/packages/insforge-packages.yml
  title: ''
  type: SDKs
  url: packages/insforge-packages.yml
- group: build
  href: https://artifacts.apis.io/insforge/cli/insforge-cli.yml
  title: ''
  type: CLI
  url: cli/insforge-cli.yml
- group: agent
  href: https://artifacts.apis.io/insforge/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/insforge/well-known/insforge-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/insforge-well-known.yml
- group: auth
  href: https://artifacts.apis.io/insforge/well-known/insforge-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/insforge-security.txt
- group: auth
  href: https://artifacts.apis.io/insforge/scopes/insforge-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/insforge-scopes.yml
- group: auth
  href: https://artifacts.apis.io/insforge/authentication/insforge-authentication.yml
  title: ''
  type: Authentication
  url: authentication/insforge-authentication.yml
- group: design
  href: https://artifacts.apis.io/insforge/conventions/insforge-conventions.yml
  title: ''
  type: Conventions
  url: conventions/insforge-conventions.yml
- group: design
  href: https://artifacts.apis.io/insforge/conventions/insforge-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/insforge-conventions.yml
- group: design
  href: https://artifacts.apis.io/insforge/errors/insforge-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/insforge-problem-types.yml
- group: design
  href: https://artifacts.apis.io/insforge/conformance/insforge-conformance.yml
  title: ''
  type: Conformance
  url: conformance/insforge-conformance.yml
- group: design
  href: https://artifacts.apis.io/insforge/lifecycle/insforge-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/insforge-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/insforge/data-model/insforge-data-model.yml
  title: ''
  type: DataModel
  url: data-model/insforge-data-model.yml
- group: auth
  href: https://artifacts.apis.io/insforge/security/insforge-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/insforge-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/insforge/security/insforge-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/insforge-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/insforge/well-known/insforge-security.txt
  title: ''
  type: Security
  url: well-known/insforge-security.txt
created: '2026-07-17'
description: InsForge is an open-source (Apache-2.0), agent-native cloud infrastructure platform built so that AI coding agents can provision and operate an entire backend end to end through a CLI and packaged agent skills instead of a human clicking through a dashboard. A single project bundles a Postgres database with schema management and row-level security, authentication (users, sessions, OAuth, JWT), S3-compatible object storage, Deno-based edge functions with cron, a unified AI model gateway, realtime subscriptions and webhooks, long-lived custom compute, frontend hosting via Vercel, transactional email, and payments via Stripe and Razorpay. The REST API is documented as fourteen OpenAPI 3.0 service specifications and is driven by an official TypeScript SDK, CLI, and hosted MCP server. InsForge is a Y Combinator company.
finops:
- has_sources: true
  method: derived
  name: Insforge Finops
  primary_unit: 2 vcpu 0.5 gb ram
  service_category: ''
  slug: insforge-finops
  template: false
image: https://insforge.dev/logo.png
layout: provider
mcp_servers:
- description: Official Model Context Protocol server for InsForge, exposing InsForge backend operations (database, auth, storage, functions, AI gateway, realtime, payments, deployments) as MCP tools for MCP-compati
  name: Insforge MCP Server
  slug: insforge
modified: '2026-07-19'
name: Insforge
nav: Providers
network: true
overview: 'Insforge publishes 11 API contracts indexed on the [APIs.io](https://apis.io/) network, including Admin API, Channels API, Client API, and 8 more. Tagged areas include Company, Backend-as-a-Service, Agent-Native, Cloud Infrastructure, and Database.


  Insforge''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, support, and 29 more developer resources.'
plans:
- name: Insforge Plans Pricing
  plan_count: 14
  slug: insforge-plans-pricing
- name: Insforge Price Estimates
  plan_count: 0
  slug: insforge-price-estimates
random_paper: 21
scopes:
- name: Insforge Scopes
  scope_count: 11
  slug: insforge-scopes
  summary_line: 11 scopes · authorizationCode/deviceCode
score:
  band: strong
  composite: 58.1
  coverage:
    artifact_dirs: 25
    catalog_earned: 55.0
    catalog_earned_first_party: 12.0
    catalog_gap: 60.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 7.9
  facets:
    access_clarity: 84.2
    contract_governance: 4.5
    contract_quality: 45.4
    developer_ergonomics: 78.6
    discoverability: 70.0
    operational_transparency: 31.6
  previous_composite: 50.2
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
    score: 36.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/insforge/insforge-2026-07-25T222527.png
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
skill_count: 1
skills:
- name: insforge-agent-guide
  slug: insforge-agent-guide
slug: insforge
tags:
- Company
- Backend-as-a-Service
- Agent-Native
- Cloud Infrastructure
- Database
- Authentication
- Storage
- Serverless
- Edge Functions
- AI Gateway
- Payments
- Real-Time
- Open Source
- Y Combinator
website: https://insforge.dev
---
