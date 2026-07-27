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
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Choozle Agentic Access
  operation_count: 3
  slug: choozle-agentic-access
  summary_line: 3 operations · 1 acting
api_count: 3
apis:
- description: The Accounts API from Choozle — 1 operation(s) for accounts.
  name: Choozle Accounts API
  slug: choozle-accounts-api
- description: The Authorization API from Choozle — 1 operation(s) for authorization.
  name: Choozle Authorization API
  slug: choozle-authorization-api
- description: The Reports API from Choozle — 1 operation(s) for reports.
  name: Choozle Reports API
  slug: choozle-reports-api
artifact_total: 12
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/choozle-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/choozle-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/choozle-authentication.yml
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/choozle/refs/heads/main/plans/plans.md
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/choozle/refs/heads/main/rate-limits/rate-limits.md
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/choozle/refs/heads/main/finops/finops.md
- group: company
  title: ''
  type: Website
  url: https://choozle.com/
- group: docs
  title: ''
  type: Documentation
  url: https://help.choozle.com/
- group: company
  title: ''
  type: Blog
  url: https://choozle.com/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://choozle.com/terms-of-service/
- group: other
  title: ''
  type: Platform
  url: https://choozle.com/the-platform/
created: '2026-06-13'
description: Choozle is a self-service digital advertising platform providing REST APIs for managing programmatic campaigns, audience segments, creative assets, publisher deals, and performance reporting across Display, CTV, Video, Audio, Native, DOOH, Search, and Social channels.
examples:
- key_count: 3
  name: Get Reports
  slug: get-reports
- key_count: 3
  name: Get Token
  slug: get-token
- key_count: 3
  name: List Accounts
  slug: list-accounts
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/choozle.png
json_schemas:
- name: AuthorizationRequest
  property_count: 3
  slug: authorization-request
- name: ReportRow
  property_count: 10
  slug: report-row
layout: provider
modified: '2026-06-13'
name: Choozle
nav: Providers
network: true
overview: 'Choozle publishes 3 APIs on the [APIs.io](https://apis.io/) network: Accounts API, Authorization API, and Reports API. Tagged areas include Digital Advertising, Programmatic Advertising, DSP, Demand-Side Platform, and Campaign Management.


  The Choozle catalog on APIs.io includes 1 Spectral governance ruleset.


  Choozle''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
random_paper: 8
rules:
- name: Choozle API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: choozle-jsonschema-spectral-rules
score:
  band: thin
  composite: 40.8
  delta: 0.0
  facets:
    commercial_clarity: 10.5
    contract_quality: 61.9
    developer_ergonomics: 21.7
    discoverability: 100.0
    governance: 73.7
    operational_transparency: 0.0
  previous_composite: 40.8
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/choozle/refs/heads/main/screenshots/choozle-2026-06-20T174326.png
security:
- kind: authentication
  name: Choozle Authentication
  slug: choozle-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Choozle Domain Security
  slug: choozle-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: choozle
tags:
- Digital Advertising
- Programmatic Advertising
- DSP
- Demand-Side Platform
- Campaign Management
- Audience Targeting
- Display Advertising
- Connected TV
- CTV
- Video Advertising
- Native Advertising
- DOOH
- Reporting
- Real-Time Bidding
- RTB
website: https://choozle.com/
---
