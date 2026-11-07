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
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/apmzoom-com/llms/apmzoom-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/apmzoom-com-llms.txt
- group: other
  href: https://artifacts.apis.io/apmzoom-com/hosts/apmzoom-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/apmzoom-com-hosts.yml
- group: company
  title: ''
  type: Website
  url: https://apmzoom.com/
- group: auth
  href: https://artifacts.apis.io/apmzoom-com/security/apmzoom-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/apmzoom-com-domain-security.yml
coverage:
  checked: '2026-11-01'
  detail: The company operates a fashion wholesale marketplace with no public developer program or API.
  evidence:
  - status: 200
    url: https://apmzoom.com/
  reason: not-a-software-company
  state: none
created: '2026-11-01'
description: apM Group (apM Korea) is a Korean fashion wholesale conglomerate operating since 1999 in Seoul's Dongdaemun district. It runs three wholesale malls—apM, apM Luxe, and apM Place—hosting over 1,000 women's and men's apparel stalls. The company offers an AI-powered service, apMZoomAI, allowing overseas buyers to search for products, place orders, and have items collected, packaged, and shipped internationally. While primarily a physical wholesale marketplace, the group maintains an online presence to facilitate global trade.
image: https://apmzoom.com/img/og.jpg
layout: provider
modified: '2026-11-01'
name: apM Group
nav: Providers
network: true
overview: apM Group is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fashion, Wholesale, South Korea, and Marketplace.
random_paper: 7
score:
  band: minimal
  composite: 3.4
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
    - south-korea
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - japan-korea
  previous_composite: 3.4
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Apmzoom Com Domain Security
  slug: apmzoom-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: apmzoom-com
tags:
- Company
- Fashion
- Wholesale
- South Korea
- Marketplace
- Artificial Intelligence
website: https://apmzoom.com/
---
