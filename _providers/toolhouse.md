---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - finops
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
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
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 48.6
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 57
  human_in_the_loop: 1
  name: Toolhouse Agentic Access
  operation_count: 124
  slug: toolhouse-agentic-access
  summary_line: 124 operations · 57 acting · 1 human-in-the-loop
api_count: 8
apis:
- description: The Toolhouse Workers API (historically the "Agents API") enables HTTP execution of any deployed Toolhouse worker. Workers defined via the Agent Editor or as code are reachable at https://agents.toolh
  name: Toolhouse Workers API
  slug: workers-api
- description: The Agent Runs API from Toolhouse — 4 operation(s) for agent runs.
  name: Toolhouse Agent Runs API
  slug: toolhouse-agent-runs-api
- description: The API Keys API from Toolhouse — 3 operation(s) for api keys.
  name: Toolhouse API Keys API
  slug: toolhouse-api-keys-api
- description: The Backoffice API from Toolhouse — 15 operation(s) for backoffice.
  name: Toolhouse Backoffice API
  slug: toolhouse-backoffice-api
- description: The Logs API from Toolhouse — 2 operation(s) for logs.
  name: Toolhouse Logs API
  slug: toolhouse-logs-api
- description: The Metrics API from Toolhouse — 4 operation(s) for metrics.
  name: Toolhouse Metrics API
  slug: toolhouse-metrics-api
- description: The SDK API API from Toolhouse — 20 operation(s) for sdk api.
  name: Toolhouse SDK API API
  slug: toolhouse-sdk-api-api
- description: The User API API from Toolhouse — 58 operation(s) for user api.
  name: Toolhouse User API API
  slug: toolhouse-user-api-api
artifact_total: 91
collections:
- collection_type: postman
  name: Toolhouse Agent Runs API
  slug: postman-toolhouse-agent-runs-api
- collection_type: postman
  name: Toolhouse Agent Runs API Keys API
  slug: postman-toolhouse-api-keys-api
- collection_type: postman
  name: Toolhouse Agent Runs Backoffice API
  slug: postman-toolhouse-backoffice-api
- collection_type: postman
  name: Toolhouse Agent Runs Logs API
  slug: postman-toolhouse-logs-api
- collection_type: postman
  name: Toolhouse Agent Runs Metrics API
  slug: postman-toolhouse-metrics-api
- collection_type: postman
  name: Toolhouse Agent Runs SDK API API
  slug: postman-toolhouse-sdk-api-api
- collection_type: postman
  name: Toolhouse Agent Runs User API API
  slug: postman-toolhouse-user-api-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/toolhouse/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/toolhouse-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/toolhouse-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/toolhouse-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://toolhouse.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.toolhouse.ai/toolhouse
- group: company
  title: ''
  type: Blog
  url: https://toolhouse.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://toolhouse.ai/pricing
- group: start
  title: ''
  type: Login
  url: https://app.toolhouse.ai
- group: company
  title: ''
  type: About
  url: https://toolhouse.ai/about
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/toolhouseai
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://toolhouse.ai/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://toolhouse.ai/tos
- group: company
  title: ''
  type: Twitter
  url: https://x.com/toolhouseai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/toolhouseai
- group: operate
  title: ''
  type: Discord
  url: https://discord.com/invite/xPvyBxhHtu
- group: learn
  title: ''
  type: YouTube
  url: https://youtube.com/@toolhouseai
- group: operate
  title: ''
  type: Support
  url: https://help.toolhouse.ai/
- group: operate
  title: ''
  type: StatusPage
  url: https://toolhouse.betteruptime.com/
- group: other
  title: ''
  type: Sitemap
  url: https://docs.toolhouse.ai/toolhouse/sitemap.md
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.toolhouse.ai/toolhouse/llms-full.txt
- group: build
  title: ''
  type: SDKs
  url: https://github.com/toolhouseai/toolhouse-sdk-python
- group: build
  title: ''
  type: SDKs
  url: https://github.com/toolhouseai/toolhouse-sdk-typescript
- group: build
  title: ''
  type: SDKs
  url: https://github.com/toolhouseai/client
- group: other
  title: ''
  type: OpenSource
  url: https://github.com/toolhouseai/mcp-distributed
- group: build
  title: ''
  type: SampleApplications
  url: https://github.com/toolhouseai/toolhouse-examples
- group: build
  title: ''
  type: SampleApplication
  url: https://github.com/toolhouseai/fastlane-demo
- group: build
  title: ''
  type: Tools
  url: https://github.com/toolhouseai/toolhouse-assessment
- group: build
  title: ''
  type: SampleApplication
  url: https://github.com/toolhouseai/toolhouse-teleprompter
- group: build
  title: ''
  type: SampleApplication
  url: https://github.com/toolhouseai/toolhouse-agenticlabs
- group: docs
  title: ''
  type: Documentation
  url: https://docs.toolhouse.ai/toolhouse/developers/workers-api
- group: auth
  title: ''
  type: Authentication
  url: https://docs.toolhouse.ai/toolhouse/developers/authentication
- group: operate
  title: ''
  type: ChangeLog
  url: https://toolhouse.ai/blog/toolhouse-changelog-august-2025
- group: other
  title: ''
  type: Article
  url: https://toolhouse.ai/blog/introducing-mcp-discovery-effortless-agent-superpowers-in-toolhouse
- group: other
  title: ''
  type: Article
  url: https://toolhouse.ai/blog/introducing-toolhouse-rag-free-yourself-from-rag-complexity
- group: other
  title: ''
  type: Article
  url: https://toolhouse.ai/blog/connect-toolhouse-agents-to-zapier-in-minutes
- group: other
  title: ''
  type: Article
  url: https://toolhouse.ai/blog/now-running-on-together-ai-models
- group: commercial
  title: ''
  type: Plans
  url: plans/toolhouse-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/toolhouse-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/toolhouse-finops.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/toolhouse-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/toolhouse-agent-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/toolhouse-agent-structure.json
- group: design
  title: ''
  type: SpectralRules
  url: rules/toolhouse-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/toolhouse-vocabulary.yml
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/toolhouseai/toolhouse-mcp
created: '2026-03-26'
description: 'Toolhouse is a Backend-as-a-Service platform for building, deploying, and managing "AI workers" (Toolhouse''s current product noun, used interchangeably with "AI agents"). The homepage frames the value proposition as "Turn your AI chats into affordable and reliable AI workers that do work while you''re busy," and the docs define a worker as "a system that carries out a task with three components: a trigger, a process that may include specialized skills, and tools or systems it can connect to." Builders describe a task in plain language in the Agent Editor and ship a worker to production; developers can do the same programmatically via SDKs. Every worker is automatically wired into Toolhouse''s pre-integrated capabilities, including web and social media search, scraping, Toolhouse RAG, persistent memory, the Virtual Computer code-execution sandbox, image generation/editing and vision, document parsing, file download, and MCP Discovery for connecting to thousands of MCP servers
  at runtime. The platform exposes a Workers API (agents.toolhouse.ai) for invoking deployed workers over REST with text and NDJSON streaming and stateful conversation continuity (X-Toolhouse-Run-ID), a Platform API for full worker and run lifecycle management, scheduling (10-minute minimum cadence), metrics, monetization, and integrations, plus no-code workflow integration through Zapier and Toolhouse n8n Nodes. Toolhouse runs on a broad model substrate including OpenAI, Anthropic, Together AI, Groq, and NVIDIA model offerings. The current public pricing surface is Business ($500/mo, 25,000 credits, 50 workers), Business Max ($1,200/mo, 80,000 credits, 500 workers), and custom Enterprise — all plans include "free unlimited tokens" and a 14-day free trial. Toolhouse reports 7,000+ teams on the platform and 40+ integrations and is backed by NextGenerationEU funding.'
examples:
- key_count: 4
  name: Toolhouse List Agents Example
  slug: toolhouse-list-agents-example
- key_count: 4
  name: Toolhouse Upsert Agent Example
  slug: toolhouse-upsert-agent-example
features:
- name: AI Worker Deployment from a Prompt (Agent Editor)
- name: Agent Studio (v2)
- name: Workers API (REST + Streaming + NDJSON)
- name: Stateful Conversational Memory (X-Toolhouse-Run-ID)
- name: Attachments via URL or Base64 (10 MB max)
- name: MCP Discovery
- name: MCP Server Integration
- name: Toolhouse RAG
- name: Skills and Knowledge (Templates, Guidelines, Reference)
- name: Virtual Computer (Python Sandbox)
- name: Browser Automation
- name: Web and Social Media Search
- name: Image Generation, Editing, and Vision
- name: Document Parser
- name: File Download
- name: Memory
- name: Scheduled Worker Runs (cron, 10-minute floor)
- name: Worker Email Inbox
- name: Worker Run Logs (incl. MCP Server Logs)
- name: Worker Run Metrics And Volume Reporting
- name: API Key Management
- name: Organizations
- name: Agent Subscriptions, Monetization, and Transfer
- name: Streaming Responses (Text + NDJSON)
- name: Free Unlimited Tokens On All Plans
finops:
- name: Toolhouse Finops
  service_category: API
  slug: toolhouse-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/toolhouse.png
integrations:
- name: OpenAI
- name: Anthropic Claude
- name: Together AI
- name: Groq
- name: NVIDIA (Llama 3.1 Nemotron 70B)
- name: Tavily (Official Partner)
- name: Vercel AI SDK
- name: LlamaIndex
- name: n8n (Toolhouse n8n Nodes)
- name: Zapier
- name: Supabase
- name: Lovable
- name: GitHub
- name: GitLab
- name: Bitbucket
- name: Stripe
- name: Square
- name: QuickBooks
- name: Salesforce
- name: HubSpot
- name: Microsoft Dynamics 365
- name: Google Workspace (Sheets, Docs, Drive)
- name: Microsoft Teams
- name: Slack
- name: Discord
- name: Notion
- name: MCP Clients (via MCP Server and MCP Discovery)
json_schemas:
- name: Toolhouse Agent
  property_count: 16
  slug: toolhouse-agent
json_structures:
- name: Toolhouse Agent Structure
  property_count: 0
  slug: toolhouse-agent-structure
jsonld:
- class_count: 0
  name: Toolhouse Context
  property_count: 12
  slug: toolhouse-context
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-22'
name: Toolhouse
nav: Providers
network: true
overview: 'Toolhouse publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Agent Runs API, API Keys API, Backoffice API, and 4 more. Tagged areas include Agent Infrastructure, AI Agents, AI Workers, Backend as a Service, and MCP.


  The Toolhouse catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Toolhouse''s developer surface includes authentication, documentation, engineering blog, pricing, YouTube channel, support, tooling, and 39 more developer resources.'
random_paper: 66
rate_limits:
- limit_count: 10
  name: Toolhouse Rate Limits
  slug: toolhouse-rate-limits
rules:
- name: Toolhouse API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: toolhouse-jsonschema-spectral-rules
- name: Toolhouse API Rules
  rule_count: 10
  severity_counts:
    error: 3
    hint: 1
    info: 0
    warn: 6
  slug: toolhouse-rules
score:
  band: strong
  composite: 58.0
  delta: -2.9
  facets:
    commercial_clarity: 52.6
    contract_quality: 57.8
    developer_ergonomics: 54.3
    discoverability: 81.5
    governance: 68.8
    operational_transparency: 44.7
  previous_composite: 60.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
security:
- kind: authentication
  name: Toolhouse Authentication
  slug: toolhouse-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Toolhouse Domain Security
  slug: toolhouse-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: toolhouse
tags:
- Agent Infrastructure
- AI Agents
- AI Workers
- Backend as a Service
- MCP
- MCP Discovery
- RAG
- Tools
- Workers API
use_cases:
- name: AI Worker Backend-as-a-Service
- name: Deal Analysis and Market Research Automation
- name: Document Processing (Policy Abstraction, Summarization, Query)
- name: Knowledge Assistants For Policy and Business Data
- name: Lead Generation and Outbound Automation (SMS, Cold Calling, Inbound)
- name: Marketing and Content Creation (Listings, Copy, Image Generation)
- name: Automated Worker Scheduling
- name: Tool-Augmented LLM Pipelines
- name: Agent Studio Chat
- name: MCP Client Integration
- name: Production Worker Deployment
website: https://toolhouse.ai/
---
