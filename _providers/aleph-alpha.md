---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 49.8
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 96
  human_in_the_loop: 0
  name: Aleph Alpha Agentic Access
  operation_count: 194
  slug: aleph-alpha-agentic-access
  summary_line: 194 operations · 96 acting
api_count: 37
apis:
- description: The API description API from Aleph Alpha — 2 operation(s) for api description.
  name: Aleph Alpha API description API
  slug: aleph-alpha-api-description-api
- description: The Application Traces API from Aleph Alpha — 2 operation(s) for application traces.
  name: Aleph Alpha Application Traces API
  slug: aleph-alpha-application-traces-api
- description: Endpoints for handling execution instances of benchmarks. These provides an overview of all evaluation steps during execution (run, evaluation, aggregation).
  name: Aleph Alpha Benchmark Executions API
  slug: aleph-alpha-benchmark-executions-api
- description: Endpoints for handling benchmarks. A Benchmark provides a way to compare and evaluate the quality of your task results for a specific dataset.
  name: Aleph Alpha Benchmarks API
  slug: aleph-alpha-benchmarks-api
- description: The cluster API from Aleph Alpha — 4 operation(s) for cluster.
  name: Aleph Alpha Cluster API
  slug: aleph-alpha-cluster-api
- description: Management of document collections
  name: Aleph Alpha Collection API
  slug: aleph-alpha-collection-api
- description: Available connectors for the Data Platform to ingest data from external sources.
  name: Aleph Alpha Connectors API
  slug: aleph-alpha-connectors-api
- description: Create, retrieve, update, delete, and list conversations.
  name: Aleph Alpha Conversations API
  slug: aleph-alpha-conversations-api
- description: Represents the primary data abstraction within the data platform, serving as a structured collection of data points. Datasets can be either manually uploaded or generated through data transformations,
  name: Aleph Alpha Datasets API
  slug: aleph-alpha-datasets-api
- description: A Document represents an individual item stored within a Search Store. Documents can contain content from various modalities, such as text, images, or pre-chunked data.
  name: Aleph Alpha Document API
  slug: aleph-alpha-document-api
- description: 'Endpoints for managing and tracking dataset download requests within the data platform. These endpoints allow users to initiate new downloads, retrieve details of specific download requests, and list '
  name: Aleph Alpha Downloads API
  slug: aleph-alpha-downloads-api
- description: Endpoints for handling evaluation datasets, which are specific datasets to be used for evaluation in the Pharia Studio SDK.
  name: Aleph Alpha Evaluation Datasets API
  slug: aleph-alpha-evaluation-datasets-api
- description: Endpoints for handling Events. Events capture detailed information about specific occurrences within a Span. This includes logs, exceptions, and other relevant data points that provide a granular view
  name: Aleph Alpha Events API
  slug: aleph-alpha-events-api
- description: Management of search filter indexes
  name: Aleph Alpha Filter Index API
  slug: aleph-alpha-filter-index-api
- description: Check content against guardrail policies.
  name: Aleph Alpha Guardrails API
  slug: aleph-alpha-guardrails-api
- description: Management of search indexes
  name: Aleph Alpha Index API
  slug: aleph-alpha-index-api
- description: Lineages represent the results of a benchmark execution. A single lineage represents an evaluation of a single example with a task and evaluation logic. They contain all task and evaluation logic inpu
  name: Aleph Alpha Lineages API
  slug: aleph-alpha-lineages-api
- description: The models API from Aleph Alpha — 6 operation(s) for models.
  name: Aleph Alpha Models API
  slug: aleph-alpha-models-api
- description: Management of namespaces
  name: Aleph Alpha Namespace API
  slug: aleph-alpha-namespace-api
- description: Health checks and operational endpoints.
  name: Aleph Alpha Operations API
  slug: aleph-alpha-operations-api
- description: The permissions API from Aleph Alpha — 1 operation(s) for permissions.
  name: Aleph Alpha Permissions API
  slug: aleph-alpha-permissions-api
- description: A Project is an abstraction representing a group of running operations associated with the same task in the Studio. Endpoints under this tag allow you to create, update, delete, and retrieve projects.
  name: Aleph Alpha Projects API
  slug: aleph-alpha-projects-api
- description: A collection of data organized by a common type, modality, and schema, stored within datasets (lists of data points) in the repositories. To share datasets externally, they must first be exported as f
  name: Aleph Alpha Repositories API
  slug: aleph-alpha-repositories-api
- description: Create, retrieve, and delete responses. Supports streaming and multi-turn conversations via response chaining.
  name: Aleph Alpha Responses API
  slug: aleph-alpha-responses-api
- description: A Search Store is a structured data repository optimized for indexing and retrieving searchable entities. It supports full-text search, metadata-based filtering, and relevance ranking. Each Search Sto
  name: Aleph Alpha Search Store API
  slug: aleph-alpha-search-store-api
- description: Service health and status
  name: Aleph Alpha Service API
  slug: aleph-alpha-service-api
- description: Endpoints for managing Spans. A Span is a single unit of work within a Trace and represents an individual operation in the execution sequence. Spans help in breaking down the Trace into more manageabl
  name: Aleph Alpha Spans API
  slug: aleph-alpha-spans-api
- description: 'Stages serve as the data platform''s entry point for data collection, where source files are securely stored, enabling subsequent transformations and dataset generation. Files can be uploaded directly '
  name: Aleph Alpha Stages API
  slug: aleph-alpha-stages-api
- description: The steering API from Aleph Alpha — 1 operation(s) for steering.
  name: Aleph Alpha Steering API
  slug: aleph-alpha-steering-api
- description: Requests for different types of tasks you can request with our models.
  name: Aleph Alpha Tasks API
  slug: aleph-alpha-tasks-api
- description: Manage tokens associated with your user account for API access.
  name: Aleph Alpha Tokens API
  slug: aleph-alpha-tokens-api
- description: Trace management endpoints. A Trace provides a mechanism similar to OpenTelemetry for tracking the execution flow of a task. It allows you to monitor and analyze the sequence of operations, their timi
  name: Aleph Alpha Traces API
  slug: aleph-alpha-traces-api
- description: Available transformations can be applied to an input data object of type A to produce an output data object of type B. The output data object will consist of a sequence of items, each of which will co
  name: Aleph Alpha Transformations API
  slug: aleph-alpha-transformations-api
- description: '**Usecases (Applications)** Usecases are full-stack end to end AI applications. The application exposes the necessary REST endpoints so AI usecases can be consumed and, optionally, a front-end (UI) to'
  name: Aleph Alpha Usecases API
  slug: aleph-alpha-usecases-api
- description: The users API from Aleph Alpha — 2 operation(s) for users.
  name: Aleph Alpha Users API
  slug: aleph-alpha-users-api
- description: The v1/models API from Aleph Alpha — 4 operation(s) for v1/models.
  name: Aleph Alpha V1/models API
  slug: aleph-alpha-v1-models-api
- description: A Workspace is a shared environment where users can collaborate on projects. Workspaces help in organizing and managing projects in large organizations efficiently.
  name: Aleph Alpha Workspaces API
  slug: aleph-alpha-workspaces-api
artifact_total: 80
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Aleph Alpha API description API
  slug: open-aleph-alpha-api-description-api
- collection_type: open
  name: PhariaStudio Application Traces API
  slug: open-aleph-alpha-application-traces-api
- collection_type: open
  name: PhariaStudio Benchmark Executions API
  slug: open-aleph-alpha-benchmark-executions-api
- collection_type: open
  name: PhariaStudio Benchmarks API
  slug: open-aleph-alpha-benchmarks-api
- collection_type: open
  name: PhariaOS Manager Cluster API
  slug: open-aleph-alpha-cluster-api
- collection_type: open
  name: Aleph Alpha Document Index Collection API
  slug: open-aleph-alpha-collection-api
- collection_type: open
  name: PhariaData Connectors API
  slug: open-aleph-alpha-connectors-api
- collection_type: open
  name: Stateful Responses Conversations API
  slug: open-aleph-alpha-conversations-api
- collection_type: open
  name: PhariaData Datasets API
  slug: open-aleph-alpha-datasets-api
- collection_type: open
  name: Aleph Alpha Document API
  slug: open-aleph-alpha-document-api
- collection_type: open
  name: PhariaData Downloads API
  slug: open-aleph-alpha-downloads-api
- collection_type: open
  name: PhariaStudio Evaluation Datasets API
  slug: open-aleph-alpha-evaluation-datasets-api
- collection_type: open
  name: PhariaStudio Events API
  slug: open-aleph-alpha-events-api
- collection_type: open
  name: Aleph Alpha Document Index Filter Index API
  slug: open-aleph-alpha-filter-index-api
- collection_type: open
  name: Stateful Responses Guardrails API
  slug: open-aleph-alpha-guardrails-api
- collection_type: open
  name: Aleph Alpha Document Index API
  slug: open-aleph-alpha-index-api
- collection_type: open
  name: PhariaStudio Lineages API
  slug: open-aleph-alpha-lineages-api
- collection_type: open
  name: Aleph Alpha Models API
  slug: open-aleph-alpha-models-api
- collection_type: open
  name: Aleph Alpha Document Index Namespace API
  slug: open-aleph-alpha-namespace-api
- collection_type: open
  name: Stateful Responses Operations API
  slug: open-aleph-alpha-operations-api
- collection_type: open
  name: Aleph Alpha Permissions API
  slug: open-aleph-alpha-permissions-api
- collection_type: open
  name: PhariaStudio Projects API
  slug: open-aleph-alpha-projects-api
- collection_type: open
  name: PhariaData Repositories API
  slug: open-aleph-alpha-repositories-api
- collection_type: open
  name: Stateful Responses API
  slug: open-aleph-alpha-responses-api
- collection_type: open
  name: PhariaData Search Store API
  slug: open-aleph-alpha-search-store-api
- collection_type: open
  name: Aleph Alpha Document Index Service API
  slug: open-aleph-alpha-service-api
- collection_type: open
  name: PhariaStudio Spans API
  slug: open-aleph-alpha-spans-api
- collection_type: open
  name: PhariaData Stages API
  slug: open-aleph-alpha-stages-api
- collection_type: open
  name: Aleph Alpha Steering API
  slug: open-aleph-alpha-steering-api
- collection_type: open
  name: Aleph Alpha Tasks API
  slug: open-aleph-alpha-tasks-api
- collection_type: open
  name: Aleph Alpha Tokens API
  slug: open-aleph-alpha-tokens-api
- collection_type: open
  name: PhariaStudio Traces API
  slug: open-aleph-alpha-traces-api
- collection_type: open
  name: PhariaData Transformations API
  slug: open-aleph-alpha-transformations-api
- collection_type: open
  name: PhariaOS Manager Usecases API
  slug: open-aleph-alpha-usecases-api
- collection_type: open
  name: Aleph Alpha Users API
  slug: open-aleph-alpha-users-api
- collection_type: open
  name: PhariaOS Manager V1/models API
  slug: open-aleph-alpha-v1-models-api
- collection_type: open
  name: PhariaStudio Workspaces API
  slug: open-aleph-alpha-workspaces-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/aleph-alpha-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aleph-alpha-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/aleph-alpha-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://aleph-alpha.com/en/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.aleph-alpha.com/phariaai-dev-guide/latest/index.html
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aleph-alpha.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.aleph-alpha.com/phariaai-dev-guide/latest/pharia-openapi/index.html
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.aleph-alpha.com/phariaai-dev-guide/latest/phariaai-applications/quick-start-custom-apps.html
- group: auth
  title: ''
  type: Authentication
  url: https://docs.aleph-alpha.com/phariaai-dev-guide/latest/get-token.html
- group: operate
  title: ''
  type: Support
  url: https://supportportal.aleph-alpha.com/
- group: company
  title: ''
  type: Blog
  url: https://aleph-alpha.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Aleph-Alpha
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.aleph-alpha.com/phariaai-home/latest/release-notes/index.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aleph-alpha.com/data-privacy/
- group: other
  title: ''
  type: Imprint
  url: https://aleph-alpha.com/imprint/
- group: other
  title: ''
  type: Research
  url: https://aleph-alpha.com/research/
- group: other
  title: ''
  type: HuggingFace
  url: https://huggingface.co/Aleph-Alpha
- group: build
  title: ''
  type: Packages
  url: packages/aleph-alpha-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/aleph-alpha-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/aleph-alpha-cli.yml
- group: design
  title: ''
  type: Components
  url: components/aleph-alpha-components.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/aleph-alpha-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/aleph-alpha-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/aleph-alpha-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/aleph-alpha-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/aleph-alpha-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/aleph-alpha-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.aleph-alpha.com/phariaai-home/latest/release-notes/index.html
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/aleph-alpha-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/aleph-alpha-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.dqsglobal.com/en/customer-database/aleph-alpha-gmbh
- group: auth
  title: ''
  type: TrustCenter
  url: security/aleph-alpha-trust-center.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/aleph-alpha-data-model.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/aleph-alpha-well-known.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/aleph-alpha-pharia-inference-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/aleph-alpha-responses-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/aleph-alpha-pharia-data-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/aleph-alpha-pharia-search-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/aleph-alpha-pharia-studio-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/aleph-alpha-pharia-os-overlay.yaml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/aleph-alpha-sandbox.yml
- group: other
  title: ''
  type: Playground
  url: https://docs.aleph-alpha.com/phariaai-dev-guide/latest/pharia-studio/playground.html
- group: operate
  title: ''
  type: Contact
  url: https://aleph-alpha.com/en/contact/
created: '2026-08-02'
description: Aleph Alpha is a Heidelberg, Germany based sovereign AI company building PhariaAI, an end-to-end, customizable AI suite for enterprises and governments that can be deployed on-premise or hosted. The stack combines leading open-source and proprietary large language models with Aleph Alpha's own Pharia-1-LLM model family and its research into transparency, explainability and domain-specific performance. PhariaAI is exposed through six documented HTTP APIs — PhariaInference (completion, chat, embeddings, tokenization), PhariaData (repositories, datasets, transformations), PhariaSearch / Document Index (semantic search over a knowledge base), PhariaStudio (projects, traces, evaluation, benchmarks), PhariaOS (cluster, use case and model lifecycle management) and a stateful, OpenAI-compatible Responses API with MCP tool calling — each published as an OpenAPI or Swagger definition on the Aleph Alpha documentation site. First-party SDKs ship for Python and Rust, alongside a CLI for
  publishing WebAssembly skills to the Pharia Kernel.
image: https://aleph-alpha.com/og-image.jpg
layout: provider
mcp_servers:
- description: ''
  name: aleph-alpha-mcp.yml
  slug: aleph-alpha-mcpyml
modified: '2026-08-02'
name: Aleph Alpha
nav: Providers
network: true
overview: 'Aleph Alpha publishes 37 APIs on the [APIs.io](https://apis.io/) network, including API description API, Application Traces API, Benchmark Executions API, and 34 more. Tagged areas include Company, Artificial Intelligence, Machine Learning, Large Language Models, and Generative AI.


  Aleph Alpha''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, changelog, and 37 more developer resources.'
random_paper: 42
score:
  band: developing
  composite: 48.5
  delta: 0.0
  facets:
    commercial_clarity: 26.3
    contract_quality: 56.8
    developer_ergonomics: 82.1
    discoverability: 75.9
    governance: 11.5
    operational_transparency: 28.9
  previous_composite: 48.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 37
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 48.1
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/aleph-alpha/refs/heads/main/screenshots/aleph-alpha-2026-08-07T161154.png
security:
- kind: authentication
  name: Aleph Alpha Authentication
  slug: aleph-alpha-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Aleph Alpha Domain Security
  slug: aleph-alpha-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Aleph Alpha Trust Center
  slug: aleph-alpha-trust-center
  summary_line: trust center published
slug: aleph-alpha
tags:
- Company
- Artificial Intelligence
- Machine Learning
- Large Language Models
- Generative AI
- Sovereign AI
- Inference
- Embeddings
- Semantic Search
- Vector Search
- Agents
- Model Context Protocol
- Germany
- Enterprise Software
- Government
website: https://aleph-alpha.com/en/
---
