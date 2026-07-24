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
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.1
  score: 83.7
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Sendspark Agentic Access
  operation_count: 23
  slug: sendspark-agentic-access
  summary_line: 23 operations · 14 acting
api_count: 4
apis:
- description: The DVM Bundles API from Sendspark — 3 operation(s) for dvm bundles.
  name: Sendspark DVM Bundles API
  slug: sendspark-dvm-bundles-api
- description: The Dynamics Campaign API from Sendspark — 12 operation(s) for dynamics campaign.
  name: Sendspark Dynamics Campaign API
  slug: sendspark-dynamics-campaign-api
- description: The Webhook API from Sendspark — 2 operation(s) for webhook.
  name: Sendspark Webhook API
  slug: sendspark-webhook-api
- description: The Workspace API from Sendspark — 2 operation(s) for workspace.
  name: Sendspark Workspace API
  slug: sendspark-workspace-api
artifact_total: 9
asyncapis:
- description: Outbound webhook event surface derived from the Sendspark REST API webhook management operations and the documented WebhookVideoEventsSchema. Subscribers are registered per workspace via POST /v1/work
  name: Sendspark Webhooks
  slug: sendspark-webhooks-asyncapi
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sendspark-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sendspark-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/sendspark-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/sendspark-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/sendspark-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/sendspark-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/sendspark-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sendspark-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.sendspark.com
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/sendspark-webhooks-asyncapi.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/sendspark-webhooks-asyncapi.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/sendspark-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/sendspark-manage-webhooks.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/sendspark-launch-dynamic-campaign.md
- group: agent
  title: ''
  type: WellKnown
  url: well-known/sendspark-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sendspark-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sendspark-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://help.sendspark.com
- group: docs
  title: ''
  type: Documentation
  url: https://help.sendspark.com
- group: docs
  title: ''
  type: APIReference
  url: https://help.sendspark.com/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://help.sendspark.com/mcp/overview
- group: operate
  title: ''
  type: Support
  url: https://help.sendspark.com
- group: company
  title: ''
  type: Blog
  url: https://blog.sendspark.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sendspark
- group: commercial
  title: ''
  type: Pricing
  url: https://www.sendspark.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://sendspark.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sendspark.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sendspark.com/privacy
- group: company
  title: ''
  type: Website
  url: https://sendspark.com
created: '2026-07-17'
description: Sendspark is a video messaging and AI-personalized video platform for sales and marketing teams. Users record a single video and use AI voice cloning, lip sync, merge tags, and dynamic thumbnails to personalize it to each prospect at scale, delivered through custom landing pages with embedded booking calendars and call-to-action buttons. Sendspark ships a Chrome extension and desktop recorder, 60+ CRM/email/automation integrations (HubSpot, Salesforce, Salesloft, Clay, Zapier, Make), a public REST API for Dynamic Video campaigns, prospects, DVM bundles, and outbound webhooks, and a hosted read-only MCP server for AI assistants. It was surfaced as a portfolio company of 500 Global.
image: https://www.sendspark.com/hubfs/favicon-96x96.png
layout: provider
mcp_servers:
- description: ''
  name: sendspark-mcp.yml
  slug: sendspark-mcpyml
modified: '2026-07-21'
name: Sendspark
nav: Providers
network: true
overview: 'Sendspark publishes 4 APIs on the [APIs.io](https://apis.io/) network, including DVM Bundles API, Dynamics Campaign API, Webhook API, and 1 more. Tagged areas include Company, Video, Sales, Marketing, and Personalization.


  The Sendspark catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Sendspark''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 22 more developer resources.'
random_paper: 2
score:
  band: developing
  composite: 53.4
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 69.0
    developer_ergonomics: 67.4
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 28.9
  previous_composite: 53.4
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Sendspark Authentication
  slug: sendspark-authentication
  summary_line: apiKey/oauth2 · 3 schemes
- kind: domain-security
  name: Sendspark Domain Security
  slug: sendspark-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sendspark
tags:
- Company
- Video
- Sales
- Marketing
- Personalization
- Artificial Intelligence
- Video Messaging
- Webhooks
- MCP
website: https://sendspark.com
---
