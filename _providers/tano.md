---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
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
    well_known_catalog: true
  schema_version: 0.1
  score: 69.2
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Tano Agentic Access
  operation_count: 17
  slug: tano-agentic-access
  summary_line: 17 operations · 9 acting
api_count: 5
apis:
- description: Brand signups for product offerings (Creator Partnership Ads, Content Analysis Framework, Creator Discovery Guide, USA waitlist).
  name: Tano Brand Signups API
  slug: tano-brand-signups-api
- description: Contact form submissions and updates.
  name: Tano Contact API
  slug: tano-contact-api
- description: Creator-side signups.
  name: Tano Creator Signups API
  slug: tano-creator-signups-api
- description: Static discovery files for AI agents (llms.txt, manifests, sitemap).
  name: Tano Discovery API
  slug: tano-discovery-api
- description: Webinar and event registrations.
  name: Tano Events API
  slug: tano-events-api
artifact_total: 9
common:
- group: company
  title: ''
  type: Website
  url: https://tano.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://tano.ai/developers.md
- group: docs
  title: ''
  type: Documentation
  url: https://tano.ai/llms-full.txt
- group: docs
  title: ''
  type: APIReference
  url: https://tano.ai/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://tano.ai/agents.md
- group: operate
  title: ''
  type: Support
  url: mailto:team@tano.ai
- group: commercial
  title: ''
  type: Pricing
  url: https://tano.ai/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tano.ai/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tano.ai/privacy-policy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tano-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/tano-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/tano-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tano-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/tano-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/tano-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/tano-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tano-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/tano-conformance.yml
- group: design
  title: ''
  type: Components
  url: components/tano-components.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tano-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tano-domain-security.yml
created: '2026-07-17'
description: 'Tano is an AI-native influencer marketing agency and AI-powered creator marketing platform that manages end-to-end creator partnership ad campaigns on TikTok and Instagram — creator sourcing and vetting, outreach and contracts, payments, content rights, whitelisting permissions, and ad-ready asset delivery. Brands plug in budget and goals and Tano delivers ad-ready creator assets. It is a managed service with a dedicated account manager rather than self-serve SaaS, but exposes a strong agent-native surface: a public OpenAPI 3.1 intake API, a hosted MCP server (Streamable HTTP with MCP Apps embeddable UIs), an A2A agent card, an agent-skills index, an ai-plugin manifest, and llms.txt / agents.md discovery docs. Other services include Product Gifting and Affiliate Programme Management. Backed by Seedcamp.'
image: https://tano.ai/tano-og-image.png
layout: provider
mcp_servers:
- description: ''
  name: tano-mcp.yml
  slug: tano-mcpyml
modified: '2026-07-21'
name: Tano
nav: Providers
network: true
overview: 'Tano publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Brand Signups API, Contact API, Creator Signups API, and 2 more. Tagged areas include Company, Influencer Marketing, Creator Economy, Marketing, and Advertising.


  Tano''s developer surface includes documentation, API reference, getting-started guide, support, pricing, authentication, and 16 more developer resources.'
random_paper: 26
score:
  band: thin
  composite: 42.8
  delta: 0.0
  facets:
    commercial_clarity: 31.6
    contract_quality: 53.6
    developer_ergonomics: 65.2
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 42.8
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: authentication
  name: Tano Authentication
  slug: tano-authentication
  summary_line: none · 0 schemes
- kind: domain-security
  name: Tano Domain Security
  slug: tano-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tano
tags:
- Company
- Influencer Marketing
- Creator Economy
- Marketing
- Advertising
- Artificial Intelligence
- Social Media
- TikTok
- Instagram
- Agent Native
website: https://tano.ai
---
