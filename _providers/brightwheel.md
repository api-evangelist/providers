---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-12'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/brightwheel-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mybrightwheel.com
- group: start
  title: ''
  type: SignUp
  url: https://schools.mybrightwheel.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/brightwheel
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/brightwheel
- group: docs
  title: ''
  type: Documentation
  url: https://help.mybrightwheel.com/en/
- group: commercial
  title: ''
  type: Pricing
  url: https://mybrightwheel.com/pricing/
- group: company
  title: ''
  type: GovernmentPartners
  url: https://mybrightwheel.com/government-and-network-partners/
created: '2026-07-03'
description: Brightwheel (mybrightwheel.com) is an all-in-one childcare and early education management platform used by childcare centers, preschools, and early-learning programs to run daily operations - attendance and check-in, digital daily sheets, tuition billing and payments, enrollment and admissions, staff/timecards, classroom (room) management, learning assessments, and real-time parent messaging and photo/video sharing. As of this catalog entry, Brightwheel does NOT publish a documented, self-serve public or partner developer API. There is no developer portal, API reference, API key signup, OpenAPI specification, or webhook documentation. The only Brightwheel API activity that is publicly acknowledged is bespoke, contract-scoped work built for individual government partners - for example a private API implemented to submit attendance and subsidy data to Iowa's childcare subsidy data system - and inbound integrations where Brightwheel pushes data into third-party products (e.g. staff
  timecards to Gusto for payroll). None of these expose a documented API surface that outside developers can build against. This entry is therefore an honest stub documenting the provider and its access model; no API definitions are asserted because none are publicly documented.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/brightwheel.png
layout: provider
modified: '2026-07-03'
name: Brightwheel
nav: Providers
network: true
overview: 'Brightwheel is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Childcare, Early Education, Preschool, Childcare Management, and Attendance.


  Brightwheel''s developer surface includes signup flow, documentation, pricing, and 5 more developer resources.'
random_paper: 93
score:
  band: minimal
  composite: 11.8
  delta: 0.0
  facets:
    commercial_clarity: 23.7
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 11.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 9.4
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/brightwheel/refs/heads/main/screenshots/brightwheel-2026-07-25T203855.png
security:
- kind: domain-security
  name: Brightwheel Domain Security
  slug: brightwheel-domain-security
  summary_line: TLSv1.3 · DMARC
slug: brightwheel
tags:
- Childcare
- Early Education
- Preschool
- Childcare Management
- Attendance
- Billing
- Payments
- Parent Communication
- EdTech
- No Public API
website: https://mybrightwheel.com
---
