---
access_model:
  confidence: high
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 16.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 44
  human_in_the_loop: 0
  name: Redditapis Com Agentic Access
  operation_count: 148
  slug: redditapis-com-agentic-access
  summary_line: 148 operations · 44 acting
api_count: 1
apis:
- description: Redditapis provides a hosted REST API for Reddit data, supporting read, search, posting, voting, direct messages and monitoring.
  name: Redditapis API
  slug: redditapis-api
artifact_total: 10
common:
- group: operate
  href: https://artifacts.apis.io/redditapis-com/rate-limits/redditapis-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/redditapis-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/redditapis-com/plans/redditapis-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/redditapis-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/redditapis-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  href: https://artifacts.apis.io/redditapis-com/changelog/redditapis-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/redditapis-com-changelog.yml
- group: design
  href: https://artifacts.apis.io/redditapis-com/conventions/redditapis-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/redditapis-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/redditapis-com/authentication/redditapis-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/redditapis-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/redditapis-com/conformance/redditapis-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/redditapis-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/redditapis-com/llms/redditapis-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/redditapis-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/redditapis-com/well-known/redditapis-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/redditapis-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/redditapis-com/hosts/redditapis-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/redditapis-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/redditapis-com/vendors/redditapis-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/redditapis-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/redditapis-com/packages/redditapis-com-packages.yml
  title: ''
  type: Packages
  url: packages/redditapis-com-packages.yml
- group: start
  title: ''
  type: SignUp
  url: https://www.redditapis.com/signup
- group: build
  title: ''
  type: SDKs
  url: https://www.redditapis.com/sdk
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.redditapis.com/privacy-and-data-handling
- group: company
  title: ''
  type: Newsroom
  url: https://www.redditapis.com/press
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.redditapis.com/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://www.redditapis.com/quickstart
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.redditapis.com\
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/redditapis
- group: auth
  href: https://artifacts.apis.io/redditapis-com/security/redditapis-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/redditapis-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://redditapis.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.redditapis.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://www.redditapis.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.redditapis.com/blogs
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.redditapis.com/terms-of-service
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://docs.redditapis.com/openapi.json
  - status: 401
    url: https://api.redditapis.com/mcp
  - status: 401
    url: https://api.redditapis.com/api/graphql
  - status: 200
    url: https://redditapis.com/
  reason: partner-login
  state: gated
created: '2026-10-31'
description: Redditapis.com provides a hosted, pay‑per‑call REST API for Reddit data, enabling reading, posting, voting, and direct messaging without the need for Reddit’s OAuth app review or subscription. The service offers transparent pricing starting at $0.0015 per call, free starter credits, and a simple bearer‑token authentication model. It is operated by an independent developer team, not affiliated with Reddit Inc., and aims to give developers immediate access to Reddit’s functionality for AI agents, bots, and applications.
image: https://www.redditapis.com/og.png
jsonld:
- class_count: 1
  name: Redditapis Com Context
  property_count: 6
  slug: redditapis-com-context
layout: provider
modified: '2026-10-31'
name: redditapis-com
nav: Providers
network: true
overview: 'redditapis-com publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Reddit, Pay-per-call, and Artificial Intelligence.


  The redditapis-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  redditapis-com''s developer surface includes changelog, authentication, signup flow, getting-started guide, documentation, pricing, engineering blog, and 19 more developer resources.'
plans:
- name: Redditapis Com Plans Pricing
  plan_count: 16
  slug: redditapis-com-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 3
  name: Redditapis Com Rate Limits
  slug: redditapis-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 60
  extends:
  - spectral:oas
  name: redditapis-com API Rules
  rule_count: 19
  severity_counts:
    error: 15
    hint: 0
    info: 1
    warn: 3
  slug: redditapis-com-rules
scopes:
- name: Redditapis Com Scopes
  scope_count: 0
  slug: redditapis-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 39.4
  coverage:
    artifact_dirs: 33
    catalog_earned: 65.5
    catalog_earned_first_party: 24.0
    catalog_gap: 49.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.7
  facets:
    access_clarity: 53.9
    contract_governance: 31.8
    contract_quality: 12.7
    developer_ergonomics: 42.1
    discoverability: 58.0
    operational_transparency: 42.1
  previous_composite: 50.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/redditapis-com/redditapis-com-2026-11-03T142101.png
security:
- kind: authentication
  name: Redditapis Com Authentication
  slug: redditapis-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Redditapis Com Domain Security
  slug: redditapis-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: redditapis-com-search
  slug: redditapis-com-search
slug: redditapis-com
tags:
- Company
- Reddit
- Pay-per-call
- Artificial Intelligence
website: https://redditapis.com/
---
