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
    agent_skills: true
    agentic_access: true
    asyncapi_events: true
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.1
  score: 57.7
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 36
  human_in_the_loop: 1
  name: Timeular Agentic Access
  operation_count: 52
  slug: timeular-agentic-access
  summary_line: 52 operations · 36 acting · 1 human-in-the-loop
api_count: 11
apis:
- description: The Activities API from Timeular — 3 operation(s) for activities.
  name: Timeular Activities API
  slug: timeular-activities-api
- description: The Authentication API from Timeular — 3 operation(s) for authentication.
  name: Timeular Authentication API
  slug: timeular-authentication-api
- description: The Current Tracking API from Timeular — 3 operation(s) for current tracking.
  name: Timeular Current Tracking API
  slug: timeular-current-tracking-api
- description: The Folders API from Timeular — 4 operation(s) for folders.
  name: Timeular Folders API
  slug: timeular-folders-api
- description: The Leaves API from Timeular — 6 operation(s) for leaves.
  name: Timeular Leaves API
  slug: timeular-leaves-api
- description: The Members API from Timeular — 2 operation(s) for members.
  name: Timeular Members API
  slug: timeular-members-api
- description: The Reports API from Timeular — 1 operation(s) for reports.
  name: Timeular Reports API
  slug: timeular-reports-api
- description: The Tags & Mentions API from Timeular — 5 operation(s) for tags & mentions.
  name: Timeular Tags & Mentions API
  slug: timeular-tags-mentions-api
- description: The Time Entries API from Timeular — 3 operation(s) for time entries.
  name: Timeular Time Entries API
  slug: timeular-time-entries-api
- description: The Users API from Timeular — 2 operation(s) for users.
  name: Timeular Users API
  slug: timeular-users-api
- description: The Webhooks API from Timeular — 3 operation(s) for webhooks.
  name: Timeular Webhooks API
  slug: timeular-webhooks-api
artifact_total: 16
asyncapis:
- description: Event surface derived from the EARLY (Timeular) public webhook API. Consumers subscribe a publicly reachable HTTPS target URL to a named event via POST /api/v4/webhooks/subscription; EARLY delivers th
  name: EARLY (Timeular) Webhooks
  slug: timeular-early-asyncapi
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.early.app/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.early.app/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.early.app/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.early.app/
- group: operate
  title: ''
  type: Support
  url: https://support.early.app/en/
- group: company
  title: ''
  type: Blog
  url: https://early.app/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://early.app/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://product.early.app/register
- group: start
  title: ''
  type: Login
  url: https://product.early.app/login
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://early.app/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/timeular
- group: company
  title: ''
  type: Website
  url: https://early.app/
- group: agent
  title: ''
  type: MCPServer
  url: mcp/timeular-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/timeular-llms.txt
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/timeular-lifecycle.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/timeular-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/timeular-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Webhooks
  url: webhooks/timeular-early-webhooks.yml
created: '2026-07-17'
description: Timeular (now branded EARLY) is a time-tracking company whose apps and physical tracking device help individuals and teams capture where their time goes. Its public REST API — hosted at api.early.app — lets developers manage activities, start and stop live tracking, create and query time entries over date ranges, generate reports, organize tags and mentions, administer folders, users and leave, and subscribe to webhooks for time-tracking and leave events. Authentication uses an API Key and API Secret exchanged for a short-lived Bearer Access Token. The API is versioned in the URI path (V4 is current; V3 and V2 remain available) and is published as a public Postman collection. Timeular is backed by Speedinvest.
image: https://content.pstmn.io/b2851088-5dea-4fb1-9fc8-ba83d3c33bc2/RUFSTFktV09SRE1BUkstREFSSy1HUkVFTi1QUklNQVJZLnBuZw==
layout: provider
mcp_servers:
- description: ''
  name: timeular-mcp.yml
  slug: timeular-mcpyml
modified: '2026-07-21'
name: Timeular
nav: Providers
network: true
overview: 'Timeular publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Activities API, Authentication API, Current Tracking API, and 8 more. Tagged areas include Company, Time Tracking, Productivity, Time Management, and Reporting.


  The Timeular catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Timeular''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 12 more developer resources.'
random_paper: 51
score:
  band: developing
  composite: 47.2
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 69.3
    developer_ergonomics: 56.5
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 47.2
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: authentication
  name: Timeular Authentication
  slug: timeular-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Timeular Domain Security
  slug: timeular-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: timeular
tags:
- Company
- Time Tracking
- Productivity
- Time Management
- Reporting
- Team Management
- Webhooks
- SaaS
website: https://early.app/
---
