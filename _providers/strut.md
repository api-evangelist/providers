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
  band: human-only
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
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/strut/plans/strut-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/strut-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/strut/changelog/strut-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/strut-changelog.yml
- group: agent
  href: https://artifacts.apis.io/strut/llms/strut-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/strut-llms.txt
- group: other
  href: https://artifacts.apis.io/strut/hosts/strut-hosts.yml
  title: ''
  type: Hosts
  url: hosts/strut-hosts.yml
- group: other
  href: https://artifacts.apis.io/strut/vendors/strut-vendors.yml
  title: ''
  type: Vendors
  url: vendors/strut-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://strut.so/terms
- group: start
  title: ''
  type: SignUp
  url: https://strut.so/auth/register
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://strut.so/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://strut.so/pricing
- group: operate
  title: ''
  type: ChangeLog
  url: https://strut.so/changelog
- group: company
  title: ''
  type: Blog
  url: https://strut.so/blog
- group: auth
  href: https://artifacts.apis.io/strut/security/strut-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/strut-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://strut.so
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://strut.so
  reason: no-developer-program
  state: none
created: '2026-10-24'
description: Strut is an AI‑powered workspace and notebook that helps users create, expand, and organize long‑form content such as essays, articles, reports, and manuscripts. It offers a free tier with daily AI token limits and a Pro plan that removes limits. The platform provides features like AI‑assisted drafting, note organization, and export options, positioning itself as a collaborative writing environment for creators and professionals.
image: https://strut.so/static/images/strut-hero.webp
layout: provider
modified: '2026-10-24'
name: Strut
nav: Providers
network: true
overview: 'Strut is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Writing, Workspace, Notebooks, and Long-form.


  Strut''s developer surface includes changelog, signup flow, pricing, engineering blog, and 9 more developer resources.'
plans:
- name: Strut Plans Pricing
  plan_count: 2
  slug: strut-plans-pricing
random_paper: 2
score:
  band: emerging
  composite: 14.6
  coverage:
    artifact_dirs: 12
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.3
  facets:
    access_clarity: 43.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 55.4
    operational_transparency: 7.9
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 20.9
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/strut/strut-2026-11-03T143940.png
security:
- kind: domain-security
  name: Strut Domain Security
  slug: strut-domain-security
  summary_line: TLSv1.3
slug: strut
tags:
- Artificial Intelligence
- Writing
- Workspace
- Notebooks
- Long-form
website: https://strut.so
---
