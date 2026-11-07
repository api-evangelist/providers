---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: conformant
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
  score: 23.7
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/marian-coach/plans/marian-coach-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/marian-coach-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/marian-coach/llms/marian-coach-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/marian-coach-llms.txt
- group: other
  href: https://artifacts.apis.io/marian-coach/a2a/marian-coach-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/marian-coach-a2a.yml
- group: agent
  href: https://artifacts.apis.io/marian-coach/well-known/marian-coach-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/marian-coach-well-known.yml
- group: other
  href: https://artifacts.apis.io/marian-coach/hosts/marian-coach-hosts.yml
  title: ''
  type: Hosts
  url: hosts/marian-coach-hosts.yml
- group: other
  href: https://artifacts.apis.io/marian-coach/vendors/marian-coach-vendors.yml
  title: ''
  type: Vendors
  url: vendors/marian-coach-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.marian.coach/privacy-policy/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.marian.coach/pricing/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/marian-kamenistak
- group: company
  title: ''
  type: Blog
  url: https://www.marian.coach/blog/
- group: auth
  href: https://artifacts.apis.io/marian-coach/security/marian-coach-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/marian-coach-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://marian.coach/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://marian.coach/
  reason: no-developer-program
  state: none
created: '2026-10-30'
description: Marian Coach provides engineering leadership mentorship and career coaching services. It helps engineers and technical leaders advance their careers, increase salaries, and secure senior roles through personalized coaching, workshops, and mentorship programs. The platform offers tailored guidance for roles such as CTO, VP of Engineering, Engineering Director, Manager, Senior Engineer, and AI leadership, as well as corporate mentorship-in-residence services.
image: https://www.marian.coach/_astro/portrait-laptop-smile.D82UYdFF_1BjCCq.jpg
layout: provider
modified: '2026-10-30'
name: marian-coach
nav: Providers
network: true
overview: 'marian-coach is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Mentorship, Engineering Leadership, Career Coaching, and Technical Coaching.


  marian-coach''s developer surface includes pricing, engineering blog, and 10 more developer resources.'
plans:
- name: Marian Coach Plans Pricing
  plan_count: 3
  slug: marian-coach-plans-pricing
random_paper: 11
score:
  band: emerging
  composite: 14.3
  coverage:
    artifact_dirs: 12
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.0
  facets:
    access_clarity: 42.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 55.4
    operational_transparency: 2.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 17.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/marian-coach/marian-coach-2026-11-03T135328.png
security:
- kind: domain-security
  name: Marian Coach Domain Security
  slug: marian-coach-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: marian-coach
tags:
- Company
- Mentorship
- Engineering Leadership
- Career Coaching
- Technical Coaching
website: https://marian.coach/
---
