---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 59.6
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 36
  human_in_the_loop: 3
  name: Spike Sh Agentic Access
  operation_count: 85
  slug: spike-sh-agentic-access
  summary_line: 85 operations · 36 acting · 3 human-in-the-loop
api_count: 17
apis:
- description: Alert rule (automation) management endpoints
  name: Spike.sh Alert Rules API
  slug: spike-sh-alert-rules-api
- description: Status page component management endpoints
  name: Spike.sh Components API
  slug: spike-sh-components-api
- description: Escalation policy management endpoints
  name: Spike.sh Escalations API
  slug: spike-sh-escalations-api
- description: Actions that can be performed on incidents
  name: Spike.sh Incident Actions API
  slug: spike-sh-incident-actions-api
- description: Incident management endpoints
  name: Spike.sh Incidents API
  slug: spike-sh-incidents-api
- description: Integration management endpoints
  name: Spike.sh Integrations API
  slug: spike-sh-integrations-api
- description: On-call override management endpoints
  name: Spike.sh On-Call Overrides API
  slug: spike-sh-on-call-overrides-api
- description: On-call schedule management endpoints
  name: Spike.sh On-Call Schedules API
  slug: spike-sh-on-call-schedules-api
- description: Organization management endpoints
  name: Spike.sh Orgs API
  slug: spike-sh-orgs-api
- description: Planned maintenance management endpoints
  name: Spike.sh Planned Maintenances API
  slug: spike-sh-planned-maintenances-api
- description: Service management endpoints
  name: Spike.sh Services API
  slug: spike-sh-services-api
- description: Status page incident management endpoints
  name: Spike.sh Status Page Incidents API
  slug: spike-sh-status-page-incidents-api
- description: Status page management endpoints
  name: Spike.sh Status Pages API
  slug: spike-sh-status-pages-api
- description: Status page subscriber management endpoints
  name: Spike.sh Subscribers API
  slug: spike-sh-subscribers-api
- description: Suppressed incident management
  name: Spike.sh Suppressed Incidents API
  slug: spike-sh-suppressed-incidents-api
- description: Team management endpoints
  name: Spike.sh Teams API
  slug: spike-sh-teams-api
- description: User management endpoints
  name: Spike.sh Users API
  slug: spike-sh-users-api
artifact_total: 34
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/spike-sh-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/spike-sh-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/spike-sh-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://spike.sh
- group: docs
  title: ''
  type: Documentation
  url: https://docs.spike.sh
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/spikehq
- group: company
  title: ''
  type: LinkedIn
  url: https://linkedin.com/company/spike-hq
- group: company
  title: ''
  type: Blog
  url: https://spike.sh/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://spike.sh/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.spike.sh
- group: other
  title: ''
  type: X
  url: https://twitter.com/spikedhq
- group: commercial
  title: ''
  type: Plans
  url: plans/spike-sh-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/spike-sh-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/spike-sh-finops.yml
- group: agent
  title: ''
  type: MCPServer
  url: https://mcp.spike.sh/mcp
created: '2026-06-13'
description: Spike.sh is an incident management and on-call platform that helps engineering teams detect, respond to, and resolve incidents faster. It provides a REST API for managing escalation policies, on-call schedules, incidents, services, integrations, and alerting rules. The platform offers phone, SMS, WhatsApp, Telegram, Slack, and Microsoft Teams notifications, along with status pages, war rooms, and 80+ integrations with tools like Prometheus, Datadog, AWS, and Sentry.
examples:
- key_count: 3
  name: Spike Sh Create Escalation Policy Example
  slug: spike-sh-create-escalation-policy-example
- key_count: 6
  name: Spike Sh Create Incident Example
  slug: spike-sh-create-incident-example
- key_count: 5
  name: Spike Sh Create On Call Schedule Example
  slug: spike-sh-create-on-call-schedule-example
- key_count: 7
  name: Spike Sh Create Status Page Incident Example
  slug: spike-sh-create-status-page-incident-example
- key_count: 12
  name: Spike Sh Incident Response Example
  slug: spike-sh-incident-response-example
finops:
- name: Spike Sh Finops
  service_category: ''
  slug: spike-sh-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/spike-sh.png
json_schemas:
- name: Spike.sh Escalation Policy
  property_count: 6
  slug: spike-sh-escalation-policy
- name: Spike.sh Incident
  property_count: 12
  slug: spike-sh-incident
- name: Spike.sh On-Call Schedule
  property_count: 7
  slug: spike-sh-on-call-schedule
jsonld:
- class_count: 15
  name: Spike Sh Context
  property_count: 38
  slug: spike-sh-context
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-07-20'
name: Spike.sh
nav: Providers
network: true
overview: 'Spike.sh publishes 17 APIs on the [APIs.io](https://apis.io/) network, including Alert Rules API, Components API, Escalations API, and 14 more. Tagged areas include Incident Management, On-Call, Alerting, Escalation Policies, and Status Pages.


  The Spike.sh catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Spike.sh''s developer surface includes authentication, documentation, engineering blog, pricing, and 11 more developer resources.'
plans:
- name: Spike Sh Plans Pricing
  plan_count: 3
  slug: spike-sh-plans-pricing
random_paper: 39
rate_limits:
- limit_count: 0
  name: Spike Sh Rate Limits
  slug: spike-sh-rate-limits
rules:
- name: Spike.sh API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: spike-sh-jsonschema-spectral-rules
score:
  band: developing
  composite: 54.7
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 68.1
    developer_ergonomics: 30.4
    discoverability: 100.0
    governance: 73.7
    operational_transparency: 21.1
  previous_composite: 54.7
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/spike-sh/refs/heads/main/screenshots/spike-sh-2026-06-20T194313.png
security:
- kind: authentication
  name: Spike Sh Authentication
  slug: spike-sh-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Spike Sh Domain Security
  slug: spike-sh-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: spike-sh
tags:
- Incident Management
- On-Call
- Alerting
- Escalation Policies
- Status Pages
- Monitoring
- DevOps
- SRE
website: https://spike.sh
---
