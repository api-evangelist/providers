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
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Eventzilla Agentic Access
  operation_count: 19
  slug: eventzilla-agentic-access
  summary_line: 19 operations · 7 acting
api_count: 7
apis:
- description: Attendee management and check-in operations
  name: Eventzilla Attendees API
  slug: eventzilla-attendees-api
- description: Event category operations
  name: Eventzilla Categories API
  slug: eventzilla-categories-api
- description: Checkout workflow operations
  name: Eventzilla Checkout API
  slug: eventzilla-checkout-api
- description: Event listing and detail operations
  name: Eventzilla Events API
  slug: eventzilla-events-api
- description: Ticket type operations
  name: Eventzilla Tickets API
  slug: eventzilla-tickets-api
- description: Transaction and order operations
  name: Eventzilla Transactions API
  slug: eventzilla-transactions-api
- description: Organizer and sub-organizer operations
  name: Eventzilla Users API
  slug: eventzilla-users-api
artifact_total: 36
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Eventzilla Attendees API
  slug: open-eventzilla-attendees-api
- collection_type: open
  name: Eventzilla Attendees Categories API
  slug: open-eventzilla-categories-api
- collection_type: open
  name: Eventzilla Attendees Checkout API
  slug: open-eventzilla-checkout-api
- collection_type: open
  name: Eventzilla Attendees Events API
  slug: open-eventzilla-events-api
- collection_type: open
  name: Eventzilla Attendees Tickets API
  slug: open-eventzilla-tickets-api
- collection_type: open
  name: Eventzilla Attendees Transactions API
  slug: open-eventzilla-transactions-api
- collection_type: open
  name: Eventzilla Attendees Users API
  slug: open-eventzilla-users-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/eventzilla-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/eventzilla-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/eventzilla-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://developer.eventzilla.net/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.eventzilla.net/docs/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.eventzilla.net/pricing/
- group: company
  title: ''
  type: Blog
  url: https://www.eventzilla.net/blog/
- group: operate
  title: ''
  type: Support
  url: https://community.eventzilla.net/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.eventzilla.net/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.eventzilla.net/privacy-policy/
- group: start
  title: ''
  type: Login
  url: https://app.eventzilla.net/us/login
- group: start
  title: ''
  type: Signup
  url: https://www.eventzilla.net/
- group: company
  title: ''
  type: About
  url: https://www.eventzilla.net/about/
description: Eventzilla is an event registration and ticketing platform that provides a REST API for managing events, ticket types, registrations, discounts, and attendee check-in workflows. The API uses predictable, resource-oriented URLs organized around the JSON format, enabling integrations for event creation, attendee management, order processing, and check-in operations.
examples:
- key_count: 2
  name: Checkin Request
  slug: checkin-request
- key_count: 6
  name: Checkin Response
  slug: checkin-response
- key_count: 4
  name: Checkout Create Request
  slug: checkout-create-request
- key_count: 8
  name: Checkout Create Response
  slug: checkout-create-response
- key_count: 2
  name: List Events
  slug: list-events
finops:
- name: Overview
  service_category: ''
  slug: overview
image: https://www.eventzilla.net/favicon.ico
json_schemas:
- name: Attendee
  property_count: 20
  slug: attendee
- name: Event
  property_count: 25
  slug: event
- name: Ticket
  property_count: 23
  slug: ticket
- name: Transaction
  property_count: 20
  slug: transaction
- name: User
  property_count: 20
  slug: user
jsonld:
- class_count: 56
  name: context Context
  property_count: 6
  slug: context
layout: provider
modified: '2026-06-13'
name: Eventzilla
nav: Providers
network: true
overview: 'Eventzilla publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Attendees API, Categories API, Checkout API, and 4 more. Tagged areas include Events, Ticketing, Registration, Attendees, and Event Management.


  The Eventzilla catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Eventzilla''s developer surface includes authentication, developer portal, documentation, pricing, engineering blog, support, signup flow, and 6 more developer resources.'
plans:
- name: Basic
  plan_count: 0
  slug: basic
- name: Plus
  plan_count: 0
  slug: plus
- name: Pro
  plan_count: 0
  slug: pro
- name: Unlimited
  plan_count: 0
  slug: unlimited
random_paper: 15
rate_limits:
- limit_count: 2
  name: Default
  slug: default
rules:
- effective_rule_count: 5
  extends: []
  name: Eventzilla API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: eventzilla-jsonschema-spectral-rules
score:
  band: developing
  composite: 41.4
  delta: -9.3
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 9.8
    contract_quality: 61.3
    developer_ergonomics: 38.1
    discoverability: 74.1
    governance: 9.8
    operational_transparency: 21.1
  previous_composite: 50.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/eventzilla/refs/heads/main/screenshots/eventzilla-2026-06-20T180909.png
security:
- kind: authentication
  name: Eventzilla Authentication
  slug: eventzilla-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Eventzilla Domain Security
  slug: eventzilla-domain-security
  summary_line: TLSv1.2 · DMARC
slug: eventzilla
tags:
- Events
- Ticketing
- Registration
- Attendees
- Event Management
website: https://developer.eventzilla.net/
---
