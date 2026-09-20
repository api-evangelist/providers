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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.0
  scored_at: '2026-09-19'
agentic_access:
- acting_count: 179
  human_in_the_loop: 0
  name: Verta Agentic Access
  operation_count: 264
  slug: verta-agentic-access
  summary_line: 264 operations · 179 acting
api_count: 12
apis:
- baseURL: https://docs.verta.ai/
  baseurl_source: declared
  description: The AuthzService API from Verta — 4 operation(s) for authzservice.
  name: Verta AuthzService API
  slug: verta-authzservice-api
- baseURL: https://docs.verta.ai/
  baseurl_source: declared
  description: The DatasetService API from Verta — 17 operation(s) for datasetservice.
  name: Verta DatasetService API
  slug: verta-datasetservice-api
- baseURL: https://docs.verta.ai/
  baseurl_source: declared
  description: The ExperimentRunService API from Verta — 60 operation(s) for experimentrunservice.
  name: Verta ExperimentRunService API
  slug: verta-experimentrunservice-api
- baseURL: https://docs.verta.ai/
  baseurl_source: declared
  description: The ExperimentService API from Verta — 25 operation(s) for experimentservice.
  name: Verta ExperimentService API
  slug: verta-experimentservice-api
- baseURL: https://docs.verta.ai/
  baseurl_source: declared
  description: The MonitoredEntityService API from Verta — 4 operation(s) for monitoredentityservice.
  name: Verta MonitoredEntityService API
  slug: verta-monitoredentityservice-api
- baseURL: https://docs.verta.ai/
  baseurl_source: declared
  description: The ProjectService API from Verta — 32 operation(s) for projectservice.
  name: Verta ProjectService API
  slug: verta-projectservice-api
- baseURL: https://docs.verta.ai/
  baseurl_source: declared
  description: The RegistryService API from Verta — 31 operation(s) for registryservice.
  name: Verta RegistryService API
  slug: verta-registryservice-api
- baseURL: https://docs.verta.ai/
  baseurl_source: declared
  description: The SCIMConfigurationService API from Verta — 1 operation(s) for scimconfigurationservice.
  name: Verta SCIMConfigurationService API
  slug: verta-scimconfigurationservice-api
- baseURL: https://docs.verta.ai/
  baseurl_source: declared
  description: The StageService API from Verta — 9 operation(s) for stageservice.
  name: Verta StageService API
  slug: verta-stageservice-api
- baseURL: https://docs.verta.ai/
  baseurl_source: declared
  description: The UACService API from Verta — 13 operation(s) for uacservice.
  name: Verta UACService API
  slug: verta-uacservice-api
- baseURL: https://docs.verta.ai/
  baseurl_source: declared
  description: The VersioningService API from Verta — 40 operation(s) for versioningservice.
  name: Verta VersioningService API
  slug: verta-versioningservice-api
artifact_total: 25
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: deployment/APISync.proto AuthzService API
  slug: open-verta-authzservice-api
- collection_type: open
  name: deployment/APISync.proto AuthzService DatasetService API
  slug: open-verta-datasetservice-api
- collection_type: open
  name: deployment/APISync.proto AuthzService ExperimentRunService API
  slug: open-verta-experimentrunservice-api
- collection_type: open
  name: deployment/APISync.proto AuthzService ExperimentService API
  slug: open-verta-experimentservice-api
- collection_type: open
  name: deployment/APISync.proto AuthzService MonitoredEntityService API
  slug: open-verta-monitoredentityservice-api
- collection_type: open
  name: deployment/APISync.proto AuthzService ProjectService API
  slug: open-verta-projectservice-api
- collection_type: open
  name: deployment/APISync.proto AuthzService RegistryService API
  slug: open-verta-registryservice-api
- collection_type: open
  name: deployment/APISync.proto AuthzService SCIMConfigurationService API
  slug: open-verta-scimconfigurationservice-api
- collection_type: open
  name: deployment/APISync.proto AuthzService StageService API
  slug: open-verta-stageservice-api
- collection_type: open
  name: deployment/APISync.proto AuthzService UACService API
  slug: open-verta-uacservice-api
- collection_type: open
  name: deployment/APISync.proto AuthzService VersioningService API
  slug: open-verta-versioningservice-api
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/cloudera/
- group: company
  title: ''
  type: Website
  url: https://verta.ai
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/VertaAI/modeldb/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/VertaAI/modeldb/releases
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/verta/refs/heads/main/overlays/verta-apisync-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/verta-apisync-overlay.yaml
- group: commercial
  title: ''
  type: License
  url: https://github.com/VertaAI/modeldb/blob/main/LICENSE
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/verta/refs/heads/main/agentic-access/verta-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/verta-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/verta/refs/heads/main/authentication/verta-authentication.yml
  title: ''
  type: Authentication
  url: authentication/verta-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/verta/refs/heads/main/conventions/verta-conventions.yml
  title: ''
  type: Conventions
  url: conventions/verta-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/verta/refs/heads/main/errors/verta-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/verta-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/verta/refs/heads/main/data-model/verta-data-model.yml
  title: ''
  type: DataModel
  url: data-model/verta-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/verta/refs/heads/main/conformance/verta-conformance.yml
  title: ''
  type: Conformance
  url: conformance/verta-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/verta/refs/heads/main/lifecycle/verta-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/verta-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/verta/refs/heads/main/changelog/verta-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/verta-changelog.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/verta/refs/heads/main/packages/verta-packages.yml
  title: ''
  type: Packages
  url: packages/verta-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/verta/refs/heads/main/packages/verta-packages.yml
  title: ''
  type: SDKs
  url: packages/verta-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/verta/refs/heads/main/mcp/verta-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/verta-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/verta/refs/heads/main/llms/verta-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/verta-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/verta/refs/heads/main/skills/_index.yml
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
modified: '2026-09-16'
name: Verta
nav: Providers
network: true
overview: 'Verta publishes 11 APIs on the [APIs.io](https://apis.io/) network, including AuthzService API, DatasetService API, ExperimentRunService API, and 8 more. Tagged areas include MLOps, Machine-Learning, Model Management, Experiment Tracking, and Model Registry.


  Verta''s developer surface includes authentication, changelog, documentation, and 19 more developer resources.'
random_paper: 18
score:
  band: emerging
  composite: 25.2
  coverage:
    artifact_dirs: 20
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 38.0
    developer_ergonomics: 20.8
    discoverability: 81.5
    operational_transparency: 18.4
  open_source:
    applies: true
    score: 25.0
  previous_composite: 25.2
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
  schema_version: 0.22.0
  scored_at: '2026-09-19'
  trend: flat
  upsert:
    applies: true
    score: 11.1
screenshot: https://raw.githubusercontent.com/api-evangelist/verta/refs/heads/main/screenshots/verta-2026-09-02T165805.png
security:
- kind: authentication
  name: Verta Authentication
  slug: verta-authentication
  summary_line: custom · 0 schemes
slug: verta
tags:
- MLOps
- Machine-Learning
- Model Management
- Experiment Tracking
- Model Registry
- Model Versioning
- Metadata
- Open-Source
- Company
website: https://verta.ai
---
