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
    agentic_access: true
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: true
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 86.5
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Exec Agentic Access
  operation_count: 32
  slug: exec-agentic-access
  summary_line: 32 operations · 11 acting
api_count: 9
apis:
- description: The Collections API from Exec — 1 operation(s) for collections.
  name: Exec Collections API
  slug: exec-collections-api
- description: The Knowledge Hub - Folders API from Exec — 2 operation(s) for knowledge hub - folders.
  name: Exec Knowledge Hub - Folders API
  slug: exec-knowledge-hub-folders-api
- description: The Knowledge Hub - Pages API from Exec — 3 operation(s) for knowledge hub - pages.
  name: Exec Knowledge Hub - Pages API
  slug: exec-knowledge-hub-pages-api
- description: The Knowledge Hub - Sources API from Exec — 2 operation(s) for knowledge hub - sources.
  name: Exec Knowledge Hub - Sources API
  slug: exec-knowledge-hub-sources-api
- description: The Scenario Studio API from Exec — 3 operation(s) for scenario studio.
  name: Exec Scenario Studio API
  slug: exec-scenario-studio-api
- description: The Scenarios API from Exec — 6 operation(s) for scenarios.
  name: Exec Scenarios API
  slug: exec-scenarios-api
- description: The Sessions API from Exec — 2 operation(s) for sessions.
  name: Exec Sessions API
  slug: exec-sessions-api
- description: The Skills API from Exec — 2 operation(s) for skills.
  name: Exec Skills API
  slug: exec-skills-api
- description: The Workspace API from Exec — 3 operation(s) for workspace.
  name: Exec Workspace API
  slug: exec-workspace-api
artifact_total: 16
asyncapis:
- description: ''
  name: Exec Webhooks
  slug: exec-webhooks
common:
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/exec-openapi-original.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/exec-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/exec-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/exec-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/exec-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/exec-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/exec-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/exec-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/exec-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.exec.com
- group: design
  title: ''
  type: Conformance
  url: conformance/exec-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.exec.com/enterprise-privacy
- group: auth
  title: ''
  type: TrustCenter
  url: https://app.vanta.com/exec.com/trust/j0xkhh5zesxvojinovqlpm
- group: design
  title: ''
  type: DataModel
  url: data-model/exec-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/exec-openapi-overlay.yaml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/exec-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/exec-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/exec-llms.txt
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.exec.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.exec.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.exec.com/api-reference/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.exec.com/api-reference/quickstart
- group: operate
  title: ''
  type: Support
  url: https://docs.exec.com
- group: company
  title: ''
  type: Blog
  url: https://www.exec.com/news
- group: commercial
  title: ''
  type: Pricing
  url: https://www.exec.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.exec.com/start
- group: start
  title: ''
  type: Login
  url: https://www.exec.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.exec.com/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.exec.com/privacy-policy
- group: company
  title: ''
  type: Website
  url: https://www.exec.com
created: '2026-07-17'
description: 'Exec is an AI-powered roleplay and sales-training platform (exec.com) for practicing high-stakes conversations. Teams run voice-based AI roleplays, automatically score real calls, build structured programs and certifications, coach one-on-one, and manage training content in a Knowledge Hub. The Exec REST API gives programmatic access to a workspace: members and groups, scenarios and collections, roleplay sessions and analytics, skills and proficiency, Scenario Studio job creation, and Knowledge Hub pages and sources. Backed by a16z.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/exec.png
layout: provider
mcp_servers:
- description: ''
  name: exec-mcp.yml
  slug: exec-mcpyml
modified: '2026-07-19'
name: Exec
nav: Providers
network: true
overview: 'Exec publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Collections API, Knowledge Hub - Folders API, Knowledge Hub - Pages API, and 6 more. Tagged areas include Company, Artificial Intelligence, Sales Enablement, Training, and Roleplay.


  The Exec catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Exec''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 24 more developer resources.'
random_paper: 13
rate_limits:
- limit_count: 3
  name: Exec Rate Limits
  slug: exec-rate-limits
score:
  band: developing
  composite: 59.9
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 68.6
    developer_ergonomics: 67.4
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 55.3
  previous_composite: 59.9
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Exec Authentication
  slug: exec-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Exec Domain Security
  slug: exec-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Exec Trust Center
  slug: exec-trust-center
  summary_line: SOC 2 Type II, SOC 3
slug: exec
tags:
- Company
- Artificial Intelligence
- Sales Enablement
- Training
- Roleplay
- Coaching
- Learning
- Knowledge Management
- LMS
website: https://www.exec.com
---
