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
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Nylas Agentic Access
  operation_count: 22
  slug: nylas-agentic-access
  summary_line: 22 operations · 8 acting
api_count: 11
apis:
- description: The Nylas v3 REST API provides programmatic access to email, calendar, contacts, scheduling, authentication, and administration features across every major email and calendar provider.
  name: Nylas API
  slug: nylas-api
- description: The Admin API from Nylas — 3 operation(s) for admin.
  name: Nylas Admin API
  slug: nylas-admin-api
- description: The Auth API from Nylas — 3 operation(s) for auth.
  name: Nylas Auth API
  slug: nylas-auth-api
- description: The Calendars API from Nylas — 1 operation(s) for calendars.
  name: Nylas Calendars API
  slug: nylas-calendars-api
- description: The Contacts API from Nylas — 1 operation(s) for contacts.
  name: Nylas Contacts API
  slug: nylas-contacts-api
- description: The Drafts API from Nylas — 1 operation(s) for drafts.
  name: Nylas Drafts API
  slug: nylas-drafts-api
- description: The Events API from Nylas — 1 operation(s) for events.
  name: Nylas Events API
  slug: nylas-events-api
- description: The Grants API from Nylas — 2 operation(s) for grants.
  name: Nylas Grants API
  slug: nylas-grants-api
- description: The Messages API from Nylas — 1 operation(s) for messages.
  name: Nylas Messages API
  slug: nylas-messages-api
- description: The Scheduling API from Nylas — 3 operation(s) for scheduling.
  name: Nylas Scheduling API
  slug: nylas-scheduling-api
- description: The Threads API from Nylas — 1 operation(s) for threads.
  name: Nylas Threads API
  slug: nylas-threads-api
artifact_total: 20
collections:
- collection_type: open
  name: Nylas API (v3)
  slug: open-nylas
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/nylas-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/nylas-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/nylas-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nylas-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/nylas-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/nylas
- group: company
  title: ''
  type: Website
  url: https://www.nylas.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.nylas.com/
- group: company
  title: ''
  type: Blog
  url: https://www.nylas.com/blog/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/nylas
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.nylas.com/legal/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.nylas.com/legal/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.nylas.com/
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.nylas.com/llms.txt
created: '2025-02-06'
description: Nylas connects your application to every email inbox and calendar in the world. The Nylas v3 platform provides REST APIs for email, calendar, contacts, scheduling, authentication, and administration with official SDKs for Node.js, Python, Ruby, and Kotlin/Java.
finops:
- name: Nylas Finops
  service_category: API
  slug: nylas-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nylas.png
layout: provider
modified: '2026-04-28'
name: Nylas
nav: Providers
network: true
overview: 'Nylas publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Admin API, Auth API, Calendars API, and 7 more. Tagged areas include Calendar, Communication, Contacts, Email, and Messaging.


  Nylas'' developer surface includes authentication, documentation, engineering blog, and 11 more developer resources.'
plans:
- name: Nylas Plans Pricing
  plan_count: 3
  slug: nylas-plans-pricing
random_paper: 76
rate_limits:
- limit_count: 5
  name: Nylas Rate Limits
  slug: nylas-rate-limits
score:
  band: developing
  composite: 45.3
  delta: 0.0
  facets:
    commercial_clarity: 68.4
    contract_quality: 53.9
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 45.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 43.1
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nylas/refs/heads/main/screenshots/nylas-2026-06-20T190645.png
security:
- kind: authentication
  name: Nylas Authentication
  slug: nylas-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Nylas Domain Security
  slug: nylas-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Nylas Vulnerability Disclosure
  slug: nylas-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Nylas Trust Center
  slug: nylas-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, HIPAA, GDPR, CSA STAR
slug: nylas
tags:
- Calendar
- Communication
- Contacts
- Email
- Messaging
- Scheduling
website: https://www.nylas.com/
---
