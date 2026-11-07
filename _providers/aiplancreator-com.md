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
  score: 21.8
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/aiplancreator-com/plans/aiplancreator-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aiplancreator-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/aiplancreator-com/llms/aiplancreator-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aiplancreator-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/aiplancreator-com/well-known/aiplancreator-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aiplancreator-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/aiplancreator-com/hosts/aiplancreator-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aiplancreator-com-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aiplancreator.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aiplancreator.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://aiplancreator.com/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://aiplancreator.com/press
- group: start
  title: ''
  type: Login
  url: https://aiplancreator.com/login
- group: docs
  title: ''
  type: Documentation
  url: https://aiplancreator.com/journal/category/guides
- group: auth
  href: https://artifacts.apis.io/aiplancreator-com/security/aiplancreator-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aiplancreator-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aiplancreator.com/
coverage:
  checked: '2026-11-01'
  detail: The provider's documentation pages are rendered via JavaScript, preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: https://aiplancreator.com/journal/category/guides
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-01'
description: AI Plan Creator is a New Zealand‑based browser application that uses AI to generate floor plans, 3D models, interior designs, landscaping and walkthroughs for homes and buildings. Users describe their idea in natural language and the platform creates detailed plans, renders 3D visualisations, and offers design tools. The service launched as PlotPilot in 2023 and rebranded in October 2026, providing free starter access with optional premium plans for advanced features.
image: https://aiplancreator.com/opengraph-image.png?opengraph-image.0j1j6isbu77f1.png
layout: provider
modified: '2026-11-01'
name: AI Plan Creator
nav: Providers
network: true
overview: 'AI Plan Creator is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Design, Architecture, 3D, and New Zealand.


  AI Plan Creator''s developer surface includes pricing, documentation, and 10 more developer resources.'
plans:
- name: Aiplancreator Com Plans Pricing
  plan_count: 3
  slug: aiplancreator-com-plans-pricing
random_paper: 17
score:
  band: emerging
  composite: 16.6
  coverage:
    artifact_dirs: 8
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.0
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 49.1
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - new-zealand
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - anz
  previous_composite: 22.6
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aiplancreator Com Domain Security
  slug: aiplancreator-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aiplancreator-com
tags:
- Artificial Intelligence
- Design
- Architecture
- 3D
- New Zealand
website: https://aiplancreator.com/
---
