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
    agent_card: flavored
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 50.5
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Hilos Agentic Access
  operation_count: 19
  slug: hilos-agentic-access
  summary_line: 19 operations · 9 acting
api_count: 6
apis:
- description: The Contact API from Hilos — 2 operation(s) for contact.
  name: Hilos Contact API
  slug: hilos-contact-api
- description: The Conversation API from Hilos — 2 operation(s) for conversation.
  name: Hilos Conversation API
  slug: hilos-conversation-api
- description: The Flow Execution API from Hilos — 3 operation(s) for flow execution.
  name: Hilos Flow Execution API
  slug: hilos-flow-execution-api
- description: The Flow Execution Contact API from Hilos — 2 operation(s) for flow execution contact.
  name: Hilos Flow Execution Contact API
  slug: hilos-flow-execution-contact-api
- description: The User API from Hilos — 1 operation(s) for user.
  name: Hilos User API
  slug: hilos-user-api
- description: The WhatsApp API from Hilos — 3 operation(s) for whatsapp.
  name: Hilos WhatsApp API
  slug: hilos-whatsapp-api
artifact_total: 20
asyncapis:
- description: ''
  name: Hilos Events
  slug: hilos-events
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Hilos Contact API
  slug: open-hilos-contact-api
- collection_type: open
  name: Hilos Contact Conversation API
  slug: open-hilos-conversation-api
- collection_type: open
  name: Hilos Contact Flow Execution API
  slug: open-hilos-flow-execution-api
- collection_type: open
  name: Hilos Contact Flow Execution Contact API
  slug: open-hilos-flow-execution-contact-api
- collection_type: open
  name: Hilos Contact User API
  slug: open-hilos-user-api
- collection_type: open
  name: Hilos Contact WhatsApp API
  slug: open-hilos-whatsapp-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/hilos-openapi-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hilos-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/hilos-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://hilos.io
- group: start
  title: ''
  type: DeveloperPortal
  url: https://hilos.io/docs
- group: docs
  title: ''
  type: Documentation
  url: https://hilos.io/docs
- group: docs
  title: ''
  type: APIReference
  url: https://hilos.io/docs/developer/apidocs/contact/get-apicontact
- group: start
  title: ''
  type: GettingStarted
  url: https://hilos.io/docs/developer/getting-started/test-request
- group: auth
  title: ''
  type: Authentication
  url: authentication/hilos-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://hilos.io/blog
- group: commercial
  title: ''
  type: Plans
  url: plans/hilos-plans-pricing.yml
- group: start
  title: ''
  type: SignUp
  url: https://hilos.io/signup-ac
- group: start
  title: ''
  type: Login
  url: https://app.hilos.io/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://hilos.io/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://hilos.io/privacy-policy
- group: operate
  title: ''
  type: Support
  url: mailto:hey@hilos.io
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hilos-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/hilos-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/hilos-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/hilos-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/hilos-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/hilos-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/hilos-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/hilos-tool-crosswalk.yml
- group: other
  title: ''
  type: AgentCard
  url: a2a/hilos-a2a.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/hilos-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/hilos-packages.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/hilos-rate-limits.yml
- group: other
  title: ''
  type: Events
  url: asyncapi/hilos-events.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: 'Hilos is a WhatsApp Business Platform automation company (backed by 500 Global and Techstars, now part of ActiveCampaign) that helps businesses capture leads, qualify prospects, and automate follow-ups over WhatsApp''s Cloud API. Its REST API exposes contacts, inbox conversations, WhatsApp message templates, and no-code flow executions, authenticated with an `Authorization: Token` API key against https://api.hilos.io/api/ and paginated with `page` / `page_size` query parameters.'
image: https://app.hilos.io/logo512.png
layout: provider
mcp_servers:
- description: ''
  name: hilos-mcp.yml
  slug: hilos-mcpyml
modified: '2026-08-13'
name: Hilos
nav: Providers
network: true
overview: 'Hilos publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Contact API, Conversation API, Flow Execution API, and 3 more. Tagged areas include Company, WhatsApp, Messaging, Automation, and CRM.


  The Hilos catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Hilos'' developer surface includes documentation, API reference, getting-started guide, authentication, engineering blog, signup flow, support, and 23 more developer resources.'
plans:
- name: Hilos Plans Pricing
  plan_count: 0
  slug: hilos-plans-pricing
random_paper: 96
rate_limits:
- limit_count: 0
  name: Hilos Rate Limits
  slug: hilos-rate-limits
score:
  band: developing
  composite: 47.3
  delta: 3.2
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 30.3
    contract_quality: 67.5
    developer_ergonomics: 58.9
    discoverability: 81.5
    governance: 30.3
    operational_transparency: 0.0
  previous_composite: 44.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: first-party
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hilos/refs/heads/main/screenshots/hilos-2026-07-25T221229.png
security:
- kind: authentication
  name: Hilos Authentication
  slug: hilos-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Hilos Domain Security
  slug: hilos-domain-security
  summary_line: TLSv1.3 · HSTS
slug: hilos
tags:
- Company
- WhatsApp
- Messaging
- Automation
- CRM
- Conversational Commerce
- Chatbots
- Customer Engagement
- Marketing
website: https://hilos.io
---
