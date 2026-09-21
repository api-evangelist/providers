---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 46.3
  scored_at: '2026-09-20'
api_count: 1
apis:
- baseURL: https://api.clix.so
  baseurl_source: declared
  description: 'Server-to-server REST API for Clix mobile push: create/update/delete project users and their properties, register devices and bind them to users, ingest events, send ad-hoc push notifications to one o'
  name: Clix External API
  slug: clix-external-api
- description: 'Agent2Agent (A2A) protocol surface: a public agent card at https://api.clix.so/.well-known/agent-card.json (0.3.0 shape by default, 1.0 shape under the A2A-Version: 1.0 header; graded conformant) and '
  name: Clix A2A Agent
  slug: clix-a2a-agent
- description: 'Model Context Protocol surfaces, both documentation-only: the provider''s stdio server @clix-so/clix-mcp-server 0.1.4 (npx -y @clix-so/clix-mcp-server@latest; tools search_docs and search_sdk over the '
  name: Clix MCP Server
  slug: clix-mcp-server
artifact_total: 10
asyncapis:
- description: ''
  name: Clix So Webhooks
  slug: clix-so-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://clix.so/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.clix.so/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.clix.so/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.clix.so/api-reference/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.clix.so/sdk-quickstart-ios
- group: start
  title: ''
  type: Login
  url: https://console.clix.so/
- group: commercial
  title: ''
  type: Pricing
  url: https://clix.so/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://clix.so/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://clix.so/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://clix.so/status
- group: operate
  title: ''
  type: SLA
  url: https://clix.so/availability
- group: company
  title: ''
  type: Blog
  url: https://blog.clix.so/
- group: company
  title: ''
  type: BlogRSS
  url: https://blog.clix.so/rss/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/clix-so
- group: operate
  title: ''
  type: Support
  url: https://docs.clix.so/troubleshooting/not-getting-push-notification
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/clix-so/refs/heads/main/llms/clix-so-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/clix-so-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://docs.clix.so/llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/clix-so/refs/heads/main/a2a/clix-so-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/clix-so-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/clix-so/refs/heads/main/mcp/clix-so-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/clix-so-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/clix-so/refs/heads/main/mcp/clix-so-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/clix-so-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/clix-so/refs/heads/main/well-known/clix-so-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/clix-so-well-known.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/clix-so/refs/heads/main/packages/clix-so-packages.yml
  title: ''
  type: Packages
  url: packages/clix-so-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/clix-so/refs/heads/main/packages/clix-so-packages.yml
  title: ''
  type: SDKs
  url: packages/clix-so-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/clix-so/refs/heads/main/cli/clix-so-cli.yml
  title: ''
  type: CLI
  url: cli/clix-so-cli.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/clix-so/refs/heads/main/authentication/clix-so-authentication.yml
  title: ''
  type: Authentication
  url: authentication/clix-so-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/clix-so/refs/heads/main/conventions/clix-so-conventions.yml
  title: ''
  type: Conventions
  url: conventions/clix-so-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/clix-so/refs/heads/main/conventions/clix-so-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/clix-so-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/clix-so/refs/heads/main/errors/clix-so-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/clix-so-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/clix-so/refs/heads/main/lifecycle/clix-so-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/clix-so-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/clix-so/refs/heads/main/changelog/clix-so-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/clix-so-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/clix-so/refs/heads/main/conformance/clix-so-conformance.yml
  title: ''
  type: Conformance
  url: conformance/clix-so-conformance.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/clix-so/refs/heads/main/rate-limits/clix-so-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/clix-so-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/clix-so/refs/heads/main/plans/clix-so-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/clix-so-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/clix-so/refs/heads/main/asyncapi/clix-so-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/clix-so-webhooks.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/clix-so/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/clix-so/refs/heads/main/data-model/clix-so-data-model.yml
  title: ''
  type: DataModel
  url: data-model/clix-so-data-model.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/clix-so/refs/heads/main/security/clix-so-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/clix-so-domain-security.yml
- group: other
  title: ''
  type: DataSubjectRequest
  url: https://clix.so/privacy
- group: other
  title: ''
  type: DataResidency
  url: https://clix.so/availability
- group: operate
  title: ''
  type: IncidentNotification
  url: https://docs.clix.so/ops/incident-communication
created: '2026-09-19'
description: 'Clix is a US-based, developer-first mobile push notification platform for iOS, Android, React Native and Flutter — one CLI command (clix install) automates Firebase Cloud Messaging and APNs setup, and the console adds behaviour-triggered and API-triggered campaigns, real-time delivery logs, full-funnel analytics and device/user lifecycle management, priced free to 100K active devices then $30/month. For developers and agents it publishes a small REST API at https://api.clix.so (OpenAPI 3.1.0 generated from clix/external/v1/clix.proto: 11 operations across users, devices, events, messages:send, live-activities:start and campaigns/{id}:trigger, authenticated with X-Clix-Project-ID + X-Clix-API-Key), an A2A agent at https://api.clix.so/a2a whose card at /.well-known/agent-card.json is served in both 0.3.0 and 1.0 shapes and exposes four skills (create-user, track-event, send-push-notification, trigger-campaign) with idempotency keys, SSE streaming, task cancellation and task webhooks,
  a stdio MCP server (@clix-so/clix-mcp-server) plus a Mintlify docs MCP endpoint — both documentation-only — an open agent-skills repo, first-party SDKs on Maven Central, CocoaPods/SwiftPM, pub.dev and npm, a self-hosted status page with a published 99.5% monthly SLO, and console-configured PUSH_SENT/PUSH_FAILED webhooks.'
image: https://clix.so/opengraph-image?04675f86137dbf70
layout: provider
mcp_servers:
- description: ''
  name: Clix MCP Server
  slug: clix-mcp-server
- description: ''
  name: Mintlify docs MCP endpoint (Streamable HTTP)
  slug: mintlify-docs-mcp-endpoint-streamable-http
modified: '2026-09-19'
name: Clix
nav: Providers
network: true
overview: 'Clix publishes 1 API on the [APIs.io](https://apis.io/) network: External API. Tagged areas include Push Notifications, Mobile, Messaging, Campaigns, and Event Tracking.


  The Clix catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Clix''s developer surface includes documentation, API reference, getting-started guide, pricing, engineering blog, support, CLI, and 33 more developer resources.'
plans:
- name: Clix So Plans Pricing
  plan_count: 3
  slug: clix-so-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 1
  name: Clix So Rate Limits
  slug: clix-so-rate-limits
score:
  band: strong
  composite: 66.1
  coverage:
    artifact_dirs: 21
    catalog_earned: 57.0
    catalog_earned_first_party: 20.0
    catalog_gap: 58.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 63.3
  facets:
    access_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 61.2
    developer_ergonomics: 78.6
    discoverability: 75.9
    operational_transparency: 65.8
  previous_composite: 2.8
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: first-party
  schema_version: 0.22.0
  scored_at: '2026-09-20'
  trend: rising
  upsert:
    applies: true
    score: 22.2
security:
- kind: authentication
  name: Clix So Authentication
  slug: clix-so-authentication
  summary_line: apiKey · 5 schemes
- kind: domain-security
  name: Clix So Domain Security
  slug: clix-so-domain-security
  summary_line: TLSv1.3 · DMARC
slug: clix-so
tags:
- Push Notifications
- Mobile
- Messaging
- Campaigns
- Event Tracking
- Customer Engagement
- A2A
- MCP
- Agents
- SDK
- United States
- Company
website: https://clix.so/
---
