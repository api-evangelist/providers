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
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 53.2
  scored_at: '2026-08-24'
api_count: 12
apis:
- description: The Analytics API from Sequel — 2 operation(s) for analytics.
  name: Sequel Analytics API
  slug: sequel-analytics-api
- description: The Client API from Sequel — 2 operation(s) for client.
  name: Sequel Client API
  slug: sequel-client-api
- description: Calls to managing companies
  name: Sequel company API
  slug: sequel-company-api
- description: The company theme API from Sequel — 1 operation(s) for company theme.
  name: Sequel company theme API
  slug: sequel-company-theme-api
- description: The company theme fonts API from Sequel — 2 operation(s) for company theme fonts.
  name: Sequel company theme fonts API
  slug: sequel-company-theme-fonts-api
- description: The company theme overrides API from Sequel — 1 operation(s) for company theme overrides.
  name: Sequel company theme overrides API
  slug: sequel-company-theme-overrides-api
- description: Calls to managing events
  name: Sequel event API
  slug: sequel-event-api
- description: The event theme API from Sequel — 1 operation(s) for event theme.
  name: Sequel event theme API
  slug: sequel-event-theme-api
- description: The event theme overrides API from Sequel — 1 operation(s) for event theme overrides.
  name: Sequel event theme overrides API
  slug: sequel-event-theme-overrides-api
- description: The Media API from Sequel — 2 operation(s) for media.
  name: Sequel Media API
  slug: sequel-media-api
- description: Calls to managing networking hubs
  name: Sequel networking API
  slug: sequel-networking-api
- description: The platform API from Sequel — 2 operation(s) for platform.
  name: Sequel platform API
  slug: sequel-platform-api
artifact_total: 33
asyncapis:
- description: ''
  name: Sequel Webhooks
  slug: sequel-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Introvoke Analytics API
  slug: open-sequel-analytics-api
- collection_type: open
  name: Introvoke Analytics Client API
  slug: open-sequel-client-api
- collection_type: open
  name: Introvoke Analytics company API
  slug: open-sequel-company-api
- collection_type: open
  name: Introvoke Analytics company theme API
  slug: open-sequel-company-theme-api
- collection_type: open
  name: Introvoke Analytics company theme fonts API
  slug: open-sequel-company-theme-fonts-api
- collection_type: open
  name: Introvoke Analytics company theme overrides API
  slug: open-sequel-company-theme-overrides-api
- collection_type: open
  name: Introvoke Analytics event API
  slug: open-sequel-event-api
- collection_type: open
  name: Introvoke Analytics event theme API
  slug: open-sequel-event-theme-api
- collection_type: open
  name: Introvoke Analytics event theme overrides API
  slug: open-sequel-event-theme-overrides-api
- collection_type: open
  name: Introvoke Analytics Media API
  slug: open-sequel-media-api
- collection_type: open
  name: Introvoke Analytics networking API
  slug: open-sequel-networking-api
- collection_type: open
  name: Introvoke Analytics platform API
  slug: open-sequel-platform-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/sequel-openapi-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://sequel.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.introvoke.com/docs
- group: docs
  title: ''
  type: Documentation
  url: https://docs.introvoke.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://docs.introvoke.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/introvoke/sequel-react-quickstart
- group: operate
  title: ''
  type: Support
  url: https://help.sequel.io/en/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/introvoke
- group: commercial
  title: ''
  type: Pricing
  url: https://sequel.io/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://sequel.io/book-a-demo
- group: start
  title: ''
  type: Login
  url: https://admin.sequel.io
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sequel.io/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sequel.io/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.sequel.io/
- group: auth
  title: ''
  type: Authentication
  url: authentication/sequel-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sequel-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/sequel-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/sequel-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/sequel-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/sequel-packages.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sequel-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/sequel-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/sequel-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/sequel-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/sequel-conformance.yml
- group: design
  title: ''
  type: Components
  url: components/sequel-components.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/sequel-webhooks.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sequel-llms.txt
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/sequel-tool-crosswalk.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/sequel-scopes.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/sequel-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sequel-rate-limits.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/sequel-changelog.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.sequel.io/
- group: auth
  title: ''
  type: Compliance
  url: https://trust.sequel.io/
- group: company
  title: ''
  type: Blog
  url: https://sequel.io/blog
- group: agent
  title: ''
  type: AgentSkill
  url: skills/sequel-create-and-embed-event.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/sequel-networking-hub-setup.md
created: '2026-07-17'
description: Sequel is a webinar and virtual-event platform for data-driven marketing teams. It runs live, simulive, and on-demand event experiences directly on a company's own domain, capturing unified first-party engagement data (watch time, polls, questions, CTA clicks) and syncing it to CRMs like Salesforce, HubSpot, Marketo, and Pardot. Sequel exposes a REST API (the Introvoke API) for managing companies, events, presenters, organizers, registrants, networking hubs, customization/theming, analytics, simulive video, MediaHub assets, and webhooks, plus pre-built embeddable video/networking components, a JavaScript SDK, and an official hosted MCP server that gives AI agents read access to webinar transcripts for content repurposing.
image: https://sequel.io/wp-content/themes/sequelio/assets/favicon-128x128.png
layout: provider
mcp_servers:
- description: Official Sequel MCP server. Makes event transcripts and audience/engagement data a native data source inside MCP-capable AI tools (the product page names Claude, ChatGPT, Microsoft Copilot and Gemini)
  name: Sequel MCP Server
  slug: sequel-mcp-server
modified: '2026-08-13'
name: Sequel
nav: Providers
network: true
overview: 'Sequel publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Analytics API, Client API, company API, and 9 more. Tagged areas include Company, Webinars, Virtual Events, Live Streaming, and Video.


  The Sequel catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Sequel''s developer surface includes documentation, API reference, getting-started guide, support, pricing, signup flow, authentication, and 31 more developer resources.'
plans:
- name: Sequel Plans Pricing
  plan_count: 3
  slug: sequel-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Sequel Rate Limits
  slug: sequel-rate-limits
scopes:
- name: Sequel Scopes
  scope_count: 0
  slug: sequel-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 60.8
  delta: 0.0
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 16.7
    contract_quality: 60.3
    developer_ergonomics: 53.0
    discoverability: 92.6
    governance: 16.7
    operational_transparency: 42.1
  previous_composite: 60.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: first-party
    skills: derived
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sequel/refs/heads/main/screenshots/sequel-2026-08-17T081812.png
security:
- kind: authentication
  name: Sequel Authentication
  slug: sequel-authentication
  summary_line: oauth2/http · 2 schemes
- kind: domain-security
  name: Sequel Domain Security
  slug: sequel-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Sequel Trust Center
  slug: sequel-trust-center
  summary_line: trust center published
slug: sequel
tags:
- Company
- Webinars
- Virtual Events
- Live Streaming
- Video
- Networking
- Marketing
- Event
- Webhook
website: https://sequel.io/
---
