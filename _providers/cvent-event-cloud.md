---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Cvent Event Cloud Agentic Access
  operation_count: 20
  slug: cvent-event-cloud-agentic-access
  summary_line: 20 operations · 11 acting
api_count: 8
apis:
- description: RESTful API for managing events, contacts, registrations, attendees, sessions, speakers, exhibitors, surveys, webhooks, and Attendee Hub data. Uses OAuth 2.0 client credentials. Authorization code flo
  name: Cvent Platform REST API (Event Cloud)
  slug: rest-api
- description: Event registrations and attendees
  name: Cvent Event Cloud Attendees API
  slug: cvent-event-cloud-attendees-api
- description: Contact/address book
  name: Cvent Event Cloud Contacts API
  slug: cvent-event-cloud-contacts-api
- description: Event lifecycle and configuration
  name: Cvent Event Cloud Events API
  slug: cvent-event-cloud-events-api
- description: Exhibitor management
  name: Cvent Event Cloud Exhibitors API
  slug: cvent-event-cloud-exhibitors-api
- description: OAuth 2.0 token issuance
  name: Cvent Event Cloud OAuth API
  slug: cvent-event-cloud-oauth-api
- description: Agenda sessions
  name: Cvent Event Cloud Sessions API
  slug: cvent-event-cloud-sessions-api
- description: Webhook subscriptions
  name: Cvent Event Cloud Webhooks API
  slug: cvent-event-cloud-webhooks-api
artifact_total: 17
collections:
- collection_type: open
  name: Cvent Event Cloud REST API
  slug: open-cvent-event-cloud
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cvent-event-cloud-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/cvent-event-cloud-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cvent-event-cloud-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cvent-event-cloud-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/cvent-event-cloud-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cvent
- group: company
  title: ''
  type: Website
  url: https://www.cvent.com/en/event-management-software
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.cvent.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.cvent.com/docs/rest-api/overview
- group: other
  title: ''
  type: AttendeeHub
  url: https://www.cvent.com/en/attendee-hub
- group: commercial
  title: ''
  type: Pricing
  url: https://www.cvent.com/en/pricing
- group: operate
  title: ''
  type: Support
  url: https://support.cvent.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cvent.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cvent.com/en/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cvent.com/en/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://www.cvent.com/blog
- group: agent
  title: ''
  type: LlmsText
  url: https://www.cvent.com/llms.txt
created: '2024-01-01'
description: 'Cvent Event Cloud is the event management product line of the Cvent Platform. It supports the full event lifecycle: event creation, registration, marketing, agenda and session management, mobile event apps, onsite check-in, virtual and hybrid event delivery via the Attendee Hub, surveys, and analytics. The Cvent Platform REST API exposes Event Cloud resources programmatically using OAuth 2.0 client credentials, with the token endpoint at api-platform.cvent.com/ea/oauth2/token. OpenAPI specifications can be downloaded from the developer portal at developers.cvent.com.'
finops:
- name: Cvent Event Cloud Finops
  service_category: API
  slug: cvent-event-cloud-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cvent-event-cloud.png
layout: provider
modified: '2026-04-28'
name: Cvent Event Cloud
nav: Providers
network: true
overview: 'Cvent Event Cloud publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Attendees API, Contacts API, Events API, and 4 more. Tagged areas include Attendee Hub, Attendees, Event Cloud, Event Management, and Event Marketing.


  Cvent Event Cloud''s developer surface includes authentication, API reference, pricing, support, engineering blog, and 12 more developer resources.'
plans:
- name: Cvent Event Cloud Plans Pricing
  plan_count: 3
  slug: cvent-event-cloud-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 5
  name: Cvent Event Cloud Rate Limits
  slug: cvent-event-cloud-rate-limits
scopes:
- name: Cvent Event Cloud Scopes
  scope_count: 9
  slug: cvent-event-cloud-scopes
  summary_line: 9 scopes · clientCredentials
score:
  band: developing
  composite: 50.4
  delta: 0.0
  facets:
    commercial_clarity: 78.9
    contract_quality: 55.4
    developer_ergonomics: 32.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 50.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cvent-event-cloud/refs/heads/main/screenshots/cvent-event-cloud-2026-06-20T175402.png
security:
- kind: authentication
  name: Cvent Event Cloud Authentication
  slug: cvent-event-cloud-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Cvent Event Cloud Domain Security
  slug: cvent-event-cloud-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Cvent Event Cloud Trust Center
  slug: cvent-event-cloud-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, PCI DSS, HIPAA, FedRAMP, GDPR
slug: cvent-event-cloud
tags:
- Attendee Hub
- Attendees
- Event Cloud
- Event Management
- Event Marketing
- Events
- Hybrid Events
- OAuth 2.0
- Onsite
- Registration
- REST
- Sessions
- Speakers
- Surveys
- Virtual Events
- Webhooks
website: https://www.cvent.com/en/event-management-software
---
