---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 52.7
  scored_at: '2026-08-17'
api_count: 3
apis:
- description: A Prometheus-compatible read API for querying Embrace metrics with PromQL. Standard Embrace metrics and any Custom Metrics an organization has created are queryable across one app, several apps, or ev
  name: Embrace Metrics API
  slug: embrace-metrics-api
- description: A REST management API for creating, retrieving and deleting the custom metrics of an Embrace organization. A custom metric is defined from a base Embrace metric plus group_by dimensions, a filter tree
  name: Embrace Custom Metrics API
  slug: embrace-custom-metrics-api
- description: A hosted Model Context Protocol server over Streamable HTTP that exposes an Embrace organization's real-user observability data to MCP-capable AI assistants. Twenty-one published tools span apps, cras
  name: Embrace MCP Server
  slug: embrace-mcp-server
artifact_total: 12
asyncapis:
- description: ''
  name: Embrace Alerts Webhooks
  slug: embrace-alerts-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/embrace-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/embrace-vulnerability-disclosure.yml
- group: company
  title: ''
  type: Website
  url: https://embrace.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://embrace.io/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://embrace.io/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://embrace.io/docs/metrics-forwarding/metrics-api/
- group: start
  title: ''
  type: GettingStarted
  url: https://embrace.io/docs/ios/6x/getting-started/
- group: operate
  title: ''
  type: Support
  url: https://embraceio-community.slack.com/join/shared_invite/zt-46iaieyz5-_684dnJ8U1yspqeQf~AGJA
- group: company
  title: ''
  type: Blog
  url: https://embrace.io/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://embrace.io/feed/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/embrace-io
- group: commercial
  title: ''
  type: Pricing
  url: https://embrace.io/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://dash.embrace.io/signup
- group: start
  title: ''
  type: Login
  url: https://dash.embrace.io/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://embrace.io/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://embrace.io/privacy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.embrace.io/
- group: operate
  title: ''
  type: ChangeLog
  url: https://embrace.io/docs/product/changelog/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.embrace.io/
- group: build
  title: ''
  type: Packages
  url: packages/embrace-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/embrace-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/embrace-cli.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/embrace-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/embrace-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/embrace-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/embrace-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/embrace-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/embrace-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/embrace-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/embrace-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/embrace-conformance.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/embrace-alerts-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/embrace-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/embrace-rate-limits.yml
created: '2026-08-12'
description: Embrace is a user-focused observability platform for mobile and web applications, built on OpenTelemetry. Its SDKs for iOS, Android, React Native, Flutter, Unity and the browser capture full-fidelity session, crash, exception, log, trace and network telemetry from real users, and the platform turns that into crash-free rates, user journeys, synthetics and custom dashboards. For programmatic access Embrace publishes a Prometheus-compatible Metrics API queried with PromQL, a Custom Metrics API for creating and managing derived metrics, OTLP forwarding to third-party destinations such as Datadog, Grafana Cloud, New Relic, Honeycomb, Elastic, Splunk, Chronosphere and Observe, outgoing alert webhooks, and a hosted Model Context Protocol server that exposes 21 read tools over crash, exception, log, span, session and network data to AI assistants using OAuth 2.0 or service-account bearer tokens.
image: https://embrace.io/wp-content/uploads/2023/07/Embrace-Logo-Pref-Lead-on-Yellow_1200x627.png
layout: provider
mcp_servers:
- description: ''
  name: embrace-mcp.yml
  slug: embrace-mcpyml
modified: '2026-08-12'
name: Embrace
nav: Providers
network: true
overview: 'Embrace publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Observability, Monitoring, Mobile, and Real User Monitoring.


  The Embrace catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Embrace''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 28 more developer resources.'
plans:
- name: Embrace Plans Pricing
  plan_count: 3
  slug: embrace-plans-pricing
random_paper: 123
rate_limits:
- limit_count: 14
  name: Embrace Rate Limits
  slug: embrace-rate-limits
scopes:
- name: Embrace Scopes
  scope_count: 3
  slug: embrace-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: exemplar
  composite: 66.5
  delta: 0.0
  facets:
    commercial_clarity: 84.2
    contract_quality: 51.6
    developer_ergonomics: 80.4
    discoverability: 92.6
    governance: 12.5
    operational_transparency: 76.3
  previous_composite: 66.5
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
security:
- kind: authentication
  name: Embrace Authentication
  slug: embrace-authentication
  summary_line: http/oauth2 · 5 schemes
- kind: domain-security
  name: Embrace Domain Security
  slug: embrace-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Embrace Vulnerability Disclosure
  slug: embrace-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Embrace Trust Center
  slug: embrace-trust-center
  summary_line: trust center published
slug: embrace
tags:
- Company
- Observability
- Monitoring
- Mobile
- Real User Monitoring
- OpenTelemetry
- Metrics
- Crash Reporting
- Application Performance Monitoring
- Developer Tools
- Model Context Protocol
website: https://embrace.io/
---
