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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.9
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 30
  human_in_the_loop: 0
  name: Arcade Agentic Access
  operation_count: 56
  slug: arcade-agentic-access
  summary_line: 56 operations · 30 acting
api_count: 11
apis:
- description: 'The ArcadeAI/schemas repo on GitHub publishes versioned JSON Schemas for the Arcade engine configuration (1.0 and 2.0) and the worker HTTP contracts (1.0) — tool_definition, execute_tool_request, and '
  name: Arcade Public Schemas
  slug: arcade-public-schemas
- description: The arcade-mcp open-source Python framework — "MCP Server Framework and Tool Development library for building custom capabilities into agents." Provides the `arcade` CLI (login, new, show, evals, mcp,
  name: Arcade MCP Framework
  slug: arcade-mcp-framework
- description: The Arcade integration catalog — 145 MCP servers across Arcade Optimized, Arcade Unoptimized, Verified, Community, and Auth Provider designations, with 37 additional "Coming Soon" integrations includi
  name: Arcade Integration Catalog
  slug: arcade-integration-catalog
- description: The Admin API from Arcade — 14 operation(s) for admin.
  name: Arcade Admin API
  slug: arcade-admin-api
- description: The Authorization API from Arcade — 4 operation(s) for authorization.
  name: Arcade Authorization API
  slug: arcade-authorization-api
- description: The Gateways API from Arcade — 3 operation(s) for gateways.
  name: Arcade Gateways API
  slug: arcade-gateways-api
- description: The Hooks API from Arcade — 3 operation(s) for hooks.
  name: Arcade Hooks API
  slug: arcade-hooks-api
- description: The LLM API from Arcade — 1 operation(s) for llm.
  name: Arcade LLM API
  slug: arcade-llm-api
- description: The Operations API from Arcade — 3 operation(s) for operations.
  name: Arcade Operations API
  slug: arcade-operations-api
- description: The Plugins API from Arcade — 2 operation(s) for plugins.
  name: Arcade Plugins API
  slug: arcade-plugins-api
- description: The Tools API from Arcade — 9 operation(s) for tools.
  name: Arcade Tools API
  slug: arcade-tools-api
artifact_total: 145
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Arcade Admin API
  slug: open-arcade-admin-api
- collection_type: open
  name: Arcade Admin Authorization API
  slug: open-arcade-authorization-api
- collection_type: open
  name: Arcade API
  slug: open-arcade-engine
- collection_type: open
  name: Arcade Admin Gateways API
  slug: open-arcade-gateways-api
- collection_type: open
  name: Arcade Admin Hooks API
  slug: open-arcade-hooks-api
- collection_type: open
  name: Arcade Admin LLM API
  slug: open-arcade-llm-api
- collection_type: open
  name: Arcade Admin Operations API
  slug: open-arcade-operations-api
- collection_type: open
  name: Arcade Admin Plugins API
  slug: open-arcade-plugins-api
- collection_type: open
  name: Arcade Admin Tools API
  slug: open-arcade-tools-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/ArcadeAI/schemas/issues
- group: commercial
  title: ''
  type: License
  url: https://github.com/ArcadeAI/schemas/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/arcade-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/arcade-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/arcade-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://arcade.dev
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.arcade.dev
- group: start
  title: ''
  type: Signup
  url: https://api.arcade.dev/dashboard
- group: start
  title: ''
  type: Console
  url: https://api.arcade.dev/dashboard
- group: commercial
  title: ''
  type: Pricing
  url: https://arcade.dev/pricing
- group: commercial
  title: ''
  type: Plans
  url: plans/arcade-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/arcade-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/arcade-finops.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://arcade.dev/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://arcade.dev/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://arcade.dev/blog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.arcade.dev
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.arcade.dev/en/references/changelog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ArcadeAI
- group: operate
  title: ''
  type: Support
  url: mailto:contact@arcade.dev
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/arcade-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/arcade-context.jsonld
- group: design
  title: ''
  type: SpectralRules
  url: rules/arcade-engine-rules.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.arcade.dev/llms.txt
created: '2026-05-22'
description: Arcade.dev is the MCP runtime for production AI agent deployments. The Arcade Engine — a hosted or self-hostable API surface — handles OAuth user authorization, manages user tokens, and exposes 7,000+ pre-built integrations as Model Context Protocol tools that agent frameworks like LangChain, OpenAI Agents, CrewAI, AG2, Google ADK, Vercel AI, Mastra, and TanStack AI can call. This profile catalogs the public Arcade Engine API (39 endpoints across Admin, Authorization, Tools, LLM, Operations, Hooks, Gateways, and Plugins), the ArcadeAI GitHub org's SDKs, the arcade-mcp framework, and the public schemas repo.
examples:
- key_count: 5
  name: Arcade Engine Arcade Health Example
  slug: arcade-engine-arcade-health-example
- key_count: 4
  name: Arcade Engine Auth Connections Delete Example
  slug: arcade-engine-auth-connections-delete-example
- key_count: 5
  name: Arcade Engine Auth Connections List Example
  slug: arcade-engine-auth-connections-list-example
- key_count: 6
  name: Arcade Engine Auth Providers Create Example
  slug: arcade-engine-auth-providers-create-example
- key_count: 5
  name: Arcade Engine Auth Providers Delete Example
  slug: arcade-engine-auth-providers-delete-example
- key_count: 5
  name: Arcade Engine Auth Providers Get Example
  slug: arcade-engine-auth-providers-get-example
- key_count: 5
  name: Arcade Engine Auth Providers List Example
  slug: arcade-engine-auth-providers-list-example
- key_count: 6
  name: Arcade Engine Auth Providers Update Example
  slug: arcade-engine-auth-providers-update-example
- key_count: 5
  name: Arcade Engine Auth Status Example
  slug: arcade-engine-auth-status-example
- key_count: 6
  name: Arcade Engine Confirm User Auth Flow Example
  slug: arcade-engine-confirm-user-auth-flow-example
- key_count: 5
  name: Arcade Engine Engine Config Example
  slug: arcade-engine-engine-config-example
- key_count: 6
  name: Arcade Engine Hooks Bulk Upsert Example
  slug: arcade-engine-hooks-bulk-upsert-example
- key_count: 6
  name: Arcade Engine Hooks Create Example
  slug: arcade-engine-hooks-create-example
- key_count: 4
  name: Arcade Engine Hooks Delete Example
  slug: arcade-engine-hooks-delete-example
- key_count: 5
  name: Arcade Engine Hooks Get Example
  slug: arcade-engine-hooks-get-example
- key_count: 5
  name: Arcade Engine Hooks List Example
  slug: arcade-engine-hooks-list-example
- key_count: 6
  name: Arcade Engine Hooks Update Example
  slug: arcade-engine-hooks-update-example
- key_count: 6
  name: Arcade Engine Initiate Authorization Example
  slug: arcade-engine-initiate-authorization-example
- key_count: 6
  name: Arcade Engine Llm Chat Example
  slug: arcade-engine-llm-chat-example
- key_count: 6
  name: Arcade Engine Plugins Create Example
  slug: arcade-engine-plugins-create-example
- key_count: 4
  name: Arcade Engine Plugins Delete Example
  slug: arcade-engine-plugins-delete-example
- key_count: 5
  name: Arcade Engine Plugins Get Example
  slug: arcade-engine-plugins-get-example
- key_count: 5
  name: Arcade Engine Plugins List Example
  slug: arcade-engine-plugins-list-example
- key_count: 6
  name: Arcade Engine Plugins Update Example
  slug: arcade-engine-plugins-update-example
- key_count: 6
  name: Arcade Engine Project Gateways Create Example
  slug: arcade-engine-project-gateways-create-example
- key_count: 4
  name: Arcade Engine Project Gateways Delete Example
  slug: arcade-engine-project-gateways-delete-example
- key_count: 5
  name: Arcade Engine Project Gateways Get Example
  slug: arcade-engine-project-gateways-get-example
- key_count: 5
  name: Arcade Engine Project Gateways List Example
  slug: arcade-engine-project-gateways-list-example
- key_count: 6
  name: Arcade Engine Project Gateways Patch Example
  slug: arcade-engine-project-gateways-patch-example
- key_count: 6
  name: Arcade Engine Project Gateways Slug Info Example
  slug: arcade-engine-project-gateways-slug-info-example
- key_count: 6
  name: Arcade Engine Project Gateways Update Example
  slug: arcade-engine-project-gateways-update-example
- key_count: 4
  name: Arcade Engine Secrets Delete Example
  slug: arcade-engine-secrets-delete-example
- key_count: 5
  name: Arcade Engine Secrets List Example
  slug: arcade-engine-secrets-list-example
- key_count: 6
  name: Arcade Engine Secrets Upsert Example
  slug: arcade-engine-secrets-upsert-example
- key_count: 5
  name: Arcade Engine Session Verification Settings Get Example
  slug: arcade-engine-session-verification-settings-get-example
- key_count: 6
  name: Arcade Engine Session Verification Settings Update Example
  slug: arcade-engine-session-verification-settings-update-example
- key_count: 5
  name: Arcade Engine Swagger Example
  slug: arcade-engine-swagger-example
- key_count: 6
  name: Arcade Engine Test Authorization Flow Example
  slug: arcade-engine-test-authorization-flow-example
- key_count: 6
  name: Arcade Engine Tool Authorize Example
  slug: arcade-engine-tool-authorize-example
- key_count: 6
  name: Arcade Engine Tool Execute Example
  slug: arcade-engine-tool-execute-example
- key_count: 6
  name: Arcade Engine Tool Requirements Example
  slug: arcade-engine-tool-requirements-example
- key_count: 5
  name: Arcade Engine Tool Scheduled Get Example
  slug: arcade-engine-tool-scheduled-get-example
- key_count: 5
  name: Arcade Engine Tool Scheduled List Example
  slug: arcade-engine-tool-scheduled-list-example
- key_count: 5
  name: Arcade Engine Tool Spec Example
  slug: arcade-engine-tool-spec-example
- key_count: 5
  name: Arcade Engine Tool Spec Formatted Example
  slug: arcade-engine-tool-spec-formatted-example
- key_count: 5
  name: Arcade Engine Tools List Example
  slug: arcade-engine-tools-list-example
- key_count: 5
  name: Arcade Engine Tools List Formatted Example
  slug: arcade-engine-tools-list-formatted-example
- key_count: 5
  name: Arcade Engine Tools List Static Example
  slug: arcade-engine-tools-list-static-example
- key_count: 5
  name: Arcade Engine Workers Authorize Example
  slug: arcade-engine-workers-authorize-example
- key_count: 6
  name: Arcade Engine Workers Create Example
  slug: arcade-engine-workers-create-example
- key_count: 4
  name: Arcade Engine Workers Delete Example
  slug: arcade-engine-workers-delete-example
- key_count: 5
  name: Arcade Engine Workers Get Example
  slug: arcade-engine-workers-get-example
- key_count: 5
  name: Arcade Engine Workers Health Example
  slug: arcade-engine-workers-health-example
- key_count: 5
  name: Arcade Engine Workers List Example
  slug: arcade-engine-workers-list-example
- key_count: 6
  name: Arcade Engine Workers Test Example
  slug: arcade-engine-workers-test-example
- key_count: 6
  name: Arcade Engine Workers Update Example
  slug: arcade-engine-workers-update-example
features:
- description: Hosted and self-hostable Model Context Protocol runtime that turns tool definitions into multi-user, authorized invocations for agents.
  name: MCP Runtime
- description: Built-in OAuth and identity-provider flows across 30+ named auth providers plus a generic OAuth 2.0 provider; per-user tokens managed without service-account workarounds.
  name: Managed OAuth Authorization
- description: 145 MCP servers across Arcade Optimized, Unoptimized, Verified, Community, and Auth Provider designations, with 37 more 'Coming Soon'.
  name: Tool Catalog
- description: First-class adapters for LangChain, OpenAI Agents, CrewAI, AG2, Google ADK, Vercel AI, Mastra, and TanStack AI.
  name: Agent-Framework Integrations
- description: '`arcade evals` CLI runs scripted tool-calling evals to gate releases on behavior, not just compile-time checks.'
  name: Evaluations
- description: Per-execution logs across the Engine plus dashboards; audit logs and compliance reporting are part of the Enterprise tier.
  name: Observability
- description: Pre- and post-call hooks plus pluggable verifiers and policy modules under /v1/hooks and /v1/plugins.
  name: Hooks and Plugins
- description: Customer-owned verification flows (e.g. Stytch, Supabase) gating tool execution via /v1/auth/validate_custom_verifier.
  name: Custom User Verifiers
- description: Tools can be registered to fire on a schedule via /v1/scheduled_tools instead of synchronously from an agent.
  name: Scheduled Tools
- description: Cloud, VPC, on-premises, or air-gapped — explicitly called out on the homepage.
  name: Deployment Flexibility
- description: Marketplace for publishing and monetizing agent-ready tools.
  name: Arcade Registry (beta)
finops:
- name: Arcade Finops
  service_category: ''
  slug: arcade-finops
image: https://avatars.githubusercontent.com/u/161780576
integrations:
- description: First-class LangChain integration; partnership extended via LangSmith Fleet announcement on 2026-04-07.
  name: LangChain
- description: Python adapter via openai-agents-arcade for using Arcade tools inside the OpenAI Agents SDK.
  name: OpenAI Agents
- description: Documented framework integration in docs.arcade.dev.
  name: CrewAI
- description: Framework support added in the 2026-04-10 changelog.
  name: AG2
- description: Adapter via google-adk-arcade Python library.
  name: Google ADK
- description: arcade-vercel-ai-template demonstrating Arcade tools inside Vercel AI SDK chatbots.
  name: Vercel AI
- description: Documented framework integration.
  name: Mastra
- description: Documented framework integration.
  name: TanStack AI
- description: Multiple Claude Code routines and on-call workflows shipped from the Arcade blog through April–May 2026.
  name: Anthropic Claude Code
- description: Asana, Atlassian, Discord, Dropbox, GitHub, Google, HubSpot, Linear, LinkedIn, Microsoft, Notion, Reddit, Slack, Spotify, Twitch, X, Zoom, Airtable, Attio, Calendly, ClickUp, Figma, Mailchimp, Miro, PagerDuty, Salesforce, Square, TickTick, Zendesk, Zoho, plus a generic OAuth 2.0 provider.
  name: Auth Providers
json_schemas:
- name: Arcade Engine AuthProviderResponse
  property_count: 9
  slug: arcade-engine-auth-provider-response
- name: Arcade Engine AuthorizationResponse
  property_count: 7
  slug: arcade-engine-authorization-response
- name: Arcade Engine AuthorizeToolRequest
  property_count: 4
  slug: arcade-engine-authorize-tool-request
- name: Arcade Engine ExecuteToolRequest
  property_count: 6
  slug: arcade-engine-execute-tool-request
- name: Arcade Engine ExecuteToolResponse
  property_count: 9
  slug: arcade-engine-execute-tool-response
- name: Arcade Engine GatewayResponse
  property_count: 14
  slug: arcade-engine-gateway-response
- name: Arcade Engine HookResponse
  property_count: 14
  slug: arcade-engine-hook-response
- name: Arcade Engine PluginResponse
  property_count: 14
  slug: arcade-engine-plugin-response
- name: Arcade Engine SecretResponse
  property_count: 4
  slug: arcade-engine-secret-response
- name: Arcade Engine ToolExecutionDetailResponse
  property_count: 14
  slug: arcade-engine-tool-execution-detail
- name: Arcade Engine ToolResponse
  property_count: 10
  slug: arcade-engine-tool-response
- name: Arcade Engine WorkerResponse
  property_count: 8
  slug: arcade-engine-worker-response
- name: Arcade Execute Tool Request
  property_count: 7
  slug: arcade-execute-tool-request
- name: Arcade Execute Tool Response
  property_count: 6
  slug: arcade-execute-tool-response
- name: Arcade Tool Definition
  property_count: 8
  slug: arcade-tool-definition
json_structures:
- name: Arcade Engine Auth Provider Response Structure
  property_count: 9
  slug: arcade-engine-auth-provider-response-structure
- name: Arcade Engine Authorization Response Structure
  property_count: 7
  slug: arcade-engine-authorization-response-structure
- name: Arcade Engine Authorize Tool Request Structure
  property_count: 4
  slug: arcade-engine-authorize-tool-request-structure
- name: Arcade Engine Execute Tool Request Structure
  property_count: 6
  slug: arcade-engine-execute-tool-request-structure
- name: Arcade Engine Execute Tool Response Structure
  property_count: 9
  slug: arcade-engine-execute-tool-response-structure
- name: Arcade Engine Gateway Response Structure
  property_count: 14
  slug: arcade-engine-gateway-response-structure
- name: Arcade Engine Hook Response Structure
  property_count: 14
  slug: arcade-engine-hook-response-structure
- name: Arcade Engine Plugin Response Structure
  property_count: 14
  slug: arcade-engine-plugin-response-structure
- name: Arcade Engine Secret Response Structure
  property_count: 4
  slug: arcade-engine-secret-response-structure
- name: Arcade Engine Tool Execution Detail Structure
  property_count: 14
  slug: arcade-engine-tool-execution-detail-structure
- name: Arcade Engine Tool Response Structure
  property_count: 10
  slug: arcade-engine-tool-response-structure
- name: Arcade Engine Worker Response Structure
  property_count: 8
  slug: arcade-engine-worker-response-structure
jsonld:
- class_count: 30
  name: Arcade Context
  property_count: 12
  slug: arcade-context
layout: provider
modified: '2026-05-22'
name: Arcade
nav: Providers
network: true
overview: 'Arcade publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Admin API, Authorization API, Gateways API, and 5 more. Tagged areas include Agents, MCP, AI Agents, Authorization, and Authentication.


  The Arcade catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Arcade''s developer surface includes authentication, developer portal, signup flow, developer console, pricing, engineering blog, changelog, and 17 more developer resources.'
plans:
- name: Arcade Plans Pricing
  plan_count: 4
  slug: arcade-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Arcade Rate Limits
  slug: arcade-rate-limits
rules:
- effective_rule_count: 49
  extends:
  - spectral:oas
  name: Arcade API Rules
  rule_count: 8
  severity_counts:
    error: 3
    hint: 0
    info: 1
    warn: 4
  slug: arcade-engine-rules
- effective_rule_count: 5
  extends: []
  name: Arcade API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: arcade-jsonschema-spectral-rules
score:
  band: strong
  composite: 61.3
  delta: 0.0
  facets:
    access_clarity: 84.2
    commercial_clarity: 84.2
    contract_governance: 69.7
    contract_quality: 74.2
    developer_ergonomics: 35.7
    discoverability: 59.3
    governance: 69.7
    operational_transparency: 34.2
  previous_composite: 61.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/arcade/refs/heads/main/screenshots/arcade-2026-06-20T172354.png
security:
- kind: authentication
  name: Arcade Authentication
  slug: arcade-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Arcade Domain Security
  slug: arcade-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: arcade
solutions:
- description: Arcade-hosted MCP servers, metered on the Growth plan at $0.05 per server-hour.
  name: Cloud Deployment
- description: Deploy the Engine inside the customer's VPC — called out on the homepage as a supported topology.
  name: VPC Deployment
- description: Self-hosted Engine and workers for regulated environments.
  name: On-Premises Deployment
- description: Disconnected deployments for the highest-control environments.
  name: Air-Gapped Deployment
- description: Custom pricing for companies under 100 employees, nonprofits, and educational institutions via contact@arcade.dev.
  name: Startup Program
tags:
- Agents
- MCP
- AI Agents
- Authorization
- Authentication
- Tool Calling
- Agent Infrastructure
- LLM
- Integration
use_cases:
- description: Agents that act on behalf of distinct end users — Gmail/Calendar/Slack/Salesforce assistants — without shared service credentials.
  name: Multi-User AI Assistant
- description: Moving agents from prototype to production with governed OAuth, evals, and observability per the May 2026 CISO governance post.
  name: Production Agent Deployment
- description: An ingress in front of one or more workers within a project applying routing, headers, and policies.
  name: Enterprise MCP Gateway
- description: On-call reliability and runbook automation per Arcade's 'AI SRE with Claude Code' blog series.
  name: Agent SRE
- description: Multi-step workflows across Salesforce, HubSpot, Attio, Slack, Linear, Jira, Asana, ClickUp, Notion, Google Workspace, and Microsoft Office.
  name: Sales and Productivity Automation
- description: WhatsApp / Telegram / Slack assistants powered by the toolkits and the Arcade Engine.
  name: Voice and Chat Assistants
website: https://docs.arcade.dev
---
