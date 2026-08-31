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
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: documented
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.8
  scored_at: '2026-08-30'
api_count: 3
apis:
- description: User account, sign-in, sessions, settings
  name: LaserData Account API
  slug: laserdata-account-api
- description: Tenant API key management
  name: LaserData API Keys API
  slug: laserdata-api-keys-api
- description: Tenant audit log + user activity
  name: LaserData Audit API
  slug: laserdata-audit-api
- description: Pricing, billing reports, invoices
  name: LaserData Billing API
  slug: laserdata-billing-api
- description: BYOC cloud accounts
  name: LaserData Cloud Accounts API
  slug: laserdata-cloud-accounts-api
- description: Available clouds, regions, clusters, storages, tiers
  name: LaserData Clouds API
  slug: laserdata-clouds-api
- description: Deployment connectors
  name: LaserData Connectors API
  slug: laserdata-connectors-api
- description: Deployment lifecycle
  name: LaserData Deployments API
  slug: laserdata-deployments-api
- description: Tenant divisions
  name: LaserData Divisions API
  slug: laserdata-divisions-api
- description: Environments within a division
  name: LaserData Environments API
  slug: laserdata-environments-api
- description: Tenant invitations
  name: LaserData Invitations API
  slug: laserdata-invitations-api
- description: Tenant members
  name: LaserData Members API
  slug: laserdata-members-api
- description: Notification channels (email, slack, webhook)
  name: LaserData Notification Channels API
  slug: laserdata-notification-channels-api
- description: Channel subscriptions to notification types
  name: LaserData Notification Subscriptions API
  slug: laserdata-notification-subscriptions-api
- description: Notifications listing
  name: LaserData Notifications API
  slug: laserdata-notifications-api
- description: Payment methods (Stripe)
  name: LaserData Payments API
  slug: laserdata-payments-api
- description: Tenant roles and permissions
  name: LaserData Roles API
  slug: laserdata-roles-api
- description: Tenant CRUD, config, structure
  name: LaserData Tenants API
  slug: laserdata-tenants-api
artifact_total: 42
asyncapis:
- description: ''
  name: Laserdata Notifications Webhooks
  slug: laserdata-notifications-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: LaserData Cloud Audit Account API
  slug: open-laserdata-account-api
- collection_type: open
  name: LaserData Cloud Audit Account API Keys API
  slug: open-laserdata-api-keys-api
- collection_type: open
  name: LaserData Cloud Account Audit API
  slug: open-laserdata-audit-api
- collection_type: open
  name: LaserData Cloud Audit Account Billing API
  slug: open-laserdata-billing-api
- collection_type: open
  name: LaserData Cloud Audit Account Cloud Accounts API
  slug: open-laserdata-cloud-accounts-api
- collection_type: open
  name: LaserData Cloud Audit Account Clouds API
  slug: open-laserdata-clouds-api
- collection_type: open
  name: LaserData Cloud Audit Account Connectors API
  slug: open-laserdata-connectors-api
- collection_type: open
  name: LaserData Cloud Audit Account Deployments API
  slug: open-laserdata-deployments-api
- collection_type: open
  name: LaserData Cloud Audit Account Divisions API
  slug: open-laserdata-divisions-api
- collection_type: open
  name: LaserData Cloud Audit Account Environments API
  slug: open-laserdata-environments-api
- collection_type: open
  name: LaserData Cloud Audit Account Invitations API
  slug: open-laserdata-invitations-api
- collection_type: open
  name: LaserData Cloud Audit Account Members API
  slug: open-laserdata-members-api
- collection_type: open
  name: LaserData Cloud Audit Account Notification Channels API
  slug: open-laserdata-notification-channels-api
- collection_type: open
  name: LaserData Cloud Audit Account Notification Subscriptions API
  slug: open-laserdata-notification-subscriptions-api
- collection_type: open
  name: LaserData Cloud Audit Account Notifications API
  slug: open-laserdata-notifications-api
- collection_type: open
  name: LaserData Cloud Audit Account Payments API
  slug: open-laserdata-payments-api
- collection_type: open
  name: LaserData Cloud Audit Account Roles API
  slug: open-laserdata-roles-api
- collection_type: open
  name: LaserData Cloud Audit Account Tenants API
  slug: open-laserdata-tenants-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/laserdata-audit-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://laserdata.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.laserdata.cloud
- group: docs
  title: ''
  type: Documentation
  url: https://docs.laserdata.cloud
- group: docs
  title: ''
  type: APIReference
  url: https://api.laserdata.cloud/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.laserdata.cloud/getting-started/quick-start
- group: start
  title: ''
  type: SignUp
  url: https://laserdata.cloud
- group: operate
  title: ''
  type: Support
  url: mailto:hey@laserdata.com
- group: company
  title: ''
  type: Blog
  url: https://laserdata.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/laserdata
- group: commercial
  title: ''
  type: TermsOfService
  url: https://laserdata.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://laserdata.com/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.laserdata.cloud
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/laserdata-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/laserdata-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/laserdata-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/laserdata-cli.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/laserdata-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/laserdata-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/laserdata-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/laserdata-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/laserdata-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/laserdata-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/laserdata-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/laserdata-sandbox.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/laserdata-changelog.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/laserdata-notifications-webhooks.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/laserdata-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/laserdata-mcp.yml
- group: auth
  title: ''
  type: Security
  url: https://github.com/laserdata/laser-sdk/blob/main/SECURITY.md
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/laserdata-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/laserdata-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: LaserData is a hyper-efficient data streaming platform built in Rust for AI-native, real-time, and latency-sensitive workloads. Founded by the creators of Apache Iggy, LaserData packages the Iggy message-streaming engine — io_uring, thread-per-core, zero-copy deserialization, no garbage collection — as a managed cloud, BYOC, and on-premise product with sub-millisecond p99 latency and millions of messages per second per node. LaserData Cloud exposes a public REST control plane across three OpenAPI 3.1 services (Core, Audit, Notifier) covering tenants, divisions, environments, deployments, connectors, networking, API keys, roles and permissions, billing, notifications, and an immutable audit log, plus a per-deployment Supervisor API for configs, metrics, logs, diagnostic snapshots, and backups. The platform ships a first-party Rust SDK, a single-binary CLI with an interactive TUI, and an official Claude Code Agent Skill pack.
image: https://assets.laserdata.com/laserdata_dark.png
layout: provider
mcp_servers:
- description: ''
  name: LaserData MCP Server
  slug: laserdata-mcp-server
modified: '2026-07-19'
name: LaserData
nav: Providers
network: true
overview: 'LaserData publishes 18 APIs on the [APIs.io](https://apis.io/) network, including Account API, API Keys API, Audit API, and 15 more. Tagged areas include Streaming, Message Streaming, Event Streaming, Data Infrastructure, and Real-Time.


  The LaserData catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  LaserData''s developer surface includes documentation, API reference, getting-started guide, signup flow, support, engineering blog, CLI, and 26 more developer resources.'
random_paper: 0
score:
  band: strong
  composite: 54.7
  coverage:
    artifact_dirs: 20
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 69.0
    developer_ergonomics: 85.7
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 36.8
  previous_composite: 54.7
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 18
    mcp: derived
    skills: first-party
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/laserdata/refs/heads/main/screenshots/laserdata-2026-07-25T224540.png
security:
- kind: authentication
  name: Laserdata Authentication
  slug: laserdata-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Laserdata Domain Security
  slug: laserdata-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Laserdata Vulnerability Disclosure
  slug: laserdata-vulnerability-disclosure
  summary_line: Hackerone · contact published
slug: laserdata
tags:
- Streaming
- Message Streaming
- Event Streaming
- Data Infrastructure
- Real-Time
- Apache Iggy
- Rust
- Cloud Infrastructure
- AI Agents
- Observability
- Company
website: https://laserdata.com
---
