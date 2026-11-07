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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: The Castos API allows managing podcasts, episodes, and private subscribers.
  name: Castos API
  slug: castos-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/castos/plans/castos-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/castos-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/castos/llms/castos-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/castos-llms.txt
- group: agent
  href: https://artifacts.apis.io/castos/well-known/castos-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/castos-well-known.yml
- group: other
  href: https://artifacts.apis.io/castos/hosts/castos-hosts.yml
  title: ''
  type: Hosts
  url: hosts/castos-hosts.yml
- group: other
  href: https://artifacts.apis.io/castos/vendors/castos-vendors.yml
  title: ''
  type: Vendors
  url: vendors/castos-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.castos.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.castos.com/terms
- group: operate
  title: ''
  type: StatusPage
  url: https://status.castos.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://castos.com/privacy/
- group: company
  title: ''
  type: Newsroom
  url: https://castos.com/press/
- group: start
  title: ''
  type: Login
  url: https://app.castos.com/login
- group: auth
  href: https://artifacts.apis.io/castos/security/castos-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/castos-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://castos.com/
- group: docs
  title: ''
  type: Documentation
  url: https://app.castos.com/docs/api/index.html
- group: docs
  title: ''
  type: APIReference
  url: https://app.castos.com/docs/api/swagger.yaml
- group: company
  title: ''
  type: Blog
  url: https://castos.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://castos.com/pricing/
- group: operate
  title: ''
  type: Support
  url: https://castos.com/support/
- group: start
  title: ''
  type: GettingStarted
  url: https://castos.com/how-to-start-a-podcast/
created: '2026-10-28'
description: Castos provides podcast hosting and publishing services, offering tools for creators to launch, grow, and monetize their shows. Their platform includes podcast hosting, hybrid and private podcasting solutions, YouTube republishing, analytics, customizable websites, transcription, AI assistance, and mobile apps. Castos serves businesses, agencies, churches, universities, and nonprofits, with features like commerce, advertising, and enterprise solutions.
image: https://images-cdn.castos.com/2026/10/castos-default-og.webp
layout: provider
modified: '2026-10-28'
name: Castos
nav: Providers
network: true
overview: 'Castos is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Podcasts, Hosting, Media, Analytics, and Enterprise.


  Castos'' developer surface includes documentation, API reference, engineering blog, pricing, support, getting-started guide, and 13 more developer resources.'
plans:
- name: Castos Plans Pricing
  plan_count: 4
  slug: castos-plans-pricing
random_paper: 5
score:
  band: emerging
  composite: 23.2
  coverage:
    artifact_dirs: 12
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.9
  facets:
    access_clarity: 57.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 17.9
    discoverability: 74.1
    operational_transparency: 7.9
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 34.1
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/castos/castos-2026-11-03T123459.png
security:
- kind: domain-security
  name: Castos Domain Security
  slug: castos-domain-security
  summary_line: TLSv1.3 · DMARC
slug: castos
tags:
- Podcasts
- Hosting
- Media
- Analytics
- Enterprise
website: https://castos.com/
---
