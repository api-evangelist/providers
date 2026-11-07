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
    agent_card: flavored
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
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
  score: 18.9
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: auth
  href: https://artifacts.apis.io/auriniaxo-com/security/auriniaxo-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/auriniaxo-com-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/auriniaxo-com/llms/auriniaxo-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/auriniaxo-com-llms.txt
- group: other
  href: https://artifacts.apis.io/auriniaxo-com/a2a/auriniaxo-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/auriniaxo-com-a2a.yml
- group: auth
  href: https://artifacts.apis.io/auriniaxo-com/well-known/auriniaxo-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/auriniaxo-com-security.txt
- group: agent
  href: https://artifacts.apis.io/auriniaxo-com/well-known/auriniaxo-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/auriniaxo-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/auriniaxo-com/hosts/auriniaxo-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/auriniaxo-com-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://auriniaxo.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://auriniaxo.com/privacy
- group: start
  title: ''
  type: Login
  url: https://auriniaxo.com/login
- group: auth
  href: https://artifacts.apis.io/auriniaxo-com/security/auriniaxo-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/auriniaxo-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/auriniaxo-com/security/auriniaxo-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/auriniaxo-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://auriniaxo.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://auriniaxo.com/
  reason: no-developer-program
  state: none
created: '2026-11-02'
description: Aurinia XO Hostel is an affordable accommodation located in the centre of Kamianets‑Podilskyi, Ukraine. It offers budget dormitory beds, Wi‑Fi, a kitchen and 24/7 self‑check‑in, catering to backpackers and travelers seeking convenient city‑center lodging near the historic old town.
image: https://auriniaxo.com/hostel/og-cover.webp
layout: provider
modified: '2026-11-02'
name: AURINIA XO HOSTEL
nav: Providers
network: true
overview: AURINIA XO HOSTEL is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Hostel, Accommodation, Ukraine, Budget Travel, and Kamianets-Podilskyi.
random_paper: 20
score:
  band: minimal
  composite: 10.6
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.0
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 10.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - ukraine
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - cee
    - europe
  previous_composite: 14.6
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Auriniaxo Com Domain Security
  slug: auriniaxo-com-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Auriniaxo Com Vulnerability Disclosure
  slug: auriniaxo-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: auriniaxo-com
tags:
- Hostel
- Accommodation
- Ukraine
- Budget Travel
- Kamianets-Podilskyi
website: https://auriniaxo.com/
---
