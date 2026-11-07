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
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
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
  score: 6.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/centscheck-com/plans/centscheck-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/centscheck-com-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/centscheck-com/changelog/centscheck-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/centscheck-com-changelog.yml
- group: agent
  href: https://artifacts.apis.io/centscheck-com/llms/centscheck-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/centscheck-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/centscheck-com/well-known/centscheck-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/centscheck-com-security.txt
- group: agent
  href: https://artifacts.apis.io/centscheck-com/well-known/centscheck-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/centscheck-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/centscheck-com/hosts/centscheck-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/centscheck-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/centscheck-com/vendors/centscheck-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/centscheck-com-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://centscheck.com/security
- group: operate
  title: ''
  type: ChangeLog
  url: https://centscheck.com/releases
- group: start
  title: ''
  type: GettingStarted
  url: https://centscheck.com/support/ai-link
- group: auth
  href: https://artifacts.apis.io/centscheck-com/security/centscheck-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/centscheck-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/centscheck-com/security/centscheck-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/centscheck-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://centscheck.com/
- group: operate
  title: ''
  type: Support
  url: https://centscheck.com/support
- group: company
  title: ''
  type: Blog
  url: https://centscheck.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://centscheck.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://centscheck.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://centscheck.com/privacy
coverage:
  checked: '2026-11-03'
  detail: CentsCheck provides a budgeting app but does not offer a public developer API or program.
  evidence:
  - status: 200
    url: https://centscheck.com/
  reason: no-developer-program
  state: none
created: '2026-11-03'
description: CentsCheck is a personal finance app that helps users track spending, set daily safe‑to‑spend limits, and manage budgets across multiple currencies. Built as a solo project with AI assistance, it offers features like receipt scanning, shared pool budgeting, portfolio tracking, and AI‑driven expense logging, all without requiring bank logins. The service is free to start and available on iOS and Android.
image: https://centscheck.com/og-image.jpg
layout: provider
modified: '2026-11-03'
name: CentsCheck
nav: Providers
network: true
overview: 'CentsCheck is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Personal Finance, Budgeting, Mobile App, iOS, and Android.


  CentsCheck''s developer surface includes changelog, getting-started guide, support, engineering blog, pricing, and 13 more developer resources.'
plans:
- name: Centscheck Com Plans Pricing
  plan_count: 3
  slug: centscheck-com-plans-pricing
random_paper: 23
score:
  band: emerging
  composite: 18.0
  coverage:
    artifact_dirs: 10
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 48.2
    operational_transparency: 13.2
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
- kind: domain-security
  name: Centscheck Com Domain Security
  slug: centscheck-com-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Centscheck Com Vulnerability Disclosure
  slug: centscheck-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: centscheck-com
tags:
- Personal Finance
- Budgeting
- Mobile App
- iOS
- Android
website: https://centscheck.com/
---
