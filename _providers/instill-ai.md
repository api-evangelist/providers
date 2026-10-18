---
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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 25.2
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 50
  human_in_the_loop: 0
  name: Instill Ai Agentic Access
  operation_count: 102
  slug: instill-ai-agentic-access
  summary_line: 102 operations · 50 acting
api_count: 2
apis:
- baseURL: https://api.instill-ai.com
  baseurl_source: declared
  description: Data orchestration for unified unstructured data representation.
  name: Instill AI Artifact API
  slug: instill-ai-artifact-api
- baseURL: https://api.instill-ai.com
  baseurl_source: declared
  description: Connections to 3rd party apps for use in pipelines.
  name: Instill AI Connection API
  slug: instill-ai-connection-api
- baseURL: https://api.instill-ai.com
  baseurl_source: declared
  description: Integration definitions for creating connections.
  name: Instill AI Integration API
  slug: instill-ai-integration-api
- baseURL: https://api.instill-ai.com
  baseurl_source: declared
  description: Resource usage metrics.
  name: Instill AI Metrics API
  slug: instill-ai-metrics-api
- baseURL: https://api.instill-ai.com
  baseurl_source: declared
  description: AI Model orchestration
  name: Instill AI Model API
  slug: instill-ai-model-api
- baseURL: https://api.instill-ai.com
  baseurl_source: declared
  description: Namespaces (e.g. User, Organization) that structure the resource hierarchy.
  name: Instill AI Namespace API
  slug: instill-ai-namespace-api
- baseURL: https://api.instill-ai.com
  baseurl_source: declared
  description: Pipeline orchestration.
  name: Instill AI Pipeline API
  slug: instill-ai-pipeline-api
artifact_total: 13
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/instill-ai/refs/heads/main/agentic-access/instill-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/instill-ai-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/instill-ai/refs/heads/main/rules/instill-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/instill-ai-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/instill-ai/refs/heads/main/rules/instill-ai-protobufs-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/instill-ai-protobufs-spectral-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/instill-ai/refs/heads/main/vocabulary/instill-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/instill-ai-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/instill-ai/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/instill-ai/refs/heads/main/data-model/instill-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/instill-ai-data-model.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/instill-ai/refs/heads/main/cli/instill-ai-cli.yml
  title: ''
  type: CLI
  url: cli/instill-ai-cli.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/instill-ai/refs/heads/main/conventions/instill-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/instill-ai-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/instill-ai/refs/heads/main/lifecycle/instill-ai-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/instill-ai-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/instill-ai/refs/heads/main/errors/instill-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/instill-ai-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/instill-ai/refs/heads/main/conformance/instill-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/instill-ai-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/instill-ai/refs/heads/main/grpc/instill-ai-usage-v1beta-usage.proto
  title: ''
  type: Protobuf
  url: grpc/instill-ai-usage-v1beta-usage.proto
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/instill-ai/refs/heads/main/grpc/instill-ai-pipeline-v1beta-secret.proto
  title: ''
  type: Protobuf
  url: grpc/instill-ai-pipeline-v1beta-secret.proto
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/instill-ai/refs/heads/main/grpc/instill-ai-pipeline-v1beta-pipeline_private_service.proto
  title: ''
  type: Protobuf
  url: grpc/instill-ai-pipeline-v1beta-pipeline_private_service.proto
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/instill-ai/refs/heads/main/grpc/instill-ai-pipeline-v1beta-pipeline.proto
  title: ''
  type: Protobuf
  url: grpc/instill-ai-pipeline-v1beta-pipeline.proto
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/instill-ai/refs/heads/main/grpc/instill-ai-pipeline-v1beta-integration.proto
  title: ''
  type: Protobuf
  url: grpc/instill-ai-pipeline-v1beta-integration.proto
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/instill-ai/refs/heads/main/grpc/instill-ai-pipeline-v1beta-component_definition.proto
  title: ''
  type: Protobuf
  url: grpc/instill-ai-pipeline-v1beta-component_definition.proto
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/instill-ai/refs/heads/main/grpc/instill-ai-pipeline-v1beta-common.proto
  title: ''
  type: Protobuf
  url: grpc/instill-ai-pipeline-v1beta-common.proto
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/instill-ai/refs/heads/main/grpc/instill-ai-model-v1alpha-model_private_service.proto
  title: ''
  type: Protobuf
  url: grpc/instill-ai-model-v1alpha-model_private_service.proto
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/instill-ai/refs/heads/main/grpc/instill-ai-model-v1alpha-model_definition.proto
  title: ''
  type: Protobuf
  url: grpc/instill-ai-model-v1alpha-model_definition.proto
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/instill-ai/refs/heads/main/grpc/instill-ai-model-v1alpha-model.proto
  title: ''
  type: Protobuf
  url: grpc/instill-ai-model-v1alpha-model.proto
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/instill-ai/refs/heads/main/grpc/instill-ai-model-v1alpha-common.proto
  title: ''
  type: Protobuf
  url: grpc/instill-ai-model-v1alpha-common.proto
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/instill-ai/refs/heads/main/grpc/instill-ai-model-ray-v1alpha-user_defined.proto
  title: ''
  type: Protobuf
  url: grpc/instill-ai-model-ray-v1alpha-user_defined.proto
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/instill-ai/refs/heads/main/grpc/instill-ai-model-ray-serve.proto
  title: ''
  type: Protobuf
  url: grpc/instill-ai-model-ray-serve.proto
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/instill-ai/refs/heads/main/grpc/instill-ai-mgmt-v1beta-mgmt_private_service.proto
  title: ''
  type: Protobuf
  url: grpc/instill-ai-mgmt-v1beta-mgmt_private_service.proto
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/instill-ai/refs/heads/main/grpc/instill-ai-mgmt-v1beta-mgmt.proto
  title: ''
  type: Protobuf
  url: grpc/instill-ai-mgmt-v1beta-mgmt.proto
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/instill-ai/refs/heads/main/grpc/instill-ai-mgmt-v1beta-metric.proto
  title: ''
  type: Protobuf
  url: grpc/instill-ai-mgmt-v1beta-metric.proto
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/instill-ai/refs/heads/main/grpc/instill-ai-mgmt-v1beta-integration.proto
  title: ''
  type: Protobuf
  url: grpc/instill-ai-mgmt-v1beta-integration.proto
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/instill-ai/refs/heads/main/grpc/instill-ai-mgmt-v1beta-auth.proto
  title: ''
  type: Protobuf
  url: grpc/instill-ai-mgmt-v1beta-auth.proto
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/instill-ai/refs/heads/main/grpc/instill-ai-common-healthcheck-v1beta-healthcheck.proto
  title: ''
  type: Protobuf
  url: grpc/instill-ai-common-healthcheck-v1beta-healthcheck.proto
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/instill-ai/refs/heads/main/grpc/instill-ai-artifact-v1alpha-update.proto
  title: ''
  type: Protobuf
  url: grpc/instill-ai-artifact-v1alpha-update.proto
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/instill-ai/refs/heads/main/grpc/instill-ai-artifact-v1alpha-system.proto
  title: ''
  type: Protobuf
  url: grpc/instill-ai-artifact-v1alpha-system.proto
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/instill-ai/refs/heads/main/grpc/instill-ai-artifact-v1alpha-object.proto
  title: ''
  type: Protobuf
  url: grpc/instill-ai-artifact-v1alpha-object.proto
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/instill-ai/refs/heads/main/grpc/instill-ai-artifact-v1alpha-knowledge_base.proto
  title: ''
  type: Protobuf
  url: grpc/instill-ai-artifact-v1alpha-knowledge_base.proto
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/instill-ai/refs/heads/main/grpc/instill-ai-artifact-v1alpha-file.proto
  title: ''
  type: Protobuf
  url: grpc/instill-ai-artifact-v1alpha-file.proto
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/instill-ai/refs/heads/main/grpc/instill-ai-artifact-v1alpha-chunk.proto
  title: ''
  type: Protobuf
  url: grpc/instill-ai-artifact-v1alpha-chunk.proto
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/instill-ai/refs/heads/main/grpc/instill-ai-artifact-v1alpha-artifact_private_service.proto
  title: ''
  type: Protobuf
  url: grpc/instill-ai-artifact-v1alpha-artifact_private_service.proto
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/instill-ai/refs/heads/main/grpc/instill-ai-artifact-v1alpha-artifact.proto
  title: ''
  type: Protobuf
  url: grpc/instill-ai-artifact-v1alpha-artifact.proto
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/instill-ai/refs/heads/main/overlays/instill-ai-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/instill-ai-openapi-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/instill-ai/refs/heads/main/llms/instill-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/instill-ai-llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/instill-ai/refs/heads/main/mcp/instill-ai-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/instill-ai-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/instill-ai/refs/heads/main/mcp/instill-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/instill-ai-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/instill-ai/refs/heads/main/well-known/instill-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/instill-ai-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/instill-ai/refs/heads/main/hosts/instill-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/instill-ai-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/instill-ai/refs/heads/main/vendors/instill-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/instill-ai-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/instill-ai/refs/heads/main/packages/instill-ai-packages.yml
  title: ''
  type: SDKs
  url: packages/instill-ai-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/instill-ai/refs/heads/main/packages/instill-ai-packages.yml
  title: ''
  type: Packages
  url: packages/instill-ai-packages.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/instill-ai/refs/heads/main/authentication/instill-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/instill-ai-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/instill-ai/refs/heads/main/security/instill-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/instill-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.instill-ai.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.instill-ai.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.instill-ai.com/reference
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/instill-ai
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.instill-ai.com
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/sevxWsqpGh
- group: design
  title: ''
  type: SpectralRules
  url: https://github.com/instill-ai/protobufs/blob/196f236ed9af8f57c672ad730a445de5daef5299/.spectral.yaml
created: '2026-10-09'
description: 'Instill AI (INSTILL AI LTD.) builds Instill Core, an open-source, full-stack AI infrastructure platform for data, pipeline and model orchestration: ETL processing of unstructured data, AI-readiness, open-source LLM hosting and RAG in one platform. It publishes a ReadMe-hosted developer reference at docs.instill-ai.com documenting a REST API at api.instill-ai.com (v1beta), plus Python and TypeScript SDKs, an Instill CLI, a Helm chart and its protobuf API definitions on GitHub. As of 2026-10-09 www.instill-ai.com answers HTTP 503 DEPLOYMENT_PAUSED and the docs guide pages return 404, while the API reference, GitHub org and trust center remain live.'
image: https://avatars.githubusercontent.com/u/66143470?s=280&v=4
layout: provider
mcp_servers:
- description: ReadMe-hosted MCP server attached to the Instill Core developer docs (docs.instill-ai.com). It exposes the published API reference (list/search/get endpoint) plus a generic execute-request tool that s
  name: Instill Core Developer Platform (docs MCP server)
  slug: instill-core-developer-platform-docs-mcp-server
modified: '2026-10-09'
name: Instill AI
nav: Providers
network: true
overview: 'Instill AI publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Artifact API, Connection API, Integration API, and 4 more. Tagged areas include Company, Artificial Intelligence, Unstructured Data, Data Pipeline, and RAG.


  The Instill AI catalog on APIs.io includes 2 Spectral governance rulesets.


  Instill AI''s developer surface includes CLI, authentication, documentation, API reference, and 52 more developer resources.'
random_paper: 2
rules:
- authorship: provider
  effective_rule_count: 41
  extends:
  - spectral:oas
  name: Instill AI — protobufs rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: instill-ai-protobufs-spectral-rules
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: Instill AI API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: instill-ai-rules
score:
  band: thin
  composite: 34.3
  coverage:
    artifact_dirs: 22
    catalog_earned: 42.8
    catalog_earned_first_party: 0.0
    catalog_gap: 72.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.1
  facets:
    access_clarity: 7.9
    contract_governance: 22.0
    contract_quality: 47.8
    developer_ergonomics: 49.4
    discoverability: 75.0
    operational_transparency: 5.3
  previous_composite: 39.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.0
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/instill-ai/refs/heads/main/screenshots/instill-ai-2026-10-11T105750.png
security:
- kind: authentication
  name: Instill Ai Authentication
  slug: instill-ai-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Instill Ai Domain Security
  slug: instill-ai-domain-security
  summary_line: TLSv1.3 · DMARC
slug: instill-ai
tags:
- Company
- Artificial Intelligence
- Unstructured Data
- Data Pipeline
- RAG
- Open Source
- LLM
website: https://www.instill-ai.com/
---
