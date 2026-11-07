---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
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
  score: 8.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Paint colour data, matching, pricing, palettes, trends and rankings.
  name: All Paint Colours API
  slug: all-paint-colours-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/allpaintcolours-co-uk/plans/allpaintcolours-co-uk-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/allpaintcolours-co-uk-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/allpaintcolours-co-uk/authentication/allpaintcolours-co-uk-authentication.yml
  title: ''
  type: Authentication
  url: authentication/allpaintcolours-co-uk-authentication.yml
- group: design
  href: https://artifacts.apis.io/allpaintcolours-co-uk/conformance/allpaintcolours-co-uk-conformance.yml
  title: ''
  type: Conformance
  url: conformance/allpaintcolours-co-uk-conformance.yml
- group: agent
  href: https://artifacts.apis.io/allpaintcolours-co-uk/llms/allpaintcolours-co-uk-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/allpaintcolours-co-uk-llms.txt
- group: other
  href: https://artifacts.apis.io/allpaintcolours-co-uk/hosts/allpaintcolours-co-uk-hosts.yml
  title: ''
  type: Hosts
  url: hosts/allpaintcolours-co-uk-hosts.yml
- group: other
  href: https://artifacts.apis.io/allpaintcolours-co-uk/vendors/allpaintcolours-co-uk-vendors.yml
  title: ''
  type: Vendors
  url: vendors/allpaintcolours-co-uk-vendors.yml
- group: auth
  href: https://artifacts.apis.io/allpaintcolours-co-uk/security/allpaintcolours-co-uk-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/allpaintcolours-co-uk-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://allpaintcolours.co.uk/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://allpaintcolours.co.uk/developers/
- group: docs
  title: ''
  type: Documentation
  url: https://allpaintcolours.co.uk/api/v2/docs
- group: docs
  title: ''
  type: APIReference
  url: https://allpaintcolours.co.uk/api/v2/openapi.json
- group: commercial
  title: ''
  type: Pricing
  url: https://allpaintcolours.co.uk/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://allpaintcolours.co.uk/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://allpaintcolours.co.uk/privacy/
created: '2026-11-01'
description: All Paint Colours provides a searchable database of every paint colour from major UK manufacturers, offering cross‑brand colour matching using CIEDE2000. The site helps users compare shades, plan renovations, and integrates with AI tools like Claude and ChatGPT to suggest matching paints and cost estimates. It is free to try and includes a developer portal for API access.
image: https://allpaintcolours.co.uk/og/default.png
layout: provider
modified: '2026-11-01'
name: All Paint Colours
nav: Providers
network: true
overview: 'All Paint Colours is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Paint, Colour, United Kingdom, and Home Renovation.


  All Paint Colours'' developer surface includes authentication, documentation, API reference, pricing, and 10 more developer resources.'
plans:
- name: Allpaintcolours Co Uk Plans Pricing
  plan_count: 3
  slug: allpaintcolours-co-uk-plans-pricing
random_paper: 16
score:
  band: emerging
  composite: 21.6
  coverage:
    artifact_dirs: 12
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.2
  facets:
    access_clarity: 47.4
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 25.0
    discoverability: 57.1
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-kingdom
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - united-kingdom-ireland
  previous_composite: 28.8
  provenance:
    conformance: derived
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Allpaintcolours Co Uk Authentication
  slug: allpaintcolours-co-uk-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Allpaintcolours Co Uk Domain Security
  slug: allpaintcolours-co-uk-domain-security
  summary_line: TLSv1.3 · DMARC
slug: allpaintcolours-co-uk
tags:
- Paint
- Colour
- United Kingdom
- Home Renovation
website: https://allpaintcolours.co.uk/
---
