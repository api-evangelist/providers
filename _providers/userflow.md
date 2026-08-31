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
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: The Userflow REST API allows back-end applications to synchronize user data, track events, and manage groups or companies within the Userflow platform. It provides endpoints for creating, updating, an
  name: Userflow REST API
  slug: userflow-rest-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/userflow-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.userflow.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.userflow.com/docs/dev
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/userflow
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/userflow
- group: company
  title: ''
  type: Blog
  url: https://www.userflow.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.userflow.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.userflow.com
- group: other
  title: ''
  type: X
  url: https://twitter.com/getuserflow
- group: commercial
  title: ''
  type: Plans
  url: plans/userflow-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/userflow-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/userflow-finops.yml
created: '2026-06-13'
description: Userflow is a product onboarding and adoption platform that enables product teams to build in-app guided flows, checklists, announcements, and NPS surveys without requiring engineering resources. The platform provides a REST API for managing users, tracking events, and organizing users into groups or companies from a back-end application. Userflow supports data synchronization via API keys with Bearer token authentication, allowing real-time user attribute updates and event tracking to power personalized onboarding experiences. The platform targets SaaS companies seeking to improve activation rates, feature adoption, and overall user retention through guided in-app engagement.
finops:
- name: Userflow Finops
  service_category: ''
  slug: userflow-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/userflow.png
jsonld:
- class_count: 0
  name: Userflow Context
  property_count: 19
  slug: userflow-context
layout: provider
modified: '2026-06-13'
name: Userflow
nav: Providers
network: true
overview: 'Userflow publishes 1 API on the [APIs.io](https://apis.io/) network: REST API. Tagged areas include User Onboarding, Product Adoption, In-App Guides, Checklists, and Announcements.


  The Userflow catalog on APIs.io includes 1 JSON-LD context.


  Userflow''s developer surface includes documentation, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Userflow Plans Pricing
  plan_count: 3
  slug: userflow-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 2
  name: Userflow Rate Limits
  slug: userflow-rate-limits
score:
  band: thin
  composite: 32.0
  coverage:
    artifact_dirs: 7
    catalog_gap: 47.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 37.3
    developer_ergonomics: 11.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 32.0
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/userflow/refs/heads/main/screenshots/userflow-2026-06-20T200712.png
security:
- kind: domain-security
  name: Userflow Domain Security
  slug: userflow-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: userflow
tags:
- User Onboarding
- Product Adoption
- In-App Guides
- Checklists
- Announcements
- NPS Surveys
- User Flows
- Software-as-a-Service
- Product-Led Growth
website: https://www.userflow.com
---
