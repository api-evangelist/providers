---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 20
  human_in_the_loop: 0
  name: Cvat Agentic Access
  operation_count: 36
  slug: cvat-agentic-access
  summary_line: 36 operations · 20 acting
api_count: 1
apis:
- baseURL: https://app.cvat.ai/api
  baseurl_source: declared
  description: External object-storage connections used as data sources.
  name: CVAT Cloudstorages API
  slug: cvat-cloudstorages-api
- baseURL: https://app.cvat.ai/api
  baseurl_source: declared
  description: Assignable annotation units that subdivide a task.
  name: CVAT Jobs API
  slug: cvat-jobs-api
- baseURL: https://app.cvat.ai/api
  baseurl_source: declared
  description: Label taxonomy shared across projects, tasks, and jobs.
  name: CVAT Labels API
  slug: cvat-labels-api
- baseURL: https://app.cvat.ai/api
  baseurl_source: declared
  description: Membership of users within organizations.
  name: CVAT Memberships API
  slug: cvat-memberships-api
- baseURL: https://app.cvat.ai/api
  baseurl_source: declared
  description: Organizations scoping resources for teams.
  name: CVAT Organizations API
  slug: cvat-organizations-api
- baseURL: https://app.cvat.ai/api
  baseurl_source: declared
  description: Annotation projects that group tasks and share a label set.
  name: CVAT Projects API
  slug: cvat-projects-api
- baseURL: https://app.cvat.ai/api
  baseurl_source: declared
  description: Annotation tasks holding media data and annotations.
  name: CVAT Tasks API
  slug: cvat-tasks-api
- baseURL: https://app.cvat.ai/api
  baseurl_source: declared
  description: The analytics API from CVAT — 1 operation(s) for analytics.
  name: CVAT Analytics API
  slug: cvat-analytics-api
- baseURL: https://app.cvat.ai/api
  baseurl_source: declared
  description: The assets API from CVAT — 2 operation(s) for assets.
  name: CVAT Assets API
  slug: cvat-assets-api
- baseURL: https://app.cvat.ai/api
  baseurl_source: declared
  description: The auth API from CVAT — 19 operation(s) for auth.
  name: CVAT Auth API
  slug: cvat-auth-api
- baseURL: https://app.cvat.ai/api
  baseurl_source: declared
  description: The comments API from CVAT — 2 operation(s) for comments.
  name: CVAT Comments API
  slug: cvat-comments-api
- baseURL: https://app.cvat.ai/api
  baseurl_source: declared
  description: The consensus API from CVAT — 3 operation(s) for consensus.
  name: CVAT Consensus API
  slug: cvat-consensus-api
- baseURL: https://app.cvat.ai/api
  baseurl_source: declared
  description: The events API from CVAT — 2 operation(s) for events.
  name: CVAT Events API
  slug: cvat-events-api
- baseURL: https://app.cvat.ai/api
  baseurl_source: declared
  description: The functions API from CVAT — 12 operation(s) for functions.
  name: CVAT Functions API
  slug: cvat-functions-api
- baseURL: https://app.cvat.ai/api
  baseurl_source: declared
  description: The growth API from CVAT — 2 operation(s) for growth.
  name: CVAT Growth API
  slug: cvat-growth-api
- baseURL: https://app.cvat.ai/api
  baseurl_source: declared
  description: The guides API from CVAT — 2 operation(s) for guides.
  name: CVAT Guides API
  slug: cvat-guides-api
- baseURL: https://app.cvat.ai/api
  baseurl_source: declared
  description: The invitations API from CVAT — 5 operation(s) for invitations.
  name: CVAT Invitations API
  slug: cvat-invitations-api
- baseURL: https://app.cvat.ai/api
  baseurl_source: declared
  description: The issues API from CVAT — 2 operation(s) for issues.
  name: CVAT Issues API
  slug: cvat-issues-api
- baseURL: https://app.cvat.ai/api
  baseurl_source: declared
  description: The lambda API from CVAT — 4 operation(s) for lambda.
  name: CVAT Lambda API
  slug: cvat-lambda-api
- baseURL: https://app.cvat.ai/api
  baseurl_source: declared
  description: The limits API from CVAT — 4 operation(s) for limits.
  name: CVAT Limits API
  slug: cvat-limits-api
- baseURL: https://app.cvat.ai/api
  baseurl_source: declared
  description: The quality API from CVAT — 13 operation(s) for quality.
  name: CVAT Quality API
  slug: cvat-quality-api
- baseURL: https://app.cvat.ai/api
  baseurl_source: declared
  description: The requests API from CVAT — 3 operation(s) for requests.
  name: CVAT Requests API
  slug: cvat-requests-api
- baseURL: https://app.cvat.ai/api
  baseurl_source: declared
  description: The schema API from CVAT — 1 operation(s) for schema.
  name: CVAT Schema API
  slug: cvat-schema-api
- baseURL: https://app.cvat.ai/api
  baseurl_source: declared
  description: The server API from CVAT — 4 operation(s) for server.
  name: CVAT Server API
  slug: cvat-server-api
- baseURL: https://app.cvat.ai/api
  baseurl_source: declared
  description: The subscriptions API from CVAT — 1 operation(s) for subscriptions.
  name: CVAT Subscriptions API
  slug: cvat-subscriptions-api
- baseURL: https://app.cvat.ai/api
  baseurl_source: declared
  description: The usage API from CVAT — 1 operation(s) for usage.
  name: CVAT Usage API
  slug: cvat-usage-api
- baseURL: https://app.cvat.ai/api
  baseurl_source: declared
  description: The users API from CVAT — 3 operation(s) for users.
  name: CVAT Users API
  slug: cvat-users-api
- baseURL: https://app.cvat.ai/api
  baseurl_source: declared
  description: The webhooks API from CVAT — 7 operation(s) for webhooks.
  name: CVAT Webhooks API
  slug: cvat-webhooks-api
artifact_total: 44
collections:
- collection_type: open
  name: CVAT REST annotations API
  slug: open-cvat-annotations-api
- collection_type: open
  name: CVAT REST annotations cloudstorages API
  slug: open-cvat-cloudstorages-api
- collection_type: open
  name: CVAT REST annotations jobs API
  slug: open-cvat-jobs-api
- collection_type: open
  name: CVAT REST annotations labels API
  slug: open-cvat-labels-api
- collection_type: open
  name: CVAT REST annotations memberships API
  slug: open-cvat-memberships-api
- collection_type: open
  name: CVAT REST annotations organizations API
  slug: open-cvat-organizations-api
- collection_type: open
  name: CVAT REST annotations projects API
  slug: open-cvat-projects-api
- collection_type: open
  name: CVAT REST annotations tasks API
  slug: open-cvat-tasks-api
- collection_type: open
  name: CVAT REST API
  slug: open-cvat
common:
- group: agent
  href: https://artifacts.apis.io/cvat/agentic-access/cvat-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/cvat-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/cvat/security/cvat-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cvat-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/cvat/authentication/cvat-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cvat-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cvat-ai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cvat-ai
- group: company
  title: ''
  type: Website
  url: https://www.cvat.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cvat.ai
- group: commercial
  href: https://artifacts.apis.io/cvat/plans/cvat-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cvat-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/cvat/rate-limits/cvat-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/cvat-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/cvat/finops/cvat-finops.yml
  title: ''
  type: FinOps
  url: finops/cvat-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.cvat.ai/resources/blog
created: '2026-06-21'
description: CVAT (Computer Vision Annotation Tool) is an open-source platform for annotating images, video, and 3D point clouds for vision AI. The CVAT REST API exposes projects, tasks, jobs, annotations, labels, organizations, memberships, and cloud storage integrations, available both self-hosted (MIT-licensed) and as the hosted CVAT Online service at app.cvat.ai.
finops:
- has_sources: true
  method: generated
  name: Cvat Finops
  primary_unit: ''
  service_category: Machine Learning and Data Annotation
  slug: cvat-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cvat.png
layout: provider
modified: '2026-06-21'
name: CVAT
nav: Providers
network: true
overview: 'CVAT publishes 28 API contracts indexed on the [APIs.io](https://apis.io/) network, including Cloudstorages API, Jobs API, Labels API, and 25 more. Tagged areas include Computer Vision, Data Annotation, Labeling, Datasets, and Open Source.


  The CVAT catalog on APIs.io includes 1 Spectral governance ruleset.


  CVAT''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Cvat Plans Pricing
  plan_count: 5
  slug: cvat-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 6
  name: Cvat Rate Limits
  slug: cvat-rate-limits
rules:
- authorship: generated
  effective_rule_count: 100
  extends:
  - spectral:oas
  name: CVAT API Rules
  rule_count: 59
  severity_counts:
    error: 47
    hint: 0
    info: 2
    warn: 10
  slug: cvat-rules
score:
  band: thin
  composite: 28.6
  coverage:
    artifact_dirs: 15
    catalog_earned: 47.5
    catalog_earned_first_party: 0.0
    catalog_gap: 67.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.9
  facets:
    access_clarity: 7.9
    contract_governance: 13.6
    contract_quality: 49.2
    developer_ergonomics: 32.1
    discoverability: 66.1
    operational_transparency: 10.5
  previous_composite: 27.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 25.0
      derived: 0
      marker_coverage: 75.7
      total: 37
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/cvat/cvat-2026-07-25T211022.png
security:
- kind: authentication
  name: Cvat Authentication
  slug: cvat-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Cvat Domain Security
  slug: cvat-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cvat
tags:
- Computer Vision
- Data Annotation
- Labeling
- Datasets
- Open Source
website: https://www.cvat.ai
---
