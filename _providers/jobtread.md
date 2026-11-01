---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 13.7
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: JobTread API is based on the Pave query language, a GraphQL‑like language for querying exactly what you need.
  name: JobTread API
  slug: jobtread-api
artifact_total: 4
common:
- group: agent
  href: https://artifacts.apis.io/jobtread/llms/jobtread-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/jobtread-llms.txt
- group: agent
  href: https://artifacts.apis.io/jobtread/well-known/jobtread-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/jobtread-well-known.yml
- group: other
  href: https://artifacts.apis.io/jobtread/hosts/jobtread-hosts.yml
  title: ''
  type: Hosts
  url: hosts/jobtread-hosts.yml
- group: start
  title: ''
  type: SignUp
  url: https://app.jobtread.com/sign-up
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.jobtread.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.jobtread.com/news
- group: other
  title: ''
  type: Leadership
  url: https://www.jobtread.com/team/dan
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/jobtread
- group: auth
  href: https://artifacts.apis.io/jobtread/security/jobtread-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/jobtread-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://jobtread.com/
- group: docs
  title: ''
  type: Documentation
  url: https://app.jobtread.com/docs
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.jobtread.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.jobtread.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.jobtread.com/terms
- group: operate
  title: ''
  type: Support
  url: https://app.jobtread.com/help
- group: company
  title: ''
  type: Blog
  url: https://www.jobtread.com/blog
coverage:
  checked: '2026-10-28'
  detail: Documentation is rendered but provides no machine‑readable OpenAPI, GraphQL SDL, AsyncAPI, gRPC, or WSDL specifications.
  evidence:
  - status: 200
    url: https://app.jobtread.com/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: JobTread provides a cloud‑based construction estimating and project management platform. It helps contractors and remodelers plan jobs, track finances, manage resources, and integrate with tools like QuickBooks and Stripe. The SaaS solution streamlines bids, schedules, budgets, and client communication across the construction lifecycle.
image: https://www.jobtread.com/images/home/home-meta-og.png
layout: provider
modified: '2026-10-28'
name: JobTread
nav: Providers
network: true
overview: 'JobTread is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Construction, Estimating, Project Management, SaaS, and Finance.


  JobTread''s developer surface includes signup flow, documentation, pricing, support, engineering blog, and 11 more developer resources.'
random_paper: 3
scopes:
- name: Jobtread Scopes
  scope_count: 0
  slug: jobtread-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 24.0
  coverage:
    artifact_dirs: 17
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 69.6
    operational_transparency: 5.3
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Jobtread Authentication
  slug: jobtread-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Jobtread Domain Security
  slug: jobtread-domain-security
  summary_line: TLSv1.3 · DMARC
slug: jobtread
tags:
- Construction
- Estimating
- Project Management
- SaaS
- Finance
website: https://jobtread.com/
---
