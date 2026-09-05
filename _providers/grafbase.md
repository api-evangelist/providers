---
access_model:
  confidence: medium
  label: Freemium (free trial)
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: true
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
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
  score: 18.0
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: GraphQL-based management API that powers the Grafbase Dashboard and enables programmatic control of organizations, projects, schemas, branches, and deployed graph endpoints. Accessible at api.grafbase
  name: Grafbase Management API
  slug: grafbase-management-api
artifact_total: 8
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/grafbase-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/grafbase-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://grafbase.com
- group: docs
  title: ''
  type: Documentation
  url: https://grafbase.com/docs
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/grafbase
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/grafbase
- group: company
  title: ''
  type: Blog
  url: https://grafbase.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://grafbase.com/pricing
- group: operate
  title: ''
  type: ChangeLog
  url: https://grafbase.com/changelog
- group: build
  title: ''
  type: CLI
  url: https://grafbase.com/cli
- group: other
  title: ''
  type: X
  url: https://x.com/grafbase
- group: commercial
  title: ''
  type: Plans
  url: plans/grafbase-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/grafbase-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/grafbase-finops.yml
created: '2026-06-13'
description: Grafbase is an enterprise GraphQL federation platform for building and deploying federated GraphQL APIs. It provides a high-performance Rust-powered gateway, schema registry, CLI, and a management API for programmatically controlling projects, schemas, branches, and deployed graph endpoints. The platform delivers enterprise-grade governance, observability, rate limiting, authentication, and AI agent integration via Model Context Protocol support.
finops:
- name: Grafbase Finops
  service_category: ''
  slug: grafbase-finops
graphqls:
- description: Grafbase provides a GraphQL-based Management API that powers the Grafbase Dashboard and enables programmatic control of all platform resources. The API exposes queries and mutations covering organizat
  name: Grafbase GraphQL API
  slug: grafbase-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/grafbase.png
jsonld:
- class_count: 35
  name: Grafbase Context
  property_count: 9
  slug: grafbase-context
layout: provider
modified: '2026-06-13'
name: Grafbase
nav: Providers
network: true
overview: 'Grafbase publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include GraphQL, Federation, API Gateway, Schema Registry, and GraphQL Federation.


  The Grafbase catalog on APIs.io includes 1 JSON-LD context.


  Grafbase''s developer surface includes documentation, engineering blog, pricing, changelog, CLI, and 9 more developer resources.'
plans:
- name: Grafbase Plans Pricing
  plan_count: 3
  slug: grafbase-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Grafbase Rate Limits
  slug: grafbase-rate-limits
score:
  band: thin
  composite: 37.2
  coverage:
    artifact_dirs: 9
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
    contract_quality: 45.7
    developer_ergonomics: 31.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 37.2
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/grafbase/refs/heads/main/screenshots/grafbase-2026-06-20T182315.png
security:
- kind: domain-security
  name: Grafbase Domain Security
  slug: grafbase-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Grafbase Vulnerability Disclosure
  slug: grafbase-vulnerability-disclosure
  summary_line: disclosure policy published
slug: grafbase
tags:
- GraphQL
- Federation
- API Gateway
- Schema Registry
- GraphQL Federation
- API Management
- Observability
- Enterprise API
website: https://grafbase.com
---
