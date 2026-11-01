---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 56.3
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 185
  human_in_the_loop: 6
  name: Orq Agentic Access
  operation_count: 330
  slug: orq-agentic-access
  summary_line: 330 operations · 185 acting · 6 human-in-the-loop
api_count: 1
apis:
- baseURL: https://my.orq.ai
  baseurl_source: declared
  description: The Agent Feedback API from Orq.ai — 1 operation(s) for agent feedback.
  name: Orq.ai Agent Feedback API
  slug: orq-agent-feedback-api
- baseURL: https://my.orq.ai
  baseurl_source: declared
  description: Run agents on a cron cadence. Minimum firing interval is 1 hour.
  name: Orq.ai Agent Schedules API
  slug: orq-agent-schedules-api
- baseURL: https://my.orq.ai
  baseurl_source: declared
  description: The Agents API from Orq.ai — 12 operation(s) for agents.
  name: Orq.ai Agents API
  slug: orq-agents-api
- baseURL: https://my.orq.ai
  baseurl_source: declared
  description: 'Alerts evaluate a Reporting API metric on a fixed interval and fire notifications through notifiers when the value breaches a threshold. Each breach opens a trigger that tracks the incident until the '
  name: Orq.ai Alerts API
  slug: orq-alerts-api
- baseURL: https://my.orq.ai
  baseurl_source: declared
  description: Annotation queues collect spans for human review.
  name: Orq.ai Annotation Queues API
  slug: orq-annotation-queues-api
- baseURL: https://my.orq.ai
  baseurl_source: declared
  description: The Annotations API from Orq.ai — 1 operation(s) for annotations.
  name: Orq.ai Annotations API
  slug: orq-annotations-api
- baseURL: https://my.orq.ai
  baseurl_source: declared
  description: API keys authenticate programmatic access to the workspace. They expose opaque tokens, per-domain access grants, and budget and rate-limit constraints.
  name: Orq.ai API keys API
  slug: orq-api-keys-api
- baseURL: https://my.orq.ai
  baseurl_source: declared
  description: The Audio API from Orq.ai — 3 operation(s) for audio.
  name: Orq.ai Audio API
  slug: orq-audio-api
- baseURL: https://my.orq.ai
  baseurl_source: declared
  description: Audit logs record workspace entity changes and access-relevant events.
  name: Orq.ai Audit Logs API
  slug: orq-audit-logs-api
- baseURL: https://my.orq.ai
  baseurl_source: declared
  description: 'Budgets govern spend, token usage, and request rate across six scopes: workspace, project, identity, API key, provider, and model. Every applicable budget is enforced, and the most restrictive limit a'
  name: Orq.ai Budgets API
  slug: orq-budgets-api
- baseURL: https://my.orq.ai
  baseurl_source: declared
  description: Split text into smaller chunks for retrieval and generation workflows.
  name: Orq.ai Chunking API
  slug: orq-chunking-api
- baseURL: https://my.orq.ai
  baseurl_source: declared
  description: Beta. Run typed classification questions against a classify model.
  name: Orq.ai Classify API
  slug: orq-classify-api
- baseURL: https://my.orq.ai
  baseurl_source: declared
  description: The Completions API from Orq.ai — 1 operation(s) for completions.
  name: Orq.ai Completions API
  slug: orq-completions-api
- baseURL: https://my.orq.ai
  baseurl_source: declared
  description: The Datasets API from Orq.ai — 5 operation(s) for datasets.
  name: Orq.ai Datasets API
  slug: orq-datasets-api
- baseURL: https://my.orq.ai
  baseurl_source: declared
  description: Beta. Run classification decisions with the classify contract.
  name: Orq.ai Decisions API
  slug: orq-decisions-api
- baseURL: https://my.orq.ai
  baseurl_source: declared
  description: The Deployments API from Orq.ai — 5 operation(s) for deployments.
  name: Orq.ai Deployments API
  slug: orq-deployments-api
- baseURL: https://my.orq.ai
  baseurl_source: declared
  description: The Embeddings API from Orq.ai — 1 operation(s) for embeddings.
  name: Orq.ai Embeddings API
  slug: orq-embeddings-api
- baseURL: https://my.orq.ai
  baseurl_source: declared
  description: Run an evaluator against a conversation and its result
  name: Orq.ai Evals API
  slug: orq-evals-api
- baseURL: https://my.orq.ai
  baseurl_source: declared
  description: The Feedback API from Orq.ai — 2 operation(s) for feedback.
  name: Orq.ai Feedback API
  slug: orq-feedback-api
- baseURL: https://my.orq.ai
  baseurl_source: declared
  description: File upload and retrieval operations.
  name: Orq.ai Files API
  slug: orq-files-api
- baseURL: https://my.orq.ai
  baseurl_source: declared
  description: Guardrail Rules conditionally enforce evaluators and plugins for AI Gateway traffic. Rules may be scoped to a project or the whole workspace.
  name: Orq.ai Guardrail Rules API
  slug: orq-guardrail-rules-api
- baseURL: https://my.orq.ai
  baseurl_source: declared
  description: Hub items are reusable templates available to a workspace.
  name: Orq.ai Hub API
  slug: orq-hub-api
- baseURL: https://my.orq.ai
  baseurl_source: declared
  description: The Human Review Sets API from Orq.ai — 2 operation(s) for human review sets.
  name: Orq.ai Human Review Sets API
  slug: orq-human-review-sets-api
- baseURL: https://my.orq.ai
  baseurl_source: declared
  description: Identities represent end users from your system for usage and engagement tracking.
  name: Orq.ai Identities API
  slug: orq-identities-api
- baseURL: https://my.orq.ai
  baseurl_source: declared
  description: The Images API from Orq.ai — 3 operation(s) for images.
  name: Orq.ai Images API
  slug: orq-images-api
- baseURL: https://my.orq.ai
  baseurl_source: declared
  description: Create and manage knowledge bases used by agents and retrieval workflows.
  name: Orq.ai Knowledge Bases API
  slug: orq-knowledge-bases-api
- baseURL: https://my.orq.ai
  baseurl_source: declared
  description: OpenTelemetry log query API. Search, filter, aggregate, and facet log records ingested via OTLP.
  name: Orq.ai Logs API
  slug: orq-logs-api
- baseURL: https://my.orq.ai
  baseurl_source: declared
  description: Management keys are workspace-scoped credentials that authenticate programmatic access to workspace administration surfaces (API keys, budgets). Unlike project-scoped API keys, a management key always
  name: Orq.ai Management keys API
  slug: orq-management-keys-api
- baseURL: https://my.orq.ai
  baseurl_source: declared
  description: Register upstream MCP servers, discover and sync their tools, and assemble gateways that expose a curated tool surface to MCP clients.
  name: Orq.ai MCP Gateway API
  slug: orq-mcp-gateway-api
- baseURL: https://my.orq.ai
  baseurl_source: declared
  description: Create and manage memory stores, memories, and memory documents.
  name: Orq.ai Memory Stores API
  slug: orq-memory-stores-api
- baseURL: https://my.orq.ai
  baseurl_source: declared
  description: 'Browse the orq.ai model catalog: every model orq offers, across every provider, with pricing, capabilities and benchmark data. List endpoints only return models that are not deprecated. This API is pu'
  name: Orq.ai Model Catalog API
  slug: orq-model-catalog-api
- baseURL: https://my.orq.ai
  baseurl_source: declared
  description: List models available through the AI Router.
  name: Orq.ai Models API
  slug: orq-models-api
- baseURL: https://my.orq.ai
  baseurl_source: declared
  description: The Moderations API from Orq.ai — 1 operation(s) for moderations.
  name: Orq.ai Moderations API
  slug: orq-moderations-api
- baseURL: https://my.orq.ai
  baseurl_source: declared
  description: Monitors are custom observability dashboards for traces, runtime metrics, and logs. Each monitor holds widgets that chart one telemetry query. List the metrics, operations, and dimensions available to
  name: Orq.ai Monitors API
  slug: orq-monitors-api
- baseURL: https://my.orq.ai
  baseurl_source: declared
  description: Notifier destinations used to send delivery and workflow notifications.
  name: Orq.ai Notifiers API
  slug: orq-notifiers-api
- baseURL: https://my.orq.ai
  baseurl_source: declared
  description: The Pii API from Orq.ai — 4 operation(s) for pii.
  name: Orq.ai Pii API
  slug: orq-pii-api
- baseURL: https://my.orq.ai
  baseurl_source: declared
  description: The Policies API from Orq.ai — 2 operation(s) for policies.
  name: Orq.ai Policies API
  slug: orq-policies-api
- baseURL: https://my.orq.ai
  baseurl_source: declared
  description: Projects organize resources within a workspace
  name: Orq.ai Projects API
  slug: orq-projects-api
- baseURL: https://my.orq.ai
  baseurl_source: declared
  description: The Prompts API from Orq.ai — 4 operation(s) for prompts.
  name: Orq.ai Prompts API
  slug: orq-prompts-api
- baseURL: https://my.orq.ai
  baseurl_source: declared
  description: GenAI reporting API over canonical analytics rollups. Accepts a metric name, time range, grain, group-by, and filters; returns a typed time series and optional totals.
  name: Orq.ai Reporting API
  slug: orq-reporting-api
- baseURL: https://my.orq.ai
  baseurl_source: declared
  description: The Rerank API from Orq.ai — 1 operation(s) for rerank.
  name: Orq.ai Rerank API
  slug: orq-rerank-api
- baseURL: https://my.orq.ai
  baseurl_source: declared
  description: The Responses API from Orq.ai — 2 operation(s) for responses.
  name: Orq.ai Responses API
  slug: orq-responses-api
- baseURL: https://my.orq.ai
  baseurl_source: declared
  description: The Router API from Orq.ai — 1 operation(s) for router.
  name: Orq.ai Router API
  slug: orq-router-api
- baseURL: https://my.orq.ai
  baseurl_source: declared
  description: Routing Rules conditionally select models and enforce request plugins for AI Gateway traffic. Rules are evaluated by ascending priority and may be scoped to a project or the whole workspace.
  name: Orq.ai Routing Rules API
  slug: orq-routing-rules-api
- baseURL: https://my.orq.ai
  baseurl_source: declared
  description: Skills are modular instructions you can use to codify processes and conventions
  name: Orq.ai Skills API
  slug: orq-skills-api
- baseURL: https://my.orq.ai
  baseurl_source: declared
  description: Create and manage workspace Smart Routers. A Smart Router selects a model from an eligible pool for each request according to a quality, balanced, or cost profile.
  name: Orq.ai Smart Routers API
  slug: orq-smart-routers-api
- baseURL: https://my.orq.ai
  baseurl_source: declared
  description: Unified query envelope for traces, metrics, and logs. One request shape, one filter dialect, and one response shape per source, validated by a per-source registry.
  name: Orq.ai Telemetry API
  slug: orq-telemetry-api
- baseURL: https://my.orq.ai
  baseurl_source: declared
  description: Threads group related trace invocations and their aggregate usage
  name: Orq.ai Threads API
  slug: orq-threads-api
- baseURL: https://my.orq.ai
  baseurl_source: declared
  description: The Tools API from Orq.ai — 4 operation(s) for tools.
  name: Orq.ai Tools API
  slug: orq-tools-api
- baseURL: https://my.orq.ai
  baseurl_source: declared
  description: 'Query and inspect ingested trace data: search trace summaries, aggregate metrics, and read individual traces and their spans.'
  name: Orq.ai Traces API
  slug: orq-traces-api
- baseURL: https://my.orq.ai
  baseurl_source: declared
  description: Workspace user administration. Requires a Management Key with user permissions or an authenticated workspace admin session. Standard API keys are not supported.
  name: Orq.ai Users API
  slug: orq-users-api
- baseURL: https://my.orq.ai
  baseurl_source: declared
  description: The Views API from Orq.ai — 2 operation(s) for views.
  name: Orq.ai Views API
  slug: orq-views-api
- baseURL: https://my.orq.ai
  baseurl_source: declared
  description: Search Gateway with managed credits or BYOK.
  name: Orq.ai Web Search API
  slug: orq-web-search-api
- baseURL: https://my.orq.ai
  baseurl_source: declared
  description: Create and manage webhooks that deliver workspace events to external HTTPS endpoints.
  name: Orq.ai Webhooks API
  slug: orq-webhooks-api
- baseURL: https://my.orq.ai
  baseurl_source: declared
  description: Workspace-level domain verification and IP allowlist controls. These operations are restricted to workspace administrators.
  name: Orq.ai Workspace Security API
  slug: orq-workspace-security-api
- baseURL: https://my.orq.ai
  baseurl_source: declared
  description: Workspace-level settings managed with a workspace credential. A workspace is the tenant, so these settings are a singleton — there is nothing to create or delete, only read and update.
  name: Orq.ai Workspace Settings API
  slug: orq-workspace-settings-api
- baseURL: https://my.orq.ai
  baseurl_source: declared
  description: A workspace is the tenant. Create is called from a user session during onboarding; Get, List, and Update are the public management surface.
  name: Orq.ai Workspaces API
  slug: orq-workspaces-api
- baseURL: https://my.orq.ai
  baseurl_source: declared
  description: The Chat Completions API from Orq.ai — 1 operation(s) for chat completions.
  name: Orq.ai Chat Completions API
  slug: orq-chat-completions-api
- baseURL: https://my.orq.ai
  baseurl_source: declared
  description: Create and manage persistent file systems that agents and MCP clients read from and write to.
  name: Orq.ai Filesystems API
  slug: orq-filesystems-api
artifact_total: 75
asyncapis:
- description: ''
  name: Orq Webhooks
  slug: orq-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/orq/agentic-access/orq-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/orq-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/orq/plans/orq-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/orq-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/orq/rules/orq-rules.yml
  title: ''
  type: Spectral
  url: rules/orq-rules.yml
- group: design
  href: https://artifacts.apis.io/orq/json-ld/orq-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/orq-context.jsonld
- group: design
  href: https://artifacts.apis.io/orq/vocabulary/orq-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/orq-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/orq/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/orq/asyncapi/orq-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/orq-webhooks.yml
- group: design
  href: https://artifacts.apis.io/orq/data-model/orq-data-model.yml
  title: ''
  type: DataModel
  url: data-model/orq-data-model.yml
- group: operate
  href: https://artifacts.apis.io/orq/changelog/orq-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/orq-changelog.yml
- group: auth
  href: https://artifacts.apis.io/orq/security/orq-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/orq-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/orq/errors/orq-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/orq-problem-types.yml
- group: design
  href: https://artifacts.apis.io/orq/conformance/orq-conformance.yml
  title: ''
  type: Conformance
  url: conformance/orq-conformance.yml
- group: agent
  href: https://artifacts.apis.io/orq/llms/orq-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/orq-llms.txt
- group: other
  href: https://artifacts.apis.io/orq/a2a/orq-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/orq-a2a.yml
- group: auth
  href: https://artifacts.apis.io/orq/well-known/orq-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/orq-security.txt
- group: auth
  href: https://artifacts.apis.io/orq/well-known/orq-docs-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/orq-docs-security.txt
- group: agent
  href: https://artifacts.apis.io/orq/well-known/orq-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/orq-well-known.yml
- group: other
  href: https://artifacts.apis.io/orq/hosts/orq-hosts.yml
  title: ''
  type: Hosts
  url: hosts/orq-hosts.yml
- group: other
  href: https://artifacts.apis.io/orq/vendors/orq-vendors.yml
  title: ''
  type: Vendors
  url: vendors/orq-vendors.yml
- group: auth
  href: https://artifacts.apis.io/orq/authentication/orq-authentication.yml
  title: ''
  type: Authentication
  url: authentication/orq-authentication.yml
- group: auth
  href: https://artifacts.apis.io/orq/security/orq-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/orq-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/orq/security/orq-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/orq-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://orq.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://orq.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.orq.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.orq.ai/reference/client-libraries
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.orq.ai/ai-gateway/get-started/introduction
- group: operate
  title: ''
  type: Support
  url: https://orq.ai/contact
- group: company
  title: ''
  type: Blog
  url: https://orq.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://orq.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://my.orq.ai/auth/signup
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://orq.ai/privacy
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/orq/workspace
created: '2026-10-21'
description: Orq.ai provides a sovereign AI gateway and software factory enabling enterprises to build, govern, and deploy AI-driven applications with robust observability, risk management, and compliance features. The platform offers AI model management, policy enforcement, and a unified API to integrate large language models, tools, and custom agents, targeting use cases from coding assistants to enterprise AI governance.
image: https://framerusercontent.com/images/2WPqC5CejT04oQzpwkTC8lYFeL0.jpg
json_schemas:
- name: Agent Started Event
  property_count: 3
  slug: orq-agent-started-streaming-event
- name: Agent Thought Event
  property_count: 3
  slug: orq-agent-thought-streaming-event
- name: InvokeDeploymentRequest
  property_count: 14
  slug: orq-invoke-deployment-request
- name: ModelMetadata
  property_count: 124
  slug: orq-model-metadata
- name: Response Stream Event
  property_count: 0
  slug: orq-response-stream-event
- name: SearchKnowledgeRequest
  property_count: 9
  slug: orq-search-knowledge-request
jsonld:
- class_count: 120
  name: Orq Context
  property_count: 153
  slug: orq-context
layout: provider
modified: '2026-10-21'
name: Orq.ai
nav: Providers
network: true
overview: 'Orq.ai publishes 59 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agent Feedback API, Agent Schedules API, Agents API, and 56 more. Tagged areas include AI, Platform, Enterprise, Governance, and SoftwareFactory.


  The Orq.ai catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Orq.ai''s developer surface includes changelog, authentication, documentation, API reference, getting-started guide, support, engineering blog, and 26 more developer resources.'
plans:
- name: Orq Plans Pricing
  plan_count: 1
  slug: orq-plans-pricing
random_paper: 2
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: Orq.ai API Rules
  rule_count: 16
  severity_counts:
    error: 6
    hint: 0
    info: 2
    warn: 8
  slug: orq-rules
score:
  band: strong
  composite: 58.5
  coverage:
    artifact_dirs: 22
    catalog_earned: 70.8
    catalog_earned_first_party: 8.0
    catalog_gap: 44.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 55.3
    contract_governance: 35.6
    contract_quality: 71.7
    developer_ergonomics: 63.7
    discoverability: 66.1
    operational_transparency: 34.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 59
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Orq Authentication
  slug: orq-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Orq Domain Security
  slug: orq-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Orq Vulnerability Disclosure
  slug: orq-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 2
skills:
- name: orq-create-user
  slug: orq-create-user
- name: orq-manage-identities
  slug: orq-manage-identities
slug: orq
tags:
- AI
- Platform
- Enterprise
- Governance
- SoftwareFactory
website: https://orq.ai/
---
