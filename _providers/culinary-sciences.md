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
    agentic_commerce: false
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
  score: 14.4
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/culinary-sciences/well-known/culinary-sciences-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/culinary-sciences-well-known.yml
- group: other
  href: https://artifacts.apis.io/culinary-sciences/hosts/culinary-sciences-hosts.yml
  title: ''
  type: Hosts
  url: hosts/culinary-sciences-hosts.yml
- group: auth
  href: https://artifacts.apis.io/culinary-sciences/security/culinary-sciences-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/culinary-sciences-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.culinarysciencescsi.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.culinarysciencescsi.com/
  - status: 200
    url: https://www.nasdaqprivatemarket.com/
  reason: no-developer-program
  state: none
created: '2026-10-11'
description: Culinary Sciences develops patented rapid-chill and food‑treatment technology for high‑volume food production. Their PrecisionVac platform combines rapid cooling and flavor infusion, delivering up to 5× faster cooling, 25× faster treatment, and significant energy savings. Based in the USA, they serve commercial kitchens and food processors with multi‑capability systems.
image: https://www.culinarysciencescsi.com/wp-content/uploads/2026/07/csithumbnail.png
layout: provider
modified: '2026-10-11'
name: Culinary Sciences
nav: Providers
network: true
overview: Culinary Sciences is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Food Tech, RapidChill, Food Processing, USA, and Startups.
random_paper: 9
score:
  band: minimal
  composite: 4.3
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 4.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/culinary-sciences/culinary-sciences-2026-11-03T125759.png
security:
- kind: domain-security
  name: Culinary Sciences Domain Security
  slug: culinary-sciences-domain-security
  summary_line: TLSv1.3
slug: culinary-sciences
tags:
- Food Tech
- RapidChill
- Food Processing
- USA
- Startups
website: https://www.culinarysciencescsi.com/
---
