---
access_model:
  confidence: high
  label: 14-day trial, pricing by quote
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  trial: true
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.5
  scored_at: '2026-09-02'
api_count: 2
apis:
- baseURL: https://{account}.logicmonitor.com/santaba/rest
  baseurl_source: declared
  description: The LogicMonitor platform API. Swagger 2.0, 220 paths, 403 operations and 743 definitions covering devices and device groups, collectors and collector groups, alerts, alert rules and escalation chains
  name: LogicMonitor REST API v3
  slug: logicmonitor
- description: A Model Context Protocol server over the LogicMonitor REST API v3, published to npm as logicmonitor-api-mcp and hosted in the LogicMonitor GitHub organization, exposing 13 resource-shaped tools for de
  name: LogicMonitor MCP Server
  slug: logicmonitor-mcp
artifact_total: 11
asyncapis:
- description: ''
  name: Logicmonitor Webhooks
  slug: logicmonitor-webhooks
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/logicmonitor/logicmonitor-api-mcp/blob/main/LICENSE
- group: company
  title: ''
  type: Website
  url: https://www.logicmonitor.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.logicmonitor.com/support
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.logicmonitor.com/support/rest-api-developers-guide/
- group: docs
  title: ''
  type: APIReference
  url: https://www.logicmonitor.com/support/rest-api-v3-swagger-documentation
- group: start
  title: ''
  type: GettingStarted
  url: https://www.logicmonitor.com/support/rest-api-developers-guide/overview/using-logicmonitors-rest-api
- group: operate
  title: ''
  type: Support
  url: https://www.logicmonitor.com/support
- group: operate
  title: ''
  type: Community
  url: https://community.logicmonitor.com/
- group: company
  title: ''
  type: Blog
  url: https://www.logicmonitor.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/logicmonitor
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/logicmonitor
- group: commercial
  title: ''
  type: Pricing
  url: https://www.logicmonitor.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.logicmonitor.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.logicmonitor.com/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.logicmonitor.com/legal/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.logicmonitor.com/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/logicmonitor-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/logicmonitor-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/logicmonitor-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/logicmonitor-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/logicmonitor-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/logicmonitor-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/logicmonitor-cli.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/logicmonitor-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/logicmonitor-trust-center.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/logicmonitor-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/logicmonitor-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/logicmonitor-authentication.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/logicmonitor-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/logicmonitor-webhooks.yml
created: '2026-03-27'
description: LogicMonitor is an AI-powered hybrid observability and AIOps platform that monitors infrastructure, cloud and multi-cloud estates, containers, networks, databases, storage, logs, traces, websites and internet performance from a single SaaS portal, with an agentic AIOps layer (Edwin AI) for event correlation and governed remediation. Everything the portal does is addressable through the LogicMonitor REST API v3 — a published Swagger 2.0 contract of 220 paths and 403 operations covering devices, device groups, collectors, alerts, scheduled downtime, dashboards, websites, reports, log pipelines, cost optimization and user administration, with per-operation x-minimum-permissions metadata. First-party Python, Go, PowerShell and Terraform tooling wraps it, and telemetry can be pushed in over OpenTelemetry OTLP, OpenMetrics/Prometheus exposition, and the Push Metrics and LM Logs ingestion APIs.
finops:
- name: Logicmonitor Finops
  service_category: API
  slug: logicmonitor-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/logicmonitor.png
layout: provider
mcp_servers:
- description: 'An MCP server over the LogicMonitor REST API v3, published to npm as logicmonitor-api-mcp and hosted in the logicmonitor GitHub organization. It is NOT a vendor-hosted remote endpoint: there is no URL'
  name: LogicMonitor MCP Server
  slug: logicmonitor-mcp-server
modified: '2026-08-29'
name: LogicMonitor
nav: Providers
network: true
overview: 'LogicMonitor publishes 1 API on the [APIs.io](https://apis.io/) network: REST API v3. Tagged areas include AIOps, Monitoring, Observability, Infrastructure, and Log Management.


  The LogicMonitor catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  LogicMonitor''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 24 more developer resources.'
plans:
- name: Logicmonitor Plans Pricing
  plan_count: 0
  slug: logicmonitor-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 20
  name: Logicmonitor Rate Limits
  slug: logicmonitor-rate-limits
scopes:
- name: Logicmonitor Scopes
  scope_count: 0
  slug: logicmonitor-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 58.0
  coverage:
    artifact_dirs: 23
    catalog_gap: 68.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 1.6
  facets:
    access_clarity: 68.4
    commercial_clarity: 68.4
    contract_governance: 18.2
    contract_quality: 48.1
    developer_ergonomics: 73.2
    discoverability: 59.3
    governance: 18.2
    operational_transparency: 73.7
  previous_composite: 56.4
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/logicmonitor/refs/heads/main/screenshots/logicmonitor-2026-06-20T184653.png
security:
- kind: authentication
  name: Logicmonitor Authentication
  slug: logicmonitor-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Logicmonitor Domain Security
  slug: logicmonitor-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Logicmonitor Trust Center
  slug: logicmonitor-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, HIPAA, FedRAMP, GDPR
slug: logicmonitor
tags:
- AIOps
- Monitoring
- Observability
- Infrastructure
- Log Management
- Network Monitoring
- Cloud Monitoring
- Alerting
- Synthetic Monitoring
- OpenTelemetry
- ITOps
website: https://www.logicmonitor.com
---
