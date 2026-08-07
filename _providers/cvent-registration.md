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
  name: Cvent Registration Agentic Access
  operation_count: 20
  slug: cvent-registration-agentic-access
  summary_line: 20 operations · 11 acting
api_count: 9
apis:
- description: The Cvent Registration REST API is the registration surface of the unified Cvent Platform REST API. It allows integrations to create and manage events, registration types, fees, sessions, contacts, at
  name: Cvent Registration REST API
  slug: rest-api
- description: Cvent Webhooks deliver real-time push notifications when registration, attendee, session, and meeting request events occur in Cvent. Webhook subscribers receive event payloads at a configured URL, ena
  name: Cvent Registration Webhooks
  slug: webhooks
- description: Event registrations and attendees
  name: Cvent Registration Attendees API
  slug: cvent-registration-attendees-api
- description: Contact/address book
  name: Cvent Registration Contacts API
  slug: cvent-registration-contacts-api
- description: Event lifecycle and configuration
  name: Cvent Registration Events API
  slug: cvent-registration-events-api
- description: Exhibitor management
  name: Cvent Registration Exhibitors API
  slug: cvent-registration-exhibitors-api
- description: OAuth 2.0 token issuance
  name: Cvent Registration OAuth API
  slug: cvent-registration-oauth-api
- description: Agenda sessions
  name: Cvent Registration Sessions API
  slug: cvent-registration-sessions-api
- description: Webhook subscriptions
  name: Cvent Registration Webhooks API
  slug: cvent-registration-webhooks-api
artifact_total: 18
collections:
- collection_type: open
  name: Cvent Registration REST API
  slug: open-cvent-registration
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cvent-registration-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/cvent-registration-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cvent-registration-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cvent-registration-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/cvent-registration-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cvent
- group: company
  title: ''
  type: Website
  url: https://www.cvent.com/en/event-management-software/online-registration-software
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.cvent.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.cvent.com/docs/rest-api/reference/reference
- group: auth
  title: ''
  type: Authentication
  url: https://developers.cvent.com/docs/rest-api/explanation/authentication
- group: auth
  title: ''
  type: OAuthTokenEndpoint
  url: https://api-platform.cvent.com/ea/oauth2/token
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cvent.com/
- group: operate
  title: ''
  type: Support
  url: https://support.cvent.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.cvent.com/en/pricing
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
  type: Twitter
  url: https://twitter.com/cvent
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cvent/
- group: company
  title: ''
  type: Blog
  url: https://www.cvent.com/en/blog/feed.xml
created: '2024-01-15'
description: Cvent Registration is the event registration product within the Cvent Event Cloud, providing online registration websites, attendee data capture, payment processing, registration travel, group registration, custom field collection, and badge / on-site check-in workflows. Registration data is exposed programmatically through the unified Cvent Platform REST API at api-platform.cvent.com (OAuth 2.0 client credentials), with a dedicated Registration Guide on the Cvent developer portal. Real-time registration changes are also delivered through Cvent Webhooks. Earlier integrations relied on the legacy Cvent SOAP API.
finops:
- name: Cvent Registration Finops
  service_category: API
  slug: cvent-registration-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cvent-registration.png
layout: provider
modified: '2026-04-28'
name: Cvent Registration
nav: Providers
network: true
overview: 'Cvent Registration publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Attendees API, Contacts API, Events API, and 4 more. Tagged areas include Attendee Management, Attendees, Conferences, Event Management, and Events.


  Cvent Registration''s developer surface includes authentication, API reference, support, pricing, engineering blog, and 14 more developer resources.'
plans:
- name: Cvent Registration Plans Pricing
  plan_count: 3
  slug: cvent-registration-plans-pricing
random_paper: 88
rate_limits:
- limit_count: 5
  name: Cvent Registration Rate Limits
  slug: cvent-registration-rate-limits
scopes:
- name: Cvent Registration Scopes
  scope_count: 9
  slug: cvent-registration-scopes
  summary_line: 9 scopes · clientCredentials
score:
  band: developing
  composite: 50.3
  delta: 0.0
  facets:
    commercial_clarity: 78.9
    contract_quality: 55.4
    developer_ergonomics: 32.6
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 50.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 54.7
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cvent-registration/refs/heads/main/screenshots/cvent-registration-2026-06-20T175407.png
security:
- kind: authentication
  name: Cvent Registration Authentication
  slug: cvent-registration-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Cvent Registration Domain Security
  slug: cvent-registration-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Cvent Registration Trust Center
  slug: cvent-registration-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, PCI DSS, HIPAA, FedRAMP, GDPR
slug: cvent-registration
tags:
- Attendee Management
- Attendees
- Conferences
- Event Management
- Events
- OAuth 2.0
- On-Site Check-In
- Payments
- Registration
- REST API
- Ticketing
- Webhooks
website: https://www.cvent.com/en/event-management-software/online-registration-software
---
