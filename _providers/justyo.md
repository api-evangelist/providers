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
    agent_skills: derived
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 35.8
  scored_at: '2026-07-28'
api_count: 2
apis:
- description: Read account/subscriber information.
  name: justyo Account API
  slug: justyo-account-api
- description: Send Yo notifications to subscribers.
  name: justyo Yo API
  slug: justyo-yo-api
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://justyo.co
- group: docs
  title: ''
  type: Documentation
  url: https://docs.justyo.co/
- group: start
  title: ''
  type: DeveloperPortal
  url: http://dev.justyo.co/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/YoApp
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.justyo.co/
- group: build
  title: ''
  type: Packages
  url: packages/justyo-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/justyo-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/justyo-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/justyo-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/justyo-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/justyo-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/justyo-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/justyo-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/justyo-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: 'Yo (justyo.co) was a single-tap notification app and "the world''s simplest API." A service registered an API username, received an api_token, and could push a lightweight "Yo" notification to a single subscriber or broadcast to all subscribers, optionally attaching a link, plus read the subscriber count. The Yo API had effectively one job — fire a push — with an api_token for auth (an OAuth 2.0 page was documented but never enabled) and first-party client SDKs across Python, PHP, Java, Node, Ruby, Scala and iOS under the github.com/YoApp organization. The Yo service is now defunct: the justyo.co host is suspended and its api/docs/dev subdomains no longer resolve. This API Evangelist profile captures the historical Yo API surface for the record.'
image: https://raw.githubusercontent.com/api-evangelist/justyo/refs/heads/main/openapi/justyo-yo-openapi.yml
layout: provider
mcp_servers:
- description: ''
  name: justyo-mcp.yml
  slug: justyo-mcpyml
modified: '2026-07-19'
name: justyo
nav: Providers
network: true
overview: 'justyo publishes 2 APIs on the [APIs.io](https://apis.io/) network: Account API and Yo API. Tagged areas include Company, Notifications, Push Notifications, Messaging, and Mobile.


  justyo''s developer surface includes documentation, signup flow, authentication, and 12 more developer resources.'
random_paper: 30
rate_limits:
- limit_count: 0
  name: Justyo Rate Limits
  slug: justyo-rate-limits
score:
  band: thin
  composite: 32.9
  delta: -4.3
  facets:
    commercial_clarity: 13.2
    contract_quality: 60.2
    developer_ergonomics: 38.6
    discoverability: 87.0
    governance: 8.3
    operational_transparency: 5.3
  previous_composite: 37.2
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 16.7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Justyo Authentication
  slug: justyo-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Justyo Domain Security
  slug: justyo-domain-security
  summary_line: no transport/DNS hardening detected
slug: justyo
tags:
- Company
- Notifications
- Push Notifications
- Messaging
- Mobile
- Developer Tools
- API
website: https://justyo.co
---
