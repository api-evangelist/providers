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
  trial: false
  try_now: true
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
  score: 19.8
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Betterstack Agentic Access
  operation_count: 28
  slug: betterstack-agentic-access
  summary_line: 28 operations · 15 acting
api_count: 4
apis:
- description: The Heartbeats API from Better Stack — 3 operation(s) for heartbeats.
  name: Better Stack Heartbeats API
  slug: betterstack-heartbeats-api
- description: The Incidents API from Better Stack — 7 operation(s) for incidents.
  name: Better Stack Incidents API
  slug: betterstack-incidents-api
- description: The Monitors API from Better Stack — 4 operation(s) for monitors.
  name: Better Stack Monitors API
  slug: betterstack-monitors-api
- description: The Status Pages API from Better Stack — 3 operation(s) for status pages.
  name: Better Stack Status Pages API
  slug: betterstack-status-pages-api
artifact_total: 28
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
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/betterstack-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/betterstack-trust-center.yml
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
  type: GettingStarted
  url: https://betterstack.com/docs/uptime/api/getting-started/
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
created: '2026-03-25'
description: Better Stack is a comprehensive infrastructure monitoring and observability platform combining uptime monitoring, log management, incident management, status pages, and AI-powered site reliability tools. This is an alias entry for the better-stack repository. See https://github.com/api-evangelist/better-stack for the full API profile with OpenAPI specs, capabilities, and vocabulary.
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
- description: AI-powered root cause analysis for automated incident investigation.
  name: AI SRE
finops:
- name: Betterstack Finops
  service_category: API
  slug: betterstack-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/betterstack.png
integrations:
- description: Receive incident alerts in Slack channels.
  name: Slack
- description: Forward incidents to PagerDuty.
  name: PagerDuty
- description: Manage Better Stack resources as infrastructure as code.
  name: Terraform
- description: Send metrics, logs, and traces using OpenTelemetry exporters.
  name: OpenTelemetry
layout: provider
modified: '2026-04-19'
name: Better Stack
nav: Providers
network: true
overview: 'Better Stack publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Heartbeats API, Incidents API, Monitors API, and 1 more. Tagged areas include Observability, Uptime Monitoring, Incidents, Logs, and Monitoring.


  Better Stack''s developer surface includes authentication, developer portal, getting-started guide, pricing, engineering blog, changelog, and 7 more developer resources.'
plans:
- name: Betterstack Plans Pricing
  plan_count: 3
  slug: betterstack-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 5
  name: Betterstack Rate Limits
  slug: betterstack-rate-limits
score:
  band: thin
  composite: 37.4
  delta: 1.4
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 54.3
    developer_ergonomics: 31.0
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 36.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/betterstack/refs/heads/main/screenshots/betterstack-2026-06-20T173220.png
security:
- kind: authentication
  name: Betterstack Authentication
  slug: betterstack-authentication
  summary_line: http · 1 scheme
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
website: https://betterstack.com/docs/
---
