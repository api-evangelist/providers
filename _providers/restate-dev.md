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
  band: human-only
  dimensions:
    agent_skills: true
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 4.8
  scored_at: '2026-07-27'
api_count: 3
apis:
- description: 'The Restate Admin API is the HTTP control plane for a running Restate Server, exposed by default on port 9070. It manages service deployment registration, lists and introspects services and handlers, '
  name: Restate Admin API
  slug: admin-api
- description: The Restate Ingress API is the HTTP data-plane for invoking services, virtual objects, and workflows running on Restate Server, exposed by default on port 8080. Requests follow the path conventions /{
  name: Restate Ingress API
  slug: ingress-api
- description: The Restate Service Protocol is the wire protocol Restate Server uses to communicate with handler endpoints implemented in any official SDK. It journals every side-effect (durable steps, RPCs, state r
  name: Restate Service Protocol
  slug: service-protocol
artifact_total: 55
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/restate-dev-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/restate-dev-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://restate.dev
- group: docs
  title: ''
  type: Documentation
  url: https://docs.restate.dev
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.restate.dev/get_started/quickstart
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.restate.dev/get_started/quickstart
- group: learn
  title: ''
  type: Tutorial
  url: https://docs.restate.dev/get_started/tour
- group: build
  title: ''
  type: SDKs
  url: https://docs.restate.dev/develop/sdks
- group: build
  title: ''
  type: CLI
  url: https://docs.restate.dev/operate/clients
- group: commercial
  title: ''
  type: Pricing
  url: https://restate.dev/pricing
- group: other
  title: ''
  type: Cloud
  url: https://restate.dev/cloud
- group: company
  title: ''
  type: Blog
  url: https://restate.dev/blog
- group: company
  title: ''
  type: Careers
  url: https://restate.dev/careers
- group: other
  title: ''
  type: Team
  url: https://restate.dev/team
- group: operate
  title: ''
  type: Contact
  url: https://restate.dev/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://restate.dev/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://restate.dev/privacy
- group: other
  title: ''
  type: Imprint
  url: https://restate.dev/imprint
- group: start
  title: ''
  type: Login
  url: https://cloud.restate.dev
- group: start
  title: ''
  type: Signup
  url: https://cloud.restate.dev
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/restatedev
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.restate.dev/llms.txt
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/restatedev/skills
created: '2026-05-25'
description: Restate is a durable execution platform for building resilient distributed applications, microservice orchestration, durable workflows, stateful services, and AI agents. Founded by Apache Flink and Apache Kafka veterans (Stephan Ewen, Igal Shilman, Till Rohrmann), Restate ships a single-binary Rust runtime that journals every step of handler execution so code survives crashes, restarts, and infrastructure failures. The platform exposes an Ingress API on port 8080 for HTTP invocation of services, virtual objects, and workflows (with idempotency keys, async /send semantics, and delayed invocations) and an Admin API on port 9070 for deployment registration, service introspection, invocation control (cancel, kill, pause, resume, restart, purge), subscriptions, and cluster health. Official SDKs target TypeScript, Java/Kotlin, Python, Go, Rust, and Ruby, with first-class integrations for AWS Lambda, Cloudflare Workers, Deno Deploy, Vercel, and Kubernetes (via the restate-operator).
  Restate Cloud is the managed offering with SOC 2 Type I compliance, enterprise SSO (Okta, Google Workspace, Azure AD), HIPAA BAAs, and an in-preview client-side journal encryption feature.
features:
- description: Restate journals every handler step so code survives crashes, restarts, and infrastructure failures and resumes exactly where it left off.
  name: Durable Execution
- description: Stateful, single-writer addressable entities with built-in key-value state and exclusive concurrency for safe stateful services.
  name: Virtual Objects
- description: Long-running, durable workflow handlers with deterministic replay, sleeps that can span months, and external signal awakeables.
  name: Workflows
- description: First-class patterns for compensating side-effects across distributed transactions with guaranteed cleanup paths.
  name: Sagas and Compensations
- description: External-event integration where workflows pause for human input, webhooks, or asynchronous callbacks without losing state.
  name: Durable Promises and Awakeables
- description: Subscribe Restate handlers to Kafka topics so events are turned into durable, exactly-once handler invocations.
  name: Kafka Event Subscriptions
- description: Idempotency-Key header makes any Ingress invocation safe to retry, with responses cached for 24 hours.
  name: Idempotent HTTP Invocations
- description: Schedule invocations into the future with ?delay= or use Restate as a cron substitute for durable timers.
  name: Delayed and Scheduled Invocations
- description: Query journal, invocation, service, and state metadata over an embedded Apache DataFusion SQL engine for live introspection.
  name: Embedded SQL Introspection
- description: A single Rust binary that runs single-node for development and scales to a multi-node cluster with embedded RocksDB and Raft.
  name: Single-Binary Distributed Server
- description: Managed Restate clusters with SOC 2 Type I, enterprise SSO (Okta, Google Workspace, Azure AD), HIPAA BAAs, and tunneling.
  name: Restate Cloud
- description: Developer-preview feature that encrypts journal entries with customer-owned keys before they reach Restate Cloud.
  name: Client-Side Journal Encryption
- description: First-party Web UI and restate CLI for inspecting invocations, registering deployments, and managing services.
  name: Web UI and CLI
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/restate-dev.png
integrations:
- description: Official Restate SDK for Node.js and TypeScript - the most-used SDK and the basis for many examples.
  name: TypeScript SDK
- description: Official Restate SDK for the JVM, with Spring Boot, Maven, and Gradle templates.
  name: Java/Kotlin SDK
- description: Official Restate SDK for Python, with AWS Lambda and standalone templates.
  name: Python SDK
- description: Official Restate SDK for Go with the standard handler/object/workflow programming model.
  name: Go SDK
- description: Official Restate SDK for Rust, sharing the same shared-core protocol implementation as the server.
  name: Rust SDK
- description: Official Restate SDK for Ruby (newer addition to the SDK family).
  name: Ruby SDK
- description: Official Kubernetes operator (restate-operator) for deploying Restate clusters on EKS, GKE, AKS, and bare-metal Kubernetes.
  name: Restate Operator for Kubernetes
- description: Deploy Restate handlers as AWS Lambda functions via the restatedev/cdk constructs and lambda templates.
  name: AWS Lambda
- description: Deploy Restate handlers to Cloudflare Workers via the cloudflare-workers-template.
  name: Cloudflare Workers
- description: Deploy Restate handlers to Deno Deploy via the deno-template.
  name: Deno Deploy
- description: Deploy Restate handlers to Vercel via the vercel-template and vercel-workflow projects.
  name: Vercel
- description: Subscribe handlers to Kafka topics for event-driven, exactly-once invocation.
  name: Kafka
- description: Run XState state machines as durable Restate workflows via restatedev/xstate.
  name: XState
- description: Make OpenAI Agents SDK loops crash-tolerant with Restate as the durable runtime.
  name: OpenAI Agents SDK
- description: Integrate Restate as the durable orchestrator behind LangChain agent workflows.
  name: LangChain
- description: Drive Pydantic AI agent workflows with Restate for fault tolerance and step replay.
  name: Pydantic AI
- description: Build resilient agents with the Google Agent Development Kit (ADK) and Restate.
  name: Google ADK
- description: Use Restate as the durable runtime for Vercel AI SDK agents and chat applications.
  name: Vercel AI SDK
- description: Integrate LiteLLM with Restate for durable LLM routing and retry across providers.
  name: LiteLLM
- description: Trace Restate handler executions and LLM calls in Langfuse for observability.
  name: Langfuse
- description: Emit traces, metrics, and logs from Restate Server and SDKs via OpenTelemetry.
  name: OpenTelemetry
- description: Use Restate to coordinate database transactions across services with durable execution guarantees.
  name: PostgreSQL and Databases
- description: Embedded Apache DataFusion SQL engine powers introspection queries against journals and state.
  name: Apache DataFusion
- description: Build stateful serverless applications by combining Knative and Restate.
  name: Knative
layout: provider
modified: '2026-05-25'
name: Restate
nav: Providers
network: true
overview: 'Restate publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include AI Agents, Durable Execution, Durable Workflows, Event-Driven, and Kafka.


  Restate''s developer surface includes developer portal, documentation, getting-started guide, tutorials, CLI, pricing, engineering blog, and 16 more developer resources.'
random_paper: 36
score:
  band: emerging
  composite: 28.7
  delta: 0.0
  facets:
    commercial_clarity: 52.6
    contract_quality: 0.0
    developer_ergonomics: 43.5
    discoverability: 87.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 28.7
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/restate-dev/refs/heads/main/screenshots/restate-dev-2026-06-20T193029.png
security:
- kind: domain-security
  name: Restate Dev Domain Security
  slug: restate-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Restate Dev Trust Center
  slug: restate-dev-trust-center
  summary_line: SOC 2
skill_count: 1
skills:
- name: building-restate-services
  slug: building-restate-services
slug: restate-dev
solutions:
- description: BSL-licensed single-binary Rust server, free for self-hosted use and the canonical runtime for the Restate Service Protocol.
  name: Restate Server (Open Source)
- description: Fully-managed Restate clusters with SOC 2, enterprise SSO, HIPAA BAA support, and Cloud Tunnel client for hybrid deployments.
  name: Restate Cloud
- description: Bring-your-own-cloud option for running Restate in customer-controlled AWS, GCP, or Azure accounts with Restate-managed operations.
  name: Restate On-Prem / BYOC
- description: Targeted positioning for durable agent orchestration with integrations across major LLM and agent frameworks.
  name: Restate for AI Agents
tags:
- AI Agents
- Durable Execution
- Durable Workflows
- Event-Driven
- Kafka
- Microservice Orchestration
- Orchestration
- ProCode_API_Composition
- Resilience
- Sagas
- Self-Hosting
- Service Protocol
- State Machines
- Stateful Services
- Step Functions
- Virtual Objects
- Workflows
- XState
use_cases:
- description: Coordinate multi-service business transactions with automatic retries, compensation, and timeout handling using durable handlers.
  name: Microservice Orchestration
- description: Build agents that survive process crashes and replay tool calls deterministically, with integrations for OpenAI, LangChain, Pydantic AI, Vercel AI, Google ADK, and LiteLLM.
  name: Durable AI Agents
- description: Replace AWS Step Functions / Azure Durable Functions / hand-rolled state machines with code-first workflows in your language of choice.
  name: Step Functions and Workflow Engines
- description: Run reliable background jobs with retries, idempotency, and scheduling without a separate queue and worker infrastructure.
  name: Background Jobs and Async Tasks
- description: Implement compensating-action sagas for cross-service operations like order fulfillment, payments, and inventory reservation.
  name: Saga-Based Distributed Transactions
- description: Combine virtual-object state with FaaS deployment on AWS Lambda, Cloudflare Workers, Deno Deploy, or Vercel for stateful serverless apps.
  name: Stateful Serverless APIs
- description: Subscribe handlers to Kafka topics so each event triggers a durable, exactly-once workflow invocation.
  name: Event-Driven Workflows
- description: Pause workflows on awakeables that wait for webhook callbacks, signed URLs, or human approvals for arbitrary durations.
  name: Human-in-the-Loop Approvals
website: https://restate.dev
---
