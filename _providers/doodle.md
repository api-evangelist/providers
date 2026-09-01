---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: The Doodle REST API for programmatically creating and managing group polls, booking pages, and meeting scheduling. This API has been deprecated and Doodle no longer supports new API integrations. Ente
  name: Doodle Scheduling API (Deprecated)
  slug: doodle-scheduling-api-deprecated
artifact_total: 7
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/doodle-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/doodle-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://doodle.com
- group: docs
  title: ''
  type: Documentation
  url: https://help.doodle.com
- group: company
  title: ''
  type: Blog
  url: https://doodle.com/en/resources/
- group: commercial
  title: ''
  type: Pricing
  url: https://doodle.com/en/premium/
- group: operate
  title: ''
  type: StatusPage
  url: https://uptime.doodle.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/doodle-ag/
- group: other
  title: ''
  type: X
  url: https://x.com/doodletweet
- group: commercial
  title: ''
  type: Plans
  url: plans/doodle-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/doodle-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/doodle-finops.yml
created: 2026-06-12
description: Doodle is a meeting scheduling platform that simplifies group coordination through polls, booking pages, 1:1 meeting links, and sign-up sheets. The platform automatically finds optimal meeting times by reading participant calendars and supports cross-timezone scheduling for distributed teams. Doodle integrates with Google Calendar, Microsoft Office 365, Zoom, Microsoft Teams, Google Meet, Webex, Stripe, and Zapier for workflow automation. The legacy public REST API has been officially deprecated and Doodle no longer supports new API integrations; enterprise customers with existing API implementations may contact support for continued assistance. Automation is now primarily available via Zapier on Professional and higher plans.
finops:
- name: Doodle Finops
  service_category: ''
  slug: doodle-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/doodle.png
jsonld:
- class_count: 19
  name: Doodle Context
  property_count: 0
  slug: doodle-context
layout: provider
modified: 2026-06-12
name: Doodle
nav: Providers
network: true
overview: 'Doodle publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Scheduling, Meetings, Calendar, Group Polls, and Booking Pages.


  The Doodle catalog on APIs.io includes 1 JSON-LD context.


  Doodle''s developer surface includes documentation, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Doodle Plans Pricing
  plan_count: 4
  slug: doodle-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 5
  name: Doodle Rate Limits
  slug: doodle-rate-limits
score:
  band: thin
  composite: 29.6
  coverage:
    artifact_dirs: 7
    catalog_gap: 43.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 57.9
    commercial_clarity: 57.9
    contract_governance: 0.0
    contract_quality: 10.7
    developer_ergonomics: 11.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 47.4
  previous_composite: 29.6
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/doodle/refs/heads/main/screenshots/doodle-2026-06-20T180154.png
security:
- kind: domain-security
  name: Doodle Domain Security
  slug: doodle-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Doodle Trust Center
  slug: doodle-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: doodle
tags:
- Scheduling
- Meetings
- Calendar
- Group Polls
- Booking Pages
- Time Management
- Productivity
website: https://doodle.com
---
