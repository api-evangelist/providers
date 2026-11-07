---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 14.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for AppWizzy platform as described in documentation.
  name: AppWizzy API
  slug: appwizzy-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/appwizzy-com/plans/appwizzy-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/appwizzy-com-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/appwizzy-com/changelog/appwizzy-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/appwizzy-com-changelog.yml
- group: agent
  href: https://artifacts.apis.io/appwizzy-com/llms/appwizzy-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/appwizzy-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/appwizzy-com/well-known/appwizzy-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/appwizzy-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/appwizzy-com/hosts/appwizzy-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/appwizzy-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/appwizzy-com/vendors/appwizzy-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/appwizzy-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/appwizzy-com/security/appwizzy-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/appwizzy-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://appwizzy.com/
- group: company
  title: ''
  type: Blog
  url: https://appwizzy.com/blog
- group: docs
  title: ''
  type: Documentation
  url: https://appwizzy.com/documentation
- group: start
  title: ''
  type: GettingStarted
  url: https://appwizzy.com/documentation/quick-start
- group: build
  title: ''
  type: GitHubOrganization
  url: https://appwizzy.com/documentation/github-integration
- group: start
  title: ''
  type: Login
  url: https://appwizzy.com/users/sign_in
- group: build
  title: ''
  type: Postman
  url: https://appwizzy.com/documentation/authorization-in-postman
- group: commercial
  title: ''
  type: Pricing
  url: https://appwizzy.com/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://appwizzy.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://appwizzy.com/terms
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://appwizzy.com/mcp
  - status: 200
    url: https://appwizzy.com/
  reason: partner-login
  state: gated
created: '2026-11-01'
description: AppWizzy provides a professional vibe‑coding platform that enables developers to build scalable web apps, SaaS, AI tools, and internal utilities with AI assistance. The platform offers templates, deployment guides, and integrations such as GitHub, aiming to simplify the creation and maintenance of modern applications for years to come.
image: https://appwizzy.com/assets/appwizzy-dashboard/appwizzy-og-6675faff5871466e034f58f230d7965fa8353b955b74352dfb3c9ea5e00b713b.png
layout: provider
modified: '2026-11-01'
name: AppWizzy
nav: Providers
network: true
overview: 'AppWizzy is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Platform, Artificial Intelligence, Software-as-a-Service, Development, and Low-Code.


  AppWizzy''s developer surface includes changelog, engineering blog, documentation, getting-started guide, pricing, and 12 more developer resources.'
plans:
- name: Appwizzy Com Plans Pricing
  plan_count: 3
  slug: appwizzy-com-plans-pricing
random_paper: 2
score:
  band: emerging
  composite: 21.7
  coverage:
    artifact_dirs: 10
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.2
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 57.1
    operational_transparency: 18.4
  previous_composite: 29.9
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Appwizzy Com Domain Security
  slug: appwizzy-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: appwizzy-com
tags:
- Platform
- Artificial Intelligence
- Software-as-a-Service
- Development
- Low-Code
website: https://appwizzy.com/
---
