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
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Gitee Agentic Access
  operation_count: 41
  slug: gitee-agentic-access
  summary_line: 41 operations · 14 acting
api_count: 1
apis:
- baseURL: https://gitee.com/api/v5
  baseurl_source: declared
  description: Gitee Enterprise Edition - enterprises, members, weekly reports.
  name: Gitee Enterprises API
  slug: gitee-enterprises-api
- baseURL: https://gitee.com/api/v5
  baseurl_source: declared
  description: Code snippets (gists) and their comments.
  name: Gitee Gists API
  slug: gitee-gists-api
- baseURL: https://gitee.com/api/v5
  baseurl_source: declared
  description: Issue tracking - issues, comments, labels, milestones.
  name: Gitee Issues API
  slug: gitee-issues-api
- baseURL: https://gitee.com/api/v5
  baseurl_source: declared
  description: Organizations and their members.
  name: Gitee Organizations API
  slug: gitee-organizations-api
- baseURL: https://gitee.com/api/v5
  baseurl_source: declared
  description: Pull requests - create, review, merge, and inspect changes.
  name: Gitee Pull Requests API
  slug: gitee-pull-requests-api
- baseURL: https://gitee.com/api/v5
  baseurl_source: declared
  description: Repositories and their contents - branches, tags, commits, contents, forks.
  name: Gitee Repositories API
  slug: gitee-repositories-api
- baseURL: https://gitee.com/api/v5
  baseurl_source: declared
  description: Search across repositories, issues, and users.
  name: Gitee Search API
  slug: gitee-search-api
- baseURL: https://gitee.com/api/v5
  baseurl_source: declared
  description: The authenticated user, keys, followers, and following.
  name: Gitee Users API
  slug: gitee-users-api
- baseURL: https://gitee.com/api/v5
  baseurl_source: declared
  description: Repository WebHooks (outbound HTTP event callbacks).
  name: Gitee Webhooks API
  slug: gitee-webhooks-api
artifact_total: 27
collections:
- collection_type: open
  name: Gitee Open API v5 (core subset) Enterprises API
  slug: open-gitee-enterprises-api
- collection_type: open
  name: Gitee Open API v5 (core subset) Enterprises Gists API
  slug: open-gitee-gists-api
- collection_type: open
  name: Gitee Open API v5 (core subset) Enterprises Issues API
  slug: open-gitee-issues-api
- collection_type: open
  name: Gitee Open API v5 (core subset) Enterprises Organizations API
  slug: open-gitee-organizations-api
- collection_type: open
  name: Gitee Open API v5 (core subset) Enterprises Pull Requests API
  slug: open-gitee-pull-requests-api
- collection_type: open
  name: Gitee Open API v5 (core subset) Enterprises Repositories API
  slug: open-gitee-repositories-api
- collection_type: open
  name: Gitee Open API v5 (core subset) Enterprises Search API
  slug: open-gitee-search-api
- collection_type: open
  name: Gitee Open API v5 (core subset) Enterprises Users API
  slug: open-gitee-users-api
- collection_type: open
  name: Gitee Open API v5 (core subset) Enterprises Webhooks API
  slug: open-gitee-webhooks-api
- collection_type: open
  name: Gitee Open API v5 (core subset)
  slug: open-gitee
common:
- group: company
  title: ''
  type: Blog
  url: https://gitee.com/blog/
- group: other
  href: https://artifacts.apis.io/gitee/capabilities/gitee-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/gitee-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/gitee/agentic-access/gitee-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/gitee-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/gitee/security/gitee-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/gitee-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/gitee/authentication/gitee-authentication.yml
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
  href: https://artifacts.apis.io/gitee/plans/gitee-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/gitee-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/gitee/rate-limits/gitee-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/gitee-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/gitee/finops/gitee-finops.yml
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
- has_sources: true
  method: generated
  name: Gitee Finops
  primary_unit: ''
  service_category: Developer Tools and DevOps
  slug: gitee-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gitee.png
layout: provider
mcp_servers:
- description: Remote MCP server at api.gitee.com over HTTP; 25 tools listed.
  name: Gitee MCP Server
  slug: gitee
modified: '2026-10-06'
name: Gitee
nav: Providers
network: true
overview: 'Gitee publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Enterprises API, Gists API, Issues API, and 6 more. Tagged areas include Code Hosting, Version Control, Git Hosting, Repositories, and Pull Requests.


  The Gitee catalog on APIs.io includes 1 Spectral governance ruleset.


  Gitee''s developer surface includes engineering blog, authentication, documentation, signup flow, and 9 more developer resources.'
plans:
- name: Gitee Plans Pricing
  plan_count: 4
  slug: gitee-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 2
  name: Gitee Rate Limits
  slug: gitee-rate-limits
rules:
- authorship: generated
  effective_rule_count: 106
  extends:
  - spectral:oas
  name: Gitee API Rules
  rule_count: 65
  severity_counts:
    error: 58
    hint: 0
    info: 2
    warn: 5
  slug: gitee-rules
score:
  band: thin
  composite: 28.4
  coverage:
    artifact_dirs: 17
    catalog_earned: 46.5
    catalog_earned_first_party: 0.0
    catalog_gap: 68.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 14.5
    contract_governance: 13.6
    contract_quality: 44.4
    developer_ergonomics: 32.1
    discoverability: 68.3
    operational_transparency: 5.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - china
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - greater-china
  previous_composite: 28.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/gitee/gitee-2026-07-25T215849.png
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
- Version Control
- Git Hosting
- Repositories
- Pull Requests
- Issue Tracking
- DevOps
- Open Source
- China
website: https://gitee.com
---
