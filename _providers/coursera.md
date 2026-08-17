---
access_model:
  confidence: medium
  label: Paid · Requires approval
  onboarding: approval
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
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.6
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Coursera Agentic Access
  operation_count: 4
  slug: coursera-agentic-access
  summary_line: 4 operations
api_count: 3
apis:
- description: Public REST API for browsing Coursera's catalog of courses, specializations, instructors, partners, and categories. Verified live at api.coursera.org/api/courses.v1 with 21,000+ courses.
  name: Coursera Catalog API
  slug: catalog-api
- description: API for affiliate marketing partners to retrieve catalog data and tracking links.
  name: Coursera Affiliate API
  slug: affiliate-api
- description: Public catalog browsing
  name: Coursera Catalog API
  slug: coursera-catalog-api
artifact_total: 12
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Coursera Catalog API
  slug: open-coursera-catalog-api
- collection_type: open
  name: Coursera Catalog API
  slug: open-coursera
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/coursera-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/coursera-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/coursera
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/coursera
- group: company
  title: ''
  type: Website
  url: https://www.coursera.org/
- group: other
  title: ''
  type: Developer
  url: https://building.coursera.org/
- group: commercial
  title: ''
  type: Plans
  url: plans/coursera-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/coursera-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/coursera-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://blog.coursera.org/feed/
created: '2026-05-08'
description: Coursera is a global online learning platform offering courses, specializations, professional certificates, and degrees. The Catalog API provides public, read-only access to courses, instructors, partners, and categories; the Affiliate API supports partner programs.
finops:
- name: Coursera Finops
  service_category: Education & Training
  slug: coursera-finops
graphqls:
- description: 'Coursera is a global online learning platform offering courses, specializations, professional certificates, and degrees from top universities and companies. The platform serves learners, instructors, '
  name: Coursera GraphQL Schema
  slug: coursera-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/coursera.png
layout: provider
modified: '2026-05-08'
name: Coursera
nav: Providers
network: true
overview: 'Coursera publishes 1 API on the [APIs.io](https://apis.io/) network: Catalog API. Tagged areas include EdTech, Online Learning, Catalog, and MOOC.


  Coursera''s developer surface includes engineering blog and 9 more developer resources.'
plans:
- name: Coursera Plans Pricing
  plan_count: 2
  slug: coursera-plans-pricing
random_paper: 123
rate_limits:
- limit_count: 1
  name: Coursera Rate Limits
  slug: coursera-rate-limits
score:
  band: emerging
  composite: 24.1
  delta: 0.0
  facets:
    commercial_clarity: 13.2
    contract_quality: 56.2
    developer_ergonomics: 2.2
    discoverability: 55.6
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 24.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/coursera/refs/heads/main/screenshots/coursera-2026-06-20T175124.png
security:
- kind: domain-security
  name: Coursera Domain Security
  slug: coursera-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: coursera
tags:
- EdTech
- Online Learning
- Catalog
- MOOC
website: https://www.coursera.org/
---
