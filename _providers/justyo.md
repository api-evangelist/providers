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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.8
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Read account/subscriber information.
  name: justyo Account API
  slug: justyo-account-api
- description: Send Yo notifications to subscribers.
  name: justyo Yo API
  slug: justyo-yo-api
artifact_total: 9
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Yo Account API
  slug: open-justyo-account-api
- collection_type: open
  name: Account Yo API
  slug: open-justyo-yo-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/justyo-yo-overlay.yaml
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
  name: justyo MCP Server
  slug: justyo-mcp-server
modified: '2026-07-19'
name: justyo
nav: Providers
network: true
overview: 'justyo publishes 2 APIs on the [APIs.io](https://apis.io/) network: Account API and Yo API. Tagged areas include Company, Notification, Push Notifications, Messaging, and Mobile.


  justyo''s developer surface includes documentation, signup flow, authentication, and 13 more developer resources.'
random_paper: 14
rate_limits:
- limit_count: 1
  name: Justyo Rate Limits
  slug: justyo-rate-limits
score:
  band: emerging
  composite: 21.2
  coverage:
    artifact_dirs: 15
    catalog_gap: 70.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 6.6
    commercial_clarity: 6.6
    contract_governance: 0.0
    contract_quality: 12.6
    developer_ergonomics: 30.4
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 21.2
  provenance:
    contracts:
      callable: 0.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
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
- Notification
- Push Notifications
- Messaging
- Mobile
- Developer Tools
website: https://justyo.co
---
