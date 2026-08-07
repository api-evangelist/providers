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
  name: Cvent Platform Agentic Access
  operation_count: 20
  slug: cvent-platform-agentic-access
  summary_line: 20 operations · 11 acting
api_count: 9
apis:
- description: The Cvent Platform REST API is the unified RESTful interface across the Event Cloud product line, providing programmatic access to events, contacts, registrations, attendees, sessions, speakers, exhib
  name: Cvent Platform REST API
  slug: rest-api
- description: Passkey RegLink APIs are RESTful JSON APIs (with legacy URL-based and SOAP options) connecting Cvent with external registration and reservation applications. Primary functions include streamlining the
  name: Cvent Passkey RegLink API
  slug: passkey-reglink
- description: Event registrations and attendees
  name: Cvent Platform Attendees API
  slug: cvent-platform-attendees-api
- description: Contact/address book
  name: Cvent Platform Contacts API
  slug: cvent-platform-contacts-api
- description: Event lifecycle and configuration
  name: Cvent Platform Events API
  slug: cvent-platform-events-api
- description: Exhibitor management
  name: Cvent Platform Exhibitors API
  slug: cvent-platform-exhibitors-api
- description: OAuth 2.0 token issuance
  name: Cvent Platform OAuth API
  slug: cvent-platform-oauth-api
- description: Agenda sessions
  name: Cvent Platform Sessions API
  slug: cvent-platform-sessions-api
- description: Webhook subscriptions
  name: Cvent Platform Webhooks API
  slug: cvent-platform-webhooks-api
artifact_total: 18
collections:
- collection_type: open
  name: Cvent Platform REST API
  slug: open-cvent-platform
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cvent-platform-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/cvent-platform-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cvent-platform-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cvent-platform-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/cvent-platform-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cvent
- group: company
  title: ''
  type: Website
  url: https://www.cvent.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.cvent.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.cvent.com/docs/rest-api/overview
- group: auth
  title: ''
  type: Authentication
  url: https://developers.cvent.com/docs/rest-api
- group: auth
  title: ''
  type: OAuthTokenEndpoint
  url: https://api-platform.cvent.com/ea/oauth2/token
- group: operate
  title: ''
  type: SupportArticles
  url: https://support.cvent.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cvent.com/
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
  type: Blog
  url: https://www.cvent.com/blog
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/cvent
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cvent/
created: '2024-01-01'
description: 'Cvent is a leading meetings, events, and hospitality technology provider serving more than 22,000 customers worldwide. The Cvent Platform spans two product groups: Event Cloud (event management, registration, mobile event apps, virtual and hybrid events, Attendee Hub, surveys, and analytics) and Hospitality Cloud (Cvent Supplier Network, Passkey hotel room block management, Venue Sourcing, and Sales & Catering). Programmatic access is delivered through the Cvent Platform REST API protected by OAuth 2.0 client credentials, with the token endpoint at api-platform.cvent.com/ea/oauth2/token. Earlier integrations also use legacy XML SOAP / RegLink web services. The developer portal at developers.cvent.com hosts API references, guides, and OpenAPI downloads.'
finops:
- name: Cvent Platform Finops
  service_category: API
  slug: cvent-platform-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cvent-platform.png
layout: provider
modified: '2026-04-28'
name: Cvent Platform
nav: Providers
network: true
overview: 'Cvent Platform publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Attendees API, Contacts API, Events API, and 4 more. Tagged areas include Attendee Hub, Conferences, Event Management, Event Marketing, and Events.


  Cvent Platform''s developer surface includes authentication, API reference, pricing, engineering blog, and 15 more developer resources.'
plans:
- name: Cvent Platform Plans Pricing
  plan_count: 3
  slug: cvent-platform-plans-pricing
random_paper: 102
rate_limits:
- limit_count: 5
  name: Cvent Platform Rate Limits
  slug: cvent-platform-rate-limits
scopes:
- name: Cvent Platform Scopes
  scope_count: 9
  slug: cvent-platform-scopes
  summary_line: 9 scopes · clientCredentials
score:
  band: developing
  composite: 49.5
  delta: 0.0
  facets:
    commercial_clarity: 78.9
    contract_quality: 55.4
    developer_ergonomics: 28.3
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 49.5
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
screenshot: https://raw.githubusercontent.com/api-evangelist/cvent-platform/refs/heads/main/screenshots/cvent-platform-2026-06-20T175402.png
security:
- kind: authentication
  name: Cvent Platform Authentication
  slug: cvent-platform-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Cvent Platform Domain Security
  slug: cvent-platform-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Cvent Platform Trust Center
  slug: cvent-platform-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, PCI DSS, HIPAA, FedRAMP, GDPR
slug: cvent-platform
tags:
- Attendee Hub
- Conferences
- Event Management
- Event Marketing
- Events
- Hospitality
- Hospitality Cloud
- Hybrid Events
- Meetings
- OAuth 2.0
- Passkey
- Registration
- REST API
- Supplier Network
- Surveys
- Venue Management
- Virtual Events
website: https://www.cvent.com/
---
