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
  band: agent-aware
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 15.5
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: REST API for the Clockwise AI calendar optimization platform, providing programmatic access to focus time management, meeting preferences, scheduling links, and team calendar coordination features.
  name: Clockwise REST API
  slug: clockwise-rest-api
artifact_total: 6
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/salesforce/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/clockwise-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.getclockwise.com
- group: docs
  title: ''
  type: Documentation
  url: https://support.getclockwise.com/hc/en-us
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/clockwisehq
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/clockwise-inc.
- group: company
  title: ''
  type: Blog
  url: https://www.getclockwise.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.getclockwise.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.getclockwise.com/
- group: other
  title: ''
  type: X
  url: https://x.com/getclockwise
- group: commercial
  title: ''
  type: Plans
  url: plans/clockwise-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/clockwise-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/clockwise-finops.yml
created: '2026-06-13'
description: Clockwise was an AI-powered calendar optimization platform that helped individuals, teams, and organizations protect focus time, reduce meeting overload, and coordinate scheduling intelligently. The platform provided REST APIs for managing focus time blocks, meeting preferences, smart scheduling links, and team calendar coordination. Clockwise was acquired by Salesforce and shut down on March 27, 2026.
finops:
- name: Clockwise Finops
  service_category: ''
  slug: clockwise-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/clockwise.png
jsonld:
- class_count: 20
  name: Clockwise Context
  property_count: 0
  slug: clockwise-context
layout: provider
modified: '2026-08-21'
name: Clockwise
nav: Providers
network: true
overview: 'Clockwise publishes 1 API on the [APIs.io](https://apis.io/) network: REST API. Tagged areas include Calendar, Artificial Intelligence, Scheduling, Focus Time, and Productivity.


  The Clockwise catalog on APIs.io includes 1 JSON-LD context.


  Clockwise''s developer surface includes documentation, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Clockwise Plans Pricing
  plan_count: 4
  slug: clockwise-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 2
  name: Clockwise Rate Limits
  slug: clockwise-rate-limits
score:
  band: thin
  composite: 29.5
  coverage:
    artifact_dirs: 7
    catalog_gap: 47.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 37.3
    developer_ergonomics: 4.8
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 29.5
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/clockwise/refs/heads/main/screenshots/clockwise-2026-06-20T174529.png
security:
- kind: domain-security
  name: Clockwise Domain Security
  slug: clockwise-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: clockwise
tags:
- Calendar
- Artificial Intelligence
- Scheduling
- Focus Time
- Productivity
- Team Coordination
- Meeting Optimization
website: https://www.getclockwise.com
---
