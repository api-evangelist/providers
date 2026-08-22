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
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-19'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/churchtrac-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/churchtrac
- group: company
  title: ''
  type: Website
  url: https://www.churchtrac.com/
- group: operate
  title: ''
  type: Support
  url: https://www.churchtrac.com/support
- group: commercial
  title: ''
  type: Plans
  url: https://www.churchtrac.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.churchtrac.com/blog
created: '2026-07-03'
description: ChurchTrac is all-in-one church management software (ChMS) for small and large churches, covering people and member management, church directory, groups, attendance and check-in, event registration, worship planning and volunteer scheduling, online giving, and fund accounting/budgeting. ChurchTrac does NOT publish a public or partner developer API - there is no documented REST API, API keys, OAuth, or webhooks for building against ChurchTrac data. Its "integrations" are ChurchTrac consuming third-party services (Stripe for giving, SendGrid/Mailchimp for email, Twilio for texting, QuickBooks for accounting, Zoom); member-facing access is via the Church Connect app and embeddable online giving forms, not a programmable API surface. This entry is documented as an honest stub.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/churchtrac.png
layout: provider
modified: '2026-07-03'
name: ChurchTrac
nav: Providers
network: true
overview: 'ChurchTrac is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Church Management, ChMS, Nonprofit, Membership, and Online Giving.


  ChurchTrac''s developer surface includes support, engineering blog, and 4 more developer resources.'
random_paper: 13
score:
  band: minimal
  composite: 6.4
  delta: 0.1
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.3
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: domain-security
  name: Churchtrac Domain Security
  slug: churchtrac-domain-security
  summary_line: TLSv1.2 · DMARC
slug: churchtrac
tags:
- Church Management
- ChMS
- Nonprofit
- Membership
- Online Giving
- Church Accounting
- Attendance
- No Public API
website: https://www.churchtrac.com/
---
