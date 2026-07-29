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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.4
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Zenml Agentic Access
  operation_count: 25
  slug: zenml-agentic-access
  summary_line: 25 operations · 7 acting
api_count: 14
apis:
- description: The ZenML Pro REST API extends the OSS API with managed control-plane features for teams, including organization and tenant management, role-based access control, audit logs, and enterprise governance
  name: ZenML Pro REST API
  slug: zenml-pro-api
- description: Artifact metadata and versions produced by pipeline runs
  name: ZenML Artifacts API
  slug: zenml-artifacts-api
- description: Authentication and token management
  name: ZenML Auth API
  slug: zenml-auth-api
- description: Pipeline deployments
  name: ZenML Deployments API
  slug: zenml-deployments-api
- description: Registered models and their versions
  name: ZenML Models API
  slug: zenml-models-api
- description: Pipeline run instances and their steps
  name: ZenML Pipeline Runs API
  slug: zenml-pipeline-runs-api
- description: ML pipeline definitions
  name: ZenML Pipelines API
  slug: zenml-pipelines-api
- description: Project workspaces
  name: ZenML Projects API
  slug: zenml-projects-api
- description: Scheduled pipeline runs
  name: ZenML Schedules API
  slug: zenml-schedules-api
- description: Encrypted secret storage
  name: ZenML Secrets API
  slug: zenml-secrets-api
- description: Connectors to external infrastructure providers
  name: ZenML Service Connectors API
  slug: zenml-service-connectors-api
- description: Individual stack components such as orchestrators, artifact stores, and experiment trackers
  name: ZenML Stack Components API
  slug: zenml-stack-components-api
- description: ZenML stacks and their components
  name: ZenML Stacks API
  slug: zenml-stacks-api
- description: User accounts
  name: ZenML Users API
  slug: zenml-users-api
arazzos:
- description: Walk from a named pipeline to its run history and drill into the most recent run.
  name: ZenML Audit Pipeline Runs
  slug: zenml-audit-pipeline-runs-workflow
- description: Exchange credentials for a token, confirm the session identity, and list pipelines.
  name: ZenML Authenticate and List Pipelines
  slug: zenml-authenticate-and-list-pipelines-workflow
- description: Identify the caller, resolve a project workspace, register a pipeline, and confirm it.
  name: ZenML Bootstrap Project Pipeline
  slug: zenml-bootstrap-project-pipeline-workflow
- description: Select a pipeline run, confirm it succeeded, and inspect an artifact produced in the deployment.
  name: ZenML Inspect Run Artifacts
  slug: zenml-inspect-run-artifacts-workflow
- description: Pick a stack, read its component wiring, and cross-reference the component catalog.
  name: ZenML Inspect Stack Topology
  slug: zenml-inspect-stack-topology-workflow
- description: Find the latest run of a pipeline, poll its status to completion, and branch on success or failure.
  name: ZenML Monitor Pipeline Run
  slug: zenml-monitor-pipeline-run-workflow
- description: Resolve a project, register a new pipeline in it, and confirm the pipeline was created.
  name: ZenML Provision Pipeline
  slug: zenml-provision-pipeline-workflow
- description: Confirm the caller identity, create a scoped secret, and confirm it appears in the secret store.
  name: ZenML Provision Secret
  slug: zenml-provision-secret-workflow
- description: Register a new model in the model control plane and enumerate its versions.
  name: ZenML Register Model
  slug: zenml-register-model-workflow
- description: Discover available stack components, assemble them into a new stack, and confirm the stack was created.
  name: ZenML Register Stack
  slug: zenml-register-stack-workflow
- description: Select a pipeline deployment, resolve its pipeline, and read the latest run it produced.
  name: ZenML Trace Deployment Runs
  slug: zenml-trace-deployment-runs-workflow
- description: Resolve a schedule, find the run it produced for its pipeline, and read that run.
  name: ZenML Track Scheduled Pipeline
  slug: zenml-track-scheduled-pipeline-workflow
artifact_total: 48
collections:
- collection_type: postman
  name: ZenML OSS REST API
  slug: postman-zenml
- collection_type: open
  name: ZenML OSS REST API
  slug: open-zenml
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/zenml-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zenml-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/zenml-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/zenml/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/zenml-audit-pipeline-runs-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/zenml-authenticate-and-list-pipelines-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/zenml-bootstrap-project-pipeline-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/zenml-inspect-run-artifacts-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/zenml-inspect-stack-topology-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/zenml-monitor-pipeline-run-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/zenml-provision-pipeline-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/zenml-provision-secret-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/zenml-register-model-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/zenml-register-stack-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/zenml-trace-deployment-runs-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/zenml-track-scheduled-pipeline-workflow.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/zenml
- group: start
  title: ''
  type: Portal
  url: https://www.zenml.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.zenml.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.zenml.io/getting-started/installation
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.zenml.io/changelog/server-sdk
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/zenml-io/zenml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/zenml-io
- group: commercial
  title: ''
  type: Pricing
  url: https://www.zenml.io/pro
- group: company
  title: ''
  type: Blog
  url: https://www.zenml.io/blog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.zenml.io/
- group: other
  title: ''
  type: Resources
  url: https://www.zenml.io/careers
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.zenml.io/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.zenml.io/privacy-policy
- group: build
  title: ''
  type: SDKs
  url: https://pypi.org/project/zenml/
- group: build
  title: ''
  type: SDKs
  url: https://docs.zenml.io/sdk-reference
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://github.com/zenml-io/zenml/releases
- group: design
  title: ''
  type: JSONLD
  url: json-ld/zenml-context.jsonld
- group: other
  title: ''
  type: Resources
  url: vocabulary/zenml-vocabulary.yml
- group: other
  title: ''
  type: Resources
  url: rules/zenml-rules.yml
- group: other
  title: ''
  type: Resources
  url: capabilities/pipeline-lifecycle.yaml
- group: other
  title: ''
  type: Resources
  url: capabilities/model-promotion.yaml
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/zenml-io/mcp-zenml
- group: agent
  title: ''
  type: AgentSkills
  url: https://www.zenml.io/blog/introducing-zenml-agent-skills-let-ai-upgrade-your-mlops-setup-in-minutes
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.zenml.io/llms.txt
created: '2025-02-08'
description: ZenML is an open-source MLOps and LLMOps framework that unifies machine learning and generative AI workflows through a single orchestration, versioning, and governance layer. It provides a Python SDK, CLI, REST API, and server for managing pipelines, stacks, artifacts, models, and deployments across any infrastructure backend, with 60+ integrations spanning orchestrators, ML frameworks, GenAI tools, cloud storage, and experiment tracking platforms.
examples:
- key_count: 2
  name: Zenml Create Stack Example
  slug: zenml-create-stack-example
- key_count: 2
  name: Zenml Get Pipeline Run Example
  slug: zenml-get-pipeline-run-example
- key_count: 2
  name: Zenml List Pipelines Example
  slug: zenml-list-pipelines-example
finops:
- name: Zenml Finops
  service_category: API
  slug: zenml-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zenml.png
json_schemas:
- name: ZenML Artifact
  property_count: 8
  slug: zenml-artifact
- name: ZenML Model
  property_count: 10
  slug: zenml-model
- name: ZenML Pipeline Run
  property_count: 9
  slug: zenml-pipeline-run
- name: ZenML Pipeline
  property_count: 9
  slug: zenml-pipeline
- name: ZenML Stack
  property_count: 6
  slug: zenml-stack
json_structures:
- name: Zenml Pipeline Run Structure
  property_count: 7
  slug: zenml-pipeline-run-structure
- name: Zenml Pipeline Structure
  property_count: 8
  slug: zenml-pipeline-structure
jsonld:
- class_count: 23
  name: Zenml Context
  property_count: 3
  slug: zenml-context
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: ZenML
nav: Providers
network: true
overview: 'ZenML publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Artifacts API, Auth API, Deployments API, and 10 more. Tagged areas include AI, Machine Learning, MLOps, LLMOps, and Pipelines.


  The ZenML catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  ZenML''s developer surface includes authentication, developer portal, documentation, getting-started guide, changelog, pricing, engineering blog, and 33 more developer resources.'
plans:
- name: Zenml Plans Pricing
  plan_count: 3
  slug: zenml-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 5
  name: Zenml Rate Limits
  slug: zenml-rate-limits
rules:
- name: ZenML API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: zenml-jsonschema-spectral-rules
- name: ZenML API Rules
  rule_count: 6
  severity_counts:
    error: 2
    hint: 0
    info: 1
    warn: 3
  slug: zenml-rules
score:
  band: strong
  composite: 64.5
  delta: -4.9
  facets:
    commercial_clarity: 71.1
    contract_quality: 63.0
    developer_ergonomics: 60.9
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 68.4
  previous_composite: 69.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 13
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/zenml/refs/heads/main/screenshots/zenml-2026-06-20T201813.png
security:
- kind: authentication
  name: Zenml Authentication
  slug: zenml-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Zenml Domain Security
  slug: zenml-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: zenml
tags:
- AI
- Machine Learning
- MLOps
- LLMOps
- Pipelines
- Open Source
- Python
website: https://www.zenml.io/
---
