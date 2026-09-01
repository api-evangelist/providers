---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
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
    agent_skills: derived
    agentic_access: derived
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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.1
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Rtbhouse Agentic Access
  operation_count: 23
  slug: rtbhouse-agentic-access
  summary_line: 23 operations · 3 acting
api_count: 1
apis:
- description: The Advertisers API from RTB House — 12 operation(s) for advertisers.
  name: RTB House Advertisers API
  slug: rtbhouse-advertisers-api
- description: The Dev API from RTB House — 1 operation(s) for dev.
  name: RTB House Dev API
  slug: rtbhouse-dev-api
- description: The Statistics API from RTB House — 8 operation(s) for statistics.
  name: RTB House Statistics API
  slug: rtbhouse-statistics-api
- description: The Tokens API from RTB House — 1 operation(s) for tokens.
  name: RTB House Tokens API
  slug: rtbhouse-tokens-api
- description: The User API from RTB House — 1 operation(s) for user.
  name: RTB House User API
  slug: rtbhouse-user-api
artifact_total: 22
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Client's panel API docs Advertisers API
  slug: open-rtbhouse-advertisers-api
- collection_type: open
  name: Client's panel API docs Advertisers Dev API
  slug: open-rtbhouse-dev-api
- collection_type: open
  name: Client's panel API docs Advertisers Statistics API
  slug: open-rtbhouse-statistics-api
- collection_type: open
  name: Client's panel API docs Advertisers Tokens API
  slug: open-rtbhouse-tokens-api
- collection_type: open
  name: Client's panel API docs Advertisers User API
  slug: open-rtbhouse-user-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/rtbhouse-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rtbhouse-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/rtbhouse-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.rtbhouse.com
- group: docs
  title: ''
  type: Documentation
  url: https://api.panel.rtbhouse.com/api/docs
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/rtbhouse-apps
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/rtb-house
- group: company
  title: ''
  type: Blog
  url: https://www.rtbhouse.com/blog
- group: other
  title: ''
  type: X
  url: https://twitter.com/rtbhouse
- group: docs
  title: ''
  type: APIReference
  url: https://api.panel.rtbhouse.com/api/redoc
- group: operate
  title: ''
  type: Support
  url: https://www.rtbhouse.com/contact
- group: start
  title: ''
  type: Login
  url: https://panel.rtbhouse.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.rtbhouse.com/privacy-center/web-privacy-policy
- group: commercial
  title: ''
  type: Plans
  url: plans/rtbhouse-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/rtbhouse-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/rtbhouse-finops.yml
- group: build
  title: ''
  type: Packages
  url: packages/rtbhouse-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/rtbhouse-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/rtbhouse-cli.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/rtbhouse-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/rtbhouse-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/rtbhouse-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/rtbhouse-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/rtbhouse-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/rtbhouse-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/rtbhouse-conformance.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-06-13'
description: RTB House is a next-generation performance demand-side platform (DSP) that uses proprietary deep learning algorithms to power retargeting and programmatic advertising campaigns. The platform provides a REST API for managing advertisers, campaigns, product feeds, audiences, RTB creatives, conversions, and accessing detailed performance analytics. RTB House operates in 90+ markets and serves thousands of leading brands worldwide.
examples:
- key_count: 2
  name: Rtbhouse Advertiser Example
  slug: rtbhouse-advertiser-example
- key_count: 2
  name: Rtbhouse Rtb Stats Example
  slug: rtbhouse-rtb-stats-example
finops:
- name: Rtbhouse Finops
  service_category: ''
  slug: rtbhouse-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rtbhouse.png
json_schemas:
- name: Advertiser
  property_count: 12
  slug: rtbhouse-advertiser
jsonld:
- class_count: 11
  name: Rtbhouse Context
  property_count: 57
  slug: rtbhouse-context
layout: provider
modified: '2026-08-13'
name: RTB House
nav: Providers
network: true
overview: 'RTB House publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Advertisers API, Dev API, Statistics API, and 2 more. Tagged areas include Advertising, Retargeting, Programmatic, DSP, and Deep Learning.


  The RTB House catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  RTB House''s developer surface includes authentication, documentation, engineering blog, API reference, support, CLI, changelog, and 20 more developer resources.'
plans:
- name: Rtbhouse Plans Pricing
  plan_count: 1
  slug: rtbhouse-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Rtbhouse Rate Limits
  slug: rtbhouse-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: RTB House API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: rtbhouse-jsonschema-spectral-rules
score:
  band: developing
  composite: 44.5
  coverage:
    artifact_dirs: 28
    catalog_gap: 52.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 46.1
    commercial_clarity: 46.1
    contract_governance: 14.4
    contract_quality: 51.6
    developer_ergonomics: 51.8
    discoverability: 75.9
    governance: 14.4
    operational_transparency: 21.1
  previous_composite: 44.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/rtbhouse/refs/heads/main/screenshots/rtbhouse-2026-06-20T193241.png
security:
- kind: authentication
  name: Rtbhouse Authentication
  slug: rtbhouse-authentication
  summary_line: http · 3 schemes
- kind: domain-security
  name: Rtbhouse Domain Security
  slug: rtbhouse-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: rtbhouse
tags:
- Advertising
- Retargeting
- Programmatic
- DSP
- Deep Learning
- RTB
- Performance Marketing
website: https://www.rtbhouse.com
---
