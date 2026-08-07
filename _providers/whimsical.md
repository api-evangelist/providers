---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
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
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Whimsical Agentic Access
  operation_count: 5
  slug: whimsical-agentic-access
  summary_line: 5 operations · 5 acting
api_count: 7
apis:
- description: 'Limited-beta REST API. Endpoints are read-oriented and use POST verbs: `users.get`, `teams.list`, `comments.list`, `files.list`, `files.get`. Authentication is OAuth 2.1, with credentials issued by Wh'
  name: Whimsical API (Beta)
  slug: whimsical-api-beta
- description: Whimsical exposes SCIM 2.0 (and only SCIM) for programmatic user provisioning; there is no separate REST endpoint for user management. Available on plans with SCIM support (Enterprise).
  name: Whimsical SCIM 2.0 API
  slug: whimsical-scim
- description: The Comments.list API from Whimsical — 1 operation(s) for comments.list.
  name: Whimsical Comments.list API
  slug: whimsical-comments-list-api
- description: The Files.get API from Whimsical — 1 operation(s) for files.get.
  name: Whimsical Files.get API
  slug: whimsical-files-get-api
- description: The Files.list API from Whimsical — 1 operation(s) for files.list.
  name: Whimsical Files.list API
  slug: whimsical-files-list-api
- description: The Teams.list API from Whimsical — 1 operation(s) for teams.list.
  name: Whimsical Teams.list API
  slug: whimsical-teams-list-api
- description: The Users.get API from Whimsical — 1 operation(s) for users.get.
  name: Whimsical Users.get API
  slug: whimsical-users-get-api
artifact_total: 16
collections:
- collection_type: open
  name: Whimsical API (Beta)
  slug: open-whimsical
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/whimsical-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/whimsical-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/whimsical-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/whimsical-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/whimsical-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/whimsicalcode
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/whimsical
- group: company
  title: ''
  type: Website
  url: https://whimsical.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://whimsical.com/pricing
- group: commercial
  title: ''
  type: Plans
  url: plans/whimsical-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/whimsical-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/whimsical-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://whimsical.com/_next_public/feed.xml
created: '2026-05-08'
description: Whimsical is a visual workspace for boards, mind maps, flowcharts, wireframes, and documents. The Whimsical API is in limited beta with read-only endpoints for users, teams, comments, and files; user provisioning is exposed only through SCIM 2.0.
finops:
- name: Whimsical Finops
  service_category: Collaboration
  slug: whimsical-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/whimsical.png
layout: provider
modified: '2026-05-08'
name: Whimsical
nav: Providers
network: true
overview: 'Whimsical publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Comments.list API, Files.get API, Files.list API, and 2 more. Tagged areas include Collaboration, Diagramming, Flowcharts, Wireframes, and Mind Maps.


  Whimsical''s developer surface includes authentication, pricing, engineering blog, and 10 more developer resources.'
plans:
- name: Whimsical Plans Pricing
  plan_count: 1
  slug: whimsical-plans-pricing
random_paper: 57
rate_limits:
- limit_count: 1
  name: Whimsical Rate Limits
  slug: whimsical-rate-limits
scopes:
- name: Whimsical Scopes
  scope_count: 0
  slug: whimsical-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 34.9
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 54.3
    developer_ergonomics: 13.0
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 34.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/whimsical/refs/heads/main/screenshots/whimsical-2026-06-20T201434.png
security:
- kind: authentication
  name: Whimsical Authentication
  slug: whimsical-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Whimsical Domain Security
  slug: whimsical-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Whimsical Vulnerability Disclosure
  slug: whimsical-vulnerability-disclosure
  summary_line: disclosure policy published
slug: whimsical
tags:
- Collaboration
- Diagramming
- Flowcharts
- Wireframes
- Mind Maps
website: https://whimsical.com/
---
