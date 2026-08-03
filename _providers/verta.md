---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.9
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 179
  human_in_the_loop: 0
  name: Verta Agentic Access
  operation_count: 264
  slug: verta-agentic-access
  summary_line: 264 operations · 179 acting
api_count: 11
apis:
- description: The AuthzService API from Verta — 4 operation(s) for authzservice.
  name: Verta AuthzService API
  slug: verta-authzservice-api
- description: The DatasetService API from Verta — 17 operation(s) for datasetservice.
  name: Verta DatasetService API
  slug: verta-datasetservice-api
- description: The ExperimentRunService API from Verta — 60 operation(s) for experimentrunservice.
  name: Verta ExperimentRunService API
  slug: verta-experimentrunservice-api
- description: The ExperimentService API from Verta — 25 operation(s) for experimentservice.
  name: Verta ExperimentService API
  slug: verta-experimentservice-api
- description: The MonitoredEntityService API from Verta — 4 operation(s) for monitoredentityservice.
  name: Verta MonitoredEntityService API
  slug: verta-monitoredentityservice-api
- description: The ProjectService API from Verta — 32 operation(s) for projectservice.
  name: Verta ProjectService API
  slug: verta-projectservice-api
- description: The RegistryService API from Verta — 31 operation(s) for registryservice.
  name: Verta RegistryService API
  slug: verta-registryservice-api
- description: The SCIMConfigurationService API from Verta — 1 operation(s) for scimconfigurationservice.
  name: Verta SCIMConfigurationService API
  slug: verta-scimconfigurationservice-api
- description: The StageService API from Verta — 9 operation(s) for stageservice.
  name: Verta StageService API
  slug: verta-stageservice-api
- description: The UACService API from Verta — 13 operation(s) for uacservice.
  name: Verta UACService API
  slug: verta-uacservice-api
- description: The VersioningService API from Verta — 40 operation(s) for versioningservice.
  name: Verta VersioningService API
  slug: verta-versioningservice-api
artifact_total: 14
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/verta-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/verta-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/verta-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/verta-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/verta-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/verta-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/verta-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/verta-changelog.yml
- group: build
  title: ''
  type: Packages
  url: packages/verta-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/verta-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/verta-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/verta-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: docs
  title: ''
  type: Documentation
  url: https://docs.verta.ai/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/VertaAI
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/VertaAI/modeldb
created: '2026-07-17'
description: Verta was an MLOps model-management, experiment-tracking, and model-registry platform (verta.ai) acquired by Cloudera on 2024-06-03; verta.ai now redirects to Cloudera Machine Learning. Its open-source core, ModelDB (Apache-2.0, github.com/VertaAI/modeldb), remains actively maintained and provides ML model versioning, metadata management, and experiment tracking. The REST API is a grpc-gateway transcoding of the ModelDB and UAC gRPC services — 11 services and 264 operations served under /v1 — covering projects, experiments, experiment runs, datasets, a model registry, Git-style versioning, deployment stages, monitoring, and SCIM/UAC access control.
image: https://github.com/VertaAI.png
layout: provider
mcp_servers:
- description: ''
  name: verta-mcp.yml
  slug: verta-mcpyml
modified: '2026-07-21'
name: Verta
nav: Providers
network: true
overview: 'Verta publishes 11 APIs on the [APIs.io](https://apis.io/) network, including AuthzService API, DatasetService API, ExperimentRunService API, and 8 more. Tagged areas include MLOps, Machine Learning, Model Management, Experiment Tracking, and Model Registry.


  Verta''s developer surface includes authentication, changelog, documentation, and 13 more developer resources.'
random_paper: 71
score:
  band: emerging
  composite: 26.3
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 32.3
    developer_ergonomics: 29.9
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 21.1
  previous_composite: 26.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: derived
    skills: derived
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: authentication
  name: Verta Authentication
  slug: verta-authentication
  summary_line: custom · 0 schemes
slug: verta
tags:
- MLOps
- Machine Learning
- Model Management
- Experiment Tracking
- Model Registry
- Model Versioning
- Metadata
- Open Source
- Company
---
