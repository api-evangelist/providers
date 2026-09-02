---
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
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.0
  scored_at: '2026-09-01'
api_count: 5
apis:
- description: User login and token management operations.
  name: Nextiva Authentication API
  slug: nextiva-authentication-api
- description: Actions specific to managing calls within workitems
  name: Nextiva Call Management API
  slug: nextiva-call-management-api
- description: The Campaigns API from Nextiva — 1 operation(s) for campaigns.
  name: Nextiva Campaigns API
  slug: nextiva-campaigns-api
- description: Operations related to conversations
  name: Nextiva Conversations API
  slug: nextiva-conversations-api
- description: DTMF tone sending for calls
  name: Nextiva DTMF API
  slug: nextiva-dtmf-api
- description: Email-related workitem operations
  name: Nextiva Email API
  slug: nextiva-email-api
- description: Operations for sending and managing SMS messages.
  name: Nextiva SMS Messaging API
  slug: nextiva-sms-messaging-api
- description: The Tickets API from Nextiva — 1 operation(s) for tickets.
  name: Nextiva Tickets API
  slug: nextiva-tickets-api
- description: Operations for transferring workitems
  name: Nextiva Transfers API
  slug: nextiva-transfers-api
- description: The Workitems API from Nextiva — 4 operation(s) for workitems.
  name: Nextiva Workitems API
  slug: nextiva-workitems-api
artifact_total: 20
asyncapis:
- description: ''
  name: Nextiva Events
  slug: nextiva-events
collections:
- collection_type: open
  name: Provider Authentication API
  slug: open-nextiva-authentication
- collection_type: open
  name: Conversation API
  slug: open-nextiva-conversation
- collection_type: open
  name: Provider Authentication API
  slug: open-nextiva-provider-authentication
- collection_type: open
  name: SMS Messaging API
  slug: open-nextiva-sms-messaging
- collection_type: open
  name: Workitem Service API
  slug: open-nextiva-workitem-service
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/nextiva-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/nextiva-authentication-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/nextiva-provider-authentication-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/nextiva-workitem-service-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/nextiva-conversation-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/nextiva-sms-messaging-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.nextiva.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.nextiva.com/nextiva/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.nextiva.com/nextiva/docs/overview-of-sdks
- group: docs
  title: ''
  type: APIReference
  url: https://developer.nextiva.com/nextiva/reference/generatetokenwithauthorities
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.nextiva.com/nextiva/docs/sdk-installation
- group: operate
  title: ''
  type: Support
  url: https://help.nextiva.com/
- group: company
  title: ''
  type: Blog
  url: https://www.nextiva.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/nextiva
- group: commercial
  title: ''
  type: Pricing
  url: https://www.nextiva.com/nextivapricing
- group: start
  title: ''
  type: Login
  url: https://login.nextiva.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.nextiva.com/legal.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.nextiva.com/privacy-policy.html
- group: operate
  title: ''
  type: StatusPage
  url: https://status.nextiva.com/
- group: auth
  title: ''
  type: Security
  url: https://www.nextiva.com/security-policy.html
- group: auth
  title: ''
  type: Compliance
  url: https://www.nextiva.com/resources/learn/security-certification-overview
- group: build
  title: ''
  type: Packages
  url: packages/nextiva-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/nextiva-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/nextiva-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/nextiva-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/nextiva-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/nextiva-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/nextiva-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nextiva-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/nextiva-vulnerability-disclosure.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/nextiva-events.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/nextiva-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/nextiva-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/nextiva-llms.txt
created: '2026-07-31'
description: 'Nextiva is a Scottsdale, Arizona based cloud communications and customer experience company whose NextOS / NEXT platform combines UCaaS business phone service, contact center (NCX), SMS and team messaging, voice AI agents, and conversation analytics for small business through enterprise. Its developer surface is the Nextiva Contact Center platform: a ReadMe-hosted developer portal at developer.nextiva.com publishing five REST OpenAPI 3.0 contracts (Provider Authentication, Provider Token Service, Workitem Service, Conversation, SMS Messaging) served from api.nextiva.com, alongside four frontend SDKs (Core, Web, React, React Native) that wrap the same backend over HTTP plus two WebSocket channels — an events socket for real-time workitem, offer, phone-state and live-transcription notifications, and an analytics socket for supervisory data.'
image: https://files.readme.io/c57cfd17e3ed303431732141b3a42eaff618f7682e4cd2c42e12470ba7ce8878-nextiva_logo_rgb_dark.svg
layout: provider
mcp_servers:
- description: ''
  name: Nextiva MCP Server
  slug: nextiva-mcp-server
modified: '2026-07-31'
name: Nextiva
nav: Providers
network: true
overview: 'Nextiva publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Call Management API, Campaigns API, and 7 more. Tagged areas include Company, Communications, Voice, Contact Center, and Customer Experience.


  The Nextiva catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Nextiva''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, authentication, and 28 more developer resources.'
random_paper: 11
score:
  band: developing
  composite: 50.6
  coverage:
    artifact_dirs: 19
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.2
  facets:
    access_clarity: 46.1
    commercial_clarity: 46.1
    contract_governance: 4.5
    contract_quality: 57.4
    developer_ergonomics: 47.0
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 36.8
  previous_composite: 50.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 56.9
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nextiva/refs/heads/main/screenshots/nextiva-2026-08-07T185215.png
security:
- kind: authentication
  name: Nextiva Authentication
  slug: nextiva-authentication
  summary_line: http · 3 schemes
- kind: domain-security
  name: Nextiva Domain Security
  slug: nextiva-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Nextiva Vulnerability Disclosure
  slug: nextiva-vulnerability-disclosure
  summary_line: Hackerone · contact published
slug: nextiva
tags:
- Company
- Communications
- Voice
- Contact Center
- Customer Experience
- SMS
- Messaging
- Unified Communications
- VoIP
- Telephony
- Conversational AI
- Call Center
website: https://www.nextiva.com/
---
