---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/join-jump-com/llms/join-jump-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/join-jump-com-llms.txt
- group: other
  href: https://artifacts.apis.io/join-jump-com/hosts/join-jump-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/join-jump-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/join-jump-com/vendors/join-jump-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/join-jump-com-vendors.yml
- group: start
  title: ''
  type: SignUp
  url: https://app.join-jump.com/sign-up
- group: commercial
  title: ''
  type: Pricing
  url: https://www.join-jump.com/en/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.join-jump.com/blog
- group: auth
  href: https://artifacts.apis.io/join-jump-com/security/join-jump-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/join-jump-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://join-jump.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: http://join-jump.com
  reason: no-developer-program
  state: none
created: '2026-10-25'
description: 'Jump is a company surfaced via the API Evangelist harvest backlog (source: vc-portfolio; backed by index-ventures) and added to the network as a stub for full-pipeline profiling.'
image: https://images.prismic.io/join-jump/IQr9FdFl969RZyfX_jump-portage.jpg?auto=format,compress&rect=0,0,2400,1260&w=2400&h=1260
layout: provider
modified: '2026-10-25'
name: Jump
nav: Providers
network: true
overview: 'Jump is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Portage Salarial, Freelance, and Consulting.


  Jump''s developer surface includes signup flow, pricing, engineering blog, and 5 more developer resources.'
random_paper: 13
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 10
    catalog_earned: 17.0
    catalog_earned_first_party: 0.0
    catalog_gap: 98.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.6
  facets:
    access_clarity: 11.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 37.5
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 7.6
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/join-jump-com/join-jump-com-2026-11-03T134203.png
security:
- kind: domain-security
  name: Join Jump Com Domain Security
  slug: join-jump-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: join-jump-com
tags:
- Portage Salarial
- Freelance
- Consulting
website: http://join-jump.com
---
