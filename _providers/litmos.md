---
access_model:
  confidence: low
  label: Paid · Requires approval
  onboarding: approval
  pricing: paid
  public: false
  source:
  - plans
  - security
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
    event_surface_described: unknown
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 4.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: RESTful API for the Litmos learning management system enabling management of users, teams, courses, learning paths, enrollments, assessments, and completion records. Supports JSON and XML data formats
  name: Litmos API
  slug: litmos-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.litmos.com/
- group: auth
  href: https://artifacts.apis.io/litmos/security/litmos-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/litmos-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://www.litmos.com/docs/litmos/apis/overview-of-developer-api
- group: start
  title: ''
  type: Signup
  url: https://www.litmos.com/free-trial
- group: start
  title: ''
  type: Login
  url: https://www.litmos.com/login
- group: company
  title: ''
  type: Blog
  url: https://www.litmos.com/blog
- group: operate
  title: ''
  type: Support
  url: https://support.litmos.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.litmos.com/litmos-pricing
- group: design
  title: ''
  type: Webhooks
  url: https://www.litmos.com/docs/litmos/webhooks
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://www.litmos.com/release-notes/tags/api
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Trifoia/litmos-sdk
- group: commercial
  href: https://artifacts.apis.io/litmos/plans/litmos-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/litmos-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/litmos/rate-limits/litmos-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/litmos-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/litmos/finops/litmos-finops.yml
  title: ''
  type: FinOps
  url: finops/litmos-finops.yml
created: '2026-06-13'
description: SAP Litmos is a cloud-based learning management system (LMS) with a REST API for managing courses, learning paths, user enrollment, completions, assessments, and training compliance reporting. The API enables organizations to automate user provisioning, synchronize training data with HR and CRM systems, manage teams, and retrieve completion records for compliance workflows.
finops:
- has_sources: false
  method: generated
  name: Litmos Finops
  primary_unit: ''
  service_category: ''
  slug: litmos-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/litmos.png
layout: provider
modified: '2026-06-13'
name: Litmos
nav: Providers
network: true
overview: 'Litmos is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include LMS, E-Learning, Training, SAP, and Course Management.


  Litmos'' developer surface includes documentation, signup flow, engineering blog, support, pricing, release notes, and 8 more developer resources.'
plans:
- name: Litmos Plans Pricing
  plan_count: 3
  slug: litmos-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 2
  name: Litmos Rate Limits
  slug: litmos-rate-limits
score:
  band: emerging
  composite: 15.7
  coverage:
    artifact_dirs: 10
    catalog_earned: 42.0
    catalog_earned_first_party: 0.0
    catalog_gap: 73.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 25.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 66.1
    operational_transparency: 23.7
  previous_composite: 15.7
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Education & Research
    regime_id: education
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/litmos/litmos-2026-06-20T184608.png
security:
- kind: domain-security
  name: Litmos Domain Security
  slug: litmos-domain-security
  summary_line: TLSv1.3 · DMARC
slug: litmos
tags:
- LMS
- E-Learning
- Training
- SAP
- Course Management
- User Enrollment
- Compliance
- Assessment
website: https://www.litmos.com/
---
