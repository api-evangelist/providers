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
  trial: true
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
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.2
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 37
  human_in_the_loop: 3
  name: Mezmo Agentic Access
  operation_count: 62
  slug: mezmo-agentic-access
  summary_line: 62 operations · 37 acting · 3 human-in-the-loop
api_count: 7
apis:
- description: Open-source Rust log collection agent (logdna-agent-v2). Tails files, journald, and Kubernetes pod logs and ships to Mezmo's ingestion endpoint. MIT-licensed.
  name: Mezmo Agent (logdna-agent-v2)
  slug: mezmo-agent
- description: 'Mezmo''s open-source agentic orchestration framework. Apache 2.0 Rust framework for composing AI agents from declarative TOML config, with MCP tool integration, RAG pipelines (Qdrant, Bedrock KB), and '
  name: AURA Agent Framework
  slug: mezmo-aura
- description: The AuditEvents API from Mezmo — 1 operation(s) for auditevents.
  name: Mezmo AuditEvents API
  slug: mezmo-auditevents-api
- description: The Classification API from Mezmo — 3 operation(s) for classification.
  name: Mezmo Classification API
  slug: mezmo-classification-api
- description: The Deployments API from Mezmo — 2 operation(s) for deployments.
  name: Mezmo Deployments API
  slug: mezmo-deployments-api
- description: The Destinations API from Mezmo — 2 operation(s) for destinations.
  name: Mezmo Destinations API
  slug: mezmo-destinations-api
- description: The EdgeClients API from Mezmo — 2 operation(s) for edgeclients.
  name: Mezmo EdgeClients API
  slug: mezmo-edgeclients-api
- description: The Exclusions API from Mezmo — 2 operation(s) for exclusions.
  name: Mezmo Exclusions API
  slug: mezmo-exclusions-api
- description: Historical log export
  name: Mezmo Export API
  slug: mezmo-export-api
- description: The Heartbeats API from Mezmo — 1 operation(s) for heartbeats.
  name: Mezmo Heartbeats API
  slug: mezmo-heartbeats-api
- description: Log line ingestion
  name: Mezmo Logs API
  slug: mezmo-logs-api
- description: The Metrics API from Mezmo — 1 operation(s) for metrics.
  name: Mezmo Metrics API
  slug: mezmo-metrics-api
- description: The Pipelines API from Mezmo — 3 operation(s) for pipelines.
  name: Mezmo Pipelines API
  slug: mezmo-pipelines-api
- description: Preset alert configuration
  name: Mezmo PresetAlerts API
  slug: mezmo-presetalerts-api
- description: The Processors API from Mezmo — 2 operation(s) for processors.
  name: Mezmo Processors API
  slug: mezmo-processors-api
- description: The Sources API from Mezmo — 2 operation(s) for sources.
  name: Mezmo Sources API
  slug: mezmo-sources-api
- description: The Suspension API from Mezmo — 4 operation(s) for suspension.
  name: Mezmo Suspension API
  slug: mezmo-suspension-api
- description: The Tasks API from Mezmo — 2 operation(s) for tasks.
  name: Mezmo Tasks API
  slug: mezmo-tasks-api
artifact_total: 77
collections:
- collection_type: postman
  name: Mezmo Alerts Archiving API
  slug: postman-mezmo-archiving-api
- collection_type: postman
  name: Mezmo Alerts Archiving AuditEvents API
  slug: postman-mezmo-auditevents-api
- collection_type: postman
  name: Mezmo Alerts Archiving Classification API
  slug: postman-mezmo-classification-api
- collection_type: postman
  name: Mezmo Alerts Archiving Deployments API
  slug: postman-mezmo-deployments-api
- collection_type: postman
  name: Mezmo Alerts Archiving Destinations API
  slug: postman-mezmo-destinations-api
- collection_type: postman
  name: Mezmo Alerts Archiving EdgeClients API
  slug: postman-mezmo-edgeclients-api
- collection_type: postman
  name: Mezmo Alerts Archiving Exclusions API
  slug: postman-mezmo-exclusions-api
- collection_type: postman
  name: Mezmo Alerts Archiving Export API
  slug: postman-mezmo-export-api
- collection_type: postman
  name: Mezmo Alerts Archiving Heartbeats API
  slug: postman-mezmo-heartbeats-api
- collection_type: postman
  name: Mezmo Alerts Archiving Logs API
  slug: postman-mezmo-logs-api
- collection_type: postman
  name: Mezmo Alerts Archiving Metrics API
  slug: postman-mezmo-metrics-api
- collection_type: postman
  name: Mezmo Alerts Archiving Pipelines API
  slug: postman-mezmo-pipelines-api
- collection_type: postman
  name: Mezmo Alerts Archiving PresetAlerts API
  slug: postman-mezmo-presetalerts-api
- collection_type: postman
  name: Mezmo Alerts Archiving Processors API
  slug: postman-mezmo-processors-api
- collection_type: postman
  name: Mezmo Alerts Archiving Sources API
  slug: postman-mezmo-sources-api
- collection_type: postman
  name: Mezmo Alerts Archiving Suspension API
  slug: postman-mezmo-suspension-api
- collection_type: postman
  name: Mezmo Alerts Archiving Tasks API
  slug: postman-mezmo-tasks-api
- collection_type: postman
  name: Mezmo Alerts Archiving Usage API
  slug: postman-mezmo-usage-api
- collection_type: postman
  name: Mezmo Alerts Archiving Views API
  slug: postman-mezmo-views-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Mezmo Alerts API
  slug: open-mezmo-alerts-api
- collection_type: open
  name: Mezmo Alerts Archiving API
  slug: open-mezmo-archiving-api
- collection_type: open
  name: Mezmo Alerts Archiving AuditEvents API
  slug: open-mezmo-auditevents-api
- collection_type: open
  name: Mezmo Alerts Archiving Classification API
  slug: open-mezmo-classification-api
- collection_type: open
  name: Mezmo Alerts Archiving Deployments API
  slug: open-mezmo-deployments-api
- collection_type: open
  name: Mezmo Alerts Archiving Destinations API
  slug: open-mezmo-destinations-api
- collection_type: open
  name: Mezmo Edge API
  slug: open-mezmo-edge-api
- collection_type: open
  name: Mezmo Alerts Archiving EdgeClients API
  slug: open-mezmo-edgeclients-api
- collection_type: open
  name: Mezmo Alerts Archiving Exclusions API
  slug: open-mezmo-exclusions-api
- collection_type: open
  name: Mezmo Alerts Archiving Export API
  slug: open-mezmo-export-api
- collection_type: open
  name: Mezmo Alerts Archiving Heartbeats API
  slug: open-mezmo-heartbeats-api
- collection_type: open
  name: Mezmo Ingestion Control API
  slug: open-mezmo-ingestion-control-api
- collection_type: open
  name: Mezmo Log Export API
  slug: open-mezmo-log-export-api
- collection_type: open
  name: Mezmo Log Ingestion API
  slug: open-mezmo-log-ingestion-api
- collection_type: open
  name: Mezmo Alerts Archiving Logs API
  slug: open-mezmo-logs-api
- collection_type: open
  name: Mezmo Alerts Archiving Metrics API
  slug: open-mezmo-metrics-api
- collection_type: open
  name: Mezmo Pipeline API
  slug: open-mezmo-pipeline-api
- collection_type: open
  name: Mezmo Pipeline Classification API
  slug: open-mezmo-pipeline-classification-api
- collection_type: open
  name: Mezmo Alerts Archiving Pipelines API
  slug: open-mezmo-pipelines-api
- collection_type: open
  name: Mezmo Alerts Archiving PresetAlerts API
  slug: open-mezmo-presetalerts-api
- collection_type: open
  name: Mezmo Alerts Archiving Processors API
  slug: open-mezmo-processors-api
- collection_type: open
  name: Mezmo Alerts Archiving Sources API
  slug: open-mezmo-sources-api
- collection_type: open
  name: Mezmo Alerts Archiving Suspension API
  slug: open-mezmo-suspension-api
- collection_type: open
  name: Mezmo Alerts Archiving Tasks API
  slug: open-mezmo-tasks-api
- collection_type: open
  name: Mezmo Alerts Archiving Usage API
  slug: open-mezmo-usage-api
- collection_type: open
  name: Mezmo Alerts Archiving Views API
  slug: open-mezmo-views-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/mezmo/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/mezmo-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/mezmo-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mezmo-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mezmo-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mezmo
- group: start
  title: ''
  type: Portal
  url: https://www.mezmo.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.mezmo.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.mezmo.com/log-analysis-api
- group: docs
  title: ''
  type: Documentation
  url: https://docs.mezmo.com/pipeline-api
- group: operate
  title: ''
  type: StatusPage
  url: https://status.mezmo.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.mezmo.com/changelog
- group: company
  title: ''
  type: Blog
  url: https://www.mezmo.com/blog
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/mezmo
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/logdna
- group: build
  title: ''
  type: CLI
  url: https://github.com/mezmo/cli
- group: build
  title: ''
  type: SDKs
  url: https://registry.terraform.io/providers/mezmo/mezmo/latest
- group: build
  title: ''
  type: SDKs
  url: https://github.com/logdna/terraform-provider-logdna
- group: build
  title: ''
  type: SDKs
  url: https://github.com/logdna/logdna-agent-v2
- group: build
  title: ''
  type: SDKs
  url: https://github.com/logdna/nodejs
- group: build
  title: ''
  type: SDKs
  url: https://github.com/logdna/python
- group: build
  title: ''
  type: SDKs
  url: https://github.com/logdna/logdna-rust
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/mezmo/mezmo-mcp
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/mezmo/aura
- group: build
  title: ''
  type: SDKs
  url: https://github.com/mezmo/helm-charts
- group: commercial
  title: ''
  type: Pricing
  url: https://www.mezmo.com/pricing
- group: commercial
  title: ''
  type: Plans
  url: plans/mezmo-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/mezmo-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/mezmo-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/mezmo-vocabulary.yml
- group: design
  title: ''
  type: SpectralRuleset
  url: rules/mezmo-rules.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/mezmo-context.jsonld
created: '2026-05-25'
finops:
- name: Mezmo Finops
  service_category: ''
  slug: mezmo-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mezmo.png
json_schemas:
- name: Mezmo Log Line
  property_count: 8
  slug: mezmo-log-line
- name: Mezmo Pipeline
  property_count: 10
  slug: mezmo-pipeline
jsonld:
- class_count: 30
  name: Mezmo Context
  property_count: 2
  slug: mezmo-context
layout: provider
mcp_servers:
- description: ''
  name: Mezmo MCP Server
  slug: mezmo-mcp-server
modified: '2026-05-25'
name: Mezmo
nav: Providers
network: true
overview: 'Mezmo publishes 16 APIs on the [APIs.io](https://apis.io/) network, including AuditEvents API, Classification API, Deployments API, and 13 more. Tagged areas include Observability, Logs, Telemetry, Telemetry Pipeline, and Log Management.


  The Mezmo catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Mezmo''s developer surface includes authentication, developer portal, documentation, changelog, engineering blog, CLI, pricing, and 25 more developer resources.'
plans:
- name: Mezmo Plans Pricing
  plan_count: 2
  slug: mezmo-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 4
  name: Mezmo Rate Limits
  slug: mezmo-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Mezmo API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: mezmo-jsonschema-spectral-rules
- effective_rule_count: 48
  extends:
  - spectral:oas
  name: Mezmo API Rules
  rule_count: 7
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 4
  slug: mezmo-rules
score:
  band: developing
  composite: 54.2
  coverage:
    artifact_dirs: 15
    catalog_gap: 44.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 28.8
    contract_quality: 57.6
    developer_ergonomics: 61.9
    discoverability: 55.6
    governance: 28.8
    operational_transparency: 68.4
  previous_composite: 54.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 19
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mezmo/refs/heads/main/screenshots/mezmo-2026-06-20T185318.png
security:
- kind: authentication
  name: Mezmo Authentication
  slug: mezmo-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Mezmo Domain Security
  slug: mezmo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Mezmo Trust Center
  slug: mezmo-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, HIPAA, GDPR
slug: mezmo
tags:
- Observability
- Logs
- Telemetry
- Telemetry Pipeline
- Log Management
- Artificial Intelligence
- SRE
- OpenTelemetry
- DevOps
website: https://www.mezmo.com/
---
