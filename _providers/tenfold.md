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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.4
  scored_at: '2026-09-01'
api_count: 1
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
artifact_total: 20
asyncapis:
- description: ''
  name: Tenfold Webhooks
  slug: tenfold-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Tenfold Analytics API
  slug: open-tenfold-analytics-api
- collection_type: open
  name: Tenfold Analytics Authentication API
  slug: open-tenfold-authentication-api
- collection_type: open
  name: Tenfold Analytics Calls API
  slug: open-tenfold-calls-api
- collection_type: open
  name: Tenfold Analytics Contact Lists API
  slug: open-tenfold-contact-lists-api
- collection_type: open
  name: Tenfold Analytics CRM Records API
  slug: open-tenfold-crm-records-api
- collection_type: open
  name: Tenfold Analytics Organizations API
  slug: open-tenfold-organizations-api
- collection_type: open
  name: Tenfold Analytics Tracking API
  slug: open-tenfold-tracking-api
- collection_type: open
  name: Tenfold Analytics Users API
  slug: open-tenfold-users-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/tenfold-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/tenfold-openapi-overlay.yaml
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
- description: Candidate MCP server tool surface derived from the Tenfold documented API. No official hosted/remote MCP server was found for Tenfold. Tools map one-to-one to documented v2 operationIds.
  name: Tenfold MCP Server
  slug: tenfold-mcp-server
modified: '2026-07-21'
name: Tenfold
nav: Providers
network: true
overview: 'Tenfold publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Analytics API, Authentication API, Calls API, and 5 more. Tagged areas include Company, CTI, Contact Center, Telephony, and CRM Integration.


  The Tenfold catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Tenfold''s developer surface includes API reference, documentation, authentication, and 9 more developer resources.'
random_paper: 13
score:
  band: thin
  composite: 31.5
  coverage:
    artifact_dirs: 22
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.2
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 53.5
    developer_ergonomics: 39.9
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 15.8
  previous_composite: 31.7
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
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
