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
    event_surface_described: false
    idempotency: documented
    mcp_server: verified
    openapi_examples: partial
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 59.1
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 38
  human_in_the_loop: 0
  name: Mem Agentic Access
  operation_count: 64
  slug: mem-agentic-access
  summary_line: 64 operations · 38 acting
api_count: 5
apis:
- description: The CoreApi__service-info API from Mem — 1 operation(s) for coreapi__service-info.
  name: Mem CoreApi__service-info API
  slug: mem-coreapi-service-info-api
- description: The external API from Mem — 53 operation(s) for external.
  name: Mem external API
  slug: mem-external-api
- description: The external-v0 API from Mem — 4 operation(s) for external-v0.
  name: Mem external-v0 API
  slug: mem-external-v0-api
- description: The external-v1 API from Mem — 3 operation(s) for external-v1.
  name: Mem external-v1 API
  slug: mem-external-v1-api
- description: The external-v2 API from Mem — 44 operation(s) for external-v2.
  name: Mem external-v2 API
  slug: mem-external-v2-api
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Mem Public Client CoreApi__service-info API
  slug: open-mem-coreapi-service-info-api
- collection_type: open
  name: Mem Public Client CoreApi__service-info external API
  slug: open-mem-external-api
- collection_type: open
  name: Mem Public Client CoreApi__service-info external-v0 API
  slug: open-mem-external-v0-api
- collection_type: open
  name: Mem Public Client CoreApi__service-info external-v1 API
  slug: open-mem-external-v1-api
- collection_type: open
  name: Mem Public Client CoreApi__service-info external-v2 API
  slug: open-mem-external-v2-api
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.mem.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.mem.ai
- group: docs
  title: ''
  type: APIReference
  url: https://docs.mem.ai/api-reference/overview/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.mem.ai/guides/get-started/quickstart
- group: company
  title: ''
  type: Blog
  url: https://get.mem.ai/blog
- group: operate
  title: ''
  type: Support
  url: https://help.mem.ai
- group: operate
  title: ''
  type: Community
  url: https://get.mem.ai/slack
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mem-ai
- group: commercial
  title: ''
  type: Pricing
  url: https://mem.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://mem.ai/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mem.ai/pages/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mem.ai/pages/privacy
- group: auth
  title: ''
  type: Security
  url: https://mem.ai/pages/security
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.mem.ai/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/mem-openapi-original.json
- group: agent
  title: ''
  type: MCPServer
  url: mcp/mem-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mem-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/mem-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mem-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/mem-scopes.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/mem-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mem-domain-security.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/mem-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/mem-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/mem-rate-limits.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/mem-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/mem-lifecycle.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/mem-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/mem-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/mem-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/mem-openapi-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Mem is an AI-native note-taking and knowledge workspace that captures notes, meetings, and ideas and keeps them instantly searchable and discoverable. It pairs a Workspace (notes, collections, projects, calendar, meeting transcription) with an Agent that tracks priorities and surfaces timely reminders. Mem exposes a REST API (the Mem Public Client API at https://api.mem.ai) for creating, reading, searching, and organizing notes and collections, plus semantic search, attachments, audio recordings, calendar, sessions, and tasks. It also ships an official hosted Model Context Protocol (MCP) server so AI tools like Claude, ChatGPT, and CLI agents can work with a user's Mem knowledge natively over OAuth. Mem is backed by a16z.
image: https://storage.googleapis.com/mem-public-assets/sq-f.jpg
layout: provider
mcp_servers:
- description: Mem ships an official hosted, remote MCP server that gives AI tools secure OAuth-authenticated access to a user's Mem notes and collections. The docs state it exposes 23 tools for reading, creating, s
  name: Mem MCP
  slug: mem-mcp
modified: '2026-07-20'
name: Mem
nav: Providers
network: true
overview: 'Mem publishes 5 APIs on the [APIs.io](https://apis.io/) network, including CoreApi__service-info API, external API, external-v0 API, and 2 more. Tagged areas include Company, Notes, Knowledge-Management, Productivity, and Artificial Intelligence.


  Mem''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, signup flow, and 25 more developer resources.'
random_paper: 4
rate_limits:
- limit_count: 4
  name: Mem Rate Limits
  slug: mem-rate-limits
scopes:
- name: Mem Scopes
  scope_count: 4
  slug: mem-scopes
  summary_line: 4 scopes · authorizationCode/clientCredentials
score:
  band: developing
  composite: 43.6
  delta: 0.0
  facets:
    access_clarity: 7.9
    commercial_clarity: 7.9
    contract_governance: 16.7
    contract_quality: 49.9
    developer_ergonomics: 58.9
    discoverability: 92.6
    governance: 16.7
    operational_transparency: 50.0
  previous_composite: 43.6
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
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mem/refs/heads/main/screenshots/mem-2026-08-07T172453.png
security:
- kind: authentication
  name: Mem Authentication
  slug: mem-authentication
  summary_line: apiKey/http/oauth2 · 3 schemes
- kind: domain-security
  name: Mem Domain Security
  slug: mem-domain-security
  summary_line: TLSv1.3 · DMARC
slug: mem
tags:
- Company
- Notes
- Knowledge-Management
- Productivity
- Artificial Intelligence
- Note Taking
- Search
- MCP
- Agents
- Meetings
website: https://docs.mem.ai
---
