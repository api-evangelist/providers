---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
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
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.0
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Sumologic Agentic Access
  operation_count: 27
  slug: sumologic-agentic-access
  summary_line: 27 operations · 15 acting
api_count: 25
apis:
- description: Sumo Logic REST API for the US1 deployment. Endpoint surface spans search jobs, dashboards, metrics, monitors, content management, roles, users, collectors, connections, partitions, lookup tables, SAM
  name: Sumo Logic REST API (US1)
  slug: rest-us1
- description: Sumo Logic REST API for the US2 deployment.
  name: Sumo Logic REST API (US2)
  slug: rest-us2
- description: Sumo Logic REST API for the EU (Ireland) deployment.
  name: Sumo Logic REST API (EU)
  slug: rest-eu
- description: Sumo Logic REST API for the AU (Australia) deployment.
  name: Sumo Logic REST API (AU)
  slug: rest-au
- description: Sumo Logic REST API for the DE (Germany) deployment.
  name: Sumo Logic REST API (DE)
  slug: rest-de
- description: Sumo Logic REST API for the JP (Japan) deployment.
  name: Sumo Logic REST API (JP)
  slug: rest-jp
- description: Sumo Logic REST API for the CA (Canada) deployment.
  name: Sumo Logic REST API (CA)
  slug: rest-ca
- description: Sumo Logic REST API for the IN (India) deployment.
  name: Sumo Logic REST API (IN)
  slug: rest-in
- description: Sumo Logic REST API for the KR (South Korea) deployment.
  name: Sumo Logic REST API (KR)
  slug: rest-kr
- description: Sumo Logic REST API for the FED deployment, serving US Federal customers (FedRAMP).
  name: Sumo Logic REST API (FED)
  slug: rest-fed
- description: Asynchronous search job API used to launch log searches, poll for state, retrieve messages and aggregate records, and pause/cancel running jobs.
  name: Sumo Logic Search Job API
  slug: search-job
- description: Endpoints for creating, retrieving, updating, and deleting dashboards and dashboard panels.
  name: Sumo Logic Dashboards API
  slug: dashboards
- description: Monitor management API for creating logs and metrics monitors, configuring conditions, and routing to notification channels including email, Slack, PagerDuty, and webhook.
  name: Sumo Logic Monitors API
  slug: monitors
- description: Endpoints for managing installed and hosted collectors, their sources, and configuration.
  name: Sumo Logic Collectors API
  slug: collectors
- description: Asynchronous import, export, copy, move, and delete operations across the user content hierarchy (folders, dashboards, searches, lookup tables).
  name: Sumo Logic Content Management API
  slug: content
- description: Cloud SIEM API for managing entities, insights, signals, and rules used for security analytics and threat detection.
  name: Sumo Logic Cloud SIEM API
  slug: cloud-siem
- description: Cloud SOAR API for security orchestration, automation, and response playbooks, incidents, and actions.
  name: Sumo Logic Cloud SOAR API
  slug: cloud-soar
- description: Outbound webhook surface for Sumo Logic alert delivery. Sumo Logic POSTs JSON payloads to user-configured receivers when monitors trigger or recover. Documented connection types include Generic Webhoo
  name: Sumo Logic Webhook Connections
  slug: webhooks
- description: The Collectors API from Sumo Logic — 2 operation(s) for collectors.
  name: Sumo Logic Collectors API
  slug: sumologic-collectors-api
- description: The Content API from Sumo Logic — 2 operation(s) for content.
  name: Sumo Logic Content API
  slug: sumologic-content-api
- description: The Dashboards API from Sumo Logic — 2 operation(s) for dashboards.
  name: Sumo Logic Dashboards API
  slug: sumologic-dashboards-api
- description: The Monitors API from Sumo Logic — 1 operation(s) for monitors.
  name: Sumo Logic Monitors API
  slug: sumologic-monitors-api
- description: The Roles API from Sumo Logic — 1 operation(s) for roles.
  name: Sumo Logic Roles API
  slug: sumologic-roles-api
- description: The Search Jobs API from Sumo Logic — 4 operation(s) for search jobs.
  name: Sumo Logic Search Jobs API
  slug: sumologic-search-jobs-api
- description: The Users API from Sumo Logic — 2 operation(s) for users.
  name: Sumo Logic Users API
  slug: sumologic-users-api
artifact_total: 35
asyncapis:
- description: 'AsyncAPI description of Sumo Logic''s outbound webhook surfaces. Sumo Logic delivers alert and recovery notifications via HTTP POST to user-configured webhook connections. Each connection type targets '
  name: Sumo Logic Webhook Connections
  slug: sumologic-asyncapi
collections:
- collection_type: open
  name: Sumo Logic REST API
  slug: open-sumologic
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sumologic-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/sumologic-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sumologic-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sumologic-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sumo-logic
- group: company
  title: ''
  type: Website
  url: https://www.sumologic.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.sumologic.com/help/docs/api/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/SumoLogic
- group: operate
  title: ''
  type: Status
  url: https://status.sumologic.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/sumologic-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sumologic-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/sumologic-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.sumologic.com/blog/
created: '2026-05-23'
description: Sumo Logic is a cloud-native log analytics, observability, and security platform. The Sumo Logic platform ingests logs, metrics, and traces from cloud and on-premise sources and exposes a deep REST API covering search jobs, dashboards, metrics, monitors and alerts, content management, roles, users, service accounts, collectors, connections, partitions, lookup tables, SAML configuration, traces and span analytics, and Cloud SIEM / Cloud SOAR. Sumo Logic operates regional deployments and surfaces a deployment-specific API endpoint for each one (us1, us2, eu, au, ca, de, jp, in, kr, and fed for US public sector). Authentication is via Access ID and Access Key (HTTP Basic) or bearer-style service account credentials.
finops:
- name: Sumologic Finops
  service_category: API
  slug: sumologic-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sumologic.png
layout: provider
modified: '2026-05-30'
name: Sumo Logic
nav: Providers
network: true
overview: 'Sumo Logic publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Webhook Connections, Collectors API, Content API, and 5 more. Tagged areas include Logs, Observability, SIEM, SOAR, and Metrics.


  The Sumo Logic catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Sumo Logic''s developer surface includes authentication, documentation, GitHub presence, status page, engineering blog, and 8 more developer resources.'
plans:
- name: Sumologic Plans Pricing
  plan_count: 1
  slug: sumologic-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 2
  name: Sumologic Rate Limits
  slug: sumologic-rate-limits
rules:
- name: Sumo Logic API Rules
  rule_count: 9
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 7
  slug: sumologic-asyncapi-spectral-rules
score:
  band: developing
  composite: 43.2
  delta: -3.5
  facets:
    commercial_clarity: 36.8
    contract_quality: 63.5
    developer_ergonomics: 21.7
    discoverability: 64.8
    governance: 47.9
    operational_transparency: 26.3
  previous_composite: 46.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sumologic/refs/heads/main/screenshots/sumologic-2026-06-20T194646.png
security:
- kind: authentication
  name: Sumologic Authentication
  slug: sumologic-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Sumologic Domain Security
  slug: sumologic-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Sumologic Trust Center
  slug: sumologic-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, HIPAA, FedRAMP, GDPR, CSA STAR
slug: sumologic
tags:
- Logs
- Observability
- SIEM
- SOAR
- Metrics
- Cloud Security
- Log Analytics
website: https://www.sumologic.com/
---
