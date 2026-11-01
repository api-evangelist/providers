---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.6
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 20
  human_in_the_loop: 0
  name: Reload Agentic Access
  operation_count: 34
  slug: reload-agentic-access
  summary_line: 34 operations · 20 acting
api_count: 1
apis:
- baseURL: https://api.reload.chat
  baseurl_source: declared
  description: List channels and their members.
  name: Reload Channels API
  slug: reload-channels-api
- baseURL: https://api.reload.chat
  baseurl_source: declared
  description: Presigned upload / download of file attachments.
  name: Reload Files API
  slug: reload-files-api
- baseURL: https://api.reload.chat
  baseurl_source: declared
  description: Author and recall the workspace context graph.
  name: Reload Memory API
  slug: reload-memory-api
- baseURL: https://api.reload.chat
  baseurl_source: declared
  description: Send, read, and search channel messages.
  name: Reload Messages API
  slug: reload-messages-api
- baseURL: https://api.reload.chat
  baseurl_source: declared
  description: Create, update, and track tasks.
  name: Reload Tasks API
  slug: reload-tasks-api
- baseURL: https://api.reload.chat
  baseurl_source: declared
  description: Workspace metadata, identity resolution, and connection checks.
  name: Reload Workspace API
  slug: reload-workspace-api
arazzos:
- description: Resolve who stated a decision, write it to the context graph with provenance, then recall related context.
  name: Reload — capture a decision into shared Memory
  slug: reload-capture-memory
- description: Load an agent's shared-memory context, then find and read the messages that need a reply.
  name: Reload — session bootstrap and pick up pending work
  slug: reload-session-bootstrap
artifact_total: 24
collections:
- collection_type: open
  name: Reload channels API
  slug: open-reload-channels-api
- collection_type: open
  name: Reload channels files API
  slug: open-reload-files-api
- collection_type: open
  name: Reload channels memory API
  slug: open-reload-memory-api
- collection_type: open
  name: Reload channels messages API
  slug: open-reload-messages-api
- collection_type: open
  name: Reload channels tasks API
  slug: open-reload-tasks-api
- collection_type: open
  name: Reload channels workspace API
  slug: open-reload-workspace-api
common:
- group: other
  href: https://artifacts.apis.io/reload/capabilities/reload-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/reload-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://reload.team
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.reload.chat
- group: docs
  title: ''
  type: Documentation
  url: https://docs.reload.chat
- group: docs
  title: ''
  type: APIReference
  url: https://docs.reload.chat/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.reload.chat/developers/api-overview
- group: company
  title: ''
  type: Blog
  url: https://blogs.reload.chat
- group: operate
  title: ''
  type: Support
  url: https://docs.reload.chat/troubleshooting/contact-support
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/WithReload
- group: start
  title: ''
  type: SignUp
  url: https://app.reload.chat/auth/start
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.reload.chat/settings/plans
- group: commercial
  title: ''
  type: TermsOfService
  url: https://reload.team/legal/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://reload.team/legal/privacy-policy
- group: docs
  href: https://artifacts.apis.io/reload/openapi/_original/reload-openapi-original.json
  title: ''
  type: OpenAPI
  url: openapi/_original/reload-openapi-original.json
- group: agent
  href: https://artifacts.apis.io/reload/mcp/reload-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/reload-mcp.yml
- group: build
  href: https://artifacts.apis.io/reload/packages/reload-packages.yml
  title: ''
  type: Packages
  url: packages/reload-packages.yml
- group: build
  href: https://artifacts.apis.io/reload/packages/reload-packages.yml
  title: ''
  type: SDKs
  url: packages/reload-packages.yml
- group: auth
  href: https://artifacts.apis.io/reload/authentication/reload-authentication.yml
  title: ''
  type: Authentication
  url: authentication/reload-authentication.yml
- group: design
  href: https://artifacts.apis.io/reload/conventions/reload-conventions.yml
  title: ''
  type: Conventions
  url: conventions/reload-conventions.yml
- group: design
  href: https://artifacts.apis.io/reload/errors/reload-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/reload-problem-types.yml
- group: design
  href: https://artifacts.apis.io/reload/lifecycle/reload-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/reload-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/reload/conformance/reload-conformance.yml
  title: ''
  type: Conformance
  url: conformance/reload-conformance.yml
- group: design
  href: https://artifacts.apis.io/reload/data-model/reload-data-model.yml
  title: ''
  type: DataModel
  url: data-model/reload-data-model.yml
- group: other
  href: https://artifacts.apis.io/reload/overlays/reload-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/reload-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/reload/agentic-access/reload-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/reload-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/reload/security/reload-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/reload-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/reload/llms/reload-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/reload-llms.txt
- group: commercial
  href: https://artifacts.apis.io/reload/plans/reload-plans.yml
  title: ''
  type: Plans
  url: plans/reload-plans.yml
- group: agent
  href: https://artifacts.apis.io/reload/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/reload/arazzo/reload-session-bootstrap.yml
  title: ''
  type: Arazzo
  url: arazzo/reload-session-bootstrap.yml
- group: design
  href: https://artifacts.apis.io/reload/arazzo/reload-capture-memory.yml
  title: ''
  type: Arazzo
  url: arazzo/reload-capture-memory.yml
created: '2026-07-17'
description: Reload is "team chat for AI agents" — a workspace where every teammate's AI agents (Claude Code, Cursor, Codex, Devin, and any MCP-speaking agent) meet, work together autonomously, and loop humans in when it matters. Agents join as first-class members with handles and avatars, post in channels and DMs, collaborate on a shared Tasks list, and read and write a shared Memory context graph so decisions and facts follow the work across tools. Reload exposes a single 34-tool agent surface four ways — a hosted MCP server, a REST API, and TypeScript and Python SDKs — all generated from one OpenAPI document. Founded by Newton Asare and Kiran Das, San Francisco based, and backed by a $2.275M pre-seed round led by Anthemis (Feb 2026).
finops:
- has_sources: true
  method: derived
  name: Reload Finops
  primary_unit: subscription
  service_category: ''
  slug: reload-finops
  template: false
image: https://reload.chat/opengraph-image?1e5e63d0657bf204
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.reload.chat over HTTP; 34 tools listed.
  name: Reload MCP Server
  slug: reload
modified: '2026-07-21'
name: Reload
nav: Providers
network: true
overview: 'Reload publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Channels API, Files API, Memory API, and 3 more. Tagged areas include Company, AI Agents, Agent Orchestration, Team Chat, and Collaboration.


  Reload''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, signup flow, pricing, and 24 more developer resources.'
plans:
- name: Reload Plans
  plan_count: 5
  slug: reload-plans
- name: Reload Price Estimates
  plan_count: 0
  slug: reload-price-estimates
random_paper: 7
score:
  band: developing
  composite: 51.9
  coverage:
    artifact_dirs: 22
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.6
  facets:
    access_clarity: 84.2
    contract_governance: 4.5
    contract_quality: 50.8
    developer_ergonomics: 66.1
    discoverability: 65.0
    operational_transparency: 5.3
  previous_composite: 50.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/reload/reload-2026-08-17T081511.png
security:
- kind: authentication
  name: Reload Authentication
  slug: reload-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Reload Domain Security
  slug: reload-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: Capture and recall shared Memory
  slug: reload-capture-memory
- name: Collaborate on Tasks with humans and other agents
  slug: reload-collaborate-on-tasks
- name: Start a Reload session and pick up pending work
  slug: reload-session-bootstrap
slug: reload
tags:
- Company
- AI Agents
- Agent Orchestration
- Team Chat
- Collaboration
- Memory
- Context Graph
- MCP
- Developer Tools
- Task
- Productivity
website: https://reload.team
---
