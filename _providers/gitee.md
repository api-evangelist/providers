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
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Gitee Agentic Access
  operation_count: 41
  slug: gitee-agentic-access
  summary_line: 41 operations · 14 acting
api_count: 9
apis:
- description: Gitee Enterprise Edition - enterprises, members, weekly reports.
  name: Gitee Enterprises API
  slug: gitee-enterprises-api
- description: Code snippets (gists) and their comments.
  name: Gitee Gists API
  slug: gitee-gists-api
- description: Issue tracking - issues, comments, labels, milestones.
  name: Gitee Issues API
  slug: gitee-issues-api
- description: Organizations and their members.
  name: Gitee Organizations API
  slug: gitee-organizations-api
- description: Pull requests - create, review, merge, and inspect changes.
  name: Gitee Pull Requests API
  slug: gitee-pull-requests-api
- description: Repositories and their contents - branches, tags, commits, contents, forks.
  name: Gitee Repositories API
  slug: gitee-repositories-api
- description: Search across repositories, issues, and users.
  name: Gitee Search API
  slug: gitee-search-api
- description: The authenticated user, keys, followers, and following.
  name: Gitee Users API
  slug: gitee-users-api
- description: Repository WebHooks (outbound HTTP event callbacks).
  name: Gitee Webhooks API
  slug: gitee-webhooks-api
artifact_total: 16
collections:
- collection_type: open
  name: Gitee Open API v5 (core subset)
  slug: open-gitee
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/gitee-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gitee-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/gitee-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://gitee.com
- group: docs
  title: ''
  type: Documentation
  url: https://gitee.com/api/v5/swagger
- group: start
  title: ''
  type: SignUp
  url: https://gitee.com/signup
- group: auth
  title: ''
  type: OAuth
  url: https://gitee.com/api/v5/oauth_doc
- group: commercial
  title: ''
  type: Plans
  url: plans/gitee-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/gitee-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/gitee-finops.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/gitee
created: '2026-07-12'
description: Gitee (码云) is a major China-based Git hosting and DevOps platform operated by OSChina / Shenzhen Oschina (开源中国). It provides code hosting, pull requests, issue tracking, gists, organizations, and enterprise DevOps workflows for millions of developers and repositories. Gitee exposes a documented REST API v5 at https://gitee.com/api/v5 (live Swagger at https://gitee.com/api/v5/swagger) covering repositories, issues, pull requests, users, organizations, gists, enterprises, webhooks, and search. Requests authenticate with a personal access token (access_token query parameter or Authorization header) or via OAuth2. Gitee offers a free personal tier plus paid Enterprise editions.
finops:
- name: Gitee Finops
  service_category: Developer Tools and DevOps
  slug: gitee-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gitee.png
layout: provider
modified: '2026-07-12'
name: Gitee
nav: Providers
network: true
overview: 'Gitee publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Enterprises API, Gists API, Issues API, and 6 more. Tagged areas include Code Hosting, Git, Git Hosting, Version Control, and Repositories.


  Gitee''s developer surface includes authentication, documentation, signup flow, and 8 more developer resources.'
plans:
- name: Gitee Plans Pricing
  plan_count: 4
  slug: gitee-plans-pricing
random_paper: 51
rate_limits:
- limit_count: 2
  name: Gitee Rate Limits
  slug: gitee-rate-limits
score:
  band: thin
  composite: 38.6
  delta: 0.0
  facets:
    commercial_clarity: 52.6
    contract_quality: 55.9
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 38.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gitee/refs/heads/main/screenshots/gitee-2026-07-25T215849.png
security:
- kind: authentication
  name: Gitee Authentication
  slug: gitee-authentication
  summary_line: apiKey/http/oauth2 · 3 schemes
- kind: domain-security
  name: Gitee Domain Security
  slug: gitee-domain-security
  summary_line: TLSv1.3 · DMARC
slug: gitee
tags:
- Code Hosting
- Git
- Git Hosting
- Version Control
- Repositories
- Pull Requests
- Issue Tracking
- DevOps
- Open Source
- China
website: https://gitee.com
---
