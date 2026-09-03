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
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.7
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Cvent Agentic Access
  operation_count: 20
  slug: cvent-agentic-access
  summary_line: 20 operations · 11 acting
api_count: 1
apis:
- description: The unified Cvent Platform REST API providing programmatic access to events, contacts, registrations, attendees, sessions, speakers, exhibitors, surveys, webhooks, and Attendee Hub resources. OAuth 2.
  name: Cvent REST API
  slug: rest-api
- description: Cvent Webhooks notify external applications when actions occur in Cvent and send relevant data to a specified URL, automatically pushing event, attendee, speaker, and meeting request data to subscribe
  name: Cvent Webhooks API
  slug: webhooks
- description: The Cvent Supplier Network (CSN) API provides integration with a database of 280,000+ hotels, suppliers, and destinations worldwide. Planners search and compare venues and manage RFPs; suppliers creat
  name: Cvent Supplier Network (CSN) API
  slug: csn-api
- description: Passkey RegLink APIs are RESTful JSON APIs (with legacy URL-based and SOAP options) connecting Cvent registration with Passkey hotel reservations. Send registrant info, fetch event and hotel availabil
  name: Cvent Passkey RegLink API
  slug: passkey-reglink
- description: The Cvent SOAP API is the original legacy API for pushing and pulling data between Cvent and internal systems. Supports contact and event management, custom fields, address book, and metadata. Being s
  name: Cvent SOAP API (Legacy)
  slug: soap-api
- description: The Cvent Custom Widgets API allows developers to build custom interactive widgets for Cvent Event Registration pages. SDK for widget elements, configuration files, and navigation methods.
  name: Cvent Custom Widgets API
  slug: custom-widgets
- description: Cvent SSO enables identity provider integration via SAML and OpenID Connect for planner login, access portals, event registrant and Attendee Hub, Events+, and portal applications.
  name: Cvent Single Sign-On (SSO) Integration
  slug: sso
- description: The Cvent White Label API enables venues and suppliers to embed Cvent RFP functionality into their own websites with custom branding, theming, and analytics for embedded RFP forms.
  name: Cvent White Label API
  slug: white-label
- description: The Cvent Salesforce App integrates Cvent event data with Salesforce CRM, enabling users to view events from Salesforce, invite contacts and leads, and sync attendee data bidirectionally.
  name: Cvent Salesforce App
  slug: salesforce-app
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Event registrations and attendees
  name: Cvent Attendees API
  slug: cvent-attendees-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Contact/address book
  name: Cvent Contacts API
  slug: cvent-contacts-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Event lifecycle and configuration
  name: Cvent Events API
  slug: cvent-events-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Exhibitor management
  name: Cvent Exhibitors API
  slug: cvent-exhibitors-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: OAuth 2.0 token issuance
  name: Cvent OAuth API
  slug: cvent-oauth-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Agenda sessions
  name: Cvent Sessions API
  slug: cvent-sessions-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Webhook subscriptions
  name: Cvent Webhooks API
  slug: cvent-webhooks-api
artifact_total: 33
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Cvent REST Attendees API
  slug: open-cvent-attendees-api
- collection_type: open
  name: Cvent REST Attendees Contacts API
  slug: open-cvent-contacts-api
- collection_type: open
  name: Cvent REST Attendees Events API
  slug: open-cvent-events-api
- collection_type: open
  name: Cvent REST Attendees Exhibitors API
  slug: open-cvent-exhibitors-api
- collection_type: open
  name: Cvent REST Attendees OAuth API
  slug: open-cvent-oauth-api
- collection_type: open
  name: Cvent REST Attendees Sessions API
  slug: open-cvent-sessions-api
- collection_type: open
  name: Cvent REST Attendees Webhooks API
  slug: open-cvent-webhooks-api
- collection_type: open
  name: Cvent REST API
  slug: open-cvent
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/cvent-capability-edges.yml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/cvent/custom-widgets-labs/issues
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cvent-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/cvent-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cvent-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cvent-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/cvent-scopes.yml
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
  url: https://developers.cvent.com/docs/rest-api/reference/reference
- group: auth
  title: ''
  type: Authentication
  url: https://developers.cvent.com/docs/rest-api/explanation/authentication
- group: auth
  title: ''
  type: OAuthTokenEndpoint
  url: https://api-platform.cvent.com/ea/oauth2/token
- group: start
  title: ''
  type: Signup
  url: https://developers.cvent.com/register
- group: other
  title: ''
  type: Standards
  url: https://developers.cvent.com/docs/rest-api/reference/api-standards
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.cvent.com/docs/rest-api/changelog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cvent.com
- group: operate
  title: ''
  type: Support
  url: https://support.cvent.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.cvent.com/en/event-management-software/cvent-pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cvent.com/en/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cvent.com/en/privacy-policy
- group: auth
  title: ''
  type: Security
  url: https://www.cvent.com/en/security
- group: learn
  title: ''
  type: Training
  url: https://www.cvent.com/en/academy
- group: operate
  title: ''
  type: Community
  url: https://community.cvent.com/home
- group: company
  title: ''
  type: Blog
  url: https://www.cvent.com/en/blog
- group: build
  title: ''
  type: GitHub
  url: https://github.com/cvent
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/cvent
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cvent
created: '2025-11-19'
description: Cvent is a leading meetings, events, and hospitality technology provider with over 4,800 employees and 22,000+ customers worldwide. The Cvent platform spans Event Cloud (event management, registration, mobile event apps, virtual and hybrid events, Attendee Hub, surveys, Diagramming, and analytics) and Hospitality Cloud (Cvent Supplier Network, Passkey, Venue Sourcing, and Sales & Catering). Programmatic access is delivered through the unified Cvent Platform REST API (api-platform.cvent.com) using OAuth 2.0 client credentials, with legacy SOAP, BadgeKit, Jifflenow, and CSN APIs documented for historical integrations. The developer portal at developers.cvent.com hosts API references, guides, OpenAPI downloads, webhooks, SSO, custom widgets, white-label, and integration documentation.
finops:
- name: Cvent Finops
  service_category: API
  slug: cvent-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cvent.png
layout: provider
modified: '2026-04-28'
name: Cvent
nav: Providers
network: true
overview: 'Cvent publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Attendees API, Contacts API, Events API, and 4 more. Tagged areas include Attendee Hub, Attendee Management, Conferences, Diagramming, and Event Management.


  Cvent''s developer surface includes authentication, API reference, signup flow, changelog, support, pricing, training material, and 20 more developer resources.'
plans:
- name: Cvent Plans Pricing
  plan_count: 3
  slug: cvent-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 5
  name: Cvent Rate Limits
  slug: cvent-rate-limits
scopes:
- name: Cvent Scopes
  scope_count: 9
  slug: cvent-scopes
  summary_line: 9 scopes · clientCredentials
score:
  band: developing
  composite: 49.1
  coverage:
    artifact_dirs: 13
    catalog_gap: 74.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 57.9
    commercial_clarity: 57.9
    contract_governance: 0.0
    contract_quality: 52.0
    developer_ergonomics: 57.1
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 55.3
  previous_composite: 49.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cvent/refs/heads/main/screenshots/cvent-2026-06-20T175359.png
security:
- kind: authentication
  name: Cvent Authentication
  slug: cvent-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Cvent Domain Security
  slug: cvent-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Cvent Trust Center
  slug: cvent-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, PCI DSS, HIPAA, FedRAMP, GDPR
slug: cvent
tags:
- Attendee Hub
- Attendee Management
- Conferences
- Diagramming
- Event Management
- Event Marketing
- Event
- Exhibitors
- Hospitality
- Hospitality Cloud
- Hybrid Events
- Meetings
- Authentication
- Passkey
- Registration
- REST API
- SOAP API
- SSO
- Supplier Network
- Surveys
- Venue Management
- Venue Sourcing
- Virtual Events
- Webhook
- White Label
website: https://www.cvent.com/
---
