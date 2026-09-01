---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
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
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.3
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 2
  human_in_the_loop: 1
  name: Agentgateway Agentic Access
  operation_count: 9
  slug: agentgateway-agentic-access
  summary_line: 9 operations · 2 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: AgentGateway provides AI-native gateway capabilities for routing LLM traffic, federating MCP tools, enabling agent-to-agent communication, and applying security and observability controls across AI ag
  name: AgentGateway
  slug: agentgateway
- description: The Config API from AgentGateway — 1 operation(s) for config.
  name: AgentGateway Config API
  slug: agentgateway-config-api
- description: The Debug API from AgentGateway — 2 operation(s) for debug.
  name: AgentGateway Debug API
  slug: agentgateway-debug-api
- description: The Lifecycle API from AgentGateway — 1 operation(s) for lifecycle.
  name: AgentGateway Lifecycle API
  slug: agentgateway-lifecycle-api
- description: The Logging API from AgentGateway — 1 operation(s) for logging.
  name: AgentGateway Logging API
  slug: agentgateway-logging-api
- description: The Memory API from AgentGateway — 1 operation(s) for memory.
  name: AgentGateway Memory API
  slug: agentgateway-memory-api
- description: The Profiling API from AgentGateway — 2 operation(s) for profiling.
  name: AgentGateway Profiling API
  slug: agentgateway-profiling-api
artifact_total: 59
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: AgentGateway Admin / Debug Config API
  slug: open-agentgateway-config-api
- collection_type: open
  name: AgentGateway Admin / Config Debug API
  slug: open-agentgateway-debug-api
- collection_type: open
  name: AgentGateway Admin / Debug Config Lifecycle API
  slug: open-agentgateway-lifecycle-api
- collection_type: open
  name: AgentGateway Admin / Debug Config Logging API
  slug: open-agentgateway-logging-api
- collection_type: open
  name: AgentGateway Admin / Debug Config Memory API
  slug: open-agentgateway-memory-api
- collection_type: open
  name: AgentGateway Admin / Debug Config Profiling API
  slug: open-agentgateway-profiling-api
- collection_type: open
  name: AgentGateway Admin / Debug API
  slug: open-agentgateway
common:
- group: company
  title: ''
  type: Website
  url: https://agentgateway.dev/
- group: docs
  title: ''
  type: APIReference
  url: https://agentgateway.dev/docs/standalone/latest/reference/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://lfprojects.org/policies/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.linuxfoundation.org/legal/privacy-policy
- group: other
  title: ''
  type: Charter
  url: https://github.com/agentgateway/agentgateway/blob/main/CHARTER.md
- group: docs
  title: Configuration Schema (LocalConfig) - first-party, JSON Schema draft 2020-12, 302 definitions
  type: JSONSchema
  url: https://agentgateway.dev/schema/config
- group: docs
  title: Configuration Schema (LocalConfig) - verbatim capture of https://agentgateway.dev/schema/config
  type: JSONSchema
  url: json-schema/agentgateway-config-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/agentgateway-route-structure.json
- group: build
  title: ''
  type: Examples
  url: https://github.com/agentgateway/agentgateway/tree/main/examples
- group: design
  title: ''
  type: SpectralRules
  url: rules/agentgateway-jsonschema-spectral-rules.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/agentgateway-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/agentgateway-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/agentgateway-finops.yml
- group: build
  title: ''
  type: Packages
  url: packages/agentgateway-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/agentgateway-cli.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/agentgateway-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/agentgateway-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/agentgateway-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/agentgateway-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/agentgateway-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://agentgateway.dev/docs/standalone/latest/reference/release-notes/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/agentgateway-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/agentgateway-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/agentgateway-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: webhooks/agentgateway-webhooks.yml
- group: auth
  title: ''
  type: Security
  url: https://github.com/agentgateway/agentgateway/blob/main/SECURITY.md
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/agentgateway-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/agentgateway-llms.txt
- group: agent
  title: ''
  type: WellKnown-probe
  url: well-known/agentgateway-well-known.yml
- group: agent
  title: ''
  type: MCPServer-candidate
  url: mcp/agentgateway-mcp.yml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/agentgateway/agentgateway/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/agentgateway/agentgateway/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/agentgateway/agentgateway/blob/main/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/agentgateway/agentgateway/blob/main/CODE_OF_CONDUCT.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/agentgateway/agentgateway/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/agentgateway-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/agentgateway-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/agentgateway
- group: docs
  title: LLM Backend Schema
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/agentgateway/refs/heads/main/json-schema/agentgateway-llm-backend-schema.json
- group: docs
  title: MCP Target Schema
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/agentgateway/refs/heads/main/json-schema/agentgateway-mcp-target-schema.json
- group: docs
  title: Route Schema
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/agentgateway/refs/heads/main/json-schema/agentgateway-route-schema.json
- group: design
  title: ''
  type: JSONLD
  url: https://raw.githubusercontent.com/api-evangelist/agentgateway/refs/heads/main/json-ld/agentgateway-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/agentgateway/refs/heads/main/vocabulary/agentgateway-vocabulary.yaml
- group: start
  title: ''
  type: Portal
  url: https://agentgateway.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://agentgateway.dev/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://agentgateway.dev/docs/quickstart/
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/y9efgEmppm
- group: agent
  title: ''
  type: LlmsText
  url: https://agentgateway.dev/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://agentgateway.dev/blog/index.xml
created: '2026-03-27'
description: AgentGateway is an open-source, AI-native proxy and gateway for routing, observing, and governing traffic to and from AI agents, LLM providers, and MCP servers. Built on the A2A and MCP protocols, it provides a unified gateway for LLM consumption, MCP tool federation, agent-to-agent communication, security, and observability. AgentGateway supports multi-provider LLM routing across OpenAI, Anthropic, Google Gemini, AWS Bedrock, and Azure OpenAI with built-in RBAC, JWT authentication, rate limiting, and OpenTelemetry integration.
examples:
- key_count: 8
  name: Agentgateway Llm Backend Example
  slug: agentgateway-llm-backend-example
- key_count: 6
  name: Agentgateway Mcp Target Example
  slug: agentgateway-mcp-target-example
- key_count: 5
  name: Agentgateway Route Example
  slug: agentgateway-route-example
features:
- description: Routes traffic to OpenAI, Anthropic, Google Gemini, AWS Bedrock, and Azure OpenAI through a unified API with model aliasing, failover, and load balancing.
  name: LLM Gateway
- description: Connects LLMs to tools via Model Context Protocol with static and dynamic routing, tool federation, and stateful MCP sessions.
  name: MCP Gateway
- description: Enables secure, governed communication between AI agents using the A2A protocol for multi-agent orchestration.
  name: Agent-to-Agent (A2A) Gateway
- description: Intelligently routes requests to self-hosted models based on GPU utilization and request priority.
  name: Inference Routing
- description: Provides JWT, OAuth2, API key management, CORS, CSRF protection, MCP authentication, and external authorization support.
  name: Security and Authentication
- description: Supports request routing and matching, header manipulation, rate limiting, retries, gRPC routing, traffic splitting, and direct responses.
  name: Traffic Management
- description: Integrates with OpenTelemetry for metrics, traces, and access logging with a built-in Admin UI and debugging tools.
  name: Observability
- description: Applies prompt guards, content filtering, regex filters, moderation policies, and custom webhooks for AI safety.
  name: Guardrails
- description: Tracks budget and spend limits per user, team, or application with RBAC-based controls on LLM consumption.
  name: Cost Controls
- description: Supports prompt templates and enrichment for standardizing and augmenting requests before routing to LLM providers.
  name: Prompt Enrichment
finops:
- name: Agentgateway Finops
  service_category: API
  slug: agentgateway-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/agentgateway.png
integrations:
- description: Route to OpenAI GPT models through the AgentGateway LLM backend with model aliasing and budget controls.
  name: OpenAI
- description: Connect to Anthropic Claude models via the unified LLM gateway with failover and load balancing.
  name: Anthropic
- description: Route traffic to Google Gemini models through the AgentGateway multi-provider backend.
  name: Google Gemini
- description: Integrate with AWS Bedrock for managed LLM access via the AgentGateway routing layer.
  name: AWS Bedrock
- description: Route requests to Azure-hosted OpenAI models through the unified gateway API.
  name: Azure OpenAI
- description: Connect to locally hosted Ollama models for self-hosted inference routing.
  name: Ollama
- description: Route to vLLM inference servers with GPU utilization-aware routing for optimal performance.
  name: vLLM
- description: Export metrics, traces, and logs to any OpenTelemetry-compatible observability backend.
  name: OpenTelemetry
- description: Deploy and configure AgentGateway on Kubernetes using the standard Gateway API for dynamic configuration.
  name: Kubernetes Gateway API
json_schemas:
- name: LocalConfig
  property_count: 14
  slug: agentgateway-config
- name: LLMBackend
  property_count: 8
  slug: agentgateway-llm-backend
- name: MCPTarget
  property_count: 6
  slug: agentgateway-mcp-target
- name: Route
  property_count: 5
  slug: agentgateway-route
json_structures:
- name: Agentgateway Llm Backend Structure
  property_count: 8
  slug: agentgateway-llm-backend-structure
- name: Agentgateway Mcp Target Structure
  property_count: 6
  slug: agentgateway-mcp-target-structure
- name: Agentgateway Route Structure
  property_count: 5
  slug: agentgateway-route-structure
jsonld:
- class_count: 5
  name: Agentgateway Context
  property_count: 21
  slug: agentgateway-context
layout: provider
modified: '2026-08-30'
name: AgentGateway
nav: Providers
network: true
overview: 'AgentGateway publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Config API, Debug API, Lifecycle API, and 3 more. Tagged areas include AI Gateway, API Gateway, MCP, LLM, and Agent-to-Agent.


  The AgentGateway catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  AgentGateway''s developer surface includes API reference, code examples, CLI, authentication, changelog, sandbox, developer portal, and 43 more developer resources.'
plans:
- name: Agentgateway Plans Pricing
  plan_count: 0
  slug: agentgateway-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Agentgateway Rate Limits
  slug: agentgateway-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: AgentGateway API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: agentgateway-jsonschema-spectral-rules
score:
  band: strong
  composite: 55.8
  coverage:
    artifact_dirs: 31
    catalog_gap: 49.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 43.2
    contract_quality: 54.4
    developer_ergonomics: 78.6
    discoverability: 75.9
    governance: 43.2
    operational_transparency: 44.7
  open_source:
    applies: true
    score: 75.0
  previous_composite: 55.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/agentgateway/refs/heads/main/screenshots/agentgateway-2026-06-20T170015.png
security:
- kind: authentication
  name: Agentgateway Authentication
  slug: agentgateway-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Agentgateway Domain Security
  slug: agentgateway-domain-security
  summary_line: TLSv1.3
- kind: vulnerability-disclosure
  name: Agentgateway Vulnerability Disclosure
  slug: agentgateway-vulnerability-disclosure
  summary_line: Hackerone
slug: agentgateway
tags:
- AI Gateway
- API Gateway
- MCP
- LLM
- Agent-to-Agent
- Open-Source
- CNCF
- Observability
- Security
use_cases:
- description: Route requests across multiple LLM providers with a single API, enabling failover, load balancing, and cost optimization without changing client code.
  name: Unified LLM Routing
- description: Aggregate tools from multiple MCP servers behind a single gateway endpoint, enabling agents to discover and invoke tools from any connected MCP server.
  name: MCP Tool Federation
- description: Apply organization-wide security policies, rate limits, budget controls, and content filters to all AI agent traffic through a centralized gateway.
  name: Enterprise AI Governance
- description: Convert existing REST APIs into MCP-native tool endpoints that AI agents can discover and invoke through the Model Context Protocol.
  name: REST API to MCP Conversion
- description: Enable secure agent-to-agent communication using the A2A protocol, allowing specialized agents to delegate tasks to each other through the gateway.
  name: Multi-Agent Orchestration
- description: Collect unified telemetry across all AI agent and LLM interactions to monitor cost, latency, and behavior at scale.
  name: Observability and Debugging
website: https://agentgateway.dev/
---
