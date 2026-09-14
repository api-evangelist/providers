---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Percy Agentic Access
  operation_count: 13
  slug: percy-agentic-access
  summary_line: 13 operations · 7 acting
api_count: 1
apis:
- baseURL: https://percy.io/api/v1
  baseurl_source: declared
  description: A build logically groups the test sessions and snapshots of a run.
  name: Percy Builds API
  slug: percy-builds-api
- baseURL: https://percy.io/api/v1
  baseurl_source: declared
  description: A project logically groups builds on Percy.
  name: Percy Projects API
  slug: percy-projects-api
- baseURL: https://percy.io/api/v1
  baseurl_source: declared
  description: Snapshots are the individual visual comparisons within a build.
  name: Percy Snapshots API
  slug: percy-snapshots-api
- baseURL: https://percy.io/api/v1
  baseurl_source: declared
  description: Branchline sync and merge of approved snapshots across branch lines.
  name: Percy Visual Git API
  slug: percy-visual-git-api
artifact_total: 15
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Percy REST Builds API
  slug: open-percy-builds-api
- collection_type: open
  name: Percy REST Builds Projects API
  slug: open-percy-projects-api
- collection_type: open
  name: Percy REST Builds Snapshots API
  slug: open-percy-snapshots-api
- collection_type: open
  name: Percy REST Builds Visual Git API
  slug: open-percy-visual-git-api
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
random_paper: 1
rate_limits:
- limit_count: 5
  name: Percy Rate Limits
  slug: percy-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/percy/refs/heads/main/screenshots/percy-2026-09-02T151040.png
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
- Developer Tools
website: https://percy.io
---
