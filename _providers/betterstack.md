---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
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
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 50.4
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Betterstack Agentic Access
  operation_count: 28
  slug: betterstack-agentic-access
  summary_line: 28 operations · 15 acting
api_count: 1
apis:
- baseURL: https://uptime.betterstack.com/api/v2
  baseurl_source: declared
  description: The Heartbeats API from Better Stack — create and manage heartbeat monitors that alert when a cron job or background task stops reporting.
  name: Better Stack Heartbeats API
  slug: betterstack-heartbeats-api
- baseURL: https://uptime.betterstack.com/api/v2
  baseurl_source: declared
  description: The Incidents API from Better Stack — create, acknowledge, escalate, resolve and reopen incidents, and read the incident timeline.
  name: Better Stack Incidents API
  slug: betterstack-incidents-api
- baseURL: https://uptime.betterstack.com/api/v2
  baseurl_source: declared
  description: The Monitors API from Better Stack — create and manage uptime monitors and read their availability and response-time series.
  name: Better Stack Monitors API
  slug: betterstack-monitors-api
- baseURL: https://uptime.betterstack.com/api/v2
  baseurl_source: declared
  description: The Status Pages API from Better Stack — create and manage public and private status pages and the resources shown on them.
  name: Better Stack Status Pages API
  slug: betterstack-status-pages-api
- description: The Telemetry API from Better Stack — manage log, trace and metric sources, fields, metric expressions, dashboards, charts and chart alerts. Declared by Better Stack's own /.well-known/api-catalog; no
  name: Better Stack Telemetry API
  slug: betterstack-telemetry-api
- description: The Errors API from Better Stack — manage error-tracking applications, application groups and releases, and triage error patterns and exceptions. Declared by Better Stack's own /.well-known/api-catalo
  name: Better Stack Errors API
  slug: betterstack-errors-api
artifact_total: 36
asyncapis:
- description: ''
  name: Betterstack Webhooks
  slug: betterstack-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Better Stack Uptime Heartbeats API
  slug: open-betterstack-heartbeats-api
- collection_type: open
  name: Better Stack Uptime Heartbeats Incidents API
  slug: open-betterstack-incidents-api
- collection_type: open
  name: Better Stack Uptime Heartbeats Monitors API
  slug: open-betterstack-monitors-api
- collection_type: open
  name: Better Stack Uptime Heartbeats Status Pages API
  slug: open-betterstack-status-pages-api
- collection_type: open
  name: Better Stack Uptime API
  slug: open-betterstack
common:
- group: company
  title: ''
  type: Website
  url: https://betterstack.com/
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/betterstack-agentic-access.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/betterstack-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/betterstack-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/betterstack-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/betterstack-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/betterstack-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/betterstack-trust-center.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/betterstack-trust-center.yml
- group: auth
  title: ''
  type: Security
  url: security/betterstack-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/betterstack-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/betterstack-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/betterstack-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/betterstack-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/betterstack-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/betterstack-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/betterstack-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/betterstack-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/betterstack-webhooks.yml
- group: build
  title: ''
  type: Packages
  url: packages/betterstack-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/betterstack-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/betterstack-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/betterstack-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/betterstack-finops.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/betterstack-changelog.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/betterstack
- group: start
  title: ''
  type: Portal
  url: https://betterstack.com/docs/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://betterstack.com/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://betterstack.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://betterstack.com/docs/uptime/api
- group: start
  title: ''
  type: GettingStarted
  url: https://betterstack.com/docs/uptime/api/getting-started-with-uptime-api/
- group: commercial
  title: ''
  type: Pricing
  url: https://betterstack.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.betterstack.com/
- group: company
  title: ''
  type: Blog
  url: https://betterstack.com/community/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://betterstack.com/tag/changelog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/BetterStackHQ
- group: operate
  title: ''
  type: Support
  url: https://betterstack.com/help
- group: start
  title: ''
  type: SignUp
  url: https://betterstack.com/users/sign-up
- group: start
  title: ''
  type: Login
  url: https://betterstack.com/users/sign-in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://betterstack.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://betterstack.com/privacy
created: '2026-03-25'
description: Better Stack is an infrastructure monitoring and observability platform that combines uptime monitoring, heartbeat monitoring for scheduled jobs, incident management with on-call paging and escalation policies, public and private status pages, log/trace/metric telemetry queried with ClickHouse SQL, error tracking with session replay, and an AI SRE for automated root cause analysis. It is OpenTelemetry-native on ingestion — OTLP/HTTP endpoints for logs, traces and metrics — and publishes three REST management surfaces (Uptime v2, Telemetry v1, Errors v1) declared in its own RFC 9727 /.well-known/api-catalog, alongside a first-party remote MCP server at mcp.betterstack.com exposing roughly 106 agent tools behind OAuth 2.1.
features:
- description: Monitor URLs, APIs, and services for availability with global region checks.
  name: Uptime Monitoring
- description: Monitor scheduled jobs and cron tasks with heartbeat pings.
  name: Heartbeat Monitoring
- description: On-call alerting with escalation policies, acknowledgement, and resolution workflows.
  name: Incident Management
- description: Public and private status pages with custom domains and real-time component status.
  name: Status Pages
- description: Collect, search, and visualize logs across your infrastructure stack.
  name: Log Management
- description: Two-layer error tracking — deduplicated error patterns over individual exceptions — with session replay.
  name: Error Tracking
- description: AI-powered root cause analysis for automated incident investigation.
  name: AI SRE
- description: First-party remote MCP server at mcp.betterstack.com exposing ~106 agent tools across Uptime, Telemetry and Errors behind OAuth 2.1.
  name: MCP Server
finops:
- name: Betterstack Finops
  service_category: API
  slug: betterstack-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/betterstack.png
integrations:
- description: Receive incident alerts in Slack channels.
  name: Slack
- description: Run incident management from initial report to resolution inside Teams.
  name: Microsoft Teams
- description: Forward incidents to PagerDuty.
  name: PagerDuty
- description: Manage Better Stack resources as infrastructure as code via the first-party BetterStackHQ providers.
  name: Terraform
- description: Send logs, metrics and traces over OTLP/HTTP to $INGESTING_HOST/v1/logs, /v1/traces and /v1/metrics.
  name: OpenTelemetry
layout: provider
mcp_servers:
- description: 'Better Stack ships a first-party remote MCP server that fronts the Uptime, Telemetry (logs/traces/metrics) and Error Tracking products, plus a documentation search tool and team administration. It is '
  name: Better Stack MCP Server
  slug: better-stack-mcp-server
modified: '2026-09-04'
name: Better Stack
nav: Providers
network: true
overview: 'Better Stack publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Heartbeats API, Incidents API, Monitors API, and 1 more. Tagged areas include Observability, Uptime Monitoring, Incidents, Logs, and Monitoring.


  The Better Stack catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Better Stack''s developer surface includes authentication, changelog, developer portal, documentation, API reference, getting-started guide, pricing, and 35 more developer resources.'
plans:
- name: Betterstack Plans Pricing
  plan_count: 6
  slug: betterstack-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Betterstack Rate Limits
  slug: betterstack-rate-limits
scopes:
- name: Betterstack Scopes
  scope_count: 0
  slug: betterstack-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 64.2
  coverage:
    artifact_dirs: 24
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 6.1
  facets:
    access_clarity: 100.0
    commercial_clarity: 100.0
    contract_governance: 18.2
    contract_quality: 61.6
    developer_ergonomics: 66.1
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 44.7
  previous_composite: 58.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/betterstack/refs/heads/main/screenshots/betterstack-2026-06-20T173220.png
security:
- kind: authentication
  name: Betterstack Authentication
  slug: betterstack-authentication
  summary_line: http/oauth2 · 3 schemes
- kind: domain-security
  name: Betterstack Domain Security
  slug: betterstack-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Betterstack Vulnerability Disclosure
  slug: betterstack-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Betterstack Trust Center
  slug: betterstack-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: betterstack
tags:
- Observability
- Uptime Monitoring
- Incidents
- Logs
- Monitoring
- Status Pages
- On-Call
- Error Tracking
- OpenTelemetry
- Model Context Protocol
website: https://betterstack.com/
---
