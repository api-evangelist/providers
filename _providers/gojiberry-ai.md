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
    well_known_catalog: false
  schema_version: 0.1
  score: 63.5
  scored_at: '2026-07-23'
api_count: 8
apis:
- description: The AppExternal API from Gojiberry AI — 2 operation(s) for appexternal.
  name: Gojiberry AI AppExternal API
  slug: gojiberry-ai-appexternal-api
- description: The Campaigns API from Gojiberry AI — 2 operation(s) for campaigns.
  name: Gojiberry AI Campaigns API
  slug: gojiberry-ai-campaigns-api
- description: The Contacts API from Gojiberry AI — 5 operation(s) for contacts.
  name: Gojiberry AI Contacts API
  slug: gojiberry-ai-contacts-api
- description: The Lead source agents API from Gojiberry AI — 3 operation(s) for lead source agents.
  name: Gojiberry AI Lead source agents API
  slug: gojiberry-ai-lead-source-agents-api
- description: The Lists API from Gojiberry AI — 2 operation(s) for lists.
  name: Gojiberry AI Lists API
  slug: gojiberry-ai-lists-api
- description: The Organization API from Gojiberry AI — 2 operation(s) for organization.
  name: Gojiberry AI Organization API
  slug: gojiberry-ai-organization-api
- description: The Unibox API from Gojiberry AI — 4 operation(s) for unibox.
  name: Gojiberry AI Unibox API
  slug: gojiberry-ai-unibox-api
- description: The User API from Gojiberry AI — 2 operation(s) for user.
  name: Gojiberry AI User API
  slug: gojiberry-ai-user-api
artifact_total: 13
asyncapis:
- description: ''
  name: Gojiberry Ai Webhooks
  slug: gojiberry-ai-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://gojiberry.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://ext.gojiberry.ai/documentation
- group: start
  title: ''
  type: Portal
  url: https://app.gojiberry.ai
- group: docs
  title: ''
  type: Documentation
  url: https://ext.gojiberry.ai/documentation
- group: docs
  title: ''
  type: APIReference
  url: https://ext.gojiberry.ai/documentation
- group: auth
  title: ''
  type: Authentication
  url: authentication/gojiberry-ai-authentication.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/gojiberry-ai-mcp.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/gojiberry-ai-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/gojiberry-ai-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/gojiberry-ai-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.gojiberry.ai/
- group: design
  title: ''
  type: Conformance
  url: conformance/gojiberry-ai-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/gojiberry-ai-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/gojiberry-ai-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gojiberry-ai-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/gojiberry-ai-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/gojiberry-ai-external-overlay.yaml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/gojiberry-ai-problem-types.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://gojiberry.ai/#pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.gojiberry.ai/registration
- group: start
  title: ''
  type: Login
  url: https://app.gojiberry.ai/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://gojiberry.ai/general-terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://gojiberry.ai/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://gojiberry.ai/faq
- group: company
  title: ''
  type: Blog
  url: https://blog.gojiberry.ai
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Gojiberry-ai
- group: other
  title: ''
  type: X
  url: https://x.com/gojiberryai
created: '2026-07-17'
description: Gojiberry AI is a Y Combinator-backed (P26), EU-hosted AI sales development platform that turns a company website into an autonomous go-to-market agent. The agent detects buying and social intent signals, scores prospects against an ideal customer profile, builds warm-lead lists, and runs multichannel (email and LinkedIn) outreach automatically. Gojiberry exposes a REST External API at ext.gojiberry.ai for programmatic access to contacts, campaigns, lists, lead-source agents, and the unified LinkedIn/email inbox (Unibox), plus a hosted Model Context Protocol (MCP) server so agents like Claude can run outreach and pull pipeline insights conversationally. Trusted by 2,000+ sales and GTM teams worldwide.
image: https://framerusercontent.com/images/0PsnqRXKIijGaB8ooIkfAThxHs.png
layout: provider
mcp_servers:
- description: ''
  name: gojiberry-ai-mcp.yml
  slug: gojiberry-ai-mcpyml
modified: '2026-07-19'
name: Gojiberry AI
nav: Providers
network: true
overview: 'Gojiberry AI publishes 8 APIs on the [APIs.io](https://apis.io/) network, including AppExternal API, Campaigns API, Contacts API, and 5 more. Tagged areas include Company, Sales, Lead Generation, Sales Intelligence, and AI Agents.


  The Gojiberry AI catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Gojiberry AI''s developer surface includes developer portal, documentation, API reference, authentication, pricing, signup flow, support, and 21 more developer resources.'
random_paper: 47
rate_limits:
- limit_count: 0
  name: Gojiberry Ai Rate Limits
  slug: gojiberry-ai-rate-limits
score:
  band: developing
  composite: 48.7
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 59.0
    developer_ergonomics: 56.5
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 28.9
  previous_composite: 48.7
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Gojiberry Ai Authentication
  slug: gojiberry-ai-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Gojiberry Ai Domain Security
  slug: gojiberry-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: gojiberry-ai
tags:
- Company
- Sales
- Lead Generation
- Sales Intelligence
- AI Agents
- Outbound
- Go-To-Market
- Prospecting
- LinkedIn
- CRM
website: https://gojiberry.ai
---
