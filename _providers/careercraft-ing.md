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
    mcp_server: documented
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
  score: 3.1
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/careercraft-ing/llms/careercraft-ing-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/careercraft-ing-llms.txt
- group: other
  href: https://artifacts.apis.io/careercraft-ing/hosts/careercraft-ing-hosts.yml
  title: ''
  type: Hosts
  url: hosts/careercraft-ing-hosts.yml
- group: other
  href: https://artifacts.apis.io/careercraft-ing/vendors/careercraft-ing-vendors.yml
  title: ''
  type: Vendors
  url: vendors/careercraft-ing-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://careercraft.ing/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://careercraft.ing/privacy
- group: start
  title: ''
  type: Login
  url: https://app.careercraft.ing/auth/login
- group: company
  title: ''
  type: Blog
  url: https://careercraft.ing/blog
- group: auth
  href: https://artifacts.apis.io/careercraft-ing/security/careercraft-ing-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/careercraft-ing-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://careercraft.ing/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://careercraft.ing/
  reason: no-developer-program
  state: none
created: '2026-11-03'
description: careercraft.ing helps engineers capture work wins, structure impact, and turn forgotten contributions into review-ready career evidence. It provides a platform to document invisible work, quantify impact, and own career history, offering tools for career growth and employer verification.
image: https://careercraft.ing/images/social/og-default.png
layout: provider
modified: '2026-11-03'
name: Careercraft
nav: Providers
network: true
overview: 'Careercraft is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Careers, Engineering, Portfolio, Impact, and Software-as-a-Service.


  Careercraft''s developer surface includes engineering blog and 8 more developer resources.'
random_paper: 5
score:
  band: minimal
  composite: 7.7
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Careercraft Ing Domain Security
  slug: careercraft-ing-domain-security
  summary_line: TLSv1.3
slug: careercraft-ing
tags:
- Careers
- Engineering
- Portfolio
- Impact
- Software-as-a-Service
website: https://careercraft.ing/
---
