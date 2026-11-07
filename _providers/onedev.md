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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 5.4
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/onedev/plans/onedev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/onedev-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/onedev/authentication/onedev-authentication.yml
  title: ''
  type: Authentication
  url: authentication/onedev-authentication.yml
- group: agent
  href: https://artifacts.apis.io/onedev/llms/onedev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/onedev-llms.txt
- group: other
  href: https://artifacts.apis.io/onedev/hosts/onedev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/onedev-hosts.yml
- group: other
  href: https://artifacts.apis.io/onedev/vendors/onedev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/onedev-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://onedev.io/privacy-policy
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.onedev.io/administration-guide/https-setup
- group: auth
  href: https://artifacts.apis.io/onedev/security/onedev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/onedev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://onedev.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.onedev.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://code.onedev.io/onedev/server/~issues
- group: company
  title: ''
  type: Blog
  url: https://onedev.io/blogs
- group: commercial
  title: ''
  type: Pricing
  url: https://onedev.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://onedev.io/signup
- group: operate
  title: ''
  type: Support
  url: https://code.onedev.io/onedev/server/~issues
coverage:
  checked: '2026-10-27'
  detail: Docs site returns HTML for the OpenAPI endpoint, providing no machine‑readable contract.
  evidence:
  - status: 200
    url: https://docs.onedev.io/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-26'
description: OneDev is an autonomous development platform that integrates Git repository hosting, issue tracking, pull requests, CI/CD pipelines, package management, wikis, and AI‑assisted workflows. It enables teams to manage the full software development lifecycle in a single self‑hosted application, offering both community and enterprise editions with extensible plugins and customizable automation.
layout: provider
modified: '2026-10-26'
name: OneDev
nav: Providers
network: true
overview: 'OneDev is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Development, CI/CD, Version Control, and Automation.


  OneDev''s developer surface includes authentication, getting-started guide, documentation, engineering blog, pricing, signup flow, support, and 8 more developer resources.'
plans:
- name: Onedev Plans Pricing
  plan_count: 2
  slug: onedev-plans-pricing
random_paper: 17
score:
  band: emerging
  composite: 18.8
  coverage:
    artifact_dirs: 13
    catalog_earned: 33.0
    catalog_earned_first_party: 8.0
    catalog_gap: 82.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.5
  facets:
    access_clarity: 38.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 31.0
    discoverability: 51.8
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 26.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/onedev/onedev-2026-11-03T140550.png
security:
- kind: authentication
  name: Onedev Authentication
  slug: onedev-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Onedev Domain Security
  slug: onedev-domain-security
  summary_line: TLSv1.3
slug: onedev
tags:
- Company
- Development
- CI/CD
- Version Control
- Automation
website: https://onedev.io/
---
