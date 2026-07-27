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
    agent_skills: true
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 49.0
  scored_at: '2026-07-27'
api_count: 8
apis:
- description: Call analytics, transcripts, keywords, and reports
  name: Tenfold Analytics API
  slug: tenfold-analytics-api
- description: OAuth 2.0 and JWT token issuance and authorization
  name: Tenfold Authentication API
  slug: tenfold-authentication-api
- description: Originate, query, control, and update calls
  name: Tenfold Calls API
  slug: tenfold-calls-api
- description: Contact list management (BETA)
  name: Tenfold Contact Lists API
  slug: tenfold-contact-lists-api
- description: Create, edit, and query CRM records and interactions
  name: Tenfold CRM Records API
  slug: tenfold-crm-records-api
- description: Organization data and integration health
  name: Tenfold Organizations API
  slug: tenfold-organizations-api
- description: Custom event tracking
  name: Tenfold Tracking API
  slug: tenfold-tracking-api
- description: Users, current-user profile, and settings
  name: Tenfold Users API
  slug: tenfold-users-api
artifact_total: 11
asyncapis:
- description: ''
  name: Tenfold Webhooks
  slug: tenfold-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://tenfold.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://apidocs.tenfold.com/
- group: docs
  title: ''
  type: APIReference
  url: https://apidocs.tenfold.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tenfold.com/
- group: auth
  title: ''
  type: Authentication
  url: authentication/tenfold-authentication.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/tenfold-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/tenfold-webhooks.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/tenfold-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tenfold-llms.txt
created: '2026-07-17'
description: Tenfold (a LivePerson company) is a computer-telephony integration (CTI) platform — marketed as the "Customer Experience Cloud" — that connects phone systems and contact-center platforms with CRM and support systems. It surfaces the caller's CRM record on inbound and outbound calls, enables click-to-call, automatic call logging, call notes, and call recording, and connects leading CRMs (Salesforce, Microsoft Dynamics, ServiceNow, Oracle NetSuite, Zendesk, SugarCRM, Bullhorn) with major phone systems (Cisco, Avaya, Genesys, RingCentral, Webex Calling, 3CX, Mitel, and more). Its REST API originates and queries calls, controls recording, manages users and organizations, reads and writes CRM records, and returns call analytics, transcripts, and keyword extraction. Tenfold was acquired by LivePerson in October 2021.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tenfold.png
layout: provider
mcp_servers:
- description: ''
  name: tenfold-mcp.yml
  slug: tenfold-mcpyml
modified: '2026-07-21'
name: Tenfold
nav: Providers
network: true
overview: 'Tenfold publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Analytics API, Authentication API, Calls API, and 5 more. Tagged areas include Company, CTI, Contact Center, Telephony, and CRM Integration.


  The Tenfold catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Tenfold''s developer surface includes API reference, documentation, authentication, and 7 more developer resources.'
random_paper: 0
score:
  band: thin
  composite: 37.7
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 62.4
    developer_ergonomics: 50.0
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 15.8
  previous_composite: 37.7
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: authentication
  name: Tenfold Authentication
  slug: tenfold-authentication
  summary_line: oauth2/http · 3 schemes
slug: tenfold
tags:
- Company
- CTI
- Contact Center
- Telephony
- CRM Integration
- Call Analytics
- Customer Experience
- Voice
website: https://tenfold.com/
---
