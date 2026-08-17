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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.1
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 18
  human_in_the_loop: 0
  name: Better Stack Agentic Access
  operation_count: 33
  slug: better-stack-agentic-access
  summary_line: 33 operations · 18 acting
api_count: 6
apis:
- description: Manage escalation policies and on-call schedules
  name: Better Stack Escalation Policies API
  slug: better-stack-escalation-policies-api
- description: Manage heartbeat monitors for scheduled jobs and cron tasks
  name: Better Stack Heartbeats API
  slug: better-stack-heartbeats-api
- description: Manage incidents and on-call alerting
  name: Better Stack Incidents API
  slug: better-stack-incidents-api
- description: Manage uptime monitors for URLs, APIs, and services
  name: Better Stack Monitors API
  slug: better-stack-monitors-api
- description: Manage public and private status pages
  name: Better Stack Status Pages API
  slug: better-stack-status-pages-api
- description: Manage team members and invitations
  name: Better Stack Team Members API
  slug: better-stack-team-members-api
artifact_total: 167
collections:
- collection_type: postman
  name: Better Stack Escalation Policies API
  slug: postman-better-stack-escalation-policies-api
- collection_type: postman
  name: Better Stack Escalation Policies Heartbeats API
  slug: postman-better-stack-heartbeats-api
- collection_type: postman
  name: Better Stack Escalation Policies Incidents API
  slug: postman-better-stack-incidents-api
- collection_type: postman
  name: Better Stack Escalation Policies Monitors API
  slug: postman-better-stack-monitors-api
- collection_type: postman
  name: Better Stack Escalation Policies Status Pages API
  slug: postman-better-stack-status-pages-api
- collection_type: postman
  name: Better Stack Escalation Policies Team Members API
  slug: postman-better-stack-team-members-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Better Stack Escalation Policies API
  slug: open-better-stack-escalation-policies-api
- collection_type: open
  name: Better Stack Escalation Policies Heartbeats API
  slug: open-better-stack-heartbeats-api
- collection_type: open
  name: Better Stack Escalation Policies Incidents API
  slug: open-better-stack-incidents-api
- collection_type: open
  name: Better Stack Escalation Policies Monitors API
  slug: open-better-stack-monitors-api
- collection_type: open
  name: Better Stack Escalation Policies Status Pages API
  slug: open-better-stack-status-pages-api
- collection_type: open
  name: Better Stack Escalation Policies Team Members API
  slug: open-better-stack-team-members-api
- collection_type: open
  name: Better Stack API
  slug: open-better-stack
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/better-stack/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/better-stack-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/better-stack-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/better-stack-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/better-stack-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/better-stack-authentication.yml
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
- group: auth
  title: ''
  type: Authentication
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
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/better-stack/refs/heads/main/rules/better-stack-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/better-stack/refs/heads/main/vocabulary/better-stack-vocabulary.yaml
created: '2025-01-08'
description: Better Stack is a comprehensive infrastructure monitoring and observability platform that combines uptime monitoring, log management, incident management, status pages, and AI-powered site reliability tools. It helps teams identify and resolve website and server issues quickly by providing real-time alerting, detailed diagnostics, on-call scheduling, and public/private status pages.
examples:
- key_count: 1
  name: Better Stack Availability Response Example
  slug: better-stack-availability-response-example
- key_count: 12
  name: Better Stack Heartbeat Attributes Example
  slug: better-stack-heartbeat-attributes-example
- key_count: 7
  name: Better Stack Heartbeat Create Request Example
  slug: better-stack-heartbeat-create-request-example
- key_count: 2
  name: Better Stack Heartbeat List Response Example
  slug: better-stack-heartbeat-list-response-example
- key_count: 3
  name: Better Stack Heartbeat Object Example
  slug: better-stack-heartbeat-object-example
- key_count: 1
  name: Better Stack Heartbeat Single Response Example
  slug: better-stack-heartbeat-single-response-example
- key_count: 3
  name: Better Stack Heartbeat Update Request Example
  slug: better-stack-heartbeat-update-request-example
- key_count: 10
  name: Better Stack Incident Attributes Example
  slug: better-stack-incident-attributes-example
- key_count: 5
  name: Better Stack Incident Create Request Example
  slug: better-stack-incident-create-request-example
- key_count: 2
  name: Better Stack Incident List Response Example
  slug: better-stack-incident-list-response-example
- key_count: 3
  name: Better Stack Incident Object Example
  slug: better-stack-incident-object-example
- key_count: 1
  name: Better Stack Incident Single Response Example
  slug: better-stack-incident-single-response-example
- key_count: 17
  name: Better Stack Monitor Attributes Example
  slug: better-stack-monitor-attributes-example
- key_count: 11
  name: Better Stack Monitor Create Request Example
  slug: better-stack-monitor-create-request-example
- key_count: 2
  name: Better Stack Monitor List Response Example
  slug: better-stack-monitor-list-response-example
- key_count: 3
  name: Better Stack Monitor Object Example
  slug: better-stack-monitor-object-example
- key_count: 1
  name: Better Stack Monitor Single Response Example
  slug: better-stack-monitor-single-response-example
- key_count: 8
  name: Better Stack Monitor Update Request Example
  slug: better-stack-monitor-update-request-example
- key_count: 4
  name: Better Stack Pagination Example
  slug: better-stack-pagination-example
- key_count: 7
  name: Better Stack Policy Attributes Example
  slug: better-stack-policy-attributes-example
- key_count: 3
  name: Better Stack Policy Create Request Example
  slug: better-stack-policy-create-request-example
- key_count: 2
  name: Better Stack Policy List Response Example
  slug: better-stack-policy-list-response-example
- key_count: 3
  name: Better Stack Policy Object Example
  slug: better-stack-policy-object-example
- key_count: 1
  name: Better Stack Policy Single Response Example
  slug: better-stack-policy-single-response-example
- key_count: 2
  name: Better Stack Policy Step Example
  slug: better-stack-policy-step-example
- key_count: 3
  name: Better Stack Policy Update Request Example
  slug: better-stack-policy-update-request-example
- key_count: 1
  name: Better Stack Response Times Response Example
  slug: better-stack-response-times-response-example
- key_count: 9
  name: Better Stack Status Page Attributes Example
  slug: better-stack-status-page-attributes-example
- key_count: 5
  name: Better Stack Status Page Create Request Example
  slug: better-stack-status-page-create-request-example
- key_count: 2
  name: Better Stack Status Page List Response Example
  slug: better-stack-status-page-list-response-example
- key_count: 3
  name: Better Stack Status Page Object Example
  slug: better-stack-status-page-object-example
- key_count: 1
  name: Better Stack Status Page Single Response Example
  slug: better-stack-status-page-single-response-example
- key_count: 3
  name: Better Stack Status Page Update Request Example
  slug: better-stack-status-page-update-request-example
- key_count: 5
  name: Better Stack Team Member Attributes Example
  slug: better-stack-team-member-attributes-example
- key_count: 2
  name: Better Stack Team Member Invite Request Example
  slug: better-stack-team-member-invite-request-example
- key_count: 2
  name: Better Stack Team Member List Response Example
  slug: better-stack-team-member-list-response-example
- key_count: 3
  name: Better Stack Team Member Object Example
  slug: better-stack-team-member-object-example
- key_count: 1
  name: Better Stack Team Member Single Response Example
  slug: better-stack-team-member-single-response-example
features:
- description: Monitor URLs, APIs, and services for availability with checks from multiple global regions every 30 seconds.
  name: Uptime Monitoring
- description: Monitor scheduled jobs, cron tasks, and background workers by pinging a unique URL on each run.
  name: Heartbeat Monitoring
- description: Automatically create and manage incidents when monitors detect downtime, with acknowledgement and resolution workflows.
  name: Incident Management
- description: Configure escalation policies with multi-step notification sequences via phone, SMS, email, and push.
  name: On-Call Scheduling
- description: Create public and private status pages with custom domains, branding, and real-time component status.
  name: Status Pages
- description: Collect, search, and visualize logs across your entire infrastructure stack.
  name: Log Management
- description: AI-powered root cause analysis that automatically investigates incidents and suggests resolutions.
  name: AI SRE
- description: OpenTelemetry-native monitoring with dashboards for metrics and infrastructure health.
  name: Infrastructure Monitoring
- description: Manage Better Stack resources as code using the official Terraform provider.
  name: Terraform Provider
- description: Model Context Protocol server for integrating Better Stack with AI tools and agents.
  name: MCP Server
finops:
- name: Better Stack Finops
  service_category: API
  slug: better-stack-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/better-stack.png
integrations:
- description: Receive incident alerts and status updates directly in Slack channels.
  name: Slack
- description: Forward incidents to PagerDuty for existing on-call workflows.
  name: PagerDuty
- description: Manage monitors, status pages, and escalation policies as infrastructure as code.
  name: Terraform
- description: Send metrics, logs, and traces using OpenTelemetry-compatible exporters.
  name: OpenTelemetry
- description: Compatible with Sentry SDK for error tracking integration.
  name: Sentry
- description: Connect Better Stack monitoring data with New Relic dashboards.
  name: New Relic
json_schemas:
- name: AvailabilityResponse
  property_count: 1
  slug: better-stack-availability-response
- name: HeartbeatAttributes
  property_count: 12
  slug: better-stack-heartbeat-attributes
- name: HeartbeatCreateRequest
  property_count: 7
  slug: better-stack-heartbeat-create-request
- name: HeartbeatListResponse
  property_count: 2
  slug: better-stack-heartbeat-list-response
- name: HeartbeatObject
  property_count: 3
  slug: better-stack-heartbeat-object
- name: HeartbeatSingleResponse
  property_count: 1
  slug: better-stack-heartbeat-single-response
- name: HeartbeatUpdateRequest
  property_count: 3
  slug: better-stack-heartbeat-update-request
- name: IncidentAttributes
  property_count: 10
  slug: better-stack-incident-attributes
- name: IncidentCreateRequest
  property_count: 5
  slug: better-stack-incident-create-request
- name: IncidentListResponse
  property_count: 2
  slug: better-stack-incident-list-response
- name: IncidentObject
  property_count: 3
  slug: better-stack-incident-object
- name: IncidentSingleResponse
  property_count: 1
  slug: better-stack-incident-single-response
- name: MonitorAttributes
  property_count: 17
  slug: better-stack-monitor-attributes
- name: MonitorCreateRequest
  property_count: 11
  slug: better-stack-monitor-create-request
- name: MonitorListResponse
  property_count: 2
  slug: better-stack-monitor-list-response
- name: MonitorObject
  property_count: 3
  slug: better-stack-monitor-object
- name: MonitorSingleResponse
  property_count: 1
  slug: better-stack-monitor-single-response
- name: MonitorUpdateRequest
  property_count: 8
  slug: better-stack-monitor-update-request
- name: Pagination
  property_count: 4
  slug: better-stack-pagination
- name: PolicyAttributes
  property_count: 7
  slug: better-stack-policy-attributes
- name: PolicyCreateRequest
  property_count: 3
  slug: better-stack-policy-create-request
- name: PolicyListResponse
  property_count: 2
  slug: better-stack-policy-list-response
- name: PolicyObject
  property_count: 3
  slug: better-stack-policy-object
- name: PolicySingleResponse
  property_count: 1
  slug: better-stack-policy-single-response
- name: PolicyStep
  property_count: 2
  slug: better-stack-policy-step
- name: PolicyUpdateRequest
  property_count: 3
  slug: better-stack-policy-update-request
- name: ResponseTimesResponse
  property_count: 1
  slug: better-stack-response-times-response
- name: StatusPageAttributes
  property_count: 9
  slug: better-stack-status-page-attributes
- name: StatusPageCreateRequest
  property_count: 5
  slug: better-stack-status-page-create-request
- name: StatusPageListResponse
  property_count: 2
  slug: better-stack-status-page-list-response
- name: StatusPageObject
  property_count: 3
  slug: better-stack-status-page-object
- name: StatusPageSingleResponse
  property_count: 1
  slug: better-stack-status-page-single-response
- name: StatusPageUpdateRequest
  property_count: 3
  slug: better-stack-status-page-update-request
- name: TeamMemberAttributes
  property_count: 5
  slug: better-stack-team-member-attributes
- name: TeamMemberInviteRequest
  property_count: 2
  slug: better-stack-team-member-invite-request
- name: TeamMemberListResponse
  property_count: 2
  slug: better-stack-team-member-list-response
- name: TeamMemberObject
  property_count: 3
  slug: better-stack-team-member-object
- name: TeamMemberSingleResponse
  property_count: 1
  slug: better-stack-team-member-single-response
json_structures:
- name: Better Stack Availability Response Structure
  property_count: 1
  slug: better-stack-availability-response-structure
- name: Better Stack Heartbeat Attributes Structure
  property_count: 12
  slug: better-stack-heartbeat-attributes-structure
- name: Better Stack Heartbeat Create Request Structure
  property_count: 7
  slug: better-stack-heartbeat-create-request-structure
- name: Better Stack Heartbeat List Response Structure
  property_count: 2
  slug: better-stack-heartbeat-list-response-structure
- name: Better Stack Heartbeat Object Structure
  property_count: 3
  slug: better-stack-heartbeat-object-structure
- name: Better Stack Heartbeat Single Response Structure
  property_count: 1
  slug: better-stack-heartbeat-single-response-structure
- name: Better Stack Heartbeat Update Request Structure
  property_count: 3
  slug: better-stack-heartbeat-update-request-structure
- name: Better Stack Incident Attributes Structure
  property_count: 10
  slug: better-stack-incident-attributes-structure
- name: Better Stack Incident Create Request Structure
  property_count: 5
  slug: better-stack-incident-create-request-structure
- name: Better Stack Incident List Response Structure
  property_count: 2
  slug: better-stack-incident-list-response-structure
- name: Better Stack Incident Object Structure
  property_count: 3
  slug: better-stack-incident-object-structure
- name: Better Stack Incident Single Response Structure
  property_count: 1
  slug: better-stack-incident-single-response-structure
- name: Better Stack Monitor Attributes Structure
  property_count: 17
  slug: better-stack-monitor-attributes-structure
- name: Better Stack Monitor Create Request Structure
  property_count: 11
  slug: better-stack-monitor-create-request-structure
- name: Better Stack Monitor List Response Structure
  property_count: 2
  slug: better-stack-monitor-list-response-structure
- name: Better Stack Monitor Object Structure
  property_count: 3
  slug: better-stack-monitor-object-structure
- name: Better Stack Monitor Single Response Structure
  property_count: 1
  slug: better-stack-monitor-single-response-structure
- name: Better Stack Monitor Update Request Structure
  property_count: 8
  slug: better-stack-monitor-update-request-structure
- name: Better Stack Pagination Structure
  property_count: 4
  slug: better-stack-pagination-structure
- name: Better Stack Policy Attributes Structure
  property_count: 7
  slug: better-stack-policy-attributes-structure
- name: Better Stack Policy Create Request Structure
  property_count: 3
  slug: better-stack-policy-create-request-structure
- name: Better Stack Policy List Response Structure
  property_count: 2
  slug: better-stack-policy-list-response-structure
- name: Better Stack Policy Object Structure
  property_count: 3
  slug: better-stack-policy-object-structure
- name: Better Stack Policy Single Response Structure
  property_count: 1
  slug: better-stack-policy-single-response-structure
- name: Better Stack Policy Step Structure
  property_count: 2
  slug: better-stack-policy-step-structure
- name: Better Stack Policy Update Request Structure
  property_count: 3
  slug: better-stack-policy-update-request-structure
- name: Better Stack Response Times Response Structure
  property_count: 1
  slug: better-stack-response-times-response-structure
- name: Better Stack Status Page Attributes Structure
  property_count: 9
  slug: better-stack-status-page-attributes-structure
- name: Better Stack Status Page Create Request Structure
  property_count: 5
  slug: better-stack-status-page-create-request-structure
- name: Better Stack Status Page List Response Structure
  property_count: 2
  slug: better-stack-status-page-list-response-structure
- name: Better Stack Status Page Object Structure
  property_count: 3
  slug: better-stack-status-page-object-structure
- name: Better Stack Status Page Single Response Structure
  property_count: 1
  slug: better-stack-status-page-single-response-structure
- name: Better Stack Status Page Update Request Structure
  property_count: 3
  slug: better-stack-status-page-update-request-structure
- name: Better Stack Team Member Attributes Structure
  property_count: 5
  slug: better-stack-team-member-attributes-structure
- name: Better Stack Team Member Invite Request Structure
  property_count: 2
  slug: better-stack-team-member-invite-request-structure
- name: Better Stack Team Member List Response Structure
  property_count: 2
  slug: better-stack-team-member-list-response-structure
- name: Better Stack Team Member Object Structure
  property_count: 3
  slug: better-stack-team-member-object-structure
- name: Better Stack Team Member Single Response Structure
  property_count: 1
  slug: better-stack-team-member-single-response-structure
jsonld:
- class_count: 43
  name: Better Stack Context
  property_count: 48
  slug: better-stack-context
layout: provider
modified: '2026-05-19'
name: Better Stack
nav: Providers
network: true
overview: 'Better Stack publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Escalation Policies API, Heartbeats API, Incidents API, and 3 more. Tagged areas include Incidents, Logs, Monitoring, Platform, and Status.


  The Better Stack catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Better Stack''s developer surface includes authentication, developer portal, getting-started guide, pricing, engineering blog, changelog, and 11 more developer resources.'
plans:
- name: Better Stack Plans Pricing
  plan_count: 3
  slug: better-stack-plans-pricing
random_paper: 33
rate_limits:
- limit_count: 5
  name: Better Stack Rate Limits
  slug: better-stack-rate-limits
rules:
- name: Better Stack API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: better-stack-jsonschema-spectral-rules
- name: Better Stack API Rules
  rule_count: 43
  severity_counts:
    error: 13
    hint: 0
    info: 7
    warn: 23
  slug: better-stack-spectral-rules
score:
  band: thin
  composite: 41.7
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 23.9
    developer_ergonomics: 37.0
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 44.7
  previous_composite: 41.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 6
      marker_coverage: 100.0
      total: 6
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/better-stack/refs/heads/main/screenshots/better-stack-2026-06-20T173204.png
security:
- kind: authentication
  name: Better Stack Authentication
  slug: better-stack-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Better Stack Domain Security
  slug: better-stack-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Better Stack Vulnerability Disclosure
  slug: better-stack-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Better Stack Trust Center
  slug: better-stack-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: better-stack
tags:
- Incidents
- Logs
- Monitoring
- Platform
- Status
- Uptime
- Observability
- On-Call
- Heartbeats
use_cases:
- description: Monitor public websites and APIs for availability and alert on-call engineers when they go down.
  name: Website Uptime Monitoring
- description: Continuously verify that REST APIs return expected status codes and response times.
  name: API Health Checking
- description: Use heartbeats to ensure scheduled tasks run on time and alert when they fail to check in.
  name: Cron Job Monitoring
- description: Automate incident creation, on-call notifications, and resolution workflows to reduce MTTR.
  name: Incident Response Automation
- description: Publish status pages that automatically reflect the real-time health of monitored services.
  name: Customer-Facing Status Communication
- description: Aggregate logs, metrics, and traces in a single platform for full-stack observability.
  name: Infrastructure Observability
website: https://betterstack.com/docs/
---
