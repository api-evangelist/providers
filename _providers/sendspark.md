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
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 51.6
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Sendspark Agentic Access
  operation_count: 23
  slug: sendspark-agentic-access
  summary_line: 23 operations · 14 acting
api_count: 1
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
artifact_total: 18
asyncapis:
- description: Outbound webhook event surface derived from the Sendspark REST API webhook management operations and the documented WebhookVideoEventsSchema. Subscribers are registered per workspace via POST /v1/work
  name: Sendspark Webhooks
  slug: sendspark-webhooks-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Sendspark DVM Bundles API
  slug: open-sendspark-dvm-bundles-api
- collection_type: open
  name: Sendspark DVM Bundles Dynamics Campaign API
  slug: open-sendspark-dynamics-campaign-api
- collection_type: open
  name: Sendspark DVM Bundles Webhook API
  slug: open-sendspark-webhook-api
- collection_type: open
  name: Sendspark DVM Bundles Workspace API
  slug: open-sendspark-workspace-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/sendspark-openapi-overlay.yaml
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
  url: https://help.sendspark.com/getting-started-guide-record-a-video
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
- group: other
  title: ''
  type: AgentCard
  url: a2a/sendspark-a2a.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/sendspark-published-skill.md
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/sendspark-tool-crosswalk.yml
- group: build
  title: ''
  type: Packages
  url: packages/sendspark-packages.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/sendspark-scopes.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/sendspark-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sendspark-rate-limits.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/sendspark-trust-center.yml
created: '2026-07-17'
description: Sendspark is a video messaging and AI-personalized video platform for sales and marketing teams. Users record a single video and use AI voice cloning, lip sync, merge tags, and dynamic thumbnails to personalize it to each prospect at scale, delivered through custom landing pages with embedded booking calendars and call-to-action buttons. Sendspark ships a Chrome extension and desktop recorder, 60+ CRM/email/automation integrations (HubSpot, Salesforce, Salesloft, Clay, Zapier, Make), a public REST API for Dynamic Video campaigns, prospects, DVM bundles, and outbound webhooks, and a hosted read-only MCP server for AI assistants. It was surfaced as a portfolio company of 500 Global.
image: https://www.sendspark.com/hubfs/favicon-96x96.png
layout: provider
mcp_servers:
- description: ''
  name: Sendspark MCP Server
  slug: sendspark-mcp-server
modified: '2026-08-13'
name: Sendspark
nav: Providers
network: true
overview: 'Sendspark publishes 4 APIs on the [APIs.io](https://apis.io/) network, including DVM Bundles API, Dynamics Campaign API, Webhook API, and 1 more. Tagged areas include Company, Video, Sales, Marketing, and Personalization.


  The Sendspark catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Sendspark''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 30 more developer resources.'
plans:
- name: Sendspark Plans Pricing
  plan_count: 5
  slug: sendspark-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 6
  name: Sendspark Rate Limits
  slug: sendspark-rate-limits
scopes:
- name: Sendspark Scopes
  scope_count: 4
  slug: sendspark-scopes
  summary_line: 4 scopes · authorizationCode/deviceCode/refreshToken
score:
  band: strong
  composite: 58.9
  coverage:
    artifact_dirs: 23
    catalog_gap: 54.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 84.2
    commercial_clarity: 84.2
    contract_governance: 4.5
    contract_quality: 62.4
    developer_ergonomics: 64.3
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 42.1
  previous_composite: 58.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
    skills: first-party
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sendspark/refs/heads/main/screenshots/sendspark-2026-08-17T081802.png
security:
- kind: authentication
  name: Sendspark Authentication
  slug: sendspark-authentication
  summary_line: apiKey/oauth2 · 3 schemes
- kind: domain-security
  name: Sendspark Domain Security
  slug: sendspark-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Sendspark Trust Center
  slug: sendspark-trust-center
  summary_line: trust center published
slug: sendspark
tags:
- Company
- Video
- Sales
- Marketing
- Personalization
- Artificial Intelligence
- Video Messaging
- Webhook
- MCP
website: https://sendspark.com
---
