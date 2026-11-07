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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 10.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Disco provides event management and audience engagement APIs as described on their developer pages.
  name: Disco API
  slug: disco-api
artifact_total: 4
common:
- group: start
  title: ''
  type: SignUp
  url: https://app.disco.co/sign-up
- group: commercial
  href: https://artifacts.apis.io/justdisco-com/plans/justdisco-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/justdisco-com-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/justdisco-com/changelog/justdisco-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/justdisco-com-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.disco.co/security
- group: agent
  href: https://artifacts.apis.io/justdisco-com/llms/justdisco-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/justdisco-com-llms.txt
- group: other
  href: https://artifacts.apis.io/justdisco-com/a2a/justdisco-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/justdisco-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/justdisco-com/well-known/justdisco-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/justdisco-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/justdisco-com/hosts/justdisco-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/justdisco-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/justdisco-com/vendors/justdisco-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/justdisco-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://privacy.disco.co/terms-of-service
- group: operate
  title: ''
  type: Support
  url: https://support.disco.co/hc/en-us/requests/new
- group: auth
  title: ''
  type: Security
  url: https://www.disco.co/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.disco.co/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.disco.co/pricing
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.disco.co/changelog
- group: company
  title: ''
  type: Blog
  url: https://www.disco.co/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.disco.co/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://docs.disco.co/
- group: docs
  title: ''
  type: APIReference
  url: https://api.production.services.disco.co/v1/docs
- group: auth
  href: https://artifacts.apis.io/justdisco-com/security/justdisco-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/justdisco-com-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/justdisco-com/security/justdisco-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/justdisco-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.disco.co
- group: company
  title: ''
  type: Website
  url: https://www.disco.co
created: '2026-10-21'
description: Disco is a technology company focused on providing innovative solutions for event management and audience engagement. The platform enables organizers to create interactive experiences, leveraging real-time data and analytics to enhance participant interaction. Backed by prominent investors, Disco aims to transform how events are planned, executed, and measured, offering tools for ticketing, live polling, and immersive digital experiences.
image: https://cdn.prod.website-files.com/60ffdd9e3c66d7e7307eb9e5/6973a96a25fc03586026ee0b_OpenGraph_Social.png
layout: provider
modified: '2026-10-21'
name: Disco
nav: Providers
network: true
overview: 'Disco is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, EventTech, Audience Engagement, Real-Time Analytics, and Ticketing.


  Disco''s developer surface includes signup flow, changelog, support, pricing, engineering blog, getting-started guide, documentation, and 16 more developer resources.'
plans:
- name: Justdisco Com Plans Pricing
  plan_count: 2
  slug: justdisco-com-plans-pricing
random_paper: 4
score:
  band: emerging
  composite: 24.5
  coverage:
    artifact_dirs: 11
    catalog_earned: 40.0
    catalog_earned_first_party: 8.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.6
  facets:
    access_clarity: 61.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 17.9
    discoverability: 64.3
    operational_transparency: 13.2
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 32.1
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/justdisco-com/justdisco-com-2026-11-03T134255.png
security:
- kind: domain-security
  name: Justdisco Com Domain Security
  slug: justdisco-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Justdisco Com Trust Center
  slug: justdisco-com-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: justdisco-com
tags:
- Company
- EventTech
- Audience Engagement
- Real-Time Analytics
- Ticketing
website: https://www.disco.co
---
