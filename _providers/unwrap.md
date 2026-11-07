---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 36.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: GraphQL API for fetching feedback entries and group taxonomy, batch-importing feedback, and building classification groups. Authenticated with a personal API key sent as an HTTP Bearer token, scoped t
  name: Unwrap GraphQL API
  slug: unwrap-graphql-api
artifact_total: 12
common:
- group: commercial
  href: https://artifacts.apis.io/unwrap/plans/unwrap-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/unwrap-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/unwrap/security/unwrap-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/unwrap-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/unwrap/security/unwrap-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/unwrap-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.unwrap.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.unwrap.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.unwrap.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.unwrap.ai/collections/6774268412-api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.unwrap.ai/articles/6140971517-getting-started
- group: company
  title: ''
  type: Blog
  url: https://www.unwrap.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.unwrap.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.unwrap.ai
- group: start
  title: ''
  type: Login
  url: https://app.unwrap.ai
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.unwrap.ai/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.unwrap.ai/legal/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/unwrap-nlp
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.unwrap.ai/collections/1750160942-unwrap_changelog
- group: auth
  href: https://artifacts.apis.io/unwrap/authentication/unwrap-authentication.yml
  title: ''
  type: Authentication
  url: authentication/unwrap-authentication.yml
- group: auth
  href: https://artifacts.apis.io/unwrap/scopes/unwrap-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/unwrap-scopes.yml
- group: design
  href: https://artifacts.apis.io/unwrap/conventions/unwrap-conventions.yml
  title: ''
  type: Conventions
  url: conventions/unwrap-conventions.yml
- group: design
  href: https://artifacts.apis.io/unwrap/conventions/unwrap-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/unwrap-conventions.yml
- group: design
  href: https://artifacts.apis.io/unwrap/errors/unwrap-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/unwrap-problem-types.yml
- group: operate
  href: https://artifacts.apis.io/unwrap/rate-limits/unwrap-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/unwrap-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/unwrap/lifecycle/unwrap-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/unwrap-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/unwrap/data-model/unwrap-data-model.yml
  title: ''
  type: DataModel
  url: data-model/unwrap-data-model.yml
- group: design
  href: https://artifacts.apis.io/unwrap/conformance/unwrap-conformance.yml
  title: ''
  type: Conformance
  url: conformance/unwrap-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.unwrap.ai/why-unwrap
- group: agent
  href: https://artifacts.apis.io/unwrap/well-known/unwrap-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/unwrap-well-known.yml
- group: agent
  href: https://artifacts.apis.io/unwrap/mcp/unwrap-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/unwrap-mcp.yml
- group: agent
  href: https://artifacts.apis.io/unwrap/llms/unwrap-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/unwrap-llms.txt
- group: build
  href: https://artifacts.apis.io/unwrap/packages/unwrap-packages.yml
  title: ''
  type: Packages
  url: packages/unwrap-packages.yml
- group: build
  href: https://artifacts.apis.io/unwrap/packages/unwrap-packages.yml
  title: ''
  type: SDKs
  url: packages/unwrap-packages.yml
- group: agent
  href: https://artifacts.apis.io/unwrap/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Unwrap is an AI-powered customer intelligence platform, founded by ex-Amazon Alexa product leaders, that aggregates customer feedback from every channel (support tickets, surveys, app reviews, sales calls, social) and uses custom NLP to auto-tag, cluster and surface actionable product insights without manual analysis. It ships a GraphQL data API (Bearer API key) for fetching feedback entries and taxonomy, batch-importing feedback, and building groups, plus a read-only remote MCP server (OAuth 2.0) and a first-party Surveys mobile SDK for iOS and Android. Unwrap is SOC 2 Type II and GDPR compliant.
finops:
- has_sources: true
  method: derived
  name: Unwrap Finops
  primary_unit: subscription
  service_category: ''
  slug: unwrap-finops
  template: false
image: https://cdn.prod.website-files.com/67c5e65b5323e6f7f216d5e7/67ddb0f28d559f418b033a59_unwrap-og-image.jpg
layout: provider
mcp_servers:
- description: Remote MCP server at nlp.api.production.unwrap.ai over HTTP; 9 tools listed.
  name: Unwrap MCP Server
  slug: unwrap
modified: '2026-07-21'
name: Unwrap
nav: Providers
network: true
overview: 'Unwrap is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Ai Apps, Customer Feedback, Customer Intelligence, and Product Analytics.


  Unwrap''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, changelog, and 25 more developer resources.'
plans:
- name: Unwrap Plans Pricing
  plan_count: 1
  slug: unwrap-plans-pricing
- name: Unwrap Price Estimates
  plan_count: 0
  slug: unwrap-price-estimates
random_paper: 21
rate_limits:
- limit_count: 4
  name: Unwrap Rate Limits
  slug: unwrap-rate-limits
scopes:
- name: Unwrap Scopes
  scope_count: 5
  slug: unwrap-scopes
  summary_line: 5 scopes · authorizationCode/clientCredentials
score:
  band: developing
  composite: 47.3
  coverage:
    artifact_dirs: 22
    catalog_earned: 60.0
    catalog_earned_first_party: 20.0
    catalog_gap: 55.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 61.3
    discoverability: 75.0
    operational_transparency: 50.0
  previous_composite: 47.3
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 39.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/unwrap/unwrap-2026-08-17T082635.png
security:
- kind: authentication
  name: Unwrap Authentication
  slug: unwrap-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Unwrap Domain Security
  slug: unwrap-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Unwrap Trust Center
  slug: unwrap-trust-center
  summary_line: SOC 2, GDPR
skill_count: 2
skills:
- name: Export Unwrap feedback and taxonomy
  slug: unwrap-export-feedback
- name: Batch-import feedback and build groups in Unwrap
  slug: unwrap-import-feedback
slug: unwrap
tags:
- Company
- Ai Apps
- Customer Feedback
- Customer Intelligence
- Product Analytics
- Voice of Customer
- Natural Language Processing
- GraphQL
- MCP
website: https://www.unwrap.ai/
---
