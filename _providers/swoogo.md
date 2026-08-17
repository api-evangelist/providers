---
access_model:
  confidence: high
  label: Paid (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: paid
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
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 17
  human_in_the_loop: 0
  name: Swoogo Agentic Access
  operation_count: 27
  slug: swoogo-agentic-access
  summary_line: 27 operations · 17 acting
api_count: 6
apis:
- description: OAuth2 client-credentials token exchange.
  name: Swoogo Authentication API
  slug: swoogo-authentication-api
- description: Organization-level CRM contacts and contact fields.
  name: Swoogo Contacts API
  slug: swoogo-contacts-api
- description: Events and their fields, questions, websites, folders, and badges.
  name: Swoogo Events API
  slug: swoogo-events-api
- description: Attendees, check-in, groups, session registration, and types.
  name: Swoogo Registrants API
  slug: swoogo-registrants-api
- description: Agenda sessions, locations, fees, attendance, and scans.
  name: Swoogo Sessions API
  slug: swoogo-sessions-api
- description: Speakers and their session assignments.
  name: Swoogo Speakers API
  slug: swoogo-speakers-api
artifact_total: 22
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Swoogo Authentication API
  slug: open-swoogo-authentication-api
- collection_type: open
  name: Swoogo Authentication Contacts API
  slug: open-swoogo-contacts-api
- collection_type: open
  name: Swoogo Authentication Events API
  slug: open-swoogo-events-api
- collection_type: open
  name: Swoogo Authentication Registrants API
  slug: open-swoogo-registrants-api
- collection_type: open
  name: Swoogo Authentication Sessions API
  slug: open-swoogo-sessions-api
- collection_type: open
  name: Swoogo Authentication Speakers API
  slug: open-swoogo-speakers-api
- collection_type: open
  name: Swoogo API
  slug: open-swoogo
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/swoogo-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/swoogo-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/swoogo-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/swoogo-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/swoogo-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/swoogo
- group: company
  title: ''
  type: Website
  url: https://swoogo.events
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.swoogo.com
- group: docs
  title: ''
  type: Documentation
  url: https://swoogo.readme.io/docs
- group: auth
  title: ''
  type: Authentication
  url: https://swoogo.readme.io/docs/authentication
- group: start
  title: ''
  type: SignUp
  url: https://swoogo.events/pricing
- group: commercial
  title: ''
  type: Plans
  url: plans/swoogo-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/swoogo-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/swoogo-finops.yml
created: '2026-07-05'
description: Swoogo is an event management and event registration platform for building event websites, registration forms, agendas, and badges across in-person, virtual, and hybrid events. Swoogo exposes a documented public REST API at https://api.swoogo.com/api/v1 secured with OAuth2 client-credentials (bearer tokens that expire every 30 minutes). The API covers events, registrants, sessions, speakers, sponsors, tracks, packages, discount codes, transactions, contacts (CRM), call-for-speakers submissions, invitation lists, and webhooks - roughly 140 endpoints. Access requires a paid Swoogo subscription; API credentials are issued from My Profile > API Credentials in the Swoogo app.
finops:
- name: Swoogo Finops
  service_category: Event Management Software
  slug: swoogo-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/swoogo.png
layout: provider
modified: '2026-07-05'
name: Swoogo
nav: Providers
network: true
overview: 'Swoogo publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Contacts API, Events API, and 3 more. Tagged areas include Event Management, Event Registration, Events, Sessions, and Speakers.


  Swoogo''s developer surface includes authentication, documentation, signup flow, and 11 more developer resources.'
plans:
- name: Swoogo Plans Pricing
  plan_count: 3
  slug: swoogo-plans-pricing
random_paper: 74
rate_limits:
- limit_count: 4
  name: Swoogo Rate Limits
  slug: swoogo-rate-limits
score:
  band: developing
  composite: 44.7
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 61.7
    developer_ergonomics: 28.3
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 44.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
security:
- kind: authentication
  name: Swoogo Authentication
  slug: swoogo-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Swoogo Domain Security
  slug: swoogo-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Swoogo Vulnerability Disclosure
  slug: swoogo-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Swoogo Trust Center
  slug: swoogo-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, GDPR
slug: swoogo
tags:
- Event Management
- Event Registration
- Events
- Sessions
- Speakers
- Attendees
- SaaS
website: https://swoogo.events
---
