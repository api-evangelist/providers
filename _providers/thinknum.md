---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 7.9
  scored_at: '2026-09-16'
api_count: 1
apis:
- description: Token-authenticated REST API over data.thinknum.com for querying Thinknum's alternative datasets. Endpoints cover dataset query (filter/group/sort/ function), historical daily and monthly feeds, compa
  name: Thinknum Data API
  slug: thinknum-data-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://thinknum.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.thinknum.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.thinknum.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.thinknum.com/docs/query-api.md
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.thinknum.com/docs/getting-started.md
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/thinknum/refs/heads/main/authentication/thinknum-authentication.yml
  title: ''
  type: Authentication
  url: authentication/thinknum-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://blog.thinknum.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://www.thinknum.com/status
- group: operate
  title: ''
  type: Support
  url: mailto:support@thinknum.com
- group: start
  title: ''
  type: Login
  url: https://www.thinknum.com/creator/account/login/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.thinknum.com/tos
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/thinknum
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/thinknum/refs/heads/main/packages/thinknum-packages.yml
  title: ''
  type: Packages
  url: packages/thinknum-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/thinknum/refs/heads/main/packages/thinknum-packages.yml
  title: ''
  type: SDKs
  url: packages/thinknum-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/thinknum/refs/heads/main/llms/thinknum-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/thinknum-llms.txt
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/thinknum/refs/heads/main/conventions/thinknum-conventions.yml
  title: ''
  type: Conventions
  url: conventions/thinknum-conventions.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/thinknum/refs/heads/main/rate-limits/thinknum-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/thinknum-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/thinknum/refs/heads/main/errors/thinknum-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/thinknum-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/thinknum/refs/heads/main/lifecycle/thinknum-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/thinknum-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/thinknum/refs/heads/main/changelog/thinknum-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/thinknum-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/thinknum/refs/heads/main/components/thinknum-components.yml
  title: ''
  type: Components
  url: components/thinknum-components.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/thinknum/refs/heads/main/mcp/thinknum-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/thinknum-mcp.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/thinknum/refs/heads/main/data-model/thinknum-data-model.yml
  title: ''
  type: DataModel
  url: data-model/thinknum-data-model.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/thinknum/refs/heads/main/security/thinknum-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/thinknum-domain-security.yml
created: '2026-07-17'
description: Thinknum is an alternative data platform that collects and structures web-sourced datasets to power investment and business intelligence. It tracks metrics such as job listings, store locations, product pricing, web traffic, app reviews, and social engagement across hundreds of thousands of companies, keyed by exchange ticker. The Thinknum Data API (data.thinknum.com) exposes these datasets over a token-authenticated REST interface with Query, Historical, Company, and Upload endpoints, plus embeddable widgets and an official Python client. Backed by 500 Global.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/thinknum.png
layout: provider
modified: '2026-07-21'
name: Thinknum
nav: Providers
network: true
overview: 'Thinknum publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Alternative Data, Financial Data, Investment Research, and Market Intelligence.


  Thinknum''s developer surface includes documentation, API reference, getting-started guide, authentication, engineering blog, support, changelog, and 17 more developer resources.'
random_paper: 20
rate_limits:
- limit_count: 1
  name: Thinknum Rate Limits
  slug: thinknum-rate-limits
score:
  band: thin
  composite: 27.2
  coverage:
    artifact_dirs: 13
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 45.2
    discoverability: 75.9
    operational_transparency: 55.3
  previous_composite: 27.2
  provenance:
    mcp: derived
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/thinknum/refs/heads/main/screenshots/thinknum-2026-09-02T163532.png
security:
- kind: authentication
  name: Thinknum Authentication
  slug: thinknum-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Thinknum Domain Security
  slug: thinknum-domain-security
  summary_line: TLSv1.3
slug: thinknum
tags:
- Company
- Alternative Data
- Financial Data
- Investment Research
- Market Intelligence
- Web Data
- Datasets
website: https://thinknum.com
---
