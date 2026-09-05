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
- description: The Domestika REST API at api.domestika.org is the internal backbone of the Domestika platform, providing access to course catalog listings, learner enrollment records, user profiles, community conten
  name: Domestika API
  slug: domestika-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/domestika-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.domestika.org
- group: docs
  title: ''
  type: Documentation
  url: https://www.domestika.org/en/organizations
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/domestika
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/domestika
- group: company
  title: ''
  type: Blog
  url: https://www.domestika.org/en/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.domestika.org/en/organizations
- group: other
  title: ''
  type: X
  url: https://x.com/Domestika
- group: commercial
  title: ''
  type: Plans
  url: plans/domestika-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/domestika-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/domestika-finops.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/domestika-context.jsonld
created: 2026-06-13
description: Domestika is an online creative education platform that connects over 8 million creative professionals and learners with high-quality courses across illustration, design, photography, marketing, and more. The platform provides a REST API at api.domestika.org that powers its web and mobile applications, exposing course catalog data, user enrollment information, and community features. Domestika for Business extends the platform to organizations, enabling teams to purchase seat licenses and track learner progress through a management dashboard. Creative professionals and businesses can leverage Domestika's catalog and learner data to integrate creative skills development into their workflows and tooling.
finops:
- name: Domestika Finops
  service_category: ''
  slug: domestika-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/domestika.png
jsonld:
- class_count: 10
  name: Domestika Context
  property_count: 1
  slug: domestika-context
layout: provider
modified: 2026-06-13
name: Domestika
nav: Providers
network: true
overview: 'Domestika publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Creative Education, Online Learning, Courses, Design, and Photography.


  The Domestika catalog on APIs.io includes 1 JSON-LD context.


  Domestika''s developer surface includes documentation, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Domestika Plans Pricing
  plan_count: 6
  slug: domestika-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Domestika Rate Limits
  slug: domestika-rate-limits
score:
  band: thin
  composite: 28.2
  coverage:
    artifact_dirs: 7
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
    contract_quality: 37.3
    developer_ergonomics: 11.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 28.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 20.4
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/domestika/refs/heads/main/screenshots/domestika-2026-06-20T180145.png
security:
- kind: domain-security
  name: Domestika Domain Security
  slug: domestika-domain-security
  summary_line: TLSv1.3 · DMARC
slug: domestika
tags:
- Creative Education
- Online Learning
- Courses
- Design
- Photography
- Illustration
- Enterprise Learning
- REST API
website: https://www.domestika.org
---
