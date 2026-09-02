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
  band: human-only
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.0
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: RESTful API v5 for managing surveys, responses, contacts, campaigns, and account resources within the Alchemer enterprise survey platform.
  name: Alchemer REST API
  slug: alchemer-rest-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/alchemer-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.alchemer.com
- group: docs
  title: ''
  type: Documentation
  url: https://apihelp.alchemer.com/help
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.alchemer.com/help
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/apptentive
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/alchemer
- group: company
  title: ''
  type: Blog
  url: https://www.alchemer.com/resources/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.alchemer.com/plans-pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://alchemer.statuspage.io/
- group: other
  title: ''
  type: X
  url: https://twitter.com/AlchemerHQ
- group: commercial
  title: ''
  type: Plans
  url: plans/alchemer-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/alchemer-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/alchemer-finops.yml
created: '2026-06-13'
description: Enterprise survey and experience management platform with a REST API for managing surveys, accessing response data, managing contacts, and automating survey workflows. The Alchemer REST API v5 supports multi-region deployments across US, EU, Canada, and Australia, with API key and OAuth 1.0 authentication. API access is available exclusively on Business Platform accounts.
finops:
- name: Alchemer Finops
  service_category: ''
  slug: alchemer-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/alchemer.png
layout: provider
modified: '2026-06-13'
name: Alchemer
nav: Providers
network: true
overview: 'Alchemer publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Survey, Experience Management, Feedback, Data Collection, and Enterprise.


  Alchemer''s developer surface includes documentation, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Alchemer Plans Pricing
  plan_count: 4
  slug: alchemer-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 6
  name: Alchemer Rate Limits
  slug: alchemer-rate-limits
score:
  band: thin
  composite: 30.3
  coverage:
    artifact_dirs: 7
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 33.3
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 30.3
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/alchemer/refs/heads/main/screenshots/alchemer-2026-06-20T171513.png
security:
- kind: domain-security
  name: Alchemer Domain Security
  slug: alchemer-domain-security
  summary_line: TLSv1.3 · DMARC
slug: alchemer
tags:
- Survey
- Experience Management
- Feedback
- Data Collection
- Enterprise
- Forms
website: https://www.alchemer.com
---
