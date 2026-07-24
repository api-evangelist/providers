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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 65.4
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Cuein Agentic Access
  operation_count: 5
  slug: cuein-agentic-access
  summary_line: 5 operations · 1 acting
api_count: 2
apis:
- description: APIs for getting answers
  name: Cuein answers API
  slug: cuein-answers-api
- description: APIs for retrieving customer-support interaction insights
  name: Cuein conversations API
  slug: cuein-conversations-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cuein-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cuein-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cuein-authentication.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cuein-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/cuein-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cuein-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/cuein-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/cuein-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cuein-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cuein-lifecycle.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/cuein-trust-center.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.cuein.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://cuein-api.readme.io/docs/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://cuein-api.readme.io/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://cuein-api.readme.io/docs/getting-started
- group: company
  title: ''
  type: Blog
  url: https://cuein.ai/blog
- group: operate
  title: ''
  type: Support
  url: mailto:support@cuein.ai
- group: start
  title: ''
  type: SignUp
  url: https://app.cuein.ai
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cuein.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cuein.ai/privacy
created: '2026-07-17'
description: 'Cuein is an AI-native customer-experience platform ("co-pilot for customer experience teams") that unifies structured and unstructured customer-support data and applies generative AI to surface contact reasons, root causes, resolutions, and metrics such as Inferred CSAT and Resolution Rate. Its public developer surface exposes two REST APIs: an Insights API for retrieving per-conversation and bulk conversation insights over a date range, and an Answers API that generates answers grounded in a tenant''s knowledge articles and documents. Both APIs use x-api-key authentication and are documented on a ReadMe-hosted developer hub. Cuein was acquired by ServiceNow (announced Q1 2025); the standalone developer hub remains live. Backed by Lightspeed Venture Partners.'
image: https://files.readme.io/083b62d-Logo.svg
layout: provider
mcp_servers:
- description: ''
  name: cuein-mcp.yml
  slug: cuein-mcpyml
modified: '2026-07-18'
name: Cuein
nav: Providers
network: true
overview: 'Cuein publishes 2 APIs on the [APIs.io](https://apis.io/) network: answers API and conversations API. Tagged areas include Company, Customer Experience, Customer Support, Conversation Intelligence, and Generative AI.


  Cuein''s developer surface includes authentication, documentation, API reference, getting-started guide, engineering blog, support, signup flow, and 14 more developer resources.'
random_paper: 22
score:
  band: thin
  composite: 43.6
  delta: 0.0
  facets:
    commercial_clarity: 42.1
    contract_quality: 49.6
    developer_ergonomics: 67.4
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 43.6
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Cuein Authentication
  slug: cuein-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Cuein Domain Security
  slug: cuein-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Cuein Trust Center
  slug: cuein-trust-center
  summary_line: trust center published
slug: cuein
tags:
- Company
- Customer Experience
- Customer Support
- Conversation Intelligence
- Generative AI
- Insights
- Knowledge Base
- Contact Center
website: https://developer.cuein.ai/
---
