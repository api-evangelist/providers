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
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: true
    idempotency: verified
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 61.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Ando Agentic Access
  operation_count: 25
  slug: ando-agentic-access
  summary_line: 25 operations · 8 acting
api_count: 1
apis:
- baseURL: https://api.ando.so/v1
  baseurl_source: declared
  description: Call detail and transcript routes.
  name: Ando Calls API
  slug: ando-calls-api
- baseURL: https://api.ando.so/v1
  baseurl_source: declared
  description: Workspace member detail routes. Existing v1 paths keep member compatibility spellings.
  name: Ando Members API
  slug: ando-members-api
- baseURL: https://api.ando.so/v1
  baseurl_source: declared
  description: Message and conversation message routes.
  name: Ando Messages API
  slug: ando-messages-api
- baseURL: https://api.ando.so/v1
  baseurl_source: declared
  description: The Realtime API from Ando — 1 operation(s) for realtime.
  name: Ando Realtime API
  slug: ando-realtime-api
- baseURL: https://api.ando.so/v1
  baseurl_source: declared
  description: Search routes.
  name: Ando Search API
  slug: ando-search-api
- baseURL: https://api.ando.so/v1
  baseurl_source: declared
  description: Outbound webhook endpoint and delivery routes.
  name: Ando Webhooks API
  slug: ando-webhooks-api
- baseURL: https://api.ando.so/v1
  baseurl_source: declared
  description: Workspace agent lifecycle routes.
  name: Ando Agents API
  slug: ando-agents-api
- baseURL: https://api.ando.so/v1
  baseurl_source: declared
  description: Programmatic API key issuance and lifecycle routes.
  name: Ando API Keys API
  slug: ando-api-keys-api
- baseURL: https://api.ando.so/v1
  baseurl_source: declared
  description: Membership-scoped conversation routes.
  name: Ando Conversations API
  slug: ando-conversations-api
- baseURL: https://api.ando.so/v1
  baseurl_source: declared
  description: File upload lifecycle routes for public API message attachments.
  name: Ando Files API
  slug: ando-files-api
- baseURL: https://api.ando.so/v1
  baseurl_source: declared
  description: Move another chat tool's history into a workspace with original authors and timestamps. Requires an owner or admin API key with the imports:write scope.
  name: Ando Imports API
  slug: ando-imports-api
- baseURL: https://api.ando.so/v1
  baseurl_source: declared
  description: The Webhook sources API from Ando — 2 operation(s) for webhook sources.
  name: Ando Webhook sources API
  slug: ando-webhook-sources-api
artifact_total: 31
asyncapis:
- description: ''
  name: Ando Webhooks
  slug: ando-webhooks
collections:
- collection_type: open
  name: Ando Public Calls API
  slug: open-ando-calls-api
- collection_type: open
  name: Ando Public Calls Clipboards API
  slug: open-ando-clipboards-api
- collection_type: open
  name: Ando Public Calls Members API
  slug: open-ando-members-api
- collection_type: open
  name: Ando Public Calls Messages API
  slug: open-ando-messages-api
- collection_type: open
  name: Ando Public Calls Realtime API
  slug: open-ando-realtime-api
- collection_type: open
  name: Ando Public Calls Search API
  slug: open-ando-search-api
- collection_type: open
  name: Ando Public Calls Tasks API
  slug: open-ando-tasks-api
- collection_type: open
  name: Ando Public Calls Webhooks API
  slug: open-ando-webhooks-api
common:
- group: commercial
  href: https://artifacts.apis.io/ando/plans/ando-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ando-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/ando/capabilities/ando-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/ando-capability-edges.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.ando.so
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ando.so
- group: docs
  title: ''
  type: APIReference
  url: https://docs.ando.so/api-reference/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.ando.so/developers/quickstart
- group: auth
  href: https://artifacts.apis.io/ando/authentication/ando-authentication.yml
  title: ''
  type: Authentication
  url: authentication/ando-authentication.yml
- group: docs
  href: https://artifacts.apis.io/ando/openapi/_original/ando-public-api-v1-openapi.json
  title: ''
  type: OpenAPI
  url: openapi/_original/ando-public-api-v1-openapi.json
- group: other
  href: https://artifacts.apis.io/ando/overlays/ando-public-api-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/ando-public-api-v1-overlay.yaml
- group: design
  href: https://artifacts.apis.io/ando/conventions/ando-conventions.yml
  title: ''
  type: Conventions
  url: conventions/ando-conventions.yml
- group: design
  href: https://artifacts.apis.io/ando/conventions/ando-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/ando-conventions.yml
- group: design
  href: https://artifacts.apis.io/ando/errors/ando-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/ando-problem-types.yml
- group: design
  href: https://artifacts.apis.io/ando/data-model/ando-data-model.yml
  title: ''
  type: DataModel
  url: data-model/ando-data-model.yml
- group: design
  href: https://artifacts.apis.io/ando/conformance/ando-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ando-conformance.yml
- group: design
  href: https://artifacts.apis.io/ando/asyncapi/ando-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/ando-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/ando/mcp/ando-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/ando-mcp.yml
- group: agent
  href: https://artifacts.apis.io/ando/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/ando/agentic-access/ando-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/ando-agentic-access.yml
- group: build
  href: https://artifacts.apis.io/ando/packages/ando-packages.yml
  title: ''
  type: Packages
  url: packages/ando-packages.yml
- group: build
  href: https://artifacts.apis.io/ando/packages/ando-packages.yml
  title: ''
  type: SDKs
  url: packages/ando-packages.yml
- group: build
  href: https://artifacts.apis.io/ando/cli/ando-cli.yml
  title: ''
  type: CLI
  url: cli/ando-cli.yml
- group: agent
  href: https://artifacts.apis.io/ando/llms/ando-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ando-llms.txt
- group: agent
  href: https://artifacts.apis.io/ando/well-known/ando-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ando-well-known.yml
- group: design
  href: https://artifacts.apis.io/ando/lifecycle/ando-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/ando-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.ando.so
- group: operate
  href: https://artifacts.apis.io/ando/changelog/ando-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/ando-changelog.yml
- group: auth
  href: https://artifacts.apis.io/ando/security/ando-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ando-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://docs.ando.so/changelog
- group: operate
  title: ''
  type: Support
  url: https://docs.ando.so/docs/start-guide
- group: start
  title: ''
  type: SignUp
  url: https://app.ando.so
- group: start
  title: ''
  type: Login
  url: https://app.ando.so
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ando.so/security/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ando.so/security/privacy-policy
- group: company
  title: ''
  type: About
  url: https://ando.so/about
- group: other
  title: ''
  type: X
  url: https://x.com/andocorporation
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/andohq/
- group: company
  title: ''
  type: Website
  url: https://ando.so
created: '2026-07-17'
description: Ando is a messaging platform built from the ground up for teams that work alongside AI agents, positioned as a rearchitected alternative to Slack for human-agent collaboration. Agents join conversations as first-class members with shared context, memory, permissions, and tools, while humans see only what needs their attention. Ando ships a public REST API v1 (api.ando.so/v1) with API-key auth, required idempotency keys on writes, cursor pagination, HMAC-signed webhooks, a realtime websocket, a hosted MCP server (mcp.ando.so), a typed TypeScript SDK (@andocorp/sdk), and an agent-first CLI (@andocorp/cli). The legal entity is Asari Inc.; the company is backed by Index Ventures, Accel, and Emergence.
finops:
- has_sources: true
  method: derived
  name: Ando Finops
  primary_unit: ''
  service_category: ''
  slug: ando-finops
  template: true
image: https://www.ando.so/opengraph-image.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.ando.so over HTTP; 29 tools listed.
  name: Ando MCP Server
  slug: ando
modified: '2026-07-17'
name: Ando
nav: Providers
network: true
overview: 'Ando publishes 12 API contracts indexed on the [APIs.io](https://apis.io/) network, including Calls API, Members API, Messages API, and 9 more. Tagged areas include Company, Business Applications, Messaging, Team Collaboration, and AI Agents.


  The Ando catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Ando''s developer surface includes documentation, API reference, getting-started guide, authentication, CLI, changelog, engineering blog, and 30 more developer resources.'
plans:
- name: Ando Plans Pricing
  plan_count: 0
  slug: ando-plans-pricing
random_paper: 10
rules:
- authorship: generated
  effective_rule_count: 110
  extends:
  - spectral:oas
  name: Ando API Rules
  rule_count: 69
  severity_counts:
    error: 53
    hint: 0
    info: 4
    warn: 12
  slug: ando-rules
score:
  band: developing
  composite: 51.9
  coverage:
    artifact_dirs: 29
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.9
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 62.9
    developer_ergonomics: 73.2
    discoverability: 75.0
    operational_transparency: 31.6
  previous_composite: 51.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 60.0
      total: 20
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 27.8
screenshot: https://apis.io/screenshots/ando/ando-2026-07-25T200233.png
security:
- kind: authentication
  name: Ando Authentication
  slug: ando-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Ando Domain Security
  slug: ando-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 3
skills:
- name: Post a message and reply in a thread
  slug: ando-post-message-and-reply
- name: Receive and verify Ando webhooks
  slug: ando-receive-and-verify-webhooks
- name: Search and read Ando workspace context
  slug: ando-search-and-read-context
slug: ando
tags:
- Company
- Business Applications
- Messaging
- Team Collaboration
- AI Agents
- Agents
- Developer Tools
- MCP
- Webhook
- Productivity
website: https://ando.so
---
