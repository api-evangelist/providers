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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.8
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 29
  human_in_the_loop: 0
  name: Mattermost Agentic Access
  operation_count: 43
  slug: mattermost-agentic-access
  summary_line: 43 operations · 29 acting
api_count: 1
apis:
- description: REST API v4 for managing users, teams, channels, posts, threads, files, integrations, plugins, webhooks, slash commands, and OAuth applications. Authentication uses Personal Access Tokens or session t
  name: Mattermost REST API
  slug: rest-api
- description: Real-time WebSocket event stream for Mattermost v4. Clients connect to /api/v4/websocket, authenticate via cookie, Authorization header, or an authentication_challenge action, and receive event envelo
  name: Mattermost WebSocket API
  slug: websocket-api
- description: The Channels API from Mattermost — 7 operation(s) for channels.
  name: Mattermost Channels API
  slug: mattermost-channels-api
- description: The Posts API from Mattermost — 9 operation(s) for posts.
  name: Mattermost Posts API
  slug: mattermost-posts-api
- description: The Teams API from Mattermost — 6 operation(s) for teams.
  name: Mattermost Teams API
  slug: mattermost-teams-api
- description: The Users API from Mattermost — 8 operation(s) for users.
  name: Mattermost Users API
  slug: mattermost-users-api
artifact_total: 21
asyncapis:
- description: Mattermost's WebSocket API delivers real-time events from a Mattermost server to authenticated clients and accepts a small set of WebSocket actions for client-to-server interaction. A client opens a s
  name: Mattermost WebSocket API
  slug: mattermost-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Mattermost REST Channels API
  slug: open-mattermost-channels-api
- collection_type: open
  name: Mattermost REST Channels Posts API
  slug: open-mattermost-posts-api
- collection_type: open
  name: Mattermost REST Channels Teams API
  slug: open-mattermost-teams-api
- collection_type: open
  name: Mattermost REST Channels Users API
  slug: open-mattermost-users-api
- collection_type: open
  name: Mattermost REST API
  slug: open-mattermost
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/mattermost-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/mattermost-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/mattermost-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mattermost-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mattermost-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mattermost
- group: company
  title: ''
  type: Website
  url: https://mattermost.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.mattermost.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.mattermost.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mattermost
- group: start
  title: ''
  type: Signup
  url: https://mattermost.com/sign-up/
- group: commercial
  title: ''
  type: Pricing
  url: https://mattermost.com/pricing/
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/mattermost/mmctl-mcp
- group: company
  title: ''
  type: Blog
  url: https://mattermost.com/blog/feed/
created: '2026-05-11'
description: Mattermost is an open-source collaboration platform for technical teams that combines secure team messaging, workflow automation, voice/video calling, and integrations as a self-hosted Slack alternative. The Mattermost REST API exposes full programmatic control over users, teams, channels, posts, files, integrations, plugins, and webhooks.
graphqls:
- description: Conceptual GraphQL schema for the [Mattermost](https://mattermost.com) open-source team messaging platform, derived from the [Mattermost REST API v4](https://api.mattermost.com/).
  name: Mattermost GraphQL Schema
  slug: mattermost-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mattermost.png
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-29'
name: Mattermost
nav: Providers
network: true
overview: 'Mattermost publishes 5 APIs on the [APIs.io](https://apis.io/) network, including WebSocket API, Channels API, Posts API, and 2 more. Tagged areas include Messaging, Collaboration, Team Chat, Open-Source, and DevOps.


  The Mattermost catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Mattermost''s developer surface includes authentication, documentation, signup flow, pricing, engineering blog, and 9 more developer resources.'
random_paper: 12
rules:
- effective_rule_count: 35
  extends:
  - spectral:asyncapi
  name: Mattermost API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 7
  slug: mattermost-asyncapi-spectral-rules
score:
  band: thin
  composite: 37.0
  coverage:
    artifact_dirs: 10
    catalog_gap: 74.3
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 11.4
    contract_quality: 56.2
    developer_ergonomics: 40.5
    discoverability: 68.5
    governance: 11.4
    operational_transparency: 2.6
  previous_composite: 37.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mattermost/refs/heads/main/screenshots/mattermost-2026-06-20T185042.png
security:
- kind: authentication
  name: Mattermost Authentication
  slug: mattermost-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Mattermost Domain Security
  slug: mattermost-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Mattermost Vulnerability Disclosure
  slug: mattermost-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Mattermost Trust Center
  slug: mattermost-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, HIPAA, FedRAMP, GDPR
slug: mattermost
tags:
- Messaging
- Collaboration
- Team Chat
- Open-Source
- DevOps
- Self-Hosted
website: https://mattermost.com
---
