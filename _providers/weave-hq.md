---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Weave Hq Agentic Access
  operation_count: 38
  slug: weave-hq-agentic-access
  summary_line: 38 operations · 11 acting
api_count: 8
apis:
- description: Patient/customer contacts and contact info.
  name: Weave Contacts API
  slug: weave-hq-contacts-api
- description: Platform events and subscription management.
  name: Weave Events API
  slug: weave-hq-events-api
- description: Weave Digital Forms - templates, links, and submissions.
  name: Weave Forms API
  slug: weave-hq-forms-api
- description: Two-way SMS/text messaging with patients.
  name: Weave Messaging API
  slug: weave-hq-messaging-api
- description: Weave Payments methods (text-to-pay, card-on-file).
  name: Weave Payments API
  slug: weave-hq-payments-api
- description: VoIP call records, recordings, voicemails, and call queues.
  name: Weave Phone & Calls API
  slug: weave-hq-phone-calls-api
- description: Review generation, reputation, and business listings.
  name: Weave Reviews API
  slug: weave-hq-reviews-api
- description: Appointments, appointment types, schedules, and calendar events.
  name: Weave Scheduling API
  slug: weave-hq-scheduling-api
artifact_total: 18
collections:
- collection_type: open
  name: Weave API
  slug: open-weave-hq
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/weave-hq-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/weave-hq-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/weave-hq-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/weave-hq-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/weave-hq-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/weave-hq-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/getweave
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/weavehq
- group: company
  title: ''
  type: Website
  url: https://www.getweave.com
- group: docs
  title: ''
  type: Documentation
  url: https://dp.getweave.com
- group: commercial
  title: ''
  type: Plans
  url: plans/weave-hq-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/weave-hq-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/weave-hq-finops.yml
created: '2026-07-03'
description: Weave is an all-in-one customer and patient communication and payments platform for small healthcare businesses - dental, optometry, veterinary, medical, audiology, and specialty practices. It unifies VoIP phone, two-way texting, online scheduling, digital forms, payments (text-to-pay), review generation, and email into a single system that syncs with practice management and EHR software. The Weave developer platform exposes a REST API (base https://api.weaveconnect.com) for building integrations across messaging, phone and calls, contacts, scheduling and appointments, payments, digital forms, reviews, and event subscriptions, authenticated with OAuth 2.0 bearer tokens issued through Weave's OIDC provider. The public API reference is published in the Weave Developer Portal at dp.getweave.com, which requires a developer login.
finops:
- name: Weave Hq Finops
  service_category: Business Communication and Payments
  slug: weave-hq-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/weave-hq.png
layout: provider
modified: '2026-07-03'
name: Weave
nav: Providers
network: true
overview: 'Weave publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Contacts API, Events API, Forms API, and 5 more. Tagged areas include Communication, Healthcare, VoIP, Messaging, and SMS.


  Weave''s developer surface includes authentication, documentation, and 11 more developer resources.'
plans:
- name: Weave Hq Plans Pricing
  plan_count: 4
  slug: weave-hq-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 4
  name: Weave Hq Rate Limits
  slug: weave-hq-rate-limits
scopes:
- name: Weave Hq Scopes
  scope_count: 0
  slug: weave-hq-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 43.0
  delta: 0.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 60.5
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 43.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 55.6
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Weave Hq Authentication
  slug: weave-hq-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Weave Hq Domain Security
  slug: weave-hq-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Weave Hq Vulnerability Disclosure
  slug: weave-hq-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Weave Hq Trust Center
  slug: weave-hq-trust-center
  summary_line: trust center published
slug: weave-hq
tags:
- Communication
- Healthcare
- VoIP
- Messaging
- SMS
- Scheduling
- Payments
- Reviews
- Dental
- Veterinary
website: https://www.getweave.com
---
