---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
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
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: REST API for managing customer satisfaction surveys, retrieving ratings and comments, tracking CSAT, CES, and NPS scores, and managing users, teams, and customers within the Nicereply platform.
  name: Nicereply API
  slug: nicereply-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nicereply-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.nicereply.com
- group: docs
  title: ''
  type: Documentation
  url: https://cdn.nicereply.com/s/api/latest/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/nicereply
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/nicereply
- group: company
  title: ''
  type: Blog
  url: https://www.nicereply.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.nicereply.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://stats.uptimerobot.com/M9lQEFqLDv
- group: other
  title: ''
  type: X
  url: https://twitter.com/nice_reply
- group: commercial
  title: ''
  type: Plans
  url: plans/nicereply-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/nicereply-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/nicereply-finops.yml
created: '2026-06-13'
description: Nicereply is a customer satisfaction and NPS survey platform providing a REST API for managing surveys, accessing ratings and comments, tracking CSAT, CES, and NPS scores, and integrating with helpdesks such as Zendesk, Front, and Helpscout.
finops:
- name: Nicereply Finops
  service_category: ''
  slug: nicereply-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nicereply.png
layout: provider
modified: '2026-06-13'
name: Nicereply
nav: Providers
network: true
overview: 'Nicereply publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Customer Satisfaction, CSAT, CES, NPS, and Surveys.


  Nicereply''s developer surface includes documentation, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Nicereply Plans Pricing
  plan_count: 5
  slug: nicereply-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Nicereply Rate Limits
  slug: nicereply-rate-limits
score:
  band: emerging
  composite: 22.0
  coverage:
    artifact_dirs: 7
    catalog_earned: 52.0
    catalog_earned_first_party: 0.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 22.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nicereply/refs/heads/main/screenshots/nicereply-2026-06-20T190319.png
security:
- kind: domain-security
  name: Nicereply Domain Security
  slug: nicereply-domain-security
  summary_line: TLSv1.3 · DMARC
slug: nicereply
tags:
- Customer Satisfaction
- CSAT
- CES
- NPS
- Surveys
- Help Desk
- Customer Experience
website: https://www.nicereply.com
---
