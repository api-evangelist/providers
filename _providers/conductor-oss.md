---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 17.3
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 15
  human_in_the_loop: 1
  name: Conductor Oss Agentic Access
  operation_count: 26
  slug: conductor-oss-agentic-access
  summary_line: 26 operations · 15 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: Conductor MCP is an official Model Context Protocol server for Orkes Conductor that exposes workflow execution, task management, and metadata operations as MCP tools so that LLMs and AI agents can orc
  name: Conductor MCP Server
  slug: conductor-mcp
- baseURL: http://localhost:8080/api
  baseurl_source: declared
  description: The Events API from Conductor OSS — 1 operation(s) for events.
  name: Conductor OSS Events API
  slug: conductor-oss-events-api
- baseURL: http://localhost:8080/api
  baseurl_source: declared
  description: The Metadata API from Conductor OSS — 4 operation(s) for metadata.
  name: Conductor OSS Metadata API
  slug: conductor-oss-metadata-api
- baseURL: http://localhost:8080/api
  baseurl_source: declared
  description: The Tasks API from Conductor OSS — 5 operation(s) for tasks.
  name: Conductor OSS Tasks API
  slug: conductor-oss-tasks-api
- baseURL: http://localhost:8080/api
  baseurl_source: declared
  description: The Workflow API from Conductor OSS — 9 operation(s) for workflow.
  name: Conductor OSS Workflow API
  slug: conductor-oss-workflow-api
artifact_total: 38
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Conductor OSS REST Events API
  slug: open-conductor-oss-events-api
- collection_type: open
  name: Conductor OSS REST Events Metadata API
  slug: open-conductor-oss-metadata-api
- collection_type: open
  name: Conductor OSS REST Events Tasks API
  slug: open-conductor-oss-tasks-api
- collection_type: open
  name: Conductor OSS REST Events Workflow API
  slug: open-conductor-oss-workflow-api
- collection_type: open
  name: Conductor OSS REST API
  slug: open-conductor-oss
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/conductor-oss/conductor-mcp/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/conductor-oss/conductor-mcp/releases
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/conductor-oss-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/conductor-oss-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://conductor-oss.org/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.conductor-oss.org/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.conductor-oss.org/getting-started
- group: build
  title: ''
  type: GitHub
  url: https://github.com/conductor-oss
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/conductor-oss
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/conductor-oss/conductor
- group: company
  title: ''
  type: Blog
  url: https://orkes.io/blog/
- group: operate
  title: ''
  type: Slack
  url: https://join.slack.com/t/orkes-conductor/shared_invite/zt-3dpcskdyd-W895bJDm8psAV7viYG3jFA
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@orkesio
- group: commercial
  title: ''
  type: License
  url: https://github.com/conductor-oss/conductor/blob/main/LICENSE
- group: commercial
  title: ''
  type: Pricing
  url: https://orkes.io/pricing
- group: start
  title: ''
  type: Portal
  url: https://cloud.orkes.io/
- group: start
  title: ''
  type: Signup
  url: https://cloud.orkes.io/signup
- group: learn
  title: ''
  type: Training
  url: https://orkes.io/academy/
- group: build
  title: ''
  type: SDKs
  url: https://github.com/conductor-oss/java-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/conductor-oss/python-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/conductor-oss/go-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/conductor-oss/javascript-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/conductor-oss/csharp-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/conductor-oss/clojure-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/conductor-oss/rust-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/conductor-oss/ruby-sdk
- group: build
  title: ''
  type: CLI
  url: https://github.com/conductor-oss/conductor-cli
created: '2026-05-25'
description: Conductor OSS is the Netflix-founded, Orkes-stewarded open source workflow and agentic AI orchestration platform. It provides a durable, event-driven workflow engine for coordinating microservices, long-running tasks, human approvals, and LLM-powered agents across any language or cloud, with first class support for HTTP, gRPC, Kafka, AMQP, SQS, and MCP-based tool calling.
features:
- description: Workflow state is persisted at every step so executions survive worker restarts, server failover, and long human-in-the-loop waits.
  name: Durable Workflow Execution
- description: Tasks are executed by language-agnostic workers that poll the server, with official SDKs in Java, Python, Go, JavaScript / TypeScript, C#, Clojure, Ruby, and Rust.
  name: Polyglot Workers
- description: Built-in HTTP, Kafka, JQ, wait, human approval, sub-workflow, fork, join, switch, do-while, and dynamic-fork operators compose workflows without writing code.
  name: System Tasks and Operators
- description: Native LLM tasks for 14+ providers, vector database integrations for RAG, MCP tool calling, and human-in-the-loop checkpoints make Conductor a runtime for agentic AI applications.
  name: Agentic AI and LLM Orchestration
- description: Event handlers consume from Kafka, AMQP, SQS, NATS, and webhook sources to start workflows or complete tasks from external systems.
  name: Event-Driven Triggers
- description: Stateless API servers and worker pools scale horizontally, with pluggable persistence (PostgreSQL, MySQL, Cassandra, Redis) and indexing (OpenSearch / Elasticsearch).
  name: Horizontal Scalability
- description: Built-in metrics, structured logs, distributed tracing, and a Swagger UI on every server expose the workflow surface for operators.
  name: Operational Observability
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/conductor-oss.png
integrations:
- description: System task and event-handler integration for Kafka topics.
  name: Apache Kafka
- description: Built-in AMQP system task and event source.
  name: AMQP / RabbitMQ
- description: Native SQS event queue and system task module.
  name: AWS SQS
- description: NATS event queue integration for triggering workflows.
  name: NATS
- description: Pluggable persistence backends for workflow and task state.
  name: PostgreSQL / MySQL / Cassandra / Redis
- description: Pluggable indexing backends powering search and history.
  name: OpenSearch / Elasticsearch
- description: External payload storage for large workflow inputs and outputs.
  name: AWS S3 / Azure Blob
- description: Official MCP server exposes Conductor to AI agents as tools.
  name: Model Context Protocol (MCP)
- description: gRPC API surface alongside the REST API for high-performance clients.
  name: gRPC
layout: provider
modified: '2026-05-25'
name: Conductor OSS
nav: Providers
network: true
overview: 'Conductor OSS publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Events API, Metadata API, Tasks API, and 1 more. Tagged areas include Agentic AI, Durable Execution, Event-Driven, Microservices, and Netflix.


  Conductor OSS''s developer surface includes documentation, getting-started guide, GitHub presence, engineering blog, YouTube channel, pricing, developer portal, and 20 more developer resources.'
random_paper: 19
score:
  band: thin
  composite: 35.3
  coverage:
    artifact_dirs: 6
    catalog_gap: 83.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 1.1
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 48.8
    developer_ergonomics: 50.0
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 18.4
  previous_composite: 34.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/conductor-oss/refs/heads/main/screenshots/conductor-oss-2026-06-20T174846.png
security:
- kind: domain-security
  name: Conductor Oss Domain Security
  slug: conductor-oss-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: conductor-oss
solutions:
- description: Apache 2.0 open source workflow engine, self-hosted via Docker, Helm, or source build.
  name: Conductor OSS
- description: Free hosted Conductor sandbox by Orkes with all enterprise features enabled for prototyping and learning.
  name: Orkes Developer Edition
- description: Fully managed Conductor on AWS, Azure, GCP, or on-prem with SOC2, RBAC, SSO, audit logs, and up to 99.99% availability SLA.
  name: Orkes Enterprise / Cloud
tags:
- Agentic AI
- Durable Execution
- Event-Driven
- Microservices
- Netflix
- Open-Source
- Orchestration
- Workflow Engine
- Workflows
use_cases:
- description: Coordinate sagas, compensations, retries, and timeouts across distributed microservices without bespoke orchestration code.
  name: Microservices Orchestration
- description: Run production-grade agentic workflows with reasoning loops, tool calling, MCP integration, RAG retrieval, and human approvals.
  name: AI Agent Orchestration
- description: Reliable long-running flows for payments, fulfillment, KYC, and onboarding — the reference example workload shipped by Conductor.
  name: Payment and Order Processing
- description: Schedule and orchestrate ETL, model training, and inference pipelines with durable retries and conditional branching.
  name: Data and ML Pipelines
- description: Pause workflows on human tasks, capture approvals via UI or API, and resume execution deterministically.
  name: Human-in-the-Loop Approvals
- description: Bridge message brokers and SaaS webhooks into deterministic workflows across the enterprise.
  name: Event-Driven Integration
website: https://conductor-oss.org/
---
