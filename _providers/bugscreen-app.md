---
access_model:
  confidence: medium
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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.8
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 3
common:
- group: operate
  title: ''
  type: Support
  url: https://www.bugscreen.app/support
- group: commercial
  href: https://artifacts.apis.io/bugscreen-app/plans/bugscreen-app-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bugscreen-app-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/bugscreen-app/changelog/bugscreen-app-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/bugscreen-app-changelog.yml
- group: design
  href: https://artifacts.apis.io/bugscreen-app/conventions/bugscreen-app-conventions.yml
  title: ''
  type: Conventions
  url: conventions/bugscreen-app-conventions.yml
- group: auth
  href: https://artifacts.apis.io/bugscreen-app/authentication/bugscreen-app-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bugscreen-app-authentication.yml
- group: agent
  href: https://artifacts.apis.io/bugscreen-app/llms/bugscreen-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bugscreen-app-llms.txt
- group: agent
  href: https://artifacts.apis.io/bugscreen-app/well-known/bugscreen-app-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bugscreen-app-well-known.yml
- group: other
  href: https://artifacts.apis.io/bugscreen-app/hosts/bugscreen-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bugscreen-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/bugscreen-app/vendors/bugscreen-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bugscreen-app-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bugscreen.app/terms
- group: build
  title: ''
  type: SDKs
  url: https://www.bugscreen.app/blog/tag/sdk
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bugscreen.app/privacy
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.bugscreen.app/changelog
- group: company
  title: ''
  type: Blog
  url: https://www.bugscreen.app/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://www.bugscreen.app/docs/android
- group: auth
  href: https://artifacts.apis.io/bugscreen-app/security/bugscreen-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bugscreen-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bugscreen.app/
- group: docs
  title: ''
  type: Documentation
  url: https://www.bugscreen.app/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://www.bugscreen.app/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.bugscreen.app/signup
- group: start
  title: ''
  type: Login
  url: https://www.bugscreen.app/login
coverage:
  checked: '2026-11-03'
  detail: Documentation pages exist but no machine‑readable OpenAPI, AsyncAPI, GraphQL, gRPC or WSDL contracts were found.
  evidence:
  - status: 200
    url: https://www.bugscreen.app/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-03'
description: BugScreen provides mobile bug reporting and visual feedback for QA and beta testing. Testers can screenshot bugs, and BugScreen attaches technical context, files tickets, and integrates with GitHub, Jira, ClickUp, Android, iOS, and React Native SDKs. It helps teams capture, track, and resolve app issues efficiently, improving software quality and user experience.
image: https://www.bugscreen.app/opengraph-image?8c05c481341c658f
layout: provider
modified: '2026-11-03'
name: BugScreen
nav: Providers
network: true
overview: 'BugScreen is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Bug Reporting, QA, Mobile, SDK, and Integration.


  BugScreen''s developer surface includes support, changelog, authentication, engineering blog, getting-started guide, documentation, pricing, and 14 more developer resources.'
plans:
- name: Bugscreen App Plans Pricing
  plan_count: 4
  slug: bugscreen-app-plans-pricing
random_paper: 4
score:
  band: emerging
  composite: 23.4
  coverage:
    artifact_dirs: 12
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 33.3
    discoverability: 48.2
    operational_transparency: 7.9
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Bugscreen App Authentication
  slug: bugscreen-app-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Bugscreen App Domain Security
  slug: bugscreen-app-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bugscreen-app
tags:
- Bug Reporting
- QA
- Mobile
- SDK
- Integration
website: https://www.bugscreen.app/
---
