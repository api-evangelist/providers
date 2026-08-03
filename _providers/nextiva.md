---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 40.8
  scored_at: '2026-08-03'
api_count: 5
apis:
- description: Login and token refresh for the Nextiva Contact Center platform. Basic authentication generates a JWT bearer token carrying the user's authorities; the token-refresh operation exchanges an existing be
  name: Nextiva Provider Authentication API
  slug: provider-authentication
- description: Spring-secured provider token endpoints that mint JWTs with user authorities, authenticate a user and redirect with a secure token, and generate time-limited multi-tenant portal access tokens.
  name: Nextiva Provider Token Service API
  slug: provider-token-service
- description: Retrieve and control workitems — the unit of work in the Nextiva Contact Center — and the calls attached to them. Fetch workitems and workitem detail, bridge, hold, hang up, mute and unmute a call, se
  name: Nextiva Workitem Service API
  slug: workitem-service
- description: Read the conversation graph across the contact center — conversations and their workitems, conversation history by participant, campaign and ticket scoped conversations, unread counts, conversation ac
  name: Nextiva Conversation API
  slug: conversation
- description: Send outbound SMS messages from a Nextiva user. Inbound SMS arrives as a workitem on the SDK event stream rather than as a customer-configured webhook.
  name: Nextiva SMS Messaging API
  slug: sms-messaging
artifact_total: 10
asyncapis:
- description: ''
  name: Nextiva Events
  slug: nextiva-events
common:
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
  name: nextiva-mcp.yml
  slug: nextiva-mcpyml
modified: '2026-07-31'
name: Nextiva
nav: Providers
network: true
overview: 'Nextiva publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Provider Authentication API, Provider Token Service API, Workitem Service API, and 2 more. Tagged areas include Company, Communications, Voice, Contact Center, and Customer Experience.


  The Nextiva catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Nextiva''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, authentication, and 22 more developer resources.'
random_paper: 7
score:
  band: developing
  composite: 55.8
  facets:
    commercial_clarity: 52.6
    contract_quality: 67.4
    developer_ergonomics: 62.5
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 39.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 56.9
  schema_version: 0.9
  scored_at: '2026-08-03'
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
