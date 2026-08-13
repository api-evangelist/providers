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
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.5
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Eventbrite Agentic Access
  operation_count: 14
  slug: eventbrite-agentic-access
  summary_line: 14 operations · 3 acting
api_count: 11
apis:
- description: The Eventbrite Platform API is a REST API that lets developers manage events, attendees, orders, organizations, ticket classes, venues, categories, and event series on Eventbrite. The API uses OAuth 2
  name: Eventbrite Platform API
  slug: platform-api
- description: Eventbrite Webhooks deliver HTTP POST notifications to subscriber URLs when events such as event publish/unpublish, order placement and updates, attendee changes, refunds, and check-ins occur on Event
  name: Eventbrite Webhooks
  slug: webhooks
- description: The Eventbrite Python SDK is an open-source client library maintained by Eventbrite that provides idiomatic Python access to the Eventbrite Platform API for managing events, orders, attendees, and rel
  name: Eventbrite Python SDK
  slug: python-sdk
- description: The Attendees API from Eventbrite — 1 operation(s) for attendees.
  name: Eventbrite Attendees API
  slug: eventbrite-attendees-api
- description: The Categories API from Eventbrite — 1 operation(s) for categories.
  name: Eventbrite Categories API
  slug: eventbrite-categories-api
- description: The Events API from Eventbrite — 2 operation(s) for events.
  name: Eventbrite Events API
  slug: eventbrite-events-api
- description: The Orders API from Eventbrite — 2 operation(s) for orders.
  name: Eventbrite Orders API
  slug: eventbrite-orders-api
- description: The Organizations API from Eventbrite — 1 operation(s) for organizations.
  name: Eventbrite Organizations API
  slug: eventbrite-organizations-api
- description: The Ticket Classes API from Eventbrite — 1 operation(s) for ticket classes.
  name: Eventbrite Ticket Classes API
  slug: eventbrite-ticket-classes-api
- description: The Users API from Eventbrite — 1 operation(s) for users.
  name: Eventbrite Users API
  slug: eventbrite-users-api
- description: The Venues API from Eventbrite — 2 operation(s) for venues.
  name: Eventbrite Venues API
  slug: eventbrite-venues-api
artifact_total: 17
collections:
- collection_type: open
  name: Eventbrite Platform API
  slug: open-eventbrite
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/eventbrite/eventbrite-sdk-python/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/eventbrite/eventbrite-sdk-python/releases
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/eventbrite/eventbrite-sdk-python/blob/master/CONTRIBUTING.rst
- group: commercial
  title: ''
  type: License
  url: https://github.com/eventbrite/eventbrite-sdk-python/blob/master/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/eventbrite-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/eventbrite-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/eventbrite-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/eventbrite-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/eventbrite-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/eventbrite
- group: company
  title: ''
  type: Website
  url: https://www.eventbrite.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.eventbrite.com/platform/
- group: docs
  title: ''
  type: Documentation
  url: https://www.eventbrite.com/platform/api
- group: start
  title: ''
  type: SignupURL
  url: https://www.eventbrite.com/platform/api-keys
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/eventbrite
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.eventbrite.com/support/articles/en_US/Troubleshooting/eventbrite-privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.eventbrite.com/support/articles/en_US/Troubleshooting/eventbrite-terms-of-service
- group: operate
  title: ''
  type: Support
  url: https://www.eventbrite.com/support/contact-us
- group: company
  title: ''
  type: Blog
  url: https://www.eventbrite.com/blog/
- group: start
  title: ''
  type: Login
  url: https://www.eventbrite.com/signin/
created: '2026-05-05'
description: A global self-service ticketing and event technology platform for live experiences. Enables creators to plan, promote, and sell tickets for events of all sizes. The Eventbrite Platform exposes a REST API plus webhooks that lets developers manage events, attendees, orders, organizations, ticket classes, and venues.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/eventbrite.png
layout: provider
modified: '2026-05-16'
name: Eventbrite
nav: Providers
network: true
overview: 'Eventbrite publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Attendees API, Categories API, Events API, and 5 more. Tagged areas include Events, Event Technology, Ticketing, and Marketplace.


  Eventbrite''s developer surface includes authentication, documentation, support, engineering blog, and 16 more developer resources.'
random_paper: 0
score:
  band: thin
  composite: 37.3
  delta: 0.0
  facets:
    commercial_clarity: 42.1
    contract_quality: 55.8
    developer_ergonomics: 34.8
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 15.8
  previous_composite: 37.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/eventbrite/refs/heads/main/screenshots/eventbrite-2026-06-20T180900.png
security:
- kind: authentication
  name: Eventbrite Authentication
  slug: eventbrite-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Eventbrite Domain Security
  slug: eventbrite-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Eventbrite Vulnerability Disclosure
  slug: eventbrite-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Eventbrite Trust Center
  slug: eventbrite-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS
slug: eventbrite
tags:
- Events
- Event Technology
- Ticketing
- Marketplace
website: https://www.eventbrite.com/
---
