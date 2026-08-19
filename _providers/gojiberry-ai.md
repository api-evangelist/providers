---
access_model:
  confidence: high
  label: Self-serve signup, paid from $99/month
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - authentication
  - plans
  trial: true
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 51.9
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 9
  human_in_the_loop: 9
  name: Gojiberry Ai Agentic Access
  operation_count: 28
  slug: gojiberry-ai-agentic-access
  summary_line: 28 operations · 9 acting · 9 human-in-the-loop
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
artifact_total: 25
asyncapis:
- description: ''
  name: Gojiberry Ai Webhooks
  slug: gojiberry-ai-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Gojiberry AI - External AppExternal API
  slug: open-gojiberry-ai-appexternal-api
- collection_type: open
  name: Gojiberry AI - External AppExternal Campaigns API
  slug: open-gojiberry-ai-campaigns-api
- collection_type: open
  name: Gojiberry AI - External AppExternal Contacts API
  slug: open-gojiberry-ai-contacts-api
- collection_type: open
  name: Gojiberry AI - External AppExternal Lead source agents API
  slug: open-gojiberry-ai-lead-source-agents-api
- collection_type: open
  name: Gojiberry AI - External AppExternal Lists API
  slug: open-gojiberry-ai-lists-api
- collection_type: open
  name: Gojiberry AI - External AppExternal Organization API
  slug: open-gojiberry-ai-organization-api
- collection_type: open
  name: Gojiberry AI - External AppExternal Unibox API
  slug: open-gojiberry-ai-unibox-api
- collection_type: open
  name: Gojiberry AI - External AppExternal User API
  slug: open-gojiberry-ai-user-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/gojiberry-ai-agentic-access.yml
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
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/gojiberry-ai-tool-crosswalk.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/gojiberry-ai-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/gojiberry-ai-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/gojiberry-ai-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/gojiberry-ai-plans-pricing.yml
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
modified: '2026-08-13'
name: Gojiberry AI
nav: Providers
network: true
overview: 'Gojiberry AI publishes 8 APIs on the [APIs.io](https://apis.io/) network, including AppExternal API, Campaigns API, Contacts API, and 5 more. Tagged areas include Company, Sales, Lead Generation, Sales Intelligence, and AI Agents.


  The Gojiberry AI catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Gojiberry AI''s developer surface includes developer portal, documentation, API reference, authentication, pricing, signup flow, support, and 27 more developer resources.'
plans:
- name: Gojiberry Ai Plans Pricing
  plan_count: 2
  slug: gojiberry-ai-plans-pricing
random_paper: 28
rate_limits:
- limit_count: 1
  name: Gojiberry Ai Rate Limits
  slug: gojiberry-ai-rate-limits
scopes:
- name: Gojiberry Ai Scopes
  scope_count: 2
  slug: gojiberry-ai-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: developing
  composite: 50.0
  delta: -4.8
  facets:
    access_clarity: 59.2
    commercial_clarity: 59.2
    contract_governance: 16.7
    contract_quality: 53.7
    developer_ergonomics: 47.0
    discoverability: 92.6
    governance: 16.7
    operational_transparency: 31.6
  previous_composite: 54.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: first-party
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gojiberry-ai/refs/heads/main/screenshots/gojiberry-ai-2026-07-25T220016.png
security:
- kind: authentication
  name: Gojiberry Ai Authentication
  slug: gojiberry-ai-authentication
  summary_line: http/oauth2 · 2 schemes
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
