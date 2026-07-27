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
  band: agent-native
  dimensions:
    agent_skills: true
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.1
  score: 67.3
  scored_at: '2026-07-27'
api_count: 15
apis:
- description: The Agent API from Langdock — 2 operation(s) for agent.
  name: Langdock Agent API
  slug: langdock-agent-api
- description: The Agent Build API from Langdock — 4 operation(s) for agent build.
  name: Langdock Agent Build API
  slug: langdock-agent-build-api
- description: The Assistant API from Langdock — 2 operation(s) for assistant.
  name: Langdock Assistant API
  slug: langdock-assistant-api
- description: The Assistant Build API from Langdock — 3 operation(s) for assistant build.
  name: Langdock Assistant Build API
  slug: langdock-assistant-build-api
- description: The Attachments API from Langdock — 2 operation(s) for attachments.
  name: Langdock Attachments API
  slug: langdock-attachments-api
- description: The Audit Logs API from Langdock — 1 operation(s) for audit logs.
  name: Langdock Audit Logs API
  slug: langdock-audit-logs-api
- description: The Chat API from Langdock — 1 operation(s) for chat.
  name: Langdock Chat API
  slug: langdock-chat-api
- description: The Embeddings API from Langdock — 1 operation(s) for embeddings.
  name: Langdock Embeddings API
  slug: langdock-embeddings-api
- description: The fim API from Langdock — 1 operation(s) for fim.
  name: Langdock fim API
  slug: langdock-fim-api
- description: The Google API from Langdock — 1 operation(s) for google.
  name: Langdock Google API
  slug: langdock-google-api
- description: The Knowledge API from Langdock — 4 operation(s) for knowledge.
  name: Langdock Knowledge API
  slug: langdock-knowledge-api
- description: The Messages API from Langdock — 1 operation(s) for messages.
  name: Langdock Messages API
  slug: langdock-messages-api
- description: The Skills API from Langdock — 3 operation(s) for skills.
  name: Langdock Skills API
  slug: langdock-skills-api
- description: The Usage Export API from Langdock — 5 operation(s) for usage export.
  name: Langdock Usage Export API
  slug: langdock-usage-export-api
- description: The User Management API from Langdock — 2 operation(s) for user management.
  name: Langdock User Management API
  slug: langdock-user-management-api
artifact_total: 22
asyncapis:
- description: ''
  name: Langdock Webhooks
  slug: langdock-webhooks
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/langdock-trust-center.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.langdock.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.langdock.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.langdock.com/en/developer/overview/api-introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.langdock.com/en/developer/overview/api-introduction
- group: learn
  title: ''
  type: Cookbook
  url: https://docs.langdock.com/en/developer/overview/cookbook
- group: company
  title: ''
  type: Website
  url: https://www.langdock.com/
- group: company
  title: ''
  type: Blog
  url: https://www.langdock.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.langdock.com/contact-us
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Langdock
- group: commercial
  title: ''
  type: Pricing
  url: https://www.langdock.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.langdock.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.langdock.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.langdock.com/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.langdock.com/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/langdock-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.langdock.com/security
- group: auth
  title: ''
  type: Security
  url: https://www.langdock.com/vulnerability-disclosure-policy
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/langdock-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/langdock-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/langdock-authentication.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/langdock-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/langdock-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/langdock-packages.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/langdock-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/langdock-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/langdock-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/langdock-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/langdock-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/langdock-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/langdock-data-model.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/langdock-well-known.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/langdock-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Langdock is an enterprise AI platform — "The Platform for AI Adoption" — that lets organizations deploy model-agnostic AI across their workforce through Chat, Workflows, Agents, Skills, Integrations, and a public API. The platform is EU-hosted on Microsoft Azure with ISO 27001 and SOC 2 Type II certification and GDPR alignment, and supports multi-tenant SaaS, single-tenant SaaS, bring-your-own-cloud, and on-premise Kubernetes deployment. The Langdock API exposes provider-compatible completion and embedding endpoints for OpenAI, Anthropic, Google Gemini, and Mistral models across EU and US regions, alongside first-party Agents, Skills, Knowledge Folder, Integrations, Audit Logs, Usage Export, and User Management APIs, plus a hosted Model Context Protocol server that exposes workspace agents as MCP tools.
image: https://www.langdock.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: langdock-mcp.yml
  slug: langdock-mcpyml
modified: '2026-07-19'
name: Langdock
nav: Providers
network: true
overview: 'Langdock publishes 15 APIs on the [APIs.io](https://apis.io/) network, including Agent API, Agent Build API, Assistant API, and 12 more. Tagged areas include Company, Artificial Intelligence, Enterprise AI, LLM, and Agents.


  The Langdock catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Langdock''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, signup flow, and 27 more developer resources.'
random_paper: 19
rate_limits:
- limit_count: 2
  name: Langdock Rate Limits
  slug: langdock-rate-limits
score:
  band: strong
  composite: 62.8
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 65.1
    developer_ergonomics: 67.4
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 84.2
  previous_composite: 62.8
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/langdock/refs/heads/main/screenshots/langdock-2026-07-25T224521.png
security:
- kind: authentication
  name: Langdock Authentication
  slug: langdock-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Langdock Domain Security
  slug: langdock-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Langdock Vulnerability Disclosure
  slug: langdock-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Langdock Trust Center
  slug: langdock-trust-center
  summary_line: SOC 2 Type II, ISO 27001, GDPR
slug: langdock
tags:
- Company
- Artificial Intelligence
- Enterprise AI
- LLM
- Agents
- Model Context Protocol
- Workflows
- Knowledge Management
- Germany
- Europe
website: https://www.langdock.com/
---
