---
access_model:
  confidence: high
  label: Paid (free trial) · Open access
  onboarding: open
  pricing: paid
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
- acting_count: 54
  human_in_the_loop: 0
  name: Pirsch Agentic Access
  operation_count: 97
  slug: pirsch-agentic-access
  summary_line: 97 operations · 54 acting
api_count: 15
apis:
- description: Manage shareable access links for dashboard visibility
  name: Pirsch Access Links API
  slug: pirsch-access-links-api
- description: Obtain access tokens using OAuth2 client credentials
  name: Pirsch Authentication API
  slug: pirsch-authentication-api
- description: Manage OAuth2 and access-key API clients
  name: Pirsch Clients API
  slug: pirsch-clients-api
- description: Define and manage conversion goals with path patterns or events
  name: Pirsch Conversion Goals API
  slug: pirsch-conversion-goals-api
- description: Manage tracked domains and their configuration
  name: Pirsch Domains API
  slug: pirsch-domains-api
- description: Schedule and manage recurring email analytics reports
  name: Pirsch Email Reports API
  slug: pirsch-email-reports-api
- description: Define and manage multi-step conversion funnels
  name: Pirsch Funnels API
  slug: pirsch-funnels-api
- description: Manage domain members, roles, and invitations
  name: Pirsch Members API
  slug: pirsch-members-api
- description: Create and manage UTM-enriched short links
  name: Pirsch Short Links API
  slug: pirsch-short-links-api
- description: Query analytics statistics by date range and filter criteria
  name: Pirsch Statistics API
  slug: pirsch-statistics-api
- description: Send page views, events, and session keep-alive signals
  name: Pirsch Tracking API
  slug: pirsch-tracking-api
- description: Filter traffic and configure spike/warning notifications
  name: Pirsch Traffic Management API
  slug: pirsch-traffic-management-api
- description: Manage the authenticated user account
  name: Pirsch User API
  slug: pirsch-user-api
- description: Save and manage custom analytics views
  name: Pirsch Views API
  slug: pirsch-views-api
- description: Configure webhooks for event-driven integrations
  name: Pirsch Webhooks API
  slug: pirsch-webhooks-api
artifact_total: 32
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/pirsch-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pirsch-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/pirsch-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://pirsch.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.pirsch.io
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/pirsch-analytics
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/products/emvi-software-gmbh-pirsch-analytics/
- group: company
  title: ''
  type: Blog
  url: https://pirsch.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://pirsch.io/pricing
- group: other
  title: ''
  type: X
  url: https://x.com/PirschAnalytics
- group: commercial
  title: ''
  type: Plans
  url: plans/pirsch-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/pirsch-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/pirsch-finops.yml
created: '2026-06-13'
description: Pirsch is a privacy-first website analytics platform built and hosted in Germany. GDPR, CCPA, PECR, and Schrems II compliant, it tracks page views, sessions, custom events, conversion goals, funnels, and traffic sources without cookies or personal data storage. Developers access all data via a RESTful API with OAuth and access-key authentication, supported by official Go, JavaScript, and PHP SDKs.
examples:
- key_count: 16
  name: Pirsch Domain Example
  slug: pirsch-domain-example
- key_count: 8
  name: Pirsch Event Request Example
  slug: pirsch-event-request-example
- key_count: 10
  name: Pirsch Hit Request Example
  slug: pirsch-hit-request-example
- key_count: 2
  name: Pirsch Token Request Example
  slug: pirsch-token-request-example
- key_count: 2
  name: Pirsch Token Response Example
  slug: pirsch-token-response-example
finops:
- name: Pirsch Finops
  service_category: ''
  slug: pirsch-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pirsch.png
json_schemas:
- name: Domain
  property_count: 16
  slug: pirsch-domain
- name: EventRequest
  property_count: 14
  slug: pirsch-event-request
- name: HitRequest
  property_count: 13
  slug: pirsch-hit-request
- name: VisitorStats
  property_count: 12
  slug: pirsch-visitor-stats
jsonld:
- class_count: 7
  name: Pirsch Context
  property_count: 63
  slug: pirsch-context
layout: provider
modified: '2026-06-13'
name: Pirsch
nav: Providers
network: true
overview: 'Pirsch publishes 15 APIs on the [APIs.io](https://apis.io/) network, including Access Links API, Authentication API, Clients API, and 12 more. Tagged areas include Analytics, Web Analytics, Privacy, GDPR, and Cookie-Free.


  The Pirsch catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Pirsch''s developer surface includes authentication, documentation, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Pirsch Plans Pricing
  plan_count: 3
  slug: pirsch-plans-pricing
random_paper: 37
rate_limits:
- limit_count: 3
  name: Pirsch Rate Limits
  slug: pirsch-rate-limits
rules:
- name: Pirsch API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: pirsch-jsonschema-spectral-rules
score:
  band: developing
  composite: 53.1
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 60.5
    developer_ergonomics: 21.7
    discoverability: 100.0
    governance: 73.7
    operational_transparency: 36.8
  previous_composite: 53.1
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pirsch/refs/heads/main/screenshots/pirsch-2026-06-20T191730.png
security:
- kind: authentication
  name: Pirsch Authentication
  slug: pirsch-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Pirsch Domain Security
  slug: pirsch-domain-security
  summary_line: TLSv1.3 · DMARC
slug: pirsch
tags:
- Analytics
- Web Analytics
- Privacy
- GDPR
- Cookie-Free
- Page Views
- Sessions
- Events
- Conversion Goals
- Funnels
- Traffic Sources
website: https://pirsch.io
---
