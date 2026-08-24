---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: documented
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 51.1
  scored_at: '2026-08-24'
api_count: 5
apis:
- description: 'Deployment-scoped conversation operations for agents built on the Kore.ai Agent Platform: send a message to a deployed agent, run a one-shot completion, and stream an agent response over Server-Sent E'
  name: Kore.ai Agent Platform ABL Runtime API — Conversation
  slug: koreai-agent-platform-abl-runtime-api-conversation
- description: Invoke and execute deployed Kore.ai Agent Platform workflows, execute a pinned workflow version, and poll asynchronous workflow execution status.
  name: Kore.ai Agent Platform ABL Runtime API — Workflows
  slug: koreai-agent-platform-abl-runtime-api-workflows
- description: Read usage metrics for a Kore.ai Agent Platform project, with optional date range and grouping.
  name: Kore.ai Agent Platform ABL Runtime API — Sessions
  slug: koreai-agent-platform-abl-runtime-api-sessions
- description: The AI for Service REST estate — Automation AI (bot lifecycle, NLP training, analytics, admin, data tables), Search AI (answer generation, content and chunk management, ingestion, connectors), Contact
  name: Kore.ai AI for Service Platform APIs
  slug: koreai-ai-for-service-platform-apis
- description: A stdio Model Context Protocol server, @koreai/arch-mcp-tools, that exposes the Kore.ai Agent Platform control plane to an MCP client as 45 tools across build, evaluate, optimize, debug and analyze. I
  name: Kore.ai Arch MCP Server
  slug: koreai-arch-mcp-server
artifact_total: 12
asyncapis:
- description: ''
  name: Koreai Webhooks
  slug: koreai-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.kore.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.kore.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.kore.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.kore.ai/ai-for-service/apis/api-list
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.kore.ai/agent-platform/getting-started
- group: operate
  title: ''
  type: Support
  url: https://www.kore.ai/support
- group: company
  title: ''
  type: Blog
  url: https://www.kore.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Koredotcom
- group: start
  title: ''
  type: SignUp
  url: https://agents.kore.ai/auth/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.kore.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.kore.ai/privacy-policy
- group: build
  title: ''
  type: Postman
  url: https://github.com/Koredotcom/Public-APIs
- group: operate
  title: ''
  type: StatusPage
  url: https://status.kore.com/
- group: auth
  title: ''
  type: Compliance
  url: https://trust.kore.ai/
- group: auth
  title: ''
  type: TrustCenter
  url: security/koreai-trust-center.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/koreai-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.kore.ai/ai-for-service/release-notes/deprecations
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/koreai-changelog.yml
- group: build
  title: ''
  type: Packages
  url: packages/koreai-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/koreai-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/koreai-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/koreai-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/koreai-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/koreai-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/koreai-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/koreai-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/koreai-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/koreai-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/koreai-plans-pricing.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/koreai-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/koreai-domain-security.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/koreai-webhooks.yml
- group: design
  title: ''
  type: Components
  url: components/koreai-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/koreai-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/koreai-sandbox.yml
created: '2026-08-23'
description: Kore.ai is an enterprise conversational and agentic AI platform used to build, deploy, govern and observe AI agents for customer experience and employee experience work — contact center automation, voice AI, IT and HR service desks, agent assist, quality assurance and no-code agent orchestration. The company ships two API estates. The newer Agent Platform ("Artemis") on agents.kore.ai exposes an ABL Runtime API for chat, streaming, workflow invocation and session usage, an Agent Blueprint Language (ABL) DSL, and a 45-tool stdio MCP server (@koreai/arch-mcp-tools) that turns the platform's own control plane into agent tooling. The longer-established AI for Service estate on platform.kore.ai exposes a large REST surface across Automation AI, Search AI, Contact Center AI, Agent AI, Quality AI and Case Management, authenticated with JWT apps and governed by an assigned API-scope model. Kore.ai is headquartered in Orlando, Florida and is recognized as a Leader in the Gartner Magic
  Quadrant for Conversational AI, the Forrester Wave for Conversational AI Platforms and the Everest Group PEAK Matrix for Agentic AI Products.
image: https://cdn.prod.website-files.com/6717a0dfaf71071a80dfce8b/68c807cb7a0e90c787610ed0_Kore.ai%20OG%20Image.jpg
layout: provider
mcp_servers:
- description: ''
  name: Kore.ai MCP Server
  slug: koreai-mcp-server
modified: '2026-08-23'
name: Kore.ai
nav: Providers
network: true
overview: 'Kore.ai publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Agent Platform ABL Runtime API — Conversation, Agent Platform ABL Runtime API — Workflows, Agent Platform ABL Runtime API — Sessions, and 1 more. Tagged areas include Company, Artificial Intelligence, Conversational AI, Agents, and Agent Platform.


  The Kore.ai catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Kore.ai''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, changelog, and 29 more developer resources.'
plans:
- name: Koreai Plans Pricing
  plan_count: 0
  slug: koreai-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Koreai Rate Limits
  slug: koreai-rate-limits
score:
  band: strong
  composite: 59.9
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 30.3
    contract_quality: 58.3
    developer_ergonomics: 83.3
    discoverability: 81.5
    governance: 30.3
    operational_transparency: 52.6
  schema_version: 0.12.1
  scored_at: '2026-08-24'
security:
- kind: authentication
  name: Koreai Authentication
  slug: koreai-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Koreai Domain Security
  slug: koreai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Koreai Trust Center
  slug: koreai-trust-center
  summary_line: SOC 2 Type 2, PCI DSS, ISO/IEC 27001:2022, GDPR, CCPA, EU AI Act, DESC Cloud Service Provider
slug: koreai
tags:
- Company
- Artificial Intelligence
- Conversational AI
- Agents
- Agent Platform
- Contact Center
- Customer Experience
- Employee Experience
- Voice
- Automation
- Model Context Protocol
- Enterprise Software
website: https://www.kore.ai/
---
