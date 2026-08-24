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
    agent_skills: derived
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: partial
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.6
  scored_at: '2026-08-24'
api_count: 42
apis:
- description: Agent configuration management
  name: Comet Agent Configs API
  slug: comet-agent-configs-api
- description: Agent Insights report results
  name: Comet Agent Insights API
  slug: comet-agent-insights-api
- description: Per-(workspace, project) Agent Insights report configuration
  name: Comet Agent Insights Jobs API
  slug: comet-agent-insights-jobs-api
- description: Alert resources
  name: Comet Alerts API
  slug: comet-alerts-api
- description: Private annotation queue operations
  name: Comet Annotation Queues API
  slug: comet-annotation-queues-api
- description: Assertion result related resources
  name: Comet Assertion Results API
  slug: comet-assertion-results-api
- description: Attachments related resources
  name: Comet Attachments API
  slug: comet-attachments-api
- description: Automation rule evaluators resource
  name: Comet Automation rule evaluators API
  slug: comet-automation-rule-evaluators-api
- description: Chat Completions related resources
  name: Comet Chat Completions API
  slug: comet-chat-completions-api
- description: Access check resources
  name: Comet Check API
  slug: comet-check-api
- description: Workspace Dashboard resources
  name: Comet Dashboards API
  slug: comet-dashboards-api
- description: Dataset resources
  name: Comet Datasets API
  slug: comet-datasets-api
- description: Environment related resources
  name: Comet Environments API
  slug: comet-environments-api
- description: Experiment resources
  name: Comet Experiments API
  slug: comet-experiments-api
- description: Feedback definitions related resources
  name: Comet Feedback-definitions API
  slug: comet-feedback-definitions-api
- description: Guardrails related resources
  name: Comet Guardrails API
  slug: comet-guardrails-api
- description: Insights View resources
  name: Comet Insights Views API
  slug: comet-insights-views-api
- description: The Is Alive API from Comet — 2 operation(s) for is alive.
  name: Comet Is Alive API
  slug: comet-is-alive-api
- description: LLM model registry resources
  name: Comet LLM Models API
  slug: comet-llm-models-api
- description: LLM Provider Key
  name: Comet LlmProviderKey API
  slug: comet-llmproviderkey-api
- description: Manual evaluation resources for traces, threads, and spans
  name: Comet Manual Evaluation API
  slug: comet-manual-evaluation-api
- description: MCP OAuth 2.1 Authorization Server resources
  name: Comet MCP OAuth API
  slug: comet-mcp-oauth-api
- description: Ollama provider configuration endpoints with OpenAI-compatible API support.
  name: Comet Ollama API
  slug: comet-ollama-api
- description: Ollie pod state persistence
  name: Comet Ollie State API
  slug: comet-ollie-state-api
- description: Resource to ingest Traces and Spans via OpenTelemetry
  name: Comet OpenTelemetry Ingestion API
  slug: comet-opentelemetry-ingestion-api
- description: Optimization resources
  name: Comet Optimizations API
  slug: comet-optimizations-api
- description: Pairing sessions for the `opik connect` and `opik endpoint` CLI commands
  name: Comet Pairing API
  slug: comet-pairing-api
- description: Project related resources
  name: Comet Projects API
  slug: comet-projects-api
- description: Prompt resources
  name: Comet Prompts API
  slug: comet-prompts-api
- description: Redirects for SDK generated links
  name: Comet Redirect API
  slug: comet-redirect-api
- description: Generic failure log for reports/jobs
  name: Comet Report Failures API
  slug: comet-report-failures-api
- description: Ollie daily report management
  name: Comet Reports API
  slug: comet-reports-api
- description: Data retention rule management
  name: Comet Retention Rules API
  slug: comet-retention-rules-api
- description: Local runner management endpoints
  name: Comet Runners API
  slug: comet-runners-api
- description: Service Toggles resources
  name: Comet Service Toggles API
  slug: comet-service-toggles-api
- description: Span related resources
  name: Comet Spans API
  slug: comet-spans-api
- description: Internal endpoint to run Agent Insights free-form SQL
  name: Comet System analytics queries API
  slug: comet-system-analytics-queries-api
- description: System usage related resource
  name: Comet System usage API
  slug: comet-system-usage-api
- description: Trace related resources
  name: Comet Traces API
  slug: comet-traces-api
- description: Welcome wizard tracking resources
  name: Comet Welcome Wizard API
  slug: comet-welcome-wizard-api
- description: Workspace permissions related resources
  name: Comet Workspace permissions API
  slug: comet-workspace-permissions-api
- description: Workspace related resources
  name: Comet Workspaces API
  slug: comet-workspaces-api
artifact_total: 89
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Opik REST Agent Configs API
  slug: open-comet-agent-configs-api
- collection_type: open
  name: Opik REST Agent Insights API
  slug: open-comet-agent-insights-api
- collection_type: open
  name: Opik REST Agent Insights Jobs API
  slug: open-comet-agent-insights-jobs-api
- collection_type: open
  name: Opik REST Alerts API
  slug: open-comet-alerts-api
- collection_type: open
  name: Opik REST Annotation Queues API
  slug: open-comet-annotation-queues-api
- collection_type: open
  name: Opik REST Assertion Results API
  slug: open-comet-assertion-results-api
- collection_type: open
  name: Opik REST Attachments API
  slug: open-comet-attachments-api
- collection_type: open
  name: Opik REST Automation rule evaluators API
  slug: open-comet-automation-rule-evaluators-api
- collection_type: open
  name: Opik REST Chat Completions API
  slug: open-comet-chat-completions-api
- collection_type: open
  name: Opik REST Check API
  slug: open-comet-check-api
- collection_type: open
  name: Opik REST Dashboards API
  slug: open-comet-dashboards-api
- collection_type: open
  name: Opik REST Datasets API
  slug: open-comet-datasets-api
- collection_type: open
  name: Opik REST Environments API
  slug: open-comet-environments-api
- collection_type: open
  name: Opik REST Experiments API
  slug: open-comet-experiments-api
- collection_type: open
  name: Opik REST Feedback-definitions API
  slug: open-comet-feedback-definitions-api
- collection_type: open
  name: Opik REST Guardrails API
  slug: open-comet-guardrails-api
- collection_type: open
  name: Opik REST Insights Views API
  slug: open-comet-insights-views-api
- collection_type: open
  name: Opik REST Is Alive API
  slug: open-comet-is-alive-api
- collection_type: open
  name: Opik REST LLM Models API
  slug: open-comet-llm-models-api
- collection_type: open
  name: Opik REST LlmProviderKey API
  slug: open-comet-llmproviderkey-api
- collection_type: open
  name: Opik REST Manual Evaluation API
  slug: open-comet-manual-evaluation-api
- collection_type: open
  name: Opik REST MCP OAuth API
  slug: open-comet-mcp-oauth-api
- collection_type: open
  name: Opik REST Ollama API
  slug: open-comet-ollama-api
- collection_type: open
  name: Opik REST Ollie State API
  slug: open-comet-ollie-state-api
- collection_type: open
  name: Opik REST OpenTelemetry Ingestion API
  slug: open-comet-opentelemetry-ingestion-api
- collection_type: open
  name: Opik REST Optimizations API
  slug: open-comet-optimizations-api
- collection_type: open
  name: Opik REST Pairing API
  slug: open-comet-pairing-api
- collection_type: open
  name: Opik REST Projects API
  slug: open-comet-projects-api
- collection_type: open
  name: Opik REST Prompts API
  slug: open-comet-prompts-api
- collection_type: open
  name: Opik REST Redirect API
  slug: open-comet-redirect-api
- collection_type: open
  name: Opik REST Report Failures API
  slug: open-comet-report-failures-api
- collection_type: open
  name: Opik REST Reports API
  slug: open-comet-reports-api
- collection_type: open
  name: Opik REST Retention Rules API
  slug: open-comet-retention-rules-api
- collection_type: open
  name: Opik REST Runners API
  slug: open-comet-runners-api
- collection_type: open
  name: Opik REST Service Toggles API
  slug: open-comet-service-toggles-api
- collection_type: open
  name: Opik REST Spans API
  slug: open-comet-spans-api
- collection_type: open
  name: Opik REST System analytics queries API
  slug: open-comet-system-analytics-queries-api
- collection_type: open
  name: Opik REST System usage API
  slug: open-comet-system-usage-api
- collection_type: open
  name: Opik REST Traces API
  slug: open-comet-traces-api
- collection_type: open
  name: Opik REST Welcome Wizard API
  slug: open-comet-welcome-wizard-api
- collection_type: open
  name: Opik REST Workspace permissions API
  slug: open-comet-workspace-permissions-api
- collection_type: open
  name: Opik REST Workspaces API
  slug: open-comet-workspaces-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/comet-opik-overlay.yaml
- group: auth
  title: ''
  type: TrustCenter
  url: security/comet-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.comet.com/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/comet-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.comet.com/docs/opik/
- group: docs
  title: ''
  type: Documentation
  url: https://www.comet.com/docs/opik/
- group: docs
  title: ''
  type: APIReference
  url: https://www.comet.com/docs/opik/reference/rest-api/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://www.comet.com/docs/opik/quickstart
- group: operate
  title: ''
  type: Support
  url: https://github.com/comet-ml/opik/issues
- group: company
  title: ''
  type: Blog
  url: https://www.comet.com/site/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/comet-ml
- group: commercial
  title: ''
  type: Pricing
  url: https://www.comet.com/site/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://www.comet.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.comet.com/site/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.comet.com/site/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.comet.com/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/comet-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/comet-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/comet-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/comet-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/comet-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/comet-changelog.yml
created: '2026-07-17'
description: 'Comet is an enterprise AI/ML developer platform used by over 150,000 developers and organizations including Netflix, Uber, and Autodesk. Its flagship open-source product, Opik, is an LLM observability, evaluation, and optimization suite for building, testing, and monitoring generative AI applications, RAG systems, and agentic workflows — with tracing, automated LLM-as-a-judge and heuristic evaluations, prompt management and optimization, and production dashboards. Comet also provides classic MLOps tooling for experiment management, model registry, artifacts, and production monitoring. Opik exposes a full REST API, Python and TypeScript SDKs, a CLI, and an official Model Context Protocol (MCP) server, and runs on Comet Cloud, self-hosted (Docker/Kubernetes), or enterprise deployments. Sector: ai-enterprise-software.'
image: https://cdn.comet.com/img/facebook-1200x630.png
layout: provider
mcp_servers:
- description: Official Model Context Protocol server for Opik. Connects MCP hosts (Claude Code, Cursor, VS Code Copilot) directly to an Opik workspace to read traces/spans/experiments/prompts, score outputs, save p
  name: Comet MCP Server
  slug: comet-mcp-server
modified: '2026-07-18'
name: Comet
nav: Providers
network: true
overview: 'Comet publishes 42 APIs on the [APIs.io](https://apis.io/) network, including Agent Configs API, Agent Insights API, Agent Insights Jobs API, and 39 more. Tagged areas include Company, Ai Enterprise Software, LLM Observability, LLMOps, and MLOps.


  Comet''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 16 more developer resources.'
random_paper: 11
score:
  band: developing
  composite: 49.3
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 16.7
    contract_quality: 52.0
    developer_ergonomics: 61.3
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 34.2
  previous_composite: 49.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 42
    mcp: first-party
    skills: derived
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/comet/refs/heads/main/screenshots/comet-2026-07-25T210115.png
security:
- kind: authentication
  name: Comet Authentication
  slug: comet-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Comet Domain Security
  slug: comet-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Comet Trust Center
  slug: comet-trust-center
  summary_line: SOC 2, ISO 27001
slug: comet
tags:
- Company
- Ai Enterprise Software
- LLM Observability
- LLMOps
- MLOps
- Evaluation
- Experiment Tracking
- Model Monitoring
- Prompt Management
- Agents
- Open-Source
website: https://www.comet.com/docs/opik/
---
