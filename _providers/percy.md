---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
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
  score: 30.6
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Percy Agentic Access
  operation_count: 13
  slug: percy-agentic-access
  summary_line: 13 operations · 7 acting
api_count: 4
apis:
- description: A build logically groups the test sessions and snapshots of a run.
  name: Percy Builds API
  slug: percy-builds-api
- description: A project logically groups builds on Percy.
  name: Percy Projects API
  slug: percy-projects-api
- description: Snapshots are the individual visual comparisons within a build.
  name: Percy Snapshots API
  slug: percy-snapshots-api
- description: Branchline sync and merge of approved snapshots across branch lines.
  name: Percy Visual Git API
  slug: percy-visual-git-api
artifact_total: 10
collections:
- collection_type: open
  name: Percy REST API
  slug: open-percy
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/percy-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/percy-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/percy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/browserstack
- group: company
  title: ''
  type: Website
  url: https://percy.io
- group: docs
  title: ''
  type: Documentation
  url: https://www.browserstack.com/docs/percy
- group: commercial
  title: ''
  type: Plans
  url: plans/percy-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/percy-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/percy-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://percy.io/blog
created: '2026-07-11'
description: Percy is an all-in-one visual testing and review platform, now part of BrowserStack. Test frameworks and CI upload DOM snapshots via the Percy CLI/SDK; Percy renders them across browsers and widths, diffs each against an approved baseline, and surfaces pixel-level visual changes for review and approval. On top of that workflow Percy exposes a documented REST API under https://percy.io/api/v1 for reading and managing Projects, Builds, and Snapshots, plus Visual Git (branchline) sync and merge operations. The snapshot capture/upload path itself is driven by the open-source Percy CLI and SDKs rather than a public REST upload endpoint.
finops:
- name: Percy Finops
  service_category: Software Testing and Quality
  slug: percy-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/percy.png
layout: provider
modified: '2026-07-11'
name: Percy
nav: Providers
network: true
overview: 'Percy publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Builds API, Projects API, Snapshots API, and 1 more. Tagged areas include Visual Testing, Visual Regression, Screenshots, QA, and Testing.


  Percy''s developer surface includes authentication, documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Percy Plans Pricing
  plan_count: 3
  slug: percy-plans-pricing
random_paper: 83
rate_limits:
- limit_count: 5
  name: Percy Rate Limits
  slug: percy-rate-limits
score:
  band: thin
  composite: 39.7
  delta: -0.6
  facets:
    commercial_clarity: 39.5
    contract_quality: 61.2
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 40.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
security:
- kind: authentication
  name: Percy Authentication
  slug: percy-authentication
  summary_line: apiKey/http · 2 schemes
slug: percy
tags:
- Visual Testing
- Visual Regression
- Screenshots
- QA
- Testing
- CI/CD
- BrowserStack
website: https://percy.io
---
