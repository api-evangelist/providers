---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
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
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.3
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 53
  human_in_the_loop: 2
  name: Langflow Agentic Access
  operation_count: 95
  slug: langflow-agentic-access
  summary_line: 95 operations · 53 acting · 2 human-in-the-loop
api_count: 15
apis:
- description: The Base API from Langflow — 6 operation(s) for base.
  name: Langflow Base API
  slug: langflow-base-api
- description: The Chat API from Langflow — 6 operation(s) for chat.
  name: Langflow Chat API
  slug: langflow-chat-api
- description: The Files API from Langflow — 11 operation(s) for files.
  name: Langflow Files API
  slug: langflow-files-api
- description: The Flow Events API from Langflow — 1 operation(s) for flow events.
  name: Langflow Flow Events API
  slug: langflow-flow-events-api
- description: The Flows API from Langflow — 8 operation(s) for flows.
  name: Langflow Flows API
  slug: langflow-flows-api
- description: The Health Check API from Langflow — 2 operation(s) for health check.
  name: Langflow Health Check API
  slug: langflow-health-check-api
- description: The Log API from Langflow — 2 operation(s) for log.
  name: Langflow Log API
  slug: langflow-log-api
- description: The MCP API from Langflow — 2 operation(s) for mcp.
  name: Langflow MCP API
  slug: langflow-mcp-api
- description: The mcp_projects API from Langflow — 4 operation(s) for mcp_projects.
  name: Langflow mcp_projects API
  slug: langflow-mcp-projects-api
- description: The Monitor API from Langflow — 12 operation(s) for monitor.
  name: Langflow Monitor API
  slug: langflow-monitor-api
- description: The OpenAI Responses API API from Langflow — 1 operation(s) for openai responses api.
  name: Langflow OpenAI Responses API API
  slug: langflow-openai-responses-api-api
- description: The Projects API from Langflow — 4 operation(s) for projects.
  name: Langflow Projects API
  slug: langflow-projects-api
- description: The Traces API from Langflow — 2 operation(s) for traces.
  name: Langflow Traces API
  slug: langflow-traces-api
- description: The Users API from Langflow — 4 operation(s) for users.
  name: Langflow Users API
  slug: langflow-users-api
- description: The Workflow API from Langflow — 2 operation(s) for workflow.
  name: Langflow Workflow API
  slug: langflow-workflow-api
artifact_total: 55
collections:
- collection_type: open
  name: Langflow
  slug: open-langflow
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/langflow-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/langflow-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/langflow-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/langflow-scopes.yml
- group: start
  title: ''
  type: Portal
  url: https://www.langflow.org
- group: docs
  title: ''
  type: Documentation
  url: https://docs.langflow.org
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.langflow.org/get-started-installation
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.langflow.org/get-started-quickstart
- group: docs
  title: ''
  type: Documentation
  url: https://docs.langflow.org/api-reference-api-examples
- group: auth
  title: ''
  type: Authentication
  url: https://docs.langflow.org/api-keys-and-authentication
- group: docs
  title: ''
  type: Documentation
  url: https://docs.langflow.org/concepts-flows
- group: docs
  title: ''
  type: Documentation
  url: https://docs.langflow.org/concepts-components
- group: docs
  title: ''
  type: Documentation
  url: https://docs.langflow.org/configuration-authentication
- group: docs
  title: ''
  type: Documentation
  url: https://docs.langflow.org/deployment-overview
- group: docs
  title: ''
  type: Documentation
  url: https://docs.langflow.org/deployment-docker
- group: docs
  title: ''
  type: Documentation
  url: https://docs.langflow.org/deployment-kubernetes
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.langflow.org/release-notes
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/langflow-ai/langflow
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/langflow-ai
- group: commercial
  title: ''
  type: License
  url: https://github.com/langflow-ai/langflow/blob/main/LICENSE
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/langflow-ai/langflow/releases
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/langflow-ai/langflow/issues
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/langflow-ai/langflow/blob/main/CONTRIBUTING.md
- group: other
  title: ''
  type: HelmChart
  url: https://github.com/langflow-ai/langflow-helm-charts
- group: build
  title: ''
  type: Tools
  url: https://github.com/langflow-ai/langflow-embedded-chat
- group: build
  title: ''
  type: SDKs
  url: https://github.com/langflow-ai/langflow-client-ts
- group: other
  title: ''
  type: Deployment
  url: https://github.com/langflow-ai/langflow-railway
- group: build
  title: ''
  type: Tools
  url: https://github.com/langflow-ai/openrag
- group: build
  title: ''
  type: Tools
  url: https://github.com/langflow-ai/langflow-bundles
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/langflow-ai/langflow-twilio-voice
- group: build
  title: ''
  type: Tools
  url: https://github.com/langflow-ai/mcp-sse-shim
- group: build
  title: ''
  type: Package
  url: https://pypi.org/project/langflow/
- group: other
  title: ''
  type: Container
  url: https://hub.docker.com/r/langflowai/langflow
- group: docs
  title: ''
  type: Documentation
  url: https://docs.langflow.org/develop-application
- group: docs
  title: ''
  type: Documentation
  url: https://docs.langflow.org/concepts-flows-import
- group: docs
  title: ''
  type: Documentation
  url: https://docs.langflow.org/concepts-file-management
- group: docs
  title: ''
  type: Documentation
  url: https://docs.langflow.org/concepts-flows-monitor
- group: docs
  title: ''
  type: Documentation
  url: https://docs.langflow.org/concepts-publish
- group: docs
  title: ''
  type: Documentation
  url: https://docs.langflow.org/concepts-playground
- group: docs
  title: ''
  type: Documentation
  url: https://docs.langflow.org/agents-overview
- group: docs
  title: ''
  type: Documentation
  url: https://docs.langflow.org/mcp-server
- group: docs
  title: ''
  type: Documentation
  url: https://docs.langflow.org/mcp-client
- group: docs
  title: ''
  type: Documentation
  url: https://docs.langflow.org/typescript-client
- group: operate
  title: ''
  type: Forums
  url: https://discord.com/invite/EqksyE2EX9
- group: learn
  title: ''
  type: Video
  url: https://www.youtube.com/@Langflow
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/langflow_ai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/langflow-ai/
- group: company
  title: ''
  type: Blog
  url: https://www.langflow.org/blog
- group: company
  title: ''
  type: Newsletter
  url: https://www.langflow.org/newsletter
- group: other
  title: ''
  type: Owner
  url: https://www.ibm.com/products/datastax
created: '2026-05-24T00:00:00.000Z'
description: Langflow is an open-source low-code visual builder for AI agents, RAG pipelines, and LangChain-based workflows. It pairs a drag-and-drop React Flow frontend with a FastAPI backend that exposes every flow as a REST API, an MCP server, and an OpenAI-compatible Responses endpoint. Components are editable Python and ship with integrations across most major LLMs, vector stores, and observability platforms. Langflow was acquired by DataStax in 2025; DataStax itself was acquired by IBM and the deal closed on May 28, 2025, making Langflow an IBM property while remaining MIT-licensed open source. The project is the canonical reference implementation for visually composing LangChain agents — 149k+ GitHub stars, distributed via PyPI, Docker, Helm, and native Desktop apps, with a hosted cloud option run by DataStax.
examples:
- key_count: 2
  name: Langflow Create Flow Example
  slug: langflow-create-flow-example
- key_count: 2
  name: Langflow List Mcp Servers Example
  slug: langflow-list-mcp-servers-example
- key_count: 2
  name: Langflow Run Flow Example
  slug: langflow-run-flow-example
- key_count: 2
  name: Langflow Webhook Example
  slug: langflow-webhook-example
features:
- Visual drag-and-drop builder for AI agents, RAG pipelines, and LangChain workflows
- FastAPI-based REST API with OpenAPI 3.1 spec served at /docs and /openapi.json on every deployment
- 67 REST endpoints covering flows, builds, projects, files, users, API keys, MCP servers, monitoring, and traces
- OpenAI-compatible Responses endpoint (/api/v1/responses) so OpenAI clients can target a Langflow flow
- Webhook execution endpoint per flow for event-driven invocation
- Streaming flow execution via SSE on the build endpoints
- Native MCP (Model Context Protocol) server — every Langflow project is exposable as an MCP server
- MCP client support for consuming external MCP servers as Langflow components
- Project / flow / component hierarchy with import-export, batch operations, and public-flow sharing
- Session-aware chat with shared sessions for read-only collaboration
- Built-in trace explorer plus integrations with LangSmith and LangFuse for observability
- Pluggable Python components — every component's source is editable in the UI
- Multi-agent orchestration with conditional routing and tool calls
- Vector-store integrations including Astra DB, Chroma, Pinecone, Milvus, Weaviate, Qdrant, and pgvector
- LLM integrations including OpenAI, Anthropic, Google, Azure, Bedrock, Mistral, Cohere, Hugging Face, Ollama, and Groq
- File upload and per-user file management with batch operations (v2 Files API)
- API key authentication via `x-api-key` header or query parameter
- Auto-login mode for local dev and superuser mode for production
- Distributed by Python package on PyPI (`pip install langflow`), Docker image (`langflowai/langflow:latest`), Helm chart, and Desktop app for macOS and Windows
- MIT-licensed, written in Python (FastAPI backend) and TypeScript (React Flow frontend)
- 149k+ GitHub stars, v1.9.3 (May 2026) — actively maintained by langflow-ai with 800+ contributors
- Hosted Langflow Cloud offering operated by IBM DataStax (post-acquisition)
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/langflow.png
json_schemas:
- name: FlowRead
  property_count: 19
  slug: langflow-flow
- name: MCPServerConfig
  property_count: 5
  slug: langflow-mcp-server
- name: MessageResponse
  property_count: 15
  slug: langflow-message
- name: FolderReadWithFlows
  property_count: 6
  slug: langflow-project
- name: UserRead
  property_count: 10
  slug: langflow-user
json_structures:
- name: Langflow Flow Structure
  property_count: 10
  slug: langflow-flow-structure
jsonld:
- class_count: 27
  name: Langflow Context
  property_count: 13
  slug: langflow-context
layout: provider
modified: '2026-05-24'
name: Langflow
nav: Providers
network: true
overview: 'Langflow publishes 15 APIs on the [APIs.io](https://apis.io/) network, including Base API, Chat API, Files API, and 12 more. Tagged areas include AI, Artificial Intelligence, Agents, Workflows, and Low-Code.


  The Langflow catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Langflow''s developer surface includes authentication, developer portal, documentation, getting-started guide, changelog, tooling, code examples, and 43 more developer resources.'
random_paper: 46
rules:
- name: Langflow API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: langflow-jsonschema-spectral-rules
- name: Langflow API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 2
    info: 1
    warn: 3
  slug: langflow-rules
scopes:
- name: Langflow Scopes
  scope_count: 0
  slug: langflow-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 41.1
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 61.3
    developer_ergonomics: 47.8
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 21.1
  previous_composite: 41.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 15
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/langflow/refs/heads/main/screenshots/langflow-2026-06-20T184304.png
security:
- kind: authentication
  name: Langflow Authentication
  slug: langflow-authentication
  summary_line: apiKey/oauth2 · 3 schemes
- kind: domain-security
  name: Langflow Domain Security
  slug: langflow-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: langflow
tags:
- AI
- Artificial Intelligence
- Agents
- Workflows
- Low-Code
- Visual Builder
- LangChain
- RAG
- MCP
- Open Source
- FastAPI
website: https://www.langflow.org
---
