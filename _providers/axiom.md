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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: true
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.9
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 52
  human_in_the_loop: 0
  name: Axiom Agentic Access
  operation_count: 88
  slug: axiom-agentic-access
  summary_line: 88 operations · 52 acting
api_count: 15
apis:
- baseURL: https://api.axiom.co
  baseurl_source: declared
  description: The Annotations API from Axiom — 2 operation(s) for annotations.
  name: Axiom Annotations API
  slug: axiom-annotations-api
- baseURL: https://api.axiom.co
  baseurl_source: declared
  description: The Dashboards API from Axiom — 2 operation(s) for dashboards.
  name: Axiom Dashboards API
  slug: axiom-dashboards-api
- baseURL: https://api.axiom.co
  baseurl_source: declared
  description: The Datasets API from Axiom — 15 operation(s) for datasets.
  name: Axiom Datasets API
  slug: axiom-datasets-api
- baseURL: https://api.axiom.co
  baseurl_source: declared
  description: The Edge API from Axiom — 3 operation(s) for edge.
  name: Axiom Edge API
  slug: axiom-edge-api
- baseURL: https://api.axiom.co
  baseurl_source: declared
  description: The Groups API from Axiom — 2 operation(s) for groups.
  name: Axiom Groups API
  slug: axiom-groups-api
- baseURL: https://api.axiom.co
  baseurl_source: declared
  description: The Mapfields API from Axiom — 1 operation(s) for mapfields.
  name: Axiom Mapfields API
  slug: axiom-mapfields-api
- baseURL: https://api.axiom.co
  baseurl_source: declared
  description: The Monitors API from Axiom — 3 operation(s) for monitors.
  name: Axiom Monitors API
  slug: axiom-monitors-api
- baseURL: https://api.axiom.co
  baseurl_source: declared
  description: The Notifiers API from Axiom — 2 operation(s) for notifiers.
  name: Axiom Notifiers API
  slug: axiom-notifiers-api
- baseURL: https://api.axiom.co
  baseurl_source: declared
  description: The Orgs API from Axiom — 3 operation(s) for orgs.
  name: Axiom Orgs API
  slug: axiom-orgs-api
- baseURL: https://api.axiom.co
  baseurl_source: declared
  description: The Roles API from Axiom — 2 operation(s) for roles.
  name: Axiom Roles API
  slug: axiom-roles-api
- baseURL: https://api.axiom.co
  baseurl_source: declared
  description: The Starred API from Axiom — 2 operation(s) for starred.
  name: Axiom Starred API
  slug: axiom-starred-api
- baseURL: https://api.axiom.co
  baseurl_source: declared
  description: The Tokens API from Axiom — 2 operation(s) for tokens.
  name: Axiom Tokens API
  slug: axiom-tokens-api
- baseURL: https://api.axiom.co
  baseurl_source: declared
  description: The Users API from Axiom — 4 operation(s) for users.
  name: Axiom Users API
  slug: axiom-users-api
- baseURL: https://api.axiom.co
  baseurl_source: declared
  description: The Views API from Axiom — 2 operation(s) for views.
  name: Axiom Views API
  slug: axiom-views-api
- baseURL: https://api.axiom.co
  baseurl_source: declared
  description: The Virtualfields API from Axiom — 2 operation(s) for virtualfields.
  name: Axiom Virtualfields API
  slug: axiom-virtualfields-api
artifact_total: 65
asyncapis:
- description: 'Axiom delivers monitor-triggered alerts to user-configured HTTP endpoints via the Custom Webhook Notifier. A monitor (match, threshold, or anomaly) runs a periodic query over event data, and when its '
  name: Axiom Custom Webhook Notifier
  slug: axiom-custom-webhook-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Axiom REST Annotations API
  slug: open-axiom-annotations-api
- collection_type: open
  name: Axiom REST Annotations Dashboards API
  slug: open-axiom-dashboards-api
- collection_type: open
  name: Axiom REST Annotations Datasets API
  slug: open-axiom-datasets-api
- collection_type: open
  name: Axiom REST Annotations Edge API
  slug: open-axiom-edge-api
- collection_type: open
  name: Axiom REST Annotations Groups API
  slug: open-axiom-groups-api
- collection_type: open
  name: Axiom REST Annotations Mapfields API
  slug: open-axiom-mapfields-api
- collection_type: open
  name: Axiom REST Annotations Monitors API
  slug: open-axiom-monitors-api
- collection_type: open
  name: Axiom REST Annotations Notifiers API
  slug: open-axiom-notifiers-api
- collection_type: open
  name: Axiom REST Annotations Orgs API
  slug: open-axiom-orgs-api
- collection_type: open
  name: Axiom REST Annotations Roles API
  slug: open-axiom-roles-api
- collection_type: open
  name: Axiom REST Annotations Starred API
  slug: open-axiom-starred-api
- collection_type: open
  name: Axiom REST Annotations Tokens API
  slug: open-axiom-tokens-api
- collection_type: open
  name: Axiom REST Annotations Users API
  slug: open-axiom-users-api
- collection_type: open
  name: Axiom REST Annotations Views API
  slug: open-axiom-views-api
- collection_type: open
  name: Axiom REST Annotations Virtualfields API
  slug: open-axiom-virtualfields-api
- collection_type: open
  name: Axiom REST API
  slug: open-axiom
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/axiom-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/axiom-domain-security.yml
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/axiomhq/skills
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/axiomhq
- group: start
  title: ''
  type: Portal
  url: https://axiom.co/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.axiom.co
- group: company
  title: ''
  type: Blog
  url: https://axiom.co/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/axiomhq
- group: commercial
  title: ''
  type: TermsOfService
  url: https://axiom.co/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://axiom.co/privacy
- group: start
  title: ''
  type: Signup
  url: https://app.axiom.co/register
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
created: '2024-01-15'
description: Axiom is a serverless log management and analytics platform that provides real-time insights into structured and unstructured data with fast querying capabilities for logs, events, and telemetry data.
features:
- description: Manage logs without managing servers or storage infrastructure.
  name: Serverless Log Management
- description: Query billions of events in seconds with APL (Axiom Processing Language).
  name: Real-Time Querying
- description: Organize data into datasets with role-based access control.
  name: Dataset Organization
- description: Create monitors with alert notifications to Slack, PagerDuty, and email.
  name: Monitors and Alerts
- description: Native OTLP ingestion for logs, metrics, and traces.
  name: OpenTelemetry Native
- description: Store data indefinitely with query-optimized cold storage.
  name: Endless Retention
- description: Build and share monitoring dashboards with rich visualization options.
  name: Dashboards
- description: Mark events like deployments on dashboards for correlation analysis.
  name: Annotations
finops:
- name: Axiom Finops
  service_category: API
  slug: axiom-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/axiom.png
integrations:
- description: Official Vercel integration for log drains and deployment tracking.
  name: Vercel
- description: Ingest OTLP telemetry from any OTel-compatible source.
  name: OpenTelemetry
- description: Forward Lambda logs to Axiom via log subscriptions.
  name: AWS Lambda
- description: Collect pod and node logs using the Axiom DaemonSet or Helm chart.
  name: Kubernetes
- description: Send CI/CD logs from GitHub Actions to Axiom for analysis.
  name: GitHub Actions
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-29'
name: Axiom
nav: Providers
network: true
overview: 'Axiom publishes 15 APIs on the [APIs.io](https://apis.io/) network, including Annotations API, Dashboards API, Datasets API, and 12 more. Tagged areas include Analytics, Log Management, Logging, Observability, and Real-Time.


  The Axiom catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Axiom''s developer surface includes developer portal, engineering blog, signup flow, pricing, documentation, getting-started guide, and 9 more developer resources.'
plans:
- name: Axiom Plans Pricing
  plan_count: 3
  slug: axiom-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 5
  name: Axiom Rate Limits
  slug: axiom-rate-limits
rules:
- effective_rule_count: 30
  extends:
  - spectral:asyncapi
  name: Axiom API Rules
  rule_count: 3
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 1
  slug: axiom-asyncapi-spectral-rules
score:
  band: developing
  composite: 45.4
  coverage:
    artifact_dirs: 12
    catalog_earned: 53.5
    catalog_earned_first_party: 0.0
    catalog_gap: 61.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 13.6
    contract_quality: 51.0
    developer_ergonomics: 40.5
    discoverability: 74.1
    governance: 13.6
    operational_transparency: 26.3
  previous_composite: 45.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 16
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/axiom/refs/heads/main/screenshots/axiom-2026-06-20T172818.png
security:
- kind: domain-security
  name: Axiom Domain Security
  slug: axiom-domain-security
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
slug: axiom
tags:
- Analytics
- Log Management
- Logging
- Observability
- Real-Time
- Serverless
use_cases:
- description: Centralize application logs for debugging and error analysis.
  name: Application Logging
- description: Monitor CI/CD pipelines, deployments, and infrastructure health.
  name: DevOps Observability
- description: Analyze audit logs and detect security anomalies.
  name: Security Analytics
- description: Monitor Vercel, Cloudflare, and other edge function execution.
  name: Edge Function Monitoring
- description: Trace requests across services using OpenTelemetry OTLP.
  name: Distributed Tracing
website: https://axiom.co/
---
