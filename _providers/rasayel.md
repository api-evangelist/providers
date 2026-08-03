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
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.4
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Rasayel Agentic Access
  operation_count: 22
  slug: rasayel-agentic-access
  summary_line: 22 operations · 13 acting
api_count: 7
apis:
- description: The Channels API from Rasayel — 1 operation(s) for channels.
  name: Rasayel Channels API
  slug: rasayel-channels-api
- description: The Contacts API from Rasayel — 5 operation(s) for contacts.
  name: Rasayel Contacts API
  slug: rasayel-contacts-api
- description: The Conversations API from Rasayel — 2 operation(s) for conversations.
  name: Rasayel Conversations API
  slug: rasayel-conversations-api
- description: The Messages API from Rasayel — 1 operation(s) for messages.
  name: Rasayel Messages API
  slug: rasayel-messages-api
- description: The Properties API from Rasayel — 2 operation(s) for properties.
  name: Rasayel Properties API
  slug: rasayel-properties-api
- description: The Tags API from Rasayel — 1 operation(s) for tags.
  name: Rasayel Tags API
  slug: rasayel-tags-api
- description: The Templates API from Rasayel — 2 operation(s) for templates.
  name: Rasayel Templates API
  slug: rasayel-templates-api
artifact_total: 12
common:
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/rasayel-rest-openapi.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/rasayel-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/rasayel-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/rasayel-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/rasayel-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/rasayel-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.rasayel.io/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/rasayel-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/rasayel-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/rasayel-conformance.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/rasayel-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/rasayel-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/rasayel-rest-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/rasayel-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rasayel-domain-security.yml
- group: build
  title: ''
  type: Postman
  url: https://rest.developers.rasayel.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.rasayel.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.rasayel.io/
- group: docs
  title: ''
  type: APIReference
  url: https://rest.developers.rasayel.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.rasayel.io/en/introduction
- group: operate
  title: ''
  type: HelpCenter
  url: https://docs.rasayel.io/
- group: company
  title: ''
  type: Blog
  url: https://learn.rasayel.io/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/rasayel
- group: commercial
  title: ''
  type: Pricing
  url: https://rasayel.io/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://app.rasayel.io/signup
- group: start
  title: ''
  type: Login
  url: https://app.rasayel.io
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docs.rasayel.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://docs.rasayel.io/privacy
- group: company
  title: ''
  type: Website
  url: https://rasayel.io
created: '2026-07-17'
description: Rasayel is a WhatsApp platform for B2B sales teams. It combines a shared team inbox, workflow automation and lead qualification, chatbots and AI, WhatsApp message templates and Flows (forms), and campaign broadcasting, alongside CRM integrations (HubSpot, Pipedrive, Salesforce, Zoho) and Zapier. Its public REST API (api.rasayel.io/v1) and GraphQL API let developers manage contacts, message templates, conversations, tags, channels, and custom properties, and send WhatsApp messages programmatically using API-key authentication with Read and Read/Write scopes.
image: https://github.com/rasayel.png
layout: provider
mcp_servers:
- description: ''
  name: rasayel-mcp.yml
  slug: rasayel-mcpyml
modified: '2026-07-20'
name: Rasayel
nav: Providers
network: true
overview: 'Rasayel publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Channels API, Contacts API, Conversations API, and 4 more. Tagged areas include Company, WhatsApp, Messaging, Business Messaging, and Sales.


  Rasayel''s developer surface includes authentication, changelog, documentation, API reference, getting-started guide, engineering blog, pricing, and 23 more developer resources.'
random_paper: 88
rate_limits:
- limit_count: 1
  name: Rasayel Rate Limits
  slug: rasayel-rate-limits
score:
  band: developing
  composite: 51.0
  delta: 2.3
  facets:
    commercial_clarity: 44.7
    contract_quality: 58.8
    developer_ergonomics: 60.3
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 57.9
  previous_composite: 48.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 34.7
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: authentication
  name: Rasayel Authentication
  slug: rasayel-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Rasayel Domain Security
  slug: rasayel-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: rasayel
tags:
- Company
- WhatsApp
- Messaging
- Business Messaging
- Sales
- CRM
- Customer Communication
- Conversational Commerce
- API
website: https://rasayel.io
---
