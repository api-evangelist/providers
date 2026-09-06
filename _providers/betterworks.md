---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
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
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: The BetterWorks REST API enables programmatic access to goals, milestones, employee data, feedback, recognition, calibration data, and performance ratings. Developers can retrieve complete goal detail
  name: BetterWorks API
  slug: betterworks-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/betterworks-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.betterworks.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.betterworks.com/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/BetterWorks
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/betterworks
- group: company
  title: ''
  type: Blog
  url: https://www.betterworks.com/magazine/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.betterworks.com/plans
- group: operate
  title: ''
  type: StatusPage
  url: https://www.betterworks.com/system-uptime-metrics/
- group: other
  title: ''
  type: X
  url: https://x.com/betterworks
- group: commercial
  title: ''
  type: Plans
  url: plans/betterworks-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/betterworks-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/betterworks-finops.yml
- group: company
  title: ''
  type: BlogPosts
  url: blogs/blogs.json
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/betterworks-context.jsonld
created: 2026-06-13
description: BetterWorks is an enterprise continuous performance management platform that enables organizations to align, develop, and engage their workforce through OKR-based goal setting, check-ins, feedback, and calibration. The platform provides a REST API allowing developers to programmatically access and update goals, employee data, feedback, recognition, and performance ratings. API access supports integration with business-critical applications to automate progress tracking and synchronize workforce data across enterprise systems. BetterWorks serves mid-market and enterprise organizations starting at 500 employees, with robust API and integration capabilities included across all plans.
finops:
- name: Betterworks Finops
  service_category: ''
  slug: betterworks-finops
graphqls:
- description: This conceptual GraphQL schema represents the BetterWorks continuous performance management platform API surface. BetterWorks provides an enterprise platform for OKR-based goal setting, check-ins, fee
  name: BetterWorks GraphQL Schema
  slug: betterworks-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/betterworks.png
jsonld:
- class_count: 3
  name: Betterworks Context
  property_count: 16
  slug: betterworks-context
layout: provider
modified: 2026-06-13
name: BetterWorks
nav: Providers
network: true
overview: 'BetterWorks publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include OKR, Performance Management, Goals, Employee Data, and HR.


  The BetterWorks catalog on APIs.io includes 1 JSON-LD context.


  BetterWorks'' developer surface includes documentation, engineering blog, pricing, and 11 more developer resources.'
plans:
- name: Betterworks Plans Pricing
  plan_count: 3
  slug: betterworks-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Betterworks Rate Limits
  slug: betterworks-rate-limits
score:
  band: thin
  composite: 33.4
  coverage:
    artifact_dirs: 8
    catalog_earned: 60.0
    catalog_earned_first_party: 0.0
    catalog_gap: 55.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 50.0
    developer_ergonomics: 16.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 33.4
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/betterworks/refs/heads/main/screenshots/betterworks-2026-06-20T173210.png
security:
- kind: domain-security
  name: Betterworks Domain Security
  slug: betterworks-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: betterworks
tags:
- OKR
- Performance Management
- Goals
- Employee Data
- HR
- Enterprise
- Feedback
- Check-ins
- Continuous Performance
- People Analytics
website: https://www.betterworks.com/
---
