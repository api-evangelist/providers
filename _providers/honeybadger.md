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
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 16
  human_in_the_loop: 0
  name: Honeybadger Agentic Access
  operation_count: 31
  slug: honeybadger-agentic-access
  summary_line: 31 operations · 16 acting
api_count: 1
apis:
- description: 'Ingestion API for submitting exceptions, deploys, check-ins, source maps, and events from instrumented applications to Honeybadger. Uses a Project API Key as the authentication credential and accepts '
  name: Honeybadger Reporting API
  slug: reporting-api
- description: REST API for reading and modifying account data such as projects, faults, comments, teams, and integrations. Authenticated via HTTP Basic auth using a Personal Authentication Token as the username.
  name: Honeybadger Data API
  slug: data-api
- description: Outbound webhook notification surface delivered by Honeybadger to subscriber URLs configured via Project Settings > Alerts & Integrations. Covers the generic Webhook integration's documented event typ
  name: Honeybadger Outbound Webhook Notifications
  slug: webhooks
- baseURL: https://api.honeybadger.io/v1
  baseurl_source: declared
  description: The Check In API from Honeybadger — 1 operation(s) for check in.
  name: Honeybadger Check In API
  slug: honeybadger-check-in-api
- baseURL: https://api.honeybadger.io/v1
  baseurl_source: declared
  description: The Deploys API from Honeybadger — 1 operation(s) for deploys.
  name: Honeybadger Deploys API
  slug: honeybadger-deploys-api
- baseURL: https://api.honeybadger.io/v1
  baseurl_source: declared
  description: The Events API from Honeybadger — 1 operation(s) for events.
  name: Honeybadger Events API
  slug: honeybadger-events-api
- baseURL: https://api.honeybadger.io/v1
  baseurl_source: declared
  description: The Notices API from Honeybadger — 1 operation(s) for notices.
  name: Honeybadger Notices API
  slug: honeybadger-notices-api
- baseURL: https://api.honeybadger.io/v1
  baseurl_source: declared
  description: The Projects API from Honeybadger — 21 operation(s) for projects.
  name: Honeybadger Projects API
  slug: honeybadger-projects-api
- baseURL: https://api.honeybadger.io/v1
  baseurl_source: declared
  description: The Source Maps API from Honeybadger — 1 operation(s) for source maps.
  name: Honeybadger Source Maps API
  slug: honeybadger-source-maps-api
artifact_total: 24
asyncapis:
- description: AsyncAPI description of the outbound webhook notifications Honeybadger delivers to subscriber URLs that have been configured via Project Settings > Alerts & Integrations. This surface covers the gener
  name: Honeybadger Outbound Webhook Notifications
  slug: honeybadger-webhooks-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Honeybadger Check In API
  slug: open-honeybadger-check-in-api
- collection_type: open
  name: Honeybadger Check In Deploys API
  slug: open-honeybadger-deploys-api
- collection_type: open
  name: Honeybadger Check In Events API
  slug: open-honeybadger-events-api
- collection_type: open
  name: Honeybadger Check In Notices API
  slug: open-honeybadger-notices-api
- collection_type: open
  name: Honeybadger Check In Projects API
  slug: open-honeybadger-projects-api
- collection_type: open
  name: Honeybadger Check In Source Maps API
  slug: open-honeybadger-source-maps-api
- collection_type: open
  name: Honeybadger API
  slug: open-honeybadger
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/honeybadger-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/honeybadger-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/honeybadger-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/honeybadger-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.honeybadger.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.honeybadger.io
- group: commercial
  title: ''
  type: Pricing
  url: https://www.honeybadger.io/plans/
- group: start
  title: ''
  type: Signup
  url: https://app.honeybadger.io/users/sign_up
- group: company
  title: ''
  type: Blog
  url: https://www.honeybadger.io/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/honeybadger-io
- group: build
  title: ''
  type: GitHub SDK
  url: https://github.com/honeybadger-io/cli
- group: operate
  title: ''
  type: Support
  url: mailto:support@honeybadger.io
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/honeybadger-industries
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/honeybadger-io/honeybadger-mcp-server
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.honeybadger.io/llms.txt
created: '2026-05-11'
description: Honeybadger is an application monitoring platform that combines exception tracking, uptime monitoring, cron and background job monitoring, and status pages into a single service for software developers and operations teams. The platform supports a wide range of languages and frameworks including Ruby, Rails, Python, Node.js, PHP, Elixir, Go, and JavaScript, and integrates with Slack, GitHub, PagerDuty, and other developer tools. Honeybadger exposes a Reporting API for ingesting errors, deploys, and check-ins, plus a Data API for accessing account data, both using HTTP Basic authentication.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/honeybadger.png
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-30'
name: Honeybadger
nav: Providers
network: true
overview: 'Honeybadger publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Outbound Webhook Notifications, Check In API, Deploys API, and 4 more. Tagged areas include Error Monitoring, Exception Tracking, Application Performance Monitoring, Uptime Monitoring, and Cron Monitoring.


  The Honeybadger catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Honeybadger''s developer surface includes authentication, documentation, pricing, signup flow, engineering blog, support, and 9 more developer resources.'
random_paper: 5
rules:
- effective_rule_count: 35
  extends:
  - spectral:asyncapi
  name: Honeybadger API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 7
  slug: honeybadger-asyncapi-spectral-rules
score:
  band: thin
  composite: 36.0
  coverage:
    artifact_dirs: 10
    catalog_gap: 74.3
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 11.4
    contract_quality: 58.7
    developer_ergonomics: 28.6
    discoverability: 75.9
    governance: 11.4
    operational_transparency: 2.6
  previous_composite: 36.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/honeybadger/refs/heads/main/screenshots/honeybadger-2026-06-20T182819.png
security:
- kind: authentication
  name: Honeybadger Authentication
  slug: honeybadger-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Honeybadger Domain Security
  slug: honeybadger-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Honeybadger Trust Center
  slug: honeybadger-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: honeybadger
tags:
- Error Monitoring
- Exception Tracking
- Application Performance Monitoring
- Uptime Monitoring
- Cron Monitoring
- Observability
website: https://www.honeybadger.io
---
