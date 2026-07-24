---
access_model:
  confidence: high
  label: Freemium (free trial) · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 22
  human_in_the_loop: 0
  name: Folk App Agentic Access
  operation_count: 39
  slug: folk-app-agentic-access
  summary_line: 39 operations · 22 acting
api_count: 9
apis:
- description: Company (organization) records.
  name: Folk Companies API
  slug: folk-app-companies-api
- description: Deals and other group-scoped custom objects.
  name: Folk Deals API
  slug: folk-app-deals-api
- description: Groups and their custom field definitions.
  name: Folk Groups API
  slug: folk-app-groups-api
- description: Recorded interactions on the relationship timeline.
  name: Folk Interactions API
  slug: folk-app-interactions-api
- description: Free-form notes attached to contacts.
  name: Folk Notes API
  slug: folk-app-notes-api
- description: People (contacts) - the core relationship records in Folk.
  name: Folk People API
  slug: folk-app-people-api
- description: Dated follow-up reminders.
  name: Folk Reminders API
  slug: folk-app-reminders-api
- description: Workspace users (members).
  name: Folk Users API
  slug: folk-app-users-api
- description: Real-time change-event subscriptions.
  name: Folk Webhooks API
  slug: folk-app-webhooks-api
artifact_total: 16
collections:
- collection_type: open
  name: Folk External API
  slug: open-folk-app
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/folk-app-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/folk-app-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/folk-app-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/folk-app
- group: company
  title: ''
  type: Website
  url: https://www.folk.app
- group: docs
  title: ''
  type: Documentation
  url: https://developer.folk.app
- group: commercial
  title: ''
  type: Plans
  url: plans/folk-app-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/folk-app-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/folk-app-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.folk.app/blog
created: '2026-07-02'
description: Folk is a lightweight, relationship-focused CRM for people who build their business on relationships. Folk's public REST API (versioned by date, base https://api.folk.app/v1, Bearer API key auth) lets you programmatically manage people, companies, groups, deals and other custom objects, notes, reminders, and interactions, and subscribe to real-time changes through webhooks. API access is a paid-plan feature.
finops:
- name: Folk App Finops
  service_category: CRM and Relationship Management
  slug: folk-app-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/folk-app.png
layout: provider
modified: '2026-07-02'
name: Folk
nav: Providers
network: true
overview: 'Folk publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Companies API, Deals API, Groups API, and 6 more. Tagged areas include CRM, Relationships, Contacts, Sales, and Pipeline.


  Folk''s developer surface includes authentication, documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Folk App Plans Pricing
  plan_count: 4
  slug: folk-app-plans-pricing
random_paper: 29
rate_limits:
- limit_count: 2
  name: Folk App Rate Limits
  slug: folk-app-rate-limits
score:
  band: thin
  composite: 35.4
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 54.7
    developer_ergonomics: 21.7
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 35.4
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Folk App Authentication
  slug: folk-app-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Folk App Domain Security
  slug: folk-app-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: folk-app
tags:
- CRM
- Relationships
- Contacts
- Sales
- Pipeline
- Webhooks
website: https://www.folk.app
---
