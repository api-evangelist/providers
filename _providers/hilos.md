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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.2
  scored_at: '2026-07-28'
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
artifact_total: 10
common:
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
  url: https://hilos-40.mintlify.app/docs/developer/apidocs/contact/get-apicontact
- group: start
  title: ''
  type: GettingStarted
  url: https://hilos-40.mintlify.app/docs/developer/getting-started/test-request
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
  type: Pricing
  url: https://hilos.io/pricing
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
modified: '2026-07-19'
name: Hilos
nav: Providers
network: true
overview: 'Hilos publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Contact API, Conversation API, Flow Execution API, and 3 more. Tagged areas include Company, WhatsApp, Messaging, Automation, and CRM.


  Hilos'' developer surface includes documentation, API reference, getting-started guide, authentication, engineering blog, pricing, signup flow, and 16 more developer resources.'
random_paper: 4
score:
  band: developing
  composite: 43.0
  delta: -3.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 54.9
    developer_ergonomics: 56.0
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 0.0
  previous_composite: 46.0
  provenance:
    agentic_access: derived
    conformance: derived
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
    score: 34.7
  schema_version: 0.6
  scored_at: '2026-07-28'
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
