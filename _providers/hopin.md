---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
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
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Hopin Agentic Access
  operation_count: 31
  slug: hopin-agentic-access
  summary_line: 31 operations · 9 acting
api_count: 14
apis:
- description: Bank question management
  name: RingCentral Events Bank Questions API
  slug: hopin-bank-questions-api
- description: Booth management
  name: RingCentral Events Booths API
  slug: hopin-booths-api
- description: Data subscription webhooks
  name: RingCentral Events Data Subscriptions API
  slug: hopin-data-subscriptions-api
- description: Event management
  name: RingCentral Events Events API
  slug: hopin-events-api
- description: Health check endpoints
  name: RingCentral Events Health API
  slug: hopin-health-api
- description: Magic link management
  name: RingCentral Events Magic Links API
  slug: hopin-magic-links-api
- description: Organization management
  name: RingCentral Events Organizations API
  slug: hopin-organizations-api
- description: Event registration management
  name: RingCentral Events Registrations API
  slug: hopin-registrations-api
- description: Event reporting
  name: RingCentral Events Reports API
  slug: hopin-reports-api
- description: Event schedule management
  name: RingCentral Events Schedule Items API
  slug: hopin-schedule-items-api
- description: Event session management
  name: RingCentral Events Sessions API
  slug: hopin-sessions-api
- description: Event stage management
  name: RingCentral Events Stages API
  slug: hopin-stages-api
- description: Event template management
  name: RingCentral Events Templates API
  slug: hopin-templates-api
- description: Ticket management
  name: RingCentral Events Tickets API
  slug: hopin-tickets-api
artifact_total: 29
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/hopin-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/hopin-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hopin-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/hopin-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/hopin-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hopin-team
- group: docs
  title: ''
  type: Documentation
  url: https://developer.events.ringcentral.com/external-api
- group: start
  title: ''
  type: Portal
  url: https://developer.events.ringcentral.com/
- group: build
  title: ''
  type: PostmanCollection
  url: https://github.com/hopin-team/hopin-external-api-collection
- group: auth
  title: ''
  type: Authentication
  url: https://developer.events.ringcentral.com/external-api/guides/authentication
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.events.ringcentral.com/external-api/changelog
- group: operate
  title: ''
  type: Status
  url: https://status.ringcentral.com/
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://support.ringcentral.com/release-notes/ringex/video/events.html
- group: commercial
  title: ''
  type: Pricing
  url: https://www.ringcentral.com/pricing/events.html
- group: company
  title: ''
  type: Blog
  url: https://www.ringcentral.com/us/en/blog/
- group: operate
  title: ''
  type: Support
  url: https://events-support.ringcentral.com/
created: '2024-01-01'
description: RingCentral Events (formerly Hopin) is a virtual and hybrid event management platform with REST APIs for managing organizations, events, sessions, stages, booths, registrations, attendees, tickets, reports, and data subscriptions. Acquired by RingCentral from Hopin in August 2023, the platform enables planning and producing engaging virtual, hybrid, and in-person event experiences. API access is available on the Enterprise plan.
examples:
- key_count: 4
  name: Create Data Subscription
  slug: create-data-subscription
- key_count: 4
  name: Create Magic Link
  slug: create-magic-link
- key_count: 4
  name: Create Registration
  slug: create-registration
- key_count: 4
  name: List Events
  slug: list-events
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hopin.png
json_schemas:
- name: RingCentral Events API Schema
  property_count: 0
  slug: ringcentral-events
jsonld:
- class_count: 44
  name: Ringcentral Events Context
  property_count: 8
  slug: ringcentral-events-context
layout: provider
modified: '2026-06-13'
name: RingCentral Events
nav: Providers
network: true
overview: 'RingCentral Events publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Bank Questions API, Booths API, Data Subscriptions API, and 11 more. Tagged areas include Events, Virtual Events, Hybrid Events, Webinars, and Event Management.


  The RingCentral Events catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  RingCentral Events'' developer surface includes authentication, documentation, developer portal, changelog, status page, release notes, pricing, and 9 more developer resources.'
plans:
- name: Plans
  plan_count: 4
  slug: plans
random_paper: 62
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
rules:
- name: RingCentral Events API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: hopin-jsonschema-spectral-rules
scopes:
- name: Hopin Scopes
  scope_count: 2
  slug: hopin-scopes
  summary_line: 2 scopes · clientCredentials
score:
  band: developing
  composite: 54.6
  delta: 0.0
  facets:
    commercial_clarity: 57.9
    contract_quality: 72.4
    developer_ergonomics: 39.1
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 21.1
  previous_composite: 54.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hopin/refs/heads/main/screenshots/hopin-2026-06-20T182829.png
security:
- kind: authentication
  name: Hopin Authentication
  slug: hopin-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Hopin Domain Security
  slug: hopin-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Hopin Trust Center
  slug: hopin-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, HIPAA, GDPR
slug: hopin
tags:
- Events
- Virtual Events
- Hybrid Events
- Webinars
- Event Management
- Registration
- Sessions
- Networking
website: https://developer.events.ringcentral.com/
---
