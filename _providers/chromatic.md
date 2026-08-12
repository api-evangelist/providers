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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
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
  score: 19.4
  scored_at: '2026-08-11'
api_count: 4
apis:
- description: Query builds produced by the Chromatic CLI - the `build(id)` and `project.lastBuild(...)` GraphQL fields expose build number, status (IN_PROGRESS, PASSED, PENDING, ACCEPTED, DENIED, BROKEN, FAILED), r
  name: Chromatic Builds API
  slug: chromatic-builds-api
- description: Inspect and act on individual visual tests. A Test carries its status, result, baseline, and per-browser snapshot comparisons (TestComparison with base/head captures and pixel diffs). The `reviewTest`
  name: Chromatic Tests and Review API
  slug: chromatic-tests-review-api
- description: Resolve project and account context. The `project(id)` field returns the project name, enabled features (uiReview, uiTests), branch names, project token, and manage/web URLs; `account(id)` and `viewer
  name: Chromatic Projects and Accounts API
  slug: chromatic-projects-accounts-api
- description: Read the published Storybook and its structure. The `storybook(url)` query and the Story and Component node types expose the components and stories captured in a build, their CSF story IDs, test param
  name: Chromatic Storybook and Stories API
  slug: chromatic-storybook-stories-api
artifact_total: 9
collections:
- collection_type: open
  name: Chromatic Public GraphQL API
  slug: open-chromatic
common:
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/chromaui
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/chromaticcom
- group: company
  title: ''
  type: Website
  url: https://www.chromatic.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.chromatic.com/docs/
- group: commercial
  title: ''
  type: Plans
  url: plans/chromatic-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/chromatic-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/chromatic-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.chromatic.com/blog/
created: '2026-07-11'
description: Chromatic is a cloud visual testing and UI review platform built by the maintainers of Storybook. It captures snapshots of components and pages across cloud browsers, then compares each new snapshot to a stored baseline to catch visual regressions in appearance, layout, fonts, and color. Chromatic runs visual tests, interaction tests, and accessibility (axe) tests against Storybook, Playwright, and Cypress, with UI Review, TurboSnap change detection, and Git/CI integration. Its primary developer surface is the Chromatic CLI, which uploads builds and drives testing over a documented public GraphQL API at index.chromatic.com used by the CLI and the Storybook Visual Tests addon.
finops:
- name: Chromatic Finops
  service_category: Developer Tools and Testing
  slug: chromatic-finops
graphqls:
- description: Chromatic is a cloud visual testing and UI review platform built by the maintainers
  name: Chromatic GraphQL API
  slug: chromatic-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/chromatic.png
layout: provider
modified: '2026-07-11'
name: Chromatic
nav: Providers
network: true
overview: 'Chromatic publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Builds API, Tests and Review API, Projects and Accounts API, and 1 more. Tagged areas include Visual Testing, Visual Regression, Storybook, UI Testing, and Snapshot Testing.


  Chromatic''s developer surface includes documentation, engineering blog, and 6 more developer resources.'
plans:
- name: Chromatic Plans Pricing
  plan_count: 4
  slug: chromatic-plans-pricing
random_paper: 26
rate_limits:
- limit_count: 3
  name: Chromatic Rate Limits
  slug: chromatic-rate-limits
score:
  band: thin
  composite: 34.3
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 48.1
    developer_ergonomics: 10.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 34.3
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/chromatic/refs/heads/main/screenshots/chromatic-2026-07-25T205300.png
slug: chromatic
tags:
- Visual Testing
- Visual Regression
- Storybook
- UI Testing
- Snapshot Testing
- Frontend
- GraphQL
website: https://www.chromatic.com
---
