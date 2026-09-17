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
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-09-16'
api_count: 1
apis:
- description: Firecamp is an open-source API development platform for designing, testing, and documenting REST, GraphQL, and WebSocket APIs. The product itself does not publish a consumer-facing HTTP API; it is a d
  name: Firecamp
  slug: firecamp
artifact_total: 5
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/firecamp-dev/firecamp/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/firecamp-dev/firecamp/releases
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/firecamp-dev/firecamp/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/firecamp-dev/firecamp/blob/main/LICENSE
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/firecamp/refs/heads/main/security/firecamp-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/firecamp-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/firecampdev
- group: company
  title: ''
  type: Website
  url: https://firecamp.io
- group: docs
  title: ''
  type: Documentation
  url: https://firecamp.io/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://firecamp.io/pricing
- group: company
  title: ''
  type: Blog
  url: https://firecamp.io/blog
- group: other
  title: ''
  type: Download
  url: https://firecamp.io/download
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/firecamp-dev
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/firecamp-dev/firecamp
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/8hRaqhK
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/FirecampDev
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/firecamp/refs/heads/main/packages/firecamp-packages.yml
  title: ''
  type: Packages
  url: packages/firecamp-packages.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/firecamp/refs/heads/main/changelog/firecamp-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/firecamp-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/firecamp/refs/heads/main/lifecycle/firecamp-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/firecamp-lifecycle.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/firecamp/refs/heads/main/llms/firecamp-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/firecamp-llms.txt
- group: commercial
  title: ''
  type: TermsOfService
  url: https://firecamp.io/legal/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://firecamp.io/legal/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://firecamp.dev
- group: operate
  title: ''
  type: Support
  url: https://discord.com/invite/8hRaqhK
created: '2026-03-27'
description: Firecamp is an open-source API development platform for designing, testing, and documenting REST, GraphQL, and WebSocket APIs. It provides multi-protocol playgrounds (REST, GraphQL, WebSocket, SocketIO), team collaboration in shared workspaces, API collection management, a test runner, and CLI/CI-CD integration. Firecamp does not expose a public consumer API; it is a tooling product for working with other APIs.
finops:
- name: Firecamp Finops
  service_category: API
  slug: firecamp-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/firecamp.png
layout: provider
modified: '2026-09-13'
name: Firecamp
nav: Providers
network: true
overview: 'Firecamp publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include API Client, Clients, GraphQL, GUI, and REST.


  Firecamp''s developer surface includes documentation, pricing, engineering blog, changelog, support, and 18 more developer resources.'
plans:
- name: Firecamp Plans Pricing
  plan_count: 3
  slug: firecamp-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Firecamp Rate Limits
  slug: firecamp-rate-limits
score:
  band: thin
  composite: 32.8
  coverage:
    artifact_dirs: 12
    catalog_earned: 47.0
    catalog_earned_first_party: 12.0
    catalog_gap: 68.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 84.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 59.3
    operational_transparency: 18.4
  open_source:
    applies: true
    score: 50.0
  previous_composite: 32.8
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/firecamp/refs/heads/main/screenshots/firecamp-2026-06-20T181227.png
security:
- kind: domain-security
  name: Firecamp Domain Security
  slug: firecamp-domain-security
  summary_line: TLSv1.3 · HSTS
slug: firecamp
tags:
- API Client
- Clients
- GraphQL
- GUI
- REST
- WebSocket
- Open-Source
- Testing
website: https://firecamp.io
---
