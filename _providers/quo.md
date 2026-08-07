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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 40.8
  scored_at: '2026-08-06'
api_count: 9
apis:
- description: Operations related to calls
  name: Quo Calls API
  slug: quo-calls-api
- description: The Contact Custom Fields API from Quo — 1 operation(s) for contact custom fields.
  name: Quo Contact Custom Fields API
  slug: quo-contact-custom-fields-api
- description: Operations related to contacts
  name: Quo Contacts API
  slug: quo-contacts-api
- description: Operations related to conversations
  name: Quo Conversations API
  slug: quo-conversations-api
- description: Operations related to text messages
  name: Quo Messages API
  slug: quo-messages-api
- description: Operations related to phone numbers
  name: Quo Phone Numbers API
  slug: quo-phone-numbers-api
- description: The Tasks API from Quo — 10 operation(s) for tasks.
  name: Quo Tasks API
  slug: quo-tasks-api
- description: Operations related to users
  name: Quo Users API
  slug: quo-users-api
- description: Operations related to webhooks
  name: Quo Webhooks API
  slug: quo-webhooks-api
artifact_total: 14
asyncapis:
- description: ''
  name: Quo Webhooks
  slug: quo-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://quo.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.quo.com/docs
- group: docs
  title: ''
  type: Documentation
  url: https://www.quo.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.quo.com/docs/mdx/api-reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://www.quo.com/docs/mdx/api-reference/send-your-first-message
- group: operate
  title: ''
  type: Support
  url: https://support.quo.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.quo.com/docs/mdx/pricing-support/pricing-overview
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.quo.com/docs/mdx/pricing-support/terms-of-service
- group: operate
  title: ''
  type: ChangeLog
  url: https://support.quo.com/changelog
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/quo-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/quo-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/quo-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/quo-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/quo-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: security/quo-trust-center.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/quo-lifecycle.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/quo-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/quo-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Quo (formerly OpenPhone) is an AI-powered business communication platform that unifies calls, texts, and contacts in one shared workspace for startups and small businesses. Its REST Public API (https://api.quo.com/v1) lets developers send and receive SMS, manage contacts, conversations, and tasks, retrieve AI-generated call summaries and transcripts, and subscribe to Standard-Webhooks-signed events for messages and calls. Authentication is via a workspace API key sent in the Authorization header. This profile was added to the API Evangelist network from VC portfolio discovery and enriched from Quo's live developer documentation and published OpenAPI.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/quo.png
layout: provider
mcp_servers:
- description: ''
  name: quo-mcp.yml
  slug: quo-mcpyml
modified: '2026-07-20'
name: Quo
nav: Providers
network: true
overview: 'Quo publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Calls API, Contact Custom Fields API, Contacts API, and 6 more. Tagged areas include Company, Communication, Messaging, SMS, and Voice.


  The Quo catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Quo''s developer surface includes documentation, API reference, getting-started guide, support, pricing, changelog, authentication, and 12 more developer resources.'
random_paper: 2
score:
  band: developing
  composite: 49.1
  delta: 0.0
  facets:
    commercial_clarity: 36.8
    contract_quality: 74.1
    developer_ergonomics: 53.8
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 31.6
  previous_composite: 49.1
  provenance:
    conformance: derived
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
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Quo Authentication
  slug: quo-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Quo Domain Security
  slug: quo-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Quo Trust Center
  slug: quo-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: quo
tags:
- Company
- Communication
- Messaging
- SMS
- Voice
- Contacts
- Webhooks
- API
website: https://quo.com
---
