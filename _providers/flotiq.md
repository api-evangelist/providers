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
- description: Auto-generated RESTful and GraphQL APIs derived from user-defined content type definitions, enabling full CRUD operations on content objects with OpenAPI schema support.
  name: Flotiq API
  slug: api
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/flotiq-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://flotiq.com/
- group: docs
  title: ''
  type: Documentation
  url: https://flotiq.com/docs/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/flotiq
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/flotiq
- group: commercial
  title: ''
  type: Pricing
  url: https://flotiq.com/pricing/
- group: commercial
  title: ''
  type: Plans
  url: plans/flotiq-plans.md
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/flotiq-rate-limits.md
- group: commercial
  title: ''
  type: FinOps
  url: finops/flotiq-finops.md
- group: company
  title: ''
  type: Blog
  url: https://flotiq.com/blog/
created: 2026-06-14
description: Open-source headless CMS with auto-generated GraphQL and REST APIs from content type definitions, hosting both self-managed and cloud deployments.
graphqls:
- description: Flotiq provides a GraphQL API that is automatically generated from your content type definitions. The schema evolves dynamically as you add or modify content types in your account.
  name: Flotiq GraphQL
  slug: flotiq-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/flotiq.png
layout: provider
modified: 2026-06-14
name: Flotiq
nav: Providers
network: true
overview: 'Flotiq publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include GraphQL, Headless CMS, Content Management, REST, and API-First.


  Flotiq''s developer surface includes documentation, pricing, engineering blog, and 7 more developer resources.'
random_paper: 4
score:
  band: emerging
  composite: 21.1
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 37.2
    developer_ergonomics: 11.9
    discoverability: 66.7
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 21.1
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/flotiq/refs/heads/main/screenshots/flotiq-2026-06-20T181326.png
security:
- kind: domain-security
  name: Flotiq Domain Security
  slug: flotiq-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: flotiq
tags:
- GraphQL
- Headless CMS
- Content Management
- REST
- API-First
website: https://flotiq.com/
---
