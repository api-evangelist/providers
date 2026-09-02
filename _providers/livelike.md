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
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.0
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: REST API for managing LiveLike applications, user profiles, programs, interactive widgets (polls, quizzes, predictions, alerts), chat rooms, gamification, and rewards. OAuth 2.0 Bearer authentication;
  name: LiveLike REST API
  slug: livelike-rest-api
artifact_total: 6
asyncapis:
- description: ''
  name: Livelike Webhooks
  slug: livelike-webhooks
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/livelike-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: security/livelike-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/livelike-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.livelike.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.livelike.com/docs/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://docs.livelike.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.livelike.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.livelike.com/docs/rest-api-getting-started
- group: auth
  title: ''
  type: Authentication
  url: https://docs.livelike.com/reference/authentication
- group: company
  title: ''
  type: Blog
  url: https://www.livelike.com/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.livelike.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://www.livelike.com/contact
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/livelike
- group: start
  title: ''
  type: Login
  url: https://cf-blast.livelikecdn.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.livelike.com/changelog
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/livelike-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/livelike-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/livelike-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/livelike-mcp.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/livelike-webhooks.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/livelike-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/livelike-problem-types.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/livelike-authentication.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/livelike-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/livelike-changelog.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: LiveLike is an AI-powered fan engagement platform used by sports teams, leagues, media companies, and venues to drive registration, retention, and monetization through interactive experiences. Its developer platform exposes a REST API, GraphQL, webhooks, and native SDKs (iOS, Android, Web, React Native) for building live interactive widgets (polls, quizzes, predictions, alerts), real-time chat and community features, gamification (leaderboards, badges, quests, streaks, rewards), user profiles, and analytics that can be synchronized to live and on-demand video. LiveLike also publishes an official Model Context Protocol (MCP) server so AI assistants can manage programs and widgets.
image: https://www.livelike.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: LiveLike MCP Server
  slug: livelike-mcp-server
modified: '2026-07-20'
name: LiveLike
nav: Providers
network: true
overview: 'LiveLike publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fan Engagement, Live Streaming, Interactive Video, and Chat.


  The LiveLike catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  LiveLike''s developer surface includes documentation, API reference, getting-started guide, authentication, engineering blog, support, changelog, and 19 more developer resources.'
random_paper: 13
score:
  band: thin
  composite: 35.2
  coverage:
    artifact_dirs: 15
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.3
  facets:
    access_clarity: 32.9
    commercial_clarity: 32.9
    contract_governance: 0.0
    contract_quality: 41.6
    developer_ergonomics: 41.1
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 18.4
  previous_composite: 35.5
  provenance:
    mcp: first-party
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/livelike/refs/heads/main/screenshots/livelike-2026-07-25T225358.png
security:
- kind: authentication
  name: Livelike Authentication
  slug: livelike-authentication
  summary_line: oauth2/http · 2 schemes
- kind: domain-security
  name: Livelike Domain Security
  slug: livelike-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Livelike Trust Center
  slug: livelike-trust-center
  summary_line: SOC 2, GDPR
slug: livelike
tags:
- Company
- Fan Engagement
- Live Streaming
- Interactive Video
- Chat
- Gamification
- Widgets
- Sports
- Media
website: https://www.livelike.com/
---
