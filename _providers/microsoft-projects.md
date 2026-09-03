---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-03'
api_count: 3
apis:
- description: REST API for managing projects, tasks, resources, and assignments in Microsoft Project for the web.
  name: Microsoft Project for the Web API
  slug: microsoft-project-for-the-web-api
- description: REST API for Microsoft Project Online, providing access to project data, timesheets, and enterprise project management features.
  name: Microsoft Project Online API
  slug: microsoft-project-online-api
- description: Client-side object model for programmatically interacting with Microsoft Project desktop applications.
  name: Microsoft Project Desktop CSOM API
  slug: microsoft-project-desktop-csom-api
artifact_total: 6
common:
- group: start
  title: ''
  type: X-portal
  url: https://developer.microsoft.com/
- group: commercial
  title: ''
  type: X-pricing
  url: https://www.microsoft.com/en-us/microsoft-365/project/compare-microsoft-project-management-software
- group: operate
  title: ''
  type: X-status
  url: https://status.cloud.microsoft/
- group: company
  title: ''
  type: X-blog
  url: https://techcommunity.microsoft.com/t5/project-blog/bg-p/ProjectBlog
- group: commercial
  title: ''
  type: X-terms-of-service
  url: https://www.microsoft.com/en-us/legal/terms-of-use
- group: commercial
  title: ''
  type: X-privacy-policy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: company
  title: ''
  type: Blog
  url: https://techcommunity.microsoft.com/t5/s/gxcuf89792/rss/board?board.id=ProjectBlog
created: '2024-01-15'
description: A collection of APIs for Microsoft Project, enabling project management, task tracking, resource allocation, and collaboration capabilities.
finops:
- name: Microsoft Projects Finops
  service_category: API
  slug: microsoft-projects-finops
image: https://www.microsoft.com/en-us/microsoft-365/project/project-management-software
layout: provider
modified: '2026-04-28'
name: Microsoft Project APIs
nav: Providers
network: true
overview: 'Microsoft Project APIs publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Collaboration, Enterprise, Microsoft, Portfolio-Management, and Project Management.


  Microsoft Project APIs'' developer surface includes engineering blog and 6 more developer resources.'
plans:
- name: Microsoft Projects Plans Pricing
  plan_count: 3
  slug: microsoft-projects-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 5
  name: Microsoft Projects Rate Limits
  slug: microsoft-projects-rate-limits
score:
  band: minimal
  composite: 9.3
  coverage:
    artifact_dirs: 5
    catalog_gap: 81.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 46.3
    governance: 0.0
    operational_transparency: 7.9
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 9.3
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-projects/refs/heads/main/screenshots/microsoft-projects-2026-06-20T185528.png
slug: microsoft-projects
tags:
- Collaboration
- Enterprise
- Microsoft
- Portfolio-Management
- Project Management
- Resources
- Task
---
