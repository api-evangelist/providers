---
access_model:
  confidence: high
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
  - scopes
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
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 36.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Klaxoon Agentic Access
  operation_count: 6
  slug: klaxoon-agentic-access
  summary_line: 6 operations
api_count: 1
apis:
- description: The Klaxoon API allows developers to integrate Klaxoon's collaborative features into their applications, enabling automation of board creation, activity management, and participant engagement. It incl
  name: Klaxoon API
  slug: klaxoon-api
- baseURL: https://developers.klaxoon.com/klaxoon/api/v1
  baseurl_source: spec
  description: Adventure activity resources
  name: Klaxoon Adventures API
  slug: klaxoon-adventures-api
- baseURL: https://developers.klaxoon.com/klaxoon/api/v1
  baseurl_source: spec
  description: Mission activity resources
  name: Klaxoon Missions API
  slug: klaxoon-missions-api
- baseURL: https://developers.klaxoon.com/klaxoon/api/v1
  baseurl_source: spec
  description: Quiz activity resources and participant results
  name: Klaxoon Quizzes API
  slug: klaxoon-quizzes-api
- baseURL: https://developers.klaxoon.com/klaxoon/api/v1
  baseurl_source: spec
  description: Survey activity resources and participant results
  name: Klaxoon Surveys API
  slug: klaxoon-surveys-api
artifact_total: 19
collections:
- collection_type: open
  name: Klaxoon Adventures API
  slug: open-klaxoon-adventures-api
- collection_type: open
  name: Klaxoon Adventures Missions API
  slug: open-klaxoon-missions-api
- collection_type: open
  name: Klaxoon Adventures Quizzes API
  slug: open-klaxoon-quizzes-api
- collection_type: open
  name: Klaxoon Adventures Surveys API
  slug: open-klaxoon-surveys-api
- collection_type: open
  name: Klaxoon API
  slug: open-klaxoon
common:
- group: commercial
  href: https://artifacts.apis.io/klaxoon/plans/klaxoon-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/klaxoon-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/klaxoon/rate-limits/klaxoon-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/klaxoon-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/klaxoon/finops/klaxoon-finops.yml
  title: ''
  type: FinOps
  url: finops/klaxoon-finops.yml
- group: agent
  href: https://artifacts.apis.io/klaxoon/agentic-access/klaxoon-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/klaxoon-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/klaxoon/security/klaxoon-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/klaxoon-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/klaxoon/authentication/klaxoon-authentication.yml
  title: ''
  type: Authentication
  url: authentication/klaxoon-authentication.yml
- group: auth
  href: https://artifacts.apis.io/klaxoon/scopes/klaxoon-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/klaxoon-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/klaxoon
- group: company
  title: ''
  type: Website
  url: https://www.klaxoon.com
- group: start
  title: ''
  type: Portal
  url: https://developers.klaxoon.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.klaxoon.com/docs
- group: auth
  title: ''
  type: Authentication
  url: https://developers.klaxoon.com/docs/authentication
- group: docs
  title: ''
  type: Reference
  url: https://developers.klaxoon.com/klaxoon/reference
- group: company
  title: ''
  type: Blog
  url: https://www.klaxoon.com/blog
- group: start
  title: ''
  type: Signup
  url: https://app.klaxoon.com/signup
- group: commercial
  title: ''
  type: Pricing
  url: https://www.klaxoon.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.klaxoon.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.klaxoon.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.klaxoon.com
- group: operate
  title: ''
  type: Support
  url: https://support.klaxoon.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/klaxoon
- group: agent
  title: ''
  type: LlmsText
  url: https://developers.klaxoon.com/llms.txt
created: '2024-01-01'
description: Klaxoon is a collaborative platform that provides tools for team collaboration, brainstorming, meetings, and workshops. The platform includes features like boards, quizzes, surveys, and other interactive activities to enhance team productivity and engagement. Klaxoon publishes a developer portal with documentation for board integration, embedding, and enterprise audit and SCIM endpoints, but does not currently publish a public OpenAPI specification.
finops:
- has_sources: false
  method: generated
  name: Klaxoon Finops
  primary_unit: request
  service_category: API
  slug: klaxoon-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/klaxoon.png
layout: provider
mcp_servers:
- description: Remote MCP server at developers.klaxoon.com over HTTP.
  name: Klaxoon MCP Server
  slug: klaxoon
modified: '2026-04-28'
name: Klaxoon
nav: Providers
network: true
overview: 'Klaxoon publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Adventures API, Missions API, Quizzes API, and 2 more. Tagged areas include Collaboration, Meetings, Productivity, Team Collaboration, and Workshops.


  The Klaxoon catalog on APIs.io includes 1 Spectral governance ruleset.


  Klaxoon''s developer surface includes authentication, developer portal, documentation, engineering blog, signup flow, pricing, support, and 15 more developer resources.'
plans:
- name: Klaxoon Plans Pricing
  plan_count: 3
  slug: klaxoon-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 5
  name: Klaxoon Rate Limits
  slug: klaxoon-rate-limits
rules:
- authorship: generated
  effective_rule_count: 101
  extends:
  - spectral:oas
  name: Klaxoon API Rules
  rule_count: 60
  severity_counts:
    error: 58
    hint: 0
    info: 1
    warn: 1
  slug: klaxoon-rules
scopes:
- name: Klaxoon Scopes
  scope_count: 10
  slug: klaxoon-scopes
  summary_line: 10 scopes · authorizationCode
score:
  band: developing
  composite: 43.4
  coverage:
    artifact_dirs: 19
    catalog_earned: 42.5
    catalog_earned_first_party: 0.0
    catalog_gap: 72.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 4.4
  facets:
    access_clarity: 31.6
    contract_governance: 13.6
    contract_quality: 49.4
    developer_ergonomics: 54.8
    discoverability: 66.7
    operational_transparency: 34.2
  previous_composite: 39.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/klaxoon/klaxoon-2026-06-20T184103.png
security:
- kind: authentication
  name: Klaxoon Authentication
  slug: klaxoon-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Klaxoon Domain Security
  slug: klaxoon-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: klaxoon
tags:
- Collaboration
- Meetings
- Productivity
- Team Collaboration
- Workshops
- Brainstorming
- Whiteboard
website: https://www.klaxoon.com
---
