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
  href: https://artifacts.apis.io/centre-for-sight/plans/centre-for-sight-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/centre-for-sight-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/centre-for-sight/llms/centre-for-sight-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/centre-for-sight-llms.txt
- group: agent
  href: https://artifacts.apis.io/centre-for-sight/well-known/centre-for-sight-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/centre-for-sight-well-known.yml
- group: other
  href: https://artifacts.apis.io/centre-for-sight/hosts/centre-for-sight-hosts.yml
  title: ''
  type: Hosts
  url: hosts/centre-for-sight-hosts.yml
- group: other
  href: https://artifacts.apis.io/centre-for-sight/vendors/centre-for-sight-vendors.yml
  title: ''
  type: Vendors
  url: vendors/centre-for-sight-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.centreforsight.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.centreforsight.com/privacy-policy/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.centreforsight.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://www.centreforsight.com/blog/
- group: auth
  href: https://artifacts.apis.io/centre-for-sight/security/centre-for-sight-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/centre-for-sight-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.centreforsight.com
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://www.centreforsight.com/mcp
  - status: 200
    url: https://www.centreforsight.com
  - status: 200
    url: https://www.nasdaqprivatemarket.com/
  reason: partner-login
  state: gated
created: '2026-10-07'
description: Centre For Sight is a UK‑based private eye‑care provider offering premium laser eye surgery, cataract surgery, glaucoma treatments and a wide range of ophthalmology services across multiple locations. Established in 1996, it operates over 95 centres in the UK and internationally, delivering advanced technology and specialist care to patients. The organisation also runs a charitable trust supporting eye health initiatives.
layout: provider
modified: '2026-10-07'
name: Centre for Sight
nav: Providers
network: true
overview: 'Centre for Sight is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare, Ophthalmology, Eye Care, Medical, and United Kingdom.


  Centre for Sight''s developer surface includes pricing, engineering blog, and 9 more developer resources.'
plans:
- name: Centre For Sight Plans Pricing
  plan_count: 17
  slug: centre-for-sight-plans-pricing
random_paper: 17
score:
  band: emerging
  composite: 15.7
  coverage:
    artifact_dirs: 10
    catalog_earned: 37.0
    catalog_earned_first_party: 12.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.8
  facets:
    access_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 58.9
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-kingdom
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - united-kingdom-ireland
  previous_composite: 19.5
  provenance:
    mcp: derived
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
screenshot: https://apis.io/screenshots/centre-for-sight/centre-for-sight-2026-11-03T123654.png
security:
- kind: domain-security
  name: Centre For Sight Domain Security
  slug: centre-for-sight-domain-security
  summary_line: TLSv1.3 · DMARC
slug: centre-for-sight
tags:
- Healthcare
- Ophthalmology
- Eye Care
- Medical
- United Kingdom
website: https://www.centreforsight.com
---
