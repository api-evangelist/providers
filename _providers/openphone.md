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
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.6
  scored_at: '2026-08-26'
api_count: 9
apis:
- description: Operations related to calls
  name: OpenPhone Calls API
  slug: openphone-calls-api
- description: The Contact Custom Fields API from OpenPhone — 1 operation(s) for contact custom fields.
  name: OpenPhone Contact Custom Fields API
  slug: openphone-contact-custom-fields-api
- description: Operations related to contacts
  name: OpenPhone Contacts API
  slug: openphone-contacts-api
- description: Operations related to conversations
  name: OpenPhone Conversations API
  slug: openphone-conversations-api
- description: Operations related to text messages
  name: OpenPhone Messages API
  slug: openphone-messages-api
- description: Operations related to phone numbers
  name: OpenPhone Phone Numbers API
  slug: openphone-phone-numbers-api
- description: The Tasks API from OpenPhone — 10 operation(s) for tasks.
  name: OpenPhone Tasks API
  slug: openphone-tasks-api
- description: Operations related to users
  name: OpenPhone Users API
  slug: openphone-users-api
- description: Operations related to webhooks
  name: OpenPhone Webhooks API
  slug: openphone-webhooks-api
artifact_total: 24
asyncapis:
- description: ''
  name: Openphone Webhooks
  slug: openphone-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Quo Public Calls API
  slug: open-openphone-calls-api
- collection_type: open
  name: Quo Public Calls Contact Custom Fields API
  slug: open-openphone-contact-custom-fields-api
- collection_type: open
  name: Quo Public Calls Contacts API
  slug: open-openphone-contacts-api
- collection_type: open
  name: Quo Public Calls Conversations API
  slug: open-openphone-conversations-api
- collection_type: open
  name: Quo Public Calls Messages API
  slug: open-openphone-messages-api
- collection_type: open
  name: Quo Public Calls Phone Numbers API
  slug: open-openphone-phone-numbers-api
- collection_type: open
  name: Quo Public Calls Tasks API
  slug: open-openphone-tasks-api
- collection_type: open
  name: Quo Public Calls Users API
  slug: open-openphone-users-api
- collection_type: open
  name: Quo Public Calls Webhooks API
  slug: open-openphone-webhooks-api
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/openphone-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/openphone-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.quo.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.quo.com/docs
- group: docs
  title: ''
  type: Documentation
  url: https://www.quo.com/docs/mdx/api-reference/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://www.quo.com/docs/mdx/api-reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://www.quo.com/docs/mdx/api-reference/send-your-first-message
- group: auth
  title: ''
  type: Authentication
  url: authentication/openphone-authentication.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://www.quo.com/docs/mdx/pricing-support/pricing-overview
- group: operate
  title: ''
  type: Support
  url: https://support.quo.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.quo.com/terms
- group: start
  title: ''
  type: SignUp
  url: https://my.openphone.com/signup
- group: start
  title: ''
  type: Login
  url: https://my.openphone.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.openphone.com
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.quo.com/docs/mdx/api-reference/changelog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/openphone-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.quo.com/security
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/openphone-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/openphone-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/openphone-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/openphone-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/openphone-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/openphone-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/openphone-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/openphone-well-known.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/openphone-openapi-overlay.yaml
- group: build
  title: ''
  type: Packages
  url: packages/openphone-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/openphone-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: OpenPhone (rebranded to Quo in 2026) is a business phone and customer communications platform that provides shared phone numbers, calling, SMS/MMS texting, AI call summaries and transcripts, contacts, conversations, and tasks for teams. Its public REST API lets developers programmatically send messages, list and retrieve calls with recordings and voicemails, manage contacts and custom fields, manage conversations and tasks, look up phone numbers and users, and subscribe to webhooks for message and call events. The API uses API-key authentication in the Authorization header, returns JSON over HTTPS at https://api.quo.com, uses cursor-based pagination, and is rate limited to 10 requests per second. OpenPhone was surfaced as a portfolio company of 500 Global and profiled into the API Evangelist network.
image: https://www.quo.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: OpenPhone MCP Server
  slug: openphone-mcp-server
modified: '2026-07-20'
name: OpenPhone
nav: Providers
network: true
overview: 'OpenPhone publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Calls API, Contact Custom Fields API, Contacts API, and 6 more. Tagged areas include Company, Communications, Voice, SMS, and Messaging.


  The OpenPhone catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  OpenPhone''s developer surface includes documentation, API reference, getting-started guide, authentication, pricing, support, signup flow, and 22 more developer resources.'
random_paper: 6
score:
  band: strong
  composite: 55.0
  delta: 0.0
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 30.3
    contract_quality: 68.5
    developer_ergonomics: 56.5
    discoverability: 81.5
    governance: 30.3
    operational_transparency: 39.5
  previous_composite: 55.0
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 36.1
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/openphone/refs/heads/main/screenshots/openphone-2026-08-07T190627.png
security:
- kind: authentication
  name: Openphone Authentication
  slug: openphone-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Openphone Domain Security
  slug: openphone-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Openphone Trust Center
  slug: openphone-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: openphone
tags:
- Company
- Communications
- Voice
- SMS
- Messaging
- Telephony
- Business Phone
- CPaaS
- Contact Center
- Webhook
website: https://www.quo.com
---
