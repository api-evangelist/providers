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
api_count: 1
apis:
- description: Provides access to vintage wine data and tasting notes.
  name: Bordeaux Guru API
  slug: bordeaux-guru-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/bordeaux-guru/plans/bordeaux-guru-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bordeaux-guru-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/bordeaux-guru/llms/bordeaux-guru-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bordeaux-guru-llms.txt
- group: agent
  href: https://artifacts.apis.io/bordeaux-guru/well-known/bordeaux-guru-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bordeaux-guru-well-known.yml
- group: other
  href: https://artifacts.apis.io/bordeaux-guru/hosts/bordeaux-guru-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bordeaux-guru-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bordeaux.guru/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bordeaux.guru/privacy/
- group: commercial
  title: ''
  type: Pricing
  url: https://bordeaux.guru/pricing/
- group: start
  title: ''
  type: Login
  url: https://bordeaux.guru/signin/
- group: auth
  href: https://artifacts.apis.io/bordeaux-guru/security/bordeaux-guru-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bordeaux-guru-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bordeaux.guru/
coverage:
  checked: '2026-11-03'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found on the provider's hosts.
  evidence:
  - status: 0
    url: https://api.bordeaux.guru/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: 'Independent Bordeaux vintage intelligence: en primeur tasting notes written first‑hand at the barrel, daily growing‑season climate for every appellation, and terroir mapped down to the parcel. We publish only what we tasted or measured ourselves — no third‑party scores.'
image: https://bordeaux.guru/og-image.jpg
layout: provider
modified: '2026-11-02'
name: bordeaux.guru
nav: Providers
network: true
overview: 'bordeaux.guru is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Wine, Vintage, En Primeur, Data, and Analytics.


  bordeaux.guru''s developer surface includes pricing and 9 more developer resources.'
plans:
- name: Bordeaux Guru Plans Pricing
  plan_count: 2
  slug: bordeaux-guru-plans-pricing
random_paper: 10
score:
  band: emerging
  composite: 13.6
  coverage:
    artifact_dirs: 8
    catalog_earned: 40.0
    catalog_earned_first_party: 8.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 43.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.1
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
  name: Bordeaux Guru Domain Security
  slug: bordeaux-guru-domain-security
  summary_line: TLSv1.2 · DNSSEC · DMARC
slug: bordeaux-guru
tags:
- Wine
- Vintage
- En Primeur
- Data
- Analytics
- Company
website: https://bordeaux.guru/
---
