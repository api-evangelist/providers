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
    dynamic_client_registration: true
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
  score: 18.7
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/achriom-com/plans/achriom-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/achriom-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/achriom-com/llms/achriom-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/achriom-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/achriom-com/well-known/achriom-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/achriom-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/achriom-com/hosts/achriom-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/achriom-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/achriom-com/vendors/achriom-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/achriom-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.achriom.com/terms/
- group: operate
  title: ''
  type: Support
  url: https://www.achriom.com/help/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.achriom.com/privacy/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.achriom.com/pricing/
- group: start
  title: ''
  type: Login
  url: https://www.achriom.com/login
- group: company
  title: ''
  type: Blog
  url: https://www.achriom.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/achriom
- group: auth
  href: https://artifacts.apis.io/achriom-com/security/achriom-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/achriom-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.achriom.com/
coverage:
  checked: '2026-10-31'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract found on the API host.
  evidence:
  - status: 404
    url: https://api.achriom.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: Achriom provides a unified platform to track books, movies, TV shows, music, anime, games, and podcasts. Users can create personal libraries, discover new content, and see connections between media they love. The service offers detailed metadata, recommendations, and the ability to share collections with friends, aiming to be a one‑stop hub for entertainment enthusiasts.
image: https://api.achriom.com/public/og/default/home.jpg?v=o5o1n4
layout: provider
modified: '2026-10-31'
name: Achriom
nav: Providers
network: true
overview: 'Achriom is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Media, Entertainment, Library, Discovery, and Community.


  Achriom''s developer surface includes support, pricing, engineering blog, and 11 more developer resources.'
plans:
- name: Achriom Com Plans Pricing
  plan_count: 2
  slug: achriom-com-plans-pricing
random_paper: 23
score:
  band: emerging
  composite: 14.2
  coverage:
    artifact_dirs: 8
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.1
  facets:
    access_clarity: 43.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 3.6
    discoverability: 48.2
    operational_transparency: 2.6
  previous_composite: 20.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Achriom Com Domain Security
  slug: achriom-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: achriom-com
tags:
- Media
- Entertainment
- Library
- Discovery
- Community
website: https://www.achriom.com/
---
