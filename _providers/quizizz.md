---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: true
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 8.5
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: Remote Model Context Protocol server operated by Wayground at https://wayground.com/_quizizzmcp/main/mcp. Its existence is declared by Wayground's own /.well-known/oauth-protected-resource document, w
  name: Wayground MCP Server
  slug: wayground-mcp-server
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://wayground.com/
- group: start
  title: ''
  type: SignUp
  url: https://wayground.com/signup
- group: start
  title: ''
  type: Login
  url: https://wayground.com/login
- group: commercial
  title: ''
  type: Pricing
  url: https://wayground.com/home/plans
- group: operate
  title: ''
  type: Support
  url: https://help.wayground.com/support/home
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.wayground.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://wayground.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/quizizz
- group: commercial
  title: ''
  type: TermsOfService
  url: https://wayground.com/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://wayground.com/privacy
- group: agent
  title: ''
  type: WellKnown
  url: well-known/quizizz-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/quizizz-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/quizizz-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/quizizz-rate-limits.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/quizizz-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/quizizz-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/quizizz-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/quizizz-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/quizizz-packages.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/quizizz-domain-security.yml
created: '2026-08-26'
description: Wayground (formerly Quizizz) is a K-12 supplemental learning platform from Santa Monica, California that blends instruction, practice and assessment with AI generation. Teachers build and run quizzes, lessons, flashcards, worksheets and video activities; administrators get school and district dashboards, rostering and grade sync. The company reports use in over 150 countries and by 90% of U.S. schools. Its integration surface is aimed at learning platforms rather than at general developers - LTI embedding into Canvas, Schoology, Blackboard and Moodle, rostering and SSO through Clever, ClassLink and Google Classroom, and automatic grade passback. Wayground publishes no public REST API or developer portal, but it does operate an undocumented remote Model Context Protocol server, declared by its own /.well-known/oauth-protected-resource document and fronted by a full OAuth 2.1 authorization server with dynamic client registration and PKCE.
image: https://cdn.prod.website-files.com/68355113496452bf05789e95/68499b8588e356f4263c24d0_57fcc3f00463cd6477e78e279a926b72_wayground-OG.png
layout: provider
mcp_servers:
- description: ''
  name: Wayground MCP Server
  slug: wayground-mcp-server
modified: '2026-08-26'
name: Wayground
nav: Providers
network: true
overview: 'Wayground publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Education, EdTech, K-12, and Learning.


  Wayground''s developer surface includes signup flow, pricing, support, engineering blog, and 16 more developer resources.'
plans:
- name: Quizizz Plans Pricing
  plan_count: 2
  slug: quizizz-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Quizizz Rate Limits
  slug: quizizz-rate-limits
scopes:
- name: Quizizz Scopes
  scope_count: 0
  slug: quizizz-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 35.6
  coverage:
    artifact_dirs: 14
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 73.7
    commercial_clarity: 73.7
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 35.6
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 74.1
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/quizizz/refs/heads/main/screenshots/quizizz-2026-09-02T152710.png
security:
- kind: authentication
  name: Quizizz Authentication
  slug: quizizz-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Quizizz Domain Security
  slug: quizizz-domain-security
  summary_line: TLSv1.3 · DMARC
slug: quizizz
tags:
- Company
- Education
- EdTech
- K-12
- Learning
- Assessment
- Artificial Intelligence
- MCP
- LTI
- Rostering
- Single Sign-On
website: https://wayground.com/
---
