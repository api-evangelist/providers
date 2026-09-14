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
  - security
  trial: false
  try_now: true
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Travis Ci Agentic Access
  operation_count: 24
  slug: travis-ci-agentic-access
  summary_line: 24 operations · 12 acting
api_count: 1
apis:
- description: Current REST API used by the Travis CI web UI. 50+ resource types covering builds, jobs, repositories, users, organizations, crons, caches, environment variables, requests and config validation. Hyper
  name: Travis CI REST API v3
  slug: v3
- description: Legacy v2/v2.1 REST API; superseded by v3 but still in use. Builds, jobs, branches, logs, env vars, caches, SSH keys, requests. Authenticated via Bearer access tokens exchanged with GitHub.
  name: Travis CI REST API v2.1 (deprecated)
  slug: v2
- baseURL: https://api.travis-ci.com
  baseurl_source: declared
  description: The Builds API from Travis CI — 3 operation(s) for builds.
  name: Travis CI Builds API
  slug: travis-ci-builds-api
- baseURL: https://api.travis-ci.com
  baseurl_source: declared
  description: The Jobs API from Travis CI — 4 operation(s) for jobs.
  name: Travis CI Jobs API
  slug: travis-ci-jobs-api
- baseURL: https://api.travis-ci.com
  baseurl_source: declared
  description: The Logs API from Travis CI — 1 operation(s) for logs.
  name: Travis CI Logs API
  slug: travis-ci-logs-api
- baseURL: https://api.travis-ci.com
  baseurl_source: declared
  description: The Organizations API from Travis CI — 4 operation(s) for organizations.
  name: Travis CI Organizations API
  slug: travis-ci-organizations-api
- baseURL: https://api.travis-ci.com
  baseurl_source: declared
  description: The Repositories API from Travis CI — 6 operation(s) for repositories.
  name: Travis CI Repositories API
  slug: travis-ci-repositories-api
- baseURL: https://api.travis-ci.com
  baseurl_source: declared
  description: The Users API from Travis CI — 4 operation(s) for users.
  name: Travis CI Users API
  slug: travis-ci-users-api
artifact_total: 22
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Travis CI REST API v3 Builds API
  slug: open-travis-ci-builds-api
- collection_type: open
  name: Travis CI REST API v3 Builds Jobs API
  slug: open-travis-ci-jobs-api
- collection_type: open
  name: Travis CI REST API v3 Builds Logs API
  slug: open-travis-ci-logs-api
- collection_type: open
  name: Travis CI REST API v3 Builds Organizations API
  slug: open-travis-ci-organizations-api
- collection_type: open
  name: Travis CI REST API v3 Builds Repositories API
  slug: open-travis-ci-repositories-api
- collection_type: open
  name: Travis CI REST API v3 Builds Users API
  slug: open-travis-ci-users-api
- collection_type: open
  name: Travis CI REST API v3
  slug: open-travis-ci
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/travis-ci-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/travis-ci-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/travis-ci-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/travis-ci
- group: company
  title: ''
  type: Website
  url: https://www.travis-ci.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.travis-ci.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.travis-ci.com/pricing/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/travis-ci
- group: operate
  title: ''
  type: StatusPage
  url: https://www.traviscistatus.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/travis-ci-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/travis-ci-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/travis-ci-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.travis-ci.com/feed/
created: '2026-05-08'
description: 'Travis CI is a hosted continuous integration service supporting GitHub, GitLab and Bitbucket. Two REST APIs are available: the legacy v2/v2.1 API (deprecated) and the current v3 API used by the web UI. Travis CI is also available as Enterprise (on-premises) and Server (private cloud).'
finops:
- name: Travis Ci Finops
  service_category: DevOps / CI/CD
  slug: travis-ci-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/travis-ci.png
layout: provider
modified: '2026-05-08'
name: Travis CI
nav: Providers
network: true
overview: 'Travis CI publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Builds API, Jobs API, Logs API, and 3 more. Tagged areas include DevOps, CI/CD, Builds, Open-Source, and Hosted.


  Travis CI''s developer surface includes authentication, documentation, pricing, GitHub presence, engineering blog, and 8 more developer resources.'
plans:
- name: Travis Ci Plans Pricing
  plan_count: 6
  slug: travis-ci-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 4
  name: Travis Ci Rate Limits
  slug: travis-ci-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/travis-ci/refs/heads/main/screenshots/travis-ci-2026-06-20T195637.png
security:
- kind: authentication
  name: Travis Ci Authentication
  slug: travis-ci-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Travis Ci Domain Security
  slug: travis-ci-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: travis-ci
tags:
- DevOps
- CI/CD
- Builds
- Open-Source
- Hosted
- GitHub
- Developer Tools
website: https://www.travis-ci.com/
---
