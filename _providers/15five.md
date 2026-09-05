---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
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
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: RESTful API for reading and modifying 15Five account data, including users, groups, objectives (OKRs), check-ins, review cycles, and performance data. Supports bulk list fetches with pagination and us
  name: 15Five Public API
  slug: 15five-public-api
artifact_total: 8
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/15five-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/15five-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.15five.com/
- group: docs
  title: ''
  type: Documentation
  url: https://my.15five.com/api/public/
- group: operate
  title: ''
  type: HelpCenter
  url: https://success.15five.com/hc/en-us/articles/360002699631-API
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/15five
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/15five
- group: other
  title: ''
  type: X
  url: https://x.com/15Five
- group: company
  title: ''
  type: Blog
  url: https://www.15five.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.15five.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.15five.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/15five-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/15five-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/15five-finops.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/15five-context.jsonld
created: '2026-06-12'
description: 15Five is a continuous performance management platform that enables organizations to manage employee check-ins, OKRs, 1-on-1 meetings, pulse surveys, and manager effectiveness data. The platform provides a REST API that allows IT admins and developers to read and modify 15Five account data via custom-built integrations. Authentication is handled via API keys using HTTP Basic Auth, and requests are rate-limited to 5 per second per IP address. The API supports reading user and organizational data, objectives, review cycles, and group management, and is available to customers on applicable subscription plans.
finops:
- name: 15Five Finops
  service_category: ''
  slug: 15five-finops
graphqls:
- description: 'This document describes a conceptual GraphQL schema for the 15Five continuous performance management platform. The schema is derived from the 15Five Public REST API and models the core domain objects '
  name: 15Five GraphQL Schema
  slug: 15five-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/15five.png
jsonld:
- class_count: 18
  name: 15Five Context
  property_count: 7
  slug: 15five-context
layout: provider
modified: '2026-06-12'
name: 15Five
nav: Providers
network: true
overview: '15Five publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Performance Management, Employee Engagement, OKRs, Check-ins, and HR.


  The 15Five catalog on APIs.io includes 1 JSON-LD context.


  15Five''s developer surface includes documentation, engineering blog, pricing, and 12 more developer resources.'
plans:
- name: 15Five Plans Pricing
  plan_count: 3
  slug: 15five-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 1
  name: 15Five Rate Limits
  slug: 15five-rate-limits
score:
  band: developing
  composite: 39.4
  coverage:
    artifact_dirs: 9
    catalog_earned: 68.0
    catalog_earned_first_party: 0.0
    catalog_gap: 47.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 57.9
    commercial_clarity: 57.9
    contract_governance: 0.0
    contract_quality: 50.0
    developer_ergonomics: 16.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 39.5
  previous_composite: 39.4
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/15five/refs/heads/main/screenshots/15five-2026-06-20T162310.png
security:
- kind: domain-security
  name: 15Five Domain Security
  slug: 15five-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: 15Five Trust Center
  slug: 15five-trust-center
  summary_line: SOC 2, GDPR
slug: 15five
tags:
- Performance Management
- Employee Engagement
- OKRs
- Check-ins
- HR
- Human Resources
- 1-on-1 Meetings
- Pulse Surveys
website: https://www.15five.com/
---
