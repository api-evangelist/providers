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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: platform
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
  score: 15.3
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/charity-miles/llms/charity-miles-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/charity-miles-llms.txt
- group: agent
  href: https://artifacts.apis.io/charity-miles/well-known/charity-miles-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/charity-miles-well-known.yml
- group: other
  href: https://artifacts.apis.io/charity-miles/hosts/charity-miles-hosts.yml
  title: ''
  type: Hosts
  url: hosts/charity-miles-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://charitymiles.org/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://charitymiles.org/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://charitymiles.org/press/
- group: start
  title: ''
  type: Login
  url: https://charitymiles.org/login/
- group: company
  title: ''
  type: Blog
  url: https://charitymiles.org/blog/
- group: auth
  href: https://artifacts.apis.io/charity-miles/security/charity-miles-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/charity-miles-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://charitymiles.org/
created: '2026-10-27'
description: Charity Miles is a mobile fitness app that lets users earn money for charity by walking, running, or biking. Participants track their activity, and the app donates a pledged amount per mile to a selected nonprofit. It partners with corporate sponsors and offers a platform for charities to engage supporters through physical activity, providing impact metrics and fundraising tools.
image: https://charitymiles.org/wp-content/uploads/2023/07/BeTheChange-High-Res1-min.webp
layout: provider
modified: '2026-10-27'
name: Charity Miles
nav: Providers
network: true
overview: 'Charity Miles is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fitness, Charity, Mobile App, and Health.


  Charity Miles'' developer surface includes engineering blog and 9 more developer resources.'
random_paper: 19
score:
  band: minimal
  composite: 9.4
  coverage:
    artifact_dirs: 10
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.2
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 56.3
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 13.6
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 12.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/charity-miles/charity-miles-2026-11-03T123903.png
security:
- kind: domain-security
  name: Charity Miles Domain Security
  slug: charity-miles-domain-security
  summary_line: TLSv1.2 · DMARC
slug: charity-miles
tags:
- Company
- Fitness
- Charity
- Mobile App
- Health
website: https://charitymiles.org/
---
