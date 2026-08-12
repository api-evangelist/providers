---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 45.9
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Axiom Controller Agentic Access
  operation_count: 5
  slug: axiom-controller-agentic-access
  summary_line: 5 operations · 5 acting
api_count: 4
apis:
- description: API for querying and analyzing data stored in Axiom datasets using APL (Axiom Processing Language).
  name: Axiom Query API
  slug: axiom-query-api
- description: The Datasets API from Axiom Controller — 1 operation(s) for datasets.
  name: Axiom Controller Datasets API
  slug: axiom-controller-datasets-api
- description: The Edge API from Axiom Controller — 3 operation(s) for edge.
  name: Axiom Controller Edge API
  slug: axiom-controller-edge-api
- description: The Ingest API from Axiom Controller — 1 operation(s) for ingest.
  name: Axiom Controller Ingest API
  slug: axiom-controller-ingest-api
artifact_total: 35
collections:
- collection_type: open
  name: Axiom Ingest Controller API
  slug: open-axiom-controller
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/axiom-controller-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/axiom-controller-domain-security.yml
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/axiomhq/skills
- group: start
  title: ''
  type: Portal
  url: https://axiom.co/
- group: auth
  title: ''
  type: Authentication
  url: https://axiom.co/docs/restapi/token
- group: operate
  title: ''
  type: StatusPage
  url: https://status.axiom.co
- group: company
  title: ''
  type: Blog
  url: https://axiom.co/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://axiom.co/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://axiom.co/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/axiomhq
- group: commercial
  title: ''
  type: Pricing
  url: https://axiom.co/pricing
- group: docs
  title: ''
  type: Documentation
  url: https://axiom.co/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://axiom.co/docs/get-started
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/axiomhq/mcp-server-axiom
created: '2024-01-01'
description: Axiom is a cloud-native observability platform providing APIs for ingesting, querying, and managing telemetry data including logs, traces, and metrics with support for datasets, monitors, and organization management.
features:
- description: Ingest logs from any source at massive scale with compression.
  name: Log Ingestion
- description: Query telemetry data using Axiom Processing Language (APL), inspired by KQL.
  name: APL Query Language
- description: Organize telemetry data in datasets for granular access control and retention.
  name: Dataset Management
- description: Set up threshold-based and anomaly-detection monitors with PagerDuty/Slack integrations.
  name: Monitors and Alerts
- description: Native support for OpenTelemetry traces, metrics, and logs via OTLP.
  name: OpenTelemetry Support
- description: Store telemetry data for extended periods at low cost with queryable archives.
  name: Long-Term Retention
- description: Build custom dashboards with rich visualization for monitoring application health.
  name: Dashboards
finops:
- name: Axiom Controller Finops
  service_category: API
  slug: axiom-controller-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/axiom-controller.png
integrations:
- description: Ingest OTLP data from any OpenTelemetry-compatible source.
  name: OpenTelemetry
- description: Built-in Vercel log drain integration for edge function and deployment logs.
  name: Vercel
- description: Forward CloudWatch logs to Axiom via Lambda log forwarder.
  name: AWS CloudWatch
- description: Deploy Axiom Helm charts to collect Kubernetes logs and metrics.
  name: Kubernetes
- description: Send CI/CD pipeline logs to Axiom from GitHub Actions workflows.
  name: GitHub Actions
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: Axiom Controller
nav: Providers
network: true
overview: 'Axiom Controller publishes 3 APIs on the [APIs.io](https://apis.io/) network: Datasets API, Edge API, and Ingest API. Tagged areas include Analytics, Cloud Native, Logging, Monitoring, and Observability.


  Axiom Controller''s developer surface includes developer portal, authentication, engineering blog, pricing, documentation, getting-started guide, and 8 more developer resources.'
plans:
- name: Axiom Controller Plans Pricing
  plan_count: 3
  slug: axiom-controller-plans-pricing
random_paper: 55
rate_limits:
- limit_count: 5
  name: Axiom Controller Rate Limits
  slug: axiom-controller-rate-limits
score:
  band: developing
  composite: 43.3
  delta: -7.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 45.5
    developer_ergonomics: 56.5
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 28.9
  previous_composite: 50.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/axiom-controller/refs/heads/main/screenshots/axiom-controller-2026-06-20T172809.png
security:
- kind: domain-security
  name: Axiom Controller Domain Security
  slug: axiom-controller-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 7
skills:
- name: axiom-alerting
  slug: axiom-alerting
- name: axiom-sre
  slug: axiom-sre
- name: building-dashboards
  slug: building-dashboards
- name: controlling-costs
  slug: controlling-costs
- name: query-metrics
  slug: query-metrics
- name: spl-to-apl
  slug: spl-to-apl
- name: writing-evals
  slug: writing-evals
slug: axiom-controller
tags:
- Analytics
- Cloud Native
- Logging
- Monitoring
- Observability
- Telemetry
use_cases:
- description: Centralize application logs for debugging and troubleshooting.
  name: Application Logging
- description: Monitor infrastructure metrics and detect anomalies.
  name: Infrastructure Monitoring
- description: Analyze security logs and audit trails for threat detection.
  name: Security Analytics
- description: Trace requests across microservices with OpenTelemetry.
  name: Distributed Tracing
- description: Analyze user behavior and business events stored as structured logs.
  name: Business Analytics
website: https://axiom.co/
---
