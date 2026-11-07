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
api_count: 1
apis:
- description: API reference for Asha News providing news content and subscription services.
  name: Asha News API
  slug: asha-news-api
artifact_total: 3
common:
- group: agent
  href: https://artifacts.apis.io/asha-news/llms/asha-news-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/asha-news-llms.txt
- group: other
  href: https://artifacts.apis.io/asha-news/hosts/asha-news-hosts.yml
  title: ''
  type: Hosts
  url: hosts/asha-news-hosts.yml
- group: other
  href: https://artifacts.apis.io/asha-news/vendors/asha-news-vendors.yml
  title: ''
  type: Vendors
  url: vendors/asha-news-vendors.yml
- group: start
  title: ''
  type: SignUp
  url: https://asha.news/agents/signup
- group: other
  title: ''
  type: Leadership
  url: https://asha.news/team
- group: auth
  href: https://artifacts.apis.io/asha-news/security/asha-news-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/asha-news-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://asha.news/
- group: docs
  title: ''
  type: Documentation
  url: https://asha.news/about
- group: commercial
  title: ''
  type: TermsOfService
  url: https://asha.news/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://asha.news/privacy
- group: operate
  title: ''
  type: Contact
  url: https://asha.news/contact
- group: commercial
  title: ''
  type: Pricing
  url: https://asha.news/pricing
coverage:
  checked: '2026-11-03'
  detail: Documentation pages are rendered via JavaScript, preventing machine‑readable contract discovery.
  evidence:
  - status: 200
    url: https://asha.news/api
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-01'
description: Asha News is an evidence‑first news organization focused on conflict, particularly the Palestine region. It provides live verified updates, a searchable memorial of victims, directories of journalists, and real‑time monitoring of conflict and finance. All claims are backed by citations and sources, offering transparent, fact‑checked reporting. The platform also offers subscription‑based deeper analysis and AI‑assisted fact‑checking while keeping the core newsroom free to read.
image: https://asha.news/og-image.png
layout: provider
modified: '2026-11-01'
name: Asha News
nav: Providers
network: true
overview: 'Asha News is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include News, Evidence-first, Conflict, Palestine, and Journalism.


  Asha News'' developer surface includes signup flow, documentation, pricing, and 9 more developer resources.'
plans:
- name: Asha News Plans Pricing
  plan_count: 0
  slug: asha-news-plans-pricing
random_paper: 15
score:
  band: minimal
  composite: 10.4
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.1
  facets:
    access_clarity: 22.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 58.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - palestine
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 16.5
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Asha News Domain Security
  slug: asha-news-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: asha-news
tags:
- News
- Evidence-first
- Conflict
- Palestine
- Journalism
website: https://asha.news/
---
