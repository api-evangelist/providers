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
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.7
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Sendhub Agentic Access
  operation_count: 28
  slug: sendhub-agentic-access
  summary_line: 28 operations · 14 acting
api_count: 6
apis:
- description: Log in via Username & Password and "Sign In As User"
  name: SendHub Authentication API
  slug: sendhub-authentication-api
- description: Create and manage contacts.
  name: SendHub Contact API
  slug: sendhub-contact-api
- description: Create and manage groups.
  name: SendHub Group API
  slug: sendhub-group-api
- description: Send and manage messages.
  name: SendHub Message API
  slug: sendhub-message-api
- description: View and manage your account and lines
  name: SendHub Profile API
  slug: sendhub-profile-api
- description: View and manage inbox threads.
  name: SendHub Thread API
  slug: sendhub-thread-api
artifact_total: 20
asyncapis:
- description: ''
  name: Sendhub Webhooks
  slug: sendhub-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: SendHub Authentication API
  slug: open-sendhub-authentication-api
- collection_type: open
  name: SendHub Authentication Contact API
  slug: open-sendhub-contact-api
- collection_type: open
  name: SendHub Authentication Group API
  slug: open-sendhub-group-api
- collection_type: open
  name: SendHub Authentication Message API
  slug: open-sendhub-message-api
- collection_type: open
  name: SendHub Authentication Profile API
  slug: open-sendhub-profile-api
- collection_type: open
  name: SendHub Authentication Thread API
  slug: open-sendhub-thread-api
common:
- group: company
  title: ''
  type: Website
  url: https://sendhub.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://sendhub.com/developer/
- group: docs
  title: ''
  type: Documentation
  url: https://integrations.sendhub.com/SendHub-API-v1-Documentation.html
- group: docs
  title: ''
  type: APIReference
  url: https://integrations.sendhub.com/SendHub-API-v1-Documentation.html
- group: commercial
  title: ''
  type: Pricing
  url: https://sendhub.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://sendhub.com/blogs/
- group: operate
  title: ''
  type: Support
  url: https://support.sendhub.com/hc/en-us
- group: start
  title: ''
  type: SignUp
  url: https://app.sendhub.com/signup/
- group: start
  title: ''
  type: Login
  url: https://app.sendhub.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sendhub.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sendhub.com/privacy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sendhub
- group: auth
  title: ''
  type: Authentication
  url: authentication/sendhub-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sendhub-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sendhub-agentic-access.yml
- group: build
  title: ''
  type: Packages
  url: packages/sendhub-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/sendhub-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/sendhub-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sendhub-llms.txt
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/sendhub-error-codes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/sendhub-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/sendhub-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sendhub-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/sendhub-conformance.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/sendhub-openapi-overlay.yaml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/sendhub-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/sendhub-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sendhub-rate-limits.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://www.sendhub.com/developer/
created: '2026-07-17'
description: SendHub is a business text messaging platform for SMS/MMS marketing campaigns, two-way texting, appointment reminders, bulk messaging, SMS surveys, group messaging, and VoIP calling, used by more than 10,000 businesses. It exposes a REST-like v1 API at api.sendhub.com for programmatically managing contacts, groups, messages, inbox threads, account settings, and enterprise users, authenticated with a line username and API key (query params) or HTTP Basic. Published plans run Lite $19/mo to Basic $100/mo plus a quoted Custom tier, and every tier lists API access, though the developer page still says API access is custom-plan only. SendHub also supports 100+ integrations via direct connectors and Zapier plus inbound-SMS webhooks, and is a New Era Technology company. Surfaced as a 500 Global portfolio company and enriched by the API Evangelist pipeline.
image: https://www.sendhub.com/wp-content/uploads/2019/01/faviconsendhub-150x150.png
layout: provider
mcp_servers:
- description: ''
  name: SendHub MCP Server
  slug: sendhub-mcp-server
modified: '2026-08-13'
name: SendHub
nav: Providers
network: true
overview: 'SendHub publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Contact API, Group API, and 3 more. Tagged areas include Company, SMS, Messaging, Text Messaging, and Communications.


  The SendHub catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  SendHub''s developer surface includes documentation, API reference, pricing, engineering blog, support, signup flow, authentication, and 23 more developer resources.'
plans:
- name: Sendhub Plans Pricing
  plan_count: 5
  slug: sendhub-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Sendhub Rate Limits
  slug: sendhub-rate-limits
score:
  band: strong
  composite: 62.3
  delta: 0.0
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 30.3
    contract_quality: 69.2
    developer_ergonomics: 66.1
    discoverability: 92.6
    governance: 30.3
    operational_transparency: 10.5
  previous_composite: 62.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 44.4
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sendhub/refs/heads/main/screenshots/sendhub-2026-08-17T081802.png
security:
- kind: authentication
  name: Sendhub Authentication
  slug: sendhub-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Sendhub Domain Security
  slug: sendhub-domain-security
  summary_line: TLSv1.3 · DMARC
slug: sendhub
tags:
- Company
- SMS
- Messaging
- Text Messaging
- Communications
- Marketing
- Webhook
- VoIP
website: https://sendhub.com
---
